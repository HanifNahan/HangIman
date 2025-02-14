import pygame
import sys
import random
from time import sleep
from pygame.locals import *
from timeit import default_timer as timer

fps = 60
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
lightred = (255, 165, 145)
darklightred = (255, 97, 81)
lightblue = (126, 178, 255)
darklightblue = (42, 129, 255)
lightgrey = (192, 192, 192)
biru = (25, 33, 148)
hijau = (161, 255, 10)
merah = (140, 53, 53)
oren = (254, 159, 1)

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (width, height))
title_img = pygame.image.load('title_img.png')

textBoxSpace = 5
textBoxNumber = 0


def button(word, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h), border_radius=20)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h), border_radius=20)

    buttonText = pygame.font.SysFont("showcardgothic", 20)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(buttonTextSurf, buttonTextRect)


def endGame():
    global textBoxSpace, textBoxNumber, end, start
    end = timer()
    print("Time it took: ", end - start)
    timeTaken = (end - start)
    textBoxSpace = 5
    textBoxNumber = 0
    message = "Time taken: " + str(round(timeTaken)) + "s"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button("Yes", (width/2)-50, 430, 100, 50,
               darklightred, lightred, quitGame)
        button("No", (width/2)-50, 495, 100, 50,
               darklightred, lightred, hangman)

        largeText = pygame.font.SysFont("algerian", 80)
        TextSurf = largeText.render("Quit Game?", True, biru)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height * 0.6)
        screen.blit(TextSurf, TextRect)

        textSurf = largeText.render(message, True, biru)
        textRect = textSurf.get_rect()
        textRect.center = (width/2, 290)
        screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(fps)


def quitGame():
    pygame.quit()
    sys.exit()


def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def main():
    global clock, screen, play
    pygame.mixer.music.play(-1)
    play = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("HangIman - Kumpulan 2")

    while True:
        hangman()


def placeLetter(letter):
    global pick, pickSplit
    space = 10
    wordSpace = 0
    while wordSpace < len(pick):
        text = pygame.font.SysFont('algerian', 40)
        if letter in pickSplit[wordSpace]:
            textSurf = text.render(letter, True, black)
            textRect = textSurf.get_rect()
            textRect.center = (((150)+space), (200))
            screen.blit(textSurf, textRect)
        wordSpace += 1
        space += 60

    pygame.display.update()
    clock.tick(fps)


def textBoxLetter(letter):
    global textBoxSpace, textBoxNumber
    if textBoxNumber <= 5:
        text = pygame.font.SysFont("algerian", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace), (300))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 10:
        text = pygame.font.SysFont("algerian", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace), (350))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 15:
        text = pygame.font.SysFont("algerian", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace), (400))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 20:
        text = pygame.font.SysFont("algerian", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace), (450))
        screen.blit(textSurf, textRect)

    pygame.display.update()
    clock.tick(fps)


def hangman():
    global textBoxSpace, textBoxNumber
    textBoxSpace = 5
    textBoxNumber = 0
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))
        space = 10
        textBoxSpace = 5

        # text = pygame.font.Font("freesansbold.ttf", 20)
        # textSurf = text.render(
        #     "Kumpulan 2 - HANGMAN!!!", True, black)
        # textRect = textSurf.get_rect()
        # textRect.center = ((width/2), (height/2))
        # screen.blit(textSurf, textRect)
        imgRect = title_img.get_rect()
        imgRect.center = ((width/2), (height/2))
        screen.blit(title_img, imgRect)

        button("Waktu Solat", 50, 400, 250, 100, biru, lightgrey, WaktuSolat)
        button("Solat Sunat", 500, 400, 250, 100, biru, lightgrey, SolatSunat)
        button("Rukun Wudhu'", 50, 100, 250,
               100, biru, lightgrey, RukunWudhuk)
        button("Syarat Wajib Solat", 500, 100,
               250, 100, biru, lightgrey, SyaratWajibSolat)

        pygame.display.update()
        clock.tick(fps)


def hangmanGame(catagory, title):
    global pause, pick, pickSplit, textBoxSpace, textBoxNumber, start
    start = timer()
    chances = 20
    pick = random.choice(catagory)
    pickSplit = [pick[i:i+1] for i in range(0, len(pick), 1)]

    screen.blit(bg, (0, 0))
    print(pick)

    # if pick == 'subuh':
    #     pygame.draw.rect(screen, black, (0, 0, 15, 15))

    wordSpace = 0
    space = 10
    while wordSpace < len(pick):
        text = pygame.font.SysFont("timesnewroman", 40)
        textSurf1 = text.render("_", True, black)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (((150)+space), (200))
        screen.blit(textSurf1, textRect1)
        space = space + 60
        wordSpace += 1

    guesses = ''
    gamePlay = True
    while gamePlay == True:
        guessLett = ''

        if textBoxNumber == 5:
            textBoxSpace = 5
        if textBoxNumber == 10:
            textBoxSpace = 5
        if textBoxNumber == 15:
            textBoxSpace = 5

        pygame.draw.rect(screen, oren, [620, 32, 150, 20])
        text = pygame.font.SysFont("timesnewroman", 20)
        textSurf = text.render(("Chances: %s" % chances), False, black)
        textRect = textSurf.get_rect()
        textRect.topright = (750, 30)
        screen.blit(textSurf, textRect)

        textTitle = pygame.font.SysFont("showcardgothic", 40)
        textTitleSurf = textTitle.render(title, True, hijau)
        textTitleRect = textTitleSurf.get_rect()
        textTitleRect.center = ((width/2), 60)
        screen.blit(textTitleSurf, textTitleRect)

        pygame.draw.rect(screen, black, [100, 260, 250, 250], 2)

        hintWaktuSolat = ['Bermula dari naik fajar sadiq sehingga terbitnya matahari', 'atau dikenali sebagai Syuruk',
                          'Bermula daripada gelincir matahari dari kedudukan tengah langit', 'hingga bayang-bayang suatu benda menyamai panjangnya', 'Sesuatu bayang objek melebihi kepanjangan sebenar', 'sehingga matahari mula terbenam', 'Bermula apabila matahari terbenam (hilang bentuk bulatannya)', 'hingga hilang cahaya kemerahan di kaki langit', 'Bermula apabila hilang cahaya merah di kaki langit hingga', 'terbit fajar sadiq']
        hintSolatSunat = ['Solat yang dilakukan selepas solat isyak pada bulan', 'ramadhan sebanyak 20 rakaat', 'Solat yang dilakukan selepas terbit matahari', 'sehingga tergelincir matahari',
                          'solat yang dilakukan pada 2/3 malam selepas terbangun', 'dari tidur', 'solat yang dilakukan untuk memohon sesuatu permintaan', 'solat yang diucapkan tasbih didalamnya sebanyak 300 kali']
        hintRukunWudhuk = ['Pertama - _____ di dalam hati',
                           'Kedua - Membasuh keseluruhan _____', 'Ketiga - Membasuh kedua _____ hingga ke siku', 'Keempat - Menyapu sebahagian _____', 'Kelima - Membasuh kedua _____ hingga ke buku lali', 'Keenam - _____, iaitu mengikut turutan']
        hintSyaratWajib = ['Solat tidak wajib keatas orang bukan _____',
                           'Tidak wajib solat ke atas orang yang belum _____,', 'iaitu belum cukup umur', 'Hendaklah _____ daripada haid dan nifas', 'Tidak wajib menunaikan solat ke atas orang yang tidak', '_____, iaitu gila']

        font = pygame.font.SysFont('timesnewroman', 25)
        # text = font.render(hintWaktuSolat.index, True, biru)
        # textRect = text.get_rect()
        # textRect.center = (width//2, height//4)

        if pick == 'subuh':
            screen.blit(font.render(
                hintWaktuSolat[0], True, oren), (width*0.1, height*0.18))
            screen.blit(font.render(
                hintWaktuSolat[1], True, oren), (width*0.1, height*0.23))
        elif pick == 'zohor':
            screen.blit(font.render(
                hintWaktuSolat[2], True, oren), (width*0.1, height*0.18))
            screen.blit(font.render(
                hintWaktuSolat[3], True, oren), (width*0.1, height*0.23))
        elif pick == 'asar':
            screen.blit(font.render(
                hintWaktuSolat[4], True, oren), (width*0.1, height*0.18))
            screen.blit(font.render(
                hintWaktuSolat[5], True, oren), (width*0.1, height*0.23))
        elif pick == 'maghrib':
            screen.blit(font.render(
                hintWaktuSolat[6], True, oren), (width*0.1, height*0.18))
            screen.blit(font.render(
                hintWaktuSolat[7], True, oren), (width*0.1, height*0.23))
        elif pick == 'isyak':
            screen.blit(font.render(
                hintWaktuSolat[8], True, oren), (width*0.1, height*0.18))
            screen.blit(font.render(
                hintWaktuSolat[9], True, oren), (width*0.1, height*0.23))
        elif pick == 'terawih':
            screen.blit(font.render(
                hintSolatSunat[0], True, oren), (width*0.2, height*0.18))
            screen.blit(font.render(
                hintSolatSunat[1], True, oren), (width*0.2, height*0.23))
        elif pick == 'dhuha':
            screen.blit(font.render(
                hintSolatSunat[2], True, oren), (width*0.2, height*0.18))
            screen.blit(font.render(
                hintSolatSunat[3], True, oren), (width*0.2, height*0.23))
        elif pick == 'tahajud':
            screen.blit(font.render(
                hintSolatSunat[4], True, oren), (width*0.2, height*0.18))
            screen.blit(font.render(
                hintSolatSunat[5], True, oren), (width*0.2, height*0.23))
        elif pick == 'hajat':
            screen.blit(font.render(
                hintSolatSunat[6], True, oren), (width*0.2, height*0.18))
        elif pick == 'tasbih':
            screen.blit(font.render(
                hintSolatSunat[7], True, oren), (width*0.2, height*0.18))
        elif pick == 'niat':
            screen.blit(font.render(
                hintRukunWudhuk[0], True, oren), (width*0.2, height*0.18))
        elif pick == 'muka':
            screen.blit(font.render(
                hintRukunWudhuk[1], True, oren), (width*0.2, height*0.18))
        elif pick == 'tangan':
            screen.blit(font.render(
                hintRukunWudhuk[2], True, oren), (width*0.2, height*0.18))
        elif pick == 'kepala':
            screen.blit(font.render(
                hintRukunWudhuk[3], True, oren), (width*0.2, height*0.18))
        elif pick == 'kaki':
            screen.blit(font.render(
                hintRukunWudhuk[4], True, oren), (width*0.2, height*0.18))
        elif pick == 'tertib':
            screen.blit(font.render(
                hintRukunWudhuk[5], True, oren), (width*0.2, height*0.18))
        elif pick == 'islam':
            screen.blit(font.render(
                hintSyaratWajib[0], True, oren), (width*0.2, height*0.18))
        elif pick == 'baligh':
            screen.blit(font.render(
                hintSyaratWajib[1], True, oren), (width*0.2, height*0.18))
            screen.blit(font.render(
                hintSyaratWajib[2], True, oren), (width*0.2, height*0.23))
        elif pick == 'suci':
            screen.blit(font.render(
                hintSyaratWajib[3], True, oren), (width*0.2, height*0.18))
        elif pick == 'berakal':
            screen.blit(font.render(
                hintSyaratWajib[4], True, oren), (width*0.2, height*0.18))
            screen.blit(font.render(
                hintSyaratWajib[5], True, oren), (width*0.2, height*0.23))

        if chances == 19:
            pygame.draw.rect(screen, black, [450, 550, 100, 10])
        elif chances == 18:
            pygame.draw.rect(screen, black, [550, 550, 100, 10])
        elif chances == 17:
            pygame.draw.rect(screen, black, [650, 550, 100, 10])
        elif chances == 16:
            pygame.draw.rect(screen, black, [500, 450, 10, 100])
        elif chances == 15:
            pygame.draw.rect(screen, black, [500, 350, 10, 100])
        elif chances == 14:
            pygame.draw.rect(screen, black, [500, 250, 10, 100])
        elif chances == 13:
            pygame.draw.rect(screen, black, [500, 250, 150, 10])
        elif chances == 12:
            pygame.draw.rect(screen, black, [600, 250, 100, 10])
        elif chances == 11:
            pygame.draw.rect(screen, black, [600, 250, 10, 50])
        elif chances == 10:
            pygame.draw.line(screen, black, [505, 505], [550, 550], 10)
        elif chances == 9:
            pygame.draw.line(screen, black, [550, 250], [505, 295], 10)
        elif chances == 8:
            pygame.draw.line(screen, black, [505, 505], [460, 550], 10)
        elif chances == 7:
            pygame.draw.circle(screen, black, [605, 325], 30)
        elif chances == 6:
            pygame.draw.rect(screen, black, [600, 350, 10, 60])
        elif chances == 5:
            pygame.draw.rect(screen, black, [600, 410, 10, 60])
        elif chances == 4:
            pygame.draw.line(screen, black, [605, 375], [550, 395], 10)
        elif chances == 3:
            pygame.draw.line(screen, black, [605, 375], [650, 395], 10)
        elif chances == 2:
            pygame.draw.line(screen, black, [605, 465], [550, 485], 10)
        elif chances == 1:
            pygame.draw.line(screen, black, [605, 465], [650, 485], 10)

        button("Back", 25, 30, 100, 50, black, lightgrey, hangman)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                failed = 0
                print("Failed", failed)
                print("Chance", chances)

                # if event.key == pygame.K_SPACE:
                #     pause()

                if event.key == pygame.K_ESCAPE:
                    gamePlay = False

                if event.key == pygame.K_a:
                    # letter a
                    guessLett = guessLett + 'a'
                    guesses += guessLett
                    print("letter a guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('a')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('a')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_b:
                    # letter b
                    guessLett = guessLett + 'b'
                    guesses += guessLett
                    print("letter b guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('b')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('b')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_c:
                    # letter c
                    guessLett = guessLett + 'c'
                    guesses += guessLett
                    print("letter c guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('c')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('c')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_d:
                    # letter d
                    guessLett = guessLett + 'd'
                    guesses += guessLett
                    print("letter d guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('d')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('d')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_e:
                    # letter e
                    guessLett = guessLett + 'e'
                    guesses += guessLett
                    print("letter e guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('e')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('e')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_f:
                    # letter f
                    guessLett = guessLett + 'f'
                    guesses += guessLett
                    print("letter f guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('f')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('f')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_g:
                    # letter g
                    guessLett = guessLett + 'g'
                    guesses += guessLett
                    print("letter g guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('g')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('g')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_h:
                    # letter h
                    guessLett = guessLett + 'h'
                    guesses += guessLett
                    print("letter h guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('h')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('h')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_i:
                    # letter i
                    guessLett = guessLett + 'i'
                    guesses += guessLett
                    print("letter i guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('i')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('i')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_j:
                    # letter j
                    guessLett = guessLett + 'j'
                    guesses += guessLett
                    print("letter j guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('j')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        #gamePlay = False
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('j')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        #gamePlay = False
                        endGame()

                if event.key == pygame.K_k:
                    # letter k
                    guessLett = guessLett + 'k'
                    guesses += guessLett
                    print("letter k guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('k')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('k')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_l:
                    # letter l
                    guessLett = guessLett + 'l'
                    guesses += guessLett
                    print("letter l guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('l')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('l')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_m:
                    # letter m
                    guessLett = guessLett + 'm'
                    guesses += guessLett
                    print("letter m guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('m')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('m')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_n:
                    # letter n
                    guessLett = guessLett + 'n'
                    guesses += guessLett
                    print("letter n guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('n')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        #gamePlay = False
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('n')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        #gamePlay = False
                        endGame()

                if event.key == pygame.K_o:
                    # letter o
                    guessLett = guessLett + 'o'
                    guesses += guessLett
                    print("letter o guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('o')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('o')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_p:
                    # letter p
                    guessLett = guessLett + 'p'
                    guesses += guessLett
                    print("letter p guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('p')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('p')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_q:
                    # letter q
                    guessLett = guessLett + 'q'
                    guesses += guessLett
                    print("letter q guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('a')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('q')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_r:
                    # letter r
                    guessLett = guessLett + 'r'
                    guesses += guessLett
                    print("letter r guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('r')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('r')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_s:
                    # letter s
                    guessLett = guessLett + 's'
                    guesses += guessLett
                    print("letter s guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('s')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('s')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_t:
                    # letter t
                    guessLett = guessLett + 't'
                    guesses += guessLett
                    print("letter t guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('t')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('t')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_u:
                    # letter u
                    guessLett = guessLett + 'u'
                    guesses += guessLett
                    print("letter u guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1
                    if guessLett in pick:
                        placeLetter('u')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('u')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_v:
                    # letter v
                    guessLett = guessLett + 'v'
                    guesses += guessLett
                    print("letter v guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('v')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('v')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_w:
                    # letter w
                    guessLett = guessLett + 'w'
                    guesses += guessLett
                    print("letter w guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('w')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('w')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_x:
                    # letter x
                    guessLett = guessLett + 'x'
                    guesses += guessLett
                    print("letter x guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1
                    if guessLett in pick:
                        placeLetter('x')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('x')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_y:
                    # letter y
                    guessLett = guessLett + 'y'
                    guesses += guessLett
                    print("letter y guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('y')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('y')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

                if event.key == pygame.K_z:
                    # letter z
                    guessLett = guessLett + 'z'
                    guesses += guessLett
                    print("letter z guessed")
                    print("")
                    for char in pick:
                        if char in guesses:
                            print(char)
                        else:
                            print("_")
                            failed += 1

                    if guessLett in pick:
                        placeLetter('z')

                    if failed == 0:
                        print("You got the word")
                        print(pick)
                        endGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        print("")
                        print(textBoxNumber)
                        print("")
                        print("That letter is not in the word")
                        textBoxLetter('z')

                    if chances == 0:
                        print("Sorry you have lost")
                        print("The word was", pick)
                        endGame()

        pygame.display.update()
        clock.tick(fps)

    pygame.display.update()
    clock.tick(fps)


def WaktuSolat():
    waktuSolat = ['subuh', 'zohor', 'asar', 'maghrib', 'isyak']
    print("Waktu Solat")
    title = "Waktu Solat"
    hangmanGame(waktuSolat, title)


def SolatSunat():
    solatSunat = ['terawih', 'dhuha', 'tahajud', 'hajat', 'tasbih']
    print("Solat Sunat")
    title = "Solat Sunat"
    hangmanGame(solatSunat, title)


def RukunWudhuk():
    rukunWudhuk = ['niat', 'muka', 'tangan', 'kepala', 'kaki', 'tertib']
    print("Rukun Wudhu'")
    title = "Rukun Wudhu'"
    hangmanGame(rukunWudhuk, title)


def SyaratWajibSolat():
    syaratWajibSolat = ['islam', 'baligh', 'suci', 'berakal']
    print("Syarat Wajib Solat")
    title = "Syarat Wajib Solat"
    hangmanGame(syaratWajibSolat, title)


if __name__ == '__main__':
    main()
