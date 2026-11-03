---
article_id: 25827228129047
category: Originação de Grãos (OG)
content_hash: 5965c607dfa116c012acace25e6ac260a8f2578d55c7906ff669d59c5200c7c4
fetched_at: '2026-06-28T22:45:44.905090+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Serviço de armazenagem - Inclusão da Rotina Automática
  MVC
type: support-article
updated_at: '2025-06-24T20:42:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25827228129047-Agro-Linha-Protheus-AGR-Servi%C3%A7o-de-armazenagem-Inclus%C3%A3o-da-Rotina-Autom%C3%A1tica-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827228120087) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Como efetuar a inclusão da **Rotina Automática MVC Serviço de armazenagem?**  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**A rotina de **Serviço de Armazenagem - OGA261** foi criado usando a arquitetura **Model-View-Controller ou MVC**, possibilitando o uso da regra de negócio em aplicações automática. Esta rotina faz uso da tabela **NKG**.

A finalidade deste documento é exemplificar a inclusão, alteração e exclusão de um serviço de armazenagem via rotina automática **MVC**. 

No Padrão, os registros de serviço de armazenagem são exclusivamente gerados via rotina de cálculo de **Serviço de Armazenagem - OGA262**, não sendo possível via rotina de serviço de armazenagem a inclusão e/ou alteração destes registros, apenas exclusão.

Porém por se tratar de uma rotina que usa a arquitetura **MVC**, é possível usar seu modelo para customização.  
Contudo, qualquer customização que faz uso do modelo de dados em **MVC**, deverá ser de responsabilidade do cliente a origem e validações dos registros.

Inclusão:

**Exemplo de código - Inclusão de um registro**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54 | `User Function zIMVC261()`  `Local lRet := .F.`  `Local oModel := Nil`  `//Exemplo inclusao serviço de entrada`  `oModel  := FWLoadModel('OGA261')`  `oModel:GetModel('NKGUNICO'):GetStruct():SetProperty('NKG_FECSER',MODEL_FIELD_OBRIGAT, .F.) //remove obrigatoriedade do campo.`    `oModel:SetOperation(3) //INCLUSÃO`  `oModel:Activate()`    `//Setando valores nos campos`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_ITEMOV', '00000003')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODROM', '0000000643')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_ITEROM', '01')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODDEV', '000002')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_LOJDEV', '01')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODENT', '000002')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_LOJENT', '01')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODSAF', '2122')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODPRO', 'AGR-SOJA GRANEL')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_UM1PRO', 'KG')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DOCSER', '267')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DOCNUM', '267178001')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DOCEMI', ctod('01/07/2024'))`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DATCAL', ctod('01/08/2024'))`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODTSE', '0001')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_ITETSE', '001')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_CODDES', '003')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_FATGER', '1') //Entrada`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_PERCOB', '0')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DATINI', ctod('01/08/2024'))`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_DATFIM', ctod('01/08/2024'))`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_QTDPER', 1)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_TIPRET', '1') //cobrança`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VALTAR', 25)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_UMTAR', 'TN')`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_QTDBAS', 20)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VLTARC', 500)`  `oModel:GetModel('NKGUNICO'):SetValue('NKG_VALSER', 500)`  `oModel:GetModel('NKGUNICO'):LoadValue('NKG_CODCTR', "000178")`    `oModel:GetModel('NKGUNICO'):SetValue('NKG_STATUS', '1')`    `If oModel:VldData() //valida os dados`  `oModel:CommitData() //realiza a gravação do registro`  `MsgInfo("Registro incluído com sucesso")`  `lRet := .T.`  `Else`  `VarInfo("",oModel:GetErrorMessage())`    `MsgAlert("Erro ao incluir o registro")`  `EndIf`    `return lRet` |

**Saiba mais:**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Alterar](https://totvssuporte.zendesk.com/knowledge/editor/new/pt-br?brand_id=1509248&template_id=115015907348)**

**[Agro - Linha Protheus - AGR - Rotina Automática MVC Serviço de armazenagem - Excluir](https://totvssuporte.zendesk.com/knowledge/editor/01J5X4X099K2AFQH7AA8KC2PVD/pt-br?brand_id=1509248&template_id=115015907348)**
