#version 330 core

layout (location = 0) out vec4 fragColor;

in vec4 oGlNormal;
in vec2 oGlTexCoord;
in vec4 oLightPos;

uniform sampler2D tex;

void main() 
{
    fragColor = texture(tex, oGlTexCoord);
    fragColor.rgb *= dot(normalize(oGlNormal.xyz), oLightPos.xyz)*0.5;
}










