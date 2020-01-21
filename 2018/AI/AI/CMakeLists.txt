#--------------------------------------------------------------------------
# AI project
#--------------------------------------------------------------------------

PROJECT(AI_env)
FILE(GLOB ai_headers code/*.h)
FILE(GLOB ai_sources code/*.cc)

SET(files_ai ${ai_headers} ${ai_sources})
SOURCE_GROUP("ai" FILES ${files_ai})

ADD_EXECUTABLE(AI ${files_ai})

