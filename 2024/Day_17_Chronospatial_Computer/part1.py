class Cpu:
    def __init__(self, reg_a: int, reb_b: int, reg_c: int, program: list[int]):
        self._opcodes = program[::2]
        self._operands = program[1::2]
        self._reg_a = reg_a
        self._reg_b = reb_b
        self._reg_c = reg_c
        self._ip = 0
        self._iteration = 0
        self._output = list()


    def adv(self):
        numerator = self._reg_a
        denominator = 2**self.get_combo_operand()
        self._reg_a = numerator // denominator

    def bxl(self):
        self._reg_b = self._reg_b ^ self.get_literal_operand()

    def bst(self):
        self._reg_b = self.get_combo_operand() % 8

    def jnz(self) -> int:
        if self._reg_a == 0:
            return self._ip + 1
        return self.get_literal_operand() // 2

    def bxc(self):
        self._reg_b = self._reg_b ^ self._reg_c

    def out(self):
        self._output.append(self.get_combo_operand() % 8)

    def bdv(self):
        numerator = self._reg_a
        denominator = 2 ** self.get_combo_operand()
        self._reg_b = numerator // denominator

    def cdv(self):
        numerator = self._reg_a
        denominator = 2 ** self.get_combo_operand()
        self._reg_c = numerator // denominator

    def get_combo_operand(self) -> int:
        op = self._operands[self._ip]
        match op:
            case 0|1|2|3: return op
            case 4: return self._reg_a
            case 5: return self._reg_b
            case 6: return self._reg_c
            case 7: raise ValueError(f'The program is ill-formed. 7 can not be an combo operand')

    def get_literal_operand(self) -> int:
        return self._operands[self._ip]

    def run(self):
        while self._ip < len(self._opcodes):
            op = self._opcodes[self._ip]
            next_ip = self._ip + 1
            match op:
                case 0: self.adv()
                case 1: self.bxl()
                case 2: self.bst()
                case 3: next_ip = self.jnz()
                case 4: self.bxc()
                case 5: self.out()
                case 6: self.bdv()
                case 7: self.cdv()

            self._ip = next_ip
            self._iteration += 1

    def get_output(self) -> str:
        return ','.join(map(str, self._output))

    def get_iterations_count(self) -> int:
        return self._iteration



def main():
    with open('input.txt') as input_file:
        reg_a = int(input_file.readline().split()[-1])
        reg_b = int(input_file.readline().split()[-1])
        reg_c = int(input_file.readline().split()[-1])
        input_file.readline()
        program = list(map(int, input_file.readline().split()[1].split(',')))

    cpu = Cpu(reg_a, reg_b, reg_c, program)
    cpu.run()

    print(f'Iterations: {cpu.get_iterations_count()}')
    print(f'Output: {cpu.get_output()}')



if __name__ == '__main__':
    main()