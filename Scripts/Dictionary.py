Courses = {
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=41': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"10"},
                        'label': {"10"},
                        'open_forum': {"10"},
                        'quiz': {"10"},
                        'attendance': {"10"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"10"},
                        'label': {"10"},
                        'open_forum': {"10"},
                        'quiz': {"10"},
                        'attendance': {"10"}
                    }
            }
        }
    },
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=31': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"0"},
                        'open_forum': {"0"},
                        'quiz': {"0"},
                        'attendance': {"0"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"0"},
                        'open_forum': {"0"},
                        'quiz': {"0"},
                        'attendance': {"0"}
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
