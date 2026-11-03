---
article_id: 4562118192535
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6b95a8ad07ab95bbf763fe4ba8fd6a1540a6798069a068fd7757cda694781191
fetched_at: '2026-06-28T22:37:21.362753+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao Realizar Revisão
  de Aditivo de prazo não é atualizado a Data final da Planilha CNA_DTFIM
type: support-article
updated_at: '2023-08-01T12:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4562118192535-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-Realizar-Revis%C3%A3o-de-Aditivo-de-prazo-n%C3%A3o-%C3%A9-atualizado-a-Data-final-da-Planilha-CNA-DTFIM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao Realizar Revisão de Aditivo de prazo não é atualizado a Data final da Planilha CNA\_DTFIM  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos – A partir da versão 12.1.17  
  
**Solução**Pelo padrão do Módulo de Gestão de Contrato, o sistema não atualiza a Data Final (***CNA\_DTFIM***) da Planilha em Revisões de Aditivo de Prazo atualizando somente no cabeçalho do contrato(CN9\_DTFIM), pois é possível a existência de planilhas com duração inferior a duração do contrato. Por conta disso, não é atualizado a Data final (***CNA\_DTFIM***), pois as Datas da Planilha são independentes desde que não ultrapasse a data do campo Data Final (**CN9\_DTFIM**).  
Já na situação em que se informe uma data no cabeçalho do contrato no **CN9\_DTFIM** que seja inferior a data final da planilha **CNA\_DTFIM**, nesse cenário o sistema atualiza o campo, pois não é possível uma planilha com duração superior à do contrato.

***Saiba Mais:***

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
