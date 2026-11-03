---
article_id: 4403486130455
category: Escrita Fiscal - Impostos - ICMS
content_hash: 6fa144d1aafc5937747328214105e758b6157b2e8afa79cd07158e17651aba08
fetched_at: '2026-06-28T22:39:26.041307+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Configuração Para Deduzir ICMS/PIS/COFINS Desonerado da base do
  CPRB
type: support-article
updated_at: '2021-06-30T18:15:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403486130455-MP-FIS-Configura%C3%A7%C3%A3o-Para-Deduzir-ICMS-PIS-COFINS-Desonerado-da-base-do-CPRB
---

**Dúvida**  
Como configurar o sistema para deduzir o ICMS/PIS/COFINS desonerado da ZFM da base do CPRB?  
  
**Ambiente**  
Cross Segmento - Microsiga Protheus – Livros Fiscais – A partir da versão 12.  
  
**Solução**Foi implementada uma nova configuração para o parâmetro **MV\_DEDBCPR**, onde ao informar **D**, será subtraído da base da CPRB o valor do ICMS/PIS/COFINS desonerado da Zona Franca de MANAUS. 

1- Segue abaixo primeiro exemplo:

**MV\_RPCBIZF = .F. -** (Retira Pis/Cofins ZFM da base do ICMS)

**MV\_DEDBCPR= D -** (Ret.ICM/PIS/COF ZFM.)

Segue abaixo exemplo do calculo:

![](https://tdn.engpro.totvs.com.br/download/attachments/602807569/image2021-3-15_17-37-31.png?version=1&modificationDate=1615840651400&api=v2)

2 - Segue abaixo segundo exemplo;

**MV\_RPCBIZF = .T. -** (Retira Pis/Cofins ZFM da base do ICMS)

**MV\_DEDBCPR= D -** (Ret.ICM/PIS/COF ZFM.)

![](https://tdn.engpro.totvs.com.br/download/attachments/602807569/image2021-3-15_17-37-52.png?version=1&modificationDate=1615840671920&api=v2)

Segue abaixo a documentação completa:

<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=602807569>
