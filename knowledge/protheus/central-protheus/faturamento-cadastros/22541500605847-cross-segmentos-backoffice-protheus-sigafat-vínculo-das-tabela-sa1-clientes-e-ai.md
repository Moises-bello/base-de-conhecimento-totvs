---
article_id: 22541500605847
category: Faturamento - Cadastros
content_hash: 0e348b03e35226171a434da875c5359763cbc91e620dce2622b6b322fc3fe6f6
fetched_at: '2026-06-28T22:38:35.483450+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Vínculo das tabela SA1 (Clientes)
  e AI0 (Complemento de Clientes)
type: support-article
updated_at: '2025-01-28T14:21:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22541500605847-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-V%C3%ADnculo-das-tabela-SA1-Clientes-e-AI0-Complemento-de-Clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22541500552215) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Qual o vínculo das tabela SA1 (Clientes) e AI0 (Complemento de Clientes)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

A tabela AI0 só será gravada (feito a relação com a SA1) quando no cadastro do cliente, ser acrescentado alguma informação em qualquer campo da tabela AI0, ai é criado o vínculo.

O campo "Código do cliente (A1\_COD)" tem seu valor levado como chave estrangeira ao campo "Código do cliente (AI0\_CODCLI).

(Isso ocorre para não sobrecarregar o banco de dados, ou seja, não ter sempre a AI0 independente de uso):

> ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29557170096279)
