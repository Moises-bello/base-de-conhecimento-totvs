---
content_hash: 0e941b0ae0cd9d5ced05c16d27e894f4918727958c54d2866e991c5aee6e6080
fetched_at: '2026-06-29T00:09:23.289816+00:00'
page_id: '422546090'
product: rm
source: tdn-rm
title: Regras Gerais (Eventos Tributários)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546090
version: 39
---

## **Conteúdo**

**Conteúdo**

## **1. Informações Comuns a Todas as Formas de Lucro e Tributação**

Independente da forma de Tributação e apresentação das pastas, algumas informações são comuns à todas as formas de Lucro e Tributação, são elas:

* Origem dos Dados
* Código na Tabela Dinâmica do Registro na ECF.
* Operação, sendo soma ou subtração.

### **1.1. Origem dos Dados**

OrigensContábil

**Origem Dados - Contábeis**

Informe que tipo de totalização será feita, com base nas Contas Contábeis, ou seja, o que será considerado para totalização e composição deste campo na regra tributaria. O sistema estará considerando a natureza da Conta (Credora ou Devedora).

|  |  |
| --- | --- |
|  | **Opções:** |
| **Tipo** | Débito Crédito Movimentação da Conta Saldo Anterior Saldo Atual |

**Algumas informações importantes**  
**Débito**: Conta (Devedora): este valor será somado ao grupo, visto que o tipo é débito e a natureza da conta é devedora.   
**Crédito**: Conta (Devedora): este valor será subtraído do grupo, visto que o tipo é crédito e a natureza da conta é devedora.  
**Débito:** Conta (Credora): este valor será subtraído do grupo, visto que o tipo é débito e a natureza da conta é credora.  
**Crédito:** Conta (Credora): este valor será somado ao grupo, visto que o tipo é crédito e a natureza da conta é credora.  
**Movimentação:** Conta (Devedora) = Débito (Conta) - Crédito (Conta)  
**Movimentação:** Conta (Credora) = Crédito  (Conta) -  Débito  (Conta)  
**Saldo anterior:** o sistema estará carregando o total a débito e o total a crédito dos lançamentos contábeis cuja data seja anterior ao início do período do evento. Feito isto, estará efetuando o seguinte cálculo:  
**Conta (Devedora)** = (Total Débito Anterior - Total Crédito Anterior) + Saldo Acumulado  
**Conta (Credora)** = (Total Crédito Anterior - Total Débito Anterior) - Saldo Acumulado  
**Saldo Atual:** o sistema estará carregando o Saldo Anterior + Movimentação da conta.

Natureza

**Origem Dados - Por Natureza de Operação**  
Serão buscadas as informações do Lançamento/tributos, selecionando Lançamento teremos as seguintes opções:

|  |  |
| --- | --- |
| **Natureza** | **Opções:** |
| **Valor a ser considerado** | Valor Contábil  Base Tributada ICMS  Isento ICMS  Outros ICMS  Valor ICMS |

***Observação*:** Poderá ser informado somente se a opção "Tributo" não estiver preenchida

Para a seleção de tributos:

|  |  |
| --- | --- |
| **Tributo** | **Opções:** |
| **Valor a ser considerado** | Base de Cálculo  Valor Tributo |

***Observação*:** Poderá ser informado somente se a opção "Lançamento" não estiver preenchida.

Lalur Parte B

**Origem de Dados - Parte B do LALUR**

Após criar as contas para a Parte B do LALUR, o usuário poderá realizar a apuração considerando estes dados. A listagem das contas será conforme sua natureza e grupo selecionado, exemplo**:** "Compensação de Prejuízo" listar somente conta com natureza = "Compensação".  
     
No item Dedução/Compensação – O controle do item tributário pelo percentual limite de dedução só é possível para itens com Origem no Lalur Parte B, hoje esse controle não é aplicável para itens com outras origens porque não é possível ao usuário alterar o valor do lançamento contábil.

|  |  |
| --- | --- |
|  | **Opções** |
| **Dedução/Compensação – Valor de aplicação** | Resultado Operacional     Resultado Não Operacional     Resultado do Exercício     Lucro Real antes da Compensação do Prejuízo      Lucro Real     Imposto apurado antes do adicional (BC \* alíquota do tributo) |

Patrimonial

**Origem de Dados - Patrimonial**

Através desta opção o Evento irá considerar os cálculos de depreciação que estão associados ao cadastro do Patrimônio nos cenários Fiscais e Contábeis.

Deverá ser criado um item com Origem Patrimonial no Grupo de Adições e outro item com Origem Patrimonial no Grupo de Exclusões. Desta forma a apuração irá considerar o valor a ser adicionado ou excluído da base de cálculo automaticamente, inclusive constituindo e baixando saldo na conta da parte B associada ao item.

Exemplo:

Neste cenário a taxa de depreciação Contábil utilizada é **maior** que a estabelecida Fiscalmente sendo necessário realizar o ajuste na apuração e constituir saldo na parte B para posterior Exclusão.

No Grupo de Adições do Evento Tributário será adicionado um item com Origem Patrimonial com efeito de constituição de Saldo na parte B.

No Grupo de Exclusões será adicionado um item com Origem Patrimonial com efeito de baixar saldo na parte B.

**Depreciação Fiscal:** 24 meses

**Depreciação Contábil:** 6 meses

Patrimônio no valor de 1.000,00 Adquirido em 01/01/2020

| Parcela | Data | Depreciação Contábil | Depreciação Fiscal | Grupo de Adições | Grupo de Exclusões | Movimentação na Parte B | Saldo da Parte B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 01/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 150,00 |
| 2 | 02/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 300,00 |
| 3 | 03/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 450,00 |
| 4 | 04/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 600,00 |
| 5 | 05/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 750,00 |
| 6 | 06/2020 | 200,00 | 50,00 | 150,00 | 0,00 | 150,00 | 900,00 |
| 7 | 07/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 850,00 |
| 8 | 08/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 800,00 |
| 9 | 09/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 750,00 |
| 10 | 10/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 700,00 |
| 11 | 11/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 650,00 |
| 12 | 12/2020 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 600,00 |
| 13 | 01/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 550,00 |
| 14 | 02/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 500,00 |
| 15 | 03/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 450,00 |
| 16 | 04/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 400,00 |
| 17 | 05/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 350,00 |
| 18 | 06/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 300,00 |
| 19 | 07/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 250,00 |
| 20 | 08/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 200,00 |
| 21 | 09/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 150,00 |
| 22 | 10/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 100,00 |
| 23 | 11/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 50,00 |
| 24 | 12/2021 | 0,00 | 50,00 | 0,00 | 50,00 | -50,00 | 0,00 |

### **1.2 Código na Tabela Dinâmica do Registro na ECF**

Na parametrização das regras tributárias serão disponibilizadas na seleção do campo "Código na [Tabela Dinâmica](http://tdn.totvs.com/pages/viewpage.action?pageId=422546165)  do Registro na ECF" as informações das tabelas dinâmicas disponíveis no layout da ECF. A tabela a ser listada será apresentada conforme a forma de tributação selecionada e pasta (Grupo) que o usuário está parametrizando.  
O objetivo deste campo é somar ou subtrair o valor do item do evento com os demais itens do grupo. Este campo independente do tratamento existente para cada item com relação à Natureza da Conta Contábil.

## **2. Apuração Filial SCP**

A definição de SCP é feita através do cadastro da [Filial](http://tdn.totvs.com/pages/viewpage.action?pageId=422545738), a partir disso, no evento tributário será habilitado o campo " Apurar para Filial SCP".  
Na apuração dos tributos do sócio ostensivo, devem ser desconsideradas as movimentações de todas as Filiais SCP, ou seja, quando o sistema estiver apurando o tributo da filial matriz será desconsideradas todas as informações das filiais. Na apuração dos tributos da SCP devem ser consideradas apenas movimentações da Filial SCP, ou seja, ao encerrar o período de apuração o sistema irá processar somente as informações da filial SCP, neste caso o usuário deverá parametrizar o evento tributário e informar a filial SCP correspondente ao mesmo.

## **3. Lançamento Manual**

Caso seja necessário acrescentar algum valor à apuração que não seja possível ser recuperado da contabilidade e da Parte B do LALUR, foi criado um anexo ao Evento Tributário que possibilita a inserção manual desses valores. Será preciso informar:

1. Período de Apuração
2. Forma de Tributação
3. Tipo de Informação
4. Item da Tabela Dinâmica ECF
5. Histórico
6. Data
7. Valor
8. Operação (soma ou subtração dentro do grupo correspondente)

Na apuração, ao calcular o valor de cada grupo do Evento, serão considerados os lançamentos manuais de acordo com as características informadas. É importante ressaltar que apuração irá identificar tanto o lançamento manual quanto o evento tributário, ou seja, um será somado ao outro.

***Observação*:**Será permitida a inclusão/alteração/exclusão nos lançamentos somente se o período estiver em aberto, o sistema faz esta validação verificando se existe apuração encerrada para o tributo do evento tributário que compreenda a data do lançamento manual.

## **4. Contas Gerencias**

Informe o código da conta, ou digite o primeiro número e clique, para que sejam mostradas todas as contas cadastradas que iniciem com o número informado. Escolha a desejada, desta forma, o campo já será preenchido automaticamente.   
Para finalizar clique no botão "Incluir"  
***Observação***: Se associar uma Conta Contábil analítica que não tenha rateio gerencial o sistema não irá permitir que seja associada uma Conta Gerencial.  
Se associar uma Conta Contábil sintética que tenha rateio gerencial em qualquer conta analítica do seu grupo o sistema irá permitir que seja associada uma Conta Gerencial.

## **5. Histórico Padrão**

Neste cadastro, o **Histórico Padrão** serve como filtro para os **Lançamentos Contábeis**.  
Podem ser definidos quais históricos padrão deverá ser **considerados ou desconsiderados** no cálculo dos valores (saldo, movimentação, saldo da conta etc.).

*Formas de Utilização:*

* É possível informar **vários históricos** com a opção **"Desconsiderar"** ao mesmo tempo.  
  Nesse caso, **também serão considerados** todos os lançamentos que **não possuírem histórico padrão**.
* Ao utilizar a opção **"Considerar"**, você deve informar **apenas um histórico**,  
  pois a aplicação **não consegue filtrar dois históricos diferentes** para o mesmo lançamento contábil.
* **Nunca utilize simultaneamente as opções "Considerar" e "Desconsiderar" para registros na mesma conta contábil.**
