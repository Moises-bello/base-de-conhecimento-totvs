---
article_id: 11153817832343
category: Materiais - Compras (SIGACOM)
content_hash: d677b9f37be9317d2bb6c9dc089f0b25037b21e9ac20b677c237f81e35d3e4da
fetched_at: '2026-06-28T22:41:16.015318+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a gravação
  do campo F1_HORA.
type: support-article
updated_at: '2023-01-12T11:40:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11153817832343-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-grava%C3%A7%C3%A3o-do-campo-F1-HORA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como realizar a gravação dos campo F1\_HORA.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras  
  
**Solução**Para gravação dos campos de hora do Protheus F1\_HORA, se faz necessária a configuração dos parâmetros abaixo:

**MV\_HORANFE**: Parâmetro responsável por gravar o campo F1\_HORA no momento da inclusão do documento de entrada.

**MV\_HORARMT** : Parâmetro responsável pela gravação dos campos de acordo com a necessidade:

- Horário do SmartClient

- Horário do servidor

- Fuso horário da filial corrente

**Observação**: Caso seja inclusa uma Nota, pela rotina de Prenota (MATA140) o campo será gravado no momento da classificação do Documento.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
