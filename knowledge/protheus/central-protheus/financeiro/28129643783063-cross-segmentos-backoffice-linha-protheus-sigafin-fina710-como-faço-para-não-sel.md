---
article_id: 28129643783063
category: Financeiro
content_hash: f7c8595946a8b8e0c14ce0e92f63adcda90934f90eb9eac01f278a37bad0acaf
fetched_at: '2026-06-28T22:38:03.063873+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como faço
  para não selecionar nenhum código de banco, para que a projeção do fluxo de caixa
  não considere nenhum saldo bancário
type: support-article
updated_at: '2024-11-28T13:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28129643783063-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-fa%C3%A7o-para-n%C3%A3o-selecionar-nenhum-c%C3%B3digo-de-banco-para-que-a-proje%C3%A7%C3%A3o-do-fluxo-de-caixa-n%C3%A3o-considere-nenhum-saldo-banc%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28129643770647) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como faço para não selecionar nenhum código de banco, para que a projeção do fluxo de caixa não considere nenhum saldo bancário

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210  
  
**Solução**

Na rotina FINA710 - Novo Fluxo de Caixa, é obrigatório selecionar pelo menos um banco, para que o saldo deste seja considerado na projeção do fluxo de caixa. Isso ocorre porque, em sua maioria, os títulos em aberto serão baixados em algum banco

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28129643770903)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28129643771415)

**Importante**: Ao comparar o funcionamento de uma nova rotina com uma rotina anterior, nem todas as funcionalidades da versão antiga serão necessariamente mantidas.

Um exemplo clássico disso é que, na rotina antiga FINC021, era possível retroceder a data base do sistema e visualizar o fluxo de caixa de períodos passados. Já na nova rotina FINA710, embora seja possível retroagir a data base, não é mais possível visualizar a retroação dos saldos dos títulos."

Se for necessário realizar a projeção sem considerar o saldo do banco, recomendamos a criação de um banco fictício, sem saldo, que não seja utilizado em nenhuma outra operação. Isso permitirá obter a projeção do fluxo de caixa desconsiderando o saldo bancário.

**Saiba mais:**

[Movimentações Financeiras - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=622668231#Movimenta%C3%A7%C3%B5esFinanceirasFINA710-FLUXODECAIXA)
