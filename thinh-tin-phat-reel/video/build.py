from pathlib import Path
import json, html, math, wave, struct

p=Path(__file__).parent
def t(x): return round(.4+x/.84,3)
# Clause boundaries fitted to measured pauses in the supplied recording.
raw=[
(.17,2.8,'Máy giặt còn đầy nước, khoan vội gọi thay bơm nha!'),
(2.98,5.23,'Có khi nguyên nhân đơn giản hơn bạn nghĩ đó!'),
(5.49,8.3,'Đầu tiên, kiểm tra xem máy đã chạy hết chương trình chưa.'),
(8.41,10.25,'Nếu chưa, thử chọn chế độ xả hoặc vắt'),
(10.25,11.95,'theo hướng dẫn của máy.'),
(12.19,14.85,'Tiếp theo, nhớ rút điện rồi kiểm tra ống xả.'),
(14.98,16.9,'Nếu ống bị gập, đè bẹp hoặc tắc nghẽn'),
(16.9,18.75,'thì nước cũng khó thoát ra ngoài.'),
(18.97,21.35,'Nếu thấy ống bị gập thì chỉnh lại cho thông thoáng.'),
(21.48,23.0,'Nhớ đặt ống đúng vị trí và độ cao'),
(23.0,24.95,'theo hướng dẫn của nhà sản xuất nha!'),
(25.21,28.04,'Kiểm tra hai chỗ này trước khi nghĩ tới chuyện thay bơm nha!'),
(28.3,30.2,'Thịnh Tín Phát, thợ điện lạnh nói thật.'),
(30.61,32.85,'Lưu video lại, biết đâu có ngày cần tới!')]
caps=[dict(start=t(a),end=t(b),text=s) for a,b,s in raw]
json.dump(caps,open(p/'captions.json','w'),ensure_ascii=False,indent=2)
def stamp(x):
 ms=round(x*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'captions.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}' for i,c in enumerate(caps))+'\n')
cuts=[0,t(5.23),t(11.95),t(14.85),t(18.75),t(24.95),40]
heads=['MÁY GIẶT KHÔNG XẢ NƯỚC?','1. KIỂM TRA CHẾ ĐỘ','2. KIỂM TRA ỐNG XẢ','2. KIỂM TRA ỐNG XẢ','CHỈNH ỐNG XẢ ĐÚNG CÁCH','THỊNH TÍN PHÁT']
notes=['Khoan vội nghĩ tới thay bơm','Chọn Xả / Vắt theo hướng dẫn máy','Tắt máy · Rút điện bằng tay khô','Tìm đoạn ống bị gập hoặc đè bẹp','Vị trí và độ cao theo nhà sản xuất','THỢ ĐIỆN LẠNH NÓI THẬT']
tiles=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
scenes=''
for i,((col,row),head,note) in enumerate(zip(tiles,heads,notes)):
 a,b=cuts[i:i+2]
 scenes+=f'''<section id="s{i}" class="clip scene" data-start="{a}" data-duration="{b-a}" data-track-index="0"><div class="scene-content"><header><div class="brand">ĐIỆN LẠNH THỊNH TÍN PHÁT</div><h1>{head}</h1><p class="note">{note}</p></header><div class="photo-frame" data-layout-allow-overflow><div id="photo{i}" class="photo" style="background-position:{col*50}% {row*100}%"></div></div><footer>Hướng dẫn kiểm tra tại nhà <span>• Hình minh họa</span></footer></div></section>'''
captions=''.join(f'<div id="c{i}" class="clip caption" data-start="{c["start"]}" data-duration="{c["end"]-c["start"]}" data-track-index="3"><span>{html.escape(c["text"])}</span></div>' for i,c in enumerate(caps))
style='''@font-face{font-family:Be Vietnam Pro;src:url(assets/fonts/package/files/be-vietnam-pro-latin-500-normal.woff2);font-weight:500}@font-face{font-family:Be Vietnam Pro;src:url(assets/fonts/package/files/be-vietnam-pro-vietnamese-500-normal.woff2);font-weight:500;unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}@font-face{font-family:Be Vietnam Pro;src:url(assets/fonts/package/files/be-vietnam-pro-latin-800-normal.woff2);font-weight:800}@font-face{font-family:Be Vietnam Pro;src:url(assets/fonts/package/files/be-vietnam-pro-vietnamese-800-normal.woff2);font-weight:800;unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}*{box-sizing:border-box;margin:0}html,body,#root{width:1080px;height:1920px;overflow:hidden;background:#132B45;font-family:Be Vietnam Pro,sans-serif;color:#fff}.scene{position:absolute;inset:0;background:#132B45}.scene-content{width:100%;height:100%;padding:175px 0 180px;display:flex;flex-direction:column;gap:0}header{height:240px;flex-shrink:0;padding:0 90px}.brand{font-size:27px;font-weight:500;color:#E6BC66;letter-spacing:2px;margin-bottom:22px}h1{font-size:58px;font-weight:800;line-height:1.22;max-width:840px;letter-spacing:-1.3px}.note{font-size:28px;margin-top:16px;color:#fff}.photo-frame{width:1080px;height:1020px;overflow:hidden;background:#F5F2EB;flex-shrink:0}.photo{width:1080px;height:1080px;background-image:url(assets/scenes.png);background-size:300% 200%;transform-origin:center center}footer{padding:20px 90px;font-size:23px;color:#E6BC66}footer span{color:#fff;font-size:21px}.caption{position:absolute;left:90px;top:1510px;width:810px;height:220px;display:flex;align-items:flex-start;justify-content:center;text-align:center;z-index:10;font-size:47px;line-height:1.4;font-weight:500}.caption span{display:block;max-width:810px}'''
anim=''
for i in range(6):
 a,b=cuts[i:i+2]
 anim+=f'tl.fromTo("#photo{i}",{{scale:1}},{{scale:1.045,duration:{b-a},ease:"none",immediateRender:false}},{a});\n'
doc=f'''<!doctype html><html lang="vi"><head><meta charset="UTF-8"><script src="assets/gsap.min.js"></script><style>{style}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="40" data-width="1080" data-height="1920">{scenes}{captions}<audio id="voice" src="assets/voice.wav" data-start="0" data-duration="40" data-track-index="1" data-volume="1"></audio><audio id="music" src="assets/music.wav" data-start="0" data-duration="40" data-track-index="2" data-volume="0.055"></audio></div><script>const tl=gsap.timeline({{paused:true}});{anim}window.__timelines=window.__timelines||{{}};window.__timelines.main=tl;</script></body></html>'''
(p/'index.html').write_text(doc)
# Original soft instrumental bed; no third-party recording.
sr=48000
chords=[[196,246.94,293.66],[164.81,196,246.94],[130.81,164.81,196],[146.83,185,220]]
with wave.open(str(p/'assets/music.wav'),'wb') as f:
 f.setnchannels(1);f.setsampwidth(2);f.setframerate(sr)
 buf=bytearray()
 for n in range(40*sr):
  sec=n/sr; beat=sec%0.6; chord=chords[int(sec//4.8)%4];freq=chord[int(sec//.6)%3]*2
  env=(1-math.exp(-beat*60))*math.exp(-beat*5)
  val=.28*env*(math.sin(2*math.pi*freq*sec)+.15*math.sin(4*math.pi*freq*sec))
  val+=.07*sum(math.sin(2*math.pi*v*sec) for v in chord)/3
  val*=min(1,sec/1.5,(40-sec)/2)
  buf.extend(struct.pack('<h',int(val*32767)))
 f.writeframes(buf)
print('Built 40s composition, 14 caption groups, six photo shots.')
