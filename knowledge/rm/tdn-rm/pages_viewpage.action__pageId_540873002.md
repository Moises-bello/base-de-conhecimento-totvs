---
content_hash: 7ccecff1e3251dd147cfa303223f44372c340edaf1f42358d1f6b1f28fceed8b
fetched_at: '2026-06-29T00:10:37.349619+00:00'
page_id: '540873002'
product: rm
source: tdn-rm
title: CONTROLADORIA01-4224 DT Cadastro de Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540873002
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Totvs Gestão Patrimonial |
| Função: | Cadastro de inventários |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | CONTROLADORIA01-4224 |

## **02. SITUAÇÃO/REQUISITO**

É necessário implementar o cadastro dos inventários que serão disponibilizados pelo aplicativo responsável por gerenciar e realizar a coleta de patrimônios.

## **03. SOLUÇÃO**

Adicionar uma nova aba, Inventário Mobile, no módulo patrimonial. Ela deve disponibilizar o cadastro de inventário que será iniciado posteriormente pelo aplicativo de inventário. Este CRUD deverá conter as seguintes informações:

**Aba Identificação**

* Código do inventário
* Descrição do inventário
* Período de validade do inventário

Será composto pelas datas inicial e final.

* Tipo de inventário

Essa opção deverá listar o Centro de Custo, o Departamento, a Filial e o Local. Após selecionar uma dessas opções deverá ser exibida uma nova aba que irá permitir adicionar um ou mais registros para o tipo de inventário informado. As demais abas não deverão ser exibidas.

**Aba Centro de Custo**

Deverá disponibilizar um LookupMultRecord que irá permitir visualizar, incluir, alterar e excluir centros de custo.

**Aba Departamento**

Deverá disponibilizar um LookupMultRecord que irá permitir visualizar, incluir, alterar e excluir departamentos.

**Aba Filial**

Deverá disponibilizar um LookupMultRecord que irá permitir visualizar, incluir, alterar e excluir filiais.

**Aba Local**

Deverá disponibilizar um LookupMultRecord que irá visualizar, incluir, alterar e excluir locais.

* Usuários do Inventário

Deverá disponibilizar uma visão (RMSDetailPanel) onde será possível visualizar, incluir, alterar e excluir usuários. Durante a inclusão ou alteração deverá ser disponibilizada uma tela onde será possível informar os campos usuário (lookup) e responsável (checkbox).

O inventário deverá possuir um ou mais usuários que poderão ser ou não responsáveis por esse inventário.
