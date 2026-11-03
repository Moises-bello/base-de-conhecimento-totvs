---
content_hash: 3961784998b1f3bf2be2cc339da9a0f04bfb28f06df5345f4db6c6d0bcc5ff64
fetched_at: '2026-06-29T00:12:02.285948+00:00'
page_id: '900451399'
product: rm
source: tdn-rm
title: Informações da NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900451399
version: 14
---

# infNFCom - Informações da NFCom

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **infNFCom** | **-** | **1-1** | **Grupo** | **Informações da NFCom** |
| versao | infNFCom | 1-1 | Atributo | Parametrização da versão: Imagem  Em ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial, Edite a Filial - etapa Ambiente NFCom. |
| Id | infNFCom | 1-1 | Atributo | Chave de acesso na NFCom, composta pelos seguintes campos:   | Campos | Tamanho | | --- | --- | | Código da UF do emitente do Documento Fiscal | 02 | | Ano e Mês de emissão da NFCom (AAMM) | 04 | | CNPJ do emitente | 14 | | Modelo do Documento Fiscal | 02 | | Série do Documento Fiscal | 03 | | Número do Documento Fiscal | 09 | | Forma de emissão da NFCom | 01 | | Site do Autorizador que recepcionou a NFCOM | 01 | | Código Numérico que compõe a Chave de Acesso | 07 | | Dígito Verificador da Chave de Acesso | 01 | |
| **ide** | **infNFCom** | **1-1** | **Grupo** |  |
| **emit** | **infNFCom** | **1-1** | **Grupo** |  |
| **dest** | **infNFCom** | **1-1** | **Grupo** |  |
| **assinante** | **infNFCom** | **1-1** | **Grupo** |  |
| **gSub** | **infNFCom** | **0-1** | **Grupo** |  |
| **gCofat** | **infNFCom** | **0-1** | **Grupo** |  |
| ****det**** | **infNFCom** | **1-990** | **Grupo** |  |
| ****total**** | **infNFCom** | **1-1** | **Grupo** |  |
| ****gFidelidade**** | **infNFCom** | **0-1** | **Grupo** |  |
| ****gFat**** | **infNFCom** | **0-1** | **Grupo de Escolha** |  |
| ****gFatCentral**** | **infNFCom** | **0-1** | **Grupo de Escolha** |  |
| ****autXML**** | **infNFCom** | **0-10** | **Grupo** |  |
| ****infAdic**** | **infNFCom** | **0-1** | **Grupo** |  |
| ****gRespTec**** | **infNFCom** | **0-1** | **Grupo** |  |

Exemploxml
]]>
