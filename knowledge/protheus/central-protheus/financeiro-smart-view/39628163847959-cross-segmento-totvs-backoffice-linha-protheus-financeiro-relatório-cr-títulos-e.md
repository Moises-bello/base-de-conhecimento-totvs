---
article_id: 39628163847959
category: Financeiro - Smart View
content_hash: e64daa26fd85e23aca1329552b871e44ca42b20fdc2819237c5affc1aa29fd03
fetched_at: '2026-06-28T22:37:44.872346+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Relatório
  CR títulos em aberto e baixados
type: support-article
updated_at: '2026-04-09T14:44:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39628163847959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-Relat%C3%B3rio-CR-t%C3%ADtulos-em-aberto-e-baixados
---

**Dúvida**  
Qual relatório possibilita a visualização consolidada de dados de emissão, vencimento, títulos baixados e títulos em aberto em um único documento?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2210  
  
**Solução:**

A consulta pode ser realizada por meio do **Smart View FINSV040**. Este recurso permite a extração analítica de dados que contemplam títulos em aberto (conforme o intervalo de datas de vencimento parametrizado), ou baixados parcialmente, além de todas as baixas realizadas no período informado, respeitando os parâmetros definidos na rotina.

**Passos**

1. No módulo **Financeiro (SIGAFIN)**, acesse **Consultas** > **Smart View**;
2. Localize e selecione o objeto de negócio **FINSV040**;
3. Configure os parâmetros de extração, definindo o intervalo de **Data de Vencimento** e o período para as **Baixas** desejadas;
4. Execute a consulta para visualizar as informações integradas de títulos e pedidos;
5. Caso necessário, utilize as ferramentas de exportação do Smart View para gerar o arquivo no formato desejado (Excel, PDF, etc).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39628163822615)
