---
article_id: 28424631692055
category: ADVPL - Ponto de Entrada
content_hash: c439c9fa7bf77b3fe6acf3bed728069a49e6976937500c917a0e447a6f9ebbf9
fetched_at: '2026-06-28T22:40:12.997982+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Linguagem TLPP
  ou TL++
type: support-article
updated_at: '2025-01-07T13:46:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28424631692055-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Linguagem-TLPP-ou-TL
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28424618778903)*Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**O que é a Linguagem TLpp (TOTVS Language plus plus)?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – Versão 12

**Solução**

A linguagem **TLpp** (**TOTVS Language plus plus**) é uma evolução do **AdvPL**.

Desenvolvida para trazer ao programador **AdvPL** algumas facilidades vistas em outras linguagens, como **Nomes longos**, **Tipagem,** entre outras facilidades.

**Exemplos**:

#include 'tlpp-core.th'  
//O recurso de namespace foi liberado na versão 17.3.0.0 para a linguagem TLPP e tem como   
//benefício a melhor organização do código.  
namespace exemplo

Class ClassWithNamespace  
   Public Method new()  
    data dataI  
Endclass

Method new() Class ClassWithNamespace  
    Local cFrase := "exemplo frase TLPP" as Character  
    conout(cFrase)  
Return self

User Function testeNamespace  
    Local nNumber := 2 as Numeric  
    conout(nNumber)  
    u\_testeNamespace2()   
//a função testeNamespace2 poderá ser chamada sem explicitar o   
//namespace nem utilizar using porque estão no mesmo fonte  
Return

user Function testeNamespace2  
    conout("testeNamespace2")  
Return

**Exemplo chamada do *namespace* em outro fonte**:

User Function nameEX2  
//para realizar a chamada basta colocar o nomedo namespace definido + o nome da função   
//definida no fonte do name space  
    exemplo.u\_testeNamespace()//faço referencia ao namespace.nomedaminhafunção

Return

**Observação:**

* Os arquivos de biblioteca (**includes**) passam a ter a extensão **.th** (**TLpp Header File**) e são utilizados da mesma maneira que os arquivos **.ch** do **AdvPL**, ou seja, são pré-processados como parte da linguagem **TLpp**.
* Para desenvolver em **TLpp** é importante você extrair os **includes** da linguagem, que já vem com o **tlpp.rpo**, adicionar [**#include** '**tlpp-core.th**'] no seu programa **tlpp** e pronto, você já pode usufruir de todos os novos recursos da linguagem.
* Os arquivos com extensão **.ch** continuam sendo aceitos, mas é recomendado que a nova extensão seja adotada para novos desenvolvimentos.
* O nome do **namespace** pode ser um nome simples ou um nome que contenha "." como separador
* Importante ressaltar que todo nome de **namespace** iniciado com "**tlpp**" está reservado ao **tlppCore**. Desse modo, qualquer tentativa de uso fora desse domínio, será bloqueada em tempo de compilação.
* Uma vez utilizado o recurso **namespace** no '***main***' da sua aplicação, é necessário que o explicite utilizando o separador "**.**"

**Importante:**

|  |
| --- |
| Uma das premissas do **TLpp** é respeitar o escopo definido pelo desenvolvedor para funções, classes, métodos, propriedades e variáveis.  Portanto, em fontes com a extensão **.tlpp**, as funções definidas como **STATIC** somente poderão ser acessadas por funções ou métodos pertencentes ao mesmo código fonte.  Devido a isso, rotinas que fazem uso do recurso "**StaticCall**" não funcionarão em **TLpp**.  Caso você possua rotinas que façam uso direto a esse recurso, aconselhamos a refatoração! |

**Saiba mais**[A Linguagem TLPP](https://tdn.totvs.com/display/tec/TLPP)  
[MVC X TLpp](https://tdn.totvs.com/display/public/framework/Suporte+a+TLPP+no+Protheus)  
[Extrair includes TLPP.RPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28308373167127)
