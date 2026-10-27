import subprocess,sys,json,os
# shots: id src start dur ycrop
cfg=json.load(open(sys.argv[1]));out=sys.argv[2];os.makedirs('sh',exist_ok=True)
SL=1.25;XF=0.5
def run(a):subprocess.run(a,check=True)
parts=[]
for s in cfg:
  i=s['id'];raw=f'sh/{i}-raw.mp4';trf=f'sh/{i}.trf';st=f'sh/{i}.mp4'
  run(['ffmpeg','-v','error','-y','-ss',str(s['t']),'-t',str(s['d']),'-i',f"hd/{s['src']}.mp4",'-an','-c:v','libx264','-crf','12','-preset','fast',raw])
  run(['ffmpeg','-v','error','-y','-i',raw,'-vf',f'vidstabdetect=shakiness=6:accuracy=15:result={trf}','-f','null','-'])
  y=s.get('y',285);z=s.get('zoom',1.0)
  vf=(f"vidstabtransform=input={trf}:smoothing=30:zoom=4:optzoom=0,unsharp=5:5:0.4,"
      f"crop=1080:1350:0:{y},"+(f"scale={int(1080*z)}:{int(1350*z)},crop=1080:1350," if z>1 else "")+
      f"setpts={SL}*PTS,fps=25,eq=contrast=1.04:saturation=0.96:gamma=1.0,colorbalance=rm=0.0:bm=0.0,format=yuv420p")
  run(['ffmpeg','-v','error','-y','-i',raw,'-vf',vf,'-an','-c:v','libx264','-crf','14','-preset','fast',st])
  d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',st]))
  parts.append((st,d))
# xfade chain + loop (append first shot start at the end)
ins=[];fc=[];lab='0:v';acc=parts[0][1]
for k,(p,d) in enumerate(parts):ins+=['-i',p]
ins+=['-i',parts[0][0]]
seq=parts+[parts[0]]
for k in range(1,len(seq)):
  off=acc-XF;nl=f'x{k}';fc.append(f'[{lab}][{k}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[{nl}]');lab=nl;acc=off+seq[k][1]
# cut so the loop ends inside first shot = start of video (loop point seamless): trim to acc-seq[0][1]+XF
total=acc-seq[-1][1]+XF
fc.append(f'[{lab}]trim=start={XF}:end={total+XF:.3f},setpts=PTS-STARTPTS[v]')
run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[v]','-an','-c:v','libx264','-crf','21','-preset','slow','-profile:v','high','-pix_fmt','yuv420p','-movflags','+faststart','-map_metadata','-1',out])
print(out,subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','csv=p=0',out]).decode().strip())
