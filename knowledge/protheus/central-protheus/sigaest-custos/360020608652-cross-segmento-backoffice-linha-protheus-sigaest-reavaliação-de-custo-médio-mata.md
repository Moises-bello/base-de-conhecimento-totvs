---
article_id: 360020608652
category: SIGAEST - CUSTOS
content_hash: 9c1e00f2a3d2bf0869bd6b98c3f582a71008a424f592723014a9d4c1573e69f2
fetched_at: '2026-06-28T22:39:00.446235+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Reavaliação de Custo
  Médio (MATA338)
type: support-article
updated_at: '2025-03-12T12:18:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23391837779223) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Rotina Reavaliação do Custo Médio (MATA338): como utilizar?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - 11.80 ou superior.  
  
**Solução:**

A rotina de **Reavaliação do Custo Médio** **(****MATA338)** tem por objetivo realizar um ajuste de **valor do custo médio** para um valor pré-definido por sua empresa para **o processo de fechamento do estoque**. Para utilização deste processo o cliente deve verificar se o seu ramo de atividade/legislação permite a execução da mesma.

**Importante:** Diferentemente da movimentação valorizada para acerto de custo no período atual (detalhes **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-MP-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque?source=search)**) Este valor será levado para o **B9\_CM1 e B2\_CM1 do próximo período ficando após todas as movimentações do estoque, e por isso *só deve ser realizado no "Final do mês"*, e o produto precisa ter SALDO FISICO, do contrario o sistema não fara o calculo automatico.**

**Atenção:**

**Esta rotina *não deve* ser utilizada caso o Método de Apropriação seja diferente de Mensal.**

* Se o parâmetro **MV\_CUSFIL = A**, então você pode fazer a reavaliação somente para o Armazém que deseja.

* Se o parâmetro **MV\_CUSFIL = F**, então você deve fazer a reavaliação **para *todos* os armazens** do produto que deseja **na Filial**.
  + **O produto precisa ter *SALDO FISICO em todos os Armazéns*, do contrario o sistema não fara o calculo automatico.**

* Se o parâmetro **MV\_CUSFIL = E**, então você deve fazer a reavaliação **para *todos* os armazens** do produto que deseja em ***todas as Filiais* da Empresa**.
  + **O produto precisa ter *SALDO FISICO em todos os Armazéns*, do contrario o sistema não fara o calculo automatico.**

Para melhor entendimento, veremos um exemplo a seguir com o Produto **PA100**:

Saldo Físico Inicial (SB2) = **0**

Entrada de nota com Quantidade 1 com Custo de **R$ 1.000,00**

Entrada de nota de Quantidade 1 com Custo de **R$ 2.000,00**

**Saldo Atual = 2 peças**

**Custo Total = R$ 3.000,00**

**Custo Médio = R$ 1.500,00**

**Porém iremos definir que  o custo unitário do produto deverá ser de R$ 5000,00.**

Então, via rotina MATA338 informaremos o Custo Unitário que queremos que seja o desejado,

como **R$** **5.000,00**.

Ao processar a rotina de Recalculo do Custo Médio (MATA330) o sistema irá verificar:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Movimento** | **Quantidade** | **Custo do  movimento** | **Quatidade Total Estoque** | **Custo Médio Estoque** | **Custo Total Estoque** |
| **Saldo Inicial** |  |  | **0** | **0** | **0** |
| **Doc. de Entrada** | 1 | 1.000,00 | 1 | 1.000,00 | 1.000,00 |
| **Doc. de Entrada** | 1 | 2.000,00 | 2 | 1.500,00 | 3.000,00 |
| **Reavaliação de Custo** |  | 7.000,00 | 2 | 5.000,00 | 10.000,00 |
| **Fechamento** |  |  | **2** | **5.000,00** | **10.000,00** |

**Saldo = 2 peças**

**Custo Total Atual = R$ 3.000,00**

**Médio Atual = R$ 1.500,00**

**Médio Desejado = R$ 5.000,00**

**Custo Total desejado = R$ 10.000,00**

Então, gravará na tabela SD3 um movimento **DEA** de R$ **7.000,00**, como diferença do saldo financeiro atual e o desejado. Ela também irá gravar, no campo **D3\_CMFIXO** a memória do valor desejado (R$ 5.000,00), e repassará o conteúdo para o campo **B2\_CMFIM1**. e tem como requisito obrigatório o reprocessamento do recalculo do custo médio após inclusão do movimento para obtenção do resultado.

***Importante**:* *É necessário destacar que, caso haja mais de uma moeda definida pelo parâmetro MV\_MOEDACM, a Reavaliação do Custo Médio irá gerar no Kardex uma linha de movimentação para cada moeda, conforme a documentação abaixo:*

* [*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao fazer a Reavaliação do Custo Médio gera várias linhas no Kardex, por que isso ocorre?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20498184810391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-fazer-a-Reavalia%C3%A7%C3%A3o-do-Custo-M%C3%A9dio-gera-v%C3%A1rias-linhas-no-Kardex-por-que-isso-ocorre)

Diferentemente da movimentação valorizada para acerto de custo no período atual (detalhes **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-MP-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque?source=search)**) Este valor será levado para o **B9\_CM1 e B2\_CM1 do próximo período ficando após todas as movimentações do estoque, e por isso só deve ser realizado no "Final do mês", e o produto precisa ter SALDO FISICO, do contrario o sistema não fara o calculo automatico.**

**Saiba mais:**

* [*Reavaliação do Custo Médio (MATA338)*](https://tdn.totvs.com/x/FbT0E)
* [*Cálculo do custo apresentado nos campos B2\_CMFIM1 e B2\_CM1*](https://tdn.totvs.com/x/qdoKDg)
* *[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
