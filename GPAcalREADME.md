### 📊 GPA Calculator
```markdown# GPA Calculator
A simple but complete tool for students to calculate their Grade Point Average. It converts letter grades to numerical values and computes both semester and cumulative GPA.
## What It Does- 
Accepts course grades (A, B+, C-, etc.) and credit hours
Converts letter grades to standard grade points using a lookup table
- Calculates weighted average based on credit hours
- Handles multiple courses and provides clear output
- Includes basic input validation


## Technologies Used- 
**Python**: Core programming language- No external libraries required

## Key Skills Demonstrated-
Dictionary mapping for grade conversion
- Loops and conditional logic
- Weighted average calculations
- Input validation and error handling
- Clean, readable code structure


## Sample Code```
python
# Grade to point conversiondef grade_to_points(grade):    scale = {        'A': 4.0, 'A-': 3.7,        
                                                                           'B+': 3.3, 'B': 3.0,       
                                                                            # ... more grades    }   
return scale.get(grade.upper(), 0.0)
