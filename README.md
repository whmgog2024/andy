# andy
Pipelined Datapath– Project 3 
Setup
Simulate what happens to data in the registers after each clock cycle
Loop through a set of instructions and then execute the following actions in
sequence:
1. IF - Instruction Fetch
2. ID - Instruction Decode
3. EX - Execute
4. MEM - Memory Access
5. WB - Write Back
6. Print everything
7. Copy Write to Read
First Cycle
IF_stage() - instruction 1 is fetched and written to the IF WRITE object
ID_stage() - method called but nothing happens because there’s no data
EX_stage() - method called but nothing happens because there’s no data
MEM_stage() - method called but nothing happens because there’s no data
WB_stage() - method called but nothing happens because there’s no data
Print_out_everything();
Copy_write_to_read() - instruction 1 is copied to the IF READ object
Second Cycle
IF_stage() - instruction 2 is fetched and written to the IF WRITE object
ID_stage() - IF READ object (which has instruction 1) is accessed and then parameters are
added to the ID WRITE object and then is decoded
EX_stage() - method called but nothing happens because there’s no data
MEM_stage() - method called but nothing happens because there’s no data
WB_stage() - method called but nothing happens because there’s no data
Print_out_everything() - Expect to see instruction 2 in IF WRITE, instruction 1 in IF READ and
ID WRITE and nothing in ID READ
Copy_write_to_read() - instruction 2 is copied to the IF READ object and instruction 1 is copied
to the ID READ object
Approach Step 1
Build your outline of the code first
Main_Mem
Regs
8 objects - Read and Write parameter sets for each instruction
Methods- IF_stage(); ID_stage(); EX_stage(); MEM_stage(); WB_stage();
Print_out_everything(); Copy_write_to_read();
Approach Step 2
Do the easy methods first
● Set up the main method to loop through the instructions
● Initialize Main_Mem and Regs
● Define Print_out_everything method
Approach Step 3
Deep Dive into each stage starting with IF
● Define your object attributes using the Pipeline Handout
○ MEM needs ALU_Result; EX has Reg_Val1 and Reg_Val2
● Add the activities (e.g. decoding the instruction) to the method
○ EX_MEM_WRITE.ALU_Result = ID_EX_READ.Reg_Val1 + ID_EX_READ.Reg_Val2;
● Add logic to copy the objects in your Copy_write_to_read() method
● Add logic to print your objects to the Print_out_everything() method
● TEST YOUR OUTPUT
● Repeat for next stage
Must Haves
Code Review
● Make sure it is easy to find Main Method that calls these methods exactly by name and in this order:
IF_stage(); ID_stage(); EX_stage(); MEM_stage(); WB_stage(); Print_out_everything();
Copy_write_to_read();
● The main memory array is called Main_Mem and the register array is called Regs. No exceptions.
● Use the control bits for each pipeline stage. The MEM_stage should only need to reference the control
bits from the EX_stage. I should not see any instruction decoding in the MEM_stage.
● Make sure the registers get updated (and only at the correct stage).
Output Review
● Print out the Regs AND Read and Write values for all 4 pipeline registers.
● Make sure to print BEFORE the copy method. I must see different values for IF read and IF write.
● All the fields are labeled with the same labels as in the Pipelines handout.
