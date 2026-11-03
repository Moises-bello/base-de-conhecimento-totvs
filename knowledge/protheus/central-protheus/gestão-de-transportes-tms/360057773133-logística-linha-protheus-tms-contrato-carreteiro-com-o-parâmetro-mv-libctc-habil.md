---
article_id: 360057773133
category: Gestão de Transportes (TMS)
content_hash: 225a6f1376188c50e43c175cab42df9f8502c28b7a6a5ca9b5976c937cc9a568
fetched_at: '2026-06-28T22:45:27.581643+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Contrato Carreteiro com o parâmetro MV_LIBCTC
  habilitado
type: support-article
updated_at: '2021-08-23T13:20:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057773133-Log%C3%ADstica-Linha-Protheus-TMS-Contrato-Carreteiro-com-o-par%C3%A2metro-MV-LIBCTC-habilitado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como gerar o **Contrato de Carreteiro** com o parâmetro **MV\_LIBCTC** habilitado no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A liberação de contrato carreteiro é utilizada em operações onde é necessário auditar os contratos antes da geração dos títulos no **Financeiro**.  
  
Para utilizar este controle, é necessário ativar o parâmetro **MV\_LIBCTC - Habilita o controle de Liberação de Contratos de Carreteiro**.  
O contrato só pode ser liberado quando o *status* estiver como **Aguardando Liberação**.  
  
Acesse: **Atualizações / Terceiros / Lib. Contratos - TMSA251**. Nos parâmetros é possível filtrar por **Contrato, Período, Fornecedor, Viagem e Status do Contrato**.  
  
Selecione os contratos e realize a liberação. Após liberar os contratos especificados no parâmetro, os títulos do contrato são gerados e o seu *status* muda para **Liberado para pagamento**.
