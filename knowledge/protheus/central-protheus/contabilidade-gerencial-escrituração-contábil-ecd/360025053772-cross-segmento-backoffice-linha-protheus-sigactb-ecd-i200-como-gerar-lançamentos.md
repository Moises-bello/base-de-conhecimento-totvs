---
article_id: 360025053772
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: d442da53bcdab203400a563e891e4b9e7dba32f3090f58ba101b6f116afe8b94
fetched_at: '2026-06-28T22:40:44.320523+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD I200  COMO GERAR
  LANÇAMENTOS EXTEMPORÂNEOS
type: support-article
updated_at: '2023-09-13T14:39:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025053772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I200-COMO-GERAR-LAN%C3%87AMENTOS-EXTEMPOR%C3%82NEOS
---

**Dúvida**Como gerar lançamento X (extemporâneo) para ECD?  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80.  
  
   
**Solução**

Na rotina de lançamento  (exemplo: CTBA102) após realizar o lançamento de "retificação, estorno, complementação ou transferência" de períodos anteriores.

Posicione no registro + "outras ações" + LCTO EXTEMP

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023840212)**

Na tela seguinte o campo DATA LANÇAMENTO EXTEMPORÂNEO deverá ser preenchida.

Esse registro é armazenado na tabela CSQ, ao ser gerado para ECD e exportado para o TXT, ele ficará com o identificador X no registro I200.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023873351)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023874111)**

**Importante!**

* Compartilhamento CSQ (SX2)

Tabela CSQ armazena os dados do lançamento para gerar o lançamento "X" na ECD. Esta tabela deverá possuir o mesmo compartilhamento da tabela CT2 .

* Histórico do lançamento tipo "X"

Caso o lançamento seja do tipo “X” – lançamento extemporâneo - em qualquer das formas de retificação, o histórico do lançamento extemporâneo deve especificar o motivo da correção, a data e o número do lançamento de origem (item 32 do ITG 2000 (R1)).

* Data do lançamento extemporâneo  (I200 DT\_LCTO\_EXT).

Dever ser anterior à data inicio da escrituração, isso porque lançamentos extemporâneos são referentes a períodos anteriores, Caso não seja possível precisar a data a que se refiram os fatos do lançamento extemporâneo, informar a data de encerramento do exercício em que ocorreram esses fatos.

**Data do lançamento extemporâneo:**

**[MP-SIGACTB ECD A DATA DE LANÇAMENTO EXTEMPORANEO (I200 DT\_LCTO\_EXT) DEVE SER ANTERIOR À DATA DE INICIO DA ESCRITURAÇÃO.](https://totvssuporte.zendesk.com/knowledge/articles/360025392431/pt-br?brand_id=1509248)**

**Saiba mais:**

**<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>**

[MP-SIGACTB ECD RELATÓRIO LANÇAMENTOS EXTEMPORÂNEOS, LANÇAMENTOS X](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026411491-MP-SIGACTB-ECD-RELAT%C3%93RIO-LAN%C3%87AMENTOS-EXTEMPOR%C3%82NEOS-LAN%C3%87AMENTOS-X?source=search).

[MP-SIGACTB :ECD I250 ADVERTENCIA VERIFIQUE SE A CONTA É EXTEMPORANEA E NAO AFETA O RESULTADO DO PERIODO ATUAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025130772-MP-SIGACTB-ECD-I250-ADVERTENCIA-VERIFIQUE-SE-A-CONTA-%C3%89-EXTEMPORANEA-E-NAO-AFETA-O-RESULTADO-DO-PERIODO-ATUAL?source=search)
