---
content_hash: 1afc424a90bdd7eedd2c52ce505a1689621d0fce6ef5aa609e9c065f8c8a9721
fetched_at: '2026-06-29T00:12:16.242711+00:00'
page_id: '982929067'
product: rm
source: tdn-rm
title: Grupo de informações de compras governamental- CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982929067
version: 3
---

# 1. CT-e

# A emissão da **Modelo Nacional** passa a considerar as informações configuradas para operações com entes governamentais.

1.1 Geração da tag tpEnteGov (Tipo de Ente Governamental)

A tag será gerada quando:

* o **Cliente/Fornecedor estiver classificado como Órgão Público**, e o campo **Tipo de Operação com Entes Governamentais** estiver **diferente de "0 - Nenhum"**.
* Ao habilitar o **Tipo de Operação com Entes Governamentais** é gerado os grupos **gCompraGov e** **gTribCompraGov** sendo respectivamente dependentes. Estes grupos deverão ser gerados sempre que o cliente/fornecedor for um Órgão Públicoee a tag **tpEnteGov** estiver em preenchida.

**gCompraGov (Grupo do grupo de compras governamentais )**

| Campo | Ele | Pai | Tipo | Ocor | Tam | Descrição | Origem dos Dados |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tpEnteGov | E | gCompraGov | N | 1-1 | 1 | Para administração pública direta e suas autarquias e fundações: 1=União 2=Estados 3=Distrito Federal 4=Municípios 5=Consórcio Público - Será implementado sob Demanda 6=Comitê Gestor do IBS - Será Implementado sob Demanda | Gerado conforme o Campo Órgão Publico do Cadastro do Cli\For - FCFO.ORGAOPUBLICO |
| pRedutor | E | gCompraGov | N | 1-1 | 3v2-4 | Percentual de redução de alíquota em compra governamental Conforme LC 214/25: TÍTULO II DAS COMPRAS GOVERNAMENTAIS, Art. 472 | TTRBMOV.PCTREDUTORGOV |
| tpOperGov | E | gCompraGov | N | 1-1 | 1 | Tipo da operação com ente governamental: 1 – Fornecimento com pagamento posterior; 2 - Recebimento do pagamento com fornecimento já realizado; 3 – Fornecimento com pagamento já realizado; 4 – Recebimento do pagamento com fornecimento posterior; | aba **“Integrações ” →** **“Fiscal 2”** As informações são geradas somente se o campo estiver diferente de 0 - Não se Aplica.   TMOVFISCAL.TPOPER |
| refDFeAnt | E | gCompraGov | N | 1-1 | 1 | Chave de acesso do documento fiscal anterior. Deverá ser informado para tpOperGov 2 e 3 e vedado para os tipos 1 e 4 Obs: a chave de acesso deverá ser de um emitente com o mesmo CNPJ base | TCHAVEACESSOREF.CHAVEACESSO |

**gTribCompraGov (Grupo de informações da composição do valor do IBS e da CBS em compras governamental)**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | Grupo Pai | **Ocorrência** | **Ele** | **Descrição** | **Descrição** |
| **gTribCompraGov** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **0-1** | **Grupo** | **Grupo de informações da composição do valor do IBS e da CBS em compras governamental** Este grupo será gerado sempre que o grupo ide.gCompraGov for gerado |  |
| pAliqIBSUF | gTribCompraGov | 1-1 | Elemento | Alíquota IBS da UF utilizada | gIBSUF.pIBSUF |
| vTribIBSUF | gTribCompraGov | 1-1 | Elemento | Valor do Tributo do IBS da UF Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/20025 | gIBSCBS.vBC \* pAliqIBSUF |
| pAliqIBSMun | gTribCompraGov | 1-1 | Elemento | Alíquota IBS do Município utilizada | gIBSMun.pIBSMun |
| vTribIBSMun | gTribCompraGov | 1-1 | Elemento | Valor do Tributo do Município da UF Valor que seria devido ao Município, sem aplicação do Art. 473. da LC 214/20025 | gIBSCBS.vBC \* pAliqIBSMun |
| pAliqCBS | gTribCompraGov | 1-1 | Elemento | Alíquota IBS do CBS utilizada | gCBS.pCBS |
| vTribCBS | gTribCompraGov | 1-1 | Elemento | Valor do Tributo da CBS Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/20025 | gIBSCBS.vBC \* pAliqCBS |
