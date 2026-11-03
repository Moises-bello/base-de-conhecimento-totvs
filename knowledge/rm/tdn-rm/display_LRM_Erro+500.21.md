---
content_hash: 1df470b4ab5a60d56d6f4fc1699151a3fad2906c18cc26a382c7cf206d84082d
fetched_at: '2026-06-29T00:05:56.377761+00:00'
page_id: '149882075'
product: rm
source: tdn-rm
title: Erro 500.21
type: documentation
url: https://tdn.totvs.com/display/LRM/Erro+500.21
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework - Web             Versão: 11.5x / 11.8x |
| **Processo** | **:** | RM Portal |
| **Subprocesso** | **:** | *Verificação / Configuração do IIS para correção do erro 500.21* |
| **Data da publicação** | **:** | 23/07/2014 |

**Caso esteja tentando acessar o portal e está se deparando com o erro 500.21.**

**ERRO 500.21** **Handler "PageHandlerFactory-Integrated" has a bad module "ManagedPipelineHandler" in its module list**

Peço por gentileza que siga o procedimento abaixo para corrigir esta inconsistência.

Primeiramente verifique qual a versão do seu Microsoft.NET Framework. Verifique se o mesmo se encontra na versão 4.0.

Segue abaixo um auxílio para verificação da versão:

Clique em Iniciar > Painel de Controle > Programas e recursos > Microsoft .NET Framework 4.0. Caso esteja na versão 4.0, favor seguir o passo a passo abaixo. Caso contrário favor instalar o Microsoft .NET Framework 4.0.

Clique em Iniciar > Painel de Controle > Ferramentas administrativas > Gerenciador do serviços de informações da internet (IIS)

Verificando o pool de aplicativos, favor seguir as setas abaixo (conforme o PRINT) e verificar se o pool de aplicativos está com a versão ASP.NET v4.0. Caso não esteja favor alterar para ASP.NET v4.0.

Para alterar o pool de aplicativos para a ASP.NET v4.0.

clique no ícone    referente a seta 3 (Print acima) irá abrir um Poq up para que seja feita a alteração, após indicar ASP.NET v4.0 clique em OK:

Caso realizou todo o procedimento acima e ainda esta de deparando com o erro 500.21, então devera ativar o IIS (Segue o procedimento abaixo) 

Para ativação do IIS:

Acesse a pasta:

Windows 64BitsC:\Windows\Microsoft.NET**Framework64**\v4.0.30319

Windows 32BitsC:\Windows\Microsoft.NET**Framework**\v4.0.30319

Localize e execute o arquivo: **aspnet\_regiis.exe**

 

**Agora peço por gentileza que abra o browser (Ex: Internet Explorer) e acesse o portal digitando o endereço:**[**http://localhost/corpore.net/Login.aspx**](http://localhost/corpore.net/Login.aspx)

   
 **COMUNIDADE** [**@FRAMEWORK**](https://totvs.byyou.com/?space=rframework)  
  
**Canais** **de** **Atendimento:**   
**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  
**Telefônico:** 4003-0015
