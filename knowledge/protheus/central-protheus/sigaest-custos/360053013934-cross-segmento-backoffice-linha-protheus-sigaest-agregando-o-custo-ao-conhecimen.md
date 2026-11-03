---
article_id: 360053013934
category: SIGAEST - CUSTOS
content_hash: 54913f8f3f81d0e46a9ba35da2920b75e120e007cc592fa8a4200e6ae0bce786
fetched_at: '2026-06-28T22:39:00.294281+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Agregando o Custo
  ao Conhecimento de Frete
type: support-article
updated_at: '2025-09-30T18:35:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053013934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Agregando-o-Custo-ao-Conhecimento-de-Frete
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35307183572375) Tempo aproximado para leitura: **00:04:20 min****

**Dúvida**

Como devo agregar o Custo de Conhecimento de Frete ao meu produto a partir de um Documento de Entrada (MATA103)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Conhecimento de Frete é um processo muito comum em compras feitas, porém neste caso abordaremos, em passo a passo, como fazer este valor agregar ao Custo do Produto.

***Sugestão*:** Assista também ao How To que apresentamos sobre como agregar o Custo ao Conhecimento de Frete:

#### 

#### **Informação importante: Para que o Custo seja agregado ao Conhecimento de Frete, no momento da execução da rotina MATA116, deve-se utilizar TES com F4\_ESTOQUE = S**

**1 - Possuir um produto cadastrado (cadastraremos um produto para exemplo).**

No menu do Estoque/Custos, acesse: Atualizações/Cadastro/Produtos (MATA010):

![20200902_090856.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360088749493)

**2 - Fazer uma nota de entrada com o(s) produto(s) adquiridos:**

 No menu do Estoque/Custos irá acessar Atualizações/Movimentações/Fiscais/Documento de Entrada (MATA103):

![20200902_091842.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360087613774)

**3 - Após dar entrada em uma nota fiscal, iremos fazer o complemento do custo á nota do conhecimento de frete**

No menu do Estoque/Custos irá acessar Atualizações/Movimentações/Fiscais/Conhecimento de Frete (MATA116):

![20200902_092327.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360088755413)

**4 - Para checar se realmente se o conhecimento agregou ao custo do produto, emita o relatório Kardex por Período.**

 No menu do Estoque/Custos irá acessar Relatórios/Movimentações/Kardex/Por Período (MATR900):

![20200902_093514.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360088755713)

Sendo assim, o Conhecimento do Frete agrega ao Custo do Produto.

|  |
| --- |
| **Outro exemplo importante a ser observado:** Quando efetuada a inclusão de um Documento de entrada com mais de 1 item e deseja que o Custo do frete seja apropriado apenas para alguns itens específicos. Veja abaixo passo a passo com exemplo: |

**- 1 -** Inclusão de um Documento de Entrada com 03 itens, nesse exemplo quantidade 1 e valor R$ 100,00 para cada item;

![DOCUMENTO ENTRADA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/35307183575319)

**- 2 -** Observe o resultado antes da inclusão do Conhecimento de Frete;

![CONSULTA ANTES INCLUIR FRETE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/35307180538007)

**- 3 -** Inclusão do Conhecimento de Frete no Valor de R$ 20,00 e nesse cenário, precisa que apenas o item 1 da nota de Entrada seja considerado para apropriação do Custo do Frete. **Nesse caso**, deve deletar os demais itens e digitar manualmente o Custo de R$ 20,00 para o item 1;

![DOCUMENTO ENTRADA FRETE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/35307180542231)

**- 4 -** Observe o resultado após a inclusão do Conhecimento de Frete, o custo foi apropriado apenas ao item 1 da Nota de Entrada como desejado;

![CONSULTA APOS INCLUIR FRETE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/35307180543383)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
