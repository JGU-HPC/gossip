cmake_minimum_required(VERSION 3.28 FATAL_ERROR)

project(
	pararch.gossip
	VERSION 1.0.0
	LANGUAGES CXX CUDA
)

find_package(CUDAToolkit REQUIRED)
find_package(pararch.hpc_helpers REQUIRED)

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
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/broadcast_plan.cpp"
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

target_link_libraries(pararch.gossip INTERFACE CUDA::cudart pararch::hpc_helpers)
add_library(pararch::gossip ALIAS pararch.gossip)

add_subdirectory("${CMAKE_CURRENT_SOURCE_DIR}/plans")

configure_file(
	"CITATION.cff.in"
	"${CMAKE_CURRENT_SOURCE_DIR}/CITATION.cff"
	@ONLY
)


