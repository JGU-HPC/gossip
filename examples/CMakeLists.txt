# SPDX-FileCopyrightText: 2026 Markus Vieth <vieth@uni-mainz.de>
# SPDX-FileCopyrightText: 2026 Parallel and Distributed Architectures <hpc@informatik.uni-mainz.de>
#
# SPDX-License-Identifier: BSL-1.0

cmake_minimum_required(VERSION 3.28 FATAL_ERROR)

find_package(clipp REQUIRED)

add_executable(pararch.gossip.execute "${CMAKE_CURRENT_SOURCE_DIR}/execute.cu" "${CMAKE_CURRENT_SOURCE_DIR}/executor.cuh")

target_link_libraries(pararch.gossip.execute PRIVATE pararch::gossip pararch::hpc_helpers clipp::clipp pararch::gossip::plan_parser)

add_executable(pararch.gossip.simulate "${CMAKE_CURRENT_SOURCE_DIR}/simulate.cu" "${CMAKE_CURRENT_SOURCE_DIR}/executor.cuh")

target_link_libraries(pararch.gossip.simulate PRIVATE pararch::gossip pararch::hpc_helpers clipp::clipp pararch::gossip::plan_parser)


