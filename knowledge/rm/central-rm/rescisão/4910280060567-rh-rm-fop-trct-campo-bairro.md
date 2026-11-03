---
article_id: 4910280060567
category: Rescisão
content_hash: b2cd5bf15f6c6e3862ccc4f053a999c91b6c59acfec4c4436f6474ebc5837d20
fetched_at: '2026-06-28T22:46:54.400175+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: campo bairro'
type: support-article
updated_at: '2025-01-21T18:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4910280060567-RH-RM-FOP-TRCT-campo-bairro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**No módulo Folha de Pagamento, ao gerar o Termo de Rescisão de Contrato de Trabalho, o campo 04- Bairro não está levando a informação, conforme cadastro do funcionário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4910261539863/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois houve uma inconsistência no relatório de Termo de Rescisão de Contrato de Trabalho.  
  
**Solução**Essa ocorrência que está sendo apresentada no **relatório TRCT | campo 4- Bairro**, foi corrigida com o ajuste do relatório. Segue abaixo passo a passo para ajuste do relatório.  
  
1. Para realização do ajuste no relatório, é necessário primeiramente realizar a exclusão do relatório existente na base. Para isso, segue abaixo documentação orientando o processo de exclusão de relatório no RM Reports.  
  
[RH - RM - FOP - RM Reports: Exclusão de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688075799-RH-RM-FOP-RM-Reports-Exclus%C3%A3o-de-Relat%C3%B3rios)  
  
2. Feito isso, será necessário importar o relatório que consta em anexo neste artigo. Para isso, segue abaixo documentação orientando o processo de importação de relatório no RM Reports.  
  
[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios)  
  
3. Logo, gere o TRCT novamente.
