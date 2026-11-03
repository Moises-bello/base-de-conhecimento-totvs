---
article_id: 8552373360023
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 82d53923441befc78f0529215fd9e7b500a5edba4edf0f09df667978ee5e8e43
fetched_at: '2026-06-28T22:38:57.109202+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 MATA311 -
  Como configurar tabela de preços para as Transferências?
type: support-article
updated_at: '2022-08-31T19:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8552373360023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-tabela-de-pre%C3%A7os-para-as-Transfer%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar tabela de preços para as rotinas de Transferências entre Filiais MATA310 e MATA311?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

***1 -*** Primeiramente incluir uma Tabela de Preços na rotina OMSA010:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8553393223447/mceclip0.png)

***2 -*** Definir na linha de itens o produto que será transferido e o preço de venda e confirmar;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8553692303511/mceclip1.png)

***3 -*** No cadastro de Clientes (Filial Destino) no campo Tabela (A1\_TABELA) informar a tabela criada para a Filial de destino:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8561483116823/mceclip0.png)

***4 -*** Para a rotina MATA310 verificar o parâmetro "Considerar como preço no PV" e selecionar a opção Tabela de Preço:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8553864838679/mceclip2.png)

***5 -*** Para a rotina de Solicitação de Transferências (MATA311) deve configurar o parâmetro ***[MV\_TPCUSST igual a  1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-definir-o-Pre%C3%A7o-de-Venda-do-Pedido-de-Venda-derivado-do-processo-de-Transfer%C3%AAncia-entre-Filiais-)***;

Após as configurações acima o Preço de Venda definido nas Tabelas de preços para os produtos sempre serão considerados como indicado. Caso não informar o produto na Tabela de Preço, é considerado por padrão o Preço de Venda a R$ 1,00.

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
