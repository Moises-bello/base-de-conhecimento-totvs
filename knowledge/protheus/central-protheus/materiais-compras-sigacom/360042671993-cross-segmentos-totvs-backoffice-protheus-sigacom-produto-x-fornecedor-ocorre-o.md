---
article_id: 360042671993
category: Materiais - Compras (SIGACOM)
content_hash: f5d9e7804808951f21efe5e0a7d292c1882c91acc89fbf500c3461a797963e4d
fetched_at: '2026-06-28T22:41:24.098950+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Produto x Fornecedor
  ocorre o Help OBRIGAT: O campo Produto (A5_PRODUTO) não foi preenchido'
type: support-article
updated_at: '2022-05-18T21:15:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042671993-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Produto-x-Fornecedor-ocorre-o-Help-OBRIGAT-O-campo-Produto-A5-PRODUTO-n%C3%A3o-foi-preenchido
---

**Ocorrência**

Produto x Fornecedor ocorre o Help OBRIGAT: O campo Produto (A5\_PRODUTO) não foi preenchido.

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Causa**

A Help pode ocorrer diversos motivos, abaixo alguns dos principais:

**Solução**

**1.** Divergência de tamanho (X3\_TAMANHO) entre os campos B1\_DESC (Descrição do Cadastro de produtos) e A5\_NOMPROD (Descrição da rotina Produto x Fornecedor);

Deve ser realizado o Ajuste nos campos para que ambos possuam o mesmo tamanho;

**2.** Divergência de tamanho (X3\_TAMANHO) entre os campos B1\_COD  (Código do Cadastro de produtos) e A5\_PRODUTO (Código da rotina Produto x Fornecedor);

Deve ser realizado o Ajuste nos campos para que ambos possuam o mesmo tamanho;

**3.** Campo A5\_PRODUTO marcado como obrigatório (Por padrão o obrigatório é desmarcado, uma vez que a validação de obrigatoriedade é feita no codigo fonte);

Deve-se Desmarcar o campo obrigatório através do modulo SIGACFG;

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
