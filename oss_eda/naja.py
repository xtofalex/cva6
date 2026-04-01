#!/usr/bin/env python3

"""Load the CVA6 SystemVerilog design with NajaEDA."""

import logging
import os

from najaeda import netlist


def _get_log_level() -> int:
  level_name = os.environ.get("NAJA_LOG_LEVEL", "INFO").upper()
  return getattr(logging, level_name, logging.INFO)


logging.basicConfig(
  level=_get_log_level(),
  format="%(asctime)s %(levelname)s %(message)s",
  force=True
)

cva6_repo_dir = os.environ.get("CVA6_REPO_DIR")
if not cva6_repo_dir:
  raise EnvironmentError("CVA6_REPO_DIR environment variable is not set")

svconfig = netlist.SystemVerilogConfig(
  top='cva6',
  flist=os.path.join(cva6_repo_dir, "core", "Flist.cva6"),
  diagnostics_report_path="diags.log"
)

top = netlist.load_system_verilog([], config=svconfig)


dump_config = netlist.VerilogDumpConfig
dump_config.dumpRTLInfosAsAttributes = True
top.dump_verilog("cva6_naja.v", config=dump_config)
