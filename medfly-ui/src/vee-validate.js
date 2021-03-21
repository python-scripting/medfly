import { required, email, max, min } from "vee-validate/dist/rules";
import { extend } from "vee-validate";

extend("required", {
  ...required,
  message: field => '' + field + ' is required.'
});
extend("min", {
  ...min,
  validate(value, args) {
    console.log(args);
    return value.length >= args.length;
  },
  params: ['length'],
  message: `At least {length} characters`
});
extend("max", {
  ...max,
  validate(value, args) {
    //console.log(args);
    return value.length <= args.length;
  },
  params: ['length'],
  message: 'Allow only {length} characters'
});

extend("maxval", {
 
  validate(value, args) {
    //console.log(args);
    return value>=args.length;
  },
  params: ['length'],
  message: 'Min value {length} is required'
});
extend("phonenumber", {
  validate: value => {
  //  console.log(value);
    value = value.replace(/\(/g, '')
    value = value.replace(/\)/g, '')
    value = value.replace(/\/-/g, '')
   // console.log(value);
    if(value.replace(/\s/g,'').length >= 10 && value.replace(/\s/g,'').length <= 12){
      
      return true;
    }else{
      return false;
    }

  },
  message: field => '' + field + ' must be 10 to 12 digits'
});
extend("email", {
  ...email,
  message: "Email address must be a valid email"
});
extend('password', {
  params: ['target'],
  validate(value, { target }) {
    return value === target;
  },
  message: 'Password confirmation does not match'
});
extend('strongpassword', {
  validate:(value)=>{
    //let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{6,})");
    let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&])(?=.{6,})");
    return strongRegex.test(value);
},
message: field => `The `+field+` must contain at least: 1 uppercase, 1 lowercase, 1 number, and one special character`,
  
});

extend('onlyNumbers', {
  validate:(value)=>{
    
    //let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{6,})");
    let strongRegex = new RegExp("^[0-9]+$");
    let rtv = strongRegex.test(value);
    console.log('onlyNumbers ==='+rtv);
    return rtv;
},
message: field => field+` Allow only numbers`,
  
});
//a-zA-Z
extend('Alphanumeric', {
  validate:(value)=>{
    
    //let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{6,})");
    let strongRegex = new RegExp("^[a-zA-Z0-9]*$");
    let rtv = strongRegex.test(value);
   
    return rtv;
},
message: field => field+` Allow Alphanumeric characters`,
  
});
extend('onlyalpha', {
  validate:(value)=>{
    
    //let strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{6,})");
    let strongRegex = new RegExp("^[a-zA-Z]*$");
    let rtv = strongRegex.test(value);
   
    return rtv;
},
message: field => field+` Allow Alphabets characters`,
  
});


extend('radioButton', {
  validate:(value)=>{
    console.log(value);
    return false;
},
message: field => `The `+field+` required`,
  
})

///var validNumber = new RegExp(/^\d*\.?\d*$/);
extend('percentage', {
  validate:(value)=>{
    //var validNumber = new RegExp(/^\d*\.?\d*$/);
    
    if ( value>0 && value<=100  ) {
      return true;
    } else {
      return false;
    }
},
message: field => { 
  console.log(field);
  return `Invalid Percentage`;
},
  
})

extend('zipcodev', {
  getMessage: field =>{ console.log(field+`+ Zipcode not valid`);  return field+`+ Zipcode not valid`} ,
  validate:  (value) => {
    //console.log(value.length+`+ Zipcode not valid`)
   if(value.length ==5 || value.length ==6 ){
    return true;
   }else{
     return false;
   }

    
   
  }
},{ hasTarget: true });



extend('urlvalidation', {
  getMessage: field =>{
    console.log(field);
    return `Invalied url`
  } ,
  validate:  (value) => {
    var res = value.match(/((http|https):\/\/)?[a-zA-Z0-9./?:@\-_=#]+\.([a-zA-Z0-9&./?:@\-_=#])*/g);
    if(res == null)
        return false;
    else
        return true;
    
   
  }
});


extend('confirmpassword', {
  params: ['target'],
  validate(value, { target }) {
    console.log(value + "== ------------- ="+target);
    return value === target;
  },
  message: 'Password confirmation does not match'
});
