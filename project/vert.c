#version 330 core

layout (location = 0) in vec3 glVertex;
layout (location = 1) in vec3 glNormal;
layout (location = 2) in vec2 glTexCoord;

out vec4 oGlNormal;
out vec2 oGlTexCoord;
out vec4 oLightPos;

uniform mat4 mPerspective;
uniform mat4 mView;
uniform mat4 mModel;

uniform vec4 vLightPos;

void main() 
{
    mat4 transormation = mPerspective * mView * mModel;
    gl_Position = transormation * vec4(glVertex, 1.0);
    oGlNormal   = transormation * vec4(glNormal, 1.0);
    oGlTexCoord = glTexCoord;
    oLightPos = mPerspective * mView * vLightPos;
}