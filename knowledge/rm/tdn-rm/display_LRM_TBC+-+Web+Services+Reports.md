---
content_hash: f8401ff1174dfcb19de7db5e88c1f665d666096365f868c9c70072569abb9e09
fetched_at: '2026-06-29T00:08:12.922879+00:00'
page_id: '243654300'
product: rm
source: tdn-rm
title: TBC - Web Services Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/TBC+-+Web+Services+Reports
version: 38
---

# Índice:

---

.\*ndice:

# Introdução:

---

       O Web Service Reports Fornece serviços para gerar relatórios do TOTVS Reports de forma síncrona e assíncrona. O modelo de autenticação utilizado é o Basic Authentication.

      [Utilizando Web Service do RM Reports no Fluig](http://tdn.totvs.com/display/LRM/Web+Service+do+RM+Reports+no+Fluig)

# Como Funciona:

---

Estão expostos no wsReport alguns serviços, onde para consumi-los, é necessário enviar através de uma requisição um envelope SOAP passando os parâmetros de cada serviço. 

      O serviço é exposto pelo host conforme documentação abaixo:

false

**Para baixar os arquivos da aplicação exemplo em ASP.Net,**

Segue abaixo o detalhamento e exemplos de utilização dos serviços em envelope SOAP:

GetReportListfalse

Retorna a lista de todos os relatórios de uma determinada coligada.

.RequestxmlRequest




1
 ]]>ResponsexmlResponse


0,TOTVS
Educacional,306,Boletim,Boletim,06/10/2010
15:43:00,597e2978-351d-4629-a2fb-b57432cad210;,0,TOTVS
Educacional,30,Contrato,Contrato,06/10/2010
15:43:00,71eff25f-0960-4ab7-bbc9-564044dde0fe;,0,TOTVS Gestão
Financeira,312,Boleto Itaú.2.1,Cópia de Cópia de Boleto Itaú,08/04/2016
07:49:00,c9c51350-3cfa-410e-b818-224a013d0296;,0,TOTVS Inteligência de
Negócios,316,filtrosNomeados,filtrosNomeados,11/04/2016
10:37:12,d19713e7-eda0-4bf1-8e92-140714240c16;,0,TOTVS
Educacional,31,EDUREL002,Listagem de Alunos com foto,06/10/2010
15:43:00,b84b941c-54e5-43c1-996b-3e9eae05e902.......
]]>GetReportMetadata:false

Retorna a estrutura de um determinado relatório (utilizado apenas para conferencia).

.RequestxmlRequest




1

306
]]>ResponsexmlResponse









































]]]]>
]]>GetReportInfofalse

Retorna as informações de filtro e parâmetros, caso o relatório possua.

O retorno é um xml de duas estruturas serializadas. Elas devem ser utilizadas separadamente ao chamar o método de geração do relatório.

.RequestxmlRequest




1

306
]]>ResponsexmlResponse







RptReport


PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010'
PFUNC
true
(PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010'
)
]]]]>



PARAM\_COLIGADA
PARAM\_COLIGADA

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089

true

PARAM\_TESTE
PARAM\_TESTE

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089

true
]]]]>
]]>GenerateReportfalse

Gera efetivamente o relatório e retorna o identificador a ser utilizado para fazer o download do relatório pelo método GetFileChunk.

Veja que os filtros e os parâmetros correspondem ao que o método GetReportInfo retornou e foi passado separadamente.

Os filtros e parâmetros podem ser alterados conforme destaque abaixo.

Importante

Caso esteja executando um relatório Global, o valor da Coligada para execução do relatório e das consultas presentes no relatório pode ser passado através do parâmetro Contexto, por exemplo:

xmlCodColigada=7;CodFilial=1]]>

Caso não seja enviado, será utilizado a Coligada do relatório.

.RequestxmlRequest




1

306




RptReport


PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010'
PFUNC
true
(PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010')
]]]]>




PARAM\_COLIGADA
PARAM\_COLIGADA

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
1
true

PARAM\_TESTE
PARAM\_TESTE

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
1
true
]]]]>

Report.pdf

CodColigada=1;CodFilial=1
]]>ResponsexmlResponse


33f3bc8a-2553-4ad2-a53f-a03b487844cf
]]>GetGeneratedReportSizefalse

Retorna o tamanho do relatório em bytes. Este resultado é utilizado para fazer o download parcial ou total do relatório pelo método GetFileChunk.

.RequestxmlRequest




33f3bc8a-2553-4ad2-a53f-a03b487844cf
]]>ResponsexmlResponse


45484
]]>GetFileChunkfalse

Retorna o relatório gerado e**m base 64** e no formato especificado no parâmetro filename do método GenerateReport.

.RequestxmlRequest




33f3bc8a-2553-4ad2-a53f-a03b487844cf

0

45484
]]>ResponsexmlResponse


[CONTEUDO DO RELATÓRIO EM BASE 64]
]]>GenerateReportAsynchronousfalse

Funciona da mesma forma que o GenerateReport, porém não aguarda a geração do relatório e retorna um identificador único a ser utilizado para consultar o status da geração.

Importante

Caso esteja executando um relatório Global, o valor da Coligada para execução do relatório e das consultas presentes no relatório pode ser passado através do parâmetro Contexto, por exemplo:

xmlCodColigada=7;CodFilial=1]]>

Caso não seja enviado, será utilizado a Coligada do relatório.

.RequestxmlRequest




1

306




RptReport


PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010'
PFUNC
true
(PFUNC.CHAPA >= '00001' AND
PFUNC.CHAPA <= '00010'
)
]]]]>




PARAM\_COLIGADA
PARAM\_COLIGADA

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
1
true

PARAM\_TESTE
PARAM\_TESTE

System.String
4
mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
1
true
]]]]>

Report.pdf

CodColigada=1;CodFilial=1
]]>ResponsexmlResponse


ff3fe362-2433-42a1-bda6-44e6d811e578
]]>GetGeneratedReportStatusfalse

Utilizado para checar o status da geração do relatório que foi demandado a partir do método GenerateReportAsynchronous.

O retorno é um código de status, seguido de um GUID a ser utilizado para fazer o download do relatório pelo método GetFileChunk. Ex:

* **0;Wait** – Indica que o relatório está sendo gerado
* **1;xxxxxxxxxxxxxxxxxxxxxxxxxxxxx** - Indica que foi gerado, seguido do GUID para download
* **2;Erro xxxxxxx** – Indica que ocorreu um erro, seguido da mensagem de erro

.RequestxmlRequest




ff3fe362-2433-42a1-bda6-44e6d811e578
]]>ResponsexmlResponse


1;24c5bc57-ffad-422e-8893-67a5c0256e76
]]>

# Aplicação de Teste:

---

        Para utilizar a aplicação de testes é necessário possuir o Microsoft Visual Studio.

* Com o Visual Studio aberto: Clique nas opções FILE -> Open -> Web Site. Conforme exemplo abaixo:

* Em seguida selecione a pasta descompactada e clique em "Open" conforme abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.12 ou superior

false

**Processo:** Web Services Reports

falsefalse

**Status:** Finalizado

false

**Data:** 15/05/2016

false

**Autores:**

false

**Download dos arquivos:**
