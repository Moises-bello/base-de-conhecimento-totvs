---
article_id: 21683091212183
category: Faturamento - Cadastros
content_hash: 04690ff159d805e6cf44d64057286278478b89edf67941680ff5a65c1b98a6a6
fetched_at: '2026-06-28T22:38:36.794727+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo B
type: support-article
updated_at: '2024-03-04T18:56:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21683091212183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-B
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21683123004823) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo B?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

É possível combinar as condições de pagamento em uma só (Exceto as do Tipo 9/A/B).

**Exemplo em vídeo de como criar (How To Tutorial):**

Para isso é utilizado o item da rotina e configurado para cada uma seu tipo e a participação para compor o total da condição de pagamento única (rateio), para isso é utilizada a “Tabela SEC - Desmembramento de Condições de Pagamento”.

Na janela de inclusão de condição de pagamento, a área superior apresenta os campos para definição dos tipos das condições de pagamento já existentes; a área inferior, apresenta linhas para definição dos itens quando a Condição de Pagamento for Tipo B (E4\_TIPO = B), neste caso, somente os campos definidos nos itens serão considerados para o cálculo dos vencimentos das duplicatas.

**Cadastrando (misturando uma condição de pagamento do Tipo 1 e uma Tipo 5):**

OBS: No exemplo, data da emissão fiscal de saída (ou simulação), gerada por um pedido de venda no dia 01/01/2022:

E4\_CODIGO = (critério do usuário)

E4\_TIPO = B

E4\_COND = 0 (o sistema desconsidera esta informação, pois trata-se do tipo B, esse campo é obrigatório, deve-se digitar qualquer valor)

E4\_DESCRI = (critério do usuário)

**Linha 1:**

EC\_ITEM = 01

EC\_TIPO = 1

EC\_COND = 00,30,90 (3 parcelas nesta linha)

EC\_RATEIO = 60

**Linha 2:**

EC\_ITEM = 02

EC\_TIPO = 5

EC\_COND = 30,3,30 (3 parcelas nesta linha)

EC\_RATEIO = 40

**Valor total de um pedido de vendas = R$1000,00 (para o exemplo de resultado à seguir:**

* Parcela 1: Valor da parcela R$200 - Data de vencimento da parcela: 01/01/2022
* Parcela 2: Valor da parcela R$200 - Data de vencimento da parcela: 31/01/2022
* Parcela 3: Valor da parcela R$200 - Data de vencimento da parcela: 01/04/2022
* Parcela 4: Valor da parcela R$133,33 - Data de vencimento da parcela: 01/05/2022
* Parcela 5: Valor da parcela R$133,33 - Data de vencimento da parcela: 31/01/2022
* Parcela 6: Valor da parcela R$133,34- Data de vencimento da parcela: 30/06/2022

O campo Rateio “EC\_RATEIO” é responsável por determinar a porcentagem em relação ao total das parcelas que será acumulada naquela condição de pagamento. A soma dos campos “EC\_RATEIO” deve resultar em 100 (100% do valor assimilado).

No exemplo acima, na linha 1, há a Condição de Pagamento Tipo 1 e, nela será concentrado 60% do valor (R$600) para ser distribuida conforme sua regra. Na linha 2, há a Condição de Pagamento Tipo 5 e, nela será concentrado 40% do valor (R$400) para ser distribuida conforme sua regra.

**MV\_AGLDUPB - Parâmetro que define se quando existirem duplicatas com a mesma data de vencimento, estas deverão ser aglutinadas. Indica se para o cálculo dos vencimentos, será aplicada a data do último título gerado como referência para a próxima condição**

* (1=Atualiza) ou será utilizada sempre a data inicial
* (2-Inicial).

Exemplos de utilização desse parâmetro no tópico "Parâmetros" da documentação "**Todas as Condições de Pagamento (MATA360)**" do Saiba Mais.

**GIF Exemplo do resultado da simulação utilizando uma condição de pagamento Tipo B (Tipo B - E4\_TIPO = “B”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipob.gif?version=1&modificationDate=1656449435757&api=v2)

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)

**[Preenchimento do campo "Tipo" (EC\_TIPO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535712844951-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Tipo-EC-TIPO)**

**[Preenchimento do campo "Cond. Pagto" (EC\_COND)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535799142295-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Cond-Pagto-EC-COND)**

**[Preenchimento do campo "% Rateio" (EC\_RATEIO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11536015641879-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Rateio-EC-RATEIO)**

**[Preenchimento do campo "Item" (EC\_ITEM)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535601660055-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Item-EC-ITEM)**
