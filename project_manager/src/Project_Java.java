import java.util.Scanner;
import javax.swing.JOptionPane;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;

public class Project_Java{
	
	public static void main (String [] args) {
	
	//Initialize dictionaries that will store all user info and project information
	//Initialize the dictionaries that will store the project details
	
	Map<String, ArrayList<String>> clients_dict 		= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> clients_dict_all 	= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> contractor_dict 		= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> contractor_dict_all 	= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> architect_dict		= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> architect_dict_all	= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> all_proj_details 	= new HashMap<String, ArrayList<String>> ();
	Map<String, ArrayList<String>> project_dict			= new HashMap<String, ArrayList<String>> ();
	int landing_menu 			 						= 0;		//Used to exit program
	String y											= "y";		//used to navigate menu
	
	
	//Main menu function using the do and switch function to navigate through options in menu
	
	do
	{
		landing_menu = Integer.parseInt( JOptionPane.showInputDialog( "Welcome to the project manager! What would you like to do?: "
				+ "\n1. Capture new Project Details"
				+ "\n2. Create a contact"
				+ "\n3. Change due date of the Project"
				+ "\n4. Change fee amount paid to date"
				+ "\n5. Update contractor details"
				+ "\n6. Finalise the project"));
	
	switch(landing_menu)
	{
	// Project details menu, takes user input and stores in into dictionary
	
	case 1: System.out.println("Project Details: ");
	Scanner project_data = new Scanner(System.in);
	do {

	System.out.println("Enter project number: ");
	int proj_number 		= Integer.parseInt(project_data.nextLine());

	System.out.println("Enter project name:  ");
	String proj_name		= project_data.nextLine();

	System.out.println("Enter the building type: ");
	String buildtype  		= project_data.nextLine();

	System.out.println("Enter building physical address: ");
	String proj_address 	= project_data.nextLine();
	
	System.out.println("Enter project cost: ");
	double proj_cost 		= Double.parseDouble(project_data.nextLine());
	
	System.out.println("Enter amount paid: ");
	double proj_paid 		= Double.parseDouble(project_data.nextLine());
	
	System.out.println("Project due date: ");
	String proj_duedate 	= project_data.nextLine();
	
	System.out.println("Customer name: ");
	String cus_name 		= project_data.nextLine();
	
	ProjectDetails project	= new ProjectDetails(proj_number, proj_name,
							  buildtype, proj_address, proj_cost,proj_paid,proj_duedate, cus_name);
	
	 project_dict   		= project.GetProjectDetails(proj_number, proj_name, buildtype, 
			                  proj_address, proj_cost,proj_paid,proj_duedate, cus_name);
	
	//All data is stored in this dictionary
	 
	all_proj_details.putAll(project_dict);
	
	//System.out.println(all_proj_details);
	
	System.out.println("Would you like to enter another project? (y/n)");
	 
	} while (project_data.nextLine().equalsIgnoreCase(y));break;

	case 2:
		
		// This section is for creating dictionaries which store all the contact
		// details
		
		Scanner personel_details     = new Scanner(System.in);
		
		do {
			System.out.println("Personal Details: ");
	
			System.out.println("Are you entering details of:"
					+ "\n1. - Client \n2. - Contractor or \n3. - architect"
					+ "\nEnter 1, 2 or 3 ?");
			
			
			int choice 		= Integer.parseInt(personel_details.nextLine());
			
			// Dictionary stores client contact details
			
			if (choice == 1){
				
				System.out.println("Enter name: ");
				String name  		= personel_details.nextLine();

				System.out.println("Enter email address ");
				String email 		= personel_details.nextLine();

				System.out.println("Enter phone number: ");
				String phonenumber  = personel_details.nextLine();

				System.out.println("Enter physical address: ");
				String address 		= personel_details.nextLine();

				ProjectPersonnel client	   	= new ProjectPersonnel(name, email,
						 phonenumber, address);
				
				clients_dict  = client.StorePersonnelInfo(name, email,
						 phonenumber, address);
				
				clients_dict_all.putAll(clients_dict);
			}
			// Dictionary stores contractor details
			
			if (choice == 2) {
				System.out.println("Enter name: ");
				String name  		= personel_details.nextLine();

				System.out.println("Enter email address ");
				String email 		= personel_details.nextLine();

				System.out.println("Enter phone number: ");
				String phonenumber  = personel_details.nextLine();

				System.out.println("Enter physical address: ");
				String address 		= personel_details.nextLine();
				
				ProjectPersonnel contractor = new ProjectPersonnel(name, email,
						 phonenumber, address);
				
				contractor_dict   = contractor.StorePersonnelInfo(name, email,
						 phonenumber, address);
				
				contractor_dict_all.putAll(contractor_dict );
			}
			
			// Dictionary stores architect dictionaries
			
			if (choice == 3){
				
				System.out.println("Enter name: ");
				String name  		= personel_details.nextLine();

				System.out.println("Enter email address ");
				String email 		= personel_details.nextLine();

				System.out.println("Enter phone number: ");
				String phonenumber  = personel_details.nextLine();

				System.out.println("Enter physical address: ");
				String address 		= personel_details.nextLine();
				
				ProjectPersonnel architect 	= new ProjectPersonnel(name, email,
						 phonenumber, address);
				
				architect_dict   = architect.StorePersonnelInfo(name, email,
						 phonenumber, address);	
				
				architect_dict_all.putAll(architect_dict );
				
			}
			
		
			 System.out.println("Would you like to enter another contact? y/n");
		
		} while (personel_details.nextLine().equalsIgnoreCase(y));break;
		
	case 3: 
		
	//editing function, edits the project due date using indexing
		
	Scanner edit_proj 		    = new Scanner(System.in);
	do{
	
	System.out.println("Edit Project Due Date");
	System.out.println("Enter project number you would like to edit: ");
	String project_name 		= edit_proj.nextLine();
	
	System.out.println("Enter new due date of the Project");
	String new_duedate 			= edit_proj.nextLine();
	
	if (all_proj_details.containsKey(project_name)) {
		
	all_proj_details.get(project_name).set(5,new_duedate );
	} 
	
	
	}while (edit_proj.nextLine().equalsIgnoreCase(y));break;
	
	

	case 4:
	// Edits the amount to be paid using indexing
		
	Scanner edit_amount   = new Scanner(System.in);
	
	do{	
	
	System.out.println("Change fee amount paid to date");	
	System.out.println("Which project do you want to edit");
	String project_name   = edit_amount.nextLine();
			
	System.out.println("Enter new amount due");
	String new_amount 	  = edit_amount.nextLine();
			
	if (all_proj_details.containsKey(project_name)) {
				

		all_proj_details.get(project_name).set(4,new_amount);
		} 
				
   System.out.println(all_proj_details);
	
   } while (edit_amount.nextLine().equalsIgnoreCase(y));break;
		
	case 5:
		
	//Edits the contractor dictionary using indexing
		
	System.out.println("Update contractor details");
	Scanner edit_contractor = new Scanner(System.in);
	
	do{
	System.out.println("Name of contractor you want to edit: ");
	String contractor_name   = edit_contractor.nextLine();
				
	System.out.println("What would you like to edit?"
				+ "\n1. Change email"
				+ "\n2. Change phone number"
				+ "\n3. Change address");
		
	int choice_ = Integer.parseInt(edit_contractor.nextLine());
		
		if (choice_ == 1) {
		
		System.out.println("Enter new email");
		String new_email = edit_contractor.nextLine();
		
		if (contractor_dict_all.containsKey(contractor_name )) {
			
			contractor_dict_all.get(contractor_name ).set(0,new_email);
			}
		}
		if (choice_ == 2){
			
		System.out.println("Enter new phone number: ");
		String new_phone = edit_contractor.nextLine();
			
		if (contractor_dict_all.containsKey(contractor_name )) {
				
			contractor_dict_all.get(contractor_name).set(1,new_phone);
			}
		}
		
		if (choice_ == 3) {
			
		System.out.println("Enter new physical addreess: ");
		String new_address = edit_contractor.nextLine();
				
		if (contractor_dict_all.containsKey(contractor_name)) {
					
		contractor_dict_all.get(contractor_name).set(2,new_address);
				}
		}
		
					
	   //System.out.println(contractor_dict_all);
	
			  
	
	} while (edit_contractor.nextLine().equalsIgnoreCase(y));break;
	
	case 6:
		
	// Prints out all projects with outstanding balance
	
	System.out.println("Finalise the project: ");
	
	Scanner final_proj = new Scanner(System.in);
	
	do{
	
	for (String key: all_proj_details.keySet()) {
		
		// outstanding balance
		
		double fees_due = Double.parseDouble(all_proj_details.get(key).get(3)) - Double.parseDouble(all_proj_details.get(key).get(4));
		
		String client_name = all_proj_details.get(key).get(5); // Client name in stored
															   // project_details dictionary
		
		if (fees_due != 0) {
			
		System.out.println("This is the invoice for the project " + key);
		System.out.println("Project number: " 		   + all_proj_details.get(key).get(0));
		System.out.println("Building type: " 		   + all_proj_details.get(key).get(1));
		System.out.println("Project completion date: " + all_proj_details.get(key).get(2));
		System.out.println("Total project cost: " 	   + all_proj_details.get(key).get(3));
		System.out.println("Amount paid " 		   	   + all_proj_details.get(key).get(4));
		System.out.println("Amount owing: "		  + "" + fees_due);
		
		for (String details: clients_dict_all.keySet()) {
			
			if(clients_dict_all.containsKey(client_name)){
			
				System.out.println("Customer name: " 	+ details);
				System.out.println("Email: " 			+ clients_dict_all.get(details).get(0));
				System.out.println("Phone number: " 	+ clients_dict_all.get(details).get(1));
				System.out.println("Physical address: " + clients_dict_all.get(details).get(2));
			}
		}
		}
		else System.out.println("Payment for this project is complete.");
		
	}
	System.out.println("Get back to main menu(y/n): ");
	
	}while (final_proj.nextLine().equalsIgnoreCase(y));break;
	
	
	default: System.out.println( "Please enter a number between 1 and 6, or 0 to quit" );break;
	
	
	}		
	
	}while (landing_menu != 0);
	}
}



				
		
	


	 
	  
	

	 
	 
	
	


