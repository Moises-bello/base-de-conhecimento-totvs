---
article_id: 22107534404503
category: Financeiro - Viagens
content_hash: f48bba97b04e2b6a142b867105dbc2d65160f5d364ee3a9db7281f32f9793b47
fetched_at: '2026-06-28T22:38:21.376769+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - APP Minha Prestação
  de Contas - Funcionamento do APP Meu Protheus quanto a aprovação de prestação de
  contas
type: support-article
updated_at: '2024-03-19T13:45:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22107534404503-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-APP-Minha-Presta%C3%A7%C3%A3o-de-Contas-Funcionamento-do-APP-Meu-Protheus-quanto-a-aprova%C3%A7%C3%A3o-de-presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22107527417367) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Funcionamento do APP Meu Protheus quanto a aprovação de prestação de contas  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

O aplicativo Meu Protheus lista na aba **"Aprovadas"**, apenas prestações de contas que estão exatamente com o status **"APROVADA"**. Os status posteriores (como **"Finalizada"**, ou **"Em avaliação do Financeiro"** por exemplo) não são considerados por padrão, pois não há na interface atual do *app* uma distinção visual entre prestação de contas com status **"aprovada"** e **"finalizada"**. Se possivelmente considerar na aba **"Aprovadas"** e também prestações de contas em status **"finalizada"**, exibe um status incorreto, que induz o usuário ao erro.

Este comportamento quanto a qual status irá ficar a prestação após aprovação do gestor, é definido na rotina **FINA691** no fluxo das **aprovações/liberações.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22107534385943)**

**Saiba mais:**[Guia de uso - Minha Prestação de Contas](https://tdn.totvs.com/pages/releaseview.action?pageId=287057777)

[Guia de uso - Meu Protheus](https://tdn.totvs.com/display/public/PROT/Guia+de+uso+-+Meu+Protheus#teste-visualize)
