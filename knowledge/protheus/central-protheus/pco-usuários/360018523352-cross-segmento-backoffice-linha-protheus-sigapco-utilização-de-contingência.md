---
article_id: 360018523352
category: PCO - Usuários
content_hash: b407bef007b0c0fab972bc7305ed47b2a62d5b97f7dbc76ab0565463c4f8338c
fetched_at: '2026-06-28T22:37:08.228087+00:00'
product: protheus
section_id: 1500001539861
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO Utilização de Contingência
type: support-article
updated_at: '2024-02-13T20:58:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Utiliza%C3%A7%C3%A3o-de-Conting%C3%AAncia
---

**Dúvida**Como utilizar a contingência no módulo PCO?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Ao preparar o módulo **Planejamento e Controle Orçamentário (SIGAPCO)** para a utilização de bloqueios e contingências é necessário:

* Que o parâmetro **MV\_PCOSDCT** (controla o saldo de contingência) tenha seu conteúdo configurado com verdadeiro (.T. = true);
* Cadastrar além dos bloqueios e lançamentos referentes aos processos que se  deseja fazer o controle, também é necessário fazer o cadastro do lançamento de **LIBERAÇÃO DE SOLICITAÇÃO DE CONTINGÊNCIA (000356)**  **Item 01 (Liberação de solicitação de contingência - lançamento de contingência) e o item 02 (Liberação de solicitação de contingência - empenho de contingência) em caso de controle do empenho.**

-> Item 01 Configurar o valor a ser orçado para a contingência.

-> Item 02 Configurar o valor empenhado na solicitação da Contingência

Segue exemplo utilizando lançamento e empenho de contingência:

 Tipos de Saldos

* OR = ORCADO
* CT = CONTINGENCIA
* RE = REALIZADO
* EM = EMPENHO

Configurações tipo de bloqueio:

               Previsto = Soma dos Tipos de Saldos orçado e contingencia

                                               ( OR + CT )

               Realizado = Soma dos Tipos de Saldos realizado e empenhado

                                               ( RE + EM )

Processo 000052- Pedidos de Compras

Considere um pedido no valor de 25.000,00

Orçado = 10.000,00

Neste caso é solicitada uma contingencia de 15.000,00.

Após inserir o pedido de compra é gerado um lançamento referente ao bloqueio de 25.000,00 reais

Ao solicitar a contingencia de 15.000,00 deve se empenhar os 10.000,00 reais por meio do processo de lançamento 000356 item 02 no tipo de saldo EM

* OR - 10000 (crédito)
* RE – 25000  (crédito)
* EM - 10000 (crédito)

Ao liberar a contingencia de 15.000,00 terá que marcar na tela apropriando-se desta contingencia.

Neste momento, ao solicitar o processo de lançamento 000356 item 01 que deve ter 2 sequencias

Sequencia 01 -> Deve incluir um lançamento no tipo de saldo CT no valor de 15000

Sequencia 02 -> Deve ter valor do empenho (000356 item 02) para anular valor no tipo de saldo EM.

* OR = 10000 (crédito)
* CT = 15000 (crédito)
* RE = 25000 (crédito)
* EM =10000 (débito)
