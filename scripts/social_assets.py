from PIL import Image, ImageDraw, ImageFont
import os, textwrap, subprocess, tempfile, shutil, math

ROOT="assets/social"
os.makedirs(ROOT, exist_ok=True)
W,H=1080,1350
RW,RH=1080,1920

def font(size,bold=False):
    paths=[
      "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
      "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
    ]
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

FB=font(72,True); FM=font(44,True); FS=font(32); FR=font(96,True); FRS=font(48,True)

def gradient(size, top=(11,17,25), bottom=(31,45,58)):
    w,h=size; im=Image.new("RGB",size); d=ImageDraw.Draw(im)
    for y in range(h):
        t=y/max(1,h-1)
        c=tuple(int(top[i]*(1-t)+bottom[i]*t) for i in range(3))
        d.line((0,y,w,y),fill=c)
    return im

def wrap(draw,text,xy,fontobj,fill,maxw,spacing=12):
    x,y=xy; words=text.split(); lines=[]; cur=""
    for w in words:
        test=(cur+" "+w).strip()
        if draw.textbbox((0,0),test,font=fontobj)[2] <= maxw: cur=test
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    for line in lines:
        draw.text((x,y),line,font=fontobj,fill=fill)
        y += fontobj.size+spacing
    return y

def card(filename,kicker,title,hook,sub):
    im=gradient((W,H)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((65,70,W-65,H-70),radius=42,fill=(20,28,37),outline=(188,204,214),width=3)
    d.rectangle((65,70,W-65,86),fill=(255,219,112))
    d.text((105,145),kicker,font=FM,fill=(163,187,204))
    y=wrap(d,title,(105,260),FB,(248,249,250),850)
    y+=65
    y=wrap(d,hook,(105,y),FM,(255,219,112),850)
    y+=55
    wrap(d,sub,(105,y),FS,(196,208,216),830)
    d.text((105,H-185),"TRIPPICK",font=FM,fill=(248,249,250))
    d.text((105,H-120),"Save this before booking",font=FS,fill=(150,169,182))
    im.save(os.path.join(ROOT,filename),quality=88,optimize=True)

cards=[
("rome-colosseum.jpg","ROME","COLOSSEUM TICKETS","30 DAYS? 7 DAYS?","Know the release window before you pay."),
("jfk-manhattan.jpg","NEW YORK","JFK → MANHATTAN","TRAIN OR TAXI?","Group size + luggage can flip the answer."),
("vegas-hotel-fees.jpg","LAS VEGAS","CHEAP HOTEL?","CHECK THE FINAL PRICE","Resort fee + parking can change the deal."),
("statue-liberty.jpg","NEW YORK","STATUE OF LIBERTY","CROWN OR PEDESTAL?","The access level changes the whole visit."),
("louvre.jpg","PARIS","LOUVRE","TOUR OR ENTRY TICKET?","Timing + meeting point matter more than hype."),
("vatican.jpg","ROME","VATICAN","CHEAPEST TOUR?","Check group size + inclusions first."),
("grand-canyon.jpg","LAS VEGAS","GRAND CANYON","WEST OR SOUTH RIM?","Travel time can change your entire day."),
("times-square.jpg","NEW YORK","TIMES SQUARE HOTEL","ROOM RATE ≠ FINAL PRICE","Fees + location + noise decide the real value."),
("rome-fco.jpg","ROME","FCO → CITY","TRAIN OR TAXI?","Bags + group size + hotel location change the answer."),
("final-price.jpg","TRAVEL","FINAL PRICE","HEADLINE ≠ CHECKOUT","Fees + add-ons + cancellation can flip the deal."),
("cancellation.jpg","BOOKING","CANCELLATION TERMS","SAVE THE SCREENSHOT","The exact wording matters when plans change."),
("city-tour.jpg","TOURS","BEFORE YOU BOOK","5 THINGS TO CHECK","Meeting point + group size + transport + cancellation + duration.")
]
for c in cards: card(*c)

def scene(text1,text2,idx):
    im=gradient((RW,RH),(8+idx*2,13+idx*2,20+idx*3),(24+idx*4,38+idx*3,52+idx*2)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((70,120,RW-70,RH-120),radius=48,fill=(18,26,35),outline=(235,235,235),width=3)
    d.rectangle((70,120,RW-70,142),fill=(255,219,112))
    d.text((100,200),"TRIPPICK",font=FRS,fill=(170,193,208))
    y=wrap(d,text1,(100,520),FR,(248,249,250),880,18)
    y+=90
    wrap(d,text2,(100,y),FRS,(255,219,112),850,18)
    d.text((100,RH-250),"SAVE THIS",font=FRS,fill=(248,249,250))
    d.text((100,RH-180),"Link in first comment",font=FS,fill=(160,180,193))
    return im

reels={
"rome-ticket-window.mp4":[("ROME TRIP?","DON'T MISS THE TICKET WINDOW"),("COLOSSEUM","30-DAY + 7-DAY WINDOWS"),("FREE CALCULATOR","LINK IN FIRST COMMENT")],
"vegas-final-price.mp4":[("CHEAP HOTEL?","ROOM RATE IS NOT FINAL COST"),("CHECK","RESORT FEE + PARKING + TAXES"),("SAVE THE CHECKLIST","LINK IN FIRST COMMENT")],
"jfk-transfer.mp4":[("JFK → MANHATTAN","TRAIN OR TAXI?"),("GROUP + BAGS","CAN FLIP THE ANSWER"),("FREE COST TOOL","LINK IN FIRST COMMENT")]
}
for fn,scenes in reels.items():
    td=tempfile.mkdtemp()
    paths=[]
    for i,(a,b) in enumerate(scenes):
        p=os.path.join(td,f"s{i}.png"); scene(a,b,i).save(p); paths.append(p)
    out=os.path.join(ROOT,fn)
    cmd=["ffmpeg","-y"]
    for p in paths: cmd += ["-loop","1","-t","2.7","-i",p]
    filt="[0:v]scale=1080:1920,setsar=1[v0];[1:v]scale=1080:1920,setsar=1[v1];[2:v]scale=1080:1920,setsar=1[v2];[v0][v1][v2]concat=n=3:v=1:a=0,format=yuv420p[v]"
    cmd += ["-filter_complex",filt,"-map","[v]","-r","30","-c:v","libx264","-preset","veryfast","-crf","22","-movflags","+faststart",out]
    subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    shutil.rmtree(td)
print("generated",len(cards),"cards and",len(reels),"reels")
