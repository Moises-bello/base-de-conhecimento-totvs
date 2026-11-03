---
article_id: 5021216166295
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: df80895b08b9556de4faab4c78ce2a27d681aaf1aeb41505eee7f9f912008a04
fetched_at: '2026-06-28T22:37:21.399121+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Campo Apropriado (CNW_FLGAPR)
  é alterado para Não após aprovação de Revisões no cronograma contabil do contrato.
type: support-article
updated_at: '2022-03-25T20:47:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5021216166295-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Campo-Apropriado-CNW-FLGAPR-%C3%A9-alterado-para-N%C3%A3o-ap%C3%B3s-aprova%C3%A7%C3%A3o-de-Revis%C3%B5es-no-cronograma-contabil-do-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Campo Apropriado (CNW\_FLGAPR) é alterado para Não no Cronograma Contabil do contrato após aprovação de Revisões em contratos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos - A partir da release 25  
  
**Solução**

Ao realizar a aprovação de uma revisão, o sistema realiza o estorno da contabilização do cronograma contábil inteiro, pois o mesmo pode ter sofrido alterações durante a revisão.

Além disso, durante esse processo, realiza a atualização do campo *flag*CNW\_FLGAPR = 2 (Não Apropriado) e a limpeza do campo CNW\_DTLANC.

Para que possa contabilizar o estorno no momento da aprovação da revisão cadastre o lançamento padrão abaixo:

* + **69J**: chamado uma vez por parcela do cronograma(CNW), o inverso do LP 693

No momento que clica na opção aprovação da revisão será chamado a contabilização do lançamento padrão 69J.

Após aprovação da revisão deve ser realizada uma nova apropriação do cronograma contábil referente ao lançamento 693.

**Observação:** A apropriação contabil lançamento 693 que foi realizada antes da revisão é mantida como histórico nas tabelas CT2 e CTK.

***Saiba Mais:***

* [MP - SIGAGCT- Como aplicar o conceito de Apropriação Contábil no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017519492-MP-SIGAGCT-Como-aplicar-o-conceito-de-Apropria%C3%A7%C3%A3o-Cont%C3%A1bil-no-Gest%C3%A3o-de-Contratos-?source=search)
* [GCT0011\_Apropriação Contábil](https://tdn.totvs.com/pages/releaseview.action?pageId=234610742)
* [GCT0084\_Nova\_Medição\_Versão\_BETA](https://tdn.totvs.com/pages/viewpage.action?pageId=274840426)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
