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
	// odeslani zpravy
	[ChatRoomService sendMessage:[inputField stringValue] author:@"Matej"];
	// vycisteni vztupniho pole
	[inputField setStringValue:@""];
}

- (void)checkMessages {
	// kontrola nove zpravy
	Message *message = [ChatRoomService checkMessage:lastSeen];
	// je-li nova zprava
	while (message != nil) {
		// pridani textu zpravy do okna
		[text appendFormat:@"%@: %@\n", message.author, message.text];
		NSAttributedString *attributedString= [[NSAttributedString alloc]
											   initWithString:text];
		[[textView textStorage] setAttributedString:attributedString];
		[attributedString release];
		// ID posledni dosle zpravy
		lastSeen = message.Id;
		[message release];
		// znovu kontrola na nove zpravy
		message = [ChatRoomService checkMessage:lastSeen];
	}
}

@end
