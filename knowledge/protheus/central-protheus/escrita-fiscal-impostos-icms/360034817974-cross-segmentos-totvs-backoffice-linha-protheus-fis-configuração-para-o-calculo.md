---
article_id: 360034817974
category: Escrita Fiscal - Impostos - ICMS
content_hash: 878beb54870debcfcc037c5a29eb70bea84bbaa4a0a7edcfdc2ba480f6017ab2
fetched_at: '2026-06-28T22:39:25.600659+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração para
  o calculo do ICMS Desonerado com redução de base  de cálculo conforme Resolução
  13/2019 RJ
type: support-article
updated_at: '2021-07-28T16:58:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034817974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-o-calculo-do-ICMS-Desonerado-com-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-conforme-Resolu%C3%A7%C3%A3o-13-2019-RJ
---

**Dúvida**Qual Configuração para o calculo do ICMS Desonerado com redução de base de cálculo conforme Resolução 13/2019 RJ?

Fórmula:  
ICMS Desonerado = Preço na Nota Fiscal \* (1 - (Alíquota \* (1 - Percentual de  
redução da BC))) / (1 - Alíquota) - Preço na Nota Fiscal   
   
 **Ambiente**

Mircosiga Protheus– Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**

Configuração do TES

F4\_ICM=Sim

F4\_BASEICM=Percentual da base para redução do cálculo do ICMS.

F4\_LFICM=Isenta ou Outros

F4\_SITTRIB=20 ou 70

Na aba outros

F4\_MOTICMS=9 Outros

Configuração do código de Reflexo (FISA072)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045284994/mceclip1.png)

Informações adicionais:

<http://www.fazenda.rj.gov.br/sefaz/content/conn/UCMServer/uuid/dDocName%3AWCC35713833000>

<https://tdn.totvs.com/pages/releaseview.action?pageId=469449117#C%C3%A1lculos-Diferimento>

<https://tdn.totvs.com/pages/viewpage.action?pageId=211062456>
