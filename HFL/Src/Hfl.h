#ifndef HFL_H
/* multiple inclusion protection */
#define HFL_H

/*=============================================================================
 *  INCLUDE FILE SECTION
 *===========================================================================*/
#include "Std_Types.h"
#include "rtwtypes.h"
#include "Hfl_Cfg.h"

/*=============================================================================
 *  EXPORTED FUNCTION MACROS
 *===========================================================================*/

#ifdef HFL_UNIT_TESTING_IS_ON
#define __interrupt
#endif

#define HFL_LOGGER_INIT 0u
#define HFL_LOGGER_STARTED 1u
#define HFL_LOGGER_STOPPED 2u
#define HFL_OPERATION_MODE_MANUAL 1u
#define HFL_OPERATION_MODE_TRIGGERED 2u
/* Transmission rate of CCP messages */
#define HFL_TX_RATE 1u

#define HFL_INTERRUPT_DISABLED 0u
#define HFL_INTERRUPT_ENABLED 1u

#define HFL_READ_FLOAT_FROM_ADDR(addr) (real32_T)(*((real32_T *)addr))
/*=============================================================================
 *  EXPORTED TYPES
 *===========================================================================*/

/*=============================================================================
 *  EXPORTED ROM CONSTANTS
 *===========================================================================*/
/*-------------------------------------
    BYTES
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_8BIT
#include "MemMap.h"
/** @endcond */

/** A brief description for this byte size constant. */

/** @cond */
#define END_SEC_CONST_8BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    HALF-WORDS
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_16BIT
#include "MemMap.h"
/** @endcond */

/** A brief description for this half-word size constant */

/** @cond */
#define END_SEC_CONST_16BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    WORDS
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_32BIT
#include "MemMap.h"
/** @endcond */

/** Brief description for this word size constant */

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

/** Brief description for this non-standard size constant */

/** @cond */
#define END_SEC_CONST_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    POINTER SIZE
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_PTR
#include "MemMap.h"
/** @endcond */

/** Brief description of this constant pointer to function variable */

/** Brief description of this constant address pointer to "Type".
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** @cond */
#define END_SEC_CONST_PTR
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    POST BUILD CONFIGURATION
-------------------------------------*/
/** @cond */
#define START_SEC_PBCFG
#include "MemMap.h"
/** @endcond */

/** Brief description for this non-standard size, post-build configuration "Type" constant
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** @cond */
#define END_SEC_PBCFG
#include "MemMap.h"
/** @endcond */

/*=============================================================================
 *  EXPORTED GLOBAL VARIABLES
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

/** Brief description of this initialized byte variable */

/** @cond */
#define END_SEC_VAR_8BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    HALF-WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_16BIT
#include "MemMap.h"
/** @endcond */

/** Brief description of this initialized half-word variable */

extern volatile uint16_T Hfl_LogState;

/** @cond */
#define END_SEC_VAR_16BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_32BIT
#include "MemMap.h"
/** @endcond */

/** Brief description of this initialized word variable */

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

/** Brief description of this initialized non-standard size variable */

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

/** Brief description of this value retaining byte variable */

/** @cond */
#define END_SEC_VAR_NOINIT_8BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    HALF-WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_16BIT
#include "MemMap.h"
/** @endcond */

/** Brief description of this value retaining half-word variable */

/** @cond */
#define END_SEC_VAR_NOINIT_16BIT
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    WORDS
 -------------------------------------*/
/** @cond */
#define START_SEC_VAR_NOINIT_32BIT
#include "MemMap.h"
/** @endcond */

/** Brief description of this value retaining word variable */

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

/** Brief description of this value retaining non-standard size variable */

/** @cond */
#define END_SEC_VAR_NOINIT_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    CRITICAL DATA STORAGE AREA
 -------------------------------------*/
/** @cond */
#define START_SEC_RAM_CRITICAL
#include "MemMap.h"
/** @endcond */

/** Brief description of this any size protected variable */

/** @cond */
#define END_SEC_RAM_CRITICAL
#include "MemMap.h"
/** @endcond */

/*=============================================================================
 *  EXPORTED DEFINES
 *===========================================================================*/

/*=============================================================================
 *  EXPORTED FUNCTIONS PROTOTYPES
 *===========================================================================*/

/** @cond */
#define START_SEC_CODE
#include "MemMap.h"
/** @endcond */

/** Global functions prototypes */
extern __interrupt void INT_E_PWM8_ISR(void);
extern inline void HFL_HWCFG_STMAN_EPWM_INTERRUPT_BASE_ISR(void);
extern void Hfl_Init(void);
extern void Hfl_MainFunction(void);

/** @cond */
#define END_SEC_CODE
#include "MemMap.h"
/** @endcond */

#endif /* multiple inclusions protection */

/* <<Form No. BUEI-DE-I-017_F2, Revision 1.5, 03/05/16 >>*/
