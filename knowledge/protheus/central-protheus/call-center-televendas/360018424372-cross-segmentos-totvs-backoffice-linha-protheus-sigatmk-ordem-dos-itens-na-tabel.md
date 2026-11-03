---
article_id: 360018424372
category: Call Center - Televendas
content_hash: b455223cee31bd1df0ace2d00434f3e76fc7233e42f986c5108c46404460f7af
fetched_at: '2026-06-28T22:41:30.339583+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Ordem dos itens na
  tabela de preços interfere no comportamento do Televendas -DA1_ESTADO
type: support-article
updated_at: '2022-06-22T19:15:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018424372-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ordem-dos-itens-na-tabela-de-pre%C3%A7os-interfere-no-comportamento-do-Televendas-DA1-ESTADO
---

**Dúvida**

Ordem dos itens na tabela de preços interfere no comportamento do Televendas (DA1\_ESTADO).  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- a partir da versão 11.  
  
  
**Solução**

Segue o exemplo:

Cadastrar:

**1.1- TABELA DE PREÇO**(exemplo)

ITEM     PRODUTO           PREÇO DE VENDA           DA1\_ESTADO

0001     PROD-A                  500,00                              BA (preenchido)

0002     PROD-A                1000,00                              GLOBAL (vazio)

**1.2- CLIENTE**

Estado = BA

**1.3- INCLUIR UM ATENDIMENTO NO TELEVENDAS**

- Cliente da Bahia = mesmo do item 1.2

- Operação = Faturamento

**1.4- SELECIONAR, PROD-A NO ACOLS**

Verificar que o Sistema  não processa a tabela de preços

**1.5- CONCEITO:**

No exemplo 1.1(mesmo Produto), entende-se que o Estado da Bahia também está compreendido no intervalo global.

Neste caso, não será possível alterações no funcionamento da rotina padrão, uma vez que poderá impactar na usabilidade dos demais clientes.

**1.6- OPCÕES DE TRABALHO:**

1.6.1- Realizar o ajuste manual da tabela, deixando o **registro que****não possui Estado** informado(default), **na primeira linha.**

1.6.2- Utilizar de pontos de entrada.
