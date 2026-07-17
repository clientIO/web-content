---
source: https://www.jointjs.com/blog/introducing-jointjs-mcp-server
generated: 2026-07-17
format: markdown
---

We’re excited to introduce the JointJS MCP Server, a tool designed to make your experience with AI assistants (such as Claude Code, Codex, Cursor, Copilot, and more) and JointJS smoother, more productive, and give you higher-quality code.

The MCP server lets your AI assistant access the latest JointJS documentation, API references, and working demo code directly. It uses a smart hybrid search index (combining semantic and keyword search) built from the official JointJS docs and demo repositories. This is updated regularly and optimized to make it easy for AI tools to find exactly what’s needed.

JointJS MCP Server docs:<https://docs.jointjs.com/learn/help-center/mcp-server/>

# Why you should use JointJS MCP Server

When you’re using AI Coding Agents with JointJS, AI Agents kind of guess what you want and how JointJS works, either by building the extensive project index that includes the JointJS library (which is expensive) or relying on their training sets, which might be incomplete, flawed, or skewed, meaning you can get hallucinated APIs, a wrong version of the library, and or other problems.

The JointJS MCP Server solves these problems by giving your AI coding agent direct access to high-quality documentation, code samples, and demo apps created by the JointJS team with best practices in mind.

In short, JointJS MCP Server gives you:

- Always up-to-date documentation, including the latest API changes, deprecation notices, and migration guides, instead of a frozen snapshot from the model's training window.
- Answers for the correct version of the JointJS with fewer hallucinations, and high-quality code rather than random snippets from the web that might not be built according to best practices.
- Reliable code that utilizes existing JointJS APIs and features, which leads to fewer prompts where the AI agent ends up recreating existing features from scratch in a suboptimal and clunky way.

# How to install JointJS MCP Server

Setting it up for your coding agent is quick, easy, and completely free.

The JointJS MCP server is located at:

```
https://mcp.jointjs.com/mcp
```

‍

The documentation walks you through installation for Claude Desktop, Claude Code (CLI), Cursor, VS Code (Copilot), OpenAI Codex / ChatGPT, and other clients. In most cases, you’ll only need to run a single command, add the MCP server endpoint, or update a configuration file.

To add JointJS MCP to Claude Code through CLI, run the following command:

```
claude mcp add jointjs --transport http https://mcp.jointjs.com/mcp
```

‍

This will add JointJS MCP to your current project directory. If you want to make it available everywhere, use the `–scope` user flag:

```
claude mcp add jointjs --transport http https://mcp.jointjs.com/mcp --scope user
```

‍

You can also share the JointJS MCP config with your team via a .mcp.json file checked into the repo:

```
{
	"mcpServers": {
		"jointjs": {
			"type": "http",
			"url": "https://mcp.jointjs.com/mcp"
		}
	}
}
```

‍

This way, the JointJS MCP server will be immediately available for anyone who checks out your repository and starts working with it. After enter Claude in the terminal, new MCP server will be automatically detected:

As a rule of thumb, restart your editor or Coding Agent whenever you add a new MCP Server to ensure everything runs smoothly.

# Tools available in JointJS MCP

AI coding agents and assistants invoke JointJS tools automatically, but you can also invoke them programmatically if you need.

- `search_docs`: Search JointJS documentation, API reference, guides, and migration notes using a natural-language query.
- `get_doc`: Retrieve the full Markdown content of a specific documentation page by its path.
- `search_demos`: Search JointJS demo projects and example code using a natural-language query. Returns a ranked list of demos with demo\_id values you can pass to get\_demo\_code.
- `get_demo_code`: Retrieve all source files of a JointJS demo. Text files (*.ts*, *.tsx*, *.js*, *.jsx*, *.json*, *.md*, *.css*, *.html*) are returned inline; binary assets (fonts, images) are returned as GitHub links.
- `list_doc_versions`: List all JointJS documentation versions available on the server.

# Code quality impact of JointJS MCP

If you use AI Coding Agents with the JointJS MCP, you consistently get code that uses accurate [JointJS](https://www.jointjs.com/) and [JointJS+](https://www.jointjs.com/jointjs-plus) APIs and follows best practices. This leads to code that is not only more maintainable, but also easier to extend and debug in the long run.

Without MCP, AI coding agents often implement custom solutions from scratch, ignoring available JointJS APIs. This results in code that is harder to maintain, can hide subtle bugs, and is much more difficult to scale, especially in enterprise applications where consistency and reliability matter.

In short, if you want high-quality, maintainable JointJS code, especially for larger or enterprise projects, using MCP makes a significant difference over time.

# Conclusion

If you are working with JointJS, using JointJS MCP Server is a no-brainer.

You can install it easily, use it in any AI Coding setup you might have, and you’ll get more maintainable code with higher quality and better architecture.

Happy diagramming!

‍

# FAQs

What is the JointJS MCP Server?

Why should I use JointJS MCP Server with my AI Coding Agent?

Is setting up the JointJS MCP Server difficult?

Where can I find help or documentation for setup and troubleshooting?