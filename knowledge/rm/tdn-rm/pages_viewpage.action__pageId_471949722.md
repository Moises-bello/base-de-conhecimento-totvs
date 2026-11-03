---
content_hash: dec8b70d0f733419635b1f7be509b8bdd9b119cfdc98d1bc76afef75077eca3b
fetched_at: '2026-06-29T00:10:16.574860+00:00'
page_id: '471949722'
product: rm
source: tdn-rm
title: FISCAL01-7867 DT Layout ECF - Alterações K156 e M010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471949722
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração do Registro K156 e M010 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-7867 |

## **02. SITUAÇÃO/REQUISITO**

Em relação ao layout da ECF, realizar as seguintes alterações:

1. No Registro K156 foram incluídos os campos:

* VL\_SLD\_INI,
* IND\_VL\_SLD\_INI,
* VL\_DEB e
* VL\_CRED.

2. No Registro M010:

* Incluído o campo 5-COD\_PB\_RFB
* Excluído o campo 6-DESC\_LAN\_ORIG

Manter compatibilidade para períodos anteriores a 2019.

## **03. SOLUÇÃO**

Layout da ECF foram realizadas as seguintes alterações, de acordo com o [Manual ECF 2019](http://sped.rfb.gov.br/estatico/84/62D84C440E97164D123ABE283B1308D53BC17A/Manual_de_Orienta%C3%A7%C3%A3o_da_ECF_Fevereiro_2019.pdf):

**- No Registro K156 foram incluídos os campos:**

* VL\_SLD\_INI
* IND\_VL\_SLD\_INI
* VL\_DEB
* VL\_CRED

**-  No Registro M010:**

* Incluído o campo 5-COD\_PB\_RFB
* Excluído o campo 6-DESC\_LAN\_ORIG

## **04. DEMAIS INFORMAÇÕES**

Estes Registros serão gerados apenas em versões superiores ao Layout ECF 0005.

**Observação:** O Registro K156 foi ligado ao layout da ECF, porém existe uma consistência no serviço do Contábil para que esse Registro seja gerado  apenas para layout ECF-TAF, contudo a versão mais recente do layout ECF-TAF é de 01/05/2016, e conforme alinhado com a PO o ajuste será feito somente na versão ECF do layout. O registro é gerado somente via PVA, conforme mapeamento.
