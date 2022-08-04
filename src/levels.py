from settings import *

LEVELS = [
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 160, 
                        "stage": 1,
                        "color": GREEN,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": HEIGHT,
                     },
            },

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
                     },
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/2, 
                        "y": 160, 
                        "stage": 3,
                        "color": GREEN,
                        "speed_x": 0, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/4, 
                        "y": 100, 
                        "stage": 2,
                        "color": BLUE,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": 3* WIDTH/4, 
                        "y": 100, 
                        "stage": 2,
                        "color": YELLOW,
                        "speed_x": -1 * BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": WIDTH /2 ,
                        "y": HEIGHT,
                     },
            },
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
                        {
                        "x": WIDTH/5 + 1*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": YELLOW,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 2*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": BLUE,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 3*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": YELLOW,
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 4*( 10 + BUBBLE_SIZES[2]), 
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
                     },
            },
        ]

NO_OF_LEVELS = len(LEVELS)
