# ----------------------------------
# 通用设置
# ----------------------------------
.PHONY: test go-test python-test clean

# 定义子目录，以便于迭代
SUBDIRS = golang python

# ----------------------------------
# 默认目标：运行所有测试
# ----------------------------------
test: go-test python-test
	@echo "✅ All tests passed successfully."

# ----------------------------------
# Go 测试目标
# ----------------------------------
go-test:
	@echo "--- 🧪 Running Go tests in golang/ ---"
	@cd golang && go test -v ./...

# ----------------------------------
# Python 测试目标
# ----------------------------------
# 假设 Python 项目使用 uv run pytest 命令运行测试
# 如果你使用 poetry run pytest 或 pipenv run pytest，请相应修改
python-test:
	@cd python && uv run pytest

# ----------------------------------
# 清理目标 (可选)
# ----------------------------------
clean:
	@echo "--- 🧹 Cleaning up build artifacts ---"
	@# 清理Go构建缓存
	@go clean -cache
