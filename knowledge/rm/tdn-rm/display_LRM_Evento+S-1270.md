---
content_hash: a157bfd4bf765f2c1f2c169215a23050ccfd16b92a6120b91d00b79d905f17b4
fetched_at: '2026-06-29T00:09:02.240209+00:00'
page_id: '379299566'
product: rm
source: tdn-rm
title: Evento S-1270
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1270
version: 8
---

LayoutLeiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do Calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| remunAvNP | tpInsc |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   Caso FCFOCEI.CEI esteja preenchido retorna "4 - CNO (Cadastro Nacional de Obra)";  Caso FCFO.CGCCFO esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica   de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| remunAvNP | nrInsc |  |  | Caso tpInsc seja 1: se o parâmetro "Utiliza tomadores de serviço"    estiver marcado retorna valor do campo FCFO.CGCCFO.   Caso contrário retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso tpInsc seja 4: retorna FCFOCEI.CEI. |
| remunAvNP | codLotacao | PESOCIALAVULSOSNAOPORT | CodLotacao |  |
| remunAvNP | vrBcCp00 | PESOCIALAVULSOSNAOPORT | VrBcCp00 |  |
| remunAvNP | vrBcCp15 | PESOCIALAVULSOSNAOPORT | VrBcCp15 |  |
| remunAvNP | vrBcCp20 | PESOCIALAVULSOSNAOPORT | VrBcCp20 |  |
| remunAvNP | vrBcCp25 | PESOCIALAVULSOSNAOPORT | VrBcCp25 |  |
| remunAvNP | vrBcCp13 | PESOCIALAVULSOSNAOPORT | VrBcCp13 |  |
| remunAvNP | vrBcFgts | PESOCIALAVULSOSNAOPORT | VrBcFgts |  |
| remunAvNP | vrDescCP | PESOCIALAVULSOSNAOPORT | VrDescCP |  |

Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do Calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| remunAvNP | tpInsc |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   Caso FCFOCEI.CEI esteja preenchido retorna "4 - CNO (Cadastro Nacional de Obra)";  Caso FCFO.CGCCFO esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica   de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| remunAvNP | nrInsc |  |  | Caso tpInsc seja 1: se o parâmetro "Utiliza tomadores de serviço"    estiver marcado retorna valor do campo FCFO.CGCCFO.   Caso contrário retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso tpInsc seja 4: retorna FCFOCEI.CEI. |
| remunAvNP | codLotacao | PESOCIALAVULSOSNAOPORT | CodLotacao |  |
| remunAvNP | vrBcCp00 | PESOCIALAVULSOSNAOPORT | VrBcCp00 |  |
| remunAvNP | vrBcCp15 | PESOCIALAVULSOSNAOPORT | VrBcCp15 |  |
| remunAvNP | vrBcCp20 | PESOCIALAVULSOSNAOPORT | VrBcCp20 |  |
| remunAvNP | vrBcCp25 | PESOCIALAVULSOSNAOPORT | VrBcCp25 |  |
| remunAvNP | vrBcCp13 | PESOCIALAVULSOSNAOPORT | VrBcCp13 |  |
| remunAvNP | vrBcFgts | PESOCIALAVULSOSNAOPORT | VrBcFgts |  |
| remunAvNP | vrDescCP | PESOCIALAVULSOSNAOPORT | VrDescCP |  |
