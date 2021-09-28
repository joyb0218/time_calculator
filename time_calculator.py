import sys
def add_time(start, duration, day=False):

    time = start.split(":", 1)          # ['3', '30 PM']    # "8:16 PM", "466:02" // "6:18 AM (20 days later)"
    time_dur = duration.split(":", 1)   # ['2', '12']
    h = int(time[0])                    # 3
    h_d = int(time_dur[0])              # 2
    days = int(h_d) // 24               # 19 (PM'S)
    days_a = days + 1                   # NEED TO PUT AN "IF" THERE IS 1 MORE DAY
    days_2 = days * 24                  # 456
    days_3 = int(h_d) - days_2          # 10 -- IF 10 + 8 > 12, THEN DAY'S + 1
    days_4 = int(h) + days_3            # 18 -- THIS MINUS 12 GIVES US THE NEW TIME
    days_5 = days_4 - 12                # 6
    time2 = time[1].split(" ")          # ['30', 'PM']
    time2_dur = time_dur[1].split(" ")  # ['12']
    m = int(time2[0])                   # 30
    m_d = int(time2_dur[0])             # 12
    am_pm = time2[1]                    # PM

    if day:
        ind = ["Sunday", "Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay"].index(day)
        count_start = ind
        #days = count_end

        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        k = count_start
        lst1 = week[k:]
        lst2 = week[:k]
        final = lst1 + lst2

    #if days == 7:
        #final = final[0]
    #if days < 7:
        #final = final[days]
    #if days > 7:
        #new_end = days % 7
        #final = final[new_end]


    #/// 1. NO DURATION TIME (00:00) (NO AM/PM CHANGE)
    if h_d == 0 and m_d == 0:
        if m < 10:
            return str(h) + ":" + "0" + str(m) + " " + am_pm
        else:
            return str(h) + ":" + str(m) + " " + am_pm

    #// 2a. SAME DAY (NO AM/PM CHANGE)             "3:30 PM", "2:12" // 5:42 PM
    if m + m_d < 59 and h + h_d < 12:
        if day:
            return str(h + h_d) + ":" + str(m + m_d) + " " + str(am_pm) + ", " + str(day)
        else:
            return str(h + h_d) + ":" + str(m + m_d) + " " + str(am_pm)

    # // 3.  NEXT DAY (AM/PM CHANGE)   "9:15 PM", "5:30"            "8:16 PM", "466:02"
    if m + m_d < 59 and h + h_d > 12:
        h = (h + h_d) - 12
        if am_pm == "PM":
            am_pm = "AM"
        if h_d > 24:                # "8:16 PM", "466:02" // "6:18 AM (20 days later)"
            if days_3 + h > 12:
                days = days + 1
                if day:
                    if days > 7:
                        new_end = days % 7
                        final = final[new_end]
                        return str(days_5) + ":" + str(m + m_d) + " " + str(am_pm) + ", " + str(final) + " (" + str(
                            days) + " days" + " later)"
                if m + m_d < 59:
                    return str(days_5) + ":" + str(m + m_d) + " " + str(am_pm) + " (" + str(days) + " days" + " later)"
        if m < 10:
            return str(h) + ":" + "0" + str(m + m_d) + " " + str(am_pm) + " (next day)"
        else:
            return str(h) + ":" + str(m + m_d) + " " + str(am_pm) + " (next day)"
            sys.exit(0)

    # 2b. SAME DAY (AM/PM CHANGE)  "11:40 AM", "0:25"  // 12:05 PM    "11:55 AM", "3:12"  // "3:07 PM"
    if m + m_d > 59 and h_d == 24:
        h = (h + h_d) + 1 - h_d
        m = (m + m_d) - 60
        if h + h_d == 12:
            if am_pm == "PM":
                am_pm = "AM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + " (2 days later)"
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm) + " (2 days later)"
    if m + m_d > 59 and h + h_d > 12:           # "11:55 AM", "3:12"  // "3:07 PM"
            h = (h + h_d) + 1 - 12
            m = (m + m_d) - 60
            if am_pm == "AM":
                am_pm = "PM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm)
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm)
    if m + m_d > 59 and h + h_d <= 12:       # "11:40 AM", "0:25"  // 12:05 PM
            h = (h + h_d) + 1
            m = (m + m_d) - 60
            if am_pm == "AM":
                am_pm = "PM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm)
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm)

    if h_d == 24 and m_d == 00:         ## // NO MINUTES (24:00) (NO AM/PM CHANGE)  "2:59 AM, Sunday (next day)"
        if day:
            if days < 7:
                final = final[days]
                return str(h) + ":" + str(m) + " " + str(am_pm) + ", " + str(final) + " (next day)"
        else:
            return str(h) + ":" + str(m) + " " + str(am_pm) + " (next day)"

    if h_d == 24 and m_d > 0:                   # "11:59 PM", "24:05"      #// WITH MINUTES (AM/PM CHANGE)
        if am_pm == "PM":
            am_pm = "AM"
        else:
            "AM"
        if day:
            if days < 7:
                if m < 10:
                    final = final[days_a]
                    return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + ", " + str(final) + " (2 days later)"
        if m < 10:
            return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + " (2 days later)"
        else:
            return str(h) + ":" + str(m) + " " + str(am_pm) + " (2 days later)"

    if h_d > 24:                    #"8:16 PM", "466:02" // "6:18 AM (20 days later)"
        if days_3 + h > 12:
            days = days + 1
            if m + m_d < 59:
                return str(days_5) + str(m + m_d) + am_pm + " (" + days + " later)"