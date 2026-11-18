"""Read elapsed and remaining playback time from VLC's local web interface."""
import base64,os,json
from urllib.request import urlopen,Request
from serve import page
INTERVAL=1
def clock(t):
    h,s=divmod(t,3600);m,s=divmod(s,60);return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"
def snapshot(o,m):
    auth=base64.b64encode((":"+os.environ["VLC_PASSWORD"]).encode()).decode()
    with urlopen(Request(o.get("url","http://127.0.0.1:8080")+"/requests/status.json",headers={"Authorization":"Basic "+auth}),timeout=4) as r:d=json.load(r)
    state=d.get("state","stopped")
    if state=="stopped":return dict(state="VLC stopped",key=state,pages=[page("PLAYER","Stopped","Open a file in VLC")])
    t=max(0,int(d["time"]));n=int(d.get("length",0));title=d.get("information",{}).get("category",{}).get("meta",{}).get("title") or "Current media"
    return dict(state=state.capitalize(),key=state,pages=[page("ELAPSED",clock(t),title,state),page("REMAINING",clock(max(0,n-t)) if n>0 else "Live",title,"Unknown duration" if n<=0 else "Total "+clock(n))])
