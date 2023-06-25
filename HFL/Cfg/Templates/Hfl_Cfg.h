#ifndef HFL_CFG_H
#define HFL_CFG_H
/*=============================================================================
 *  INCLUDE FILE SECTION
 *===========================================================================*/
#include "Std_Types.h"
#include "Hfl.h"

/*=============================================================================
 *  EXPORTED FUNCTION MACROS
 *===========================================================================*/
#define HFL_MAX_EVENTS {{len(_HFL_CAL[_TAG_ITERATOR])}}
#define HFL_LOGGER_BUFFER_SIZE {{_HFL_CAL[_TAG_BUFFERSIZE][0]}}
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
extern uint32_T Hfl_OperationMode;
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
typedef struct
{
    real32_T Hfl_CpuDataLogger[HFL_LOGGER_BUFFER_SIZE];/* Circular Buffer to store signal values */
    real32_T *Hfl_DaqCopyVar; /* Copy Var DAQ */
    uint32_T Hfl_LogAddr;/* Signal Address*/
    uint16_T DAQChannel_State;

} HFLConfigType;
extern HFLConfigType HflConfig[HFL_MAX_EVENTS];

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

/** @cond */
#define END_SEC_CODE
#include "MemMap.h"
/** @endcond */

#endif /* multiple inclusions protection */