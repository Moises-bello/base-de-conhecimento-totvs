---
article_id: 21251019303959
category: Faturamento - Cenários de Venda
content_hash: 1da964ec695e7108b20d350b9c167356b74a62af1c586f7d76550193a415f7b5
fetched_at: '2026-06-28T22:38:34.104954+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus – SIGAFAT – Help NODELETA ao excluir
  tabela de preços (OMSA010)
type: support-article
updated_at: '2025-01-15T19:43:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21251019303959-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-NODELETA-ao-excluir-tabela-de-pre%C3%A7os-OMSA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21251066272151) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Ao excluir tabela de preços o Help "NODELETA" aparece, como resolver?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões;

**Solução**

Por questões de integridade de banco de dados, não é possível excluir um registro que está inserido em outra tabela (chave primária em outra tabela como chave estrangeira).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21251066276119)

Ao excluir e esse Help aparecer, significa que a tabela de preços a ser excluída está em outra tabela como chave estrangeira.

**OBSERVAÇÃO:** Se o campo "Código da Publicação (DA0\_CODPUB)" estiver preenchido, a tabela não poderá ser excluída pois foi gerada pela rotina "Publicação de Preços".

**Verifique se a tabela não está nos campos:**

ACO\_CODTAB (Tabela ACO - Regras de Desconto)  
ACQ\_CODTAB (Tabela ACQ - Regras de Bonificação)  
ACT\_CODTAB (Tabela ACT - Itens da regra de negócio)  
ADA\_TABELA (Tabela ADA - Contrato de parceria  
AB3\_TABELA (Tabela AB3 - Orçamento técnico)  
AAT\_TABELA (Tabela AAT - Vistoria Técnica Cabeçalho)

Nas demais filiais, só será possível excluir a tabela de preços, caso ela não esteja em nenhum registro das tabelas/campos acima. Para excluir, basta excluir os registros que a possuem pelo Protheus.
