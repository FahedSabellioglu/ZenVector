use ZenVector



create table Users
(ID int Primary key Identity(1,1),Usr_name varchar(50) not null, Usr_password varchar(255) not null,
email varchar(255) not null unique, Picture varBinary(MAX))

Create table Project
(ID int Primary key IDENTITY(1,1),Project_name varchar(255) not null, creation_time DATETIME DEFAULT GETDATE(),
Usr_Id int not null,unique(Project_name, Usr_Id),
foreign key (Usr_Id) references Users(ID) on delete cascade)

drop table tasks

create table tasks
(Task_name varchar(255) not null, deadline DATETIME not null, descrip varchar(max) not null, Task_status varchar(20) not null,
creation_time DATETIME DEFAULT GETDATE(), Project_ID int,
GivenBy int not null,
foreign key (GivenBy) references Users(ID),
Foreign key (Project_ID) references Project(ID) on delete cascade,
ID int Primary Key Identity(1,1),Unique(Task_name,GivenBY))

create table User_Projects
( Project_ID int not null, ID int not null,
Foreign key (Project_ID) references Project(ID) on delete cascade, 
Foreign key (ID) references Users(ID))

create table Activity
( Usr_Id int not null, Last_Login DATETIME DEFAULT GETDATE(),
foreign key (Usr_Id) references Users(ID) on delete cascade)


create table User_Tasks
(Task_id int not null, Usr_ID int not null,
Unique(Task_id,Usr_ID),
foreign key (Task_id) references tasks(ID) on delete cascade,
foreign key (Usr_ID) references Users(ID))



/* Function for Registering a student, you can either supply a picture or not */
create procedure UserRegister @Usr_name varchar(50), @Usr_password varchar(255), 
@email varchar(255), @Picture varbinary(max)=null
as
begin
	
	if @Picture = null
			insert into Users(Usr_name,Usr_password,email)
			values (@Usr_name,@Usr_password,@email)
	else
			insert into Users(Usr_name,Usr_password,email,Picture)
			values (@Usr_name,@Usr_password,@email,@Picture)

end
Go

/*END */

execute UserRegister @Usr_name = "Fahed", @Usr_password = "1234", @email = "Fahedshaabani@std.sehir.edu.tr";

/*Function to create a project */
create procedure ProjectCreation @Project_name varchar(255), @Usr_email varchar(255)
as
begin

	insert into Project(Project_name,Usr_Id)
	values (@Project_name,(Select ID from Users where email = @Usr_email))

end
go

select * from tasks

/*END */

create procedure TaskCreation @Task_name varchar(255), @Deadline DateTIME, @Descrip varchar(max), @Task_Status varchar(20),
@Project_Name varchar(255), @Usr_email varchar(255)
as
begin
	declare @Usr_ID int;
	select @Usr_ID = ID from Users where email = @Usr_email;
	declare @ProjectID int;
	Select @ProjectID = ID from Project where Project_name = @Project_Name and Usr_Id = @Usr_ID;

	insert into tasks(Task_name,deadline,descrip,Task_status,Project_ID,GivenBy)
	values (@Task_name,@Deadline, @Descrip,@Task_Status,@ProjectID,@Usr_ID)
end
go

select * from Users

execute UserRegister @Usr_name = "Fahed", @Usr_password = "123", @email = "Fahedshaabani@std.sehir.edu.tr"

execute ProjectCreation @Project_name = "New Project", @Usr_email = "Fahedshaabani@std.sehir.edu.tr"

execute TaskCreation @Task_name = "New task", @Deadline = "10/14/2019", @Descrip = "Nothing", @Task_Status = "Active",@Project_Name = "New Project",
@Usr_email="Fahedshaabani@std.sehir.edu.tr"


create procedure AssignTasks @Taskname varchar(255), @leader_email varchar(255), @ToWho_email varchar(255)
as
begin
	declare @taskId int;
	Select @taskId = ID from tasks where Task_name = @Taskname and GivenBy = (Select ID from Users where email = @leader_email);
	insert into User_Tasks(Task_id,Usr_ID)
	values (@taskId,(Select ID from Users where email = @ToWho_email))

end
go

create procedure ProjectDeletion @Project_name varchar(255),@Usr_email varchar(255)
as
begin

	delete from Project
	where Project_name = @Project_name and Usr_Id = (Select ID from Users where email = @Usr_email);

end



create procedure TaskDeletion @Task_name varchar(255), @Usr_email varchar(255)
as
begin
	
	delete from tasks where Task_name = @Task_name and GivenBy = (Select ID from Users where email=@Usr_email);
	
end
go


create procedure DeleteUser @Usr_email varchar(255)
as
begin
	
	delete from Users where email = @Usr_email


end

create procedure RemoveFromTask @Task_name varchar(255), @Usr_email varchar(255), @GivenBy_email varchar(255)
as 
begin
	
	declare @TaskID int;
	Select @TaskID = t.ID from tasks t where t.GivenBy = (Select u.ID from Users u where u.email = @GivenBy_email)
	and t.Task_name = @Task_name

	delete from User_Tasks
	where Task_id = @TaskID
	
end

create procedure ChangeStatus @Task_name varchar(255), @Usr_email varchar(255), @status varchar(20)
as
begin
	update tasks
	set Task_status = @status
	where Task_name = @Task_name
	and GivenBy = (Select ID from Users where email = @Usr_email)
	
end
go


select * from User_Tasks

create procedure AddMember @Task_name varchar(255), @Owner_Email varchar(255), @Usr_email varchar(255)
as
begin
	
	insert into User_Tasks
	values ((Select ID from tasks where Task_name = @Task_name and GivenBy = (Select ID from Users where email = @Owner_Email)),
			(Select ID from Users where email = @Usr_email))



end

create procedure DeleteMemeber @Task_name varchar(255), @Owner_email varchar(255), @Usr_email varchar(255)
as
begin
	
	delete from User_Tasks
	where Task_id = (Select ID from tasks where Task_name = @Task_name and GivenBy = (Select ID from Users where email = @Owner_email))
	and Usr_ID = (Select ID from Users where email = @Usr_email)


end





