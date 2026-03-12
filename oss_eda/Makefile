YOSYS=/Users/xtof/WORK/yosys/install/bin/yosys
export CVA6_REPO_DIR=/Users/xtof/WORK/cva6
export HPDCACHE_DIR=${CVA6_REPO_DIR}/core/cache_subsystem/hpdcache"
export TARGET_CFG="cv64a6_imafdc_sv39"

all:
	${YOSYS} -l yosys.log -v 10 -c yosys.ys
	
najaeda:
	python3 naja.py
