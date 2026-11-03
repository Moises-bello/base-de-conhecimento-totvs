---
content_hash: 689579fb4305cb36c4b790bdbfa211351bfe3dbc5776b00b029a605c70de38a3
fetched_at: '2026-06-29T00:05:48.477262+00:00'
page_id: '1024825495'
product: rm
source: tdn-rm
title: infDPS/IBSCBS/imovel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024825495
version: 5
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **imovel** | **IBSCBS** | **Não** | **Grupo** | **Grupo de informações relativas ao Imóvel** |
| inscImobFisc | imovel | Sim | aba **“Dest. Serviço”** Grupo Imóvel -   Campo **→** TMOVFISCALSERV/INSCRICAOIMOBILIARIA | Inscrição Imobiliária Fiscal do Imóvel destinado ao serviço. |
| cCIB | imovel | **Sim\*** | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/CIB | Cadastro Imobiliário Brasileiro do Imóvel destinado ao serviço. |
| **end** | **imovel** | **Sim\*** | **Grupo** | **Grupo de informações do endereço do Imóvel destinado ao serviço.** |
| CEP | end | **Sim\*** | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/CEPENDIMOVEL | Código numérico do Endereçamento Postal nacional (CEP)    do endereço do Imóvel destinado ao serviço. |
| **endExt** | **end** | **Sim\*** | **Grupo** | **Grupo de informações do endereço no exterior.** |
| cEndPost | endExt | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELEXTCEP | Código alfanumérico do Endereçamento Postal no exterior do Imóvel destinado ao serviço. |
| xCidade | endExt | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELEXTCIDADE | Nome da cidade no exterior do Imóvel destinado ao serviço. |
| xEstProvReg | endExt | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELEXTREGIAO | Estado, província ou região da cidade no exterior do Imóvel destinado ao serviço. |
| xLgr | end | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELLOGRADOURO | Tipo e nome do logradouro do endereço do Imóvel destinado ao serviço. |
| nro | end | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELNUMERO | Número no logradouro do endereço do Imóvel destinado ao serviço. |
| xCpl | end | Não | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELCOMPLEMENTO | Complemento do endereço do Imóvel destinado ao serviço. |
| xBairro | end | Sim | aba **“Dest. Serviço”** Grupo Imóvel -  Campo **→** TMOVFISCALSERV/ENDIMOVELBAIRRO | Bairro do endereço do Imóvel destinado ao serviço. |

Elemento de escolha

Para os campos marcados com asterisco ("**Sim\***"), é obrigatório que pelo menos uma das informações sejam preenchidas. Por exemplo, caso o **cCIB** seja informado, não será informado o **end**, assim como se o **CEP** seja informado, não será informado o **endExt**.
