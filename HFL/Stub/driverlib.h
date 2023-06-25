#ifndef DRIVERLIB_H
#define DRIVERLIB_H
#include "Std_Types.h"
//static inline void EPWM_clearEventTriggerInterruptFlag(uint32_t base);
 void EPWM_clearEventTriggerInterruptFlag();
 uint32_t CPUTimer_getTimerCount();
 void Interrupt_clearACKGroup();
#endif