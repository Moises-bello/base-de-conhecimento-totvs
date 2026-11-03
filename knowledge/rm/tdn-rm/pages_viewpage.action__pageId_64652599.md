---
content_hash: 39d1c9ee80bb824e992369b48c05f83a0749cda669b717c2ec999e4f0124a9d8
fetched_at: '2026-06-29T00:11:11.442839+00:00'
page_id: '64652599'
product: rm
source: tdn-rm
title: Correção TimeOut Delph e ".Net"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652599
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.52 |
| **Processo** | **:** | Alteração do Time Out |
| **Subprocesso** | **:** | Alteração do Time Out para Telas Delph e .Net |
| **Data da publicação** | **:** | 04/07/2013 |

###### **Definição do Processo**

---

Este documento foi criado para auxiliar o usuário na alteração do “Time Out” nas Rotinas executadas pelo aplicativo RM LIBER.

**1. “Rotinas Desenvolvidas na Tecnologia “.Net”**

**Exemplo: Sped Fiscal, EFD Contribuições etc...**

**• Mensagem apresentada na geração da rotina:**

O framework da TOTVS tem um timeout default de 120 segundos para execução de comandos no banco de dados. Para prevenir erros de timeout, estamos sugerindo aos clientes Gestão Fiscal aumentarem o timeout para 100000 segundos, inserindo a seguinte linha no arquivo **“RM.Host.exe.config”** e**“RM.Host.Service.exe.config”**:

<add key="DBSCommandTimeout" value="100000" />

O arquivo ficará semelhante ao exemplo:

<?xml version="1.0" encoding="utf-8" ?>  
<configuration>  
<appSettings>  
<add key="JobServer3Camadas" value="True" />  
<add key="Port" value="1120" />  
<add key="ActionsPath" value="C:\RM.Net\Bin" />  
<add key="WorkflowEnabled" value="True" />  
<add key="DBSCommandTimeout" value="100000" />  
</appSettings>  
<runtime>  
<NetFx40\_LegacySecurityPolicy enabled="true"/>  
</runtime>  
<startup>  
<supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>  
</startup>  
</configuration>

**Obs.:**

Alterar somente o conteúdo na linha amarela. As outras linhas do arquivo podem variar de acordo com o ambiente do cliente. O serviço deverá ser reiniciado para que a alteração tenha efeito.

**2. “Rotinas Desenvolvidas na Tecnologia “Delph”**

**a)** Exemplo: Sintegra , GIA, DIRF, DACON etc...

Para realiza alteração do Time Out, basta acessar o Painel de Controles | BDE Adminstrator CONNECT TIMEOUT = 7200  TIMEOUT = 7200

Logo após, grave as alterações e reinicie a aplicação:

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.ParamArquConfig.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
