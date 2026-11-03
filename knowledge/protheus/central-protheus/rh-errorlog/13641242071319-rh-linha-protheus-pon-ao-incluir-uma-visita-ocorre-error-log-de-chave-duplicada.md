---
article_id: 13641242071319
category: RH - Error.log
content_hash: a50fca47ed065128bbb21452b85fe869a8a122985765bcbbc5ee5714e6ac7481
fetched_at: '2026-06-28T22:44:49.515958+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: RH - Linha Protheus - PON - Ao incluir uma visita ocorre error log de chave
  duplicada na tabela SPY
type: support-article
updated_at: '2025-09-08T17:07:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13641242071319-RH-Linha-Protheus-PON-Ao-incluir-uma-visita-ocorre-error-log-de-chave-duplicada-na-tabela-SPY
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32125120560151) Tempo aproximado para leitura: **00:05:00 min******Dúvida****Ao incluir uma **visita (Atualizações>Cadastro de Visitantes>Visitas),** ocorre *error log "****SPY010: DB error (Update): -29 File: SPY010 - Error : 2601 (23000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]* Não é possível inserir uma linha de chave duplicada no objeto 'dbo.SPY010' com índice exclusivo"****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Esse incidente pode ocorrer por conta do campo **PY\_NUMERO**, que guarda o número da visita, estar **repetindo os códigos**. Isso pode ser causado por configuração incorreta do**s campos da tabela SPY**, **falta de atualização do ambiente** ou controle de numeração da tabela SPY incorreto. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/13640920125335)****Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Verifique no **dicionário de dados** da tabela **SPY**, via **SIGACFG**, a **configuração do campo PY\_NUMERO**, que deve seguir a estrutura abaixo;  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32125151134359)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32125151136151)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32125120567703)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32125120569111)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32125120571927)  
  
**2.** Se o campo estiver correto, verifique se as ordens dos campos na tabela SPY estão corretas, conforme o padrão, abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13640983412375)  
  
**3.** Verifique se os índices estão conforme abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/AvgTFtjR0YWPqoyM9P5lsVAq5/?name=image.png)  
  
**4.** A numeração da visita, é gerada de forma automática, assim, verifique também no Configurador, o [controle de numeração da tabela SPY](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026703731-Framework-Linha-Protheus-Acerto-de-Numera%C3%A7%C3%A3o-Autom%C3%A1tica), a numeração deve seguir o mesmo tamanho do campo **PY\_NUMERO**, ou seja, com **tamanho 9.**   
**5.** O ambiente deve estar atualizado, sendo necessário aplicar no ambiente o último [Pacote de Expedição contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus) de RH, [LIB](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/lib) e Binário, conforme links abaixo.  
[Binário - Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
[Binário - SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)  
  
**Saiba Mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
