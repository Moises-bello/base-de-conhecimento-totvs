---
article_id: 360059477413
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4f40f3b8a3b3177b7478ec3a04b8a25b74692363c74cf83053cda4de79bb0aca
fetched_at: '2026-06-28T22:42:04.890163+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Ajuste de Credito
  ou Debito na apuração da EFD Contribuições Ajuste PIS/COFINS - Tabelas CLA - Ajuste
  PIS/COFINS e CL4 - Detalhamento do Ajuste de Crédito
type: support-article
updated_at: '2022-08-31T12:39:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059477413-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Ajuste-de-Credito-ou-Debito-na-apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es-Ajuste-PIS-COFINS-Tabelas-CLA-Ajuste-PIS-COFINS-e-CL4-Detalhamento-do-Ajuste-de-Cr%C3%A9dito
---

**Dúvida**  
Ao gerar o arquivo da EFD Contribuições, foi identificado um ajuste de 0,01 centavo nas tabelas CLA (Ajuste PIS/COFINS) e CL4 (Detalhamento do Ajuste)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Os ajustes gravados nas tabelas CLA (Ajuste PIS/COFINS) e CL4 (Detalhamento do Ajuste) são gravados de forma automática na rotina Ajuste Pis/Cofins com sua devida descrição.  
  
Exemplo: Ajuste- Redução Crédito - Pis.  
  
Para que o ajuste tenha efeito é necessário que exista nota de saída para composição do debito de PIS e COFINS no qual serão gravados os ajustes nas tabelas CLA e CL4.  
  
Caso seja apresentando algum ajuste e não tenha documento fiscal vinculado, será necessário verificar se o ajuste é oriundo de algum título.
