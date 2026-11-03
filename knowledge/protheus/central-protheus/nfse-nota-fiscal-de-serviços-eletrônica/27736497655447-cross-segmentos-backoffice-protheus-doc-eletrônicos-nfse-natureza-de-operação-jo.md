---
article_id: 27736497655447
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 64a6d99bea0e57851162ae3f7df2e985ea311287b82a7e842184bc8cad48ce4d
fetched_at: '2026-06-28T22:39:57.570829+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Natureza
  de Operação Joinville-SC
type: support-article
updated_at: '2025-05-21T19:26:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27736497655447-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Natureza-de-Opera%C3%A7%C3%A3o-Joinville-SC
---

**Dúvida**Como gerar a Natureza de Operação para Joinville/SC?  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32273474046743)

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução**Cada Natureza de Operação exige uma combinação de campos dentro do Protheus, sendo elas:

**Natureza 119** - ISS retido pelo tomador (Poder Publico)  
A1\_TPESSOA=EP, A1\_EST/A1\_CODMUN=Joinville e A1\_RECISS/C5\_RECISS=SIM.  
  
**Natureza 101** - ISS devido para Joinville  
F4\_ISSST=1, C5\_RECISS OU A1\_RECISS=2 e MV\_OPTSIMP=2  
  
**Natureza 102** - ISS devido para outro Município  
F4\_ISSST=2  
  
**Natureza 104** - Imune  
F4\_ISSST=3 ou F4\_ISSST=4 ou F4\_ISSST=5 ou F4\_ISSST=7 ou F4\_ISSST=6 ou F4\_ISSST=A  
  
**Natureza 105** - ISS retido pelo tomador  
F4\_ISSST=1, C5\_RECISS OU A1\_RECISS=1 e MV\_OPTSIMP=2  
  
**Natureza 106** - ISS Fixo Prestado em Joinville  
F4\_CSTISS=05  
  
**Natureza 107** - ISS devido para Joinville (Simples Nacional)  
MV\_OPTSIMP=1 e Município de incidência (MV\_NFSEINC) igual a Joinville.  
  
**Natureza 108** - ISS devido para outro Município (Simples Nacional)  
MV\_OPTSIMP=1 e Município de incidência (MV\_NFSEINC) diferente de Joinville.  
  
**Natureza 110** - ISS retido pelo tomador (Simples Nacional)  
MV\_OPTSIMP=1 e C5\_RECISS OU A1\_RECISS=1  
  
**Natureza 112** - ISS devido em Joinville, prestado fora  
F4\_ISSST=1, C5\_RECISS OU A1\_RECISS=2, MV\_OPTSIMP=2, MV\_NFSEINC=4209102 e C5\_MUNPRES + C5\_ESTPRES= Município onde o serviço foi prestado.  
  
**Natureza 113** - Não incidência de ISS (Tomador Internacional)A1\_PAIS=Diferente de Brasil e MV\_OPTSIMP=2. **Natureza 116** - ISS Devido para Joinville (Tomador Internacional)  
F4\_ISSST=1, [País de Prestação=Brasil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101732), MV\_OPTSIMP=2 e A1\_PAIS=Diferente de Brasil.  
  
**Natureza 121** - ISS devido para outro Município, retido pelo tomador  
F4\_ISSST=2, C5\_RECISS ou A1\_RECISS=1 e C5\_MUNPRES+C5\_ESTPRES=Município diferente de Joinville.  
  
Veja o uso do correto do parâmetro MV\_NFSEINC para configurar o Município de Incidência caso seja necessário: [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026239231-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Municipio-de-Incidencia).
