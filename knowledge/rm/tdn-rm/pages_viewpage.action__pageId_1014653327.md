---
content_hash: 8a84c599627c8b0cbad542f6ef53cc7338a2a9ebb980c5e3233d9990eb2add20
fetched_at: '2026-06-29T00:05:47.444627+00:00'
page_id: '1014653327'
product: rm
source: tdn-rm
title: infDPS/IBSCBS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1014653327
version: 15
---

Grupo gerado apenas quando a Base do Tributo IBS/CBS esta maior que zero ou quando a mesma for igual a zero e o Valor Total do Serviço do Item for igual a zero.

card

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **IBSCBS** | **infDPS** | **Não** | **Grupo** | **Grupo de informações declaradas pelo emitente referentes ao IBS e à CBS** |
| finNFSe | IBSCBS | Sim | **FIXO:** 0 = NFS-e regular | Indicador da finalidade da emissão de NFS-e  0 = NFS-e regular |
| indFinal | IBSCBS | Sim | aba **“Integrações Fiscais” →** flag **“Consumidor Final”**.  TMOVFISCAL.OPERACAOCONSUMIDORFINAL | Indica operação de uso ou consumo pessoal.  0 = Não 1 = Sim |
| cIndOp | IBSCBS | Sim | Item do Movimento **→ Integrações → Fiscal**   TITMMOVFISCAL.CODINDOP | Código indicador da operação de fornecimento, conforme tabela “código indicador de operação” |
| tpOper | IBSCBS | Não | aba **“Integrações ” →** **“Fiscal 2”**  As informações são geradas somente se o campo estiver diferente de 0 - Não se Aplica.    TMOVFISCAL.TPOPER | Código indicador da Operação com Entes Governamentais ou serviços sobre bens e imóveis. |
| [gRefNFSe](https://tdn.totvs.com/pages/viewpage.action?pageId=1065234342) | IBSCBS | Não | aba "**Integrações**" → "**Referências Doc**" | Indica o grupo de informações de Notas Fiscais de Serviço Eletrônicas referenciadas. O preenchimento ocorre de forma automática quando houver documentos de referência no movimento, em conformidade com o [guia de parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=574128446) |
| tpEnteGov | IBSCBS | Não | aba **“Cadastro” →** **“Cliente/Fornecedor”**  O campo está na aba de edição do cliente em  **“Outros” →** **“Tributos”** | Código identifica se o cliente/fornecedor é do tipo Ente Governamental.  Para ser considerado um Ente Governamental a campo Órgão Público deve esta selecionado com uma das opção.   * Federal. * Estadual * Municipal * Distrito Federal   Caso a seleção escolhida seja a "não se aplica" a tag não será evidenciada no xml |
| indDest | IBSCBS | Sim | aba **“Integrações Fiscais” →** **“Dest. Serviço”**  Se os dados do destinatário forem os mesmos do Tomador é gerado como "0". Caso contrário é gerado como  "1" | A respeito do Destinatário dos serviços:  0 – o destinatário é o próprio tomador/adquirente identificado na NFS-e (tomador=adquirente=destinatário); 1 – o destinatário não é o próprio adquirente, podendo ser outra pessoa, física ou jurídica (ou equiparada), ou um estabelecimento diferente do indicado como tomador (tomador=adquirente ≠ destinatário); |
|  | IBSCBS | Não | aba **“Integrações Fiscais” →** **“Dest. Serviço”**  As informações do Destinatário são geradas somente se o campo "*indDest*" for igual a 1 | Grupo de informações relativas ao Destinatário |
|  | IBSCBS | Não | aba **“Integrações Fiscais” →** **“Dest. Serviço”** | Grupo de informações relativas ao Imóvel |
|  | IBSCBS | Sim |  | Grupo de informações relativas aos valores do serviço prestado para IBS e CBS |
