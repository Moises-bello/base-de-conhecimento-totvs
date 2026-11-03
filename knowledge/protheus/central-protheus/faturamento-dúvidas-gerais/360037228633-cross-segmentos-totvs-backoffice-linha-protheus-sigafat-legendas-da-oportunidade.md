---
article_id: 360037228633
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 03bb712824e6c087f8c2cadcf946bc337041c2db8b2a946d05154ce53ef5f12b
fetched_at: '2026-06-28T22:38:29.994255+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Legendas da
  Oportunidade de Vendas (FATA300) '
type: support-article
updated_at: '2023-08-25T11:53:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037228633-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Legendas-da-Oportunidade-de-Vendas-FATA300
---

**Dúvida**

Como funcionam as legendas da Oportunidade de Vendas (FATA300)?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução**

A Rotina de Oportunidade de Vendas possui um conjunto de legendas para indicar o status de seu processo de conclusão.

**OPORTUNIDADE**  
A primeira coluna de legendas demonstra o Status da Oportunidade, demonstrando visualmente o conteúdo do campo **AD1\_STATUS (Status da Oportunidade)**

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048918973)

**PROCESSO DE VENDA**  
A Segunda coluna de legendas demonstra o prazo do Processo de Venda, ao criar um processo de vendas (FATA010) é possível estabelecer, nos campos **AC2\_DDURAC (Dias de duração) e AC2\_HDURAC (Hr. Duração)**, a quantidade de dias/horas de duração do estágio do processo de vendas:

![02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048918993)

O prazo do processo de venda fica em alerta ou em atraso quando a **soma de todos os AC2\_DDURAC (Dias de duração) e AC2\_HDURAC (Hr. Duração)** está próxima de exceder ou excedido:

![03.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048919013)

**EVOLUÇÃO DE VENDA**  
A terceira coluna demonstra os prazos de evolução da venda, ela indica alerta ou atraso na conclusão do estágio de venda.

![04.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048919053)

Quando estabelecido um prazo para conclusão do estágio nos campos **AC2\_DDURAC (Dias de duração) e AC2\_HDURAC (Hr. Duração)**, essa legenda indicará o **Status do Estágio da oportunidade (AD1\_STAGE)**.

**Saiba mais**: [Oportunidades (FATA300 - SIGAFAT)](https://tdn.totvs.com/pages/releaseview.action?pageId=362450568)
