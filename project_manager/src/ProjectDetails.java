import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class ProjectDetails {

	// Project attributes, details required when capturing each project
	
	int projectnumber;
	String projectname;
	String buildingtype;
	String projectaddress;
	double projectcost;
	double amountpaid;
	String projectdue;
	String customername;
	ArrayList<String> proj_details 		       = new ArrayList<String>();
	Map<String, ArrayList<String>> project_det = new HashMap<String, ArrayList<String>> ();
	
	// Instantiating the variable which will store all the project details
	
	public ProjectDetails(int projectnumberInput, String projectnameInput,
			String buildingtypeInput,String projectaddressInput,double projectcostInput,
			double amountpaidInput, String projectdueInput, String customernameInput) {
		
		this.projectnumber 	= projectnumberInput;
		this.projectname   	= projectnameInput;
		this.buildingtype 	= buildingtypeInput;
		this.projectaddress = projectaddressInput;
		this.projectcost 	= projectcostInput;
		this.amountpaid		= amountpaidInput;
		this.projectdue		= projectdueInput;
		this.customername	= customernameInput;
	}
	
	// Dictionary method which is used to store user input about the project
	// returns a dictionary with project name as key and ArrayList as the  key value
	// as list with details
	
	public Map<String, ArrayList<String>>  GetProjectDetails(int projectnumberInput, String projectnameInput,
			String buildingtypeInput,String projectaddressInput,double projectcostInput,
			double amountpaidInput, String projectdueInput, String customernameInput) {
		
	
		proj_details.add(String.valueOf(projectnumberInput));
		proj_details.add(buildingtypeInput);
		proj_details.add(projectaddressInput);
		proj_details.add(String.valueOf(projectcostInput));
		proj_details.add(String.valueOf(amountpaidInput));
		proj_details.add(projectdueInput);
		proj_details.add(customernameInput);
		project_det.put(projectnameInput, proj_details);
		
		return project_det;
	}
	
}
