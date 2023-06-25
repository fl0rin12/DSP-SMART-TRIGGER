/*=============================================================================
 *  INCLUDE FILE SECTION
 *===========================================================================*/
#include "cla_header.h" /* CM variables */
#include "PFCCtrl.h"    /* CM init function */
#include "Ccp.h"
#include "interrupt.h" /* Interrupt ack group definition */
#include "board.h"
#include "epwm.h"
#include "Hfl.h"
#include "Hfl_Cfg.h"
#include "Hfl_Internal.h"
#include "HwCfg_Cfg.h"
/*=============================================================================
 *  LOCAL FUNCTION MACROS
 *===========================================================================*/

/*=============================================================================
 *  LOCAL TYPES
 *===========================================================================*/

/*=============================================================================
 *  ROM CONSTANTS
 *===========================================================================*/
/*-------------------------------------
    BYTES
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_8BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_CONST_8BIT
#include "MemMap.h"
/** @endcond */
/*-------------------------------------
    WORDS
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_16BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_CONST_16BIT
#include "MemMap.h"
/** @endcond */
/*-------------------------------------
    LONGS
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_32BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_CONST_32BIT
#include "MemMap.h"
/** @endcond */
/*-------------------------------------
    UNKNOWN SIZE
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_CONST_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*=============================================================================
 *  RAM VARIABLES
 *===========================================================================*/

/*---------------------------------------------------------
    Initialized and cleared RAM
---------------------------------------------------------*/
/*-------------------------------------
    BYTES
-------------------------------------*/
/** @cond */
#define START_SEC_VAR_8BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_8BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_16BIT
#include "MemMap.h"
/** @endcond */

uint16_T Hfl_Buffer_Index;
uint16_T Hfl_DaqBuff_Index;
uint16_T Hfl_Event;
volatile uint16_T Hfl_TxRateIdx;
volatile uint16_T Hfl_LogState;
/*
@@ SYMBOL = Hfl_LogState
@@ A2L_TYPE = PARAMETER
@@ DATA_TYPE = UWORD
@@ END
*/
volatile uint16_T Hfl_SmartTrigger;
/*
@@ SYMBOL = Hfl_SmartTrigger
@@ A2L_TYPE = PARAMETER
@@ DATA_TYPE = UWORD
@@ END
*/
uint16_T Hfl_Isr_State;

/** @cond */
#define END_SEC_VAR_16BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 LONGS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_32BIT
#include "MemMap.h"
/** @endcond */

volatile uint32_T Hfl_StartTs;
real32_T Hfl_SmartTrigger_Index;

/** @cond */
#define END_SEC_VAR_32BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 UNKNOWN SIZE
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*---------------------------------------------------------
    Non initialized RAM
---------------------------------------------------------*/
/*-------------------------------------
    BYTES
-------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_8BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_NOINIT_8BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_16BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_NOINIT_16BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 LONGS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_32BIT
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_NOINIT_32BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
 UNKNOWN SIZE
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/** @cond */
#define END_SEC_VAR_NOINIT_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*=============================================================================
 *  PRIVATE FUNCTIONS PROTOTYPES
 *===========================================================================*/

/*=============================================================================
 *  INLINE FUNCTIONS
 *===========================================================================*/

/*=============================================================================
 *  FUNCTIONS
 *===========================================================================*/

/** @cond */
#define START_SEC_CODE
#include "MemMap.h"
/** @endcond */

/**
 * Hfl_Init
 *
 * @param   none
 *
 * @return  none
 */
void Hfl_Init(void)
{
    /* Data logger by default should be stopped */
    Hfl_LogState = HFL_LOGGER_INIT;
    /* Init Logger Buffer Index */
    Hfl_Buffer_Index = 0;
    Hfl_SmartTrigger_Index = 0;
    Hfl_DaqBuff_Index = 0;
    Hfl_StartTs = (uint32_T)0;
    Hfl_Isr_State = HFL_INTERRUPT_DISABLED;
    Interrupt_disable(HWCFG_STMAN_EPWM_INTERRUPT_BASE);
}
/**
 * HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR
 *
 * @param   none
 *
 * @return  none
 */
inline void HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR(void)
{

    if (Hfl_OperationMode == HFL_OPERATION_MODE_TRIGGERED)
    {
        /*Log state is started when operation mode is triggered*/
        Hfl_LogState = HFL_LOGGER_STARTED;
    }
    if (HFL_LOGGER_STARTED == Hfl_LogState && Hfl_SmartTrigger == FALSE)
    {
        Hfl_Event = 0;
        if (0 == Hfl_Buffer_Index)
        {
            /* On first index read timestamp */
            Hfl_StartTs = CPUTimer_getTimerCount(CPUTIMER1_BASE);
        }

        if (HFL_LOGGER_BUFFER_SIZE > Hfl_Buffer_Index)
        {
            /*While current buffer index is less than max buffer size read from the signal adress*/
            for (Hfl_Event = 0; Hfl_Event < HFL_MAX_EVENTS; Hfl_Event++)
            {
                HflConfig[Hfl_Event].Hfl_CpuDataLogger[Hfl_Buffer_Index] = HFL_READ_FLOAT_FROM_ADDR(HflConfig[Hfl_Event].Hfl_LogAddr);
            }
            Hfl_Buffer_Index++;
        }
        if (HFL_LOGGER_BUFFER_SIZE == Hfl_Buffer_Index)
        {
            /*if we reach the max size we follow the code flow depending of operation mode*/
            if (Hfl_OperationMode == HFL_OPERATION_MODE_MANUAL)
            {
                Hfl_LogState = HFL_LOGGER_STOPPED;
            }
            else if (Hfl_OperationMode == HFL_OPERATION_MODE_TRIGGERED)
            {
                Hfl_Buffer_Index = 0;
            }
        }
    }
    if (Hfl_SmartTrigger == TRUE)
    {
        if (Hfl_SmartTrigger_Index == 0)
        {
            Hfl_SmartTrigger_Index = Hfl_Buffer_Index;
        }
        /*if the trigger index is less than max buffer size/2 read from the the adress next max buffer size/2 values  */
        if (Hfl_SmartTrigger_Index < ((uint16_T)(HFL_LOGGER_BUFFER_SIZE / 2 + 0.5)))
        {
            if (Hfl_Buffer_Index <= (Hfl_SmartTrigger_Index + (uint16_T)(HFL_LOGGER_BUFFER_SIZE / 2 + 0.5)))
            {
                for (Hfl_Event = 0; Hfl_Event < HFL_MAX_EVENTS; Hfl_Event++)
                { /*store for each signal next buffer size/2 values*/
                    HflConfig[Hfl_Event].Hfl_CpuDataLogger[Hfl_Buffer_Index] = HFL_READ_FLOAT_FROM_ADDR(HflConfig[Hfl_Event].Hfl_LogAddr);
                }
                Hfl_Buffer_Index++;
            }
            else
            {
                Hfl_LogState = HFL_LOGGER_STOPPED;
            }
        }
        else
        {    /*if the trigger index is greate than max buffer size/2
                read from the the adress next max buffer size/2
                values until we reach max buffer size, reset counter
                 and contiune read the difference until we finally
                 read buffer size/2 values */
            if (Hfl_Buffer_Index == (Hfl_SmartTrigger_Index - (uint16_T)(HFL_LOGGER_BUFFER_SIZE / 2 + 0.5)))
            {
                Hfl_LogState = HFL_LOGGER_STOPPED;
                /*Log state will be stoped when we terminate to read the buffer size/2 values*/
            }
            if (Hfl_LogState == HFL_LOGGER_STARTED)
            {
                for (Hfl_Event = 0; Hfl_Event < HFL_MAX_EVENTS; Hfl_Event++)
                {
                    HflConfig[Hfl_Event].Hfl_CpuDataLogger[Hfl_Buffer_Index] = HFL_READ_FLOAT_FROM_ADDR(HflConfig[Hfl_Event].Hfl_LogAddr);
                }
                Hfl_Buffer_Index++;
                if (HFL_LOGGER_BUFFER_SIZE == Hfl_Buffer_Index)
                {
                    Hfl_Buffer_Index = 0;
                }
            }
        }
    }
    EPWM_clearEventTriggerInterruptFlag(EPWM8_BASE);

    /* Acknowledge this interrupt to receive more interrupts from group 3 */
    Interrupt_clearACKGroup(INTERRUPT_ACK_GROUP3);
}
/**
 * Hfl_DisableInterrupt
 *
 * @param   none
 *
 * @return  none
 */
void Hfl_DisableInterrupt(void)
{
    if (HFL_LOGGER_INIT == Hfl_LogState)
    {
        /* Init state */

        /* Stop data sampling when logging is off or init */
        if (HFL_INTERRUPT_ENABLED == Hfl_Isr_State)
        {
            Interrupt_disable(HWCFG_STMAN_EPWM_INTERRUPT_BASE);
            Hfl_Isr_State = HFL_INTERRUPT_DISABLED;
        }
    }
}
/**
 * Hfl_EnableInterrupt
 *
 * @param   none
 *
 * @return  none
 */
void Hfl_EnableInterrupt(void)
{
    if (HFL_LOGGER_STARTED == Hfl_LogState)
    {
        /* When Logging is started we should enable the data sampling interrupt */
        if (HFL_INTERRUPT_DISABLED == Hfl_Isr_State)
        {
            Interrupt_enable(HWCFG_STMAN_EPWM_INTERRUPT_BASE);
            Hfl_Isr_State = HFL_INTERRUPT_ENABLED;
        }
    }
}
/**
 * Hfl_MFProcessTransmission
 *
 * @param   none
 *
 * @return  none
 */
void Hfl_MFProcessTransmission(void)
{

    if (HFL_LOGGER_STOPPED == Hfl_LogState)
    {
        /* Stop data sampling when logging is off or init */
        if (Hfl_Isr_State == HFL_INTERRUPT_ENABLED)
        {
            Interrupt_disable(HWCFG_STMAN_EPWM_INTERRUPT_BASE);
            Hfl_Isr_State = HFL_INTERRUPT_DISABLED;
        }

        if (HFL_TX_RATE == Hfl_TxRateIdx)
        {
            if (HFL_LOGGER_BUFFER_SIZE <= Hfl_DaqBuff_Index)
            {
                /* Data has been transmitted to CCP, reset index and Logger state */
                Hfl_DaqBuff_Index = 0;

                Hfl_LogState = HFL_LOGGER_INIT;
            }
            else
            {
                if (Hfl_Event < HFL_MAX_EVENTS)
                {
                    /* Send Logger data to CCP */
                    *(HflConfig[Hfl_Event].Hfl_DaqCopyVar) = HflConfig[Hfl_Event].Hfl_CpuDataLogger[Hfl_DaqBuff_Index];
                    ccpDaq(HflConfig[Hfl_Event].DAQChannel_State);
                    Hfl_Event++;
                }
                else
                {
                    Hfl_DaqBuff_Index++;
                    Hfl_Event = 0;
                }
            }

            Hfl_TxRateIdx = 0;
        }
        else
        {
            Hfl_TxRateIdx++;
        }
    }
}
/**
 * Hfl_MainFunction
 *
 * @param   none
 *
 * @return  none
 */
void Hfl_MainFunction(void)
{

    Hfl_MFProcessTransmission();
    Hfl_EnableInterrupt();
    Hfl_DisableInterrupt();
}

/* Callout for DAQ timestamp */
uint16_t ccpGetTimestamp()
{
    /* Timestamp handling -> Clock is at 120kHz and sampling is done at 10kHz  */
    uint16_t aux=Hfl_StartTs + (uint32_T)(Hfl_DaqBuff_Index * 12);
    aux=(aux<<8)|(aux>>8);
    return aux;
}

void ccpClearTimestamp()
{
    /* TBD */
}

/** @cond */
#define END_SEC_CODE
#include "MemMap.h" /*lint !e9019 header inclusion after declaration is part of memmory map mechanism*/
/** @endcond */

/* <<Form No. BUEI-DE-I-017_F2, Revision 1.5, 03/05/16 >>*/
