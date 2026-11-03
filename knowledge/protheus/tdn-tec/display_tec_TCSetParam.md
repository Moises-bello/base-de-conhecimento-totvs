---
content_hash: fb78c3faa2ca8f4144b386aae7a2746a6bf0aadcec0f5a719539ceaada465d25
fetched_at: '2026-07-02T19:24:22.547634+00:00'
page_id: '270907361'
product: protheus
source: tdn-tec
title: TCSetParam
type: documentation
url: https://tdn.totvs.com/display/tec/TCSetParam
version: 2
---

TCSetParam

Insere ou atualiza um parâmetro na TOP\_PARAM.

## Sintaxe

false, < cValue > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cParam | caractere | Indica o nome do parâmetro que será criado ou atualizado. | X |  |
| cValue | caractere | Indica o valor do parâmetro indicado em **cParam**. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna 0 (zero) se a operação foi completada com sucesso ou diferente em caso de erro. |

## Observações

* **TCSetParam** utiliza a o identificador de conexão entre o DBAccess e o SGBD (igual ao valor retornado pela função ) para diferenciar os parâmetros inseridos por cada conexão.
* Caso exista mais de uma conexão no mesmo programa para o mesmo ambiente de DBAccess e cada conexão insira o mesmo parâmetro com o mesmo valor, cada conexão terá uma entrada na tabela TOP\_PARAM.
* A função utiliza necessariamente a RDD **TOPCONN**. Caso não haja conexão com o DBAccess, será exibida uma mensagem de advertência no log de console do **AppServer** "*Warning - TCSetParam - statement ignored - No connection.*" e a função irá retornar **-2**.
* Caso **cValue** esteja vazio, a função irá retornar erro e será exibido no log de console do **DBAccess** a mensagem "*SetParam [PPP] does not accept NULL parameter value.*", onde **PPP** é o nome passado em **cParam**.
* Em builds do AppServer superiores a **7.00.131227A**, se **cParam** estiver vazio, a função irá retornar erro.
* Se o ambiente do DBAccess que será acessado não suportar conexãoes ISAM (chave **IsamConnection** no arquivo ini do DBAccess), a função retornará erro e será exibido no log de console do **DBAccess** a mensagem "*SetParam only supported when IsamConnection is ENABLED.*".
* Se o ambiente do DBAccess que será acessado está como somente leitura (chave **ReadOnly** no arquivo ini do DBAccess), a função retornará erro e será exibido no log de console do **DBAccess** a mensagem "*SetParam not supported on READONLY Connection.*".
* Em caso de erro, consulte a função  para saber o motivo.
* A função funciona para os SGBDs: **MS SQL Server**, **Oracle**, **Informix**, **DB2**, **OpenEdge**. Para os demais, a função retornará **0**, mas não efetuará operação alguma.
* O SGBD **PostgreSQL** é suportado a partir da build **20161016** com data de geração superior a **03/01/2017**.

## Exemplos

O teste abaixo considera que a tabela TOP\_PARAM está vazia.

cppEclipsetruefalseCNT ) // Vai exibir: 1
DBCloseArea()
// Pega o valor do parâmetro "PARAM1"
cQuery := "SELECT PARAM\_VALUE FROM TOP\_PARAM WHERE PARAM\_NAME='PARAM1'"
DBUseArea( .T., cRDD, TCGenQry( , , cQuery ), (cAlias), .F., .T. )
conout( (cAlias)->PARAM\_VALUE ) // Vai exibir: Value2
DBCloseArea()
TCUnlink( nHandle1 )
return
]]>

## Veja também
