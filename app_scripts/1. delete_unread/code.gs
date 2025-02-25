<<<<<<< HEAD
function deleteUnreadEmails() {
  // Search for all unread emails in the inbox
  var threads = GmailApp.search('is:unread');
  
  // Log how many threads we found
  Logger.log("Found " + threads.length + " unread threads.");
  
  for (var i = 0; i < threads.length; i++) {
    threads[i].moveToTrash();  
  }
  
  Logger.log('Moved ' + threads.length + ' unread threads to trash.');

  // may show wrong number but works correctly 
}
=======
function deleteUnreadEmails() {
  // Search for all unread emails in the inbox
  var threads = GmailApp.search('is:unread');
  
  // Log how many threads we found
  Logger.log("Found " + threads.length + " unread threads.");
  
  for (var i = 0; i < threads.length; i++) {
    threads[i].moveToTrash();  
  }
  
  Logger.log('Moved ' + threads.length + ' unread threads to trash.');

  // may show wrong number but works correctly 
}
>>>>>>> update
