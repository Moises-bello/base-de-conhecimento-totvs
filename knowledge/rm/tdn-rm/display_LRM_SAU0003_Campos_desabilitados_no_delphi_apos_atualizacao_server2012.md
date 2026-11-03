---
content_hash: 2d7b8cd84e675cb27ec75c4efd1e6cce94333b5bcaed4392fea59dbf75865502
fetched_at: '2026-06-29T00:05:59.863444+00:00'
page_id: '192100362'
product: rm
source: tdn-rm
title: SAU0003_Campos_desabilitados_no_delphi_apos_atualizacao_server2012
type: documentation
url: https://tdn.totvs.com/display/LRM/SAU0003_Campos_desabilitados_no_delphi_apos_atualizacao_server2012
version: 115
---

# SAU0003\_Campos\_desabilitados\_no\_delphi\_apos\_atualizacao\_server2012

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Versões:** | 11.8X e 12.1X |
| **Ocorrência:** | Após atualizar meu SQL Server para a versão 2012, todos os Menus em DELPHI foram desabilitados. |
| **Passo a passo:** | Primeiro realize o passo a passo que esta nesse link abaixo:  <http://tdn.totvs.com/display/public/rm/RM+Conversor+-+ODBC+SQL+Server+2012>  [Após isto, realizar o passo a passo abaixo.](http://tdn.totvs.com.br/display/public/rm/SQL+Server+-+ODBC+SQL+Server+2012)  Acesse seu BDE => Aba Database => Selecione o alias desejado (Ex.: CorporeRM) => Na propriedade BLOB SIZE coloque o valor 512 e na propriedade BLOBS TO CACHE coloque o valor 1024;  Acesse seu BDE => Aba Configuration => Configuration => Drivers => ODBC => Selecione SQL Server Native Client 11.0 => Na propriedade BLOB SIZE coloque o valor 512 e na propriedade BLOBS TO CACHE coloque o valor 1024;  Salve as alterações, feche o BDE, feche a aplicação, abra novamente e teste se os menus voltaram a funcionar corretamente. |

divs
