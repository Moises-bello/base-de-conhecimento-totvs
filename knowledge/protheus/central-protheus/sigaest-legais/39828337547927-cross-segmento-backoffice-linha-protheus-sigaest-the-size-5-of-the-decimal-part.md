---
article_id: 39828337547927
category: SIGAEST - LEGAIS
content_hash: 3af58afeb60c888b73757b8eb15e84f2d219837597e637867d8a31e885b627b3
fetched_at: '2026-06-28T22:38:51.911477+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - The size (5) of the
  decimal part of the number (254.25789) informed is greater than the size (3) supported
  by the field (QTD)
type: support-article
updated_at: '2026-04-17T17:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39828337547927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-The-size-5-of-the-decimal-part-of-the-number-254-25789-informed-is-greater-than-the-size-3-supported-by-the-field-QTD
---

O problema ocorre ao gerar arquivo SPEDFISCAL com campos numéricos de 4 decimais, causando erro por excesso de casas decimais no campo QTD.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39828337534359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao gerar o arquivo de extensão "txt" do SPEDFISCAL utilizando campos numéricos com 4 decimais, a rotina apresenta a seguinte inconsistência: "The size (5) of the decimal part of the number (254.25789) informed is greater than the size (3) supported by the field (QTD)".  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Efetuada tratamento na geração do bloco H, limitando os decimais de acordo com o layout padrão.

**12.1.2310**:<https://r.totvs.io/p/1174900>

**12.1.2410**:<https://r.totvs.io/p/1174899>

**Issue TDN:** DMANMAT01-43142  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
