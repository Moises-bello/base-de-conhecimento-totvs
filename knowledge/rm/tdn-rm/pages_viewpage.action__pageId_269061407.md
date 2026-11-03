---
content_hash: 8af15377b9af987542a79fd38ada918d5b8ca1efddd2fa2e196ea0d00199efba
fetched_at: '2026-06-29T00:08:21.587389+00:00'
page_id: '269061407'
product: rm
source: tdn-rm
title: RMFIS00001_Correção TimeOut Delphi e ".Net"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269061407
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.X |
| **Ocorrência:** | Alteração do Time Out para Telas Delphi e .Net |
| **Ambiente:** |  |
| **Passo a passo:** | Este documento foi criado para auxiliar o usuário na alteração do “Time Out” nas Rotinas executadas pelo aplicativo RM LIBER.    **1. “Rotinas Desenvolvidas na Tecnologia “.Net”**  **Exemplo: Sped Fiscal, EFD Contribuições etc...**  **• Mensagem apresentada na geração da rotina:**    O framework da TOTVS tem um timeout default de 120 segundos para execução de comandos no banco de dados.  Para prevenir erros de timeout, sugerimos aos clientes  aumentarem este tempo limite para 100000 segundos, inserindo a seguinte linha nos arquivo: **“RM.Host.exe.config”**,**“RM.Host.Service.exe.config” e "*RM.Host.JobRunner.exe.config*"**:  Estes arquivos encontram-se no caminho abaixo: C: | TOTVS | CORPORERM | RM.NET |      Assim deverá ser acrescentada a linha abaixo:  ***<add key="DBSCommandTimeout" value="100000" />***    Após inserir a linha o arquivo ficará da seguinte forma. Segue um exemplo semelhante:  <?xml version="1.0" encoding="utf-8" ?> <configuration> <appSettings> <add key="JobServer3Camadas" value="True" /> <add key="Port" value="1120" /> <add key="ActionsPath" value="C:\RM.Net\Bin" /> <add key="WorkflowEnabled" value="True" /> ***<add key="DBSCommandTimeout" value="100000" />*** </appSettings> <runtime> <NetFx40\_LegacySecurityPolicy enabled="true"/> </runtime> <startup> <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/> </startup> </configuration>    **Obs.:**  Alterar somente o conteúdo na linha amarela. As outras linhas do arquivo podem variar de acordo com o ambiente do cliente. O serviço deverá ser reiniciado para que a alteração tenha efeito.    **2. “Rotinas Desenvolvidas na Tecnologia “Delphi”**  **a)** Exemplo: Sintegra , GIA, DIRF, DACON etc...    Para realiza alteração do Time Out, basta acessar o Painel de Controles | BDE Adminstrator CONNECT TIMEOUT = 7200  TIMEOUT = 7200      **Logo após, grave as alterações e reinicie a aplicação:** |
| **Observações:** |  |
