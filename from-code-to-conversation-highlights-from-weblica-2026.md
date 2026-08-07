---
source: https://www.jointjs.com/blog/from-code-to-conversation-highlights-from-weblica-2026
generated: 2026-08-07
format: markdown
---

A few weeks ago, I had the pleasure of attending Weblica, a fantastic local conference that covers a wide range of tech topics, with a focus on web development. It took me a little while to process everything I experienced, but I’m excited to finally share my thoughts.

## About Weblica

What stood out to me most at Weblica wasn’t just the talks themselves, but the exchanges with fellow developers, speakers, and attendees. Unsurprisingly, AI was a hot topic, and almost every talk and conversation touched on it in some way.

We discussed how AI is transforming our development workflows and changing our approach to development. I also had the chance to talk about JointJS, share excitement about our upcoming JointJS for React, and share ideas with others who were just as excited about the future of web tech.

What follows are a few key takeaways and random thoughts from the sessions and chats I had.

## Key takeaways

- **AI in the dev workplace is fundamental today.** Some teams have strict guidelines for using AI, while others are still figuring things out as they go. My observation? The general consensus devs share is that at least a bit of structure is helpful. You don’t want to just accept everything AI suggests; code requests and revisions should be handled thoughtfully to avoid blindly trusting the machine.
- A common assumption is that **using AI in coding makes you faster and more productive**. But what I found interesting is that some teams aren’t using AI to get more done, but instead to improve the quality of what they ship. As one developer shared, their delivery estimates didn’t change after adopting AI, but the quality of their code did, with emphasis on tests, documentation, and code comments. AI Coding Agents can free up dev time and make these important (but often tedious) tasks much more manageable.
- Of course, many developers are still very skeptical of using AI, and **some companies have strict policies against incorporating AI into their code, usually due to concerns related to privacy and security**. Developers sometimes go around those restrictions by sharing only approximate data or manually integrating AI-generated code without granting agents access to their codebase. If you're building AI tools, keep in mind that not everyone is comfortable sending private code to remote servers, so offering tokenization in your MCP Server, for example, can go a long way toward alleviating those concerns.
- I heard some funny stories, too. For example, **a few developers admitted that when they hit the usage limits on their AI tools, they just take a break and wait for their quota to reset**, stating that manual coding is simply too slow and feels like a waste of time. While that’s an extreme example, it does highlight just how much we’re beginning to rely on AI coding assistants. If you’re working on a tool, framework, or library for developers, ensure it’s optimized for AI Coding Agents and delivers high-quality code suggestions. Otherwise, you will get left behind.
- **A lot of focus in AI workflows these days is on agent handoffs, multi-agent orchestrations, and MCP Servers.** I was more than excited to share that we have already shipped the JointJS MCP Server, which helps developers get higher-quality JointJS code from their coding agents.
- Another thing that kept coming up in presentations and conversations was the importance of visualization. Developers who rely only on chat boxes for AI workflows are missing out. **Visualization tools like diagrams can make working with AI clearer, more user-friendly, and even enjoyable**, which is precisely the segment where JointJS shines.
- **The more you know about AI, the better you can work around its issues and sidestep potential problems.** For example, when using AI to generate unit or integration tests, awareness that AI only has access to your code, or rather to the internals of your code, means that generated tests will be tightly coupled to the code, and you’ll test implementation details. This means you’ll have to rewrite your tests every time you refactor the code. On the flip side, AI does an amazing job at code refactoring if you have a solid test suite in place.
- If you’re building products today, first and foremost, **design for humans** and focus on creating the best possible user experience. Second, make sure they work well with AI agents, especially if you’re building tools for developers. If your library can’t be used effectively by AI coding agents, developers might, or rather probably will, switch to alternatives. (By the way, JointJS works great with AI, so if you’re creating diagrams or using AI in your workflow, definitely give it a try, especially with our JointJS MCP Server.)

## Conclusion

As I mentioned at the start, the greatest value I got from Weblica was connecting with other developers and sharing our experiences. And I wasn’t alone. Almost everyone I talked to felt the same way. If you’re organizing a conference, I’d suggest longer breaks between talks or even shorter talks overall. Developers can get technical information directly from social media, blogs, YouTube, or even AI, but what they crave from conferences is the interpersonal connection. Maybe this is a side effect of more remote work and more and more automatically generated content, but it’s clear that in-person networking and conversation are more valuable than ever.

Attending Weblica was a really rewarding and fulfilling experience. I loved talking with developers, business owners, and speakers, and I recommend you join us next year. You’ll learn about the latest development trends, and more importantly, you’ll get to meet some amazing, friendly people.

‍