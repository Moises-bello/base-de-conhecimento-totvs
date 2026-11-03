---
article_id: 360021297791
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 19fe42dd6b1cd19dd5e403bc12dc02d95b87f28fd371d2b6541c3b795a4c095b
fetched_at: '2026-06-28T22:42:11.811352+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - NOVAGISS - Preenchido
  do campo TP_DOC_NF
type: support-article
updated_at: '2022-08-18T14:06:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021297791-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-NOVAGISS-Preenchido-do-campo-TP-DOC-NF
---

**Dúvida**

Como é preenchido o campo **TP\_DOC\_NF** no arquivo da **NOVAGISS** **/ GISSONLINE** ?

**Ambiente**Microsiga Protheus - A partir da versão 11.80  
  
**Solução**É realizada a seguinte condição para o preenchimento das informações:

**Entradas:**

Se o documento fiscal estiver com o campo F3\_DTCANC preenchido   
TP\_DOC\_NF = "2"

Se o livro fiscal de ISS na TES estiver configurado como "Isento" ou "Outros" (Será gravado o campo F3\_ISENICM ou F3\_OUTRICM mesmo se tratando de ISS)   
TP\_DOC\_NF = "4"

Se o campo F3\_RECISS igual a "2" ou "N" e os campos F3\_ISENICM e F3\_OUTRICM zerados   
TP\_DOC\_NF = "5"

Se não atender nenhuma das opções acima   
TP\_DOC\_NF = "1"

**Saídas****:**

Se o documento fiscal estiver com o campo F3\_DTCANC preenchido   
TP\_DOC\_NF = "2"

Se o livro fiscal de ISS na TES estiver configurado como "Isento" ou "Outros" (Será gravado o campo F3\_ISENICM ou F3\_OUTRICM mesmo se tratando de ISS)   
TP\_DOC\_NF = "4"

Se o campo F3\_RECISS igual a "1" ou "S" e os campos F3\_ISENICM e F3\_OUTRICM zerados   
TP\_DOC\_NF = "5"

Se não atender nenhuma das opções acima   
TP\_DOC\_NF = "1"
