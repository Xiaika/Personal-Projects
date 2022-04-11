#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <climits>
#include <limits>
#include "functions.h"


/*This function evaluates the shortest path based on set tiebreakers, and colors the pixels it travels to
based on the color parameter then returns the total distance that the path took*/
int colorPath(const int elevations[MAX_ROWS][MAX_COLS], Pixel Image[MAX_ROWS][MAX_COLS], int rows, int cols, Pixel color, int start_row, int start_col)
{
	//Initialize variables
	int pos;
	long int pathUpElevations;
	int pathRightElevations;
	int pathDownElevations;
	int distance = 0;
	int pathRightVal;
	long int pathUpVal;
	long int pathDownVal;
	int col = start_col;
	int row = start_row;
	//Set current position to the elevation value at that element
	pos = elevations[row][col];
	//Loop through all cols except the last one which will be set after the loop
	for (; col < cols-1; col++)					
	{
		/*Initialize paths each time we loop, then get the value
		by subtraacting the path value from the position value and taking
		the absolute value of the result*/
		pathRightElevations = elevations[row][col + 1];
		pathRightVal = abs(pos - pathRightElevations);
		
		/*If our position is at the bottom of the map then we cant go down
		so we set the value to the maximum for integers so that it will
		never be the least of the 3 values and therefore wont be chosen*/
		if (row == rows - 1 )
			pathDownVal = INT_MAX;
		//Otherwise our pathdown is the next row down and the next column over
		else
		{
			pathDownElevations = elevations[row + 1][col + 1];
			pathDownVal = abs(pos - pathDownElevations);
		}
		//If we are at the top of the map, same as before
		if (row == 0)
			pathUpVal = INT_MAX; //Large value so that the path will never be chosen

		//Otherwise our path up is the next row up and one column over
		else
		{
			pathUpElevations = elevations[row - 1][col + 1];
			pathUpVal = abs(pos - pathUpElevations);
		}

		//If tie between right and up or down, go right
		//Set distance to itself plus the new value of the epath we chose
		//Color the current position
		//Set our new position to the path we chose
		if (pathRightVal <= pathDownVal && pathRightVal <= pathUpVal)
		{
			distance += pathRightVal;
			Image[row][col] = color;
			pos = pathRightElevations;
		}
		//If down is smallest or equal to up, go down
		else if (pathDownVal <= pathUpVal)
		{
			distance += pathDownVal;
			Image[row][col] = color;
			pos = pathDownElevations;
			row++;
		}
		//Otherwise up must be smallest so go up
		else 
		{
			distance += pathUpVal;
			Image[row][col] = color;
			pos = pathUpElevations;
			row--;
		}
	}
	//After the loop we want to color our final current position then return total distance
	Image[row][col] = color;
	return distance;
}


/*This function will iterate through every element in our 2D elevations array and if any value is 
greater than the current max, or less than current min, set them to the corresponding values.
Max and min are changed by reference so that ur main function can pass them elsewhere*/
void findMaxMin(const int elevations[MAX_ROWS][MAX_COLS], int rows, int cols, int &max, int &min)
{
	//Initialize max and min to first element in the array
	max = elevations[0][0];
	min = elevations[0][0];
	for (int x = 0; x < rows; x++)
	{
		for (int y = 0; y < cols; y++)
		{
			if (elevations[x][y] > max)
				max = elevations[x][y];
			if (elevations[x][y] < min)
				min = elevations[x][y];
		}
	}
}

/*This function loads our elevation array with all of the values in the file, it will create 
a 2D array from a constant input stream of integers and construct rows and columns corresponding
to what the user enters*/
void loadData(int elevations[MAX_ROWS][MAX_COLS], int rows, int cols, std::istream &inData)
{
	int number;
	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			//Extract the data from the filestream
			inData >> number;
			//If fail bit is set and not end of file, then error.
			/*if (inData.fail())
			{
				if (!inData.eof())
				{
					std::cout << "Error: Read a non-integer value.";
					exit(1);
				}
			}
			//otherwise load the value
			else*/
				elevations[row][col] = number;
		}
	}

}

/*This function Determines our scale value using the given formula
(Value - Min)/(max - min) all times 255
We static cast each variable as a double so as not to lose data if the resulting fracation
is less than one i.e 0.15 is 0 in integers. Then we round the final result to an integer*/
int scaleValue(int value, int max, int min)
{
	double grey_shade = 0;
	grey_shade = 255.0 * ((static_cast<double>(value) - static_cast<double>(min)) / (static_cast<double>(max) - static_cast<double>(min)));
	grey_shade = round(grey_shade);
	return grey_shade;
}

/*Much like loadData this function iterates through all values in our elevations array,
and for each value we will assign a greyscale value to it then use our Pixel class
to assign RGB values all equal to the greyscale*/
void loadGreyscale(Pixel Image[MAX_ROWS][MAX_COLS], const int elevations[MAX_ROWS][MAX_COLS],
	int rows, int cols, int max, int min)
{
	int grey_value;
	int maxVal = max;
	int minVal = min;
	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			//Call scaleValue function for each data point to determine "greyness"
			grey_value = scaleValue(elevations[row][col], maxVal, minVal);
			//Set RGB
			Image[row][col].red = grey_value;
			Image[row][col].blue = grey_value;
			Image[row][col].green = grey_value;
		}
	}
}

/*The outputImage functon iterates through our Image array of objects of the Pixel class 
and creates a PPM file with correct formatting*/
void outputImage(Pixel Image[MAX_ROWS][MAX_COLS], int rows, int cols, std::ostream &outData)
{
	//P3 is the header line in a PPM file
	outData << "P3" << '\n';
	//Second line is number of columns then rows, space delimitted
	outData << cols << ' ' << rows << '\n';
	//Third line is the max color value, in this case 255 which is white
	outData << 255 << '\n';
	for (int row = 0; row < rows; row++)
	{
		for (int col = 0; col < cols; col++)
		{
			//Output Data to the PPM file in RGB format space delimitted
			outData << Image[row][col].red << ' ' << Image[row][col].green << ' ' << Image[row][col].blue << ' ';
		}
	}

}

/*Validates input is an integer*/
int validateInput(int number)
{
	if (number <= 0)
	{
		//If negative number or 0, error
		std::cout << "Error: Problem reading in rows and columns.";
		exit(1);
	}
	/*if fail bit or bad bit set then ouput error 
	I used a while loop because in my version that i keep, i want to actually validate
	input and run a loop that gets a new input until one is valid, i feel it is more
	user friendly and more likely in the real world rather than a single-time check*/

	while(!std::cin.good())
	{
		//Reset stream state
		std::cin.clear();

		//Clear the buffer
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

		std::cout << "Error: Problem reading in rows and columns.";
		//Prompt user to enter a new number for continuous error checking
		//std::cin >> number;
		exit(1);
	}
	return number;
}

/*Validates that the file can be opened correctly and if it can then close the file
and return the correct name to the user*/
std::string validateInput(std::string filename)
{
		//Test that the file opens
		std::ifstream elevationFile(filename);
		std::cout << filename << std::endl;
		if (!elevationFile.is_open())
		{
			std::cout << "Error: Unable to open file " << filename;
			exit(1);
		}

		else
		{
			elevationFile.close();
			return filename;
		}
}

/*This function validates that our input file stream is given all the correct data, while
this may be redundant, I feel for a fast enough program like this, it is better to catch an 
error in a mach version than the actual loadData function, and helps readability*/
int validateInput(int rows, int cols, std::istream &inData)
{

	int number;
	//Counter to detect how many integers are in the file
	int integers = 0;
	while (inData >> number) //While there is something to extract from the file stream, do it
	{
			//If we extract something, it must be an integer so increment our counter
			integers++;
	}
	//If the fail bit is set, then a non integer value was read into the stream
	/* (inData.fail())
	{
		std::cout << "Error: Read a non-integer value.";
	}*/
	//If there are less integers in the file than the maximum of the matrix then error
	if (integers < (rows * cols))
	{
		std::cout << "Error: End of file reached prior to getting all the required data.";
		exit(1);
	}
	//If there are more integers in the file than the maximum of the matrix then error
	if (integers > (rows*cols))
	{
		std::cout << "Error: Too many data points.";
		exit(1);
	}

}
