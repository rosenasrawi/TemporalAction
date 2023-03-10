from psychopy import visual
from psychopy.hardware import keyboard

from settings import *

window = visual.Window(
    color = monitor['col'],
    monitor = "testMonitor", 
    size = monitor['res'],
    units = "pix",
    fullscr = True)

kb = keyboard.Keyboard()

mouse = visual.CustomMouse(
    win = window,
    visible = False)

fixcross = visual.ShapeStim(
    win = window, 
    vertices = ((0,-fix['size']), (0,fix['size']), (0,0), (-fix['size'],0), (fix['size'],0)),
    lineWidth = fix['line'],
    closeShape = False,
    units = 'pix')

def makeBar(pos):

    barstim = visual.Rect(
        win = window,
        units = "pix",
        width = bar['size'][0],
        height = bar['size'][1],
        pos = pos)

    return barstim

leftbar = makeBar(pos = (-bar['shift'], 0))
rightbar = makeBar(pos = (bar['shift'], 0))
centerbar = makeBar(pos = (0,0)); centerbar.fillColor = fix['basecol']

def makeDial(rad, pos = (0,0), handle = False):

    circle = visual.Circle(
        win = window,
        radius = rad,
        edges = dial['edge'],
        lineWidth = dial['line'],
        lineColor = dial['col'],
        pos = pos)

    if handle:
        circle.fillColor = monitor['col'] 
    return circle

dialcirc = makeDial(dial['rad'])
turntop = makeDial(dial['hrad'], pos = (0, dial['hpos']), handle = True)
turnbot = makeDial(dial['hrad'], pos = (0, -dial['hpos']), handle = True)

def makeText(input, pos = (0,0), col = text['col']):

    textstim = visual.TextStim(
        win = window, 
        font = text['font'],
        text = input,
        color = col,
        pos = pos,
        height = text['size'])

    return textstim

feedback = makeText('', text['fbpos'])
blockfb = makeText('')

col1 = makeText('', text['lpos'])
then = makeText('then')
col2 = makeText('', text['rpos'])

time2practice = makeText('Time to practice first:', text['tpos'])
time2block = makeText('All clear? Remember:', text['tpos'])
practicedial = makeText('Turn the dial to match the bar', text['tpos'])

space2start = makeText('Press SPACE to continue',  text['bpos'])
calibwait = makeText('Please wait for the experimenter to calibrate the eye-tracker')

blockcount = makeText('', text['tpos'])
takebreak = makeText('You can take a short break')

taskstart = makeText('Ready to start?')
taskend = makeText('You have completed this part of the task! Well done :>}')
savingdata = makeText('Saving data! Please wait')
space2close = makeText('Press SPACE to close this screen',  text['bpos'])
