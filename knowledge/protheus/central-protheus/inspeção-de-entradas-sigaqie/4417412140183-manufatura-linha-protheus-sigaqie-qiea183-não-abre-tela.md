---
article_id: 4417412140183
category: Inspeção de Entradas (SIGAQIE)
content_hash: 0b6a9cb6b311617dc4cb10a351bf3bf2e25769fef2abe28d23955ecf2b0273e8
fetched_at: '2026-06-28T22:42:27.143924+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - QIEA183 - Não abre tela
type: support-article
updated_at: '2021-12-29T12:03:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417412140183-Manufatura-Linha-Protheus-SIGAQIE-QIEA183-N%C3%A3o-abre-tela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:48 min** **Dúvida**Por que ao tentar acessar a rotina **QIEA183 - Importação** a tela é fechada automaticamente?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Este é o procedimento padrão da rotina quando não existe nenhum registro à ser importado, ou seja, quando não existem registros na tabela **QEP - Controle Entregas Importadas** ou então, quando os registros existentes estão com o campo **QEP\_CODTAB - Status** igual à **1 - Importação Correta**, indicado que já foram importados.  
A rotina somente irá abrir quando existirem registros na tabela **QEP** em que o campo **QEP\_CODTAB** é igual à **2 - Inconsistência na Importação**.
