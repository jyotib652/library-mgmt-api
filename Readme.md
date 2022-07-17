
    THE ENDPOINTS ARE:


    'admin/',   -->  to access admin panel for admin user
    'api/auth/user-crud/'  --> to create, retrieve, update & delete users for 'LIBRARIAN' users only
    'api/auth/book/'  --> to create, retrieve, update & delete books for 'LIBRARIAN' users only
    'api/auth/member-only/'  --> to view, borrow, return & update books for 'MEMEBER' users only
    'token-obtain/' -->  to get token for users for authentication purposes
    'api/auth/register/'  --> to register a new user
    'api/auth/get-details/'  --> to get details about the user including token (akin to login)
    'api/auth/delete-own-ac/<uuid:pk>/'  --> to delete a user's own account
    

