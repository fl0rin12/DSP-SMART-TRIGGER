"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""

@istest
def test_Hfl_Init_VerifyThatMemoryIsInitialized():
   '''Test will check if the Memory is initialized correctly with HFL_Init().'''

   Hfl_Init()

   assert(Hfl_LogState.value == 0)
   assert(Hfl_Buffer_Index.value == 0)
   assert(Hfl_SmartTrigger_Index.value == 0)
   assert( Hfl_DaqBuff_Index.value == 0)
   assert(Hfl_StartTs.value == 0)
   assert(Hfl_Isr_State.value == 0)

@istest
def test_Hfl_MFProcessTransmission_LogState_Not_Stopped():
   '''Test will check MainFunction by default'''

   Hfl_Init()
   Hfl_MainFunction()
@istest
def test_Hfl_MFProcessTransmission_LogState_Stopped_And_IsrState_Enabled():
   '''Test will check MainFunction if HFL is stopped and Isr state is enabled'''

   Hfl_Init()
   Hfl_LogState.value=2
   Hfl_Isr_State.value=1
   Hfl_MainFunction()
   assert(Hfl_Isr_State.value == 0)

@istest
def test_Hfl_MFProcessTransmission_LogState_Stopped_And_IsrState_Disabled():
   '''Test will check MainFunction if HFL is stopped and Isr state is disabled'''

   Hfl_Init()
   Hfl_LogState.value=2
   Hfl_Isr_State.value=0
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 0)
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 1)
@istest
def test_Hfl_MFProcessTransmission_LogState_Stopped_And_IsrState_Disabled_And_Buff_Index_Less_than_Max():
   '''Test will check MainFunction if HFL is stopped and Isr state is disabled'''

   Hfl_Init()
   Hfl_LogState.value=2
   Hfl_Isr_State.value=0
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 0)
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 1)
   Hfl_DaqBuff_Index.value=660
   Hfl_MainFunction()
   assert(Hfl_DaqBuff_Index.value == 0)
   assert(Hfl_LogState.value == 0)
@istest
def test_Hfl_MFProcessTransmission_LogState_Stopped_And_IsrState_Disabled_And_Buff_Index_Is_Max():
   '''Test will check MainFunction if HFL is stopped and Isr state is disabled'''

   Hfl_Init()
   Hfl_LogState.value=2
   Hfl_Isr_State.value=0
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 1)
   Hfl_MainFunction()
   assert(Hfl_TxRateIdx.value == 0)
   Hfl_DaqBuff_Index.value=640
   Hfl_MainFunction()
   Hfl_MainFunction()
   assert(Hfl_DaqBuff_Index.value == 641)
   assert(Hfl_Event.value==0)
@istest
def test_Hfl_MainFunctionStartedbyDefault():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_LogState.value=1
   Hfl_MainFunction()
   assert(Hfl_Isr_State.value==1) #test if interrupt was enabled by succes if it s not enabled before
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   Hfl_SmartTrigger.value=1
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode1():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   Hfl_SmartTrigger.value=1
   Hfl_SmartTrigger_Index.value=100
   Hfl_Buffer_Index.value=500
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode7():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   Hfl_SmartTrigger.value=1
   Hfl_SmartTrigger_Index.value=350
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode8():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   Hfl_SmartTrigger.value=1
   Hfl_SmartTrigger_Index.value=350
   Hfl_Buffer_Index.value=25
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode9():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   Hfl_SmartTrigger.value=1
   Hfl_SmartTrigger_Index.value=350
   Hfl_LogState.value=1
   Hfl_Buffer_Index.value=649
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode2():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=1
   Hfl_LogState.value=2
   Hfl_SmartTrigger.value=0
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()

@istest
def test_Hfl_MainFunctionDissableInterrupt():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_Isr_State.value=1
   Hfl_MainFunction()
   assert(Hfl_Isr_State.value == 0)
@istest
def test_Hfl_MainFunctionStartedOperationMode3():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_OperationMode.value=1
   Hfl_LogState.value=2
   Hfl_SmartTrigger.value=0
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode4():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_LogState.value=1
   Hfl_SmartTrigger.value=0
   Hfl_Buffer_Index.value=650
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode5():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_LogState.value=1
   Hfl_SmartTrigger.value=0
   Hfl_Buffer_Index.value=650
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
@istest
def test_Hfl_MainFunctionStartedOperationMode6():
   '''Test will check MainFunction if HFL started mode by default'''

   Hfl_Init()
   Hfl_MainFunction()
   Hfl_LogState.value=1
   Hfl_SmartTrigger.value=0
   Hfl_Buffer_Index.value=650
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
   Hfl_OperationMode.value=2
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()
   Hfl_OperationMode.value=1
   HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR()
   Hfl_MainFunction()