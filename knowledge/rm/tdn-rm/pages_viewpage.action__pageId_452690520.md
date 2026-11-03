---
content_hash: 6e074339f4470319248a44d469c6a5699c0b58276a6d0c2a89eabd17528875d4
fetched_at: '2026-06-29T00:09:58.345138+00:00'
page_id: '452690520'
product: rm
source: tdn-rm
title: Nf-e Geração de movimento por regime de caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452690520
version: 21
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar a geração de movimento por regime de caixa via WebService para boletos gerados para a parcela . Os movimentos gerados poderão ser consultados no módulo TOTVS Gestão de Estoque, Compras e Faturamento.

Através do processServer "**EduNFESliceableData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a geração do movimento por regime de caixa.

**[Se necessário clique aqui para obter ajuda na configuração do Host](http://tdn.totvs.com/display/LRM/Webservices) ou****[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)**

**Método ExecuteWithXmlParams**

Este é o método publicado no WebService (wsProcess) para que seja consumido o serviço de geração do movimento por regime de caixa (**EduNFESliceableData***->* **a partir do patch 12*****.1.2410.149 e versões superiores***)

Até a **versão 12.1.2406 e até o patch 12.1.2410.149** este é o método publicado no WebService (wsProcess) para que seja consumido o serviço de geração do movimento por regime de caixa (**EduNFEData**)

#### **Utilização do WebService**

Para realizar a geração de movimento por regime de caixa , deve ser utilizado a operação de **ExecuteWithXmlParams**.

Deve ser passado um XML contendo as informações para execução do processo e os campos do contexto de execução com os valores como se o usuário estivesse logado no sistema (os campos destacados são obrigatórios para processos que serão executado no contexto do TOTVS Educacional).

* O preenchimento dos campos abaixo deve ser realizado na TAG "**Context**" e "**CodUsuario**"

Campos obrigatórios: $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA, $CODUSUARIO

* O filtro de quais boletos serão processados podem ser informados na TAG "**EduNFEParamsProc / FiltroBoleto**"

Exemplo:

O filtro de boleto funciona basicamente igual aos filtros de tela do RM, e com isso pode ser utilizado comandos SQL utilizando por exemplo a clausula "IN"

* Na TAG "**MovimentoNFEParams**" também devem ser preenchidos outros parâmetros

Acessar XML no RM

**Dica:**

Para conhecer melhor o XML e suas informações é possível acessar no RM o XML de processos que foram executados.

Por exemplo, podemos executar o processo de geração de movimento em um base de dados de homologação e observar no XML gerado as informações preenchidas.

Para isso acesse o menu “Executar” digite “XML” e clique em “XML de parâmetros de JOB”  na tela apresentada crie um filtro para que seja carregados os JOB do processo em questão.

### Exemplo do XML completo pronto para ser consumido via o WebService responsável em executar o processo de geração de movimento por regime de caixa

Geração do movimento por regime de caixa pelo serviço EduNFESliceableData

É recomendando a utilização do serviço EduNFESliceableData **a partir do patch 12*****.1.2410.149 e versões superiores***

### Exemplo do retorno da execução

xmlGeração do Movimentotrue




EduNFESliceableData



S
EduNFEAction
true
false
false
mestre





$EXERCICIOFISCAL
22

$CODLOCPRT
12

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

459e24dc-3cfd-449e-b099-c633bce235d0
Falha na execução do processo

false
BHN050104664
true
10.173.95.198
false


1
124667
false
BHN050104664

1000
1
wesley.costa
false

false
false



Geração de movimentos
0
true
false
2025-01-10T13:57:06.6541489-03:00
JobMonitor
false
EduNFESliceableData

RM.Edu.Interfaces.IEduNFE
4
RM.Edu.Interfaces.Intf, Version=12.1.2410.145, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false
false
false
RMSJobData

0
1
1
1


FLANBOLETO.IDBOLETO = :F1
14470
false
0001-01-01T00:00:00



false
false
false
mestre




false

50615434-97e4-4ca3-9c69-3c55cca704d4
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
2025-01-10T13:57:06.6541489-03:00
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
2.2.10
1
mestre

2025-01-10T00:00:00
2025-01-06T00:00:00


false


false
DataEmissaoLan
false
true
RespFinanceiroAluno
GeracaoRegeracaoMov
Todos
GeracaoRegeracaoMov
]]]]>
]]>

O ExecuteWithXmlParamsResult = 1 indica que o processo foi executado com sucesso.

xmlRetorno Geração de Movimentotrue
   
      
         1
      
   
]]>Geração do movimento por regime de caixa pelo serviço EduNFEData

### Exemplo do retorno da execução

xmlGeração do Movimentotrue




EduNFEData



S
EduNFEAction
true
false
false
mestre





$EXERCICIOFISCAL
22

$CODLOCPRT
12

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

717d6d42-05ba-4ff0-8798-e0a87fdee7b5
Falha na execução do processo

false
BHN050104664
true
10.173.95.198
false


1
124662
false
BHN050104664

1000
1
wesley.costa
false

false
false



Geração de movimentos
0
true
false
2025-01-10T11:44:16.2439762-03:00
JobMonitor
false
EduNFEData

RM.Edu.Interfaces.IEduNFE
4
RM.Edu.Interfaces.Intf, Version=12.1.2410.145, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false
false
false
RMSJobData

0
1
1
1


FLANBOLETO.IDBOLETO = :F1
14470
false
0001-01-01T00:00:00



false
false
false
mestre




false

e313572d-b4d4-4a98-a181-23ff6b0a0fb3
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
2025-01-10T11:44:16.2445804-03:00
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
2.2.10
1
mestre

2025-01-10T00:00:00
2025-01-06T00:00:00


false


false
DataEmissaoLan
false
true
RespFinanceiroAluno
GeracaoRegeracaoMov
Todos
GeracaoRegeracaoMov
]]]]>
]]>

O ExecuteWithXmlParamsResult = 1 indica que o processo foi executado com sucesso.

xmlRetorno Geração de Movimentotrue


1
]]>
