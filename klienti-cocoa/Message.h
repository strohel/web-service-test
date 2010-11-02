//
//  Message.h
//  SOAP chat
//
//  Created by Matěj Novotný on 16.10.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface Message : NSObject {
	NSString *author;
	NSString *text;
	int Id;
}

@property (retain) NSString *author;
@property (retain) NSString *text;
@property (assign) int Id;

@end
