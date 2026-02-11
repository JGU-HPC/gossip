# SPDX-FileCopyrightText: 2026 Markus Vieth <vieth@uni-mainz.de>
# SPDX-FileCopyrightText: 2026 Parallel and Distributed Architectures <hpc@informatik.uni-mainz.de>
#
# SPDX-License-Identifier: BSL-1.0

cmake_minimum_required(VERSION 3.28 FATAL_ERROR)

add_library(pararch.gossip.plan_parser "${CMAKE_CURRENT_SOURCE_DIR}/plan_parser.cpp")

find_package(nlohmann_json REQUIRED)

target_sources(
	pararch.gossip.plan_parser
	PUBLIC
		FILE_SET HEADERS
		BASE_DIRS
			include
		FILES
			"${CMAKE_CURRENT_SOURCE_DIR}/include/gossip/plan_parser.hpp"
)


target_link_libraries(pararch.gossip.plan_parser PRIVATE pararch::gossip nlohmann_json::nlohmann_json)
add_library(pararch::gossip::plan_parser ALIAS pararch.gossip.plan_parser)

install(
	TARGETS pararch.gossip.plan_parser
	COMPONENT pararch.gossip.plan_parser
	EXPORT pararch.gossip.plan_parser
	FILE_SET HEADERS
)
