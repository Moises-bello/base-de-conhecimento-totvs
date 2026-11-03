---
article_id: 28919278184343
category: Materiais - Compras (SIGACOM)
content_hash: 17c1e5a8c18383bb7f21ecd7866426b0982913481d51e65486e979bfc135ea2c
fetched_at: '2026-06-28T22:41:11.833169+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Calculo da Quantidade de Segunda Unidade
  de Medida do Item do Documento de Entrada do Campo D1_QTSEGUM
type: support-article
updated_at: '2025-03-10T17:10:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28919278184343-Cross-Segmentos-Backoffice-Protheus-Calculo-da-Quantidade-de-Segunda-Unidade-de-Medida-do-Item-do-Documento-de-Entrada-do-Campo-D1-QTSEGUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28919292495895) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Como efetuar o Calculo da Quantidade de Segunda Unidade de Medida do Item do Documento de Entrada do Campo D1\_QTSEGUM

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSÃO 12

**Solução**

Para realizar o processo corretamente, deve-se  seguir as informações abaixo ao cadastrar os produtos:

### Cadastro de Produtos:

* **B1\_UM**: Primeira unidade de medida.
* **B1\_SEGUM**: Segunda unidade de medida.
* **B1\_CONV**: Fator de conversão da primeira unidade para a segunda unidade.
* **B1\_TIPCONV**: Indica se o fator de conversão será utilizado para multiplicar ou dividir, a fim de calcular a primeira unidade de medida.

#### Exemplo Prático:

**Multiplicação**

* **1ª Unidade (B1\_UM):** UN (Unidade)
* **2ª Unidade (B1\_SEGUM):** CX (Caixa)
* **Fator de Conversão (B1\_CONV):** 10

O sistema calcula:  
**2ª Unidade × Fator de Conversão = 1ª Unidade**, ou seja:  
1 Peça × 10 = 1 Caixa (1 Caixa contém 10 Peças).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28919297033239)

### 

### Funcionamento no Sistema:

Em todas as rotinas de **Entrada**, **Saída** e **Movimentação Interna**, o sistema apresenta campos para digitação nas duas unidades de medida.

* **Com Fator de Conversão:**  
  Ao informar a quantidade em uma das unidades de medida, o sistema calculará automaticamente a quantidade correspondente na outra unidade, preenchendo o campo automaticamente.
* **Sem Fator de Conversão:**  
  Ambos os campos deverão ser preenchidos manualmente.

### Documento de Entrada:

Ao informar a quantidade no campo **D1\_QUANT** (Quantidade), o sistema automaticamente realizará a conversão no campo de Quantidade de Segunda Unidade de Medida "**D1\_QTSEGUM"** correspondente à segunda unidade de medida.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Unidades de Medida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412135361815-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Unidades-de-Medida)
