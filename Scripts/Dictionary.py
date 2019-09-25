Courses = {
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=51': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"5"},
                        'open_forum': {"0"},
                        'quiz': {"0"},
                        'attendance': {"0"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "2": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "3": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "4": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "5": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            }
        }
    },
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=53': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "2": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "3": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "4": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            },
            "5": {
                'Actions':
                    {
                        'assignment': {"5"},
                        'label': {"5"},
                        'open_forum': {"5"},
                        'quiz': {"5"},
                        'attendance': {"5"}
                    }
            }
        }
    }

}

if __name__ == "__main__":

    for i, j in Courses.items():
        k = Courses[i]["cover"]
        k = int(''.join(k))
        m = Courses[i]["Section"]
        m = int(''.join(m))
        for x, y in Courses[i]["Section"].items():
            p = Courses[i]["Section"][x]["Actions"]["assignment"]
            p = int(''.join(p))
            print(p)
