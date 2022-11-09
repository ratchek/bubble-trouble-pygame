from settings import *

LEVELS = [
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 160, 
                        "stage": 1,
                        "color": "1",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 20,
            },

            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 60, 
                        "stage": 2,
                        "color": "5",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 30,
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/2, 
                        "y": 160, 
                        "stage": 3,
                        "color": "1",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED*2,

                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/4, 
                        "y": 100, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": 3* WIDTH/4, 
                        "y": 100, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": -1 * BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": WIDTH /2 ,
                        "y": GAME_FLOOR,
                     },
            "time": 60,
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 1*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 2*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 3*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 4*( 10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 75,
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 160, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 1*(10 + BUBBLE_SIZES[2]), 
                        "y": 180, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 2*(10 + BUBBLE_SIZES[2]), 
                        "y": 200, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 3*(10 + BUBBLE_SIZES[2]), 
                        "y": 220, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 4*( 10 + BUBBLE_SIZES[2]), 
                        "y": 240, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 75,
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 1*(10 + BUBBLE_SIZES[2]), 
                        "y": 160, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 2*(10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 3*(10 + BUBBLE_SIZES[2]), 
                        "y": 160, 
                        "stage": 2,
                        "color": "4",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 4*( 10 + BUBBLE_SIZES[2]), 
                        "y": 60, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 90,
            },
            {
            "bubbles":[
                        {
                        "x": WIDTH/5, 
                        "y": 240, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 1*(10 + BUBBLE_SIZES[2]), 
                        "y": 220, 
                        "stage": 2,
                        "color": "7",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 2*(10 + BUBBLE_SIZES[2]), 
                        "y": 200, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 3*(10 + BUBBLE_SIZES[2]), 
                        "y": 180, 
                        "stage": 2,
                        "color": "7",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                        {
                        "x": WIDTH/5 + 4*( 10 + BUBBLE_SIZES[2]), 
                        "y": 160, 
                        "stage": 2,
                        "color": "3",
                        "speed_x": BUBBLE_HORIZONTAL_SPEED, 
                        "speed_y": 0,
                        },
                    ],
            "player":{ 
                        "x": 4 * WIDTH /5 ,
                        "y": GAME_FLOOR,
                     },
            "time": 90,
            },
        ]

NO_OF_LEVELS = len(LEVELS)
