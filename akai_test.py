import mido
import threading
import time
import concurrent.futures
import sounddevice as sd
import numpy as np
# List all available input ports
print(mido.get_input_names())

# List all available output ports
print(mido.get_output_names())

qjack = 'Client-128:qjackctl 128:0'
lp = 'Launchpad Mini MK3:Launchpad Mini MK3 LPMiniMK3 MI 28:1'
akai = 'MPK mini 3:MPK mini 3 MIDI 1 20:0'
cc = 'control_change'
tempo = 120
spb = 60/tempo #seconds per beat

melodies={} #key is track, value is array of 2 measure 4/4 melodies
recording=[] # array of channels being recorded
def midi_to_freq(note):
    a440 = 440.0
    return a440 * 2.0**(note-69)/12
def numToNoise(note,duration):
    t = np.linspace90,
def listenLp():        
    with mido.open_input(lp) as inport:
        for msg in inport:
            print('lp',msg)
            # match msg:
            #     case mido.Message('control_change', value=127):
            #         print('DOWNLOAD REAPER ON THE PI')
                    
                
            

def listenAkai():     
    output = mido.open_output(qjack)

            
    with mido.open_input(akai) as inport:
        for msg in inport:
            if (msg.channel in recording):
                match msg:
                    case mido.Message('note_on'):
                        melodies[msg.channel].push(msg)
                
            print('AKAI',msg)
            # message = mido.Message(msg)
            # note_off = mido.Message('note_off', note=msg.note, velocity=msg.velocity)

            # Send Note On message
            # output.send(message)
            # time.sleep(quarter_note_duration)  # Wait for the duration of the quarter note

            # Send Note Off message
            # output.send(note_off)

            # Close the MIDI output port
    # output.close()




def metronome():
    #TODO:CLEAR ALL CONTROLS FIRST
    output = mido.open_output(lp)
    while True:
        for beat in range(8):
            # print(beat)
            on = mido.Message(cc, channel=7,control=beat,value=127)
            off = mido.Message(cc, channel=7,control=beat,value=0)
            output.send(on)
            time.sleep(spb)
            output.send(off)


#threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(listenAkai)
    executor.submit(metronome)
    executor.submit(listenLp)

listenAkai()