---
content_hash: 0b893a5a87c11d82a4a726f7b29231e251056835083f3b87583b4713dde04105
fetched_at: '2026-06-29T00:06:00.244011+00:00'
page_id: '195300153'
product: rm
source: tdn-rm
title: RMFIS00001_05.001 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_05.001+-+Perguntas+e+Respostas
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

## **Será necessário utilizar a apuração virtual para Lucro Presumido?**

Sim. O objetivo da Apuração Virtual é fechar o balanço patrimonial da empresa nos trimestres de apuração dos tributos. Caso contrário, ao validar a ECF no PVA ocorre erro de fechamento de balanço. Opcionalmente, o cliente pode efetuar o fechamento de forma manual diretamente no PVA.

A apuração Virtual não irá efetuar nenhum lançamento na base de dados. O fechamento é “virtual” processado somente na geração da ECF e o resultado enviado para o PVA.

Ela deve ser previamente criada na Gestão Contábil e, posteriormente, associada ao Anexo “**Parâmetros da Escrituração Contábil Fiscal**”. Acesso: Cadastros | Filial | Anexos | Parâmetros – ECF | Parâmetros Contábeis | Outras Informações.

Para mais informações sobre a apuração Virtual acesse: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.ApuracaoVirtual.aspx>

## **Para a forma de tributação de Lucro Real - Trimestral terei que usar a apuração virtual?**

Sim. O objetivo da Apuração Virtual é fechar o balanço patrimonial da empresa nos trimestres de apuração dos tributos. Caso contrário, ao validar a ECF no PVA ocorre erro de fechamento de balanço. Opcionalmente, o cliente pode efetuar o fechamento de forma manual diretamente no PVA.

A apuração Virtual não irá efetuar nenhum lançamento na base de dados. O fechamento é “virtual” processado somente na geração da ECF e o resultado enviado para o PVA.

Ela deve ser previamente criada na Gestão Contábil e, posteriormente, associada ao Anexo “**Parâmetros da Escrituração Contábil Fiscal**”. Acesso: Cadastros | Filial | Anexos | Parâmetros – ECF | Parâmetros Contábeis | Outras Informações.

Para mais informações sobre a apuração Virtual acesse: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.ApuracaoVirtual.aspx>

## **A Apuração Virtual deve ser feita somente para empresas que utilizam o fechamento trimestral?**

Exatamente. Opcionalmente, as empresas que apuram pelo lucro real anual também podem utilizá-la para fechar o fechamento do balanço patrimonial mensalmente.

## **Tenho que fazer a apuração virtual trimestralmente ou coloco o período para o ano inteiro?**

A Apuração Virtual é única e o sistema vai utilizar o mesmo molde para fechar o balanço patrimonial nos quatro trimestres do ano.

## **Esse recurso de Apuração Virtual seria apenas para o caso da empresa não estar com o balanço 2014 fechado ainda?**

Não. Todas as empresas que fazem apuração trimestral do IRPJ e CSLL, precisarão utilizar a Apuração Virtual. Essa Apuração Virtual não substitui a Transferência de Grupos Contábeis já existente na Gestão Contábil. Mesmo porque, a Apuração Virtual não faz nenhum lançamento na base de dados. Todo o processamento é feito virtualmente, apenas para fins de ECF.

## **Essa apuração virtual será utilizada apenas para apuração do lucro real trimestral?**

Não somente lucro real trimestral, mas, no lucro presumido e imunes e isentas que possuem apurações trimestrais.

## **Essa apuração virtual não interfere em nenhum outro processo correto? Balancetes, DRE acumulada?**

Exatamente! A Apuração Virtual não faz nenhum lançamento na base de dados. Todo o processamento é feito virtualmente, apenas para fins de ECF.

## **Como fica a apuração virtual no 4º Trimestre? Sendo que no 4º Trimestre já foi efetuado um encerramento anual?**

Para fins de ECF o encerramento anual, realizado através da Transferência de Grupos Contábeis, é desconsiderado e todo o fechamento feito através da Apuração Virtual.

## **Com a atualização da ECF a transferência de grupos contábeis acaba?**

Não, a transferência de grupos contábeis não acaba, para a ECF o cliente poderá optar por utilizar a transferência ou a apuração virtual.

## **A Apuração Virtual deverá ser baixada em txt?**

Não, a apuração virtual deve ser criada pelo cliente de acordo com as informações da empresa.
