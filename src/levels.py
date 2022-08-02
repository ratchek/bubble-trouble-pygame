from settings import *

LEVELS = [
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 60, 
                        "stage": 2,
                        "color": BLUE,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": HEIGHT,
                     }
            }
        ]

NO_OF_LEVELS = len(LEVELS)
