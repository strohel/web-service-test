//
//  SOAP_chatAppDelegate.h
//  SOAP chat
//
//  Created by Matěj Novotný on 16.10.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import <Foundation/Foundation.h>
#import "ChatroomService.h"

@interface Delegate : NSObject <NSApplicationDelegate> {
    NSWindow *window;
	IBOutlet NSTextView *textView;
	IBOutlet NSTextField *inputField;
	NSMutableString *text;
	int lastSeen;
}

@property (assign) IBOutlet NSWindow *window;


- (IBAction)send:(id)sender;

@end
