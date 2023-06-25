#include "stubbed_Ccp.h"
void (*_p_ccpDaq)(uint16 data);
void ccpDaq(uint16 data)
{
  return _p_ccpDaq(data);
}

void set_p_ccpDaq(void *f)
{
  _p_ccpDaq = f;
}

