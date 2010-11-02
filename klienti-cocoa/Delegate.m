//
//  SOAP_chatAppDelegate.m
//  SOAP chat
//
//  Created by Matěj Novotný on 16.10.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "Delegate.h"


@implementation Delegate

@synthesize window;

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
	if (text == nil) {
		text = [[NSMutableString alloc] initWithString:@""];
	}
	lastSeen = 0;
	[NSTimer scheduledTimerWithTimeInterval:2.0
									 target:self
								   selector:@selector(checkMessages)
								   userInfo:nil
									repeats:YES];
}

- (IBAction)send:(id)sender {
	[ChatRoomService sendMessage:[inputField stringValue] author:@"Matej"];
	[inputField setStringValue:@""];
}

- (void)checkMessages {
	Message *message = [ChatRoomService checkMessage:lastSeen];
	while (message != nil) {
		[text appendFormat:@"%@: %@\n", message.author, message.text];
		NSAttributedString *attributedString= [[NSAttributedString alloc]
											   initWithString:text];
		[[textView textStorage] setAttributedString:attributedString];
		[attributedString release];
		lastSeen = message.Id;
		[message release];
		message = [ChatRoomService checkMessage:lastSeen];
	}
}

@end
