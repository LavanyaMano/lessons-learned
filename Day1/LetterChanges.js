function LetterChanges(str) { 

  // code goes here  
  var al="abcdefghijklmnopqrstuvwxyz";
  al = al.toLowerCase().split("");
  str = str.toLowerCase().split("");
  for (var i=0;i<str.length;i++){
      if (str[i]==="z"){
          str[i]="A";
      }
      else{
          for (var j=0;j<al.length;j++){
              var flag = true;
              if (str[i]===al[j]){
                  str[i]=al[j+1];
                  flag =false;
              }
            if(flag){
                str[i]=str[i];
            }
          }
          
      }
      for (var a=0;a<str.length;a++){
          switch(str[a]){
              case"e":
                  str[a]="E";
                  break;
                case"i":
                  str[a]="I";
                  break;
                case"o":
                  str[a]="O";
                  break;
                case"u":
                  str[a]="U";
                  break;
                default:
                str[a];
          }
      }
  }
  return str.join(""); 
         
}
   
// keep this function call here 
LetterChanges(readline());  