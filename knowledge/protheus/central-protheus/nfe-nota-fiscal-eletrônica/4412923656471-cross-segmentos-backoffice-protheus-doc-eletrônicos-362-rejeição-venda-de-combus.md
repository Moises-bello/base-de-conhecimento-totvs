---
article_id: 4412923656471
category: NFe - Nota Fiscal Eletrônica
content_hash: b14c6f0dffbe3cb36f18f9f0d54de93f698472f39f7a40936077ff62b2c75621
fetched_at: '2026-06-28T22:40:04.992865+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 362 Rejeição: Venda
  de combustível sem informação do Transportador'
type: support-article
updated_at: '2025-06-25T12:10:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412923656471-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-362-Rejei%C3%A7%C3%A3o-Venda-de-combust%C3%ADvel-sem-informa%C3%A7%C3%A3o-do-Transportador
---

**Dúvida**Como solucionar a rejeição abaixo:

362 Rejeição: Venda de combustível sem informação do Transportador ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1.  Ao utilizar CFOP de combustível conforme o Anexo XIII.02, **página 297 do Manual do link abaixo****é obrigatória a informação de identificação do Transportador.**

[Manual de Orientação do Contribuinte - versão 6.00](Manual%20de%20Orienta%C3%A7%C3%A3o%20do%20Contribuinte%20-%20vers%C3%A3o%206.00)

2. Caso o CFOP da nota esteja errado alterar no campo do TES ***"Cod. Fiscal F4\_CF"  um CFOP***que não conste na lista acima.

![F4_CF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412907147031)

3. Após isso, ***exclua a nota e gere novamente.***

4. Caso o CFOP da nota esteja correto, se for nota de saída no pedido de vendas preencher o campo ***"Transp. C5\_TRANSP  e Veic. Transp C5\_VEICULO e Tipo frete C5\_TPFRETE."***

***![FRETE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412923363479)***

5. Após isso, **exclua a nota e gere novamente.**

6. Caso o CFOP da nota esteja correto, se for nota de entrada no pedido de vendas preencher o campo ***"Cod. Transp. F1\_TRANSP  e Veiculo 1  F1\_VEICUL1 e Tipo frete F1\_TPFRETE."***

![frete_documento_de_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412923496087)

7. Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

**NT 2022.002** ***Exceção:*** Regra não se aplica quando existir algum item com a UF de consumo do ***combustível igual a exterior (tag: comb/UFCons = “EX”) e com CFOP = “7667***- Venda de combustível ou lubrificante a consumidor ou usuário final”

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040882033559)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040882033559)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040882035607)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040882039319)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

5. Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF" = *7667***

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040882041495)

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](https://tdn.totvs.com/pages/releaseview.action?pageId=642645988)

* **Validação da Sefaz:**

![362.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7475452456855)
