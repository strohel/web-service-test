//
//  Message.m
//  SOAP chat
//
//  Created by Matěj Novotný on 16.10.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "Message.h"


@implementation Message

@synthesize author;
@synthesize text;
@synthesize Id;

- (void)dealloc {
	[author release];
	[text release];
	[super dealloc];
}

- (NSString *)description {
	return [NSString stringWithFormat:@"%@: %@", self.author, self.text];
}

@end
