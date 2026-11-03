---
article_id: 360026972112
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c56b4e448e9878fbdbacd859c852ce318ffb44a44d1cc19b325df278b511013e
fetched_at: '2026-06-28T22:39:57.599883+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Número de
  DPS/RPS x Número de NFSe
type: support-article
updated_at: '2026-02-27T16:39:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026972112-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-N%C3%BAmero-de-DPS-RPS-x-N%C3%BAmero-de-NFSe
---

**Dúvida**  
Controle de Número de RPS x Número de NFSe  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**  
O Documento de Saída é o DPS (Declaração de Prestação de Serviço) ou RPS (Recibo Provisório de serviço), portanto o F2\_DOC é o número do RPS.

Todas as prefeituras ou governo que trabalham com o webservice, fornecem o layout do Recibo Provisório, nesse layout existe o número do DPS ou RPS e o número da NFSe que retorna após processamento e conversão do DPS/RPS em NFSE.  
  
Se trata de documentos distintos (tratado dessa forma pela prefeitura ou governo), um provisório e o outro oficial, inclusive no Protheus você consegue extrair o número dos dois documentos, sendo 'F2\_DOC' número do DPS/RPS e 'F2\_NFELETR' número da NFSe.  
  
Existem empresas que querem manter DPS/RPS e NFSe com a mesma numeração, mas esse controle pode falhar. Por esse motivo a maioria dos prestadores de serviços não fazem esse controle, justamente pelo fato de transmitir um lote e a prefeitura/governo recepcionar e processar na ordem que nem sempre é a mesma da transmissão, independente se há RPSs no lote com erros, ela não interrompe o processamento, o que está correto.

Caso possua alguma legislação que obrigue o uso do número de RPS igual ao Número da NFSe, deverá ser informado com o suporte da TOTVS, mencionando o link da legislação com o trecho para que possa ser analisado.  
  
Veja também: [Campos de retorno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026100812-MP-NFSE-Campos-de-Retorno-da-NFSe-)
