---
article_id: 360046079234
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 733945092ba165e8f8c043fd16121fa0511c8ec9b92c22fed8e91f8534e4d885
fetched_at: '2026-06-28T22:38:54.003990+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível ter um
  Mile ou ExecAuto para dar saldo inicial para produtos que usam lote?
type: support-article
updated_at: '2025-09-26T14:17:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046079234-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-ter-um-Mile-ou-ExecAuto-para-dar-saldo-inicial-para-produtos-que-usam-lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19590283453207) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**É possível ter um Mile ou ExecAuto para dar saldo inicial para produtos que usam lote?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.

**Solução**O **ExecAuto** da rotina **MATA220** não faz a criação de lotes;  
A Criação de lotes é feita no **ExecAuto** da rotina **MATA390;**  
A Própria tela de saldo inicial normal, usa o **ExecAuto** da **MATA390** para criar os lotes;  
A opção é usar o **ExecAuto** da rotina **MATA220** e dar saldo inicial zerado e depois executar o **ExecAuto** da **MATA240** ou **MATA241** com a inclusão de uma devolução informando a quantidade e o lote.

**Saiba Mais**  
*[MATA220 - Controle de Itens do Estoque](https://tdn.totvs.com/display/public/mp/MATA220+-+Controle+de+Itens+do+Estoque)*

[*Rotina automática - MATA390*](https://tdn.totvs.com/pages/viewpage.action?pageId=307851505)  
*[Rotina automática - MATA241](https://tdn.totvs.com/pages/releaseview.action?pageId=36308382)*  
*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
