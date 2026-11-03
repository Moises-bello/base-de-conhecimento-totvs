---
content_hash: 70f98c6dd16354e8cd882304c67e183f61a85cd688b4768663f9f0932bfd8d20
fetched_at: '2026-06-29T00:10:36.387278+00:00'
page_id: '532039771'
product: rm
source: tdn-rm
title: DT Serviço de WebService - Processo Seletivo RM - EduMatricAprovadosPSData
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532039771
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Processo Seletivo RM |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-12543,  EDUCACIONAL01-12544,  EDUCACIONAL01-12545 |

02. SITUAÇÃO/REQUISITO

Para redução de chamadas aos serviços após a execução do processo de matricular alunos pelo processo seletivo RM, foi disponibilizado dois novos parâmetros que estão descritos abaixo.

* **DiasVencimentoPrimeiraParcela**, este parâmetro permite definir quais os dias para o vencimento da primeira parcela do contrato quando definido para gerar contrato.
* **GerarContratoAssinado**, este parâmetro permite se ao gerar o contrato o mesmo já vai indicar que está assinado

 Foi também criado dois parâmetros que permitem definir formulas visuais para serem executadas antes ou depois da criação do contrato se no processo seletivo estiver definido para cadastrar um contrato.

* Configurações -> Parâmetros -> 15.03 - Matrícula -> Fórmulas Visuais 2/2

Importante

Este parâmetros somente estão disponíveis para os serviços webservice do dataserver EduMatricAprovadosPSData, não sendo possível parametrizar na tela do processo pelo RM exe.

Para mais informações acesso o .
