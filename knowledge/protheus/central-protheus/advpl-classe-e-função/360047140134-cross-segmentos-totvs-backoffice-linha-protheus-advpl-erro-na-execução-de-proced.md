---
article_id: 360047140134
category: ADVPL - Classe e Função
content_hash: d806127ef23e03626ba003fe0a594f12abc70a1f7b00754191edb0e89e842534
fetched_at: '2026-06-28T22:40:18.351025+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro na execução
  de procedures via ADVPL '
type: support-article
updated_at: '2022-01-10T14:36:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047140134-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-na-execu%C3%A7%C3%A3o-de-procedures-via-ADVPL
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Problemas ao executar procedures após a atualização do DBACCESS, como corrigir?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Foi identificado um comportamento na execução de **procedures** no **SGBD** **SQL** Server, que caso a chave ***ODBC30***esteja ligada (***ODBC30**=1*) e a **procedure** possuir comentários, a mesma dá erro ao executar. Esse comportamento é relacionado ao *driver* do ***SQL Server***usando a ***ODBC 3.0*** ao executar uma **procedure** com comentários.  
Como a partir da **versão 19.2.1.0** a chave **ODBC30** vem ligada por padrão, conforme nota de release(saiba mais), pedimos que coloque no arquivo ***dbaccess.ini***a chave ***ODBC30**=0* na seção ***General***, reinicie o **DBAccess** e verifique se o problema persiste.  
  
**Saiba mais**[Melhoria - As funções ODBC 3.0 serão mapeadas por default](https://tdn.totvs.com/x/Eg9XHw)  
[DBAccess - Seção [General], chave ODBC30](https://tdn.totvs.com/pages/viewpage.action?pageId=36799225)
