import Vue from 'vue'
import moment from 'moment'
//import * as _ from "lodash";

import { parsePhoneNumberFromString } from 'libphonenumber-js'
const formatter = new Intl.NumberFormat("en-US", {
	style: "currency",
	currency: "USD",
	minimumFractionDigits: 2
  });

Vue.filter('capitalize', function (value) {
	if (!value) return ''
	value = value.toString()
	let arr = value.split(" ")
	let capitalized_array = []
	arr.forEach((word) => {
		let capitalized = word.charAt(0).toUpperCase() + word.slice(1)
		capitalized_array.push(capitalized)
	})
	return capitalized_array.join(" ");
})

Vue.filter('truncate', function (value, limit) {
	return value.substring(0, limit)
})

Vue.filter('tailing', function (value, tail) {
	return value + tail;
})


Vue.filter('formatDateTime', function (value) {
	if (value) {
		return moment(String(value)).format('MMM DD, YYYY hh:mm A')
	}
}
)
Vue.filter('formatDateDM', function (value) {
	if (value) {
		return moment(String(value)).format('MMM DD')
	}
}
)
Vue.filter('formatPhone', function (value) {
	if (value) {
		const phoneNumber = parsePhoneNumberFromString(value)
		if(phoneNumber){
		return phoneNumber && phoneNumber.formatInternational()

		}
		return value.replace(/(\d{3})(\d{3})(\d{4})/,"($1)$2-$3");

	}
}
)

Vue.filter('empty', function (value) {
	if (value == null) {
		return "--";
	}
	return value;
}
)
Vue.filter('addressformat', function (value) {
	var address = '';
	if (value.line1) address = value.line1;
	if (value.line2 && value.line2 !=null && value.line2 !='') address = address + ', ' + value.line2 ;
	if (value.locationDetails) address = address + '<br/>'+ value.locationDetails.name;
	if (value.stateDetails) address = address + ', ' + value.stateDetails.name + '<br/>';
	if (value.countryDetails) address = address + value.countryDetails.name;
	if (value.zipcode) address = address + ', ' + value.zipcode;
	return address;
}
)


Vue.filter('addformat', function (value) {
	var address = [];
	if(value.location && value.location.name !=null  && value.location.name !='') address.push(value.location.name);
	if(value.state && value.state.name !=null  && value.state.name !='') address.push(value.state.name);
	if(value.country && value.country.name !=null  && value.country.name !='') address.push(value.country.name);
	if(address.length == 0) return null;
	address = address.join(', ')
	return address;
}
)


Vue.filter('formatDate', function (value) {
	if (value) {
		return moment.utc(value).format('MMM DD, YY')
	}
}
)


Vue.filter('time', function (value, is24HrFormat = false) {
	if (value) {
		const date = new Date(Date.parse(value));
		let hours = date.getHours();
		const min = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes()
		if (!is24HrFormat) {
			const time = hours > 12 ? 'AM' : 'PM';
			hours = hours % 12 || 12;
			return hours + ':' + min + ' ' + time
		}
		return hours + ':' + min
	}
})

Vue.filter('date', function (value, fullDate = false) {
	value = String(value)
	const date = value.slice(8, 10).trim();
	const month = value.slice(4, 7).trim();
	const year = value.slice(11, 15);

	if (!fullDate) return date + ' ' + month;
	else return date + ' ' + month + ' ' + year;
})

Vue.filter('month', function (val, showYear = true) {
	val = String(val)

	const regx = /\w+\s(\w+)\s\d+\s(\d+)./;
	if (!showYear) {
		return regx.exec(val)[1];
	} else {
		return regx.exec(val)[1] + ' ' + regx.exec(val)[2];
	}

})

Vue.filter('csv', function (value) {
	return value.join(', ')
})

Vue.filter('filter_tags', function (value) {
	return value.replace(/<\/?[^>]+(>|$)/g, "")
})

Vue.filter('k_formatter', function (num) {
	return num > 999 ? (num / 1000).toFixed(1) + 'k' : num
});

Vue.filter('timeago', function (value) {
	if (value) {
		return moment(String(value)).fromNow()
	}
}
)

Vue.filter('formatprice', function (amount) {
	if (amount) {
		return formatter.format(amount);
	}
})

Vue.filter('getTwolatters', function(items) {
// alert(items);
	if (items) {
	let str_arr = items.split(" ");
	if(str_arr.length>=2){
		return str_arr[0].charAt(0)+str_arr[1].charAt(0);

	}else{
		return items.charAt(0)+items.charAt(1);

	} 
		
	}
})
