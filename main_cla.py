import sys
import DataSchema
# Total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passeddj dhjshd
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")
for i in range(1, n-1):
    print(sys.argv[i], end=" ")
    DataSchema.calling_api()
	
	



