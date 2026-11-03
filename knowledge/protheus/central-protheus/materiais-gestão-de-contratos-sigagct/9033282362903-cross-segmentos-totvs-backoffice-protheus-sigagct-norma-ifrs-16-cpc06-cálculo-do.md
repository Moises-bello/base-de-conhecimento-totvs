---
article_id: 9033282362903
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b2c960f08202a310e62dcb3416f6bde5bc6ebd5626e18b05c933647df440d50c
fetched_at: '2026-06-28T22:37:23.944724+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Norma IFRS 16 (CPC06)
  - Cálculo do valor presente na inclusão do contrato
type: support-article
updated_at: '2024-10-03T14:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9033282362903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Norma-IFRS-16-CPC06-C%C3%A1lculo-do-valor-presente-na-inclus%C3%A3o-do-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26810140483735) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Qual o calculo do valor presente na inclusão do contrato utilizando IFRS16  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - 12.1.27 superior  
  
**Solução**

Foi realizada a implementação do cálculo do valor presente em contratos fixos, ou seja, que tenham cronograma financeiro. Além do valor presente, é possível visualizar a taxa de juros e o valor dos juros.

Será necessário a **criação de campos e da pergunta** conforme demonstrado no passo a passo abaixo via configurador.

Ao gerar o cronograma financeiro de uma planilha, deve-se informar a taxa de juros no pergunte, conforme abaixo:

![](https://tdn.totvs.com/download/attachments/555255542/image2020-7-8_14-20-14.png?version=1&modificationDate=1594229647717&api=v2)

Após a geração do cronograma, é possível visualizar os valores calculados no Cronograma Financeiro, conforme imagem:

![](https://tdn.totvs.com/download/attachments/555255542/image2020-7-8_14-20-50.png?version=1&modificationDate=1594229647677&api=v2)

Além dos totalizadores por cronograma, é possível visualizar os totalizadores do contrato inteiro:

![](https://tdn.totvs.com/download/attachments/555255542/image2020-7-8_14-21-56.png?version=1&modificationDate=1594229647630&api=v2)

O cálculo do valor presente leva em consideração a fórmula abaixo:

**Fórmula**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | `/*`  `nJuros......= Taxa de Juros(Exemplo: para 5% de juros, nJuros será 0.05)`  `nTotParcel..= Número de parcelas`  `nParcela....= Número da parcela atual`  `nFuturo.....= Valor da parcela(valor futuro)`  `P = F/(1 + i)^n`  `*/`  `nDivisor := ( (1 + nJuros) ^ (nTotParcel - nParcela) )`    `If (nDivisor > 0)`  `nPresente := nFuturo / nDivisor`  `EndIf` |

O valor de entrada da variável **nFuturo**(obtida diretamente do campo **CNF\_VLPREV**) pode ser modificado através da fórmula informada no campo Form. Vl. Pres (**CN9\_FRMVL**). Este cálculo somente é realizado ao incluir o cronograma financeiro. Exemplo:

![](https://tdn.totvs.com/download/attachments/555255542/image2020-7-8_14-31-35.png?version=1&modificationDate=1594229647550&api=v2)

**Saiba mais:**

[Calculo Valor Presente](https://tdn.totvs.com/pages/releaseview.action?pageId=555255542)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Norma IFRS 16 (CPC06) no módulo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018928012-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Norma-IFRS-16-CPC06-no-m%C3%B3dulo-Gest%C3%A3o-de-Contratos?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
