---
content_hash: 8883ebdbd3e0572e14bf515b537e8c8af87182558eb05bb5e0cd62b41c871cf4
fetched_at: '2026-06-29T00:12:10.819065+00:00'
page_id: '953003737'
product: rm
source: tdn-rm
title: Grupo ZA - Informações de Comércio Exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003737
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo ZA - Informações de Comércio Exterior** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 402 | ZA01 | exporta | Grupo Exportação | G | A01 |  | 0-1 |  | Informar apenas na exportação. |  |  |  |
| 403 | ZA02 | UFSaidaPais | Sigla da UF de Embarque ou de transposição de fronteira | E | ZA01 | C | 1-1 | 2 | Não aceita o valor "EX". | TMOVFISCAL.UFDESEMBARACO | UF do Desembaraço/Embarque | Aba Informações do movimento, na pasta Exportação. |
| 404 | ZA03 | xLocExporta | Descrição do Local de Embarque ou de transposição de fronteira | E | ZA01 | C | 1-1 | 1-60 |  | TMOVFISCAL.LOCALDESEMBARACO | Local de Desembaraço/Embarque | Aba Informações do movimento, na pasta Exportação. |
| 404a | ZA04 | xLocDespacho | Descrição do local de despacho | E | ZA01 | C | 0-1 | 1-60 | Informação do Recinto Alfandegado |  | Campo Complementar LOCDESPACHO do cadastro do Cliente/Fornecedor. | Criar campo complementar no cadastro do Cliente /Fornecedor selecionado no Local de Entrega , aba Transporte, pasta Coleta e Entrega do movimento. O campo complementar deverá ser criado com as seguintes informações:  **Nome da Coluna**: LOCDESPACHO  **Descrição**: Local de Despacho  **Tamanho**: 60  **Tipo**: Alfanumérico  **Tipo de Texto**: Texto  ***Observações:***  Marcar a opção "Habilita NF 2018.05" disponível nos Dados Fiscais do cadastro da Filial, pasta Dados Adicionais;  Habilitar a edição de dados de Coleta/Entrega, campo "Utilizar Endereço de Coleta e Entrega como Destinatário" através dos parâmetros do Tipo de Movimento, etapa Mov - Transportes 2/3;  Tag será gerada apenas para movimentos de venda (Tipo de Movimento **2.X.XX**). |
