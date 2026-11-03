---
content_hash: 3ab0ca689933bd45162613dbe406695815bc87489f5843513c4f35ddb40deb56
fetched_at: '2026-06-29T00:11:10.060549+00:00'
page_id: '641157858'
product: rm
source: tdn-rm
title: DT 12462869 FISCAL01-16639 REINF - R-1000
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+12462869+FISCAL01-16639+REINF+-+R-1000
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Ticket: | 12462869 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16639 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DA DEMANDA

Ao realizar a geração do evento R-1000 para empresa de órgão publico ao tentar realizar a transmissão do evento, ocorre o erro MS1010 - ID Invalido.

TESTES REALIZADOS

Em base exemplo foi realizada a geração do evento R-1000 e ao tentar realizar a validação do evento ocorre erro de MS1010 - ID Invalido. O Erro ocorre pois a TAG <nrInsc> quando for gerada para empresas de natureza jurídica do declarante for de administração publica a mesma deve gerar o CNPJ Completo e não somente a raiz do CNPJ, fato que está correto. Porém o ID informado <evtInfoContri id="ID1000000073336832021091509565000000> na posição referente ao CNPJ está informado somente a RAIZ quando o mesmo deverá ser informado todo o CNPJ. Abaixo XML gerado em base exemplo:

<?xml version="1.0" encoding="utf-8"?><Reinf xmlns="http://www.reinf.esocial.gov.br/schemas/evtInfoContribuinte/v1\_05\_01"><evtInfoContri id="ID1000000073336832021091509565000000"><ideEvento><tpAmb>2</tpAmb><procEmi>1</procEmi><verProc>1\_05\_01</verProc></ideEvento><ideContri><tpInsc>1</tpInsc><nrInsc>07333683000148</nrInsc></ideContri><infoContri><inclusao><idePeriodo><iniValid>2021-08</iniValid></idePeriodo><infoCadastro><classTrib>11</classTrib><indEscrituracao>0</indEscrituracao><indDesoneracao>0</indDesoneracao><indAcordoIsenMulta>0</indAcordoIsenMulta><indSitPJ>0</indSitPJ><contato><nmCtt>Décio Antonio da Silva</nmCtt><cpfCtt>75924072649</cpfCtt><foneFixo>03102812940</foneFixo><foneCel>031999999999</foneCel><email>rm@[com.br](http://com.br)</email></contato><softHouse><cnpjSoftHouse>53113791001285</cnpjSoftHouse><nmRazao>TOTVS S.A.</nmRazao><nmCont>Eduardo Pires</nmCont><telefone>3121229000</telefone><email>desenvolvimento-dfe-rm@[totvs.com.br](http://totvs.com.br)</email></softHouse><infoEFR><ideEFR>S</ideEFR></infoEFR></infoCadastro></inclusao></infoContri></evtInfoContri></Reinf>

## **03. SOLUÇÃO.**

Na geração do ID da R-1000, quando a filial for de Natureza Jurídica de Órgão Público, Cnpj virá com os 14 dígitos.

Ex:

       <evtInfoContri id="ID1**17827056000117**2021092017351800000">
