#include "stubbed_driverlib.h"
void (*_p_EPWM_clearEventTriggerInterruptFlag)();
void EPWM_clearEventTriggerInterruptFlag()
{
  return _p_EPWM_clearEventTriggerInterruptFlag();
}

void set_p_EPWM_clearEventTriggerInterruptFlag(void *f)
{
  _p_EPWM_clearEventTriggerInterruptFlag = f;
}

uint32_t (*_p_CPUTimer_getTimerCount)();
uint32_t CPUTimer_getTimerCount()
{
  return _p_CPUTimer_getTimerCount();
}

void set_p_CPUTimer_getTimerCount(void *f)
{
  _p_CPUTimer_getTimerCount = f;
}

void (*_p_Interrupt_clearACKGroup)();
void Interrupt_clearACKGroup()
{
  return _p_Interrupt_clearACKGroup();
}

void set_p_Interrupt_clearACKGroup(void *f)
{
  _p_Interrupt_clearACKGroup = f;
}

