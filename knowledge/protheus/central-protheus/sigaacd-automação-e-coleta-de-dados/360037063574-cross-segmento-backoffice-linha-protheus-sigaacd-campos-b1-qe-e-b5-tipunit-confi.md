---
article_id: 360037063574
category: SIGAACD - Automação e Coleta de Dados
content_hash: 27266f790c89fef23df7111c871e165a5dca6824da570f3e457a868fafa43854
fetched_at: '2026-06-28T22:39:11.123645+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Campos B1_QE e B5_TIPUNIT
  configuração. '
type: support-article
updated_at: '2023-09-20T21:47:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037063574-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Campos-B1-QE-e-B5-TIPUNIT-configura%C3%A7%C3%A3o
---

**Dúvida**

Configuração correta de como funciona o campo **B1\_QE** e **B5\_TIPUNIT** no SIGAACD.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.

**Solução:**  
Campo impacta diretamente nos processos do SIGAACD, ao gerar uma ordem separação, inventario e outras rotinas que requer etiqueta do produto.  
  
Conceitualmente o tratamento do campo B1\_QE dá-se para os processos de compras relativos ao lote econômico e também define a quantidade interna do volume da etiqueta, onde é feito um cálculo de multiplicação desta quantidade do campo pela quantidade informada na separação.

Por exemplo, se informada uma quantidade de  60 no campo e , separação com 50, isto indicará que serão, 60 volumes com 50 unidades internas, logo serão necessário uma quantidade de 3000 no estoque. Para atender esta necessidade, será necessária a utilização do ponto de entrada **[CBQTDVAR](https://tdn.totvs.com/pages/releaseview.action?pageId=6091003)**para isolar esta definição de lote econômico de compras e permitir a separação de forma unitária .  
  
Os produtos utilizados na integração com o módulo  SIGAACD, possuem o campo B1\_QE preenchido. Quando se faz  movimentações através do módulo SIGAACD, estas já estão sendo referenciadas pela quantidade vinculada no campo B1\_QE.

**Exemplo**:

A transferência entre armazéns, onde consta a quantidade 1 no campo B1\_QE=24, o resultado desta  transferência realizada será de 24, quando o campo B1\_QE não estiver preenchido, será realizado a transferência de uma unidade apenas.  
  
A configuração é realizada através do campo **B5\_TIPUNIT**  que desconsiderará o campo **B1\_QE**.

Quando informado o código do produto é verificado o campo **Tipo Unit -** **B5\_TIPUNIT.** Caso esteja como **1(Sim)**, retornará o valor do campo **Qtd.Emb.Lei -** **B5\_QEL,** do contrário retornará 1.

**Processo de Embalagem por Ordem de Separação por Pedido de Venda:**

Apresenta o Help abaixo quando realiza uma embalagem com o campo **B5\_TIPUNIT** igual a NÃO.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17694770909719)

**Solução:**

Para a tratativa dessa mensagem é necessário o uso do Ponto de entrada [CBRETEAN](https://tdn.totvs.com/pages/releaseview.action?pageId=6091038)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
