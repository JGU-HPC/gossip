# SPDX-FileCopyrightText: 2026 Markus Vieth <vieth@uni-mainz.de>
# SPDX-FileCopyrightText: 2026 Parallel and Distributed Architectures <hpc@informatik.uni-mainz.de>
#
# SPDX-License-Identifier: BSL-1.0

cmake_minimum_required(VERSION 3.28 FATAL_ERROR)

project(
	pararch.gossip
	VERSION 1.0.0
	LANGUAGES CXX CUDA
)

find_package(CUDAToolkit REQUIRED)
find_package(pararch.hpc_helpers REQUIRED)
find_package(CCCL REQUIRED)

add_library(pararch.gossip INTERFACE)
target_sources(
	pararch.gossip
	INTERFACE
		FILE_SET HEADERS
		BASE_DIRS
			"include"
		FILES
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/all_to_all.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/all_to_all_async.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/all_to_all_plan.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/broadcast.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/broadcast_plan.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/common.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/config.h"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/context.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/error_checking.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/gather.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/gather_plan.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/gossip.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/memory_manager.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/multisplit.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/point_to_point.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/scatter.cuh"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/scatter_plan.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/transfer_plan.hpp"
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/utils.cuh"
)

set_target_properties(
	pararch.gossip
	PROPERTIES
		VERIFY_INTERFACE_HEADER_SETS ON
)

target_link_libraries(pararch.gossip INTERFACE CUDA::cudart pararch::hpc_helpers CCCL::CCCL)
add_library(pararch::gossip ALIAS pararch.gossip)

install(
	TARGETS pararch.gossip
	COMPONENT pararch.gossip
	EXPORT pararch.gossip
	FILE_SET HEADERS
)

add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/plan_parser")
add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/examples")

