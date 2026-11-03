---
article_id: 235301587
category: Materiais - Compras (SIGACOM)
content_hash: 7d3fbf86844c5fb7113740ed86eb11651eaa3548059a00bae755c1d6d081d9e6
fetched_at: '2026-06-28T22:41:24.089495+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Procedimento para utilizar
  múltiplas naturezas no documento de entrada
type: support-article
updated_at: '2022-11-09T13:53:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301587-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Procedimento-para-utilizar-m%C3%BAltiplas-naturezas-no-documento-de-entrada
---

**Dúvida**

Procedimento para utilizar múltiplas naturezas no documento de entrada  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

Para utilizar múltiplas naturezas no documento de entrada deverá configurar o parâmetro **MV\_MULNATP** com conteúdo **T**.

O parâmetro é utilizado para identificar se o título utiliza múltiplas naturezas no **Contas a Pagar**.

![20220705_092755.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7236525861143/20220705_092755.gif)

**OBSERVAÇÃO :**

Existem casos onde o cliente deseja informar o *valor* ao invés do *percentual*, com objetivo de facilitar a digitação do usuário.

Para tratar estas situações o cliente deverá criar um campo customizado na tabela SEV para informar o valor, e criar um gatilho customizado para que o percentual informado no EV\_PERC seja alimentado ao informar o valor no campo customizado.

Por padrão o valor do rateio é gravado no campo EV\_VALOR, com o resultado do cálculo do percentual do EV\_PERC vezes o valor total dos títulos. Este calculo é feito internamente pela rotina de Documento de Entrada.

***Saiba Mais :***

**[PCOM12054 - Campos de Multiplas Naturezas (SEV) na aba Duplicatas](https://tdn.totvs.com/x/gB9eHQ)**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)**
