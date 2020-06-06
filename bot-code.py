import discord
import random

zitat=['"Louis, ich denke das ist der Beginn einer wunderbaren Freundschaft." - Casablanca',
'"Ich mache ihm ein Angebot, das er nicht ablehnen kann." - Der Pate',
'"Möge die Macht mit dir sein!" - Star Wars',
'"Nach Hause telefonieren!" - E.T. - Der Außerirdische',
'"Was ist das" – "Das ist blaues Licht" – "Und was macht es?" – "Es leuchtet blau" - Rambo III',
'"Ich schau dir in die Augen, Kleines!" - Casablanca',
'"Das Leben ist wie eine Schachtel Pralinen, man weiß nie was man kriegt." - Forrest Gump',
'"Dumm ist der, der Dummes tut." - Forrest Gump',
'"Alles was du besitzt, besitzt irgendwann dich" - Fight Club',
'"Ich habe den Mut zu sterben. Ich frage dich aber, hast du den Mut zu leben" - Die Katze auf dem heißen Blechdach',
'"Das Leben bewegt sich sehr, sehr schnell. Wenn du nicht gelegentlich anhältst und dich umschaust, könntest du es verpassen" - Ferris macht Blau',
'"Yippie-Ya-Yeah, Schweinebacke!" - Stirb Langsam',
'"Mein Name ist Bond. James Bond." - James Bond jagt Dr. No',
'"Das ist doch kein Messer...DAS ist ein Messer!" - Crocodile Dundee – Ein Krokodil zum Küssen',
'"Wenn du versuchen solltest zu fliehen, habe ich sechs kleine Freunde, die alle schneller rennen können als Du." - From Dusk Till Dawn',
'"Ich liebe dich!" - "Ich weiß!" - Star Wars: Episode V – Das Imperium schlägt zurück',
'"Ich bin zu alt für diesen Scheiß!" - Lethal Weapon',
'"Ich bin der König der Welt!" - Titanic',
'"Ich geh jetzt mal pinkeln!" - "Das ist ein bißchen mehr Information, als ich mir erwünscht hatte, Vince. Aber gehen Sie ruhig." - Pulp Fiction',
'"Niemand verarscht Jesus!" - The Big Lebowski',
'"Mein Name ist Maximus Decimus Meridius. Kommandeur der Truppen des Nordens, Tribun der spanischen Legion, treuer Diener des wahren Imperators Marcus Aurelius. Vater eines ermordeten Sohnes, Ehemann einer ermordeten Frau und ich werde mich dafür rächen. In diesem Leben oder im nächsten." - Gladiator',
'''"I'll be back!" - Terminator''',
'"Hasta la vista, Baby!" - Terminator 2 - Tag der Abrechnung',
'"Wenn es blutet, kann man es töten." - Predator',
'''"Sprich zu der Hand"|"Talk to the hand, because the face won't listen" - Terminator 3 – Rebellion der Maschinen''',
''''"Wenn ich zwischen ihrem Glauben und meiner Neun-Millimeter wählen soll, dann nehm' ich meine Kanone." - End of Days''',
'"Ich will genau das, was sie hatte!" - Harry und Sally',
'"Normalerweise werde ich geküsst, bevor ich gebumst werde!" - Black Rain',
'"Ein hübsches kleines Nichts, das Sie da beinahe anhaben." - Diamantenfieber',
'''"Wie wär's mit einem Drink bei mir? Ganz harmlos, keine halben Sachen, nur guter Sex" - Bridget Jones''',
'"Du kannst nicht einfach drauflos fummeln. Du musst den Ofen einheizen, bevor Du den Truthahn reinstellst" - American Pie',
'"Oh Captain, mein Captain" - Club der Toten Dichter',
'"Rosebud" - Citizen Kane',
'"Freeeiiiheeeiiit!" - Braveheart',
'"Lauf Forrest! Lauf!" - Forrest Gump',
'"Flieht, ihr Narren!" - Herr der Ringe']

izitat=['''Der Film "Casablanca" gilt als Klassiker der Filmgeschichte und so haben auch einige Zitate aus dem Film die Zeit überdauert. Am Ende des Films geht Humphrey Bogart mit dem Polizeichef Captain Renault in den Nebel und spricht: "Louis, ich denke das ist der Beginn einer wunderbaren Freundschaft." (USA 1942)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Das Mafia-Epos "Der Pate" von Francis Ford Coppola ist definiti Kult. Dieses Zitat von Marlon Brando als Familienoberhaupt Don Corleone auch: "Ich mache ihm ein Angebot, das er nicht ablehnen kann." (USA 1972)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Möge die Macht mit dir sein!" sagt  Sir Alec Guinness als Obi-Wan Kenobi in George Lucas' "Star Wars"- Filmreihe. (USA 1977)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Nach Hause telefonieren!" Der niedliche Außerirdische E.T. will wieder zurück auf seinen Heimatplaneten und muss dafür Kontakt mit seinen Artgenossen aufnehmen. Der Satz aus "E.T. - Der Außerirdische" wurde in den 1980er Jahren zum geflügelten Wort und ist es bis heute geblieben. (USA 1982)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Aus "Rambo III" stammt dieser legendäre Dialog: "Was ist das" – "Das ist blaues Licht" – "Und was macht es?" – "Es leuchtet blau". (USA 1988)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Eines der schönsten, aber missverstandenen Filmzitate: "Ich schau dir in die Augen, Kleines!" Im Original sagt Humphrey Bogart als Rick in "Casablanca": "Here's looking at you, kid", was man mit: "Ich trinke auf dein Wohl, Kleines!" übersetzen könnte. In der Synchronfassung für Deutschland wurde das nicht verstanden – die Geburtsstunde dieses kultigen und so romantischen Zitats. (USA 1942)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Wenn es um einfache Lebensweisheiten geht, dann ist der mit sechs Oscars ausgezeichnete Film "Forrest Gump" eine wahre Schatzkiste. Hier unsere Nummer eins: "Das Leben ist wie eine Schachtel Pralinen, man weiß nie was man kriegt." Diesen Satz sagt Forrest Gump (Tom Hanks) auf der Parkbank zu einer Fremden. Er stammt natürlich von seiner Mutter, die ihn mit vielen klugen Merksätzen ausgestattet hat, zum Beispiel auch… (USA 1994)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Dumm ist der, der Dummes tut." Sehr richtig. Und eine Erkenntnis, zu der nicht nur die Gumps kamen, Denn schon in der Bibel steht: "An ihren Taten sollt ihr sie erkennen!"  (USA 1994)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Kurt Cobain bündelte Anfang der 1990er Jahre in seinem Song "Smells Like Teens Spirit" die Orientierungslosigkeit seiner Generation. Regisseur David Fincher brachte dieses Gefühl in dem Kultfilm "Fight Club" ebenfalls auf den Punkt. Dieser Satz von Tyler Durden (gespielt von Brad Pitt) steht für sich: "Alles was du besitzt, besitzt irgendwann dich". (USA 1999).
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Wenn ein Theaterstück von Tennessee Wiliams verfilmt wird, dann erwartet man starke Dialoge und einprägsame Sätze. So wie diesen hier: "Ich habe den Mut zu sterben. Ich frage dich aber, hast du den Mut zu leben" ausgesprochen von Harvey "Big Daddy" Pollitt (Burl Ives) in "Die Katze auf dem heißen Blechdach". Der Film behandelte einige "heiße" Themen in den USA der 1950er Jahre und war der Karriere-Boost für Paul Newman.
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Cameron Frye glaubt, dass ihm alles misslingt. Gut, dass er einen Freund wie Ferris Bueller hat, der ihn auf seine Abenteuer mitnimmt und den ein oder anderen Rat gibt. Zum Beispiel: "Das Leben bewegt sich sehr, sehr schnell. Wenn du nicht gelegentlich anhältst und dich umschaust, könntest du es verpassen", so Matthew Broderick in der kultigen 80er Komödie "Ferris macht Blau" (USA 1986)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Yippie-Ya-Yeah, Schweinebacke!" Wenn man sich nach stundenlangem Kampf eines Feindes entledigt, dann bitte so cool wie Bruce Willis als John McClane in dem Action-Klassiker "Stirb Langsam". (USA 1988)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Mein Name ist Bond. James Bond." Ein Zitat, dass jeder kennt und bis heute nichts von seiner Coolness verloren hat. Zuerst gesagt hat es Sean Connery in "James Bond jagt Dr. No" (USA 1962)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Das ist doch kein Messer...DAS ist ein Messer!" Ein gelungener Konter taugt immer als gutes Zitat. Schlagfertig und ordentlich bestückt zeigte sich Mick Dundee (Paul Hogan) in der australischen Komödie "Crocodile Dundee – Ein Krokodil zum Küssen". (USA 1986)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Wenn du versuchen solltest zu fliehen, habe ich sechs kleine Freunde, die alle schneller rennen können als Du." George Clooney spielte schon Ärzte ("Emergency Room"), Liebhaber ("Tage wie dieser") und smarte Ganoven ("Oceans-Filme"). Einen so abgebrühten Gangster wie in "From Dusk Till Dawn" verkörperte er allerdings nur einmal.
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''In "Star Wars: Episode V – Das Imperium schlägt zurück" soll Han Solo (Harrison Ford) in Anwesenheit der Prinzessin Leia (Carrie Fisher) in Karbonit eingefroren werden. Sie gesteht ihm daraufhin ihre Zuneigung: "Ich liebe dich!" Seine coole Antwort im Angesicht des Todes: "Ich weiß!" (USA 1980)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Danny Glover als Roger Murtaugh muss in "Lethal Weapon" mit seinem jungen Kollegen Martin Riggs (Mel Gibson) mithalten und der löst die Fälle als Polizist in L.A. gerne unkonventionell und mit viel Action. Was soll man da besseres sagen als: "Ich bin zu alt für diesen Scheiß!"  (USA 1987)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Wer nach 1997 auf einem Schiff war und am Bug stand, der hat sicherlich "den Leo gemacht". Leonardo DiCaprio spielte in "Titanic" die Rolle des Jack Dawson und stand mit seiner großen Liebe Rose (Kate Winslet) ganz an der Spitze des Schiffes und rief: "Ich bin der König der Welt!" - und das fand bis heute viele Nachahmer (1997)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Vincent Vega (John Travolta) kommt mit der Braut seines Boss nach einem großartigen Abend nach Hause und beide wollen es sich gemütlich machen. Vince sagt: "Ich geh jetzt mal pinkeln!", klare Ansage! Noch besser ist aber, was Mia Wallace (Uma Thurman) entgegnet: "Das ist ein bißchen mehr Information, als ich mir erwünscht hatte, Vince. Aber gehen Sie ruhig."
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Niemand verarscht Jesus!" oder im Original: "Nobody fucks with the Jesus!" In diesem Fall ist mit Jesus allerdings Jesus Quintana alias John Turturro gemeint, der in der Komödie "The Big Lebowski" einen herrlich nerdigen Bowling-Spieler mit diesem Namen spielt. (USA 1998)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Mein Name ist Maximus Decimus Meridius. Kommandeur der Truppen des Nordens, Tribun der spanischen Legion, treuer Diener des wahren Imperators Marcus Aurelius. Vater eines ermordeten Sohnes, Ehemann einer ermordeten Frau und ich werde mich dafür rächen. In diesem Leben oder im nächsten." Diese Ansage von "Gladiator" Russel Crowe lässt einem heute noch Gänsehaut entstehen. Das Zitat verrät, dass der Film nicht nur ein historisches Actiondrama ist – er ist ein unerbittliches Racheepos mit einem fulminanten Helden. (USA 2000)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"I'll be back!" oder im Deutschen: "Ich komme wieder!" Bei diesem wohl bekanntesten Zitat von Arnold Schwarzenegger als Terminator (T-800 in "Terminator") ist das englischsprachige Original-Zitat in Deutschland mindestens so bekannt, wie die deutsche Fassung. Und sind wir doch mal ehrlich, "I'll be back!" klingt viel cooler! (USA 1984)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Hasta la vista, Baby!" ist die Nummer zwei in Sachen Arnold Schwarzenegger-Zitaten, die jeder kennt. Es stammt aus dem zweiten Film – Schwarzenegger in "Terminator 2 - Tag der Abrechnung" (USA 1991)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Wenn es blutet, kann man es töten." Oder im Original: "If it bleeds, we can kill it." Simpel, aber war! Ausgesprochen von Dutch (Arnold Schwarzenegger) in dem Action-Science-Fiction-Movie "Predator". (USA 1987)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Dafür, dass Schwarzenegger oft als wortkarge Ein-Mann-Armee verunglimpft wurde, haben viele seiner Zitate die Zeit überdauert und sind Kult geworden. Zum Beispiel: "Sprich zu der Hand" - es stammt aus "Terminator 3 – Rebellion der Maschinen". Im Original und vollständig klingt es noch besser: "Talk to the hand, because the face won't listen". (USA 2003)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Wenn ich zwischen ihrem Glauben und meiner Neun-Millimeter wählen soll, dann nehm' ich meine Kanone." Kein Wunder, dass der Actionheld der 1980er und 90er Jahre sich in "End of Days" für die Knarre entschied. Ohne Waffe hat man den Österreicher auf der Leinwand selten gesehen. (USA 1999)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Harry (Billy Crystal) glaubt nicht, dass ihm eine Frau jemals einen Orgasmus vorgetäuscht hat. Sally (Meg Ryan), zeigt ihm daraufhin, wie realistisch ein vorgetäuschter Orgasmus klingen kann. Und das in einem vollbesetzen Cafe beim Frühstück. Am Ende des gespielten Orgasmus sagt die Frau vom Nachbartisch: "Ich will genau das, was sie hatte!" (USA 1989)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Normalerweise werde ich geküsst, bevor ich gebumst werde!" sagt Nick Conklin (Michael Douglas) in "Black Rain". Der Polizist fragt: "Was meint er damit?" Charly Vincent (Andi Garcia) erklärt, dass es nicht wirklich um Sex geht: "Vorspiel... er hätte gern ein Vorspiel, er möchte informiert werden." (USA 1989)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Ein hübsches kleines Nichts, das Sie da beinahe anhaben." Oder im Original: "That's a nice little nothing you're almost wearing." Gemeint ist Tiffany Case im für damalige Zeiten äußerst knappen Bikini. Gesagt hat es James Bond (Roger Moore) in "Diamantenfieber" (USA 1971)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''"Wie wär's mit einem Drink bei mir? Ganz harmlos, keine halben Sachen, nur guter Sex" – zu hören in "Bridget Jones". (USA 2001)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''','''Subtil geht es bei der Blödel-Orgie "American Pie" nie zu. Da wundert auch dieser Spruch aus dem zweiten Teil nicht: "Du kannst nicht einfach drauflos fummeln. Du musst den Ofen einheizen, bevor Du den Truthahn reinstellst". (USA 1999)
Quelle: https://www.tvdigital.de/entertainment/toplisten/filmzitate''']


help=('''
#####################
|     Hier ist eine Info zu                 |
| V den Befehlen für den Bot! V  | 
#####################
|  !help = Info zu Bot Befehlen     |
|   zitat = zufälliges Filmzitat       |
|  izitat = Hintergrunginfo mit     |
|          zufälligem Filmzitat           |
|!finally = Lass den Bot                 |
|          sich freuen!                          | 
|   Es gibt noch mehr Befehle,      |
|      finde diese heraus!                 |
|          Viel Spaß! :)                         | 
#####################
''')

final=['"WUUUHHHUUUU!!!! Geschafft! :partying_face: "','"Nice! :thumbsup:"','"Yay! :smile:"']

class MyClient(discord.Client):
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop. ")

    #Wenn eine Nachricht gepostet wird
    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " enthält " + message.content)
        if message.author == client.user:
            return

        if message.content.startswith("hey bot"):
            await message.channel.send("Hallo!!!111!1")

        if message.content.startswith("test"):
            await message.channel.send("123, test, test")

        if message.content.startswith("pi"):
            await message.channel.send("ist 3,1415926535 8979323846 2643383279 5028841971 6939937510 ...")

        if message.content.startswith("zitat"):
            await message.channel.send(random.choice(zitat))

        if message.content.startswith("izitat"):
            await message.channel.send(random.choice(izitat))

        if message.content.startswith("!help"):
            await message.channel.send(help)

        if message.content.startswith("!finally"):
            await message.channel.send(random.choice(final))

client = MyClient()
client.run("YOUR_CLIENT_ID_HERE")
