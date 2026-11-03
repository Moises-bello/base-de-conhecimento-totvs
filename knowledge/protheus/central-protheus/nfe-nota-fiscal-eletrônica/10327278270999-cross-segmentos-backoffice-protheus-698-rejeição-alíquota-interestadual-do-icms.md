---
article_id: 10327278270999
category: NFe - Nota Fiscal Eletrônica
content_hash: 60298edd9c96371a317281731c920f29379fb60bb6073d490db00af5a9f055c8
fetched_at: '2026-06-28T22:40:03.090551+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - 698 Rejeição: Alíquota interestadual
  do ICMS incompatível com as UF envolvidas na operação'
type: support-article
updated_at: '2025-07-03T12:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10327278270999-Cross-Segmentos-Backoffice-Protheus-698-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-interestadual-do-ICMS-incompat%C3%ADvel-com-as-UF-envolvidas-na-opera%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a 698 Rejeição: Alíquota interestadual do ICMS incompatível com as UF envolvidas na operação ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informada alíquota interestadual ***(tag:pICMSInter) de 7% ou 12% em NF de Saída Normal (tpNF=1 e finNFe=1)*** e alíquota interestadual incompatível com as UF envolvidas:

- 7% para os Estados de origem do Sul e Sudeste, exceto ES, destinado para os Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo;

- 12% para os demais casos.  
  
***Exceção 1:*** A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias (Anexo XIII.04).

A lista completa dos CFOPS consta no link abaixo na página 22:  
  
[Nota Técnica 2015.003 - v 1.94](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)

Caso seja necessário alterar o CFOP altere pela TES da nota no campo **Cod. Fiscal "F4\_CF":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33225623938071)

***Exceção 2:*** A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016.

***Exceção 3:*** A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF);

[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-entrega-e-retirada-no-XML-)

***Exceção 4:*** A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF);

[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-entrega-e-retirada-no-XML-)
