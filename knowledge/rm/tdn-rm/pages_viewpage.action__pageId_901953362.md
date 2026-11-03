---
content_hash: 27387e0f432ae579486b51fbaacf340d41b5a5a8cb9e0939012edf9141be09f9
fetched_at: '2026-06-29T00:12:02.427141+00:00'
page_id: '901953362'
product: rm
source: tdn-rm
title: Dados do assinante (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901953362
version: 22
---

# assinante - Dados do assinante

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **assinante** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **1-1** | **Grupo** | **Dados do assinante** |
| iCodAssinante | assinante | 1-1 | Elemento | Se tipo destinatário igual a empresa, CGC da filial de destino.  Senão o CPF, CNPJ ou Documento estrangeiro do cliente fornecedor. |
| tpAssinante | assinante | 1-1 | Elemento | Movimento | Integrações | Comunicação / Telecomunicação | campo: Tipo Assinante. TMOV.TIPOASSINANTE |
| tpServUtil | assinante | 1-1 | Elemento | Movimento | Integrações | Comunicação / Telecomunicação | campo: Tipo Utilização. TMOVFISCAL.IDTIPOUTILIZACAO |
| nContrato | assinante | 0-1 | Elemento | Movimento | Integrações | Comunicação / Telecomunicação | campo: Número do contrato.  TMOVFISCAL.NROCONTRATOASSINANTE |
| dContratoIni | assinante | 0-1 | Elemento | Movimento | Integrações | Comunicação / Telecomunicação | campo: Data de inicio do contrato.  TMOVFISCAL.DATACONTRATOINIASSINANTE, |
| dContratoFim | assinante | 0-1 | Elemento | Movimento | Integrações | Comunicação / Telecomunicação | campo: Data de término do contrato.  TMOVFISCAL.DATACONTRATOFIMASSINANTE |
| **--- x — Sequência opcional do XML:  Será gerado de acordo com o preenchimento dos campos. Caso um campo seja preenchido o outro se torna obrigatório.** | | | | |
| NroTermPrinc | assinante | 1-1 | Elemento da Sequencia | Movimento | Integrações | Comunicação / Telecomunicação | campo: Numero do terminal.  TMOVFISCAL.NROTERMINALPRINCASSINANTE |
| cUF | assinante | 1-1 | Elemento da Sequencia | Movimento | Integrações | Comunicação / Telecomunicação | campo: UF de habilitação do terminal.  TITMMOVFISCAL.CODETDHABILITACAOTEL |
| **--- x — Sequência opcional do XML: Não será gerado** | | | | |
| NroTermAdic | assinante | 1-1 | Elemento da Sequencia | Não será gerado. |
| cUF | assinante | 1-1 | Elemento da Sequencia | Não será gerado. |

Exemplo

<Assinante>  
     <iCodAssinante>00000000000010</iCodAssinante>  
     <tpAssinante>99</tpAssinante>  
     <tpServUtil>5</tpServUtil>  
     <nContrato>123456789</nContrato>  
     <dContratoIni>2025-09-11</dContratoIni>  
     <dContratoFim>2025-09-11</dContratoFim>  
     <NroTermPrinc>98765432</NroTermPrinc>  
     <cUF>MG</cUF>  
</Assinante>
