---
content_hash: 45902d867c94f029c64862d171b5f0bd85cd12b5b7c8281d4ec7e38a90b198c3
fetched_at: '2026-06-29T00:08:11.476042+00:00'
page_id: '243010482'
product: rm
source: tdn-rm
title: TVDVQ1_DT_Utilização_DataServer_MntLogServData
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243010482
version: 113
---

# Utilização de DataServer RMOfficina

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | TOTVS Gestão de Manutenção. |
| **Função:** | *Utilização do DataServer de apontamento MntLogServData* |
| **Situação/Requisito:** | *Ao realizar a utilização do dataserver o sistema estava exibindo um erro não tratado.*  "DataServer MntLogServData - Não há linha na posição 0." |
| **Solução/Implementação:** | *Foi realizado a implementação para que o dataserver possa ser utilizado. O xml que deve ser utilizado deve seguir exatamente o formato abaixo:*  <MntLogServ>  <OfLogServ> <CODCOLIGADA>1</CODCOLIGADA> <IDMOV>6038</IDMOV> <NSEQITMMOV>1</NSEQITMMOV>  <INICIO>2016-07-05T00:00:00</INICIO> <TERMINO>2016-07-05T00:00:00</TERMINO>  <HORAINICIO>12:16:00</HORAINICIO> <HORATERMINO>14:00:00</HORATERMINO>  <DATA>2016-07-05T10:59:00</DATA>  <CODPESSOA>186</CODPESSOA> <CHAPA>00038</CHAPA> <DESCRICAO>Outro serviço a executar</DESCRICAO> </OfLogServ> </MntLogServ> |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |

divs
