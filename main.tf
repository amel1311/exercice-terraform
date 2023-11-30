provider "github" {
  token = "ghp_EuiVgxJP5AZWhWEWZcyjzGiGKq9JA02v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BYgF"
}

resource "github_repository" "exo6" {
  name        = var.exo6
  description = "Created with Terraform"
  visibility     = "public"
}

variable "exo6" {
  description = "exo6"
  type        = string
}