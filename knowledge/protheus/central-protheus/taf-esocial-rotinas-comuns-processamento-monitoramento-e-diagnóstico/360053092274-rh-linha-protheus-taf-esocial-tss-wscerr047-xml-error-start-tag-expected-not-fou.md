---
article_id: 360053092274
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: f3ca0e12ec6fda0d53ae3de9645af7fb85627736e1bbcac12117a8e58b7b5b79
fetched_at: '2026-06-28T22:45:21.097418+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - TSS - WSCERR047 / XML Error Start tag
  expected, '<' not found
type: support-article
updated_at: '2024-09-24T19:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053092274-RH-Linha-Protheus-TAF-eSocial-TSS-WSCERR047-XML-Error-Start-tag-expected-not-found
---

**Dúvida**Ao enviar os eventos para o e-Social ocorre o problema no TSS:

**WSCERR047 / XML Error Start tag expected, '<' not found**   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - À partir da release 12.1.33  
  
**Solução**

1 - Abre o arquivo **appserver.ini** do TSS **(TSS | BIN | Appserver)**, e vá na sessão **[TOPCONNECT]** e veja qual o alias preenchido;

2 - Verifique se o ALIAS preenchido é o mesmo configurado no **ODBC** (*SQL*) ou no arquivo **TNSNAMES.ORA** (*Oracle*). Se for diferente o ALIAS no arquivo APPSERVER.INI do TSS, modifique-o para o mesmo nome da conexão ODBC ou TNSNAMES;

3 - Verifique se o DBAccess está conectando com o banco de dados:

[TAF - CONFIGURAÇÃO - Criando e testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)
