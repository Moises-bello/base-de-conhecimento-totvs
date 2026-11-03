---
article_id: 5986881139607
category: SIGAEST - CUSTOS
content_hash: 062ab848590e4a2551d4839556dd01fe65074195e7cfdc2e306bc68e96316602
fetched_at: '2026-06-28T22:39:02.286041+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é um produto
  do tipo MOD e GGF?
type: support-article
updated_at: '2025-11-18T20:58:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5986881139607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-que-%C3%A9-um-produto-do-tipo-MOD-e-GGF
---

O artigo explica que MOD (Mão de Obra) refere-se ao custo do trabalho manual na fabricação, enquanto GGF (Gastos Gerais de Fabricação) são custos indiretos da produção. No Protheus, MOD e GGF são tratados como produto tipo MOD, podendo ser cadastrados vinculados a centros de custo. O cálculo do custo MOD varia conforme a integração contábil, e o custeamento é realizado via recálculo do custo médio.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36426496705687) Tempo aproximado para leitura: **00:03:30 min**

**Dúvida**

O que é um produto do tipo MOD (Mão de Obra) e GGF (Gastos Gerais de Fabricação)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O objetivo deste documento de referência é explicar o conceito de **Mão de Obra (MOD)**, sua regra de negócio e como o sistema Protheus trata produtos do tipo Mão de Obra e informar oque é um produto do tipo **GGF (Gastos gerais de fabricação).**

**O que é a MOD (Mão de Obra)?**

Mão de obra é o termo utilizado para se referir, geralmente, ao trabalho manual empregado na fabricação de um bem ou serviço.

O custo da MOD representa a parcela de custo que o trabalho empregado representa no custo total do produto ou bem gerado.

**Exemplo:**

Na produção de um copo de vidro foi empregada uma mão de obra que é o funcionário que molda o vidro. O custo desse trabalhador deve ser

embutido no custo total do copo de vidro para que a venda do mesmo possa custear a mão de obra utilizada na fabricação.

**O que são os GGFs (Gastos Gerais de Fabricação)?**

GGF são gastos envolvidos direta ou indiretamente na produção do produto. Mas que não podem ser apropriados diretamente a cada unidade produzida.

**Exemplo:**

Água, energia elétrica, depreciação de máquinas, aluguel do prédio e etc...

**Produto MOD no Protheus.**

O Protheus trata o custo da mão de obra e dos gastos gerais de fabricação em um único tipo de produto, o produto tipo MOD.

Logo, podemos entender que no sistema o MOD é:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5986754059543)

É possível incluir no sistema um produto MOD de **duas maneiras:**

* Cadastrar o produto com o campo Código **(B1\_COD) = MOD + Código do Centro de Custo**  
  **Importante:** Essa forma de cadastrar irá fazer com que todo valor do centro de custo seja alocado no produto.
* Informar o campo **CC p/ Custo (B1\_CCCUSTO) = Código do Centro de Custo.**  
  **Importante:** Se for necessário dividir o valor do centro de custo entre mais de um produto, informar o campo **Gr Cnt Custo (B1\_GCCUSTO),** para utilizar o conceito de **Grupo dentro do Centro de Custo.**

**Fluxo de processo do produto MOD.**

Conforme dito anteriormente, há duas formas de fazer o processo de um produto **MOD dentro de um período:**

**Sem integração contábil**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5986786276887)

*Nesse processo o cálculo do custo da MOD é feito da seguinte forma pelo sistema:*

**Custo da Movimentação do MOD** = Custo Médio do Produto MOD **(B2\_CM1) \* Quantidade da Requisição do produto MOD para a OP (D3\_QUANT)**

**Com integração contábil**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5986832723351)**

*Nesse processo o cálculo do custo da MOD é feito da seguinte forma pelo sistema:*

**Custo da Movimentação do MOD** = (Soma dos Lançamentos Contábeis no Centro de Custo **(CT2\_VALOR) / Soma das Quantidades Requisitadas do produto MOD para a OP (D3\_QUANT)) \* Quantidade da Requisição do produto MOD para a OP (D3\_QUANT)**

**Importante:** Ao executar o Recálculo do Custo Médio, a pergunta "Calcula MOD" deve estar como "Sim", pois o custeamento das requisições de MOD e do produto acabado é realizado ao rodar o Recálculo do Custo Médio, através da obtenção do saldo no centro de custo atrelado, e valorizando os movimentos de MOD de acordo com os valores obtidos.

**Importante:** O suporte não orienta em processo de implantação para utilização dos tipos de produto MOD ou GGF, devem ser verificados internamente por conta do cliente e ou analista consultor in loco, para entendimento da regra de negócios.

Para um passo a passo mais detalhado verifique o documento abaixo em Saiba mais.

**Saiba mais**

[(Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF com e sem integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)
