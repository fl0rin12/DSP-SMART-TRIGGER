/*=============================================================================
 *  INCLUDE FILE SECTION
 *===========================================================================*/
/* Include system headers */
/* Include dependent modules headers */
#include "Hfl_Cfg.h"
#include "PFCCtrl.h"
/*=============================================================================
 *  PRIVATE DEFINES
 *===========================================================================*/

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
    HALF_WORDS
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
    WORDS
-------------------------------------*/
/** @cond */
#define START_SEC_CONST_32BIT
#include "MemMap.h"
/** @endcond */
uint32_T Hfl_OperationMode={{_HFL_CAL[_TAG_OPERATIONMODE][0]}};
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
/* This is the only pointer section where the scope can be both local and global.
 * No scope restriction is available here as the pointer will always access the same address
 * when dereferencing.
 */
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

/** Brief description for this non-standard size, post-build configuration constant */

/** @cond */
#define END_SEC_PBCFG
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
{% for idx in _HFL_CAL[_TAG_ITERATOR] %}
real32_T Hfl_DAQCopyVar{{_HFL_CAL[_TAG_ITERATOR][idx]}};
/*
@@ SYMBOL = Hfl_DAQCopyVar{{_HFL_CAL[_TAG_ITERATOR][idx]}}
@@ A2L_TYPE = PARAMETER
@@ DATA_TYPE = FLOAT
@@ DESCRIPTION = "DAQ CopyVar for {{_HFL_CAL[_TAG_ITERATOR][idx]}}'s signal"
@@ END
*/
{%- endfor %}
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
HFLConfigType HflConfig[HFL_MAX_EVENTS] =
{  /*Buffer*/        /*Daq Copy Var*/       /*Signal*/           /*CCPEvent*/
{% for idx in _HFL_CAL[_TAG_ITERATOR] %}
{  {0},                &Hfl_DAQCopyVar{{_HFL_CAL[_TAG_ITERATOR][idx]}},                 (uint32_T)(&{{_HFL_CAL["Signal"][idx]}}),           {{_HFL_CAL["CCPEvent"][idx]}}},
{%- endfor %}

};
/** @cond */
#define END_SEC_VAR_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    POINTER SIZE
 -------------------------------------*/
/* All variables within this section must have qwasi-global scope (STATIC).
 * This offers a series of advangtages:
 *  - isolation of variable
 *  - improved debugability
 *  - avoiding undesired access to memory (ex: racing conditions)
 */
/** @cond */
#define START_SEC_VAR_PTR
#include "MemMap.h"
/** @endcond */

/** Brief description of this non-retaining address of pointer to function variable */

/** Brief description of this non-retaining address of pointer to "Type" constant.
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** Brief description of this non-retaining address of pointer to Type variable
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** @cond */
#define END_SEC_VAR_PTR
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

/** Brief description of this value retaining byte variable
 * This variable will me relocated to the SEC_NOINIT_BSS because
 * it does not receive any value for initialization during startup
 */

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

/** Brief description of this value retaining non-standard size variable
 * This variable will me relocated to the SEC_NOINIT_BSS because
 * it does not receive any value for initialization during startup
 */

/** @cond */
#define END_SEC_VAR_NOINIT_UNSPECIFIED
#include "MemMap.h"
/** @endcond */

/*-------------------------------------
    POINTER SIZE
 -------------------------------------*/
/* All variables within this section must be qwasi-global (STATIC).
 * This offers a series of advangtages:
 *  - isolation of variable
 *  - improved debugability
 *  - avoiding undesired access to memory (ex: racing conditions)
 */
/** @cond */
#define START_SEC_VAR_NOINIT_PTR
#include "MemMap.h"
/** @endcond */

/** Brief description of this address retaining pointer to function variable */

/** Brief description of this address retaining pointer to "Type" constant.
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** Brief description of this address retaining pointer to Type variable
 * Type can be: void, uint8, uint16, uint32, exportedType
 */

/** @cond */
#define END_SEC_VAR_NOINIT_PTR
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
 *  PRIVATE DEFINES
 *===========================================================================*/

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

/** @cond */
#define END_SEC_CODE
#include "MemMap.h"
/** @endcond */
