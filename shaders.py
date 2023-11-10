# shaders.py
vertexShader = """
#version 330 core

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec2 aTexCoord;
layout(location = 2) in vec3 aNormal;

out vec2 UV;
out vec3 FragPos;
out vec3 Normal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    UV = aTexCoord;
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
}
"""

fragmentShader = """
#version 330 core

in vec2 UV;
in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

uniform sampler2D ourTexture;

void main()
{
    // Fragment shader code for basic rendering
    vec3 color = texture(ourTexture, UV).rgb;
    FragColor = vec4(color, 1.0);
}
"""

customShader1 = """
#version 330 core

in vec2 UV;
in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

uniform sampler2D ourTexture;

void main()
{
    // Toon shading
    vec3 lightDir = normalize(vec3(1.0, 1.0, 1.0));
    float diff = max(dot(Normal, lightDir), 0.0);
    float intensity = smoothstep(0.2, 1.0, diff);

    vec3 color = texture(ourTexture, UV).rgb;
    FragColor = vec4(color * intensity, 1.0);
}
"""

customShader2 = """
#version 330 core

in vec2 UV;
in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

uniform sampler2D ourTexture;

void main()
{
    // Cel shading
    vec3 lightDir = normalize(vec3(1.0, 1.0, 1.0));
    float diff = max(dot(Normal, lightDir), 0.0);
    float intensity = smoothstep(0.2, 1.0, diff);

    if (intensity > 0.8)
        intensity = 1.0;
    else if (intensity > 0.5)
        intensity = 0.8;
    else if (intensity > 0.2)
        intensity = 0.5;
    else
        intensity = 0.2;

    vec3 color = texture(ourTexture, UV).rgb;
    FragColor = vec4(color * intensity, 1.0);
}
"""

customShader3 = """
#version 330 core

in vec2 UV;
in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

uniform sampler2D ourTexture;

void main()
{
    // Escala de grises con bordes resaltados
    vec3 color = texture(ourTexture, UV).rgb;
    float grayscale = (color.r + color.g + color.b) / 3.0;

    float edge = fwidth(grayscale);
    float threshold = 0.5;
    float outline = smoothstep(threshold - edge, threshold + edge, grayscale);

    FragColor = vec4(mix(vec3(outline), color, 0.7), 1.0);
}
"""
