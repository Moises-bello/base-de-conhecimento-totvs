---
content_hash: 44073ae3b2bb1a171152b0c01607fd91161502f41af59619733e86582730ed0d
fetched_at: '2026-06-29T00:12:02.297953+00:00'
page_id: '900452469'
product: rm
source: tdn-rm
title: Identificação da NFCom
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900452469
version: 25
---

# ide- Identificação da NFCom

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **ide** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **1-1** | **Grupo** | **Identificação da NFCom** |
| cUF | ide | 1-1 | Elemento | Código da UF da Filial Emitente |
| tpAmb | ide | 1-1 | Elemento | Tipo de ambiente definido nos parâmetros da NFCom  1 - Produção; 2 - Homologação |
| mod | ide | 1-1 | Elemento | Modelo de Documento da NFCom (62) |
| serie | ide | 1-1 | Elemento | Série definida no Movimento da NFCom |
| nNF | ide | 1-1 | Elemento | Número do Movimento da NFCom |
| cNF | ide | 1-1 | Elemento | Código gerado de forma aleatória no momento de geração da NFCom. Depois de gerado este código não será alterado |
| cDV | ide | 1-1 | Elemento | Ultimo digito da chave de acesso |
| dhEmi | ide | 1-1 | Elemento | Data de emissão e hora de Emissão do Movimento da NFCom |
| tpEmis | ide | 1-1 | Elemento | Modalidade de Operação definida para o Documento  1 - Normal 2 - Contingência |
| nSiteAutoriz | ide | 1-1 | Elemento | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial | Edite a filial Emitente da NFCom | Ambiente NFCom | Número do Site Autorizador |
| cMunFG | ide | 1-1 | Elemento | Classificação IBGE do município de incidência definido no Movimento.  Aba: Integrações | Fiscal | Município do movimento da NFCom. |
| finNFCom | ide | 1-1 | Elemento | **Se** Campo IDMOVRELAC estiver preenchido  Aba: Identificação | Cabeçalho do movimento da NFCom  **Então** 3 - NFCom de Substituição;  **Se** A CFOP for definida como Ajuste  Aba: Outros Dados | Tipo de Operação = Natureza de Ajuste.  Na natureza de operação (CFOP) informada no movimento de NFCom  **Então** 4 - NFCom ajuste de débito;  **Senão** 0 - NFCom Normal; |
| tpFat | ide | 1-1 | Elemento | Fixo 0- Faturamento Normal; |
| verProc | ide | 1-1 | Elemento | Versão do RM |
| indPrePago | ide | 0-1 | Elemento | Não será gerado |
| indCessaoMeiosRede | ide | 0-1 | Elemento | Não será gerado |
| **--- x — Sequência opcional do XML: Será gerado somente para notas em contingência** | | | | |
| dhCont | ide | 1-1 | Elemento da Sequencia | **Gerar com a mesma regra da NF-e  Implementação futura** |
| xJust | ide | 1-1 | Elemento da Sequencia | **Gerar com a mesma regra da NF-e**  **Implementação futura** |
| **Fim da sequência opcional do XML — x ---** | | | | |
| **gCompraGov** | **ide** | **0-1** | **Grupo** | O **grupo é gerado** nos seguintes cenários:   * + O campo **Órgão Público** no cadastro de Cliente/Fornecedor estiver diferente de **“Não se aplica”**; |

Exemploxml    
42
2
62
1
55656
3944137
4
2025-09-11T11:04:52-03:00
1
9
3304557
3
0
12.1.2510.1

2
0.1000
3
31230922635197000178551000005214641102230473
31230922635197000178551000005214641102230999
  
]]>
