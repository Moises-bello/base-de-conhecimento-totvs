---
article_id: 360020205491
category: NFe - Nota Fiscal Eletrônica
content_hash: f70c19f53f6e33627a3d2d3d4e615050546e97a9d2d06d785e4daf5a5743cbf9
fetched_at: '2026-06-28T22:40:03.084606+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - 693 : Rejeição  - Alíquota de ICMS
  superior a definida para a operação interestadual'
type: support-article
updated_at: '2025-06-17T19:18:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205491-Cross-Segmentos-Backoffice-Protheus-693-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-de-ICMS-superior-a-definida-para-a-opera%C3%A7%C3%A3o-interestadual
---

**Dúvida**

Como solucionar a rejeição ?

693 : Rejeição - Alíquota de ICMS superior a definida para a operação interestadual

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A validação dessa rejeição ocorre para operação interestadual e para nota de saída do tipo normal  **(idDest=2, tpNF=1 e finNFe=1);**

Além disso, a Sefaz irá verificar se a origem da nota é   **0, 4, 5, 6 ou 7**

Caso esteja dentro das condições acima será valida a TAG **<pICMS>**que não pode ser :

* Maior do que **“7.00” (7 por cento)** para os Estados de origem **(enderEmit/UF)** do **Sul e Sudeste, exceto ES,** Destinado **(enderDest/UF)** para os Estados do **Norte, Nordeste, Centro-Oeste e Espírito Santo. -** Valor alíquota do ICMS **(tag:pICMS) maior do que “12.00”** (12 por cento) para os demais casos.

1- Caso tenha informado a origem errada do Produto alterar no campo **Origem** "**B1\_ORIGEM" :**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061346473)

2- Há **Exceção 3**: A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias ou Anulação de Valor **(Anexos XIII.04 e XIII.05).**  
  
A lista completa dos CFOPS consta no link abaixo na página 22:  
  
[Nota Técnica 2015.003 - v 1.94](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)

Caso seja necessário alterar o CFOP altere pela TES da nota no campo **Cod. Fiscal "F4\_CF":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060423754)  
  
  
3- Há **Exceção 4**: A regra de validação acima não se aplica para as operações de venda à ordem (CFOP 6.118, 6.119, 6.122 e 6.123).

Caso seja necessário alterar o CFOP altere pela TES da nota no campo **Cod. Fiscal "F4\_CF":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060423754)

4- Caso a nota esteja correto a **origem do Produto e o seu CFOP** será necessário ajustar no sistema alíquota correta.

* **Saiba mais:**

Há na nota técnica as demais exceções:

**Exceção 1:** Para as NF-e com Data de Emissão anterior a 01/07/2016, a regra de validação acima não se aplica para destinatário Não Contribuinte (tag:dest/indIEDest=9).

**Sendo assim, essa exceção não se aplica mais.**

**Exceção 2:** A regra de validação acima não se aplica na venda de veículos novos (grupo “veicProd”) se existir ao menos um item de Venda direta para grandes consumidores (tpOp=3), ou de Faturamento direto para consumidor final (tpOp=2).

Para essa exceção há documentação **do link abaixo:**

[MP - NFE - Como gerar Detalhamento Específico de Veículos novos no XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026946731)

**Exceção 5:** A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF);

Para essa exceção há documentação **do link abaixo:**

[MP - NFE - Como gerar as TAGS de cliente de entrega e cliente de retirada no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711)

**Exceção 6:** A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF);

Para essa exceção há documentação **do link abaixo:**

[MP - NFE - Como gerar as TAGS de cliente de entrega e cliente de retirada no XML ?](MP%20-%20NFE%20-%20Como%20gerar%20as%20TAGS%20de%20cliente%20de%20entrega%20e%20cliente%20de%20retirada%20no%20XML%20?)

* **Validação da Sefaz:**

![](https://totvssuporte.zendesk.com/attachments/token/6V0WK6lbaqSAzDmWxrmyH4Kq0/?name=inline74248811.png)​  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/YnntokfTyE2tEJoUslq2h0xHG/?name=inline-676206539.png)​
