---
article_id: 38427361406487
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b6681737e7ed518ced7e7a4852741fad616c7a15de534f63afc26db853ccb8ee
fetched_at: '2026-06-28T22:38:55.618588+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help: SLDBLQSB2 -
  O saldo do produto deste armazém está Indisponível.'
type: support-article
updated_at: '2026-02-16T13:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38427361406487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-SLDBLQSB2-O-saldo-do-produto-deste-armaz%C3%A9m-est%C3%A1-Indispon%C3%ADvel
---

O artigo explica que o erro "Help: SLDBLQSB2" ocorre quando o status do saldo (B2\_STATUS) de um produto em um armazém está como indisponível no TOTVS Protheus. Para resolver, basta acessar a rotina SALDO ATUAL, localizar o produto, alterar o status para disponível e salvar.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38427385153175) Tempo aproximado para leitura: **00:02:45 min**  
  
**Ocorrência**

Ao tentar efetuar alguma Movimentação de Saldo ou mesmo digitar o Inventario do produto em determinado Armazém apresenta o **Help: SLDBLQSB2**. Como alterar o Saldo ou o Armazém para Disponível?

![help sldblqsb2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/38427477795991)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse incidente ocorre, devido o **STATUS (B2\_STATUS)** do Saldo nesse determinado Armazém estar **marcado como Indisponível**, essa funcionalidade é utilizada quando a empresa precisa indisponibilizar determinado Armazém para Movimentações e inclusive para Consultas ao Saldo em Estoque ([link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)).

![B2_STATUS.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/38427757861655)

**Solução**

Para não apresentar esse Help ou mesmo para alterar o Status do Saldo do produto em determinado Armazém realizar o passo a passo abaixo:

**- 1 -** Acessar a rotinas SALDO ATUAL(MATA225);

**- 2 -**Pesquisar o Produto e Armazém que esta indisponível;

![B2_STATUS 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/38428213926295)

**- 3 -**Clicar e Outras Ações e na Opção **Status**.

![B2_STATUS 03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/38428213927319)

**- 4 -**Alterar o Status para Disponível e clicar em Salvar.

![b2_status 04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38428200199959)

Após esse passo a passo **não apresenta** mais o **Help SLDBLQSB2.**

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)
