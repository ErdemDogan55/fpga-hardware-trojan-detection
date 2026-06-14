module golden_top(
    input clk,
    output led0,
    output led1
);

wire r0, r1, r2, r3, r4;
(* KEEP = "TRUE" *) LUT1 #(.INIT(2'b01)) inv0(.I0(r4), .O(r0));
(* KEEP = "TRUE" *) LUT1 #(.INIT(2'b01)) inv1(.I0(r0), .O(r1));
(* KEEP = "TRUE" *) LUT1 #(.INIT(2'b01)) inv2(.I0(r1), .O(r2));
(* KEEP = "TRUE" *) LUT1 #(.INIT(2'b01)) inv3(.I0(r2), .O(r3));
(* KEEP = "TRUE" *) LUT1 #(.INIT(2'b01)) inv4(.I0(r3), .O(r4));

reg [26:0] counter;
always @(posedge clk) counter <= counter + 1;
assign led0 = counter[26];
assign led1 = ~counter[26];

endmodule
