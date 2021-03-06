template = """
{
  "packagingVersion": "4.0",
  "upgradesFrom": ["{{upgrades-from}}"],
  "downgradesTo": ["{{downgrades-to}}"],
  "minDcosReleaseVersion": "1.9",
  "name": "%(template)s",
  "version": "{{package-version}}",
  "maintainer": "support@YOURNAMEHERE.COM",
  "description": "YOURNAMEHERE on DC/OS",
  "selected": false,
  "framework": true,
  "tags": ["%(version)s", "%(template)s"],
  "postInstallNotes": "DC/OS YOURNAMEHERE is being installed!\\n\\n\\tDocumentation: {{documentation-path}}\\n\\tIssues: {{issues-path}}",
  "postUninstallNotes": "DC/OS YOURNAMEHERE is being uninstalled."
}
"""
