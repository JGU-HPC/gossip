cmake_minimum_required(VERSION 3.28 FATAL_ERROR)

add_executable(pararch.gossip.plan_parser PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/plan_parser.cpp")

find_package(nlohmann_json REQUIRED)

target_sources(
	pararch.gossip.plan_parser
	PUBLIC
		FILE_SET HEADERS
		FILES
			"${CMAKE_CURRENT_SOURCE_DIR}/plan_parser.hpp"
)

target_link_libraries(pararch.gossip.plan_parser PRIVATE pararch::gossip nlohmann_json::nlohmann_json)
