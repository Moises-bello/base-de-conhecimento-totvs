---
article_id: 360044369294
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e16e05af3f0a170ea2313d0d340de387474e9ddda0151bea018bf567ea9890da
fetched_at: '2026-06-28T22:38:43.973402+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Ao tentar excluir
  uma nota, o sistema apresenta Help informando que o prazo para o cancelamento da
  nota expirou, porém a nota esta dentro do prazo.
type: support-article
updated_at: '2023-07-20T18:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044369294-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Ao-tentar-excluir-uma-nota-o-sistema-apresenta-Help-informando-que-o-prazo-para-o-cancelamento-da-nota-expirou-por%C3%A9m-a-nota-esta-dentro-do-prazo
---

**Ocorrência**

Ao tentar excluir uma nota, o sistema apresenta Help informando que o prazo para o cancelamento da nota expirou, porém a nota esta dentro do prazo.

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Causa**

O **Help** de **prazo expirado**, tem relação com a configuração do parâmetro **MV\_SPEDEXC**, nele são informadas em até quantas **horas** a **nota** pode ser **excluída**.  
O sistema verifica os campos "**DT Emissao**" (**F2\_EMISSAO**), "**Hora**" (**F2\_HORA**), "**Data de Auto**"  (**F2\_DAUTNFE**) e "**Hora de Auto**" (**F2\_HAUTNFE**) para determinar se a nota está ou não no prazo para ser **cancelada**.

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360061370333)

**Solução**

Para verificar se a nota está ou não no prazo para cancelamento:  
1. Verifique a data e hora de emissão da nota pelos campos "**DT Emissao**" (**F2\_EMISSAO**), "**Hora**" (**F2\_HORA**);  
2. Verifique a data e hora de **Autorização** da nota pelos campos "**Data de Auto**"  (**F2\_DAUTNFE**) e "**Hora** **de Auto**" (**F2\_HAUTNFE**);  
3. Caso a nota realmente tenha expirado seu prazo, ela só poderá ser excluída por cancelamento **extemporâneo**:[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Cancelamento extemporâneo fora do prazo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10017801361687--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Cancelamento-extempor%C3%A2neo-fora-do-prazo)
