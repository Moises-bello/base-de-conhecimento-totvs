---
content_hash: 4480ca20b904475236628d583852e54050e531ce9fa167355c8c5f8ca0a81fdd
fetched_at: '2026-06-29T00:09:29.262027+00:00'
page_id: '423938856'
product: rm
source: tdn-rm
title: Cálculo Saldo Consolidado 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938856
version: 3
---

Afim de atender as instituições que precisam entregar demonstrações consolidadas através da ECD (Bloco K), disponibilizamos um processo que irá "alimentar" o plano de contas consolidado com os saldos das contas das empresas envolvidas na consolidação.

O processo calcula os valores consolidados de acordo com as coligadas do [Grupo Empresarial](https://tdn.totvs.com/display/LRM/Grupo+Empresarial) informado no plano de contas paralelo e também pelo percentual de consolidação informado no cadastro de [Movimentações do Investimentos Societários](https://tdn.totvs.com/pages/viewpage.action?pageId=627971088).

Este processo insere informação em banco de dados, mais precisamente na tabela CSALDOCONSOLIDADO, há três campos na tabela referente a valores, sendo eles:  
   
Saldo aglutinado: O processo encontra esse saldo através da soma dos saldos das contas contábeis que estão vinculadas a uma conta consolidada;  
Valor Eliminado: Caso o usuário tenha cadastrado eliminações, o valor eliminado será informado com base na eliminação cadastrada;  
Saldo Consolidado: Basicamente é o resultando de uma eliminação no saldo aglutinado, segue abaixo exemplos de como chegar no saldo consolidado:

|  |  |  |  |
| --- | --- | --- | --- |
| Exemplo | **Aglutinado** | **Eliminação** | **Consolidado** |
| 1 | 1.000,00 D | 100,00 D | 900,00 D |
| 2 | 1.000,00 D | 100,00 C | 1.100,00 D |
| 3 | 1.000,00 D | 1.100,00 D | 100,00 C |

Regra para atender ao validador disponibilizado pela RFB

A eliminação deve ter natureza igual ao saldo aglutinado para que haja subtração para composição do saldo consolidado, caso contrário haverá a soma para composição do saldo consolidado.

**Filtro:** O usuário poderá filtrar Coligada/Filial, o filtro flexibiliza ao usuário poder escolher coligadas ou filiais específicas para que o saldo seja calculado. Caso o filtro não seja ativado, o sistema considera para o cálculo todas as coligadas cadastradas como controladas e todas as suas filiais respectivamente.

Foi disponibilizado para o usuário, a opção de consultar os saldos que foram gerados pelo processo, para isso, basta acessar os anexos do cadastro do plano de contas paralelo (Finalidade: Consolidação de Saldos) a opção "Saldo das Contas do Plano de Contas Consolidado". 

Veja Também

* Cadastro de Controladas
* K100 - Código do País
* Plano de Contas Consolidado
* Eliminação de Valores
* [Eventos societários](http://tdn.totvs.com/x/U6sEGw)
