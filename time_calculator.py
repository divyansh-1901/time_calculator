def add_time(start_time,increment,dow=''):
    s = start_time.split() 
    s1 = s[0].split(':')
    if str.lower(s[1])=='am':
        st_24 = (int(s1[0]) * 60) + int(s1[1])
    elif str.lower(s[1])=='pm':
        st_24 = ((int(s1[0])+12) * 60) + int(s1[1])
    i = increment.split(':')
    inc = (int(i[0])*60) + int(i[1])
    end_24_m = st_24 + inc
    hr = int(end_24_m/60)
    m = end_24_m%60
    end_24 = '{}:{}'.format(hr,str(m).rjust(2,'0'))
    
    days = 0
    while hr>=24:
        days= days+1
        hr = hr - 24
    end_12_wo_am_pm = '{}:{}'.format(hr,str(m).rjust(2,'0'))
    n_days = ''
    if days == 1:
        n_days = ' (next day)'
    elif days>1:
        n_days = ' ({} days later)'.format(days)
        
    if hr>12:
        hr = hr - 12
        end = '{}:{} PM'.format(hr,str(m).rjust(2,'0'))
    elif hr==0:
        hr = 12
        end = '{}:{} AM'.format(hr,str(m).rjust(2,'0'))
    elif hr == 12:
        end = '{}:{} PM'.format(hr,str(m).rjust(2,'0'))
    else:
        end = '{}:{} AM'.format(hr,str(m).rjust(2,'0'))
    
    
    
    dows = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if len(dow)>0:
        for i in range(len(dows)):
            if str.lower(dow)==str.lower(dows[i]):
                k = i
                break
        
        i = 0
        while i <= days:
            day = dows[k]
            k = k+1
            i = i+1
            if k==len(dows):
                k = 0 
        end = end + ', {}'.format(day)
    if len(n_days)>0:
        end = end + n_days
    
    return end
