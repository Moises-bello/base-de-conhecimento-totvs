---
article_id: 1500007815781
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1bcafbfefa694648e30c861e0382794c9eb01d8a445d5eb671f61e24944b9bbb
fetched_at: '2026-06-28T22:38:54.399579+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar um Documento
  de Entrada para atender à uma Ordem de Produção (OP)?
type: support-article
updated_at: '2023-09-11T14:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007815781-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-Documento-de-Entrada-para-atender-%C3%A0-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP
---

**Dúvida**Possuo uma Ordem de Produção em aberto, porém preciso comprar produtos para atender a OP. É possível na Nota de Entrada gerar automaticamente um empenho para a minha Ordem de Produção

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

É possível dar entrada numa Nota Fiscal mencionando a OP, desta forma, automaticamente é gerado o empenho do produto filho contido na estrutura do produto final. Veja abaixo um exemplo:

**Cenário para exemplificação:**

Teremos o produto PA81 e MP81, numa estrutura de 1:1 entre os dois (1 MP81 para 1 PA81).

Quantidade Atual PA81: 0

Quantidade Atual MP81: 0

**1° Passo - Abertura de Ordem de Produção de quantidade 50 do PA81:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011611142)

**2° Passo - Como não temos saldo físico do produto MP81 para atender à OP, iremos comprar 50 itens, mencionando que essa compra é exclusivamente para atender à OP criada.**

![Criando_Doc_de_Entrada_para_a_OP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011644462)

Com isso, é feita automaticamente uma Requisição para atender à OP, ela é gerada diretamente na tabela de Movimentações Internas (SD3), com o tipo de movimento **RE5**(Requisição para OP informando na nota fiscal de entrada).

Sendo assim, temos quantidade suficiente do MP81, já com requisição, para atender à produção.

**3° Passo - Apontamento da Produção do PA81**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011646462)

**Passo 4° - Visualização do saldo do PA81:**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011925941)**

**Como faço para excluir um Documento de Entrada feito para atender uma Ordem de Produção?**

Caso haja a necessidade de excluir o Documento de Entrada neste cenário, deve-se excluir o Apontamento da Produção (MATA250) ao qual o saldo comprado foi utilizado. Em alguns cenários, quando se movimentou o saldo posterior ao Apontamento, estes devem ser estornados também para que consiga efetuar o estorno do Apontamento para depois a Exclusão da Nota Fiscal de Entrada.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
