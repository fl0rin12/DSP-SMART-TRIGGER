#include "stubbed_interrupt.h"
void (*_p_Interrupt_enable)();
void Interrupt_enable()
{
  return _p_Interrupt_enable();
}

void set_p_Interrupt_enable(void *f)
{
  _p_Interrupt_enable = f;
}

void (*_p_Interrupt_disable)();
void Interrupt_disable()
{
  return _p_Interrupt_disable();
}

void set_p_Interrupt_disable(void *f)
{
  _p_Interrupt_disable = f;
}

