Courses = {
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=20': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"0"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"1"}
                    }
            }
        }
    },
    'https://snap2perf-sandbox.mrooms.net/course/view.php?id=21': {
        'cover': {"0"},
        'Section': {
            "0": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"0"}
                    }
            },
            "1": {
                'Actions':
                    {
                        'assignment': {"0"},
                        'label': {"1"}
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
