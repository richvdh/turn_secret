A quick hack to generate username/password pairs for access to TURN servers,
as per https://tools.ietf.org/html/draft-uberti-behave-turn-rest-00.

It reads the shared secret from coturn's configuration file
(/etc/turnserver.conf), and spits out a username/password pair which
can then be used in TURN clients, or things like
https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/.
