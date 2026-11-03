---
content_hash: 709bd5b35a7152ebc16b81d320c21801052def9c8dc85e123bf6db2320a37e67
fetched_at: '2026-06-29T00:12:02.303999+00:00'
page_id: '900452652'
product: rm
source: tdn-rm
title: Identificação do Emitente do documento fiscal (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900452652
version: 11
---

# emit - Identificação do Emitente do documento fiscal

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **emit** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **1-1** | **Grupo** | **Identificação do Emitente do documento fiscal** |
| CNPJ | emit | 1-1 | Elemento | CNPJ da Filial Emitente |
| IE | emit | 1-1 | Elemento | Inscrição Estadual da Filial Emitente |
| IEUFDest | emit | 0-1 | Elemento | Inscrição Estadual ST cadastrada para o estado do destinatário.   É gerado quando:  Operação interestadual E Destinatário "Não contribuinte" E a filial possuir Inscrição estadual ST cadastrada para o Estado do Destinatário.  Se não se enquadrar na regra este campo não será gerado |
| CRT | emit | 1-1 | Elemento | * **1=Simples Nacional:** Será gerado 1 se no cadastro da Filial estiver configurado Optante pelo Simples * **2=Simples Nacional:** Para o caso de excesso de sublimite deve ser marcado o parâmetro SUBLIMITE EXCEDIDO que só estará disponível para filiais optantes pelo simples. * **3=Regime Normal:** Todas as demais situações |
| xNome | emit | 1-1 | Elemento | Campo Nome informado na aba Identificação do cadastro da Filial Emitente. |
| xFant | emit | 0-1 | Elemento | Campo Nome Fantasia informado na aba Identificação do cadastro da Filial Emitente.  Se estiver em branco este campo não será gerado |
| **enderEmit** | **emit** | **1-1** | **Grupo** |  |

Exemploxml
99999999000191
700005305991
3
NFCOM EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL
NFCOM EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL

...
]]>
