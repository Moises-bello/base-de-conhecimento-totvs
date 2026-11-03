---
article_id: 360020672612
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c53c8573a37680ab109c0531be05d69c7cd37e76979d14f6893467b7d876f541
fetched_at: '2026-06-28T22:38:53.918675+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como ativar o controle
  de Lote/Rastro para produtos com saldo?
type: support-article
updated_at: '2025-12-15T17:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo
---

O artigo orienta como ativar o controle de Lote/Rastro em produtos com saldo físico no TOTVS Protheus. A recomendação é copiar o código do produto para um novo código com controle de lote ativado. Caso não seja possível, deve-se alterar o parâmetro MV\_RASTRO para "S", ajustar o saldo por lote na rotina MATA390 e incluir os lotes correspondentes. Após isso, o produto controla saldo físico, financeiro e por lote.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21742090034327)** **Tempo aproximado para leitura:****00:04:30 min**

**Dúvida**

Como pdoemos ativar o controle de **Lote/Rastro** para produtos que possuem saldo Físico (SB2) e ja tino sistema?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Sugestão:**Veja também no vídeo abaixo as instruções sobre o cenário descrito.

**Observações importantes:** Para esse cenário mais adequado, é realizar a **cópia do Código do Produto** para um **Novo Código de Produto** definindo que esse **Novo Código inicie controlando Lote (B1\_RASTRO=L OU S)**, dessa forma o produto inicia com o conceito de rastro.

**Caso não possa efetuar o procedimento acima**, realize os seguintes passos:

**- 1 -** Alterar o parâmetro **MV\_RASTRO** para **S (Sim)** no módulo Configurador

**- 2 -** Revisar o **saldo** do(s) produto(s) para que faça a inclusão ***exatamente*** **de todo o Saldo** nos lotes correspondentes;

**Exemplo:** O produto abaixo consta um saldo de quantidade 100 no Armazém 01.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7151903739287)

**-3 -**Alterar o campo Rastro (B1\_RASTRO) para iniciar o controle de Lote, observe que exibe um alerta para ajustar o saldo por Lote pela rotina MANUTENÇÃO DE LOTES (MATA390);

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7152065125399)

**- 4 -** Acessar a rotina MANUTENÇÃO DE LOTES (MATA390) clicar em incluir e digitar as informações dos novos lotes desejados para todo o saldo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7152089462679)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7152161232663)

***Obs:*** Após efetuado o processo acima, o produto passa a controlar além do saldo físico e financeiro o saldo por lote. Com isso, todo saldo que for movimentado ou requisitado deve ser informado o lote e atualizará as tabelas referenciadas, abaixo segue o fluxo de movimentação dos saldos e as principais tabelas envolvidas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7151783400983)

|  |
| --- |
| ***Informações importantes:***  Para os casos em que esta incluindo um produto que ainda não teve um Saldo Inicial incluido no sistema, deve utilizar a rotina de Saldos Iniciais (MATA220) e informar os Lotes desejados. Veja na FAQ abaixo as instruções passo a passo para esse cenário.    [***SIGAEST - Como incluir Saldo Inicial em um produto que utiliza controle de Lote/Sub-lote?***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005072201-MP-SIGAEST-Como-dar-Saldo-Inicial-em-um-produto-com-Lote-Sub-lote?source=search) |

**Saiba mais:**

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
