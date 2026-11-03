---
article_id: 360026076693
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 12b8fb8abbf0cbf892810edc205a742683d594febae9928a0c7d3dcea112f18e
fetched_at: '2026-06-28T22:38:41.034949+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - HELP A410NOEMP
type: support-article
updated_at: '2021-09-22T19:42:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026076693-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-HELP-A410NOEMP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min***

**Ocorrência**Como tratar o HELP A410NOEMP na associação da Ordem de Produção no botão beneficia?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12

**Causa**

O Help A410NOEMP, que indica que o tipo do pedido**,** produto ou tipo de saída é inválido para a utilização deste recurso, é apresentado sempre que uma das configurações necessárias para o vínculo da Ordem de Produção com o Pedido de vendas não for atendida.

**Solução**

Na inclusão do pedido de vendas, devem ser atendidos os requisitos abaixo:

- O Tipo do Pedido (**C5\_TIPO**) é **B-Utiliza Fornecedor**;  
- O produto do pedido possui o campo “Tipo” (**B1\_TIPO**) configurado como **BN-Beneficiamento**;  
- O TES possui movimento de estoque (**F4\_ESTOQUE** = **S-Sim**) e Controla Poder de Terceiros (**F4\_PODER3** = **R-Remessa**);  
- O parâmetro **MV\_EMPBN** deve estar configurado como verdadeiro (**.T.**)

**Observação**: Para que o sistema apresente as Ordens de Produção para seleção, é necessário ter gerado o **Empenho do material** (**Tabela SD4**), o empenho pode ser realizado através das rotinas de **Empenho Simples** (**MATA380**) ou **Empenho Múltiplo** (**MATA381**).

Em caso de dúvidas nos processos de inclusão da Ordem de Produção ou de Empenho dos materiais, solicite apoio ao Suporte dos módulos Protheus Estoque (SIGAEST) ou Protheus Plan.Contr.Produção (SIGAPCP).

Saiba mais: **[Ordem de Produção x Pedido de Vendas](https://tdn.totvs.com/x/YW52Hw)**
