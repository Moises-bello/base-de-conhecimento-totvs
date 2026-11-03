---
content_hash: c4367f5701e9c1d5324927b548b5f156640f7dc635f172e2fdccf18aefa4635b
fetched_at: '2026-06-29T00:06:02.170659+00:00'
page_id: '198944063'
product: rm
source: tdn-rm
title: RMFIS00002_09.002 - Controle de Compensação de Prejuízo Fiscal e Base de Cálculo
  Negativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198944063
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.39 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 13/08/2015 |

**Lucro Real – Compensação de Prejuízo Fiscal / Base Negativa**

Para controle do Prejuízo/Base Negativa a Compensar, devem ser criadas contas na Parte B do Lalur, em função do:

a)       Tributo: IRPJ ou CSLL

b)       Tipo de prejuízo: operacional e não operacional (para IRPJ) e do

c)       Período de apuração.

No caso de Prejuízos **apurados** **anteriormente a 2014**, a criação das contas deve seguir a seguinte orientação:

1. A **Natureza** da conta deve ser “**Compensação de Prej. Fiscal/ BC Negativa**”.
2. A **Data de Início de Vigência**, deve ser o último dia do período de apuração do tributo que originou a conta. No exemplo acima, como o prejuízo foi apurado no ajuste anual de 2013, a Data de Início de Vigência é 31/12/2013.
3. Na aba “Informações Fiscais” deve ser inserido o tributo.
4. Deve ser informado, também, o valor do prejuízo apurado.

**OBSERVAÇÃO**: Em caso de prejuízos apurados há mais tempo, fica a critério do cliente transportar toda a movimentação da conta para a Parte B do Lalur desde sua constituição, ou apenas transferir o saldo em 31/12/2013.

No caso de prejuízos **apurados em 2014**, a criação das contas deve seguir a seguinte orientação:

5. A **Natureza** da conta continua sendo “**Compensação de Prej. Fiscal/ BC Negativa**”.

 6. A **Data de Início de Vigência**, o último dia do período de apuração do tributo que originou a conta. No exemplo acima, como o prejuízo foi apurado no 1º Trimestre de 2014, a Data de Início de Vigência é 31/03/2014.

7. Na aba Informações Fiscais, associa-se o tributo e no campo “**Saldo Inicial**” deve ser informado “**0,00**” (zero). A Constituição do saldo da conta será feito através de um lançamento nessa conta com o Tipo “**Constituição de Saldo**”:

**Compensação**

Para a compensação dos prejuízos apurados, as contas criadas nos moldes acima, devem ser informadas no Evento Tributário, no Grupo Compensação de Prejuízo/Base Negativa:

1. No Grupo “**Compensação de Prejuízo**” só é possível informa no campo “**Origem da Informação**” a opção “**Lalur Parte B**”.
2. Informe uma Descrição e associe o Código da Tabela Dinâmica da ECF.
3. Informe a conta criada na Parte B do Lalur onde foi registrado o prejuízo a ser compensado.
4. No campo “**Tipo**” existem as opções “**Movimentação Conta**” e “**Crédito**”. Utilize aquela que melhor se aplica.  
     
   **DICA:** No caso de apuração mensal por estimativa, sugere-se utilizar a opção “**Movimentação Conta**” porque pode ser necessário ajustar o valor compensado no avançar dos meses. Isso pode ser necessário porque o lucro da empresa pode diminuir e, consequentemente, o valor do limite permito para dedução vai diminuir também. Nestes casos, deve-se fazer um lançamento a débito na conta da Parte B do Lalur para ajustar o valor acumulado que está sendo compensado no período.
5. Na pasta “**Dedução/Compensação**”, informe o **Percentual** limite de dedução (atualmente 30%).
6. Informe, também, o valor de aplicação do percentual (atualmente o lucro líquido ajustado).

**Simulação**

Na Simulação do Evento Tributário, o sistema irá calcular o valor que poderá ser compensado a partir do percentual limite informado para conta do Lalur – B **(1)**. Observe que no log da imagem acima, o sistema informa, também, que o valor do limite calculado pelo percentual ($ 673.583,97) é maior que o saldo da conta na Parte B do Lalur ($ 215.000,00). Portanto, na simulação dos cálculos, o valor considerado foi o limite da conta **(2)**.

Antes do encerramento do período de Apuração, o lançamento da compensação deve ser efetivado, manualmente, na conta da Parte B para que o encerramento considere esse valor:

1. Informe a data do Período onde deve ocorrer a compensação.
2. Informe o valor (o limite máximo já foi calculado pelo sistema na simulação, portanto, pode ser compensado qualquer valor até o limite).
3. Informe o Tipo “**Crédito**”.

Só será possível, incluir, editar ou excluir lançamentos de compensação de prejuízo da Parte B se o período de apuração equivalente estiver aberto.

**Reclassificação do Prejuízo:**

Os prejuízos operacionais e não operacionais devem ser controlados em contas distintas na Parte B.

A reclassificação do Prejuízo Fiscal, de acordo com § 11 do art. 36 da IN SRF 11/96, deve ser realizada na Parte B do Lalur, através do Processo de “Lançamento de Reclassificação do Prejuízo”. A reclassificação acontece apenas do prejuízo não operacional para operacional.

Deve-se selecionar a conta do prejuízo não operacional para executar o processo, informar a conta de destino e o valor. O sistema irá inserir um lançamento de crédito na conta origem e um de débito na conta destino.

**IMPORTANTE!**

* Para incluir o lançamento de reclassificação, o período de apuração equivalente à data do lançamento deve estar encerrado.
* Ao reabrir um período de apuração que possua lançamento de reclassificação de prejuízo, o sistema irá excluir o lançamento de reclassificação antes de reabrir o período.
* O lançamento de reclassificação pode, também, ser excluído diretamente no Cadastro de Lançamentos da Parte B. As duas partidas serão excluídas concomitantemente.
