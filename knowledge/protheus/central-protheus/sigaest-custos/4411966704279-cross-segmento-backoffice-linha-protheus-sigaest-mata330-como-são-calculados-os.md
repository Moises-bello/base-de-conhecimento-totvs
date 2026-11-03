---
article_id: 4411966704279
category: SIGAEST - CUSTOS
content_hash: 6e2c16dc5e299c0d9aaaf3e1e6bd4aa633d61b58d52d115c09e3dc6fc178361e
fetched_at: '2026-06-28T22:39:02.132087+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como são
  calculados os custos apresentados nos campos B2_CMFIM1 e B2_CM1?
type: support-article
updated_at: '2025-09-24T14:59:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411966704279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-s%C3%A3o-calculados-os-custos-apresentados-nos-campos-B2-CMFIM1-e-B2-CM1
---

**Dúvida**  
Qual o funcionamento dos campos B2\_CMFIM1 e B2\_CM1 e sua relação com a rotina de Recálculo de Custo Médio - MATA330?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Exemplo de cálculo do Custo Médio Unitário:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Movimento** | **Qtd** | **Custo   Unitário** | **Custo   Total** | **Valor   em estoque** | **Qtd   em estoque** | **CM Unitário\*** |
| Nota   fiscal de entrada | 10 | R$   1,00 | R$   10,00 | R$   10,00 | 10 | R$ 1,00 |
| Nota   fiscal de entrada | 10 | R$   4,00 | R$   40,00 | R$   50,00 | 20 | R$ 2,50 |
| Nota   fiscal de saída | 08 | R$   2,50 | R$   20,00 | R$   30,00 | 12 | R$ 2,50 |
| Nota   fiscal de saída | 07 | R$   2,50 | R$   17,50 | R$   12,50 | 05 | R$ 2,50 |
| Nota   fiscal de entrada | 05 | R$   10,00 | R$   50,00 | R$   62,50 | 10 | R$ 6,25 |
| Requisição   para consumo | 03 | R$   6,25 | R$   18,75 | R$   43,75 | 07 | R$ 6,25 |

**CM Unitário: Esta coluna sempre é calculada pelo valor total em estoque / quantidade total de estoque.**

O cálculo do campo **B2\_CMFIM1** ocorre durante o processamento da rotina de **Custo Médio** (**MATA330**) e sua fórmula contempla a divisão do **valor total do armazém pela quantidade total.**

Vale ressaltar que a rotina de Custo Médio (MATA330) altera a ordem dos movimentos que devem ser processados, o que causa o acerto do custo médio.

**Diferenças entre os campos B2\_CMFIM1 e B2\_CM1**

* **B2\_CMFIM1**: utilizado no reprocessamento do custo médio para apurar o **valor unitário do produto.**
* **B2\_CM1**: utilizado durante a movimentação de estoque (quando os usuários estão incluindo movimentos internos, documentos de entrada etc).

Por legado, ao final do processamento da rotina de Custo Médio (MATA330) o valor processado no campo **B2\_CMFIM1** pode ser repassado para o campo **B2\_CM1**, com uso do parametro **MV\_330ATCM = .T.** porém, caso não seja desejado este repasse, é possível realizar alteração por meio do parâmetro **MV\_330ATCM** =.**F**.   
  
**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
