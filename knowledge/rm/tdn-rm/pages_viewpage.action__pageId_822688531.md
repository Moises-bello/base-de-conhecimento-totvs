---
content_hash: 0bc4de047ad5eecaf6d1e366cdf82836ef358f5b404cb9fc7a69821d96b2d077
fetched_at: '2026-06-29T00:11:46.527104+00:00'
page_id: '822688531'
product: rm
source: tdn-rm
title: valores/vDedRed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688531
version: 30
---

A geração destes grupos é de escolha com 3 opções para informação de Dedução/Redução, caso exista, são:

1. **`pDR`**: Grupo de Percentual.
2. **`vDR`**: Grupo de Valor.
3. **`documentos`** : Grupo de Documento.

A opção foi pela geração do Grupo de Valor, os outros grupos não serão gerados.

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| vDedRed | NFSe/infNFSe/DPS/infDPS/valores/ | Não | grupo | Grupo de informações relativas ao valores para dedução/redução do valor da base de cálculo (valor do serviço) |
| pDR | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/ | Não | Valor percentual padrão para dedução/redução do valor do serviço. | Tag gerada quando parâmetro: Dedução = Usa Ambos ou Usa percentual no item de movimento (Item - Valores Financeiros 2/2) e campo preenchido no item de movimento.  campo disponível em: item de movimento - tributos e valores - valores: percentual deduzido. (TITMMOV.PERCENTUALDEDUCAO) |
| vDR | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/ | Não | Valor monetário padrão para dedução/redução do valor do serviço. | Tag gerada com a Soma do Valor de Dedução do ISS e Valor de Materiais, campos disponíveis no Movimento – Pasta Dados Fiscais (TMOVFISCAL.VLRDEDUCAOOUTRO + TMOVFISCAL.VLRDEDUCAOMATERIAL) |
| **documentos** | **NFSe/infNFSe/DPS/infDPS/valores/vDedRed/** |  | **Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço** | **Não é Gerado** |
| **docDedRed** | **NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos** |  | **Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço** | **Não é Gerado** |
| Expandir Layout docDedRed  | Nome | Pai | Obrigatório | Origem | Descrição | | --- | --- | --- | --- | --- | | chNFSe | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Chave de acesso da NFS-e (padrão nacional). | Não é Gerado | | chNFe | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Chave de acesso da NF-e. | Não é Gerado | | **NFSeMun** | **NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/** |  | **Grupo de informações para outras notas eletrônicas municipais** **(Nota eletrônica municipal emitida fora do padrão nacional)** | **Não é Gerado** | | Expandir Layout NFSeMun  | Nome | Pai | Obrigatório | Origem | Descrição | | --- | --- | --- | --- | --- | | cMunNFSeMun | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFSeMun/ |  | Código Município emissor da nota eletrônica municipal. (Tabela do IBGE) | Não é Gerado | | nNFSeMun | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFSeMun/ |  | Número da nota eletrônica municipal. | Não é Gerado | | cVerifNFSeMun | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFSeMun/ |  | Código de Verificação da nota eletrônica municipal. |  | | | | | | | NFNFS | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Grupo de informações de NF ou NFS (Modelo não eletrônico) | **Não Gerado** | | Expandir Layout NFNFS  | Nome | Pai | Obrigatório | Origem | Descrição | | --- | --- | --- | --- | --- | | nNFS | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFNFS/ |  | Número da Nota Fiscal NF ou NFS. | Não é Gerado | | modNFS | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFNFS/ |  | Modelo da Nota Fiscal NF ou NFS. | Não é Gerado | | serieNFS | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/NFNFS/ |  | Série Nota Fiscal NF ou NFS. | Não é Gerado | | | | | | | nDocFisc | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Identificador de documento fiscal diferente dos demais do grupo. | Não é Gerado | | nDoc | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Identificador de documento não fiscal diferente dos demais do grupo. | Não é Gerado | | tpDedRed | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Tipo da Dedução/Redução:  01 – Alimentação e bebidas/frigobar; 02 – Materiais; 03 – Produção externa; 04 – Reembolso de despesas; 05 – Repasse consorciado; 06 – Repasse plano de saúde; 07 – Serviços; 08 – Subempreitada de mão de obra; 99 – Outras deduções; | Não é Gerado | | xDescOutDed | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Descrição da Dedução/Redução quando a opção é "99 – Outras Deduções". | Não é Gerado | | dtEmiDoc | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Data da emissão do documento dedutível. Ano, mês e dia (AAAA-MM-DD) | Não é Gerado | | vDedutivelRedutivel | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Valor monetário total dedutível/redutível no documento informado (R$). Este é o valor total no documento informado que é passível de dedução/redução. | Não é Gerado | | vDeducaoReducao | NFSe/infNFSe/DPS/infDPS/valores/vDedRed/documentos/docDedRed/ |  | Valor monetário utilizado para dedução/redução do valor do serviço da NFS-e que está sendo emitida (R$). Deve ser menor ou igual ao valor deduzível/redutível (vDedutivelRedutivel). | Não é Gerado | | | | | |
