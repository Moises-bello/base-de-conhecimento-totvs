---
content_hash: 84659b53a6c150001af4f8421196a79ee148f694f25db847f0ef5258b927625b
fetched_at: '2026-06-29T00:12:10.775412+00:00'
page_id: '953003696'
product: rm
source: tdn-rm
title: Grupo X - Informações do Transporte da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003696
version: 5
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo X - Informações do Transporte da NF-e** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 356 | X01 | transp | Grupo Informações do Transporte | G | A01 |  | 1-1 |  |  |  |  |  |
| 357 | X02 | modFrete | Modalidade do frete | E | X01 | N | 1-1 | 1 | 0=Contratação do Frete por conta do Remetente (CIF); 1=Contratação do Frete por conta do Destinatário (FOB); 2=Contratação do Frete por conta de Terceiros; 3=Transporte Próprio por conta do Remetente; 4=Transporte Próprio por conta do Destinatário; 9=Sem Ocorrência de Transporte. | TMOV.FRETECIFOUFOB CIF = 0 FOB = 1 TERCEIROS = 2 OUTROS = 9 |  |  |
| 358 | X03 | transporta | Grupo Transportador | G | X01 | N | 0-1 |  |  |  |  | Este grupo será gerado se o nome ou CNPJ da transportadora estiverem preenchidos. |
| 359 | X04 | CNPJ | CNPJ do Transportador | CE | X03 | N | 0-1 | 14 | Preencher os zeros não significativos | TTRA.CGC |  |  |
| 360 | X05 | CPF | CPF do Transportador | CE | X03 | C | 0-1 | 11 |  |  |
| 361 | X06 | xNome | Razão Social ou nome | E | X03 | C | 0-1 | 2-60 |  | TTRA.NOME |  |  |
| 362 | X07 | IE | Inscrição Estadual do Transportador | E | X03 | C | 0-1 | 2-14 | Informar: - Inscrição Estadual do transportador contribuinte do ICMS, sem caracteres de formatação (ponto, barra, hífen, etc.); - Literal “ISENTO” para transportador isento de inscrição no cadastro de contribuintes ICMS; - Não informar a tag para não contribuinte do ICMS, A UF deve ser informada se informado uma IE. (v2.0) | TTRA.INSCRESTADUAL |  | A UF deve ser informada se informado uma IE. (v2.0). |
| 363 | X08 | xEnder | Endereço Completo | E | X03 | C | 0-1 | 1-60 |  | TTRA.RUA + TTRA.NUMERO + TTRA.COMPLEMENTO + TTRA.BAIRRO |  |  |
| 364 | X09 | xMun | Nome do município | E | X03 | C | 0-1 | 1-60 |  | GMUNICIPIO.NOMEMUNICIPIO |  |  |
| 365 | X10 | UF | Sigla da UF | E | X03 | C | 0-1 | 2 | A UF deve ser informada se informado uma IE. (v2.0). Informar "EX" para Exterior. | TTRA.CODETD |  | A UF deve ser informada se informado uma IE. (v2.0). Informar "EX" para Exterior.. |
| 366 | X11 | retTransp | Grupo Retenção ICMS transporte | G | X01 |  | 0-1 |  |  |  |  | Gerado somente se existir "Produto Tipo Frete" indicado nos parâmetros do tipo de Movimento e associado a um CFOP, e se o valor do frete for maior que zero.. |
| 367 | X12 | vServ | Valor do Serviço | E | X11 | N | 1-1 | 13v2 |  | TMOV.VALORFRETE |  |  |
| 368 | X13 | vBCRet | BC da Retenção do ICMS | E | X11 | N | 1-1 | 13v2 |  | vServ |  |  |
| 369 | X14 | pICMSRet | Alíquota da Retenção | E | X11 | N | 1-1 | 3v2-4 |  |  |  | FIXO 0 |
| 370 | X15 | vICMSRet | Valor do ICMS Retido | E | X11 | N | 1-1 | 13v2 |  |  |  | NÃO SERÁ GERADO |
| 371 | X16 | CFOP | CFOP | E | X11 | N | 1-1 | 4 | CFOP de Serviço de Transporte (Anexo XIII.03). |  |  | Código da Natureza que possui o "Produto Tipo Frete" associado. |
| 372 | X17 | cMunFG | Código do município de ocorrência do fato gerador do ICMS do transporte | E | X11 | N | 1-1 | 7 | Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País) . | DCODIFICACAOMUNICIPIO.CODIGO |  |  |
| 372.1 | X17.1 | -x- | Sequência XML | CG | X01 |  | 0-1 |  | Transporte por Veículo, Vagão ou Balsa. |  |  |  |
| 373 | X18 | veicTransp | Grupo Veículo Transporte | G | X17.1 |  | 1-1 |  | Informar o veículo trator (v2.0) |  |  | Será gerado somente se a placa do veiculo estiver preenchida. |
| 374 | X19 | placa | Placa do Veículo | E | X18 | C | 1-1 | 7 | Informar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999. Informar a placa em informações complementares quando a placa do veículo tiver lei de formação diversa. (NT 2011/005) . | TMOV.PLACA |  |  |
| 375 | X20 | UF | Sigla da UF | E | X18 | C | 0-1 | 2 | Informar "EX" se Exterior. | TMOV.CODETDPLACA |  |  |
| 376 | X21 | RNTC | Registro Nacional de Transportador de Carga (ANTT) | E | X18 | C | 0-1 | 1-20 |  | Se existir Veículo cadastrado com mesma Placa e UF, preenche com o campo RNTC (TVEICULOS.RNTC). |  |  |
| 377 | X22 | reboque | Grupo Reboque | G | X17.1 |  | 0-5 |  | Informar os reboques/Dolly (v2.0) |  |  |  |
| 378 | X23 | placa | Placa do Veículo | E | X22 | C | 1-1 | 7 | Informar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999. Informar a placa em informações complementares quando a placa do veículo tiver lei de formação diversa. (NT 2011/005) | TMOV.PLACA |  |  |
| 379 | X24 | UF | Sigla da UF | E | X22 | C | 1-1 | 2 | Informar "EX" se Exterior. | TMOV.CODETDPLACA |  |  |
| 380 | X25 | RNTC | Registro Nacional de Transportador de Carga (ANTT) | E | X22 | C | 0-1 | 1-20 |  | Se existir Veículo cadastrado com mesma Placa e UF, preenche com o campo RNTC (TVEICULOS.RNTC) |  |  |
| 380a | X25a | vagao | Identificação do vagão | CE | X01 | C | 0-1 | 1-20 | (v2.0) |  |  | NÃO SERÁ GERADO |
| 380b | X25b | balsa | Identificação da balsa | CE | X01 | C | 0-1 | 1-20 | (v2.0) |  |  | NÃO SERÁ GERADO |
| 381 | X26 | vol | Grupo Volumes | G | X01 |  | 0-5000 |  | (NT 2012/003) |  |  |  |
| 382 | X27 | qVol | Quantidade de volumes transportados | E | X26 | N | 0-1 | 1-15 |  | TMOV.QUANTIDADE |  |  |
| 383 | X28 | esp | Espécie dos volumes transportados | E | X26 | C | 0-1 | 1-60 |  | TMOV.ESPECIE |  |  |
| 384 | X29 | marca | Marca dos volumes transportados | E | X26 | C | 0-1 | 1-60 |  | TMOV.MARCA |  |  |
| 385 | X30 | nVol | Numeração dos volumes transportados | E | X26 | C | 0-1 | 1-60 |  | TMOV.NUMERO |  |  |
| 386 | X31 | pesoL | Peso Líquido (em kg) | E | X26 | N | 0-1 | 12v3 |  | TMOV.PESOLIQUIDO |  |  |
| 387 | X32 | pesoB | Peso Bruto (em kg) | E | X26 | N | 0-1 | 12v3 |  | TMOV.PESOBRUTO |  |  |
| 387a | X33 | lacres | Grupo Lacres | G | X26 |  | 0-5000 |  | (NT 2012/003) |  |  | NÃO SERÁ GERADO |
| 388 | X34 | nLacre | Número dos Lacres | E | X33 | C | 1-1 | 1-60 |  |  |  | NÃO SERÁ GERADO |
