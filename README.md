# Playback Dial

See how far into a film or audio file you are without opening VLC’s controls over the picture. Leave the remaining time on the desk during a screening or a listening session.

## Setup

In desktop VLC, switch Preferences to **All**, open **Interface → Main interfaces** and enable **Web**. Under **Main interfaces → Lua**, set the Lua HTTP password. Save and restart VLC. Open a media file. Put the password in the `VLC_PASSWORD` environment variable on the companion computer. The example connects to `http://127.0.0.1:8080`. Change `url` only if VLC uses a different address or port.

From the repository root, copy the example and start the companion with Python 3.10 or newer.

```sh
cp companion/example.json config.json
# Edit config.json for your source before starting the server.
python3 companion/serve.py --config config.json
```

In the emulator, run `~/.busy-emulator/bin/busy-emulator allow-local 8770` and approve that port. Open **Apps → Playback Dial → Setup**, set **Local companion URL** to `http://127.0.0.1:8770/reading`, save, then reopen the app. For a physical bar, start the companion with `--host YOUR_LAN_IP` and replace `127.0.0.1` with that address. Bind only to your trusted network. Open `/reading` on the host to inspect the current reading. Keep credentials in the host environment.

## Read the playhead

Start a file in VLC. ELAPSED follows its playhead and stops advancing when playback pauses. Turn the wheel to REMAINING. At 24:12 in a 90-minute film, 1:05:48 is left.

![The example switches from elapsed time to 1:05:48 remaining.](media/guide/use-1.gif)

## Keep the ending time in view

Press Start on REMAINING to pin it. Seek in VLC and click to refresh. Press Start again to unpin, then turn back to ELAPSED. A stream without a known duration reads Live on the remaining-time page.

![The wheel returns from time remaining to the current playhead.](media/guide/use-2.gif)

## Run in the emulator

Install BUSY Bar Emulator and open it. From this repository run the following command, then press **Back** when you finish.

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

The recordings use example responses on emulator firmware. Each display pixel is enlarged to a 9 × 9 square.

[VLC HTTP interface](https://wiki.videolan.org/VLC_HTTP_requests/).

[Rear display](screenshots/back-1.png) · [MIT license](LICENSE)
