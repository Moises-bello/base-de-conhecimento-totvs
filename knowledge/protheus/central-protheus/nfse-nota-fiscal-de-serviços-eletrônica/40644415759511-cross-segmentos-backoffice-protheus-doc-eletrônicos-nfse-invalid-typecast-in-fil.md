---
article_id: 40644415759511
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f80f3fc123f8bfc68e1320e7749f661366a42e6cdbb51a7f74554012e0b938ce
fetched_at: '2026-06-28T22:39:57.512769+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - invalid
  typecast in file E:\build-dir\TP11-OF2431X-W6\advpl\instrvar.inl at line 1068  on
  GETTPRETPCC(NFSEXMLENV.PRW) XX/XX/2026 11:02:31 line : XXXX'
type: support-article
updated_at: '2026-05-21T17:47:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40644415759511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-invalid-typecast-in-file-E-build-dir-TP11-OF2431X-W6-advpl-instrvar-inl-at-line-1068-on-GETTPRETPCC-NFSEXMLENV-PRW-XX-XX-2026-11-02-31-line-XXXX
---

**Ocorrência**  
Ao realizar a transmissão de uma nota, ocorre o error.log abaixo:  
  
**invalid typecast in file E:\build-dir\TP11-OF2431X-W6\advpl\instrvar.inl at line 1068**  
**on GETTPRETPCC(NFSEXMLENV.PRW) 07/05/2026 11:02:31 line : 6045**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Esse error.log ocorre por conta do tipo do parâmetro MV\_NT007 estar configurado incorretamente no ambiente, exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40644972322327)  
  
**Solução**  
Para correção **deverá ser ajustado o tipo do parâmetro para LÓGICO** ao invés de CARACTERE e/ou outro:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40644425955607)  
  
**Obs**.: O parâmetro deverá ser configurado como True caso a prefeitura tenha aderido à NT 007, caso contrário, devera estar como False.
