---
article_id: 8348248171671
category: SIGAEST - CUSTOS
content_hash: d7f2e52831f88651f5704a270f1692cfe86b646e59eeba68b319412e662a7f5f
fetched_at: '2026-06-28T22:39:00.871189+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo incorreto na
  Transferência Múltipla
type: support-article
updated_at: '2022-08-22T20:13:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8348248171671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-incorreto-na-Transfer%C3%AAncia-M%C3%BAltipla
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:12 min****Ocorrência**Custo de movimento de transferência múltipla ficando incorreto.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

A Rotina MATA261 gerando inconsistência no calculo do D3\_CUSTO1.

**Solução**

Foi realizado o tratamento para que execute o calculo correto do custo na movimentação de transferência. Aplique o Pacote de Expedição Contínua para que seu ambiente contemple esta correção.

***Expedição Contínua Estoque/Custos:***

Release 12.1.33 - **[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1039086)**

Boletim Técnico: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=691445002>

Após a atualização, para registros já gravados na base de dados com o custo incorreto, as alternativas são:

* Executar a rotina Recálculo do Custo Médio (MATA330) para que o Sistema ajuste o custo do movimento;
* Estornar e refazer o movimento para que o mesmo receba o custo correto.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
