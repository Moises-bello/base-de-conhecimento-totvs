---
article_id: 28953830209559
category: Suricato
content_hash: 3c6671a2048cab230e5ccc24f424b0891de787465bf103dc34df2cf9a62fec23
fetched_at: '2026-06-28T22:46:26.345102+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: 'RH - RM - PTO - Erro na integração RM e Suricato - The SELECT permission was
  denied on the object ''APARAM'' ou ORA-00942: a tabela ou view não existe'
type: support-article
updated_at: '2025-09-05T20:21:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28953830209559-RH-RM-PTO-Erro-na-integra%C3%A7%C3%A3o-RM-e-Suricato-The-SELECT-permission-was-denied-on-the-object-APARAM-ou-ORA-00942-a-tabela-ou-view-n%C3%A3o-existe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28953846398615) Tempo aproximado para leitura: **00:03:00min****Dúvida**Como corrigir o erro a seguir ao editar um funcionário, realizar a carga inicial para Suricato ou algum outro processo que acione a integração com Suricato?

Base SQL:

Houve um erro na execução da Fórmula Visual:  
Erro na execução da Atividade: 'CargaInicial'  
Erro: Erro no Agente de Envio (mensagem assíncrona). System.Web.Services.Protocols.SoapException: O servidor não pôde processar a solicitação. ---> System.Data.SqlClient.SqlException: The SELECT permission was denied on the object 'APARAM', database 'EXE1212302', schema 'dbo'. em System.Data.SqlClient.SqlConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)

Base Oracle:

Houve um erro na execução da Fórmula Visual:

Erro na execução da Atividade: 'Empresa'  
Erro: Erro no Agente de Envio (mensagem assíncrona). System.Web.Services.Protocols.SoapException: O servidor não pôde processar a solicitação. ---> Devart.Data.Oracle.OracleException: ORA-00942: a tabela ou view não existe

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28953830187671)

**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
**Solução**  
Para solucionar esse erro, realize os seguintes passos:

1. Acesse o servidor onde foi  instalado o Webservice RM;

2. Localize a pasta do Webservice (pasta padrão C:\TSA) e edite o arquivo Alias.dat;

3. Dentro do arquivo altere as tags  UserName (usuário) e Password (senha) para um usuário e senha do banco de dados que tenha acesso a todas as tabelas do RM;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28953846407575)

4. Após o ajuste, reinicie o IIS para aplicar o ajuste.

**Saiba mais**

[RH - RM - PTO - Instalação e configuração do Webservice RM para integração com o Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27720600761367)
