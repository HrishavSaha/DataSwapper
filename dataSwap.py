def dataSwap(a,b):
    file_a = open(a, 'r');
    file_b = open(b, 'r');
    print('Files opened. Awaiting reading and swapping...');

    fileData_a = file_a.read();
    fileData_b = file_b.read();
    print('Files read. Awaiting swapping...');

    file_A = open(a, 'w');
    file_B = open(b, 'w');
    file_A.write(fileData_b);
    file_B.write(fileData_a);

    print('File Data have been successfully swapped.');

print("Welcome to the Data Swapping program");
print("Please make sure that both the files are in the same folder as the program");
data_a = input("Please type in the name of the first file (including extension):  ");
data_b = input("Please type in the name of the second file (including extension):  ");

dataSwap(data_a, data_b);