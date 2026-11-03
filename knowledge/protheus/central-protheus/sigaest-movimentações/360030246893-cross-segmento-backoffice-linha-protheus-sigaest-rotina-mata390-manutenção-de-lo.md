---
article_id: 360030246893
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 087154ac20b3107471e48ddb14397754dbc40f4ca2310362ffa95040d7c737a8
fetched_at: '2026-06-28T22:38:54.161721+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina MATA390 - Manutenção
  de Lotes
type: support-article
updated_at: '2026-04-17T15:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030246893-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes
---

A rotina MATA390 ajusta produtos com rastreabilidade por lote, corrigindo saldos entre SB2 (saldo físico/financeiro) e SB8 (saldo por lote). Permite incluir/excluir lotes e ajustar produtos que passaram a ter controle de rastreabilidade. Para ajustes, acessa-se Atualização Movimentação Internas Rastreabilidade Manutenção, preenchendo dados do produto, armazém, data, quantidade e validade do lote, gerando movimentação na tabela SD5.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35983644965143) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Qual a finalidade da rotina de Manutenção de Lotes (MATA390) e como ajustar por meio desta rotina o saldo entre SB2 x SB8 (Saldo físico e financeiro X Saldo de Rastreabilidade por Lote)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A rotina MATA390 tem como objetivo fazer ajustes nos Produtos que contém rastreabilidade por Lote. Estes ajustes podem envolver casos em que um produto não tinha rastreabilidade e passará a ter, ou mesmo caso em que algum produto tenha um saldo na tabela SB2 maior do que tabela SB8

Essa rotina permite pesquisar e visualizar lotes já existentes e incluir/excluir lotes novos (somente lotes incluídos manualmente poderão ser excluídos). A inclusão de lotes deve ser utilizada quando um produto com saldo em estoque e sem controle de rastreabilidade passa a utilizar este controle.

**Como ajustar desbalanceamento de saldo entre a SB2 e a SB8?**  
  
Se houver um produto em que possui um saldo na tabela SB2 que é maior do que o saldo da SD5 **(TABELA QUE GRAVA AS MOVIMENTAÇÕES DOS LOTES)** é gerado um desbalanceamento do saldo do produto. Para realizar o ajuste, basta utilizar a rotina seguindo os seguintes passos:

* Acessar o seguinte caminho **-> Atualização ->Movimentação -> Internas ->Rastreabilidade -> Manutenção**.
* Ao acessar e clicar em "**Incluir**", será apresentada a tela de campos da rotina, onde deverá preencher os campos *Produto, Armazém, Data de Movimento, Quantidade (em que deve constar no Lote) e Validade do Lote*.
* Assim a rotina irá realizar o processo de Ajuste entre sua SB2 x SB8. Este ajuste pode ser visto direto na tabela SD5, no qual gerará uma movimentação da quantidade da diferença.

**Como ajustar Lote para um produto não possuía controle de rastreabilidade e passou a controlar?**

Quando o produto já possui saldo em estoque e será necessário que o mesmo passe a controlar Rastreabilidade, siga os passos abaixo:

* Acesse à rotina MATA390 (**Atualização ->Movimentação -> Internas ->Rastreabilidade -> Manutenção**).
* Ao acessar e clicar em "**Incluir**", será apresentada a tela de campos da rotina, onde deverá preencher os campos: *Produto, Armazém, Data de Movimento, Quantidade (total do produto, caso todo o saldo vá fazer parte deste mesmo lote), Lote (ao qual ele vai pertencer) e Validade do Lote*.

**OBS:** Como a rotina exibe a tabela SD5, para configurações visuais e ajustes de campos via browse por exemplo, será necessário realizar através da tabela em questão(SD5).

Situação relacionada:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Campo BF\_DATAVEN não é exibido na rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13439653954839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-Campo-BF-DATAVEN-n%C3%A3o-%C3%A9-exibido-na-rotina)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina Automática ExecAuto MATA390 - Manutenção de Lotes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38167891160343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-Autom%C3%A1tica-ExecAuto-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes)

**Saiba mais:**

[Clique aqui e saiba mais sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
