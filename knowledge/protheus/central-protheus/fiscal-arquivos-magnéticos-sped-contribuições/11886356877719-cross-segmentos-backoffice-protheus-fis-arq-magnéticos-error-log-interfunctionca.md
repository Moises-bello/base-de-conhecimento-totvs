---
article_id: 11886356877719
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: fb8a47a7b1d7e6cd29957333bbdc99d5773d797383d17284ce855224f3e24579
fetched_at: '2026-06-28T22:42:04.871136+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Error log
  InterFunctionCall: cannot find function SPEDPISCOF in AppMap on __EXECUTE(APLIB090.PRW)'
type: support-article
updated_at: '2023-01-24T12:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11886356877719-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-log-InterFunctionCall-cannot-find-function-SPEDPISCOF-in-AppMap-on-EXECUTE-APLIB090-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Ocorrência**Ao tentar gerar o **Sped Contribuições** pela rotina Sped Pis/Cofins é apresentado o erro **InterFunctionCall: cannot find function SPEDPISCOF in AppMap on \_\_EXECUTE(APLIB090.PRW)**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**O errorlog ocorre porque  a rotina em questão foi descontinuada em 2015 e desde então não existe mais pacotes para atualização.  
  
**Solução**Atualmente, para gerar o **Sped Contribuições,** primeiramente é preciso utilizar a rotina **Apuração EFD Contribuições - FISA001** para geração da **Apuração do PIS e COFINS** e em seguida a rotina **Geração do Arquivo EFD Contribuições - FISA008** para geração do arquivo txt.

![](https://totvssuporte.zendesk.com/attachments/token/mQA7gzF6VVe5jsEqfKOAfsdVZ/?name=image.png)  
Abaixo, segue link com os manuais de geração tanto da apuração quanto do arquivo.

***Link:* Boletim Técnico Apuração EFD Contribuições:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>  
  
***Link:*Boletim Técnico Geração Arquivo txt EFD Contribuições:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=715144991>
