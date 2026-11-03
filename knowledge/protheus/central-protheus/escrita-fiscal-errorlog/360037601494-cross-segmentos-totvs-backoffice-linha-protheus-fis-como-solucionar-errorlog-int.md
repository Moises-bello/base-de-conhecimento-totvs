---
article_id: 360037601494
category: Escrita Fiscal - Error.log
content_hash: 60dc5ee5542d55f4e22f2e9bb3c412372739df0a7cb9b51f022ecce947886cbb
fetched_at: '2026-06-28T22:39:32.814490+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como solucionar
  Error.Log: InterFunctionCall: cannot find function FINCXSIMP in AppMap on REGCXSIMP(FISR153B.PRW) '
type: support-article
updated_at: '2021-07-08T13:42:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037601494-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-solucionar-Error-Log-InterFunctionCall-cannot-find-function-FINCXSIMP-in-AppMap-on-REGCXSIMP-FISR153B-PRW
---

**Dúvida**

Ao solicitar relatório do Simples Nacional de regime de caixa FISR153B apresenta o error.log em tela:

InterFunctionCall: cannot find function FINCXSIMP in AppMap on REGCXSIMP(FISR153B.PRW) 17/07/2019 09:28:39 line : 387

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Aplicar patch que contenha o fonte; (FINXSPD.PRX 26/09/2019 11:46:41), pois a função FINCXSIMP não existe no seu RPO, para solução aplique a atualizado da rotina FINXSPD para que a função seja criada no RPO.

LINK:  <https://suporte.totvs.com/portal/p/10098/download?e=808192>
