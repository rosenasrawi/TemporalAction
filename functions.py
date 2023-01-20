from psychopy import core, event

import random
from math import cos, sin
from statistics import mean

from stimuli import *
from settings import *

def turnHandle(pos, rad):
    
    x, y = pos
    pos = (x * cos(rad) + y * sin(rad), -x * sin(rad) + y * cos(rad))

    return pos

def getReportori(key, turns):
    
    repori = degrees(turns * dial['step'])

    if key == 'z':
        repori *= -1
    
    return repori
 
def getPerformance(repori, targori):

    diff = abs(targori - round(repori))

    if diff > 90:
        diff -= 180
        diff *= -1

    perf = round(100 - diff/90 * 100)

    return perf

def getOri(tilt):

    ori = [random.randint(bar[tilt[0]][0], bar[tilt[0]][1]),
           random.randint(bar[tilt[1]][0], bar[tilt[1]][1])]

    return ori

def setBlock():

    cols = bar['cols'].copy()
    names = bar['colnames']
    random.shuffle(cols)

    col1.color = cols[0]; col1.text = names[bar['cols'].index(cols[0])]
    col2.color = cols[1]; col2.text = names[bar['cols'].index(cols[1])]
    
    return cols

def setTrial(trial, cols):
    
    tcol = cols[:2]; ncol = cols[2:]
    random.shuffle(ncol) 
    
    order, loc, tilt = trials[trial]

    if order == 'second':
        tcol.reverse()

    tori = getOri(tilt); nori = getOri(tilt)
    nori.reverse()
    
    if loc == 'LR':
        enc1 = [tcol[0], ncol[0], tori[0], nori[0]]
        enc2 = [ncol[1], tcol[1], nori[1], tori[1]]
    elif loc == 'RL':
        enc1 = [ncol[0], tcol[0], nori[0], tori[0]]
        enc2 = [tcol[1], ncol[1], tori[1], nori[1]]

    if order == 'second':
        tori.reverse()

    return enc1, enc2, tori

def showCue():

    cols = setBlock()

    fixcross.setAutoDraw(False)
    col1.draw(); then.draw(); col2.draw()

    space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')

    return cols

def showFix(tfix):

    fixcross.lineColor = fix['basecol']
    
    for _ in range(tfix):
        fixcross.draw()
        window.flip()

def showBars(settings):

    leftbar.fillColor, rightbar.fillColor, leftbar.ori, rightbar.ori = settings

    for _ in range(timing['enc']):
        fixcross.draw(); leftbar.draw(); rightbar.draw()
        window.flip()

def showStim(trial, cols):

    tfix = random.randint(timing['fix'][0], timing['fix'][1])
    enc1, enc2, tori = setTrial(trial, cols)
    
    showFix(tfix)

    showBars(enc1)
    showFix(timing['del1'])

    showBars(enc2)
    showFix(timing['del2'])

    return tori

def showDial():
    
    kb.clearEvents()
    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

    released = []; pressed = []; turns = 0

    fixcross.lineColor = fix['probecol']
    fixcross.draw()
    window.flip()

    pressed = event.waitKeys(keyList = ['z', 'm', 'q'])

    if 'm' in pressed: 
        key = 'm'; rad = dial['step']
    elif 'z' in pressed: 
        key = 'z'; rad = -dial['step']
    if 'q' in pressed:
        core.quit()
    
    while released == [] and turns <= dial['max']:

        released = kb.getKeys(keyList = [key], waitRelease = True, clear = True)

        turntop.pos = turnHandle(turntop.pos, rad)
        turnbot.pos = turnHandle(turnbot.pos, rad)

        turns += 1
        dialcirc.draw(); fixcross.draw()
        turntop.draw(); turnbot.draw()
        window.flip()

    fixcross.lineColor = fix['basecol']

    return key, turns

def showFeedback(perf):

    fixcross.lineColor = fix['basecol']
    feedback.text = perf
    
    for _ in range(timing['fb']):
        fixcross.draw(); feedback.draw()
        window.flip()

def showBlockfb(blockperf):

    showFix(timing['enc'])

    blockfb.text = 'Average score this block: ' + blockperf + '/100'

    blockfb.draw(); space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')