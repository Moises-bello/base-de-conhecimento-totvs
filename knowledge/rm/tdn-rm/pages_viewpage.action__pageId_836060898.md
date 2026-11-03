---
content_hash: 1a0d7a729213d11bbe8d3fb80c47e9e89a7aa40bc1a2517b2b898b9bb176e4c7
fetched_at: '2026-06-29T00:11:49.642346+00:00'
page_id: '836060898'
product: rm
source: tdn-rm
title: Nf-e Geração de movimento por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=836060898
version: 5
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar a geração de movimento por competência via WebService para os contratos . Os movimentos gerados poderão ser consultados no módulo TOTVS Gestão de Estoque, Compras e Faturamento.

Através do processServer "***EduNFECompetenciaSliceableData***" é possível, por meio do método **ExecuteWithXmlParams**, realizar a geração do movimento por competência.

**[Se necessário clique aqui para obter ajuda na configuração do Host](http://tdn.totvs.com/display/LRM/Webservices) ou****[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)**

**Método ExecuteWithXmlParams**

Este é o método publicado no WebService (wsProcess) para que seja consumido o serviço de geração do movimento por competência (*EduNFECompetenciaSliceableData -> a partir da versão **12.1.2406***)

Até a versão **12.1.2402** este é o método publicado no WebService (wsProcess) para que seja consumido o serviço de geração do movimento por competência (EduNFECompetenciaData)

#### **Utilização do WebService**

Para realizar  a geração de movimento por competência , deve ser utilizado a operação de ExecuteWithXmlParams.

Deve ser passado um XML contendo as informações para execução do processo e os campos do contexto de execução com os valores como se o usuário estivesse logado no sistema (os campos destacados são obrigatórios para processos que serão executado no contexto do TOTVS Educacional).

* O preenchimento dos campos abaixo deve ser realizado na TAG "**Context**" e "**CodUsuario**"

Campos obrigatórios: $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA, $CODUSUARIO

Acessar XML no RM

**Dica:**

Para conhecer melhor o XML e suas informações é possível acessar no RM o XML de processos que foram executados.

Por exemplo, podemos executar o processo de geração de movimento em um base de dados de homologação e observar no XML gerado as informações preenchidas.

Para isso acesse o menu “Executar” digite “XML” e clique em “XML de parâmetros de JOB”  na tela apresentada crie um filtro para que seja carregados os JOB do processo em questão.

### Exemplo do XML completo pronto para ser consumido via o WebService responsável em executar o processo de geração de movimento por competência.

xmlGeração do movimento




EduNFECompetenciaSliceableData



S
EduNFECompetenciaAction
true
false
false
mestre





$EXERCICIOFISCAL
22

$CODLOCPRT
-1

$CODTIPOCURSO
1

$EDUTIPOUSR
-1

$CODUNIDADEBIB
-1

$CODCOLIGADA
1

$RHTIPOUSR
-1

$CODIGOEXTERNO
-1

$CODSISTEMA
S

$CODUSUARIOSERVICO


$CODUSUARIO
mestre

$IDPRJ
-1

$CHAPAFUNCIONARIO
-1

$CODFILIAL
1
DotNet

false

2a136ce1-29ad-455a-9726-90aae610440b
Falha na execução do processo

false
BHN050104412
true
10.31.6.129
false


1
108837
false
BHN050104412
EduContratoAction
1000
1
wesley.costa
false

false
false


1
PACMEN-000491
72
1128

CODCOLIGADA
RA
IDPERLET
CODCONTRATO
SCONTRATO
Gerar Movimento por competência
1
true
false
2024-04-03T11:39:12.0477894-03:00
JobMonitor
false
EduNFECompetenciaSliceableData

RM.Edu.Interfaces.Financeiro.IEduNFECompetenciaData
4
RM.Edu.Interfaces.Intf, Version=12.1.2406.1, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false
false
false


0
1
1
1


true
2022-01-31T00:00:00



false
false
false





false

b8565991-276a-4c93-93b8-2c96237d269c
Falha na execução do processo

false

false

false


-1
-1
false


1000
1

false

false
false




0
true
false
2024-04-03T11:39:12.0477894-03:00
JobMonitor
false


false
true

Processo executado com sucesso
false
true

false
1
1

S
2.2.62
1
mestre

0001-01-01T00:00:00
0001-01-01T00:00:00


false


false
DataEmissaoLan
false
false
RespFinanceiroAluno
GeracaoMov
Aberto
GeracaoRegeracaoMov
]]]]>
]]>

### Exemplo do retorno da execução

O ExecuteWithXmlParamsResult = 1 indica que o processo foi executado com sucesso.

xml


1
]]>
