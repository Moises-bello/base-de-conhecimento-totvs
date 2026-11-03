---
content_hash: e085bc4fa966606f9ed184bdd1888f963e104537f28497d9b18b9994af637bfc
fetched_at: '2026-06-29T00:11:04.095187+00:00'
page_id: '624983323'
product: rm
source: tdn-rm
title: FISCAL01-15840 DT Filial - Incluir um campo "ATIVO" no cadastro da Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624983323
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Filial |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15840 |

## **02. SITUAÇÃO/REQUISITO**

Incluir um campo "ATIVO" no cadastro da Filial

Inicialmente este campo não tem regras, mas gradativamente iremos evoluir os processos do sistema para considerarem apenas as filiais Ativas.

## **03. SOLUÇÃO**

No formulário de cadastro de filiais *FisFilialFormBR* foi incluído um campo *checkbox* denominado cATIVO para validação do status da filial, sendo ele por default selecionado como ativo.

**O campo não tem efeitos de desativar a Filial, trata-se de um campo auxiliar meramente informativo.**

Campo criado na base como SMALLINT, sendo 1 para *true* e 0 *false.*

Não há regras específicas para o campo no código, apenas um *CheckedChanged* validando se o mesmo não está marcado, com isso, é passado via *bindingSource* os valores pelo *enum FisTipoSimNaoEnum*.

* Foi criado o método *ValidarCampoDefensivo* dentro de *FisFilialDataBR* para validar se existe o campo dentro de bases diferentes. O método é chamado dentro do *GetQueryRecordSQL* por interpolação no SELECT para SQL Server e Oracle.
* Dentro da classe *FisFilialDataApi* foi incluído o campo *GFILIAL.ATIVO*.

* Foi criado em *Resources* o *SFisCaptionAtivo* com o valor *Ativo*.

* Na classe *FisFilialPropsBR* foi criado o *SetProps* para o campo *Ativo* da tabela *GFILIAL* passando o *Caption*.
* Foi criado a propriedade *Ativo* dentro de *FisFilialEntity* e o mapeamento da mesma dentro da classe *FisFilialMapper.*
