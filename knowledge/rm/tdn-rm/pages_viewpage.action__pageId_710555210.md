---
content_hash: 0e48f3a2885bf9214373f8f13944cbecbf1f03b4fcf2c7448a6e9da149ead96f
fetched_at: '2026-06-29T00:11:25.534059+00:00'
page_id: '710555210'
product: rm
source: tdn-rm
title: 1 - Criando a Solução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=710555210
version: 5
---

## **Visão geral**

Crie uma nova solução .NET MAUI.

Certifique-se de que o novo nome da solução corresponda ao namespace raiz do aplicativo existente. 

Isso garantirá o mínimo de conflito possível ao importar os componentes existentes.

### Linha de Comando

Em um terminal, execute o seguinte comando para gerar um novo MAUI App:

### Visual Studio 2022

Crie um novo projeto com o modelo padrão .NET MAUI App.

## **Navegando na Solução**

A nova solução será criada e conterá um arquivo **`TotvsApp`**`.sln` que pode ser aberto com o Visual Studio 2022 no Windows ou Mac.

A solução recém-gerada conterá um aplicativo MAUI simples. Os projetos MAUI têm uma nova estrutura, consolidando todos os projetos específicos de plataforma em um único projeto. 

Eles foram movidos para a pasta **`Platforms`**. Ainda é possível escrever código iOS, Android ou Windows e configurações específicas para cada plataforma nesta pasta. 

Em **`Resources`** conterá outros arquivos necessários para o aplicativo, como imagens, fontes, arquivos de banco de dados etc.

## **Compatibilidade entre Plataformas**

Para evitar erros de compilação, remova as plataformas que não são compatíveis com os pacotes do seu Aplicativo no arquivo de projeto (.csproj):

Exemplo

<TargetFrameworks>net6.0-android;net6.0-ios;~~net6.0-maccatalyst~~</TargetFrameworks>

~~<TargetFrameworks Condition="$([MSBuild]::IsOSPlatform('windows'))">$(TargetFrameworks);net6.0-windows10.0.19041.0</TargetFrameworks>~~

<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'ios'">14.2</SupportedOSPlatformVersion>

~~<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'maccatalyst'">14.0</SupportedOSPlatformVersion>~~

<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'android'">21.0</SupportedOSPlatformVersion>

~~<SupportedOSPlatformVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'windows'">10.0.17763.0</SupportedOSPlatformVersion>~~

~~<TargetPlatformMinVersion Condition="$([MSBuild]::GetTargetPlatformIdentifier('$(TargetFramework)')) == 'windows'">10.0.17763.0</TargetPlatformMinVersion>~~
