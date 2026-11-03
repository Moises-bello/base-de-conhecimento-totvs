---
article_id: 35189952694295
category: Reforma Tributária
content_hash: 51bddfaa5b466e8ad0c2aa9d0d9fe6d3670bdd2ab8a943f50c29fc53361f88de
fetched_at: '2026-06-28T22:39:53.721493+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  - Rejeição 1021 Grupo IBS/CBS informado indevidamente [nItem: 999]'
type: support-article
updated_at: '2026-06-18T14:46:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35189952694295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Rejei%C3%A7%C3%A3o-1021-Grupo-IBS-CBS-informado-indevidamente-nItem-999
---

**Dúvida**  
Como corrigir a **Rejeição 1021 Grupo IBS/CBS informado indevidamente [nItem: 999]?**  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões      
  
**Solução**  
Caso apresente as rejeição Rejeição 1021 Grupo IBS/CBS informado indevidamente [nItem: 999] ao emitir nota com cClassTrib que não deva gerar grupo de IBS e CBS.

Para correção da rejeição é necessario aplicar os pacotes da documentação abaixo no Protheus:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

Os CST's 010, 011, 221, 400, 410, 620, 800 e 820 não vão gerar as tags de IBS e CBS no xml da nota.  
   
Segue retorno da nossa Consultoria de Segmentos:  
   
[https://tdn.totvs.com.br/pages/releaseview.action?pageId=984985677#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosPSCONSEG18564PerguntaseRespostasReformaTribut%C3%A1riadoConsumo-2.22ParaosCST'sondeaSefazdefiniucomind\_gIBSCBS=0,devegerarogrupoIBS/CBSnoxml](https://tdn.totvs.com.br/pages/releaseview.action?pageId=984985677#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosPSCONSEG18564PerguntaseRespostasReformaTribut%C3%A1riadoConsumo-2.22ParaosCST%27sondeaSefazdefiniucomind_gIBSCBS=0,devegerarogrupoIBS/CBSnoxml)  
   
Tópico: 2.22 Para os CST's onde a Sefaz definiu com ind\_gIBSCBS = 0,

![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVdCTvZrrKIWyjZqnUubnHQQofKS8T3T9NIojb2R%2Fvjb76CaxLewdisN9eaQaXsuYQy0DA%2Fo4I5313FYk%2B4wx%2B03ELaUQYewtlVOjdPf10LXgrNs3OY8n7b687U46W9cAXQVvfWTxLF8kX3rqIisyOvC3jpzVh9L%2FzDj6A7kN3es8b3JbqpwTfRS5320PFuuCzGligkN9PJ96KNrpuT%2Fr1z2%2F%2FHTldj8I0AkqtPWnmWREbhUwNieVhuIIGioIPw1brUOIn7IyG%2F%2FEYQ5aUPYzXwNWRGsdRpfZA2jAO1F%2FS%2BsuZozoY7a1HnCgnp1VxzsPlZ042eir9I67Oa%2BCsJv65jq%2Byn6HWQNRazIQ1MTv2exu0QTiHF1US4oQGAxcX%2BO1Cl9%2FW5i11fnP0hLCiLT9FDz9onNvgau3WSlVlyKmg2cQPoOk5xRlBRpyLx3oBR1lPcEgSx4AQvOSIMyW3sjP%2BLym5iI1ZtjViutpbnpBSAC9mtTl1jAsf9my6do1aglJ%2Bso8RgHyk7RcD0DgxFtjnXrGZGTv8J2DW4KmqMb%2FIImWsLfwezU1fPkR7TPN5n5obM%2Fcx2L355OdeYzg%3D%3D&allow_caching=true&sz=w1580-h744-rw)
