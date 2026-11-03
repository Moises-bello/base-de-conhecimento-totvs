---
article_id: 360042275094
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 8cf8baf7b307686ad498ba2a61167c37274ae7bb9e227eb15deaa93c1d5820e4
fetched_at: '2026-06-28T22:38:45.120538+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Ao excluir um documento
  de saída o sistema gera error.log type mismatch on compare on MACANDELF2
type: support-article
updated_at: '2021-08-16T18:47:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042275094-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-excluir-um-documento-de-sa%C3%ADda-o-sistema-gera-error-log-type-mismatch-on-compare-on-MACANDELF2
---

**Dúvida**Ao tentar excluir um documento de saída o sistema gera error.log **type mismatch on compare on MACANDELF2(MATA521.PRX)**.  
  
**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – A partir da versão 12.

**Causa**

O erro **type mismatch on compare on MACANDELF2(MATA521.PRX)** ocorre quando o parâmetro **MV\_SPEDEXC**esta configurado com o tipo Caractere e não com o tipo Numérico.

No fonte **MATA521** (**exclusão do Documento de Saída**),o sistema verifica a quantidade de horas da nota (**nHoras**) e verifica se é maior que o conteúdo do parâmetro (**nSpedExc**).

Outra situação de ocorrência deste erro está relacionado **a exclusão a nota de serviço**, e ao excluir a nota o sistema irá verificar o parâmetro **MV\_TIPOPRZ** (Tipo de prazo para exclusão das notas fiscais de serviço) , mas a tipagem do parâmetro está configurada como carácter ao invés de numérico.

No fonte **MATA521** , o sistema verifica o conteúdo que a variável **nTpPrz** que recebe direto o conteúdo do parâmetro MV\_TIPOPRZ para saber as regras de exclusão da nota de serviço. 

**Solução**

Para a solução deste erro:

* Quando **MV\_SPEDEXC** está com a tipagem incorreta, é  necessário ajustar de Carácter para o tipo Numérico, abaixo apresentamos um exemplo para comparação:

![MV_SPEDEXC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103515853/MV_SPEDEXC.png)

* Quando **MV\_TIPOPRZ** está com a tipagem incorreta, é  necessário ajustar de Carácter para o tipo Numérico, abaixo apresentamos um exemplo para comparação:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406437576855/mceclip0.png)

**Outros assuntos relacionados a exclusão da nota:**

[**MP - FAT - Excluir Nota de Serviço após prazo do município**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000617328-MP-FAT-Excluir-Nota-de-Servi%C3%A7o-ap%C3%B3s-prazo-do-munic%C3%ADpio?source=search)

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Exclusão de Nota Fiscal por seleção em lote/sequencia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404560225559-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclus%C3%A3o-de-Nota-Fiscal-por-sele%C3%A7%C3%A3o-em-lote-sequencia)**

**[MP-FAT-Falta de checkbox no browse da exclusão da nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044746454-MP-FAT-Falta-de-checkbox-no-browse-da-exclus%C3%A3o-da-nota)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - MTA520DEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644562583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-MTA520DEL)**

**[MP-FAT-InterFunctionCall: cannot find function SUBTHORAS in AppMap on MACANDELF2(MATA521.PRX)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035004053-MP-FAT-InterFunctionCall-cannot-find-function-SUBTHORAS-in-AppMap-on-MACANDELF2-MATA521-PRX-)**

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Validação de exclusão do Documento de Saída com uso do JOB FATJOBNFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004391207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Valida%C3%A7%C3%A3o-de-exclus%C3%A3o-do-Documento-de-Sa%C3%ADda-com-uso-do-JOB-FATJOBNFE)**
