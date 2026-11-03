---
article_id: 360017468312
category: Faturamento - Cadastros
content_hash: 0c0f542f5c645a700e7299a9909547cd6dddc2e3eb529191799b8529ca9d2790
fetched_at: '2026-06-28T22:38:35.436778+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Conceito das Condições de
  Pagamento
type: support-article
updated_at: '2024-04-10T18:58:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Conceito-das-Condi%C3%A7%C3%B5es-de-Pagamento
---

**Dúvida**Qual o conceito das dez condições de pagamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Há 9 tipos de condições de pagamentos mais 1 tipo especial que mistura as condições para uso no processo da Venda.

**OBS:** Caso queira criar alguma condição de pagamento lida a seguir, vá até a opção "Saiba mais" no final desse documento.

[**Condição de pagamento tipo 1**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14178272061463-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-1)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade baixa; É possível determinar a distância dos vencimentos entre as parcelas tendo como base a emissão do documento de saída. Cada espaço entre as vírgulas da estruturação, representa as parcelas e os dias para o vencimento de cada parcela, após a emissão.

[**Condição de pagamento tipo 2**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14191561177879-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-2)

* **Situações em que ela é recomendada:** Recomendado para condições de pagamento de complexidade baixa; Representa o tempo até o vencimento (com um multiplicador), o números das parcelas e o intervalo entre elas também com um multiplicador.

  Nessa condição, o conteúdo código da condição de pagamento (E4\_CODIGO) ajuda na montagem da regra, juntamente com o conteúdo da regra da condição (E4\_COND). O campo da regra [E4\_COND] é o multiplicador do primeiro e terceiros número do código.

[**Condição de pagamento tipo 3**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14307548200215-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-3)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade média; Determina-se os dias até o primeiro vencimento, a quantidade de parcelas e os dias exatos de vencimento. (para o sistema ajustar para os dias colocados).

  O primeiro espaço entre vírgulas simboliza a quantidade parcelas. O segundo espaço entre vírgulas simboliza os dias de intervalo até o vencimento da primeira parcela. O terceiro espaço entre vírgulas para frente simboliza os dias do mês em que o vencimento será reajustado para cair caso naturalmente não caia após o primeiro intervalo.

[**Condição de pagamento tipo 4**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21677974135447-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-4)

* **Situações em que ela é recomendada:** Recomendado para condições de pagamento com média complexidade; Declara-se a quantidade de parcelas, o intervalo entre estas e o dia da semana padrão de vencimento.

[**Condição de pagamento tipo 5**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678177657367-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-5)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade baixa; Determina-se os dias até o primeiro vencimento, a quantidade de parcelas e a carência entre elas.

[**Condição de pagamento tipo 6**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678283458455-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-6)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade alta; Determina-se a quantidade de parcelas, o tempo em dias) até o início dos pagamentos, o dia da semana que o vencimento pode cair e a carência entre os vencimentos das parcelas (duplicatas).

[**Condição de pagamento tipo 7**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678463843991-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-7)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade muito alta; O primeiro algarismo simboliza a quantidade de parcelas, seguido dos dias do mês de cada mês que as parcelas cairão.

[**Condição de pagamento tipo 8**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678582446999-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-8)

* **Situações em que ela é recomendada:** Recomendado para condições de complexidade muito alta;

  Determinado com dois blocos numéricos. O primeiro determina a distância de dias para o vencimento das duplicatas (a partir da emissão da nota fiscal, assim como a condição de pagamento do Tipo 1).

  O segundo determina a porcentagem de pagamento em relação ao total das duplicatas a ser paga nas respectivas parcelas.

[**Condição de pagamento tipo 9**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21682807800471-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-9)

* **Situações em que ela é recomendada:** Recomendado para condições da mais extrema complexidade, onde caso nenhum dos Tipos de Condição disponíveis atenda plenamente a particularidade de sua necessidade.

  Determina-se manualmente no pedido de vendas (Rotina MATA410 - Tabela SC5), a data das parcelas e os valores das parcelas.  
  O cadastro é feito na rotina Condições de Pagamento - [Rotina MATA360 - Tabela SE4], mas a configuração dos valores das parcelas e data de vencimento das parcelas é informada na rotina Pedidos de Vendas - [Rotina MATA410 - Tabela SC5] ou Orçamentos de Vendas - [Rotina MATA415 - Tabela SCJ].

**Condição de pagamento tipo A**

* **Orientamos que contate as equipes** de Automação Comercial **SIGAVEI** (**Veículos**) e **SIGAOFI** (**Oficina**).  
  Para tratamento relacionado a condição de pagamento para tratamento de formas de pagamento Nt2020.006, **opção 90 - Sem Pagamento/**TAG **<tPag>, cheque**: **[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tPag-forma-de-pagamento-duplicata-fatura-)**

[**Condição de pagamento tipo B**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21683091212183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-B)

* **Situações em que ela é recomendada:** É possível combinar as condições de pagamento em uma só (Exceto as do Tipo 9/A/B).

  Para isso é utilizado o item da rotina e configurado para cada uma seu tipo e a participação para compor o total da condição de pagamento única (rateio), para isso é utilizada a “Tabela SEC - Desmembramento de Condições de Pagamento”.

  Na janela de inclusão de condição de pagamento, a área superior apresenta os campos para definição dos tipos das condições de pagamento já existentes; a área inferior, apresenta linhas para definição dos itens quando a Condição de Pagamento for Tipo B (E4\_TIPO = B), neste caso, somente os campos definidos nos itens serão considerados para o cálculo dos vencimentos das duplicatas.

**Saiba Mais:**

**[Todas as Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)**

**[Criação da condição de pagamento Tipo 1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14178272061463-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-1)**

**[Criação da condição de pagamento Tipo 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14191561177879-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-2)**

**[Criação da condição de pagamento Tipo 3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14307548200215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-3)**

**[Criação da condição de pagamento Tipo 4](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21677974135447-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-4)**

**[Criação da condição de pagamento Tipo 5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678177657367-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-5)**

**[Criação da condição de pagamento Tipo 6](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678283458455-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-6)**

**[Criação da condição de pagamento Tipo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678463843991-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-7)**

**[Criação da condição de pagamento Tipo 8](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678582446999-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-8)**

**[Criação da condição de pagamento Tipo 9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21682807800471-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-9)**

**[Criação da condição de pagamento Tipo B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21683091212183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-B)**
