---
content_hash: a911e37f0e532ad570265ae9a7dd694aaa833388060ae6163ffaffd8dd3f223f
fetched_at: '2026-06-29T00:12:02.617652+00:00'
page_id: '901961557'
product: rm
source: tdn-rm
title: Informações suplementares da NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901961557
version: 16
---

# infNFComSupl - Informações suplementares da NFCom

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **infNFComSupl** | **-** | **1-1** | **Grupo** | **Informações suplementares da NFCom** |
| qrCodNFCom | infNFComSupl | 1-1 | Elemento | Para NFCom com Modalidade de Operação definida como "1 - Normal"   * Composição:   + Url QrCode que será disponibilizado por cada unidade federativa ([Clique aqui](https://dfe-portal.svrs.rs.gov.br/nfcom/Servicos)).   + Chave de Acesso "chNFCom=35251999999990001011621730000000031034451783"   + Tipo do ambiente "tpAmb=2" (1 - Produção / 2 - Homologação) * **Url QrCode** & **chNFCom=Chave de Acesso** & **tpAmb=Tipo do ambiente**    Para NFCom com Modalidade de Operação definida como "2 - Contingência"  **NÃO IMPLEMENTADO**   * Composição:   + Url QrCode que será disponibilizado por cada unidade federativa ([Clique aqui](https://dfe-portal.svrs.rs.gov.br/nfcom/Servicos)).   + Chave de Acesso "chNFCom=35251999999990001011621730000000031034451783"   + Tipo do ambiente "tpAmb=2" (1 - Produção / 2 - Homologação)   + Assinatura "sign=4d4467617356526a4b307a5642627851704a6b4d6c5459664535413d" * **Url QrCode** & **chNFCom=Chave de Acesso** & **tpAmb=****Tipo do ambiente** & **sign=Assinatura**     Parametrização da Url do QrCode: Imagem   Em ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial, Edite a Filial - etapa Ambiente NFCom.   A URL será utilizada no DANFE-COM para consulta. |

Exemploxml
https://www.sefaz.uf.gov.br/nfcom/qrcode?chNFCom=35251999999990001011621730000000031034451783&tpAmb=2
]]>
