Diagnostic Event:

The Diagnostic Event Manager (Dem) handles and stores the events detected by diagnostic monitors
A ‘Diagnostic Event’ defines the atomic unit that can be handled by the Dem module.
The status of a ‘Diagnostic Event’ represents the result of a monitor

The Dem module uses the EventId to manage the status of the ‘Diagnostic Event’ of
a system and performs the required actions for individual test results, e.g. stores the
freeze frame.

The Dem module shall represent each Diagnostic Event by an EventId and the related EventName.

Event priority
Event priority is defined as a ranking of events based upon level of importance. It is
used to determine which fault entries may be removed from the event memory in case the 
number of stored events exceeds the maximum number of memory entries.

A priority value of 1 shall be the highest priority. Larger priority
value shall define lower importance.

Event Occurence
The Dem module shall provide an occurrence counter per event memory entry.
The Dem module shall initialize the occurrence counter with
the value one if the related event is entered in the respective event memory.

the Dem module shall increment the occurrence counter by one, triggered by each UDS status 
bit 0 (TestFailed) transition from 0 to 1, if the related event is already stored in the event
memory.  

The Dem module shall not increment the event-specific occurrence counter anymore, if it has reached 
its maximum value 

Event destination
The configuration parameter DemMemoryDestinationRef defines the dedicated storage location(s) of 
the event and its related data The “permanent event memory” assignment is implicitly derived from 
the related DTC


Diagnostic monitor definition
A diagnostic monitor is a routine entity determining the proper functionality of a component. 
This monitoring function identifies a specific fault type (e.g. short to ground, open
load, etc.) for a monitoring path. A monitoring path represents the physical system or a
circuit, that is being monitored (e.g. sensor input). Each monitoring path is associated
with exactly one diagnostic event.


Diagnostic trouble code definition
A ‘Diagnostic trouble code’ defines a unique identifier (shown to the diagnostic tester)
mapped to a ‘Diagnostic event’ of the Dem module. The Dem provides the status of
‘Diagnostic trouble codes’ to the Dcm module

DTC severity
The DTC severity is used to provide information regarding the importance of the specific 
events according to ISO-14229-1[2] “DTC severity and class definition”.
The DemDTCSeverity is only available for UDS DTCs.


Operation Cycle Counters
Cycles since last failed
The counter Cycles since last failed is representing the number of operation cycles
since the DTC fault detection counter last reached its maximum value +127 (since
DTC information was last cleared). All operation cycles, including those during which
the test was not completed shall be included.

If internal debounce counter reach DemDebounceCounterFailedThreshold (latest UDS status bit 0 changes from 0 to 1) and this
counter is not stored in event memory and there are available event memory entry, new entry shall be allocated and the counter shall be started and initialized to
zero

In case the counter is available and started, it shall be incremented at the end of the referenced operation cycle 

The counter shall be implemented as one byte. If any count
operation occurs which would cause a counter to roll over past 0xFF then the count
value shall instead be maintained at 0xFF

Cyles since first failed
The counter Cycles since first failed is representing the number of operation cycles
since the DTC fault detection counter first reached its maximum value of +127 (since
DTC information was last cleared). All operation cycles, including those in which the
test has not been completed shall be included


Failed cycles
The counter Failed cycles is representing the number of operation cycles during which
the DTC fault detection counter reached its maximum value of +127 
(since DTC information was last cleared)

If the counter ‘Failed cycles’ is mapped to an extended data record (DemInternalDataElement 
set to DEM_FAILED_CYCLES), it shall be available per ‘event related data’ record.

If internal debounce counter reach DemDebounceCounterFailedThreshold (latest UDS status bit 0 changes from 0 to 1) and this
counter is not stored in event memory and there are available event memory entry, new entry shall be allocated 
and the counter shall be started and initialized to zero.

In case the counter is available and started, it shall be incremented at the end of the 
referenced operation cycle (refer to DemOperationCycleRef) in case the UDS status bit 1 is set to 1.

The counter shall be implemented as one byte. If any count
operation occurs which would cause a counter to roll over past 0xFF then the count
value shall instead be maintained at 0xFF


Event memory description
The ‘event memory’ is defined as a set of event records located in a dedicated memory block. 
The event record includes at least the UDS status and the event related data.

















