---
content_hash: 53692378eeadcab6b9beaeb584c95828cc52aaa143380a2f041e03ebe873ff58
fetched_at: '2026-06-29T00:10:08.678150+00:00'
page_id: '452719557'
product: rm
source: tdn-rm
title: Atualização de Saldo de FGTS.Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719557
version: 2
---

Neste módulo será possível atualizar para todos os funcionários o saldo de FGTS depositado no banco para cálculo das rescisões dos funcionários com demissão sem justa causa e também para emissão da GRFC. Para que o processo seja executado de forma correta o usuário deverá acessar: Administração de Pessoal | Cadastros | Funcionários, editar ou incluir o funcionário desejado, aba: Rotinas Mensais / Anuais | FGTS/SEFIP, campo: "Saldo FGTS Fins Rescisório" informar a soma dos valores recolhidos para o funcionário até a presente data já com a correção aplicada mensalmente e no campo: "Data Último Saldo FGTS" informar a data do último saldo.  
 Outra informação importante a ser cadastrada no sistema antes da execução do processo, é a atualização das cotações. O usuário deverá acessar: Administração de Pessoal | Cadastros | Cadastros Globais | Moedas e Índices, e certificar-se que tenha um registro do tipo "Índice" e com símbolo "FGTS" cadastrado. Acessando: Administração de Pessoal | Cadastros | Cadastros Globais | Moedas e Índices| FGTS | Anexos | Cotações, deverá ser incluído mensalmente o fator de atualização disponibilizado pela CEF, com a data sempre sendo o primeiro dia da competência.

**Atualizando o Saldo de FGTS**

Para realizar a atualização do saldo de FGTS o usuário deverá acessar: Administração de Pessoal | Alterações Globais | Alterações Cadastrais | Atualização do Saldo de FGTS, escolher o(s) funcionário(s) desejado(s) e clicar no botão: "Executar". Ao final do processo, o sistema gera um arquivo de log para conferência dos valores atualizados.

**Exemplo do cálculo realizado pelo sistema para atualização do saldo de FGTS**

**S** - Saldo de FGTS do Mês Anterior;

**D** - Depósito de FGTS da Última Competência;

**F** - Fator de Atualização de FGTS;

...então...

**Saldo de FGTS Atualizado = S + (S x F) + D**

**Observação:**

O sistema sempre processa a atualização até a competência anterior. Isso porque precisa que todos os dados estejam cadastrados no sistema para que o cálculo fique correto. Para incluir a competência atual, é necessário marcar o parâmetro "Incluir a competência atual" nos parâmetros do processo. Entretanto, a utilização desse parâmetro não é aconselhável, uma vez o saldo de FGTS de cada funcionário pode ser atualizado apenas uma vez por competência e, caso haja alguma inconsistência nos dados informados, o saldo ficará incorreto.

**Parâmetro "Incluir a competência atual"**

Em casos específicos, como na rescisão de muitos funcionários em uma mesma competência, o parâmetro "Incluir a competência atual" pode ser útil para atualizar o saldo de FGTS desses funcionários sem que seja necessário liberar a competência. Entretanto, o parâmetro deve ser usado com cautela, uma vez o saldo de FGTS de cada funcionário pode ser atualizado apenas uma vez por competência e, caso haja alguma inconsistência nos dados relacionados ao FGTS do funcionário, o saldo ficará incorreto. Para evitar que isso ocorra, é importante verificar os seguintes itens:

* Certifique-se que todos os lançamentos necessários no envelope dos funcionários selecionados já foram realizados;
* Certifique-se que não é necessária nenhuma mudança de parametrização que impacte na base e valor de FGTS dos funcionários cujo saldo será atualizado;
* Certifique-se que foi realizado recálculo da folha para os funcionários selecionados no processo;
* Confira se os índices de atualização foram cadastrados corretamente, conforme explicado acima;
* Deve ser preenchida a "Data Último Saldo FGTS" no cadastro de funcionários;
* Certifique-se que o "Saldo FGTS Fins Rescisório" está correto.

**Exemplo:**

Mês de competência: 08/2010.

Última atualização de saldo FGTS do funcionário: 10/07/2010

Valor do último saldo atualizado: 1000.00

Valor de FGTS depositado no mês 07/2010: 40.00

Fator de Atualização de FGTS em 01/07/2010: 0.01500

Após atualização do Saldo de FGTS o valor atualizado será 1.055,00.

**Memória do cálculo:**

10/07/2010 = 1000.00

10/07/2010 = 15.00 (índice de correção: 0.015)

30/07/2010 = 40.00 (deposito do mês 07/2000)

10/08/2010 = 1055.00 (Total corrigido até esta data)

**Aplicando a fórmula:**

**S** = 1000.00

**D** = 40.00

**F** = 0.015000

1000 + (1000 x 0.015000) + 40 = 1055.

É possível incluir informações de resgate de saldo, acessando: Administração de Pessoal | Cadastros | Funcionários | Anexos | Folha de Pagamento | Manutenção do FGTS. Os registros incluídos nessa visão são utilizados para calcular o saldo real de FGTS, que é apresentado no campo "Saldo FGTS na CEF". Dessa forma o cálculo sofre uma pequena alteração, descrita abaixo:

**Se tivermos:**

**S** - Saldo de FGTS do Mês Anterior;

**D** - Depósito de FGTS da Última Competência;

**F** - Fator de Atualização de FGTS;

**R1** - Resgate de Salgo de FGTS feito antes do dia 10\*;

**R2** - Resgate de Salgo de FGTS feito depois do dia 10\*;

\* Verificar na legislação vigente em quais casos o resgate é permitido.

...então...

**Saldo de FGTS Atualizado = S + ((S - R1) x F) + D - R2**

Dessa maneira calcula-se o saldo real de FGTS, ou seja, o saldo que ainda permanece depositado na CEF, e não o saldo que deverá ser considerado no cálculo rescisório. Para fins rescisórios o montante considerado para o cálculo da multa rescisória desconsidera os valores de resgate. Nesse caso o sistema utiliza a primeira forma de cálculo para a apuração da correção monetária do mês e a adiciona ao montante total de FGTS. Ao final, os dois valores (Saldo Real e Saldo p/ Fins Rescisórios) serão demonstrados no cadastro do funcionário.

**Observação:**

Para um processo de atualização mais preciso é aconselhável a execução desse módulo todos os meses. Porém, isso não é uma necessidade: caso a atualização não tenha sido executada nos últimos meses, será possível atualizar o saldo desde a data do último saldo conhecido, com a única desvantagem da necessidade de atualização retroativa das cotações.

|  |  |
| --- | --- |
|  | Veja Também |

---

[Caixa Ecômica Federal](http://www.caixa.gov.br/)
