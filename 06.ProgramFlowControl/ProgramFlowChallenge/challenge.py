inputPrompt = "Please enter an IP Address. An IP address consists of 4 numbers, " \
                  "separated from each other with a full stop: "

ipAddress = input(inputPrompt)

if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segmentLength = 0
# character = ""

for character in ipAddress:
    if character == '.':
        print('Segment {} contains {} characters'. format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

# Unless the final character in the string was a . then we haven't printed the last segment
# if character != '.':
#     print("Segment {} contains {} characters" . format(segment, segmentLength))