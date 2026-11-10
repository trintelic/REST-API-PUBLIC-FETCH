# REST-API-PUBLIC-FETCH

This one was a little difficult in terms of managing the error that I ran into. I replicated the steps by creating the file, setting up the environment, and creating the skeleton with only the GET portion. The error that I was receiving had to do with the filter line, and the error stated "TypeError: string indices must be integers, not &#39;str&#39;." I ran into something saying this could be a ComfyUI error, but I was struggling to find a solution to that. I then realized that this is just a different version of k for v.
I then learned that GroupName was not the first key term, and that "Results" was a key that came beforehand.

""Results":[{"DataType":"string","Description":"<p>This field stores any other battery information that does not belong to any of the other battery related fields.<\/p>","GroupName":"Mechanical\/Battery","ID":1,"Name":"Other Battery Info"}" 
In this line, GroupName is within Results, so in order for me to get to GroupName, I have to filter Results first. From what I understand, Results is the first key where the records are the value, and GroupName is the second key, and then "Active Safety System" is the value.
