---
content_hash: 4c6a51103a05592b29104b42c5d28a81a7ba89b6c02c08138d9f5ab6c982365c
fetched_at: '2026-06-29T00:12:02.317217+00:00'
page_id: '900727351'
product: rm
source: tdn-rm
title: Identificação do destinatário / assinante (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900727351
version: 12
---

# dest - Identificação do destinatário / assinante

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **dest** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **1-1** | **Grupo** | **Identificação do destinatário / assinante**  **O grupo será gerado com os dados do destinatário que poderá ser um Cliente/Fornecedor ou Filial**  Conforme marcado o parâmetro do tipo de movimento localizado em:  Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento | Emitente/Destinatário 1/2 | Campo Destinatário |
| xNome | dest | 1-1 | Elemento | Nome do Cliente/Fornecedor ou da Filial. |
| CNPJ | dest | 1-1 | Elemento de escolha | CNPJ do Cliente/Fornecedor ou Filial Destino |
| CPF | CPF do Cliente/Fornecedor ou Filial Destino |
| idOutros | Campo Documentos Estrangeiro do Cliente/Fornecedor |
| indIEDest | dest | 1-1 | Elemento | Indicador da inscrição estadual do destinatário:  1 - Contribuinte ICMS (informar a IE do destinatário); 2 - Contribuinte isento de Inscrição no cadastro de Contribuintes do ICMS; 9 - Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS.  No cadastro do Cliente/Fornecedor, pasta Integrações | Tributos.  No caso do cadastro da Filial, Anexos | Dados Fiscais | pasta Dados Adicionais | aba Tributos. |
| IE | dest | 0-1 | Elemento | Se o campo indIEDest = 1, Inscrição Estadual da Filial Emitente ou do Cliente/Fornecedor  Se o campo indIEDest = 2, este campo será gerado com a palavra ISENTO  Se o campo indIEDest = 9, este campo não será gerado |
| IM | dest | 0-1 | Elemento | Inscrição Municipal Filial ou do Cliente/Fornecedor.  Se não possuir este campo não será gerado |
| **enderDest** | **dest** | **1-1** | **Grupo** |  |

Exemploxml  
TOTVS
00009654000672
2
ISENTO
2606715555

RUA - Centralina
100
complemento filial
BAIRRO - Santa inês
4202008
Balneario Camboriu
22222222
SC
03133221144
teste@totvs.com.br
]]>
