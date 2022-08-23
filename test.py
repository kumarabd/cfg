contents = """
always_comb
  begin
    if (AXI_DATA_WIDTH == 64)
    begin
      case (word_size_i)
        4'h1:
          begin
            if(addr_i[2:0] == 3'b000)      be_dec = 8'b00000001;
            else if(addr_i[2:0] == 3'b001) be_dec = 8'b00000010;
            else if(addr_i[2:0] == 3'b010) be_dec = 8'b00000100;
            else if(addr_i[2:0] == 3'b011) be_dec = 8'b00001000;
            else if(addr_i[2:0] == 3'b100) be_dec = 8'b00010000;
            else if(addr_i[2:0] == 3'b101) be_dec = 8'b00100000;
            else if(addr_i[2:0] == 3'b110) be_dec = 8'b01000000;
            else                           be_dec = 8'b10000000;
          end
        4'h2:
          begin
            if(addr_i[2:1] == 2'b00)       be_dec = 8'b00000011;
            else if(addr_i[2:1] == 2'b01)  be_dec = 8'b00001100;
            else if(addr_i[2:1] == 2'b10)  be_dec = 8'b00110000;
            else                           be_dec = 8'b11000000;
          end
        4'h4:
          begin
            if(addr_i[2] == 1'b0)          be_dec = 8'b00001111;
            else                           be_dec = 8'b11110000;
          end
        4'h8:                              be_dec = 8'b11111111;
        default:                           be_dec = 8'b11111111;  // default to 64-bit access
      endcase
    end
    else if (AXI_DATA_WIDTH == 32)
    begin
      case (word_size_i)
        4'h1:
          begin
            if(addr_i[1:0] == 2'b00)       be_dec = 4'b0001;
            else if(addr_i[1:0] == 2'b01)  be_dec = 4'b0010;
            else if(addr_i[1:0] == 2'b10)  be_dec = 4'b0100;
            else                           be_dec = 4'b1000;
          end
        4'h2:
          begin
            if(addr_i[1] == 1'b0)          be_dec = 4'b0011;
            else                           be_dec = 4'b1100;
          end
        4'h4:
                                           be_dec = 4'b1111;
        4'h8:
                                           be_dec = 4'b1111;  //error if it happens
        default:                           be_dec = 4'b1111;  // default to 32-bit access
      endcase // word_size_i
    end
  end"""