# -*- coding: utf-8 -*-
"""
Created on  July  7  2020

@author: Lyapin A.
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

class CheckListEvaluator():
    def __init__(self, debug = False):
        self.debug = debug
        self.parameterRange = np.arange(0, 97, 1)
        
        self.mechanism = []
        self.mechanism_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.mechanism_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.mechanism_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.mechanism_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.mechanism_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.mechanism_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.mechanism_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.mechanism.append(self.mechanism_perfect)
        self.mechanism.append(self.mechanism_good)
        self.mechanism.append(self.mechanism_pretty_good)
        self.mechanism.append(self.mechanism_above_average)
        self.mechanism.append(self.mechanism_acceptable)
        self.mechanism.append(self.mechanism_bad )
        self.mechanism.append(self.mechanism_unacceptable )
        
        self.fences = []
        self.fences_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.fences_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.fences_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.fences_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.fences_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.fences_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.fences_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.fences.append(self.fences_perfect)
        self.fences.append(self.fences_good)
        self.fences.append(self.fences_pretty_good)
        self.fences.append(self.fences_above_average)
        self.fences.append(self.fences_acceptable)
        self.fences.append(self.fences_bad )
        self.fences.append(self.fences_unacceptable )
        
        
        self.oil_rope = []
        self.oil_rope_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.oil_rope_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.oil_rope_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.oil_rope_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.oil_rope_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.oil_rope_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.oil_rope_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.oil_rope.append(self.oil_rope_perfect)
        self.oil_rope.append(self.oil_rope_good)
        self.oil_rope.append(self.oil_rope_pretty_good)
        self.oil_rope.append(self.oil_rope_above_average)
        self.oil_rope.append(self.oil_rope_acceptable)
        self.oil_rope.append(self.oil_rope_bad )
        self.oil_rope.append(self.mechanism_unacceptable )
        
        self.metalworks = []
        self.metalworks_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.metalworks_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.metalworks_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.metalworks_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.metalworks_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.metalworks_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.metalworks_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.metalworks.append(self.metalworks_perfect)
        self.metalworks.append(self.metalworks_good)
        self.metalworks.append(self.metalworks_pretty_good)
        self.metalworks.append(self.metalworks_above_average)
        self.metalworks.append(self.metalworks_acceptable)
        self.metalworks.append(self.metalworks_bad )
        self.metalworks.append(self.metalworks_unacceptable )
        
        self.winch = []
        self.winch_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.winch_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.winch_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.winch_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.winch_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.winch_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.winch_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.winch.append(self.winch_perfect)
        self.winch.append(self.winch_good)
        self.winch.append(self.winch_pretty_good)
        self.winch.append(self.winch_above_average)
        self.winch.append(self.winch_acceptable)
        self.winch.append(self.winch_bad )
        self.winch.append(self.winch_unacceptable )
        
        self.hook = []
        self.hook_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.hook_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.hook_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.hook_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.hook_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.hook_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.hook_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.hook.append(self.hook_perfect)
        self.hook.append(self.hook_good)
        self.hook.append(self.hook_pretty_good)
        self.hook.append(self.hook_above_average)
        self.hook.append(self.hook_acceptable)
        self.hook.append(self.hook_bad )
        self.hook.append(self.hook_unacceptable )
        
        self.сounterweight = []
        self.сounterweight_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.сounterweight_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.сounterweight_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.сounterweight_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.сounterweight_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.сounterweight_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.сounterweight_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.сounterweight.append(self.сounterweight_perfect)
        self.сounterweight.append(self.сounterweight_good)
        self.сounterweight.append(self.сounterweight_pretty_good)
        self.сounterweight.append(self.сounterweight_above_average)
        self.сounterweight.append(self.сounterweight_acceptable)
        self.сounterweight.append(self.сounterweight_bad )
        self.сounterweight.append(self.сounterweight_unacceptable )
        
        self.device = []
        self.device_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.device_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.device_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.device_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.device_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.device_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.device_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.device.append(self.device_perfect)
        self.device.append(self.device_good)
        self.device.append(self.device_pretty_good)
        self.device.append(self.device_above_average)
        self.device.append(self.device_acceptable)
        self.device.append(self.device_bad )
        self.device.append(self.device_unacceptable )
        
        self.lighting = []
        self.lighting_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.lighting_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.lighting_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.lighting_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.lighting_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.lighting_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.lighting_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.lighting.append(self.lighting_perfect)
        self.lighting.append(self.lighting_good)
        self.lighting.append(self.lighting_pretty_good)
        self.lighting.append(self.lighting_above_average)
        self.lighting.append(self.lighting_acceptable)
        self.lighting.append(self.lighting_bad )
        self.lighting.append(self.lighting_unacceptable )
        
        self.lock = []
        self.lock_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.lock_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.lock_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.lock_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.lock_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.lock_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.lock_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.lock.append(self.lock_perfect)
        self.lock.append(self.lock_good)
        self.lock.append(self.lock_pretty_good)
        self.lock.append(self.lock_above_average)
        self.lock.append(self.lock_acceptable)
        self.lock.append(self.lock_bad )
        self.lock.append(self.lock_unacceptable )
        
        self.cranetracks = []
        self.cranetracks_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.cranetracks_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.cranetracks_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.cranetracks_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.cranetracks_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.cranetracks_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.cranetracks_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.cranetracks.append(self.cranetracks_perfect)
        self.cranetracks.append(self.cranetracks_good)
        self.cranetracks.append(self.cranetracks_pretty_good)
        self.cranetracks.append(self.cranetracks_above_average)
        self.cranetracks.append(self.cranetracks_acceptable)
        self.cranetracks.append(self.cranetracks_bad )
        self.cranetracks.append(self.cranetracks_unacceptable )
        
        self.current_cable = []
        self.current_cable_perfect       = fuzz.trapmf(self.parameterRange, [84,92,96,96])
        self.current_cable_good          = fuzz.trapmf(self.parameterRange, [68,76,84,92])
        self.current_cable_pretty_good   = fuzz.trapmf(self.parameterRange, [52,60,68,76])
        self.current_cable_above_average = fuzz.trapmf(self.parameterRange, [36,44,52,60])
        self.current_cable_acceptable    = fuzz.trapmf(self.parameterRange, [20,28,36,44])
        self.current_cable_bad           = fuzz.trapmf(self.parameterRange, [ 4,12,20,28])
        self.current_cable_unacceptable  = fuzz.trapmf(self.parameterRange, [ 0, 0, 4,12])
        self.current_cable.append(self.current_cable_perfect)
        self.current_cable.append(self.current_cable_good)
        self.current_cable.append(self.current_cable_pretty_good)
        self.current_cable.append(self.current_cable_above_average)
        self.current_cable.append(self.current_cable_acceptable)
        self.current_cable.append(self.current_cable_bad )
        self.current_cable.append(self.current_cable_unacceptable )
    
        self.w_factors = [0.08,0.08,0.09,0.09,0.09,0.09,0.08,0.08,0.08 ,0.08 ,0.08, 0.08]

    def __w_summ(self, states, weights):
        assert(len(states)>0)
        assert(len(states)==len(weights))
        
        res = [0 for s in range(len(states[0]))]
        for state, weight  in zip(states,weights):
            for i, s in enumerate(state):
                res[i] += s*weight
        return res

    def __createStates(self, answers):
        self.states=[]
        self.states.append(self.mechanism[answers[0]])
        self.states.append(self.fences[answers[1]])
        self.states.append(self.oil_rope[answers[2]])
        self.states.append(self.metalworks[answers[3]])
        self.states.append(self.winch[answers[4]])
        self.states.append(self.hook[answers[5]])
        self.states.append(self.сounterweight[answers[6]])
        self.states.append(self.device[answers[7]])
        self.states.append(self.lighting[answers[8]])
        self.states.append(self.lock[answers[9]])
        self.states.append(self.cranetracks[answers[10]])
        self.states.append(self.current_cable[answers[11]])

    def evaluateSafetyState(self, answers):
        self.__createStates(answers)
                
        res = self.__w_summ(self.states, self.w_factors)
        val_current_cable = fuzz.defuzzify.centroid(self.parameterRange,res)

        if (val_current_cable <= 30):
            level=0
        else:
            if (val_current_cable <= 70):
                level = 1
            else:
                level = 2
                
        if (self.debug): 
            print("Level = ", level)
            plt.plot(self.parameterRange, res)
        
        return level



    

def run():
    # Определение значений лингвистических переменных
    answers = [0,1,2,1,2,1,0,3,4,1,1,2]
    
    clEvaluator = CheckListEvaluator()
    print(clEvaluator.evaluateSafetyState(answers))
   


if __name__ == "__main__":
    run()





