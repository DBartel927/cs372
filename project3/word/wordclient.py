import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def packet_complete(data):
    if len(data) < WORD_LEN_SIZE:
        return False

    word_len = int.from_bytes(data[:WORD_LEN_SIZE], "big")
    if len(data) >= WORD_LEN_SIZE + word_len:
        return True

    return False

def packet_extract(data):
    word_length = int.from_bytes(data[:WORD_LEN_SIZE], "big")
    packet = data[:WORD_LEN_SIZE + word_length]
    remaining = data[WORD_LEN_SIZE + word_length:]
    return (packet, remaining)

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    global packet_buffer

    # TODO -- Write me!
    while not packet_complete(packet_buffer):
        data = s.recv(4096)
        if data == b"":
            return None
        packet_buffer += data

    packet, packet_buffer = packet_extract(packet_buffer)
    return packet


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """

    # TODO -- Write me!
    word = word_packet[WORD_LEN_SIZE:].decode("utf-8")
    return word

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))