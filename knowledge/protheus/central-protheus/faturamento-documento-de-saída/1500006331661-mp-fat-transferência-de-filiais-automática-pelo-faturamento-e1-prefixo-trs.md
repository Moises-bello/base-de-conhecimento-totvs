---
article_id: 1500006331661
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: b66e4c5cfa6deb921a1fe074d47de35979711ce59dfd037adf08f45a2c6f9ad8
fetched_at: '2026-06-28T22:38:45.458986+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Transferência de Filiais automática pelo Faturamento - E1_PREFIXO
  TRS
type: support-article
updated_at: '2021-04-28T15:12:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006331661-MP-FAT-Transfer%C3%AAncia-de-Filiais-autom%C3%A1tica-pelo-Faturamento-E1-PREFIXO-TRS
---

**Dúvida**Como realizar transferência de filiais de títulos de forma automática ao gerar nota fiscal de saída ?  
  
**Ambiente**

Microsiga Protheus -  a partir da versão 12  
  
**Solução** 

Abaixo um exemplo para gerar títulos em uma filial diferente da Filial de Origem (transferências de títulos) de forma automática  
  
Parâmetros  
  
MV\_RETAUTO .T.  
MV\_REMATRI 10  
MV\_APRAUTO​ .T.  
  
Premissa para o teste  
  
Ter 3 filiais e usar o controle de numeração exclusiva.

Duas filiais vão gerar NFs com titulo e outra somente receber os títulos transferidos de acordo com os parâmetros acima   
  
1) Gerar uma NF na Filial 01  
2) Gerar uma NF na Filial 02 com a mesma numeração da Filial 01  
3)   
a) O sistema gravou o Titulo da Filial 01 com prefixo 1 e  Titulo da Filial 10 com prefixo TRS  
b) O sistema gravou o Titulo da Filial 02 com prefixo 1 e  Titulo da Filial 10 com prefixo TRS e E1\_PARCELA 01  
  
O sistema vai emitir a mensagem abaixo

![](https://p23.zdusercontent.com/attachment/888110/LL2tmXSfqYjJhEKXX6ujmSLXK?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..vY6eHfGC83YLTjn-TkvcHw.j9Tv5h9nTGJOkUCOZHz0Di5uCTiCdedo9Qi87leS2LwJmTuQMhwKBh5BZ9I7sdcDw-9zp43PZyDPyXIPu_WaK1xGo7sejaYgp0Dybv8S_Z0xlIEhIyUfzrTz9F_DWPNNeq6YlDPJelXc5UGf7YP1zApzV6s6Tx2qz5IR8iikO_My6MwpL-QGMfg0ZDRc-F47cU9WVMCkPhag0BgDwMwmYZ48KEHLd8vDUVE5Jv6_vY_ori9Fjmhb8TIU2iHnDd2k-i1fiE4Bhfx7ZvfdJi4EtuzTCRl99jdMxdaeXsBrOD8.rSjYMoJBgIs46pXc-7G6SQ)  
O Modulo faturamento aciona a rotina FINA620, portanto, é importante atualizar a rotina
