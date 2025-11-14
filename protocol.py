#stop-and-wait
n = int(input("Total packets: "))

i = 1
while i <= n:
    print("Sending packet", i)
    ack = input("ACK received? (y/n): ")
    if ack == 'y':
        i += 1
    else:
        print("Resending...")





#go-back-n
ws = int(input("Window size: "))
total = int(input("Total frames: "))

sent = 0
while sent < total:
    for i in range(sent, min(sent+ws, total)):
        print("Sent frame", i)
    ack = int(input("Enter last ACK+1: "))
    sent = ack







#selective-repeat
ws = int(input("Window size: "))
frames = list(map(int, input("Enter frames: ").split()))

i = 0
while i < len(frames):
    print("Sending:", frames[i:i+ws])
    input("Press Enter for ACK...")
    i += ws

print("All frames acknowledged.")
