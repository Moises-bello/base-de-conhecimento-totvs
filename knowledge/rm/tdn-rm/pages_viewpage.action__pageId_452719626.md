---
content_hash: edea74a4f091680e12d21f6156d02c47faca678348b85c1fafb0fefd7d46dbc5
fetched_at: '2026-06-29T00:10:09.313543+00:00'
page_id: '452719626'
product: rm
source: tdn-rm
title: Código de Cálculo 92 - Restituições de INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719626
version: 2
---

Provento do tipo valor.   
 O sistema lançará o evento com código de cálculo 092 na movimentação quando ocorrer alguma alteração na tabela de INSS que gere mudança de faixa (para menor) nas férias, conforme parágrafo 17, artigo 37, capítulo VII - Suplemento Especial IOB 08/1992.

**Exemplo**

Um funcionário sairá de férias no dia 01/06/1997 e voltará no dia 01/07/1997. As férias foram calculadas no mês 05/1997 com a seguinte tabela de INSS:

Limite Superior       Percentual  
       176,00                    8,00  
       396,00                    9,00  
        590,00                 10,00  
    
 O cálculo do recibo de férias ficará:

Salário: 385,00 Férias  - 385,00 1/3 de Férias - 128,33 10% INSS de Férias - 51,33

No mês seguinte (06/1997), a tabela de INSS foi alterada para:

Limite Superior       Percentual  
       400,00                  8,00  
       660,00                  9,00  
       900,00                 10,00

No mês 06/1997 foram lançadas as férias no mês.

O lançamento ficará:

Férias no Mês  - 385,00  (P)

1/3 Férias no Mês - 128,33 (P) 9% Restit. De INSS - 17,13 (P)

Adiant. Conf. Recibo - 462,00(D)

10% INSS nas Férias - 51,33(D)

Totais  de proventos - 530,46 Totais de descontos - 513,33

Diferença  - 17,13

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo

O cálculo do sistema foi:

513,33 (férias) \* 9% (aplicada a tabela) = 46,19

51,33 (INSS anterior) - 34,20 (INSS atual) = 17,13
