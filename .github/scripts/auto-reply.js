// 独立的 Issue 关键词回复逻辑
module.exports = async ({ github, context }) => {
  // 获取 Issue 标题和内容，并转换为小写以便进行不区分大小写的匹配
  const title = context.payload.issue.title.toLowerCase();
  const body = context.payload.issue.body.toLowerCase();
  const issueNumber = context.payload.issue.number;

  // ⚠️ 预定义的关键词及其对应的随机回复列表
  const keywordMap = {
    入门: "你似乎想要获取算法入门方法？可以先去 leetcode.com 做一些**简单**题目。",
  };

  // 遍历关键词，检查 Issue 标题或内容是否包含它
  for (const keyword in keywordMap) {
    if (title.includes(keyword) || body.includes(keyword)) {
      // 随机选择一个回复
      const responses = keywordMap[keyword];
      const response = responses;

      // 使用 GitHub API 发送评论
      await github.rest.issues.createComment({
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: issueNumber,
        body: `🤖 **自动回复**\n\n${response}`,
      });

      // 找到匹配项后，结束，避免重复回复
      return;
    }
  }

  // 如果没有匹配到任何关键词
  console.log("Issue 未包含预设的关键词，跳过自动回复。");
};
