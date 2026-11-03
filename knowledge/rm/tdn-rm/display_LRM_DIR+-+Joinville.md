---
content_hash: 315fc75981a4f4ee5127fe51af027e178cd7a14355c2e32d7a07f1d9d358c29a
fetched_at: '2026-06-29T00:11:56.574418+00:00'
page_id: '867145609'
product: rm
source: tdn-rm
title: DIR - Joinville
type: documentation
url: https://tdn.totvs.com/display/LRM/DIR+-+Joinville
version: 30
---

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

A DIR (Declaração de Impostos Retidos de Joinville) é uma ferramenta destinada a efetivar a retenção na fonte do ISSQN nas hipóteses em que não haja a efetiva geração da Nota Fiscal.

Conforme Nota Explicativa disponível no portal da [NFem de Joinville](https://nfem.joinville.sc.gov.br/area_conteudo.aspx?id=6), "[...] as pessoas jurídicas responsáveis pela retenção na fonte do Imposto Sobre Serviços de Qualquer Natureza (ISSQN), na forma do artigo 10, 11 e 12 da Lei Complementar Municipal n. 155/2003, com redação dada pela Lei Complementar n. 169/2004, que receberem notas fiscais das empresas sujeitas as prerrogativas do art. **80 do Decreto Municipal n. 15.007/2008**, deverão efetuar a DECLARAÇÃO DE IMPOSTO RETIDO (DIR), para efeito do recolhimento do imposto retido."

# 2. Geração do Arquivo XML

A geração da DIR Joinville é executada a partir do menu *Obrigações Acessórias | Rotinas Fiscais | Municipais*. Na tela de geração da rotina, informe os seguintes dados:

* Código da Filial
* Data de Emissão Inicial e Data de Emissão Final;

***Observação***: O arquivo será gerado em formato XML para depois deverá ser importado no site da Prefeitura.

# 3. Mapeamento de campos do xml

O arquivo xml será gerado com base em Lançamentos Fiscais de Entrada que sejam referente a prestação de serviço.

xmlExemplo de Arquivo

1.0
40
2

20000000002000
TOTVS

000002
1
2024-10-14

10000000000001
Teste2
Belo Horizonte
    MG
1
144.00
144.00
1.80
2.88
2.00

000000
1
2024-10-14

00000000000000
Teste
Itaperuçu
PR
1
144.00
144.00
1.80
2.88
2.00
]]>

Os campos do xml serão gerados conforme abaixo.

DIRJoinvilleDeclaraçãodeImpostosRetidos-gruposxmllotelote

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Quantidade** | **Tamanho** | **Tabela Campo** | **Observações** |
| versao | CPF ou CNPJ do prestador de serviço | 1 | 14 | GFILIAL.CGCCFO | Valor fixo: 1.0 |
| numero | Identificador único do lote | 1 |  |  | Deverá ser um número diferente para cada lote enviado. |
| tipo | Tipo do lote. | 1 |  |  | Valor fixo: 2 |
|  | Grupo de informações do Tomador | 1 |  |  |  |
|  | Grupo de informações da DIR | 999 |  |  |  |

tomadorTomador

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Quantidade** | **Tamanho** | **Tabela Campo** | **Observações** |
| documento | CPF ou CNPJ do prestador de serviço | 1 | 14 | GFILIAL.CGCCFO |  |
| razao\_social | Razão Social da Filial | 1 | 60 | GFILIAL.NOME |  |

truedirDir

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Quantidade** | **Tamanho** | **Tabela Campo** | **Observações** |
| numero | Identificador único da DIR | 1 | 6 | DLAF.DOCINI | Valor máximo: 999999 |
| serie | Série da DIR. | 1 | 5 | DLAF.SERIE |  |
| data\_emissao | Data de emissão da DIR. | 1 |  | DLAF.DATAEMISSAO |  |
|  | Grupo de informações do Prestador | 1 |  |  |  |
| valor\_total | Valor total do serviço em Reais. | 1 |  | DLAFAGRUP.VALORCONT | Formato: 12345.67 |
| valor\_base\_calculo | Valor da base de cálculo do ISSQN em Reais. | 1 |  | DTRBITEM.BASETRB | Formato: 12345.67 |
| servico | Subitem da lista de serviços anexa à Lei Complementar 155/2003 | 1 | 5 | DITEM.CODIGOSERVICO |  |
| codigo\_cei | Matrícula CEI (Cadastro Específico do INSS) | 0-1 |  |  | Não é gerado |
| valor\_iss | Valor do ISSQN em Reais | 1 |  | DTRBITEM.VALORTRB | Formato: 12345.67 |
| aliquota\_iss | Aliquota do serviço prestado em percentual | 1 |  | DTRBITEM.ALIQTRB | Formato: 12.34 |

prestadorPrestador

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo XML** | **Descrição** | **Quantidade** | **Tamanho** | **Tabela Campo** | **Observações** |
| documento | CNPJ do prestador | 1 | 14 | FCFO.CGCCFO |  |
| nome | Nome do prestador | 1 | 60 | FCFO.NOME |  |
| cidade | Nome do município do prestador | 0-1 | 60 | GMUNICIPIO.NOMEMUNICIPIO | Seleciona o nome conforme município preenchido no cadastro do Cli/For |
| estado | Sigla do estado do prestador | 0-1 | 2 | FCFO.CODETD |  |
| internacional | Nacionalidade do prestador | 0-1 | 1 | GETD.NACIONAL | Preenche com valor **inverso** ao cadastrado no estado, ou seja:  SE GETD.NACIONAL = 0, ENTÃO internacional = 1 SENÃO SE GETD.NACIONAL = 1, ENTÃO internacional = 0 |
| simples\_nacional | Se prestador é optante pelo Simples Nacional | 0-1 | 1 | FCFO.OPTANTEPELOSIMPLES |  |

# 4. Validação de Schema

Ao executar a rotina de geração da DIR, o sistema realiza uma validação automática do arquivo XML, utilizando o modelo de Schema XSD exigido pela Prefeitura de Joinville. Esse processo tem como objetivo antecipar e sinalizar possíveis erros estruturais ou de dados que possam impedir o aceite do arquivo pelo sistema da prefeitura.

Caso sejam detectados erros na geração do arquivo xml, a mensagem descreverá a causa para facilitar a correção antes do envio ao portal municipal.

textExemplo de log com erros de validação

Neste caso o campo obrigatório "documento" não está preenchido e os campos "valor\_total" e "serviço" estão com valores inválidos.

**Observação:** Mesmo com os erros na validação o arquivo é gerado normalmente.
