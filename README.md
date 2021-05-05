# Face Recognition Based Attendance
Using OpenCv,Haar Cascade XML and Python developed a program that uses the face recognition to mark the attendance of the students.

For the face recogntion real time camera is used and face is recognize on the basis of the previously stored images of the students 
along with their names and Unique ID's (in case two students having same name) and storing the images in a seperate folder then 
converting the images to grayscale images and store them in .YAML file in form of array of the Images.

When in recognizing it uses the .YAML file as dataset and mathes with the real time images converting them to the array and matching
them with the array in the .YAML file it crates and opens an EXCEL sheet in which student name and ID is written

# Libraries Used
<ol>
  <li><a href="https://www.python.org/downloads/">Python 3</a></li>
  <li><a href="https://pypi.org/project/opencv-python/">OpenCV</a></li>
</ol>

# Usage
The following command can be used to run the program <code>python Run.py</code>
