---
article_id: 7477025360535
category: NFe - Nota Fiscal Eletrônica
content_hash: e66a41b218c28756d09f7ba8637b2e38c9516b5d01586d77bcdf8f11d4d34e9c
fetched_at: '2026-06-28T22:40:05.268016+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 727 Rejeição: Operação
  com Exterior e UF diferente de EX'
type: support-article
updated_at: '2025-07-14T14:08:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7477025360535-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-727-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-Exterior-e-UF-diferente-de-EX
---

**Dúvida**Como solucionar a rejeição abaixo:

727 Rejeição: Operação com Exterior e UF diferente de EX  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Se endereço destinatário é no Exterior ***(dest/UF = “EX"):*** – UF de destino diferente de “EX”

1. Preencher no cadastro no ***Protheus no cadastro de Cliente* nos *campos* *Estado*** A1\_EST = EX e ***Pais*** A1\_PAIS

**![A1_EST__A1_PAIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040910657687)**

**Ou**

2- Preencher no *Protheus no cadastro de Fornecedor* ***nos campos Estado A2\_EST = EX e Pais A2\_PAIS.***

![A2_PAIS_A2_EST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040888899991)

***Exceção:*** Regra não se aplica quando existir algum item com a UF de consumo do ***combustível igual a exterior (tag: comb/UFCons = “EX”) e com CFOP = “7667***- Venda de combustível ou lubrificante a consumidor ou usuário final”

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040910659223)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040910659223)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040910660631)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040910661655)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

5. Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF" = *7667***

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11753703049495)

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](https://tdn.totvs.com/pages/releaseview.action?pageId=642645988)

* ***Validação da Sefaz:***

![727.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7476752204567)
