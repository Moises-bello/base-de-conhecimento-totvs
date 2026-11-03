---
article_id: 10017801361687
category: NFe - Nota Fiscal Eletrônica
content_hash: 5d7eede9e00d96adb9a5aec5deb86b151ca5111df90dd36a89134bdd19b3564f
fetched_at: '2026-06-28T22:40:05.610001+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Cancelamento extemporâneo
  fora do prazo
type: support-article
updated_at: '2025-06-17T12:31:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10017801361687-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Cancelamento-extempor%C3%A2neo-fora-do-prazo
---

**Dúvida**Como realizar o Cancelamento extemporâneo fora do prazo ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em ***editar***  ***MV\_CANCEXT e o  MV\_SPEDEXC***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12319343539479)***

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12319346304919)***

***Exemplo:***

Caso um documento tenha sido emitido no dia 01/12 e você queira inutilizar/cancelar esse documento no dia 30/12, o parâmetro ***MV\_CANCEXT (parâmetro configurado em dias)*** deve estar preenchido com o valor 31 pelo menos e o ***MV\_SPEDEXC (parâmetro configurado em horas) com um valor que ENGLOBE a data de emissão do documento.** C*om 744 horas, que será maior que os 30 dias e as horas que a nota já foi emitida.   Além disso, refaça a configuração abaixo: Faturamento > NFE SEFAZ > Outras Ações > Parâmetros > Eventos ***(FAVOR REFAZER ATÉ CLICAR NO BOTÃO "OK" PARA RECONFIGURAR O TSS)***

2. Acessar a rotina de exclusão do documento de saída, exclua o documento e em seguida na rotina do ***NFESEFAZ Em Outras Ações > Transmissão transmita a numeração da nota   Outras Ações  >  Monitor  >  Faixa.***

* ***Saiba mais:***

No momento da transmissão apresentará a mensagem ***0 notas transmitidas,*** pois é um evento que está sendo transmitindo.

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Validação de exclusão do Documento de Saída com uso do JOB FATJOBNFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004391207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Valida%C3%A7%C3%A3o-de-exclus%C3%A3o-do-Documento-de-Sa%C3%ADda-com-uso-do-JOB-FATJOBNFE?source=search)  
   
**Para mais detalhes do processo Fatjobnfe, acesse:**  
[FAT0191\_FATJOBNFE\_para\_Exclusão\_documento\_de\_Saída\_MATA521](https://tdn.totvs.com/pages/releaseview.action?pageId=272154294#FATJOB-FATJOB)
