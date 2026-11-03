---
content_hash: 97006fffa731eda098222ed8dcde32dadf68a66fa3f67fc78ae49887b1acab7d
fetched_at: '2026-06-29T00:10:56.994793+00:00'
page_id: '593953075'
product: rm
source: tdn-rm
title: FISCAL01-14806 DT - Mascara do código de serviço Federal - Mashup e NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593953075
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Atualização de Municípios Homologados  Transmissão de NFS-e através do TSS |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14806  FISCAL01-14807 |

## **02. SITUAÇÃO/REQUISITO**

* Alterar o processo de Atualização de Municípios Homologados para sincronizar com a coluna criada no mashups
* Alterar o Form do RM.Fiscal.exe para reconhecer o novo campo
* Renomear Label Duplicada "Validar Schema" o nome correto é "Gerar CNAE"
* Alterar o processo de Transmissão de NFS-e via TSS para considerar a máscara definida na DMUNICIPIONFSE na geração da tag do Código do Serviço Federal no XML

## **03. SOLUÇÃO**

* No Mashup foi criado a coluna MASCARACODFEDERAL e incluída no CRUD dos Municípios Homologados
* Foi alterado o Processo de Atualização de Municípios Homologados, para que ao ser executado a coluna na DMUNICIPIONFSE atualize a MASCARACODFEDERAL
* No form RM.Fiscal.exe foi alterado o cadastro de Inclusão de Municípios Homologados incluindo a coluna MASCARACODFEDERAL
* No Processo de Atualização de Municípios Homologados foi alterado a label "Validar Schema" que estava duplicada
* Na transmissão da NFS-e através do TSS, caso esteja definido uma máscara para este município no campo DMUNICIPIONFSE.MASCARACODFEDERAL, o sistema irá gerar a tag referente ao Código do Serviço Federal no XML conforme definido na máscara.

Opções de Preenchimento da Máscara:

* # - Preenchimento obrigatório do dígito
* Q - Preenchimento do dígito apenas se for maior 0 (Deve ser utilizado somente no primeiro dígito da máscara)

Exemplo das opções de Máscara:

| Código Cadastro do Serviço | Máscara definida na DMUNICIPIONFSE | Valor no XML |
| --- | --- | --- |
| 1.05 | ##.## | 01.05 |
| 1.05 | Q#.## | 1.05 |
| 1.05 | #### | 0105 |
| 1.05 | Q### | 105 |
| 12.05 | ##.## | 12.05 |
| 12.05 | Q#.## | 12.05 |
| 12.05 | #### | 1205 |
| 12.05 | Q### | 1205 |

**Observações:**

* O Código é definido no cadastro do serviço em Anexos | Dados Fiscais do Produto, campo: Código de Serviço Federal
* A Máscara é definida pela TOTVS no Mashups. Caso o cliente identifique algum município que precise desta definição é necessário entrar em contato com o Suporte Técnico
