import sys

USAGE = "Usage: python identify.py <file>"

def literally_end(msg):
    print("========= error =========")
    print(msg)
    exit(1)

def main():
    if len(sys.argv) < 2:
        literally_end(USAGE)
        
    try:
        with open(sys.argv[1], 'rb') as file:
            magic = file.read(12)
            prnt = 'identified file as '
            if magic[:4] == b'RIFF' and magic[8:12] == b'WAVE':
                prnt += 'WAVE'
            elif magic[0] == 0xff and (magic[1] == 0xfb or magic[1] == 0xf3 or magic[1] == 0xf2) or magic[:3] == b'ID3':
                prnt += 'mp3'
            elif magic[:4] == 'fLaC':
                prnt += 'flac'
            elif magic[:4] == 'ftyp':
                prnt += 'mp4'
            
            if len(prnt) != len('identified file as '):
                print(prnt)
                return
            
            literally_end('idk your file type :(')
        
    except IOError:
        literally_end("Couldn't open file: " + sys.argv[1])
    
if __name__ == '__main__':
    main()