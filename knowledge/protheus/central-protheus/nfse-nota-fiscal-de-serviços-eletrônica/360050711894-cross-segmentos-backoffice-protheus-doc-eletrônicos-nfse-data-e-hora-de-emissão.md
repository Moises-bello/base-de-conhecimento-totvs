---
article_id: 360050711894
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f2702806f197c0082e6a1be5b6aeed93f847ac3399b2b642386ae12fb458afa4
fetched_at: '2026-06-28T22:39:56.434817+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Data e Hora
  de Emissão (FISA022)
type: support-article
updated_at: '2025-07-08T20:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050711894-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Data-e-Hora-de-Emiss%C3%A3o-FISA022
---

**Dúvida**Por que a data e/ou hora de emissão estão sendo apresentadas zeradas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Os campos de Data e Hora de Emissão dentro da rotina FISA022 são um espelho do que a própria prefeitura retorna após uma transmissão.  
Os campos **só são populados após monitorar** a(s) notas(s) e **se a prefeitura retornar esses dados**.  
Vale lembrar que nem sempre a prefeitura irá devolver esses dados da emissão, nesse caso impossibilitando o TSS/ERP de popular os campos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079270013/mceclip0.png)  
  
**Solução**Caso tenha monitorado a nota e os campos não foram preenchidos, existe uma maneira de que poderá verificar se a prefeitura de fato não retornou essas informações: através do botão **Outras Ações -> Exportar**.   
Segue abaixo um exemplo desse conteúdo da nota que foi preenchida (print acima):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078111994/mceclip0.png)  
  
*Obs.: Vale lembrar que uma mesma prefeitura poderá ter dois tipos de retorno, ou seja, hora devolverá, hora não os dados com data e hora de emissão.*
