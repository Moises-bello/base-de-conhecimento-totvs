---
content_hash: af809921eb70c9d92cd36a3b6e761fe9b4c2e1aff8483fb85e1d3ef88ae0c6d2
fetched_at: '2026-06-29T00:11:02.475999+00:00'
page_id: '618482603'
product: rm
source: tdn-rm
title: Mapeamento Campos - MDF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapeamento+Campos+-+MDF-e
version: 1
---

## Origem dos dados

Abaixo seguem as estruturas e o mapeamento das origens campo a campo.

falseinfoCadastroleft0ide

## Informações de Identificação do MDF-e

xmlide
43
2
1
1
1
4
1
2017-01-17T09:32:00
-02:00
1
RS
SC
2020-05-13T14:49:00
{...}
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| cUF | Código da UF |  |  |
| tpAmb | Tipo do Ambiente |  | 1 - Produção 2 - Homologação |
| tpEmit | Tipo do Emitente |  | 1 – Prestador de serviço de transporte 2 – Transportador de carga própria 3 - Prestador de serviço de transporte que emitirá CT-e Globalizado |
| tpTransp | Tipo do Transportador |  | 1 - ETC 2 - TAC 3 – CTC |
| serie | Série do Documento Fiscal |  |  |
| nMDF | Número do Documento Fiscal |  |  |
| modal | Código da modalidade de transporte |  | 1 - Rodoviário 2 - Aéreo 3 - Aquaviário 4 - Ferroviário |
| dhEmi | Data de emissão do Documento Fiscal |  |  |
| fusoHorario | Fuso horário da emissão |  |  |
| tpEmis | Forma de emissão |  | 1 - Normal 2 - Contingência |
| UFIni | Sigla da UF de Carregamento |  |  |
| UFFim | Sigla da UF de Descarregamento |  |  |
| dhIniViagem | Data e Hora de Início da Viagem |  |  |
| indCanalVerde | Informação de prestação de serviço participante do projeto Canal Verde |  |  |
| indCarregaPosterior | Indicador de MDF-e com inclusão de Carga posterior a emissão |  |  |

1 MunicipiosCarreg

## Municípios de Carregamento

Gerar um registro para cada ........

xmlMunicipiosCarregItem
4321808
TRES DE MAIO
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| cMunCarreg | Código do município |  |  |
| xMunCarreg | Nome do município |  |  |

2emit

## Identificação do Emitente do MDF-e

xmlemit
99458836000120
Empresa Emissora
4510210101

Rua das Pedras
900
Centro
4321808
TRES DE MAIO
98910000
RS
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CNPJ\_emit | CNPJ do emitente |  |  |
| CPF\_emit | CPF do emitente |  |  |
| xNome | Razão Social ou Nome do emitente |  |  |
| xFant | Nome fantasia |  |  |
| IE | Inscrição Estadual |  |  |
| enderEmit | Grupo do endereço do emitente |  |  |
| xLgr | Logradouro |  |  |
| nro | Número |  |  |
| xCpl | Complemento |  |  |
| xBairro | Bairro |  |  |
| cMun | Código do município |  |  |
| xMun | Nome do município |  |  |
| CEP | Código do CEP |  |  |
| UF | Sigla da UF |  |  |
| fone | Telefone |  |  |
| email | E-mail do Emitente |  |  |

4Modal Rodoviário

## Modal Rodoviário

xml Rodoviario
UIASDHI332
{...}
{...}
{...}
{...}
{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| codAgPorto | Código de Agendamento no Porto |  |  |

5 infCIOT

## Informações do Código Identificador da Operação de Transporte

Gerar um registro para cada ........

xml infCIOTItem
123456789611
12045632101
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CIOT | Código  Identificador  da  Operação  de Transporte |  |  |
| CPF\_CIOT | CPF do responsável pela geração do CIOT |  |  |
| CNPJ\_CIOT | CNPJ do responsável pela geração do CIOT |  |  |

6Contratante

## Informações do Contratante

Gerar um registro para cada ........

xmlContratanteItem
10521032564
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CPF\_Contr | CPF do contratante do serviço |  |  |
| CNPJ\_Contr | CNPJ do contratante do serviço |  |  |
| IdEstrangeiro\_Contr | Identificador do contratante do serviço em caso de contratante estrangeiro |  |  |
| Nome\_Contr | Razão social ou Nome do contratante do serviço |  |  |

7InfPagamento

## Informações do Pagamento do Frete

Gerar um registro para cada ........

xmlInfPagamentoItem
José da Silva
10521032564
10000
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| nome\_respPag | Nome do responsável pelo pagamento |  |  |
| CPF\_respPag | Número do CPF do responsável pelo pagamento |  |  |
| CNPJ\_respPag | Número do CNPJ do responsável pelo pagamento |  |  |
| idEstrangeiro\_respPag | Identificador do responsável pelo pagamento em caso de ser estrangeiro |  |  |
| valor\_Contrato | Valor total do contrato |  |  |
| indAltoDesemp | Indicador de operação de transporte de alto desempenho |  |  |
| indPag | Indicador da forma de pagamento |  | 0 - Pagamento à vista 1 - Pagamento à prazo |

8Componentes

## Componentes do pagamento do frete

Gerar um registro para cada ........

xmlComponentesItem
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| tipo\_comp | Tipo do componente |  | 01 - Vale pedágio 02 - Impostos, taxas e contribuições 03 - Despesas (bancárias, meios de pagamentos, outras) 99 - Outros |
| valor\_comp | Valor do componente |  |  |
| desc\_comp | Descrição do componente |  |  |

9InfPrazo

## Informações do pagamento a prazo

Gerar um registro para cada ........

xmlInfPrazoItem
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| numeroParcela | Número da parcela |  |  |
| dataVencimento | Data de vencimento da parcela |  |  |
| valorParcela | Valor da parcela |  |  |

10InfBanco

## Informações bancárias

Gerar um registro para cada ........

xmlInfBanco
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| codBanco | Número do banco |  |  |
| codAgencia | Número da Agência |  |  |
| CNPJIPEF | Número do CNPJ da Instituição de pagamento Eletrônico do Frete |  |  |
| PIX | Chave PIX |  | Novo |

11 VeicTracao

## Informações da tração do veículo

xmlVeicTracao
001
MBA1478
13000
666
333
01
02
RS

{...}
{...}
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| codigo\_veiculo | Código interno |  |  |
| placa | Placa do veículo |  |  |
| tara | Tara |  |  |
| capacidadeKG | Capacidade de carga |  |  |
| capacidadeM3 | Capacidade de carga |  |  |
| tipoRodado | Tipo de rodado |  | 01 - Truck 02 - Toco 03 - Cavalo Mecânico 04 - VAN 05 - Utilitário 06 - Outros |
| tipoCarroceria | Tipo de carroceria |  | 00 - Não aplicável 01 - Aberta 02 - Fechada/Baú 03 - Graneleira 04 - Porta Conteiner 05 - Sider |
| UF\_veiculo | Sigla da UF |  |  |
| RENAVAM | RENAVAM do Veículo |  |  |

12Proprietario

## Informações da tração do veículo

xmlProprietario
12345678912
12345772
Julio
123456
RS
2
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CPF\_prop | CPF do proprietário |  |  |
| CNPJ\_prop | CNPJ do proprietário |  |  |
| RNTRC\_prop | Registro  Nacional  dos  Transportadores Rodoviários de Carga |  |  |
| nome\_prop | Razão Social ou nome |  |  |
| IE\_prop | Incrição Estadual |  |  |
| UF\_prop | Sigla da UF |  |  |
| tipo\_prop | Tipo do proprietário ou possuidor |  | 0 - TAC -Agregado 1 - TAC Independente 2 - Outros |

14Condutores

## Informações da tração do veículo

Gerar um registro para cada ........

xmlCondutoresItem
Maria
12045612345

Pedro
45612378945
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| nome\_cond | Nome do condutor |  |  |
| CPF\_cond | CPF do condutor |  |  |

15 VeicReboque

## Informações quando há reboques no veículo

Gerar um registro para cada ........

xmlVeicReboqueItem

0027
GQS1686
254
652
255
01
RS

{...}
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| codigo\_veiculo | Código interno |  |  |
| placa | Placa do veículo |  |  |
| tara | Tara |  |  |
| capacidadeKG | Capacidade de carga |  |  |
| capacidadeM3 | Capacidade de carga |  |  |
| tipoRodado | Tipo de rodado |  | 01 - Truck 02 - Toco 03 - Cavalo Mecânico 04 - VAN 05 - Utilitário 06 - Outros |
| tipoCarroceria | Tipo de carroceria |  | 00 - Não aplicável 01 - Aberta 02 - Fechada/Baú 03 - Graneleira 04 - Porta Conteiner 05 - Sider |
| UF\_veiculo | Sigla da UF |  |  |
| RENAVAM | RENAVAM do Veículo |  |  |

16Proprietario\_reb

## Informações do proprietário ou possuidor do reboque

xmlVeicReboqueItem
12345678956
12345678
Laura
12345678
SC
1
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CPF\_prop\_reb | CPF do proprietário |  |  |
| CNPJ\_prop\_reb | CNPJ do proprietário |  |  |
| RNTRC\_reb | Registro  Nacional  de  Transportadores Rodoviários de Carga |  |  |
| nome\_prop\_reb | Razão Social ou nome |  |  |
| IE\_prop\_reb | Incrição Estadual |  |  |
| UF\_prop\_reb | Sigla da UF |  |  |
| tipo\_prop\_reb | Tipo do proprietário ou possuidor |  |  |

17ValePedagio

## Informações dos vales-pedágio

Gerar um registro para cada ........

xmlValePedagioItem
12312312123312
13123213213123
5544
66.80
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| CNPJForn | CNPJ |  |  |
| CNPJPagamento | CNPJ |  |  |
| numeroCompra | Número do comprovante |  |  |
| vValePed | Valor do vale pedágio |  |  |
| tpValePed | Tipo do Vale Pedágio |  | 01 - TAG; 02 - Cupom; 03 - Cartão |
| categCombVeic | Categoria de Combinação Veicular |  | 02 - Veículo Comercial 2 eixos; 04 - Veículo Comercial 3 eixos; 06 - Veículo Comercial 4 eixos; 07 - Veículo Comercial 5 eixos; 08 - Veículo Comercial 6 eixos; 10 - Veículo Comercial 7 eixos; 11 - Veículo Comercial 8 eixos; 12 - Veículo Comercial 9 eixos; 13 - Veículo Comercial 10 eixos; 14 - Veículo Comercial Acima de 10 eixos; |

18LacresRodo

## Informações dos vales-pedágio

Gerar um registro para cada ........

xmlLacresRodoItem
1234567891234562871
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| nLacreRodo | Número do lacre |  |  |

19LacresRodo

## Informações dos vales-pedágio

Gerar um registro para cada ........

xmlLacresRodoItem
1234567891234562871
]]>

### Origem de dados

| Elemento do XML | Descrição | Origem | Observações |
| --- | --- | --- | --- |
| nLacreRodo | Número do lacre |  |  |

As demais estruturas não destacadas irão seguir o padrão geral dos eventos
