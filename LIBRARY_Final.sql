use library;
create database library;
-- Create the Books table
CREATE TABLE Books (
    location VARCHAR(255),
    book_id VARCHAR(255) PRIMARY KEY, 
    title VARCHAR(255),
    author_id VARCHAR(255), 
    status_of_book VARCHAR(255),
    publisher_id VARCHAR(255) , 
    publication_date DATE,
    category_id VARCHAR(255), 
    number_of_copies INT
);

-- Create the Librarian table
CREATE TABLE Librarian_details (
    id VARCHAR(255) PRIMARY KEY, 
    fname VARCHAR(255),
    lname VARCHAR(255),
    position VARCHAR(255)
);

-- Create the Supplier table
CREATE TABLE Supplier (
    sid VARCHAR(255) PRIMARY KEY, 
    scompany VARCHAR(255),
    fname VARCHAR(255),
    lname VARCHAR(255),
    payment_terms VARCHAR(255),
    delivery_methods VARCHAR(255)
);

-- Create the Category table
CREATE TABLE Category (
	category_id VARCHAR(255), 
    category_name VARCHAR(255),
    description TEXT
);

-- Create the Author table
CREATE TABLE Author (
    author_id VARCHAR(255), 
    fname VARCHAR(255),
    lname VARCHAR(255),
    about TEXT,
    published_work TEXT
);

-- Create the Borrower table
CREATE TABLE Borrower (
    borrower_id VARCHAR(255) PRIMARY KEY, 
    fname VARCHAR(255),
    lname VARCHAR(255),
    fines DECIMAL(10, 2)
);

CREATE TABLE Fines (
	borrower_id VARCHAR(255),
    amount DECIMAL(10, 2),
    due_date VARCHAR(255),
    returned_date VARCHAR(255),
    paid_date varchar(255)
);

-- Create the Publisher table
CREATE TABLE Publisher (
	publisher_id VARCHAR(255), 
    pname VARCHAR(255),
    publishedwork VARCHAR(255)
);

-- Create the Transaction table
CREATE TABLE Transactionss (
    transaction_id VARCHAR(255),
    borrower_id VARCHAR(255), 
    book_id VARCHAR(255), 
    due_date VARCHAR(255),
    returned_date VARCHAR(255)
);

CREATE TABLE Contact (
    contact_id VARCHAR(255),
    contact_details VARCHAR(255)
);

ALTER TABLE Borrower
Drop COLUMN borrowedbook;
SET @@local.net_read_timeout=6;
-- Drop the tables in the reverse order of their creation to avoid foreign key constraints
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Fines;
DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS Borrower;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Supplier;
DROP TABLE IF EXISTS Librarian;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Contact;


ALTER TABLE books DROP COLUMN publication_date;
INSERT INTO Books (location, book_id, title, author_id, availability_status, publisher_id, category_id, number_of_copies)
VALUES
    ('Shelf A1', 'bk001', 'Introduction to Physics', 'A001', 'Available', 'P001', 'C001', 5),
    ('Shelf B2', 'bk002', 'Programming in C++', 'A002', 'Available', 'P002', 'C002', 8),
    ('Shelf C3', 'bk003', 'History of World War II', 'A003', 'Available', 'P003', 'C003', 6),
    ('Shelf D4', 'bk004', 'Data Structures and Algorithms', 'A004', 'Available', 'P002', 'C002', 7),
    ('Shelf A1', 'bk005', 'Chemistry Essentials', 'A005', 'Available', 'P004', 'C004', 4),
    ('Shelf B2', 'bk006', 'Introduction to Psychology', 'A006', 'Available', 'P005', 'C005', 5),
    ('Shelf C3', 'bk007', 'Computer Networks', 'A007', 'Available', 'P006', 'C002', 6),
    ('Shelf D4', 'bk008', 'Art History', 'A008', 'Available', 'P007', 'C006', 3),
    ('Shelf A1', 'bk009', 'Linear Algebra', 'A009', 'Available', 'P008', 'C007', 5),
    ('Shelf B2', 'bk010', 'Literary Classics', 'A010', 'Available', 'P009', 'C008', 4);
    
DELETE FROM Books
WHERE availability_status = 'Not Available';

select * from books;

INSERT INTO Librarian_details (id, fname, lname, position)
VALUES
    ('L001', 'Rahul', 'Sharma', 'Head Librarian'),
    ('L002', 'Priya', 'Patel', 'Assistant Librarian'),
    ('L003', 'Amit', 'Gupta', 'Librarian'),
    ('L004', 'Neha', 'Kumar', 'Library Clerk'),
    ('L005', 'Rajesh', 'Singh', 'Library Clerk');

INSERT INTO Supplier (sid, scompany, fname, lname, payment_terms, delivery_methods)
VALUES
    ('S001', 'BookCo', 'John', 'Smith', 'Net 30', 'Courier'),
    ('S002', 'Textbook World', 'Alice', 'Johnson', 'Net 45', 'Mail'),
    ('S003', 'Publishers Unlimited', 'David', 'Williams', 'Net 60', 'Courier'),
    ('S004', 'Readers Delight', 'Emily', 'Davis', 'Net 30', 'Mail'),
    ('S005', 'Book Nook', 'Michael', 'Brown', 'Net 45', 'Courier');

INSERT INTO Category (Category_id, category_name, description)
VALUES
    ('C001', 'Physics', 'Books related to the study of physics'),
    ('C002', 'Computer Science', 'Books related to computer science and programming'),
    ('C003', 'History', 'Books on various historical topics'),
    ('C004', 'Chemistry', 'Books related to the study of chemistry'),
    ('C005', 'Psychology', 'Books related to the field of psychology'),
    ('C006', 'Art', 'Books on various forms of art'),
    ('C007', 'Mathematics', 'Books related to mathematics'),
    ('C008', 'Literature', 'Books covering classic and contemporary literature');



INSERT INTO Author (author_id, fname, lname, about, published_work)
VALUES
    ('A001', 'Richard', 'Feynman', 'Renowned physicist and Nobel laureate', 'Introduction to Physics'),
    ('A002', 'Bjarne', 'Stroustrup', 'Creator of C++ programming language', 'Programming in C++'),
    ('A003', 'Stephen', 'Ambrose', 'Notable historian and author', 'History of World War II'),
    ('A004', 'Thomas', 'Cormen', 'Computer scientist and co-author of CLRS', 'Data Structures and Algorithms'),
    ('A005', 'Marie', 'Curie', 'Renowned chemist and physicist', 'Chemistry Essentials'),
    ('A006', 'Sigmund', 'Freud', 'Father of psychoanalysis', 'Introduction to Psychology'),
    ('A007', 'Andrew', 'Tanenbaum', 'Computer scientist and author', 'Computer Networks'),
    ('A008', 'Vincent', 'van Gogh', 'Famous Dutch painter', 'Art History'),
    ('A009', 'Gilbert', 'Strang', 'Mathematician and MIT professor', 'Linear Algebra'),
    ('A010', 'William', 'Shakespeare', 'Greatest playwright in English literature', 'Literary Classics');

INSERT INTO Borrower (borrower_id, fname, lname, fines)
VALUES
    ('B001', 'Amit', 'Sharma', 0.00),
    ('B002', 'Rahul', 'Patel', 5.50),
    ('B003', 'Sneha', 'Gupta', 2.25),
    ('B004', 'Rajesh', 'Kumar', 0.00),
    ('B005', 'Neha', 'Singh', 1.75),
    ('B006', 'Vikas', 'Yadav', 0.00),
    ('B007', 'Ritu', 'Verma', 3.75),
    ('B008', 'Pooja', 'Mishra', 0.00),
    ('B009', 'Divya', 'Shukla', 1.50),
    ('B010', 'Sachin', 'Goyal', 0.00);

INSERT INTO Fines (borrower_id, amount, due_date, returned_date, paid_date)
VALUES
    ('B002', 0.00, '2023-10-10','2023-10-08', ''),
    ('B004', 1.00, '2023-10-10','2023-10-11', '2023-10-11'),
    ('B005', 5.00, '2023-10-05','2023-10-10', '2023-10-11'),
    ('B007', 0, '2023-10-15', '2023-11-19', ''),
    ('B009', 4.00, '2023-10-15', '2023-11-19', '2023-10-20');

INSERT INTO Transactionss (transaction_id, borrower_id, book_id, due_date,returned_date)
VALUES
    ('T001', 'B002', 'bk001', '2023-10-10','2023-10-08'),
    ('T002', 'B004', 'bk003', '2023-10-10','2023-10-11'),
    ('T003', 'B007', 'bk005', '2023-10-15','2023-11-15'),
    ('T001', 'B009', 'bk007', '2023-10-15','2023-11-19'),
    ('T005', 'B005', 'bk002', '2023-10-05','2023-10-10');

UPDATE Fines SET amount = amount + (DATEDIFF(returned_date, due_date) * 2.00) WHERE returned_date > due_date;
UPDATE Fines SET amount =0.0;
select * from fines;

UPDATE Fines
SET amount = amount + (CASE WHEN Transactionss.returned_date > Fines.due_date THEN DATEDIFF(Transactionss.returned_date, Fines.due_date) * 2.00 ELSE 0 END)
WHERE borrower_id IN (SELECT borrower_id FROM Transactionss);


UPDATE Fines
SET amount = amount + (DATEDIFF(Transactionss.returned_date, Fines.due_date) * 2.00)
WHERE borrower_id IN (SELECT borrower_id FROM Transactionss WHERE transactions_returned_date > Fines.due_date);



UPDATE Fines
SET amount = amount + (DATEDIFF(Transactionss.returned_date, Fines.due_date) * 2.00)
FROM Fines
JOIN Transactionss ON Fines.borrower_id = Transactionss.borrower_id
WHERE Transactionss.returned_date > Fines.due_date;



INSERT INTO Publisher (publisher_id, pname, publishedwork)
VALUES
    ('P001', 'Pearson', 'Various educational books and materials'),
    ('P002', 'Addison-Wesley', 'Academic textbooks and reference materials'),
    ('P003', 'Simon & Schuster', 'Popular and literary fiction'),
    ('P004', 'Chemical Society', 'Chemistry-related publications'),
    ('P005', 'Psychology Press', 'Psychology books and journals');
    
INSERT INTO Contact (contact_id, contact_details)
VALUES
    ('L001', 'rahulsharma@pes.edu'),
    ('L001', '9876543210'),
    ('L002', 'priyapatel@pes.edu'),
    ('L002', '8551234567'),
    ('L003', 'amitgupta@pes.edu'),
    ('L003', '8779876543'),
    ('L006', 'nehakumar@pes.edu'),
    ('L006', '9764862641'),
    ('L007', 'rajeshsingh@pes.edu'),
    ('L007', '94351002233'),
    ('B001', 'amitsharma@pes.edu'),
    ('B001', '9756483416'),
    ('B002', 'rahulpatel@pes.edu'),
    ('B002', '769843169'),
    ('B003', 'snehagupta@pes.edu'),
    ('B003', '6579134698'),
    ('B004', 'rajeshkumar@pes.edu'),
    ('B004', '6973145894'),
    ('B005', 'nehasingh@pes.edu'),
    ('B005', '9431587642'),
    ('B006', 'vikasyadav@pes.edu'),
    ('B006', '7894531562'),
    ('B007', 'rituverma@pes.edu'),
    ('B007', '6785423969'),
    ('B008', 'poojamishra@pes.edu'),
    ('B008', '8674931598'),
    ('B009', 'divyashukla@pes.edu'),
    ('B009', '9764821579'),
    ('B010', 'sachingoyal@pes.edu'),
    ('B010', '7648546794'),
    ('P001', 'contact@pearson.com'),
    ('P001', '800-123-4567'),
    ('P002', 'contact@addisonwesley.com'),
    ('P002', '800-987-6543'),
    ('P003', 'contact@simonandschuster.com'),
    ('P003', '800-555-1212'),
    ('P004', 'contact@chemicalsociety.com'),
    ('P004', '800-333-3333'),
    ('P005', 'contact@psychologypress.com'),
    ('P005', '800-444-4444'),
    ('S001', 'info@bookco.com'),
    ('S001', '800-111-1111'),
    ('S002', 'info@textbookworld.com'),
    ('S002', '800-222-2222'),
    ('S003', 'info@publishersunlimited.com'),
    ('S003', '800-333-3333'),
    ('S004', 'info@readersdelight.com'),
    ('S004', '800-444-4444'),
    ('S005', 'info@booknook.com'),
    ('S005', '800-555-3223');




SELECT L.id AS librarian_id, L.fname AS first_name, L.lname AS last_name, C.contact_details AS contact_info
FROM Librarian AS L
JOIN Contact AS C ON L.id = C.contact_id;

-- Retrieve data from the Books table
SELECT * FROM Books;

-- Retrieve data from the Librarian table
SELECT * FROM Librarian;

-- Retrieve data from the Supplier table
SELECT * FROM Supplier;

-- Retrieve data from the Category table
SELECT * FROM Category;

-- Retrieve data from the Author table
SELECT * FROM Author;

-- Retrieve data from the Borrower table
SELECT * FROM Borrower;

-- Retrieve data from the Fines table
SELECT * FROM Fines;

-- Retrieve data from the Publisher table
SELECT * FROM Publisher;

-- Retrieve data from the Transaction table
SELECT * FROM Transactionss;

-- Retrieve data from the Contact table
SELECT * FROM Contact;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1Q@z0plm';

ALTER TABLE Fines
ADD CONSTRAINT FK_Fines_Borrower
FOREIGN KEY (borrower_id)
REFERENCES Borrower (borrower_id);

ALTER TABLE Transaction
ADD CONSTRAINT FK_Transaction_Borrower
FOREIGN KEY (borrower_id)
REFERENCES Borrower (borrower_id);

ALTER TABLE Transaction
ADD CONSTRAINT FK_Transaction_Books
FOREIGN KEY (book_id)
REFERENCES Books (book_id);

ALTER TABLE Books
ADD CONSTRAINT FK_Books_Publisher
FOREIGN KEY (publisher_id)
REFERENCES Publisher (publisher_id)
ON DELETE CASCADE;

-- Create a librarian user and grant privileges
CREATE USER 'librarian'@'localhost3000' IDENTIFIED BY 'password';
GRANT INSERT, DELETE, UPDATE ON library.Books TO 'librarian'@'localhost3000';

DELIMITER //
CREATE TRIGGER UpdateFine
AFTER UPDATE
ON Fines FOR EACH ROW
BEGIN
    -- Check if the updated fine amount becomes zero
    IF NEW.amount = 0 THEN
        -- Update the Borrower table to set fines to zero for the same borrower_id
        UPDATE Borrower
        SET fines = 0
        WHERE borrower_id = NEW.borrower_id;
    END IF;
END;
//
DELIMITER ;

UPDATE Fines
SET amount = 0
WHERE borrower_id = 'YourBorrowerID';

DELIMITER //
CREATE PROCEDURE ClearFine(IN borrowerID VARCHAR(255))
BEGIN
    -- Set the fine amount to 0 for the specified borrower
    UPDATE Fines
    SET amount = 0
    WHERE borrower_id = borrowerID;
END;
//
DELIMITER ;
CALL ClearFine('B001');


DELIMITER //
CREATE TRIGGER UpdateBookStatus
BEFORE INSERT ON Transaction
FOR EACH ROW
BEGIN
   DECLARE current_copies INT;
   SELECT number_of_copies INTO current_copies FROM Books WHERE book_id = NEW.book_id;
   IF current_copies = 1 THEN
       SET availability_status = 'Not Available';
   END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE FUNCTION ClearFineFunction(IN borrowerID VARCHAR(255))
RETURNS INT
BEGIN
    -- Initialize a variable to hold the result status
    DECLARE result INT;

    -- Set the fine amount to 0 for the specified borrower
    UPDATE Fines
    SET amount = 0
    WHERE borrower_id = borrowerID;

    -- Check the affected row count
    IF ROW_COUNT() > 0 THEN
        -- Fine cleared successfully
        SET result = 1;
    ELSE
        -- No records were updated (borrower not found)
        SET result = 0;
    END IF;

    -- Return the result status
    RETURN result;
END;
//
DELIMITER ;

SET @result = ClearFineFunction('B001');

IF @result = 1 THEN
    SELECT 'Fine cleared successfully.';
ELSE
    SELECT 'Borrower not found or no fine to clear.';
END IF;

UPDATE Books
SET number_of_copies = number_of_copies - 1,
    availability_status = CASE WHEN number_of_copies - 1 = 0 THEN 'Not Available' ELSE availability_status END
WHERE book_id = 'bk001';

UPDATE Books
SET number_of_copies = number_of_copies + 1,
    availability_status = 'Available'
WHERE book_id = 'bk001';

DELIMITER //
CREATE PROCEDURE BorrowBook(IN bookID VARCHAR(255))
BEGIN
    -- Decrease the number of copies and change availability status when a book is borrowed
    UPDATE Books
    SET number_of_copies = number_of_copies - 1,
        availability_status = CASE WHEN (number_of_copies - 1) = 0 THEN 'Not Available' ELSE 'Available' END
    WHERE book_id = bookID;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ReturnBook(IN bookID VARCHAR(255))
BEGIN
    -- Increase the number of copies and set availability status to 'Available' when a book is returned
    UPDATE Books
    SET number_of_copies = number_of_copies + 1,
        availability_status = 'Available'
    WHERE book_id = bookID;
END;
//
DELIMITER ;

CALL BorrowBook('bk001');
