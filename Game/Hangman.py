import pygame, random
from Game.settings import *
class Hangman:
    
    def __init__(self,word=None):
        pygame.init()
        self.window=pygame.display.set_mode((WIDTH,HEIGHT))
        self.btn_font = pygame.font.SysFont("arial", 20)
        self.guess_font = pygame.font.SysFont("monospace", 24)
        self.lost_font = pygame.font.SysFont('arial', 45)
        self.word = word
        if(not word):
            self.word=self.randomWord()
        self.buttons = []
        self.guessed = []
        self.hangmanPics = [
            pygame.image.load('Game/resources/hangman0.png'),
            pygame.image.load('Game/resources/hangman1.png'),
            pygame.image.load('Game/resources/hangman2.png'),
            pygame.image.load('Game/resources/hangman3.png'),
            pygame.image.load('Game/resources/hangman4.png'),
            pygame.image.load('Game/resources/hangman5.png'),
            pygame.image.load('Game/resources/hangman6.png')
            ]
        self.limbs = 0
        self.initialize_buttons()
        self.playing=True


    #handles draw functionalities of game
    def draw(self):
        self.window.fill(GREEN)
        # Buttons
        for i in range(len(self.buttons)):
            if self.buttons[i][4]:
                pygame.draw.circle(self.window, BLACK, (self.buttons[i][1], self.buttons[i][2]),self.buttons[i][3])
                pygame.draw.circle(self.window, self.buttons[i][0], (self.buttons[i][1], self.buttons[i][2]), self.buttons[i][3] - 2)
                label = self.btn_font.render(chr(self.buttons[i][5]), 1, BLACK)
                self.window.blit(label, (self.buttons[i][1] - (label.get_width() / 2), self.buttons[i][2] - (label.get_height() / 2)))

        spaced = self.spacedOut(self.word, self.guessed)
        label1 = self.guess_font.render(spaced, 1, BLACK)
        rect = label1.get_rect()
        length = rect[2]
        
        self.window.blit(label1,(WIDTH/2 - length/2, 400))

        pic = self.hangmanPics[self.limbs]
        self.window.blit(pic, (WIDTH/2 - pic.get_width()/2 + 20, 150))
        pygame.display.update()
    

    def hang(self,guess):
        if guess.lower() not in self.word.lower():
            return True
        else:
            return False
    
    def spacedOut(self,word, guessed=[]):
        spacedWord = ''
        guessedLetters = guessed
        for x in range(len(word)):
            if self.word[x] != ' ':
                spacedWord += '_ '
                for i in range(len(guessedLetters)):
                    if self.word[x].upper() == guessedLetters[i]:
                        spacedWord = spacedWord[:-2]
                        spacedWord += self.word[x].upper() + ' '
            elif word[x] == ' ':
                spacedWord += ' '
        return spacedWord
    
    def buttonHit(self,x, y):
        for i in range(len(self.buttons)):
            if x < self.buttons[i][1] + 20 and x > self.buttons[i][1] - 20:
                if y < self.buttons[i][2] + 20 and y > self.buttons[i][2] - 20:
                    return self.buttons[i][5]
        return None

    
    def gameOver(self,winner=False):
        lostTxt = 'You Lost, press any key to play again...'
        winTxt = 'WINNER!, press any key to play again...'
        self.draw()
        pygame.time.delay(1000)
        self.window.fill(GREEN)

        if winner == True:
            label = self.lost_font.render(winTxt, 1, BLACK)
        else:
            label = self.lost_font.render(lostTxt, 1, BLACK)

        wordTxt = self.lost_font.render(self.word.upper(), 1, BLACK)
        wordWas = self.lost_font.render('The phrase was: ', 1, BLACK)

        self.window.blit(wordTxt, (WIDTH/2 - wordTxt.get_width()/2, 295))
        self.window.blit(wordWas, (WIDTH/2 - wordWas.get_width()/2, 245))
        self.window.blit(label, (WIDTH / 2 - label.get_width() / 2, 140))
        pygame.display.update()
        again = True
        while again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    again = False
        self.startNewGame('testing')
    
    def randomWord(self):
        file = open('Game/resources/words.txt')
        f = file.readlines()
        i = random.randrange(0, len(f) - 1)

        return f[i]
    def startNewGame(self,word=None):
        if(not word):
            self.randomWord()
        for i in range(len(self.buttons)):
            self.buttons[i][4] = True

        self.limbs = 0
        self.guessed = []
        self.word = word

    # Setup buttons
    def initialize_buttons(self):
        increase = round(WIDTH / 13)
        for i in range(26):
            if i < 13:
                y = 40
                x = 25 + (increase * i)
            else:
                x = 25 + (increase * (i - 13))
                y = 85
            self.buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
            #                  [color, x_pos, y_pos, radius, visible, char])
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                letter = self.buttonHit(clickPos[0], clickPos[1])
                if letter != None:
                    self.guessed.append(chr(letter))
                    self.buttons[letter - 65][4] = False
                    if self.hang(chr(letter)):
                        if self.limbs != 5:
                            self.limbs += 1
                        else:
                            self.gameOver()
                    else:
                        print(self.spacedOut(self.word, self.guessed))
                        if self.spacedOut(self.word, self.guessed).count('_') == 0:
                            self.gameOver(True)


    def run(self):
        while self.playing:
            self.draw()
            self.events()
        pygame.quit()
