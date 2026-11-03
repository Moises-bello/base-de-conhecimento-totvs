---
article_id: 4405487736343
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: e0254123a270c0920a2d552bfc3e25774db755a3861e3771b149b805dc34ee13
fetched_at: '2026-06-28T22:39:44.415551+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Sistema não está
  sincronizando moeda com o Financeiro
type: support-article
updated_at: '2023-01-24T11:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405487736343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Sistema-n%C3%A3o-est%C3%A1-sincronizando-moeda-com-o-Financeiro
---

**Dúvida**O sistema não está realizando a sincronização de moeda da SYE para a SM2 no módulo SIGAEIC (*Easy Import Control*).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Será necessário verificar se o parâmetro **MV\_EIC0067** esta habilitado. Pois com este parâmetro ativo, ao alterar a cotação de moeda no SIGAEIC será mantida a integridade dos valores com o módulo financeiro.  
  
**Pré-requisitos****:**

* MV\_EASYFIN = S
* MV\_EIC0067 = S
* Possuir uma cotação cadastrada para a moeda utilizada no SIGAFIN.
* Possuir uma cotação cadastrada no SIGAEIC.

**Sequência 001 - Parâmetro MV\_EIC0067 = S**

1. No *Easy Import Control* (SIGAEIC), acesse Atualizações/Cadastros/Cotação das Moedas.
2. Selecione o cadastro e clique em Alterar.
3. Atualize as informações de taxa com o valor diferente da informada no SIGAFIN (tabela SM2) e mesma moeda.
4. Clique em Confirmar.

Valor da taxa da moeda alterado no módulo financeiro.

**Saiba Mais:**

[MTRADE-1134 DT Sincronização de cotação de moedas, utilizando os parâmetros MV\_EIC0067 e MV\_EEC0055](https://tdn.totvs.com/pages/viewpage.action?pageId=284469753)
