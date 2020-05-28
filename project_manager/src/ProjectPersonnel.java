
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class ProjectPersonnel {
	
//These are the attributes of this class
// These are the personal details of the each object 
// of class Project personnel
	
	String name;
	String email;
	String phonenumber;
	String address;
	ArrayList<String> details_list 					   = new ArrayList<String>();
	Map<String, ArrayList<String>> personalinformation = new HashMap<String, ArrayList<String>>();
	
	
	
	//Instantiating the variables
	
	public ProjectPersonnel(String nameInput, String emailInput,
			String phonenumberInput, String addressInput) {
	
		this.name 			= nameInput;
		this.email  		= emailInput;
		this.phonenumber	= phonenumberInput;
		this.address		= addressInput;
		
		
		
	}
	//This method takes in user input and stores details into a dictionary
	// returns a dictionary with name as key and ArrayList as values
	
	public Map<String, ArrayList<String>> StorePersonnelInfo(String nameInput, String emailInput,
			String phonenumberInput, String addressInput)  {
		
		
		details_list.add(emailInput);
		details_list.add(phonenumberInput);
		details_list.add(addressInput);
		personalinformation.put(nameInput, details_list);
		
		return personalinformation;
	}

	


		
	
		
	}
	


