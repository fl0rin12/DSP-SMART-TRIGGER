*** Settings ***
Resource          ../../TestEnvironment/Robot_Framework_Resource_Files/stla_obc_it.resource

*** Test Cases ***
SCHM_dependency
    GHOST_CCS_Reset
    GHOST_CCS_Restart    #we reset the software to get the SCHM start of state machine
    obc_ccs_check_fct_call    OsTask_5_ms    #Check if the OsTask_5_ms has been called
    : FOR    ${_run}    IN RANGE    10    #check the functions of the OsTask_5_ms are called in accordance with the sw architecture document
    \    obc_ccs_check_fct_call    IoHwAb_Main_PreApp
    \    obc_ccs_check_fct_call    BTMG_PeriodicFunction
    \    obc_ccs_check_fct_call    HwCfg_MainFunction
    \    obc_ccs_check_fct_call    HwMon_Main_5
    \    obc_ccs_check_fct_call    Meas_MainFunction
    \    obc_ccs_check_fct_call    StMan_MainFunction
    \    obc_ccs_check_fct_call    Com_MainFunctionRX
    \    obc_ccs_check_fct_call    Com_MainFunctionTX
    \    obc_ccs_check_fct_call    Nm_MainFunction
    \    obc_ccs_check_fct_call    ccpBackground
    \    obc_ccs_check_fct_call    IoHwAb_Main_Slow
    \    obc_ccs_check_fct_call    IoHwAb_Main_PostApp
    \    obc_ccs_check_fct_call    ClaIf_MainFunction
    \    obc_ccs_check_fct_call    Hfl_MainFunction

Hfl_period
    GHOST_CCS_Reset
    GHOST_CCS_Restart    #we reset the software to get the SCHM start of state machine
    GHOST_CCS_RunAsynch
    ${min_jitter}    Set Variable    4.75    #5% jitter value
    ${max_jitter}    Set Variable    5.25    #5% jitter value
    ${over_five_percent}    Set Variable    0    #Number of times when the function exceeded 5% jitter. The value needs to be 0
    GHOST_CCS_SetBreakpointAtSymbol    Hfl_MainFunction
    ${period}    obc_ccs_read_period_in_ms    CpuTimer1Regs_TIM    Hfl_MainFunction
    ${exceeded_five_percent_jitter}    obc_ccs_check_jitter_range    ${period}    ${min_jitter}    ${max_jitter}    #Check if the period value exceeded 5%
    GHOSTEqualAsNumbers    ${exceeded_five_percent_jitter}    ${over_five_percent}    #If the period value exceeded 5% fail the test

Hfl_periodity_check
    GHOST_CCS_Reset
    GHOST_CCS_Restart    #we reset the software to get the SCHM start of state machine
    GHOST_CCS_RunAsynch
    GHOST_CCS_SetBreakpointAtSymbol    Hfl_MainFunction
    ${normal_task_period}    Set Variable    5    #Set the actual normal value of task period
    ${counter}    Set Variable    0    #Initialised a counter
    ${under_five_percent_jitter}    Set Variable    4.75    #5% jitter value
    ${over_five_percent_jitter}    Set Variable    5.25    #5% jitter value
    ${over_five_percent}    Set Variable    0    #Number of times when the function exceeded 5% jitter. The value needs to be 0
    ${max_period}    Set Variable    0    #Set a minimum value for calculate the maximum value of period time for n values
    ${min_period}    Set Variable    10000000    #Set a maximum value for calculate the minimum value of period time for n values
    ${max_percent}    Set Variable    0    #Set a minimum value for calculate the maximum value of jitter percente
    ${min_percent}    Set Variable    10000000    #Set a maximum value for calculate the minimum value of jitter percente
    ${max_jitter_percentage_accepted}    Set Variable    5    #Set the maximum value for jitter wich is accpeted
    : FOR    ${index}    IN RANGE    20
    \    ${period}    obc_ccs_read_period_in_ms    CpuTimer1Regs_TIM    Hfl_MainFunction    #Read the value between two reads of a timer
    \    ${dummy_max}    Run Keyword If    ${period}>${max_period}    Set Variable    ${period}    #Check if the period readed is a maximum period and then place into dummy variable or save the previous max value
    \    ...    ELSE    Set Variable    ${max_period}
    \    ${max_period}    Run Keyword IF    ${dummy_max}>${max_period}    Set Variable    ${dummy_max}    #Place the maximum period value into variable else save the previous max value
    \    ...    ELSE    Set Variable    ${max_period}
    \    ${dummy_min}    Run Keyword IF    ${period}<${min_period}    Set Variable    ${period}    #Check if the period readed is a minimum period and then place into dummy variable or save the previous min value
    \    ...    ELSE    Set Variable    ${min_period}
    \    ${min_period}    Run Keyword IF    ${dummy_min}<${min_period}    Set Variable    ${dummy_min}    #Place the minimum period value into variable else save the previous min value
    \    ...    ELSE    Set Variable    ${min_period}
    \    ${exceeded_one_percent_jitter}    obc_ccs_check_jitter_range    ${period}    ${under_five_percent_jitter}    ${over_five_percent_jitter}    #Check if the period readed exceeds a given jitter
    \    ${counter}    Run Keyword If    ${exceeded_one_percent_jitter}>0    Ghost Equation    x[0]+1    ${counter}    #Increment a counter every time when period readed exceeds a given jitter
    \    ...    ELSE    Set Variable    ${counter}
    \    ${rest}    Ghost Equation    x[0]-x[1]    ${normal_task_period}    ${period}    #Calculate the difference between how it should actually be the task period and how it actually is
    \    ${percent}    Ghost Equation    x[0]*100/x[1]    ${rest}    ${normal_task_period}    #Calculate the percent of the jitter from the normal value
    \    ${max_percent}    Run Keyword IF    ${percent}>${max_percent}    Set Variable    ${percent}    #If the percent value which was calculated is a max percent save the percent into a variable else save the previous percent
    \    ...    ELSE    Set Variable    ${max_percent}
    \    ${min_percent}    Run Keyword IF    ${percent}<${min_percent}    Set Variable    ${percent}    #If the percent value which was calculated is a min percent save the percent into a variable else save the previous percent
    \    ...    ELSE    Set Variable    ${min_percent}
    GHOSTEqualAsNumbers    ${counter}    0    #Check if all values was under five jitter percent value
    GHOSTSmallerOrEqual    ${max_period}    ${over_five_percent_jitter}    #Check if max period is under five percent jitter
    GHOSTBiggerOrEqual    ${min_period}    ${under_five_percent_jitter}    #Check if min period is under five percent jitter
    GHOSTSmallerOrEqual    ${max_percent}    ${max_jitter_percentage_accepted}    #Chekc if the max percent is under five
    ${min_percent_positive_number}    Evaluate    abs(${min_percent})
    GHOSTSmallerOrEqual    ${min_percent_positive_number}    ${max_jitter_percentage_accepted}    #Chekc if the min percent is under five

CCP_dependency
    GHOST_CCS_Reset    #we reset the software to get the CCP start of state machine
    GHOST_CCS_Restart
    GHOST_CCS_SetBreakpointAtSymbol    Hfl_Init
    GHOST_CCS_RunAsynch
    ${_breakpoint_adress}    ${time_out}    GHOST_CCS_WaitForHalt
    ${_symbol_adress}    GHOST_CCS_GetSymbolAddress    Hfl_Init
    GHOSTEqualAsIntegers    ${_breakpoint_adress}    ${_symbol_adress}
    GHOST_CCS_RunAsynch
    ${adress}    GHOST_CCS_GetSymbolAddress    Hfl_Isr_State
    ${PAGE}    Evaluate    1
    ${TYPE}    Evaluate    32
    ${valueHfl_Isr_State}    Evaluate    0
    GHOST_CCS_WriteData    ${PAGE}    ${adress}    ${valueHfl_Isr_State}    ${TYPE}
    ${Hfl_Isr_State}    GHOST_CCS_ReadData    ${PAGE}    ${adress}    ${TYPE}
    GhostEqualAsNumbers    ${Hfl_Isr_State}    0
    GHOST_CCS_RunAsynch
    ${adress}    GHOST_CCS_GetSymbolAddress    Hfl_LogState
    ${PAGE}    Evaluate    1
    ${TYPE}    Evaluate    32
    ${valueHfl_LogState}    Evaluate    2
    GHOST_CCS_WriteData    ${PAGE}    ${adress}    ${valueHfl_LogState}    ${TYPE}
    ${Hfl_LogState}    GHOST_CCS_ReadData    ${PAGE}    ${adress}    ${TYPE}
    GhostEqualAsNumbers    ${Hfl_LogState}    2
    GHOST_CCS_RunAsynch
    ${adress}    GHOST_CCS_GetSymbolAddress    Hfl_TxRateIdx
    ${PAGE}    Evaluate    1
    ${TYPE}    Evaluate    32
    ${valueHfl_TxRateIdx}    Evaluate    1
    GHOST_CCS_WriteData    ${PAGE}    ${adress}    ${valueHfl_TxRateIdx}    ${TYPE}
    ${Hfl_TxRateIdx}    GHOST_CCS_ReadData    ${PAGE}    ${adress}    ${TYPE}
    GhostEqualAsNumbers    ${Hfl_TxRateIdx}    1
    GHOST_CCS_RunAsynch
