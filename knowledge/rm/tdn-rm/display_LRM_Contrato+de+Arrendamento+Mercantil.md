---
content_hash: a8acf7d3d5b086a89652505618f1804139071909424d0fa40e317538f01891c5
fetched_at: '2026-06-29T00:10:39.016971+00:00'
page_id: '545639006'
product: rm
source: tdn-rm
title: Contrato de Arrendamento Mercantil
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+de+Arrendamento+Mercantil
version: 116
---

## Legislação IFRS 16 - CPC06

As normas internacionais de contabilidade (IFRS – International Financial Reporting Standards) passam constantemente por revisões e atualizações para garantir a melhoria contínua de sua aplicação. Essas mudanças têm como proposta garantir maior clareza nas informações financeiras e contábeis.

Em janeiro de 2019, a IFRS 16 / CPC 06 (R2), referente a leasing, entrou em vigor, impondo modificações para os registros de arrendamento das empresas, como por exemplo, locação veículos, escritórios e outros tipos de ativos. De imediato, isso impactará a forma de identificar, mensurar e divulgar os contratos de arrendamento.

A legislação estabelece que os contratos do tipo de arrendamento mercantil devem ser reconhecidos como ativo imobilizado da empresa arrendatária, e seus valores e correções contabilizados como direitos de uso e não como despesas.

A legislação também  determinam que valores a pagar registrados na contabilidade, devem ser contabilizados no curto prazo e no longo prazo (Ativo de direito de uso, passivo de arrendamento e encargos financeiros).

## Descrição do Processo

Para a gestão dos contratos de Arrendamento Mercantil a empresa arrendatária irá incluir um contrato do tipo *Arrendamento Mercantil*. 

O contrato de natureza Arrendamento Mercantil terá **um** **item** de tipo de faturamento “Periódico” com a finalidade de controle dos pagamentos mensais, contabilização dos valores, geração de previsões financeiras, reajustes e faturamento para pagamento.

## Procedimento para Implantação e Utilização

A implementação está disponível nas versões 12.1.29 e posteriores.

Arrendamentotrue1Inclusão de Contrato

### Inclusão de Contrato

### **Cadastros**

* Tipo de Contrato: Deve ser incluído o tipo de contrato referente ao Arrendamento.

           Gestão de Estoque, Compras e Faturamento → Contratos → Tipos de contrato.

Observação: Contrato do tipo arrendamento Mercantil, não está preparado para afetar orçamento. 

Para mais informações sobre o cadastro, acesse:

[Tipos de Contratos - Linha RM - TDN](https://tdn.totvs.com/display/public/LRM/Tipos+de+Contratos)

* Status de Contrato: Deve ser incluído dois status de contrato, sendo para faturamento e cancelamento.

Faturamento:

Marque a opção “Faturar”

Cancelamento:

Marque a opção “cancelamento”

Observação: Caso a empresa já utiliza a gestão de contratos RM, os status já cadastrados podem utilizados para o contrato de Arrendamento Mercantil.

Para mais informações sobre o cadastro, acesse:

[Status de Contrato  - Linha RM - TDN](https://tdn.totvs.com/display/public/LRM/Status+de+Contrato)

* Arrendatário: O arrendatário será a filial que será o "locatário" do bem. Este Arrendatário deve utilizar a mesma filial relacionada ao pagamento de aluguel e a contabilização dos valores do bem alugado.
* Arrendador: Deve ser incluído no cadastro de Cliente/Fornecedor um Arrendador, do tipo Fornecedor ou ambos, que será o "locador" do bem. Este Arrendador será  mesma pessoa relacionada ao pagamento do aluguel.

### **Processo**

* Cabeçalho

Os campos “Código do Tipo de contrato”,”Código de Status”, Arrendador e Arrendatário, devem ser preenchidos com os dados previamente cadastrados;

O campo Natureza de contrato deve ser preenchido com a opção “Arrendamento Mercantil;

Preencher as demais informações obrigatórias do contrato.

### Inclusão de Item de Contrato

Para os Contratos de natureza "**Arrendamento Mercantil**" e item cujo tipo de faturamento seja "**Periódico**", deverão ser cadastrados os campos abaixo:

* Produto: Deve ser informado o produto que será usado para os valores de arrendamento, ou seja, cadastrar um item especifico para esta finalidade;
* Valor Arrendamento: Valor total do contrato;
* Taxa de Juros: Juros aplicado ao arrendamento;
* Data Início;
* Data Fim;
* Condição de Pagamento a Prazo;
* Qte de Faturamentos.

Após informar os campos acima, o sistema calculará o Vlr. Presente e o Vlr. Parcela.

Vlr. Presente:

PV = FV / (1 + i) n

Parcela:

VP = FV /n

Onde:

PV = Valor presente

FV = Valor Futuro (Valor do arrendamento)

i = Taxa de Juros/100

n = Prazo

Após informar todos os campos, as parcelas serão calculadas automaticamente. Caso altere algum deles, as parcelas também serão recalculadas.

Após a inclusão do item “Período” deverá acessar ao Aba Parcelas para definir a **Data Fim Curto Prazo**, para que o sistema classifique as parcelas em curto e longo prazo, isso se faz necessário pois a regra contábil se diferencia para curto e longo prazo. Será detalhado melhor este processo na explicação de Classificação Contábil.

**Parcelas calculadas:**

**Regra de cálculo:**

* Valor Parcela: Vlr. Parcela.
* Valor Presente: Vlr. Presente da Parcela.
* Amortização Juros:  Saldo Devedor (Primeira Parcela = Valor Presente Total) \* (Taxa Juros / 100).
* Amortização Parcela: Valor Parcela - Amortização Juros;
* Saldo Devedor: Saldo Devedor (Primeira Parcela = Valor Presente Total) + Amortização Juros - Valor Parcela;

**Data da parcela:** Para calculo da data da parcela é levado em consideração parâmetros do contrato em conjunto com informações do item de contrato.

* **Primeira parcela:** Para calculo da data da primeira parcela é levado em consideração parâmetros do contrato em conjunto com informações do item de contrato.

**Primeiro passo:** Encontrar data de carência parametrizada, para isso é levado em consideração a data de inicio do contrato e as parametrizações de contrato e de integração;

**Parâmetros do contrato:** Ambiente | Gestão de Estoque, Compras e Faturamento | Contratos | Faturamento

* + - * Definições Fat de Contrato 1/3:  
        + **Dia de Termino da Carência:** Define o dia parcela a partir da data de inicio do contrato;
      * Definições Fat de Contrato 2/3:
        + **N°  de Meses da Carência:** Define a quantidade de meses de carência (soma a quantidade de meses a data de inicio do contrato);

**Parâmetros de Integrações:** Ambiente | Gestão de Estoque, Compras e Faturamento | Integrações | Financeira

* + - * Condição de pagamentos:
        + **Faturar com data do próximo mês:** Define se o faturamento será no próximo mês caso o dia de carência seja maior que o ultimo dia do mês. (dia de vencimento = 31, mês de fevereiro possui 28 dias, neste caso, a data será 03/3);

**Exemplo:**

Dia de inicio do contrato: 01/01/2000

Dia de término da Carência: 05

N° de Meses da Carência: 1

Faturar com data do próximo mês: não

**A** **data de carência será:** 05/02/2000

**Segundo passo:** Encontrar data de carência calculada, para isso é levado em consideração a data de inicio contrato e o campo Dias de Carência para Faturamento, informado na aba "Condições Gerais" no item de contrato;

Exemplo:

Dia de inicio do contrato: 01/01/2000

Dias de Carência para Faturamento: 10

**A data de carência será:** 11/01/2000

Após encontrar esta data de carência, é feito uma validação onde a data da primeira parcela, será a maior data de carência, neste caso, será **05/02/2000;**

**Terceiro passo:** Validar se o campo "Data de Carência"  informada na aba "Condições Gerais" no item de contrato é maior que a data da primeira parcela encontrada no passo anterior;

Exemplo:

Data de Carência: 01/02/2000

Como a data de carência informada no item de movimento é menor que a data de vencimento da parcela encontrada anteriormente, a data de primeiro vencimento será mantida, 05/02/2000;

**Quarto passo:** Verificar parâmetro do contrato "Vencimento em Dias Fixos" em conjunto com o campo "Dia do Faturamento"  informada na aba Condições Gerais do item de contrato);

**Parâmetros do contrato:** Ambiente | Gestão de Estoque, Compras e Faturamento | Contratos | Faturamento

* + - * Definições Fat de Contrato 2/3:  
        + **Vencimento em Dias Fixos:** Define o dia de vencimento de todas as parcelas;

Exemplo:

Dia primeira parcela: 05/02/2000 (data encontrada com base nos passos anteriores)

Dia do Faturamento: 3

Neste caso, como o dia de faturamento é menor que o dia da primeira parcela, a data da primeira parcela será ajustada para **03/03/2000**, caso fosse maior ou igual, a data da primeira parcela seria mantida. **05/02/2000.**

Caso não esteja parametrizado como "Vencimento em dias Fixos", a data da primeira parcela, será a data encontrada no passo anterior

**Demais Parcelas:** Para calculo das demais parcelas é feito validação a cerca do parâmetro do contrato "Vencimento em Dias Fixos, onde estando parametrizado para utilizar dias fixos, todas as parcelas sequentes terão o mesmo dia de vencimento, caso contrario, as parcelas serão acrescidas com base na condição de pagamento informada;

Para mais informações sobre o cadastro, acesse:

[Manutenção de Contratos - Linha RM - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=423938074)

2Previsão Financeira

### Inclusão de Previsão Financeira

O processo de **Inclusão de Previsão Financeira** irá gerar as previsões com base nas parcelas do arrendamento. Este processo é interessante utilizar principalmente para os contratos de longa duração, para que o sistema financeiro tenha todas as previsões a pagar, podendo alimentar o Fluxo de Caixa da empresa.

Deve-se marcar apenas 1 contrato e então clicar em Processos / Inclusão de Previsão Financeira.

Deve-se escolher o Tipo de Documento e a Contabilização sempre será do "Não Contábil".

Lançamentos financeiros gerados.

Após gerar a previsão, o status da previsão do item de contrato será alterado para "Gerou Previsão".

A partir deste momento, não será possível alterar as informações do item de contrato, apenas realizar reajustes de preços pelo rotina.

3Faturamento do Contrato

### Faturamento do Contrato de Arrendamento Mercantil

O Faturamento do Contrato poderá ser realizado de todas as parcelas ou parcialmente, geralmente as empresa optam em faturar as parcelas anualmente ou de acordo com o período de reajuste dos contratos.

Existem duas maneiras de faturar um contrato. Através da tela de manutenção de contratos ou pelo faturamento por lote.

No momento do faturamento do contrato pela tela de manutenção de contratos, é criado automaticamente um lote com as informações do contrato e posteriormente o faturamento do mesmo.

Para faturar pela tela de manutenção de contratos, basta selecionar o mesmo e ir em Processos / Faturamento Contrato.

Abrirá uma tela solicitando as informações do tipo de movimento de compra a ser criado.

Observação

O tipo de movimento que será faturado deverá estar parametrizado para Integração Contrato - Etapa 52 - Contratos.

Após a execução, o contrato será faturado para o tipo de movimento de compra selecionado.

Os faturamentos do contrato podem ser visualizados através do anexo "Visualizar Faturamentos".

Na tela abaixo podemos ver o lote que foi criado pelo faturamento.

Em seus Anexos também podemos ver os faturamentos, através do menu "Visualizar Faturamentos".

No cadastro manual de um Lote de Faturamento, quando selecionada a Natureza Contrato igual a "Arrendamento Mercantil", o tipos de faturamento permitido é: **Periódico**, assim como na inclusão de um item em um Contrato de mesma natureza.

Pelo Lote gerado podemos realizar 4 ações, que são:

* Faturamento Lote: Irá faturar os contratos de acordo com as informações do lote.
* Exclusão de Faturamento de Lote: Irá excluir todos os faturamentos vinculados a este lote.
* Cancelamento de Faturamento de Lote: Irá cancelar todos os faturamentos vinculados a este lote.
* Cópia de Lote de Faturamento: Irá gerar uma cópia do lote selecionado.

Ao realizar o faturamento, as parcelas de arrendamento mercantil tem seu status alterado para 'Faturada'. Caso seja feita exclusão ou cancelamento do lote faturado, o status das parcelas correspondentes volta a ser: 'A Faturar'.

Ao realizar o faturamento, o 'status faturamento' do item de contrato também é atualizado. Caso todas as parcelas foram faturadas o novo status será '**Faturado**', se apenas parte das parcelas forem faturadas, o status será: '**Parcialmente Faturado**' e, se ainda não foi faturado ou teve o faturamento excluído ou cancelado; o status será: '**A Faturar**'.

Foi criado o campo "Encargos" no item de movimento que receberá o valor da "Amortização Juros" da Parcela que foi faturada.

Este campo criado no item do movimento poderá ser utilizado para contabilizar os encargos mensalmente das parcelas do contrato, portanto o movimento que recebe o faturamento do contrato para o item periódico terá que ter um evento parametrizado conforme a regra contábil da empresa aplicada para esta contabilização.

Importante ressaltar que este campo não ajustará nos valores do tipo de movimento, ele tem única função de contabilização do juros mensalmente.

4Classificação Prazo das Parcelas

### Classificação Prazo das Parcelas (curto e longo prazo)

Ao informar a data final de curto prazo, o sistema irá calcular automaticamente a classificação do prazo das parcelas.

**Regra de cálculo:**

* Se a data de vencimento da parcela for menor do que a data fim de curto prazo, então será classificada como "Curto Prazo"; caso contrário será "Longo Prazo".
* Caso não seja informado a data fim de curto prazo, será classificado como "Nenhum".

### Reclassificação Contábil

É possível reclassificar as parcelas utilizando o processo de reclassificação contábil, esse processo permite incrementar a "Data Fim Curto Prazo", as parcelas "Longo Prazo" que ficarem anterior a nova data são reclassificadas para "Curto Prazo".

**Regra de cálculo:**

* A processo de reclassificação atua sobre o item de contrato sendo possível reclassificar itens separadamente.
* É necessário ser um contrato de arrendamento e ter feito o processo de classificação para utilizar a reclassificação.
* Um item de contrato que tenha todas suas parcelas em "Curto Prazo" deixa de ser listado no processo de reclassificação contábil.

O processo de **Reclassificação Contábil** pode ser chamado na visão do contrato com um ou vários contratos selecionados ou na edição contrato, em ambos os casos o processo vai listar os itens de contrato que pode realizar a reclassificação.

*Data Fim Curto Prazo*

* Deve-se escolher a quantidade de meses que a data fim curto prazo vai avançar.

* O parâmetro "Utilizar último dia do mês na "Data Fim Curto Prazo", deverá ser marcado quando se deseja que seja o ultimo dia do mês, caso este parâmetro esteja desmarcado o sistema utilizará o dia que esta sendo realizada a rotina, o mês/ano que será preenchido dependerá dos meses definidos no parâmetro anterior.

*Data de Contabilização*

O campo opcional "Data de Contabilização" é utilizado quando se deseja registrar uma data de contabilização da reclassificação diferente da atual.

*Log para simulação*

O parâmetro "Gerar somente LOG" simula todo o processo de reclassificação e retorna o LOG de reclassificação, no entanto sem afetar o sistema. Pode ser utilizado para fazer simulações e verificar como o processo vai afetar as parcelas e os valores.

Exemplo de LOG:

Observação:

A contabilidade relacionada a **Reclassificação Contábil** vai ser gerada de forma automática e sem intervenção do usuário, conforme regra contábil parametriza, ver item "Contabilização Contrato Arrendamento Mercantil" para mais detalhes do processo contábil.

8Contabilização Contrato Arrendamento Mercantil

Contabilização Contrato Arrendamento Mercantil

O processo de contabilização dos contratos de arrendamento mercantil será gerado nas seguintes situações:

 1) Inclusão do Contrato (A contabilização não é gerada automaticamente será necessário realizar processo de **Inclusão de Contabilidade**)

 2) Reclassificação da Parcela (transferência de curto para longo prazo) (Contabilização gerada automaticamente no momento da execução do processo **Reclassificação Contábil)**

 3) Reajuste do Contrato (Contabilização gerada automaticamente no momento da execução do processo **Reajuste de Preços**)

As situações descritas acima serão tratadas no processo de Contratos do módulo Gestão de Estoque, Compras e Faturamento.

Além das contabilizações relacionadas acima o processo de Arrendamento Mercantil poderá necessitar das contabilizações abaixo:

Encargos do Contrato

Sugerimos que seja tratada no evento contábil do tipo de movimento que foi faturado o item do contrato periódico do módulo Gestão de Estoque, Compras e Faturamento.

Pagamento das Parcelas dos Contratos

Será tratada no evento contábil de baixa do módulo Gestão Financeira.

Depreciação do Bem Direito de Uso

Será tratada no processo de depreciação mensal do módulo Gestão Patrimonial.

Inclusão de Contabilidade - (Contabilização da Implantação do Contrato)

Para geração da Contabilidade dos Itens do Contrato, foi criado um novo processo chamado "Inclusão de Contabilidade" para ser executado na visão do contrato.

Neste processo será exibido apenas os itens contratos do tipo Arrendamento Mercantil que ainda estão pendentes de contabilização.

Após selecionar os itens a contabilizar e executar o processo, a contabilidade será realizada.

Depois de gerado a contabilidade, o Status da Contabilidade do item de contrato será atualizado.

Uma das exigências para executar o processo com sucesso, independente de qual tabela será buscado o default contábil, é que no cadastro da Conta Contábil a opção de uso de Rateio esteja desabilitada, como indicado na imagem:

### Exclusão da Contabilidade

Para exclusão da Contabilidade dos Itens do Contrato, foi criado um novo processo chamado "Exclusão de Contabilidade" para ser executado na visão do contrato.

Neste processo será exibido apenas os itens contratos do tipo Arrendamento Mercantil que geraram contabilidade.

Após selecionar os itens e executar o processo, a contabilidade será excluída.

Depois de excluído a contabilidade, o Status da Contabilidade do item de contrato será atualizado.

### Estorno da Contabilidade

Para estorno da Contabilidade dos Itens do Contrato, foi criado um novo processo chamado "Estorno de Contabilidade" para ser executado na visão do contrato.

Neste processo será exibido apenas os itens de contrato do tipo Arrendamento Mercantil que geraram contabilidade.

Após selecionar os itens e executar o processo, a contabilidade será estornada.

* **Obs.**: Só será estornada a contabilidade quando a mesma estiver integrada ao Lote oficial da Contabilidade (ZERO). Caso contrário, ocorrerá uma exceção.

Depois de estornado a contabilidade, o Status da Contabilidade do item de contrato será atualizado.

Exclusão de Toda a Operação Contábil

Este processo solicitará ao Módulo Gestão Contábil a exclusão de toda a operação contábil dos itens selecionados. Para realizar a solicitação, foi criado um novo processo chamado "Solicitação de Exclusão de Toda Operação Contábil" para ser executado na visão do contrato.

Neste processo será exibido apenas os itens de contrato do tipo Arrendamento Mercantil que geraram contabilidade e foram estornados.

Após selecionar os itens e executar o processo, será gerada uma solicitação ao Contábil de exclusão de toda a contabilidade.

Após a execução desta tarefa no Contábil, será atualizado as informações contábeis do item de contrato.

10Edição da ContabilidadeEdição da Contabilidade

### Edição da Contabilidade

Permite editar a contabilidade do contrato

O parâmetro "Edição da Contabilização" controla o acesso tanto a edição quanto a permissão de "Refazer Cálculo da Contabilidade".

Observação:

Só será possível realizar este processo se o usuário tem liberação de acesso.

09Liberação de ContabilidadeLibera Contabilidade

### Liberação de Contabilidade

O processo de "Liberar Contabilidade" permite selecionar vários contratos e para cada item de contrato vai mostrar as contabilizações existentes e que podem ser liberadas.

A liberação da contabilidade escolhe entre excluir a contabilidade se ainda não foi integralizado ao lote zero ou estornar no caso da contabilidade ter sido integralizada ao lote zero.

A liberação da contabilidade também conta com alguns aceleradores, é possível expandir ou colapsar os itens, marcar todos ou desmarcar todos os itens.

11Reajuste de PreçosReajuste de Preços

### Reajuste de Preços de Contratos

O processo de reajuste de contratos de arrendamento será realizado através do processo "Reajuste de Preço" localizado em "Manutenção de contrato | Processos → Reajuste de Preço".

Como premissa, a fórmula de reajuste deve utilizar a função IUR ou IUR2, a única diferente entre elas é que na IUR2 o campo "Data do Reajuste" pode ser preenchido por uma função de fórmula ou com a data fixa como em IUR.

Na fórmula IUR ou IUR2 deve ser informando os seguintes parâmetros:

* Data do reajuste
* Índice base utilizado para o reajuste do contrato ("Obrigatório que seja utilizado um índice").
* Número de meses para o reajuste
* Defasagem da moeda
* Dia da cotação do índice base

Exemplos de fórmula:

* IUR ( ‘01/09/2010’, 'IPCA' , 6 , 0 , 11)
* IUR2 (HOJE , 'IGPM' , 3 , 0 , 1),
* IUR2 (DAT , 'IGPM' , 3 , 0 , 1),
* IUR2 ( ‘20/09/2017’, 'SELIC' , 6 , 0 , 11)

O processo irá reajustar as parcelas do item do contrato de acordo com os dados informados na fórmula e realizará a atualização do preço de arrendamento de acordo com os novos valores.

Atualização das parcelas:

Para cada parcela, as seguintes colunas serão atualizadas: Valor da parcela, Valor presente, Saldo devedor, Amortização do juros e Amortização da parcela.

O valor das parcelas é reajustada sempre a partir da data de reajuste do item.

As parcelas anteriores a data do reajuste são desconsideradas no reajuste.

As parcelas já faturadas não serão reajustadas.

#### Histórico de Reajustes:

Todos os reajustes realizados para cada item de contrato pode ser verificado na tela ‘Reajustes’ na aba de ‘Informações adicionais’ do item de contrato:

**Importante**: O campo "Data Último Reajuste" é preenchido automaticamente através do processo "Reajuste de Preço", e indica até onde o contrato já foi reajustado. No entanto esse campo também pode ser preenchido manualmente para desconsiderar reajuste até a data determinada ou para permitir novo reajuste em intervalo já reajustado.

**Observação**: Se o campo "Data Último Reajuste" for preenchido com a mesma data de reajuste do processo "Reajuste de Preço" nenhum reajuste vai ser efetivado.

### Desfazer reajuste de preços

Após realizar o reajuste é possível desfazer e retornar os itens de contrato a um estado anterior.

O processo Desfazer Reajuste de Preços será realizado através de processo em Manutenção de contrato | Processos → Desfazer Reajuste de Preços.

O processo deve receber como parâmetros a Moeda Índice (mesma informada na aba Informações adicionais | Reajuste), e a data do último reajuste realizado.

A data de reajuste deve ser a ultima data de reajuste realizado. Caso tenha sido realizado vários reajustes para o mesmo item, estes deverão ser desfeitos um a um na ordem inversa do reajuste.

Caso alguma parcela já tenha sido faturada após o reajuste, o processo não irá desfazer o reajuste da parcela faturada.

Ao término do processo o contrato vai ser afetado da seguinte forma:

* Histórico do reajuste será excluído.
* Data de último reajuste no item do contrato vai ser atualizada para data do último reajuste anterior ao desfeito ou a data vai ser elimina se não houver reajuste anterior.
* Atualização da previsão financeira das parcelas de arrendamento para os novos valores de parcela após desfazer o "Reajuste de Preço".
* A contabilidade relacionada ao "**Reajuste de Preço** " vai ser liberada de forma automática e sem intervenção do usuário.

5Parametrizações - Fórmulas

### **Funções de fórmulas a serem utilizadas no processo de Arrendamento Mercantil**

### **Contabilização Implantação do Contrato**

**Função de fórmula:**

**Nome da função:** SOMATABITMPARCELA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA.

**Sintaxe**:

A função de fórmula **SOMATABITMPARCELA**(STRING, STRING) exige dois parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas.

"VALORPARCELA" - Use para somar o valor das parcelas.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo.

"L" - Considera na soma as parcelas de longo prazo.

"T" - Considera na soma todas as parcelas, curto e longo prazo.

**Exemplo**:

SOMATABITMPARCELA('VALORPRESENTE', 'T')

Nesse caso a fórmula vai retornar a soma de VALOR PRESENTE de todas parcelas classificadas como Longo Prazo e Curto Prazo e o retorno é do tipo VALOR.

### **Contabilização das Parcelas Reclassificadas**

**Função de fórmula:**

**Nome da função:** SOMATABITMPARCELARECLASSIFICADA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELARECLASSIFICADA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo reclassificadas.

**Sintaxe**:

A função de fórmula **SOMATABITMPARCELARECLASSIFICADA**(STRING, DATA) exige um parâmetro do tipo string:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas.

"VALORPARCELA" - Use para somar o valor das parcelas.

**Exemplo**:

SOMATABITMPARCELARECLASSIFICADA('VALORPRESENTE',)

Nesse caso a fórmula vai retornar a soma de VALOR PRESENTE de todas parcelas classificadas entre a data de curto prazo e a data atual.

Ponto de Atenção: As fórmulas não  podem ser testadas através do executo de fórmulas da MDI, pois precisam do contexto de execução do processo.

### **Contabilização das Parcelas Reajustadas**

**Função de fórmula:**

**Nome da função:** SOMATABITMPARCELAREAJUSTADA:

**Contexto exigido**: O uso da função de fórmula "SOMATABITMPARCELAREAJUSTADA" exige o identificador do contrato e do item do contrato, campos ] 

**Retorno**: Retorna a soma dos valores da tabela TITMCNTPARCELA, considerando apenas parcelas que estão sendo Reajustadas.

**Sintaxe**:

A função de fórmula **SOMATABITMPARCELAREAJUSTADA**(STRING,  STRING) exige três parâmetros do tipo string, são eles:

<**Parâmetro 1**>

"VALORPRESENTE" - Use para somar o valor presente das parcelas.

"AMORTIZACAOJUROS" - Use para somar o valor de amortização das parcelas.

"VALORPARCELA" - Use para somar o valor das parcelas.

<**Parâmetro 2**>  

"C" - Considera na soma as parcelas de curto prazo.

"L" - Considera na soma as parcelas de longo prazo.

"T" - Considera na soma todas as parcelas, curto e longo prazo.

**Exemplo**:

SOMATABITMPARCELAREAJUSTADA('VALORPARCELA', 'T')

Nesse caso a fórmula vai retornar a soma de VALOR PARCELA de todas parcelas reajustadas.

Ponto de Atenção: As fórmulas não  podem ser testadas  através do executo de fórmulas da MDI, pois precisam do contexto de execução do processo.

6Parametrizações - Evento Contábil

### Cadastro de Evento Contábil

Caminho de Acesso: BackOffice > Gestão de Estoque, Compras e Faturamento > Cadastro > Eventos Contábeis (*Dentro do grupo contábeis*).

Para contabilização do Contrato de Arrendamento Mercantil, foi criada uma nova opção de "Processo" no cadastro de Eventos Contábeis.

Para este novo Processo, nas caixas de seleção de: "Buscar Filial/Depto em" e "Buscar Centro de Custo em", é apresentadas a opção de "Item de Contrato".

No cadastro do Item do Evento Contábil, em "Aplicar" é apresentada a opção: "Item de Contrato" .

Para ambas as opções selecionadas, serão apresentadas no campo "Busca default em", os itens:

* Produto - Cliente/Fornecedor - Centro de Custo - Tabelas de Classificação do Produto (05 opções possíveis presentes no parâmetros do sistema)

Observações:

1) Quando for utilizado buscar default em uma Tabela de Classificação a regra de preenchimento das contas contábeis buscará  primeiro na classificação contábil vinculada no item do contrato, caso não seja atendido buscará  na classificação do produto que esta vinculado no item do contrato.

2) Os mnemônicos que podem ser utilizados nos complementos dos históricos nos eventos contábeis são:

| Mnemônico | Descrição |
| --- | --- |
| CCF | Código do Fornecedor |
| NOM | Nome Fantasia do Fornecedor |
| FAN | Nome Fantasia do Fornecedor |
| RAZ | Razão Social do Fornecedor |
| COD | Código do Contrato |
| HIS | Histórico do Contrato |
| CTR | Nome do Contrato |
| DCTR | Data do Contrato |
| OBS | Observação do Contrato |

7Parâmetros - Contratos Contabilidade

### Parâmetros Contábeis do Contrato

Nos parâmetros do contrato, foi criado os dados de Contabilidade:

**Habilita Evento Contábil:**

* Não Usa evento.
* Usa Evento: Por esta opção o evento contábil será buscado diretamente no parâmetro **Evento Default** do item de contrato.

**Edição da Contabilização:**

* Edita: O sistema dará acesso à contabilização do contrato e o usuário poderá efetuar qualquer alteração que for necessária.
* Mostra: A contabilização somente será mostrada ao usuário sem que seja possível a alteração na mesma.

**Contabilização Obrigatória:**Marcando esta opção o contrato de Arredamento Mercantil só poderá ser salvo após serem indicados os eventos contábeis.

* ***Observação**:*Se o campo acima estiver marcado, não será permitida exclusão da contabilidade do movimento.

**Evento Default Item de Contrato:**Informe qual evento contábil para ser utilizado no item de contrato. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil do Item de Contrato:**Informe qual o código do lote contábil.

**Código do Lote para Estorno do Item de Contrato:**Informe neste campo o código do lote contábil que guardará os lançamentos estornados do item de contrato.

**Evento Default Reclassificação Contábil:**Informe qual evento contábil para ser utilizado para reclassificação contábil. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil Reclassificação Contábil:**Informe qual o código do lote contábil.

**Código do Lote para Estorno Reclassificação Contábil:**Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reclassificação.

**Evento Default Reajuste do Contrato:**Informe qual evento contábil para ser utilizado no reajuste do contrato. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil Reajuste do Contrato:**Informe qual o código do lote contábil.

**Código do Lote para Estorno Reajuste do Contrato:**Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reajuste do contrato.

* ***Observação**:*Para cada um dos códigos de Lote definidos, caso o mesmo já possua registro na base de dados (chave composta pelo código da coligada + código do lote, da tabela de lotes do Contábil), será definido para este item em específico. Caso contrário, será criado um novo Lote com o código inserido nos respectivos campos e nomenclatura conforme funcionalidade à qual o item está destinado.

7Integração Gestão Patrimonial

### Integração item do contrato com o Módulo Gestão Patrimonial

Os itens do contratos poderão ser inseridos no módulo gestão patrimonial através do processo .

## Webinar TOTVS | IFRS 16 - Contrato de Arrendamento Mercantil
