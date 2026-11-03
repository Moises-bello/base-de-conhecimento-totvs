---
article_id: 4408832720791
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9a484b12e4a954db6762537379fcad674d180c7fc1e947e2498d0dfcaa485159
fetched_at: '2026-06-28T22:39:24.243052+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais os campos novos
  criados na CD2 para atender  Nota técnica 2020.005?
type: support-article
updated_at: '2021-09-17T16:57:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408832720791-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-os-campos-novos-criados-na-CD2-para-atender-Nota-t%C3%A9cnica-2020-005
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00**min** **Dúvida** Quais os campos novos criados na CD2 para atender Nota técnica 2020.005?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para atender a nota técnica 2020.005  deve rodar o UPDDISTR para criar os novos campo na CD2

### 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408832332439/mceclip0.png)

O campo CD2\_PSCFST foi criado com o intuito de indicar se o valor do PIS/Cofins-ST serão somados no total do Documento Fiscal. Esse campo servirá como base para o preenchimento das tags <indSomaPISST> e <indSomaCofinsST>, criados nesta Nota Técnica. 

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408510846871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-PIS-COFINS-ST-no-total-da-NF-?source=search>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408832381591/mceclip1.png)

* O campo CD2\_VFCPDI fará a geração da tag <vFCPDif>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) diferido.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408832434327/mceclip2.png)

o campo CD2\_VFCPEF fará a geração da tag <vFCPEfet>, onde é gravado o Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) efetivo, ou seja, o valor total de FCP - o valor diferido de FCP.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408539014935-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gravar-os-campos-CD2-VFCPDI-e-CD2-VFCPEF-?source=search>
