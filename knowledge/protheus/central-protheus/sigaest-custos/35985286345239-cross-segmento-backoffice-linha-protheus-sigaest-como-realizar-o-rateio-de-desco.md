---
article_id: 35985286345239
category: SIGAEST - CUSTOS
content_hash: 168e7b1fb2a7d6aa03c5db2f8ef4db83b401662c6e00de4c49604b5c9e99ce98
fetched_at: '2026-06-28T22:39:00.780909+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o rateio
  de Desconto, Despesas e Frete no Documento de Entrada
type: support-article
updated_at: '2026-03-03T20:23:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35985286345239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-rateio-de-Desconto-Despesas-e-Frete-no-Documento-de-Entrada
---

O rateio de desconto em documentos de entrada no TOTVS Protheus é feito por valor, ativando o campo D1\_VALDESC. Já o rateio de despesas, frete e seguro pode ser por valor ou peso, conforme o parâmetro MV\_RATDESP. Valores informados manualmente são somados automaticamente. O rateio ocorre independentemente da geração de duplicata e não é possível desconsiderar o custo do frete sem customização via ponto de entrada A103CUST.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35985286331159) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Como é realizado o rateio de Desconto e Despesas em documentos de entrada?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

#### **1. Rateio de Desconto**

1. O **rateio de desconto** é sempre realizado **por valor** no documento de entrada.  
   Para acompanhar o tratamento, marque o campo **D1\_VALDESC** como **usado** via **Configurador**.
2. **Exemplo:**  
   Ao informar R$ 5,00 no folder *Descontos/Frete/Despesas*, o sistema distribui automaticamente entre os itens conforme o valor total:

```
Produto   Quant.   V.Unit.   Total   Desconto
Item 01: MP.001    1,00     30,00     30,00   3,00
Item 02: MP.002    1,00     10,00     10,00   1,00
Item 03: MP.003    1,00     10,00     10,00   1,00
```

**Nota**: Caso os valores de desconto sejam informados **manualmente em cada item**, a rotina **soma** os valores e apresenta o total no folder de *Descontos/Frete/Despesas*.

#### **2. Rateio de Despesas, Frete e Seguro**

Para esses valores, é possível definir se o rateio será **por valor** ou **por peso**, conforme o parâmetro **MV\_RATDESP**.

* **MV\_RATDESP = 1** → Rateio por valor
* **MV\_RATDESP = 2** → Rateio por peso

Os campos utilizados são:

* **D1\_DESPESA**
* **D1\_VALFRE**
* **D1\_SEGURO**
* **D1\_PESO** (necessário para rateio por peso – deve ser preenchido manualmente ou via gatilho/customização)

**Exemplo prático – valores informados:**

* Despesa: R$ 5,00
* Frete: R$ 10,00
* Seguro: R$ 20,00

**POR VALOR**

```
Produto   Quant.   V.Unit.   Total   Despesa   Frete   Seguro
Item 01: MP.001    1,00     30,00     30,00   3,00      6,00    12,00
Item 02: MP.002    1,00     10,00     10,00   1,00      2,00     4,00
Item 03: MP.003    1,00     10,00     10,00   1,00      2,00     4,00
```

**POR PESO**

```
Produto   Quant.   V.Unit.   Total   Peso    Despesa   Frete   Seguro
Item 01: MP.001    1,00     30,00     30,00   20,00   1,66       3,33    6,66
Item 02: MP.002    1,00     10,00     10,00   30,00   2,50      5,00    10,00
Item 03: MP.003    1,00     10,00     10,00   10,00   0,84      1,67    3,34
```

Caso os valores sejam informados **manualmente item a item**, o sistema **soma** e apresenta o total no folder de *Descontos/Frete/Despesas*.

### **Observações importantes:**

 - O tratamento de rateio é realizado **independente da TES gerar duplicata ou não**.

 - Caso existam itens que **não gerem duplicata** e **não se deseje** que os valores sejam rateados automaticamente, é necessário informar os valores **individualmente (item a item)**.

**-** **Não é possível desconsiderar o Custo do Frete** na Nota de Entrada, porém é possível customizar com apoio de seu Analista Desenvolvedor utilizando o Ponto de Entrada [A103CUST](https://tdn.totvs.com/x/i9pc). Abaixo link com a Documentação do Ponto de Entrada.

**A103CUST - Manipula Custo de Entrada ->** [***https://tdn.totvs.com/x/i9pc***](https://tdn.totvs.com/x/i9pc)

### **Veja também:**

[Backoffice (Linha Protheus) - SIGAEST - Agregando o Custo ao Conhecimento de Frete](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)
