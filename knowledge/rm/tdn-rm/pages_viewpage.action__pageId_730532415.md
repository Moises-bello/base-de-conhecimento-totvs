---
content_hash: 8ff760f9e56bd161ea0bf58589e05f57bddc792d86a52aeeeda9eb3a40e8a433
fetched_at: '2026-06-29T00:11:28.178593+00:00'
page_id: '730532415'
product: rm
source: tdn-rm
title: Cópia de DT Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=730532415
version: 1
---

# Desconto por Antecipação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional.* |
| **Módulo:** | **TOTVS Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro* | *Desconto por Antecipação* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Geração de Lançamento Financeiro** | *Geração de Lançamento Financeiro.* | | **Baixa de Lançamento Financeiro** | **Baixa de Lançamento Financeiro** | | **Serviços Educacionais** | **Serviços** | |
| **Cadastros Iniciais:** | *N/\A.* |
| **Parâmetro(s):** | *N/A.* |
| **Ponto de Entrada:** | *N/A.* |
| **Tickets relacionados** | *N/A.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUINTEGRACOES-1087 |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *N/A.* |
| **Tabelas Utilizadas:** | *FAgrupaDescontoPontual, FDescontoPontual.* |
| **Sistema(s) Operacional(is):** | *N/A.* |

## Descrição

Com o objetivo de flexibilizar a configuração de descontos para serem concedidos pela Instituição de Ensino aos alunos que efetuarem pagamento antecipado dos lançamentos financeiros provenientes do Educacional, foi liberado o cadastro de ‘Desconto por Antecipação’ no Educacional juntamente com o cadastro dos Itens de desconto por antecipação.

Desconto por AntecipaçãotrueCadastrosCadastrosCadastrosDescAntCadastro do Desconto por AntecipaçãoDesconto por Antecipação

## Cadastro do Desconto por Antecipação

No módulo Educacional o cadastro está disponível no menu "Financeiro / Contábil → Geração → Financeiro → Desconto por Antecipação"

O desconto por antecipação tem os seguintes campos:

* Código: Informa o código do desconto por antecipação, e é inserido automaticamente pelo sistema.
* Descrição: Informa a descrição do desconto por antecipação.
* Período de Vigência: Informa o período de vigência do desconto por antecipação, porém esse período é opcional.   
  Pode ser informada somente a data de início ou a data final de vigência. Caso não seja informado, o desconto por antecipação sempre será válido.  
  + Data Início de Vigência: Informa a data inicial de vigência do desconto por antecipação.
  + Data Final de Vigência: Informa a data final de vigência do desconto por antecipação.

Quando o cliente informa um período de vigência no cadastro do desconto por antecipação, essa data é validada no momento da baixa do lançamento, exemplo abaixo:

* Cadastro do desconto por antecipação: Data inicio de vigência: 01/01/2020 — Data final de vigência: 31/06/2020
* Parcela com data de vencimento 15/01/2020

No momento de baixar informo a data 15/12/2016 (data anterior ao período de vigência), nesse caso o desconto não será aplicado.   
Só é considerado o desconto que esteja compreendido dentro do período de vigência no cadastro do desconto por antecipação. 

Pensando no cenário acima foi implementado o parâmetro "Considerar a data de vencimento do lançamento na regra de validação da vigência" **(****Configurações | Parâmetros| Integração| Financeiro | Conta a receber | Baixas | Manutenção  de baixas | Desconto por Antecipação), [clique aqui.](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)**

Para que o parâmetro seja reconhecido na base siga os passos abaixo:

Com esse parâmetro marcado ao realizar uma baixa com data de vencimento inferior a vigência do cadastro do desconto por antecipação, esse desconto será aplicado.   
Será validado a data de vencimento do lançamento e não a data de baixa, então se a data de vencimento do lançamento estiver compreendida dentro da vigência será aplicado o desconto.

Desconto por Antecipação com período de vigência.

Desconto por Antecipação sem período de vigência.

(Permissão no perfil do usuário)

Cadastro do Item do Desconto por AntecipaçãoItem do Desconto por Antecipação

## Cadastro do Item do Desconto por Antecipação

O desconto por antecipação poderá ter um ou vários itens do desconto por antecipação. O item do desconto por antecipação informará as regras de aplicação do desconto por antecipação juntamente com o valor ou percentual do desconto. O item do desconto por antecipação é acessado via anexo "Item do Desconto por Antecipação" presente no cadastro do desconto por antecipação.

O item do desconto por antecipação tem os seguintes campos:

* Código: Informa o código do item do desconto por antecipação, e é inserido automaticamente pelo sistema.
* Desconto por Antecipação: Informa o desconto por antecipação ao qual o item pertence, e é inserido automaticamente pelo sistema.
* Descrição: Informa a descrição do item do desconto por antecipação.
* Tipo de Desconto: Informa se o desconto será um valor ou um percentual sobre o valor original do lançamento.
* Tipo Limite Desconto: Informa o tipo de limite de aplicação do desconto. O tipo limite pode ser:
  + Dia Fixo:  Informa o dia fixo de limite que será utilizado para calcular a data limite do item de desconto que considerará esse dia limite / mês da data de vencimento / ano da data de vencimento. Se o dia fixo for maior do que o último dia do mês, esse último dia do mês é que será considerado.
  + Dia Útil: Informa o dia útil do mês da data de vencimento que será utilizado para calcular a data limite do item de desconto. A data calculada será <dia útil calculado> / <mês da data de vencimento> / <ano da data de vencimento>. Se o dia útil calculado for maior do que o último dia do mês, esse último dia do mês é que será considerado. O sistema considerará o calendário setado na filial do lançamento. Caso não exista calendário setado na filial, o sistema irá verificar nos parâmetros do Totvs Gestão Financeira parâmetro: "Calendário Oficial → Calendário Oficial"
* Valor do Desconto: Informa o valor ou percentual do desconto por antecipação a ser aplicado conforme configuração no campo "Tipo de Desconto".
* Dia Útil/Dia Fixo: Informa a quantidade de dias fixos ou dias úteis a ser aplicada no desconto conforme configuração do campo "Tipo Limite Desconto".

Item do Desconto por Antecipação por dia limite.

AssociaçõesAssociaçõesAssociaçõesDescAntAssociação do Desconto por AntecipaçãoAssociação do Desconto por Antecipação

## Associação do Desconto por Antecipação

O desconto por antecipação pode ser associado à matriz aplicada, campus/polo **da matriz aplicada** ou contrato do aluno da Instituição de Ensino.

1. Desconto por antecipação associado à matriz aplicada:  Será disponibilizado o anexo "Desconto por antecipação por matriz aplicada" na matriz aplicada e permissões conforme telas abaixo:  
   (Anexo)  
     
   (Permissão no perfil do usuário)
2. Desconto por antecipação associado ao campus/polo da matriz aplicada somente no ensino superior: Será disponibilizado o anexo "Desconto por antecipação por campus/polo da matriz aplicada" (**válido somente para o ensino superior**) no cadastro de campus/polo da matriz aplicada e permissões conforme telas abaixo:  
   (Anexo)  
     
   (Permissão no perfil do usuário)

   IMPORTANTE

   O campus/polo a ser considerado para cálculo do valor do desconto por antecipação será o campus/polo "Ativo" vinculado ao curso do aluno (Cursos/Habilitações)
3. Desconto por antecipação associado ao contrato do aluno: Será disponibilizado o anexo "Desconto por antecipação por contrato" na cadastro de contratos e permissões conforme telas abaixo:  
   (Anexo)  
     
     
   (Permissão no perfil do usuário)
4. Criação do processo para a associação de descontos por antecipação a múltiplas matrizes aplicadas e a múltiplos campus/polos de matrizes aplicadas.   
   Mais informações sobre o processo podem ser visualizadas no seguinte documento: [Desconto por antecipação - Associar descontos por antecipação para matrizes aplicadas ou campus/polos da matriz aplicada](http://tdn.totvs.com/pages/viewpage.action?pageId=330836967)

Importante:

Cada associação de desconto por antecipação a algum item: matriz aplicada, campus/polo ou contrato do aluno, validará a vigência do desconto por antecipação que está sendo associado. Não serão permitidas inclusões de descontos por antecipações com vigências sobrepostas.

Exemplo:

       (Associação inválida  - Vigências sobrepostas em 01/2017)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

       (Associação válida  - Vigências não sobrepostas)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

Essa validação foi implementada tanto na associação dos descontos por antecipação, quanto na alteração da vigência de qualquer desconto por antecipação já associado.

Bolsa Condicionada ao Desconto por AntecipaçãoBolsa Condicionada ao Desconto por Antecipaçãobolsacondicionadaaodescontoporantecipacao

## **Bolsa Condicionada ao Desconto por Antecipação**

Com desconto por antecipação da bolsa você tem a possibilidade de informar se a bolsa condicional será ou não aplicada de acordo com a data limite dos itens de desconto.

O cadastro do desconto por antecipação associado à bolsa estará disponível no anexo "Desconto por antecipação da bolsa" no cadastro de bolsa.

 (Importante lembrar de habilitar a permissão no perfil do usuário)

IMPORTANTE

* Só será permitido cadastrar os descontos por antecipação da bolsa caso o parâmetro do educacional 'Mantém fórmula default para valor opcional / integração de bolsas condicionais' esteja marcado e a bolsa seja do tipo condicional.
* Não será possível alterar o tipo de bolsa para incondicional caso essa bolsa já tenha descontos por antecipação cadastrados.
* O menu "Desconto por antecipação da bolsa" disponível no anexo do cadastro de bolsa somente ficará habilitado se a bolsa selecionada for uma bolsa condicional.

**Regras para processamento**

Caso tenha um item de [d](http://tdn.totvs.com/pages/viewpage.action?pageId=325847718)esconto por antecipação associado à bolsa condicional, significa que o aluno somente terá direito à bolsa se o pagamento for realizado até a data limite do item do desconto por antecipação vinculado à bolsa, ou seja, a bolsa passa a ser condicionada ao pagamento do desconto por antecipação estipulado.

Exemplo:

Bolsa "Você Merece": 10%, vinculada ao desconto por antecipação "Pagamento até o dia 10, ganha 10%".

O Aluno somente irá ganhar os 10% de bolsa se realizar o pagamento até o dia 10 do vencimento do boleto.

Observação:

Caso não tenha nenhum desconto por antecipação associado à bolsa, a regra de processamento da bolsa não é alterada, ou seja, ao processar o valor da bolsa o sistema não realizará nenhuma validação com relação ao desconto por antecipação.

Em quais processos o sistema aplicará a regra?

**- Geração de lançamento**

Durante a geração de lançamento, caso seja identificado descontos por antecipação para o aluno, o mesmo será processado já identificando os valores de pagamento para cada vencimento do desconto por antecipação. O valor para pagamento apresentado já considerará a perda da bolsa, caso a bolsa esteja condicionada a um desconto por antecipação.

**- Simulação de Parcela**

Na visão de parcela é possível selecionar a parcela e realizar a simulação dos valores, neste momento o sistema também apresentará colunas demonstrando os valores para pagamento conforme cada vencimento do desconto por antecipação. O valor para pagamento apresentado já considerará a perda da bolsa, caso a bolsa esteja condicionada a um desconto por antecipação.

**- Baixa de Lançamento**

Para que o sistema considere a perda da bolsa que está condicionada a um desconto por antecipação, durante a baixa do lançamento será necessário utilizar na fórmula uma função de fórmula que calcule o valor da bolsa considerando a data da baixa, pois somente durante a baixa do lançamento é que saberemos qual é o desconto por antecipação ao qual o aluno terá direito e se o mesmo dará direito à bolsa.

Importante:

Para utilizar o recurso de perda da bolsa condicionada conforme o desconto por antecipação, o valor da bolsa condicional deverá sempre ser processado por fórmula .

*Veja neste documento na parte de “Lançamento Financeiro / Baixa do Lançamento Financeiro”* *e* *“Fórm**ula /**Fórmula Valor de Bolsa Condicional Conforme Desconto Por Antecipação**"* *c**omo utilizar este recurso.*

---

## **Processo de associação de desconto por antecipação à bolsas condicionaisassistentedescontobolsa**

Este processo visa facilitar a associação de descontos por antecipação à bolsas condicionais a fim de que essas bolsas sejam válidas até um vencimento específico conforme descrito previamente no tópico **Bolsa Condicionada ao Desconto por Antecipação**.

O mesmo se encontrará em processos da visão de bolsas conforme abaixo:

Somente bolsas "**CONDICIONAIS**" poderão ser selecionadas para processamento. Caso seja selecionada alguma bolsa "**INCONDICIONAL**", o sistema exibirá uma mensagem para o usuário e não permitirá prosseguir conforme abaixo:

O processo também só estará visível, se o parâmetro de sistema "***Mantem fórmula default para valor opcional / integração de bolsas condicionais***" estiver marcado

São três status possíveis para os registros de associação do processo:

1. **Banco de dados**: Indica que a associação entre o desconto por antecipação e a bolsa já existe no banco de dados. Esse registro permanecerá inalterado na execução do processo.
2. **Inclusão**: Indica que a associação entre o desconto por antecipação e a bolsa será incluída no banco de dados após execução do processo. Somente terão esse status, os registros que não existiam no banco de dados. Caso a associação do desconto já exista para alguma bolsa, o sistema não adicionará nenhuma linha na grid de associação.
3. **Exclusão**: Indica que a associação entre o desconto por antecipação e a bolsa será excluída no banco de dados após execução do processo. Somente os registros carregados do banco de dados terão esse status. Caso o usuário tenha incluído no processo uma associação que não existia previamente no banco de dados, o respectivo registro será excluído da grid de associações.

Segue abaixo a tela do processo:

Após execução do processo, o sistema exibirá um log com todas as inclusões e exclusões feitas conforme abaixo:

ConsiderarConsiderar Desconto por AntecipaçãoConsiderarDescAntConsiderar Desconto por Antecipação no ServiçoServiço

**Considerar Desconto por Antecipação no Serviço**

Para que o desconto por antecipação seja considerado, o 'serviço' deverá ser configurado para considerar o desconto por antecipação através do campo "Considera desconto por antecipação".

Importante

Para que um desconto por antecipação seja considerado na geração de lançamentos, os campos "Considera desconto por antecipação" deverão estar marcados no contrato e no serviço. Caso não esteja marcado em algum desses lugares, o desconto por antecipação será desconsiderado.

consideradescantecipcontratoContratoIndica se o contrato irá considerar ou desconsiderar o desconto por antecipação

**Desconto por Antecipação no Contrato**

**=> Considerar desconto por antecipação**

Para que o desconto por antecipação seja considerado, o 'contrato' deverá ser configurado para considerar o desconto por antecipação através do campo "Considera desconto por antecipação".

Importante

Para que um desconto por antecipação seja considerado na geração de lançamentos, os campos "Considera desconto por antecipação" deverão estar marcados no contrato e no serviço. Caso não esteja marcado em algum desses lugares, o desconto por antecipação será desconsiderado.

**=> Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)**

Quando o sistema estiver parametrizado para que a aplicação de Bolsa seja por contrato (Educacional >> Integração >> Financeiro >> Educacional >> Fin – Geral 2/4), e o tipo de classificação do contrato, seja igual a,“Somar Bolsa” ou “Maior Bolsa”, será disponibilizada no contrato a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”.***

Aviso

A opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”*** ficará disponível somente se o sistema estiver parametrizado para que a aplicação de bolsa seja por contrato.

**Calculo da bolsa:**

Considerando o tipo de bolsa “Somar” ou “Maior Bolsa”, por padrão ao calcular o valor de uma bolsa o sistema considera como valor base o valor da parcela.

Exemplo:

Valor da parcela:1000,00 | Desconto por antecipação: 10% (100,00) | Bolsa: 20% (200,00).

Caso a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)***” esteja marcada, o valor base para o cálculo da bolsa levara em consideração o valor do desconto por antecipação.

Exemplo:

Valor da parcela:1000,00 | Desconto por antecipação: 10% (100,00) | Bolsa: 20% (180,00).

O valor base será: valor da parcela (1000,00) – desconto por antecipação (100) = 900,00

Novos contratos

Sempre ao incluir um novo contrato a opção “***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”*** será preenchida conforme o parâmetro “Considerar desconto por antecipação para Somar Bolsa” ou “Considerar desconto por antecipação para Maior Bolsa”, disponível em Educacional >> Integrações >> Financeiro >> Educacional >> Fin-Geral 2/4, estes parâmetros tem a função de indicar o comportamento padrão para os contratos.

CalculosRegras de CálculosCalculosDescAntRegra de cálculo do desconto por antecipaçãoRegra de cálculo do desconto por antecipação

## Regra de cálculo do desconto por antecipação

Somente serão considerados os lançamentos do Educacional que estão sendo gerados ou lançamentos já gerados e não vencidos com status "Em Aberto".

Sistema buscará descontos por antecipação no Educacional na seguinte ordem de prioridade:

1. Descontos por antecipação no contrato
2. Descontos por antecipação no campus/polo da matriz aplicada (Anexo da matriz aplicada)
3. Matriz aplicada

Se o sistema encontrar descontos por antecipação em qualquer entidade citada acima (contrato / campus\_polo / matriz aplicada) obedecendo a ordem de prioridade, essa entidade é que será considerada para o cálculo não havendo buscas em outra entidade.

    Exemplo:

- Se houver um desconto por antecipação cadastrado no contrato do aluno, mesmo que o valor do desconto calculado seja zero, o sistema não buscará descontos por antecipação no campus/polo da matriz aplicada ou na matriz aplicada.  
- Se não houver um desconto por antecipação cadastrado no contrato, o sistema busca no campus/polo da matriz aplicada e, somente se não encontrar registros no campus/polo e que o sistema buscará descontos por antecipação cadastrados na matriz aplicada.

O sistema considerará o valor original do lançamento como valor base para o cálculo. 

Sistema considerará as vigências cadastradas nos descontos por antecipação. Os campos "Data início de vigência" e "Data final de vigência" definirão um período válido para a escolha do desconto por antecipação a ser utilizado. Somente terão desconto por antecipação os lançamentos financeiros cuja as parcelas do contrato estejam dentro da vigência de um desconto por antecipação. O que define se uma parcela está compreendida dentro da vigência de um desconto é a data da baixa do lançamento. Os campos de vigência podem aceitar o valor nulo indicando que, caso esse campo seja nulo, o mesmo sempre será válido, ou seja, caso seja a data início de vigência nula, todas as datas a serem comparadas com ela serão maiores que a mesma, da mesma forma que, caso o campo data final de vigência seja nulo, todas as datas a serem comparadas com ela serão menores.

Seguem abaixo alguns exemplos:

a) Desconto com data de início e data final de vigência preenchidas

* + Data início de vigência: 01/01/2018
  + Data final de vigência : 31/01/2018  
    => Significa que o desconto por antecipação só será aplicado se a data da baixa do lançamento estiver dentro do período de vigência explicitamente especificado.

b) Desconto com data de início nula e data final de vigência preenchida

* + Data início de vigência: NULA
  + Data final de vigência : 31/01/2018  
    => Significa que o desconto por antecipação só será aplicado se a data da baixa do lançamento for menor ou igual à data final de vigência

        c) Desconto com data de início preenchida e data final de vigência nula

* + Data início de vigência: 01/01/2018
  + Data final de vigência : NULA  
    => Significa que o desconto por antecipação só será aplicado se a data da baixa do lançamento for maior ou igual à data inicial de vigência

        d) Desconto com data de início e data final de vigência nulas

* + Data início de vigência: NULA
  + Data final de vigência :  NULA  
    => Significa que o desconto por antecipação será válido para qualquer data da baixa do lançamento

A data da data da baixa do lançamento é utilizada para se definir a qual desconto por antecipação (agrupamento de itens de descontos) que o lançamento financeiro estará associado, conforme a vigência do desconto por antecipação. Uma vez o lançamento financeiro gerado e associado ao desconto por antecipação, o item de desconto considerado irá variar conforme a data da baixa, em caso de baixa do lançamento, ou conforme a data do valor líquido, em caso do cálculo do valor líquido.   

Quando o cliente informa um período de vigência no cadastro do desconto por antecipação, essa data é validada no momento da baixa do lançamento, exemplo abaixo:

* Cadastro do desconto por antecipação: Data inicio de vigência: 01/01/2020 — Data final de vigência: 31/06/2020
* Parcela com data de vencimento 15/01/2020

No momento de baixar informo a data 15/12/2016 (data anterior ao período de vigência), nesse caso o desconto não será aplicado.   
Só é considerado o desconto que esteja compreendido dentro do período de vigência no cadastro do desconto por antecipação. 

Pensando no cenário acima foi implementado o parâmetro "Considerar a data de vencimento do lançamento na regra de validação da vigência" **(****Configurações | Parâmetros| Integração| Financeiro | Conta a receber | Baixas | Manutenção  de baixas | Desconto por Antecipação), [clique aqui.](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)**

Com esse parâmetro marcado ao realizar uma baixa com data de vencimento inferior a vigência do cadastro do desconto por antecipação, esse desconto será aplicado.   
Será validado a data de vencimento do lançamento e não a data de baixa, então se a data de vencimento do lançamento estiver compreendida dentro da vigência será aplicado o desconto.

**Cálculo dos valores dos itens de desconto**

Após a seleção do desconto por antecipação a ser utilizado serão verificados os itens de descontos a serem utilizados.

Os itens de desconto a serem verificados dependerão do processo que estará calculando o valor do desconto por antecipação pois o processo poderá considerar todos os itens de desconto independente do dia limite (Ex.: Geração de lançamentos do Educacional) ou poderá considerar apenas o item de desconto com a menor data limite calculada entre os itens de desconto cujo valor é maior ou igual à data base a ser considerada. (Ex.: Baixa de lançamentos e Valor líquido)

Para se fazer a comparação com a data base a ser utilizada, o dia (fixo ou útil) configurado no item de desconto será transformado internamente em uma data limite calculada no seguinte formato: (<dia do item de desconto calculado> / <mês da data de vencimento do lançamento> / <ano da data de vencimento do lançamento>)

Os itens serão ordenados pela data limite calculada e o desconto será concedido sempre para a menor data limite calculada maior ou igual à data do processo que está sendo considerado.

Se a data base para o cálculo for maior que a data limite do item de desconto de maior valor, devemos calcular o item de desconto cuja data limite calculada seja maior ou igual à data base. Se a data base para o cálculo for menor ou igual à data limite do item de desconto de maior valor, o valor do desconto resultante assumirá o maior de desconto calculado.

Caso sejam selecionados dois descontos com o mesmo dia de vencimento calculado, o sistema considerará o maior valor de desconto calculado.

**Dia do item de desconto calculado**

Se o item estiver parametrizado para "**Dia fixo**", será verificado se o dia informado é maior do que o último dia do mês da data de vencimento. Caso o dia informado seja maior, a data limite calculada considerará o último dia do mês da data de vencimento.

    Exemplos:

    a) Dia **fixo** informado MENOR OU IGUAL ao último dia do mês

* Dia informado no item de desconto  : 25
* Data de vencimento do lançamento   :    
  => Data limite calculada para o item :

    b) Dia **fixo** informado MAIOR que o último dia do mês

* Dia informado no item de desconto  : 31
* Data de vencimento do lançamento   :    
  => Data limite calculada para o item :  (última data válida do mês)

     c) Dia **fixo** informado é o ULTIMO ou PENÚLTIMO dia do mês e não é dia útil

* Dia informado no item de desconto: 31
* Data de vencimento do lançamento:     
  => Data limite calculada para o item :  (próximo dia útil)

Se o item estiver parametrizado para "**Dia útil**", o mesmo será calculado conforme os dias úteis do mês da data de vencimento. Será verificado se o dia útil calculado é maior que o último dia do mês da data de vencimento. Caso o dia seja maior, a data limite calculada considerará o último dia do mês da data de vencimento.

    Exemplos:

    a) Dia **útil** calculado MENOR OU IGUAL ao último dia do mês:

* Parâmetro "Considerar sábado como dia útil" desmarcado.
* Dia informado no item de desconto  : 5 (quinto dia útil)
* Data de vencimento do lançamento :    
  => Data limite calculada para o item :

    b) Dia **útil** calculado MAIOR que o último dia do mês:

* Parâmetro "Considerar sábado como dia útil" desmarcado.
* Dia informado no item de desconto  : 25 (vigésimo quinto dia útil)
* Data de vencimento do lançamento  :    
  => Data limite calculada para o item :  (última data válida do mês)

Para cálculo dos dias úteis, o sistema considerará o calendário especificado na filial do lançamento.

Caso não tenha calendário especificado na filial, o sistema buscará o calendário oficial parametrizado no Totvs Gestão Financeira (Parâmetro "Calendário Oficial -> Calendário Oficial") e considerará sábado como dia útil se o parâmetro "Calendário Oficial -> Considerar sábado como dia útil" estiver marcado.

**Valor calculado para o item de desconto**

O valor calculado dependerá do tipo de desconto setado no item de desconto.

Os valores de tipos de desconto poderão ser:

* "**Valor**": Indica que o valor informado é um valor fixo. Caso o valor informado seja maior do que o valor original do lançamento, o valor calculado para o desconto por antecipação será igual ao valor original do lançamento.
* "**Percentual**": Indica que o valor informado trata-se de um percentual sobre o valor original do lançamento.
Cálculo dos valores de bolsas Cálculo dos valores de bolsas 

## Cálculo dos valores de bolsas

O desconto por antecipação influenciará no valor calculado para as bolsas de tipo "**Aplicar bolsas em cascata**" por padrão (seja a bolsa por contrato ou bolsa por classificação) ou para bolsa "**Exclusiva**" (para bolsas por classificação).

**Somar Bolsas e Aplicar somente a maior bolsa**

Caso o sistema esteja parametrizado com aplicação de bolsa por "**Contrato**", serão habilitados os parâmetros abaixo localizados em **Fin - Geral 2/4**:

* "Considerar desconto por antecipação para Somar Bolsas": Indicará que o desconto por antecipação deverá ser subtraído do valor original para cálculo do valor base que será utilizado no cálculo dos valores de bolsas quando o tipo de bolsa informado no contrato for "**Somar Bolsas**".
* "Considerar desconto por antecipação para Maior Bolsa": Indicará que o desconto por antecipação deverá ser subtraído do valor original para cálculo do valor base que será utilizado no cálculo dos valores de bolsas quando o tipo de bolsa informado no contrato for "**Aplicar somente a maior bolsa**".

Importante

As opções acima tem como objetivo definir o comportamento padrão para todos os contrato que serão criados com a classificação "Somar Bolsas" ou "Maior Bolsa", caso as opções acima esteja marcada a opção "***Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s)”*** disponível no contrato também será marcada na inclusão de um novo contrato.

As opções acima só definem o comportamento padrão que o contrato deve assumir ao ser cadastrado, o comportamento do cálculo sempre respeitará a opção definida no cadastro.

Para os tipos de bolsa "**Aplicar bolsas em cascata**" e para bolsa "**Exclusiva**", o valor base será calculado da seguinte forma:

Valor base = (Valor original - Valor de desconto da parcela - Valor de desconto por antecipação)

Caso o tipo de bolsa seja "**Somar Bolsas**" ou "**Aplicar somente a maior bolsa**" e o respectivo parâmetro para considerar valor do desconto por antecipação estiver marcado, o valor base será calculado da seguinte forma:

Valor base = (Valor original - Valor de desconto por antecipação)

Caso o sistema esteja parametrizado para **NÃO** considerar o desconto por antecipação (parâmetro desmarcado) nos dois casos citados acima, o valor base será o valor original da parcela.

O valor base será igual a zero caso o valor calculado seja negativo.

 Exemplos Geração de Lançamentos com Desconto Antecipação, [Clique Aqui.](http://tdn.totvs.com/pages/viewpage.action?pageId=331852043)

**Gravação dos Itens de Descontos processados pelo Lançamento**

Durante a geração ou regeração de lançamento o sistema irá gravar na tabela SLANDESCPONTUAL todos os itens de desconto processados para o aluno, já com as informações de data de pagamento, valor do desconto, valor de pagamento e valores de bolsa.

Estas informações poderão ser consultadas no anexo “Desconto por antecipação da parcela” disponível no cadastro de Parcela ou no menu principal em Educacional >> Financeiro/Contábil >> Financeiro >> Descontos por Antecipação das Parcelas / Lançamentos.

IMPORTANTE

O valor para pagamento é calculado e gravado na tabela SLANDESCPONTUAL e leva em consideração as informações parametrizadas no Educacional, tais como descontos de parcela, descontos por antecipação, bolsa e regras da perda da bolsa conforme o desconto por antecipação. Demais valores que serão processados por fórmula no TOTVS Gestão Financeira não irão compor o valor.

**Como é realizado o cálculo:**

**Valor para pagamento** = valor da parcela – desconto da parcela – descontos por antecipação – descontos de bolsa.

Projeção do valor da bolsa condicional para cada vencimento do desconto por antecipação

Durante a geração do lançamento o sistema gravará na tabela SBOLSALANDESCPONTUAL a projeção do valor da bolsa condicinal calculado para cada vencimento do desconto por antecipação processado, ou seja, será gravado o valor da bolsa condicional processado levando em consideração todas as características de parametrização, tais como, somar bolsa, considera desconto por antecipação, afeta base de calculo entre outras.

A informação armazenada nesta tabela poderá ser utilizada pelo sistema ao identificar o valor da bolsa na baixa quando o cliente optou em utilizar a fórmula **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’)** ou **VLRBOLSALANDESCANT(' ', DATA DESEJADA)** para calcular o valor da bolsa condicional conforme o desconto por antecipação aplicado na data da baixa**.**

O anexo para visualizar estas informações estará disponível nomenu principal em Educacional >> Financeiro/Contábil >> Financeiro >> Descontos por Antecipação das Parcelas / Lançamentos >> Anexo >> Cálculo da bolsa condicional conforme o desconto por antecipação.

**Importante:**

Para que o comportamento citado aqui seja executado é necessário que o parâmetro "***O cálculo das bolsas condicionais levará em consideração o desconto por antecipação aplicado no momento da baixa do lançamento financeiro.***" esteja marcado. 

Parâmetro disponível em: *Educacional >> Integração >> Financeiro >> Educacional >> Fin - Vlrs. Opcionais / Integração*

**Valores de pagamento com bolsas condicionadas a um determinado vencimento**

Caso o contrato do aluno possua bolsa condicional e essa bolsa possua um vencimento associado (item de desconto por antecipação), os valores de pagamentos poderão considerar ou desconsiderar a bolsa.

Essa restrição de bolsas a determinados vencimentos só será válida se o parâmetro "Mantém fórmula default para valor opcional / integração de bolsas condicionais" estiver marcado. Caso esse parâmetro não esteja marcado, as bolsas sempre serão consideradas nos valores de pagamento independente de existir vínculo com item de desconto por antecipação.

Segue a regra abaixo que o sistema executa para saber se a bolsa "condicional" será considerada ou não no cálculo dos valores de pagamentos para os vencimentos:

A) Bolsa condicional NÃO possui associação com item de desconto por antecipação: Nesse caso, a bolsa será válida no cálculo de todos os valores de pagamentos por vencimento.

B) Bolsa condicional com associação a um item de desconto por antecipação: Nesse caso, o sistema verificará se a bolsa possui associação a um item de desconto (vencimento) pertencente ao desconto por antecipação considerado na geração do lançamento.

B.1) Bolsa NÃO possui vínculo com o desconto por antecipação considerado na geração do lançamento: Essa bolsa será válida no cálculo de todos os valores de pagamentos por vencimento.

B.2) Bolsa possuindo vínculo com o desconto por antecipação considerado no lançamento: Serão verificados todos os itens de desconto vinculados à bolsa referentes ao desconto por antecipação do lançamento. A partir dessa lista de itens de desconto encontrada, será considerado o item de desconto com maior data limite de vencimento calculada. O cálculo do valor a ser pago para cada vencimento somente irá considerar a bolsa caso a data limite do respectivo vencimento a ter o valor de pagamento calculado seja menor ou igual à maior data limite de vencimento calculada nas associações de itens de desconto da bolsa.

Observação:

Todas as vezes que o lançamento financeiro de uma parcela for "regerado", o sistema tornará a calcular os possíveis descontos por antecipação aplicáveis à parcela conforme cada data de vencimento indicada nos itens (ou faixas) de descontos e os gravará novamente no banco de dados.

**Valores da tabela SBOLSALAN**

Durante a geração ou regeração do lançamento financeiro do Educacional o sistema passará a gravar na tabela SBOLSALAN o campo VALORSEMDESCPONTUAL.

Este campo é responsável em guardar o valor calculado para a bolsa do aluno considerando o valor da bolsa na data de vencimento do lançamento, e como regra o desconto por antecipação não é processado para o lançamento se a baixa do mesmo ocorrer na data do vencimento ou posterior.

Conforme citado anteriormente dependendo da parametrização do sistema o valor da bolsa vai ser processado considerando o valor do desconto por antecipação, e em alguns cenários podem haver a necessidade de obter o valor da bolsa sem o desconto por antecipação e que posteriormente poderá ser recuperado através de fórmula para ser utilizado na contabilização ou geração de notas.

Fórmula

Veja no tópico “Fórmula VALORBOLSALAN” como utilizar a fórmula VALORBOLSALAN para retornar o valor da bolsa desconsiderando o valor do desconto por antecipação (valor da bolsa na data do vencimento).

ParcelasContratoParcelas do ContratoParcelasContratosSimulação de valores de parcelasSimulação de valores de parcelas

## Simulação de valores de parcelas

Ao simular o valor para uma determinada parcela, o sistema criará uma coluna para demonstrar o valor de pagamento para cada vencimento cadastrado para o desconto por antecipação.

Caso o valor original - valores de descontos - valores de bolsas seja negativo, esse valor negativo calculado será apresentado.

* O valor líquido apresentado na visão considerará o maior valor do desconto por antecipação apresentado.
* A simulação levará em consideração a data de vencimento para a data base do cálculo do valor de desconto.
* A data limite para conceder o desconto por antecipação será apresentada através de um hint ao posicionar o cursor do mouse sobre o vencimento desejado.
ParcelasDescAntDesconto por Antecipação das Parcelas / Lançamentos

Na tela de Desconto por Antecipação as Parcelas / Lançamentos é possível visualizar os valores calculados para o desconto por antecipação durante a geração do lançamento financeiro vinculado na parcela do contrato. E através do anexo "Cálculo da bolsa condicional conforme o desconto por antecipação" é possível visualizar dos valores calculados para as bolsas condicionais vinculadas ao contrato conforme o desconto por antecipação.

Os descontos por antecipação podem ser visualizados também pelo anexo "Desconto por Antecipação da parcela" presente na tela da parcela.

LancamentoFinLançamento FinanceiroLancamentoDescAntGeração de lançamentosGeração de lançamentos

## Geração de lançamentos

O sistema irá calcular o desconto por antecipação se o 'serviço' da parcela estiver parametrizado para considerar desconto por antecipação.

Será selecionado um desconto por antecipação (agrupamento de itens de descontos) cuja vigência compreenda a data da baixa do lançamento, se o parâmetro "Considerar a data de vencimento do lançamento na regra de validação da vigência" marcado cuja vigência compreenda a data do lançamento. (veja a regra no tópico "**Regra de cálculo do desconto por antecipação**").

Após selecionar o desconto por antecipação a ser utilizado no cálculo do valor de desconto, o sistema considerará o maior item de desconto calculado, independentemente da data limite calculada com base no dia fixo ou dia útil informado, para compor o valor base para os cálculos de bolsa (veja a regra no tópico "**Cálculo dos valores de bolsas**").

O valor original do lançamento será o valor base para o cálculo dos valores dos itens de desconto.

Após o lançamento da parcela gerado caso o desconto por antecipação sofro algum alteração no cadastro de vigência ou seja desassociado da matriz ou contrato, a parcela deverá ser regerada para que possa ser atualizados as informações do desconto no lançamento

Baixa de Lançamento FinanceiroBaixa de Lançamento Financeiro

## **Baixa de Lançamento Financeiro**

Na baixa de lançamento financeiro proveniente do TOTVS Educacional, o desconto por antecipação poderá ser concedido para o aluno conforme as regras cadastradas nos itens do desconto por antecipação. O desconto por antecipação será efetivamente concedido para o aluno na baixa do lançamento, mas somente na baixa *total* do valor a ser pago. A ordem de verificação para conceder o desconto por antecipação na baixa de lançamento é:

* Contrato.
* Campus/Polo da Matriz Aplicada (Somente para Ensino Superior).
* Matriz Aplicada.

Desta forma, para conceder os Descontos por Antecipação aos alunos, o sistema sempre procurará pelos descontos que tiverem associados na seguinte ordem: primeiro procurará pelos descontos associados nos contratos dos alunos e os aplicará, caso não existam Desconto por Antecipação associados nos contratos, irá procurar por Descontos por Antecipação associados aos campus/polo das matrizes aplicadas às quais pertencem e os aplicará, caso não encontre, irá por último, procurar pelos Descontos por Antecipação associados às matrizes aplicadas às quais pertencem e os aplicará.

A data da baixa do lançamento financeiro será a data base para cálculo do desconto. E para os itens do desconto por antecipação do tipo percentual, o valor original do lançamento será o valor base para o cálculo.

Exemplo:

Um aluno possui um desconto por antecipação associado ao seu contrato com a seguinte regra:

* Pagamento até o dia 10 = R$ 100,00
* Valor da mensalidade de R$ 1000,00

O aluno tem um lançamento financeiro com valor original de R$ 1000,00 (valor da mensalidade), e com data de vencimento no dia 11/01/2018. O aluno realizou o pagamento do lançamento no dia 10/01/2018. O sistema irá calcular um valor de desconto por antecipação de R$ 100,00. E o valor a ser pago pelo aluno será de R$ 900,00.

Lançamento financeiro com data de vencimento no dia 11/01/2018 e com data de baixa no dia 10/01/2018:

Valores calculados na baixa no dia 10/01/2018:

Os lançamentos financeiros que **não** terão o Desconto por Antecipação concedidos para os alunos são:

* Lançamento financeiro de parcela onde o Serviço não irá considerar o desconto por antecipação.
* Lançamento financeiro com pagamento parcial do valor a ser pago, isto é, com a realização de uma baixa parcial.
  + Exemplos:  
    ( Desconto por antecipação não concedido )
  + A) Lançamento financeiro 1:
    - Valor original de R$ 1000,00
    - Valor desconto por antecipação de R$ 100,00
    - Valor restante a ser pago de R$ 900,00
    - Se o aluno realizar o pagamento no valor de R$ 500,00, ou seja, se  realizar uma baixa parcial, o desconto por antecipação não será concedido para o aluno, e o valor restante a ser pago será de R$ 500,00.( Desconto por antecipação concedido )
  + B) Lançamento financeiro 2:
    - Valor original de R$ 1000,00
    - Valor desconto por antecipação de R$ 100,00
    - Valor restante a ser pago de R$ 900,00
    - Se o aluno realizar a baixa do lançamento financeiro no valor de R$ 900,00, valor total a ser pago, o desconto por antecipação será concedido para o aluno.

* Lançamento financeiro com pagamento a menor via retorno bancário ou via baixa manual.
  + Valor original de R$ 1000,00
  + Valor desconto por antecipação de R$ 100,00
  + Valor restante a ser pago de R$ 900,00
  + Valor de integração configurado para registrar pagamentos a menor = 'Pgto a Menor'
  + O valor pago pelo aluno presente no arquivo de retorno bancário é de R$ 800,00. Na importação do arquivo de retorno bancário o desconto por antecipação *não* será concedido para o aluno, visto que o aluno realizou um pagamento a menor que o valor a ser pago (como se tivesse feito uma baixa parcial) . Desta forma, o desconto por antecipação *não* será considerado e o campo de valor de integração 'Pgto a Menor' configurado para registrar pagamentos a menor terá o valor da diferença entre o valor original e o valor pago, presente no arquivo de retorno bancário, que nesse exemplo é de R$ 200,00.

+ Exemplo:
+ A) Lançamento financeiro 3:
+ Observação: O pagamento a maior via retorno bancário não teve alteração no seu comportamento.

* Lançamentos de Acordo:

+ Os lançamentos oriundos do Educacional baixados pelo processo de Acordo, **caso estejam vencidos na data em que o acordo é realizado**, assim como os respectivos lançamentos gerados pelo processo de Acordo, **não** terão o Desconto por Antecipação aplicados.
Bolsa Condicional X Desconto Por Antecipação

Como observado acima, o valor de bolsa poderá ser calculado depois de aplicar o desconto por antecipação e, claro, isto vai depender da parametrização.

Existindo algum desconto por antecipação associado ao aluno, por padrão o sistema ao gerar o lançamento vai considerar o maior valor de desconto por antecipação calculado para calcular o valor da bolsa e, durante a baixa, independente da data de pagamento, o valor da bolsa não será alterado.

Dica:

É possível parametrizar o sistema para que durante a baixa o Educacional recalcule o valor da bolsa conforme o desconto por antecipação concedido, neste caso o valor da bolsa irá variar conforme o valor de pagamento.

**Exemplo:**

Parcela: 1000.00

Desconto por antecipação:

* Pagamento até dia  05 => 50%
* Pagamento até dia  15 => 5%

Bolsa Condicional (Considera o desconto):

* Bolsa você merece => 10%

Cenários:

* Se o aluno efetuar o pagamento no dia 05, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 500,00 (Desconto Antecipação) = 500,00 (Vlr pagamento) = **50,00** (Vlr Bolsa de 10 %)

* Se o aluno efetuar o pagamento no dia 15, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 50,00 (Desconto Antecipação) = 950,00 (Vlr pagamento) = **95,00** (Vlr Bolsa de 10 %)

Observe que o valor da bolsa varia conforme o valor de pagamento.

**Requisitos para utilizar este recurso:**

* Funcionará somente para bolsas condicionais
* O sistema deve estar parametrizado para processar o valor da bolsa condicional por fórmula
* Na fórmula deverá ser utilizada a função de fórmula VLRBOLSALANDESCANTPORDTBAIXA ou VLRBOLSALANDESCANT (*Veja no final deste documento como utilizar estas formulas*)

  Bolsa Condicional Condicionada ao Desconto Por Antecipação

  Conforme visto no início deste documento é possível condicionar a bolsa ao pagamento de qualquer desconto por antecipação, ou seja, se o aluno efetuar o pagamento no dia 05 ele ganha a bolsa, senão, ele perde a bolsa.

  Para que esta regra funcione, o cálculo da bolsa deverá ser realizado por fórmula no momento da baixa.
Dia útil para descontos com dia fixo

Quando o sistema for processar o desconto por antecipação que estiver parametrizado como da fixo será respeitado para a data limite do vencimento do desconto por padrão o primeiro dia útil posterior. Respeitando o calendário do sistema se o dia fixo for correspondente a sábado, domingo ou feriado, o sistema irá considerar o próximo dia útil.

Esta mesma regra será levada em consideração nas informação que serão gravadas na tabela SLANDESCPONTUAL durante a geração do lançamento.

Controle da perda do Desconto por Antecipação ao Baixar o LançamentoControle da perda do Desconto por Antecipação ao Baixar o Lançamento

## Controle da perda do Desconto por Antecipação ao Baixar o Lançamento

Na geração do lançamento o cálculo da bolsa para tipo cascata sempre vai ser executado considerando a aplicação do desconto por antecipação, ou seja, primeiro calcula o desconto por antecipação e depois aplica o cálculo da bolsa. Para calcular a bolsa do tipo cascata será considerando o maior desconto por antecipação cadastrado para o aluno.

Exemplo:

Um aluno possui um desconto por antecipação cadastrado com a seguinte regra:

* Pagamento até o dia 05 = 50% de desconto
* Pagamento do dia 06 até o dia 10 = 20% de desconto

Parcela:

* Valor da mensalidade de R$ 1000,00
* Bolsa = 10 %

O cálculo do valor da bolsa levara em consideração o desconto por antecipação considerando que o aluno irá pagar a mensalidade no dia 05.

Valor da bolsa = valor mensalidade (R$ 1000.00) – desconto por antecipação (R$ 500,00 – 50%) \* percentual da bolsa(10%)  = R$ 50,00;

O cálculo acima é realizado durante a geração do lançamento, porem o aluno poderá realizar o pagamento no dia 06.

Com a possibilidade de possíveis auditorias ou conferencias será possível controlar o valor da perda do desconto por antecipação através de um valor de integração previamente parametrizado que será processado durante a baixa do lançamento financeiro.

Exemplo:

Um aluno possui um desconto por antecipação cadastrado com a seguinte regra:

* Pagamento até o dia 05 = 50% de desconto

* Pagamento do dia 06 até o dia 10 = 20% de desconto

* Valor da mensalidade de R$ 1000,00.

Vamos considerar que o aluno realizou o pagamento no dia 07, então o desconto por antecipação será de R$ 200,00 com isso será lançado no campo do valor de integração parametrizado como “Valor de perda do desconto por antecipação” o valor de R$ 300,00 que representa a perda do desconto por antecipação em relação ao maior desconto que o aluno teria direito caso realizasse o pagamento até o dia 05.

O valor de perda do desconto por antecipação será processado somente se o aluno tiver algum desconto por antecipação processado durante baixa.

**Parametrização:**

Para utilizar este recurso deverá ser preenchido nos parâmetros (Educacional >> Integração >> Financeiro >> Educacional >> Fin – Vlrs. Opcionais/Integração 1/3) o campo “Valor de parda do desconto por antecipação” que identifica qual o valor de integração controlará a informação durante a baixa.

* O campo valor de integração que será utilizado deverá estar cadastrado no cadastro de valores de integração do Educacional com ação igual a “Nada”, pois o objetivo deste campo é apenas informativo e seu valor não terá nenhum impacto sobre o valor líquido do lançamento financeiro.
* O parâmetro "Valor de perda do desconto por antecipação" uma vez já preenchido não poderá ser alterado se o valor de perda do desconto por antecipação já foi processado em algum item de baixa.

Após a baixa do lançamento financeiro será possível consultar o valor da perda do desconto por antecipação nos itens de baixa do lançamento através do valor de integração.

* Para baixa parcial sempre ocorrerá a perda do desconto por antecipação, neste caso se o sistema estiver parametrizado o valor da perda do desconto por antecipação será apurado.
* Quando houver um pagamento a menor, seja pela baixa manual ou retorno bancário também ocorrerá a perda do desconto por antecipação.
Alterar Vencimento do Desconto por Antecipação do LançamentoAlterar Vencimento do Desconto por Antecipação do Lançamento

**Alterar Vencimento do Desconto por Antecipação do Lançamento**

Em função de alguma eventualidade poderão haver necessidades pontuais de alterar os vencimentos do descontos por antecipação que já foram processados para o lançamento.

Por exemplo:

Descontos por antecipação original:

* 1º - Até o dia 05 – 30 %
* 2º - Até o dia 10 – 20 %
* 3º - Até o dia 20 – 5 %

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no recebimento via cartão, neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 08.

A realização da alteração deste vencimento deverá ser realizada através do processo “Alterar Vencimento do Desconto por Antecipação do Lançamento”.

Disponível em:

Crie um filtro que selecione as informações (parcelas, contratos...) dos alunos que terão os vencimentos dos desconto alterados. Este filtro tem o objetivo de facilitar e flexibilizar a seleção de dados de uma forma genérica.

O campo "Exibir os descontos por antecipação inativos" como padrão está marcado para exibir os descontos por antecipação inativos.

Após a seleção do filtro clique em “Carregar vencimentos dos descontos por antecipação”.

Após o processamento, serão apresentadas na aba “Alteração dos vencimentos” as informações dos vencimentos dos descontos por antecipação identificados através do filtro.

As informações serão apresentadas agrupadas pelo agrupador do desconto e vencimentos das parcelas. Para cada agrupador serão mostrados os descontos processados para a parcela. Preencha na coluna em destaque a data correspondente ao novo vencimento.

Como as informações serão apresentadas agrupadas, foi disponibilizado a opção “Pré-visualizar Aluno(s)”. Está opção apresenta todos os alunos que fazem parte do agrupamento da linha em questão e que terá o vencimento do desconto alterado.

Após o preenchimento da data correspondente ao novo vencimento, clique em executar o processo. O processo irá informar os descontos por antecipação que poderão ser desativados após a execução do processo.

Ao final da execução o será apresentado um log com as informações do processo e quais os alunos tiveram o vencimento alterado.

Importante

Importante

* O processo altera pontualmente o vencimento somente dos descontos processados para as parcelas / lançamentos filtrados no processo (tabela SLANDESCPONTUAL), ou seja, o cadastro oficial do desconto por antecipação não é alterado.
* Na geração dos lançamentos do mês seguinte o sistema respeitará o cadastro oficial do desconto que estiver vinculado à matriz ou ao contrato do aluno.
* Caso o lançamento que teve o vencimento do desconto alterado seja regerado o sistema vai reprocessar os descontos por antecipação considerando os desconto do cadastro oficial, ou seja, a alteração do vencimento é perdida.
Data do novo vencimento do desconto sobrepondo outros vencimentos

Dependendo da data do novo vencimento, a mesma poderá sobrepor a data de outros vencimentos.

Por exemplo:

Descontos por antecipação original:

* 1º - Até o dia 05 – 30 %
* 2º - Até o dia 10 – 20 %
* 3º - Até o dia 20 – 5 %

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no recebimento via cartão, neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 10/05.

Observem que o dia 10/05 é quando finaliza o 2º vencimento, para este cenário o sistema realizará a alteração do 1º vencimento para o dia 10/05 e o 2º vencimento será inativado.

Visualização dos Descontos

Os descontos processados para as parcelas / lançamentos poderão ser consultados através do menu “Financeiro/Contábil >> Desconto por Antecipação das Parcelas / Lançamento” e a mesma informação também está disponível no anexo da parcela do contrato.

Através da visualização destes dados é possível consultar a data do vencimento original (preenchida somente quando for alterada), se o desconto está ativo e qual usuário realizou a alteração.

FormulasFórmulasFormulaDescAntFórmula Desconto por AntecipaçãoFórmula Desconto por Antecipação

## **Fórmula Desconto por Antecipação**

Com o objetivo de disponibilizar o valor do desconto por antecipação no contexto de fórmula no TOTVS Gestão Financeira foram criadas fórmulas para que sejam utilizadas na baixa do lançamento, no cálculo do valor líquido do lançamento e em outros processos ou recursos do produto.

As fórmulas criadas são:

* **ValorDescontoAntecipacao**: Essa fórmula tem o objetivo de  retornar o valor do desconto por antecipação calculado no momento do cálculo do valor líquido ou na baixa de lançamento financeiro através da data da baixa ao calcular o valor líquido. Caso essa fórmula seja utilizada em algum processo que não execute o cálculo do valor líquido, o valor retornado será o valor calculado conforme a data parametrizada no parâmetro "Data Default da Baixa a Receber" presente nos parâmetros do *TOTVS Gestão Financeira*em Contas a Receber → Baixa → Manutenção de Baixa → Baixa a Receber.

  **Atenção:**  
  Utilização da fórmula ValorDescontoAntecipacao é recomendada quando quiser retornar o valor do desconto por antecipação calculado no momento do cálculo do valor líquido ou na baixa de lançamento financeiro através da data da baixa ao calcular o valor líquido.
* **ValorDescontoAntecipacaoPorData**: Essa fórmula tem o objetivo de retornar o valor do desconto por antecipação calculado conforme a data passada por parâmetro.

Vale ressaltar que já existe a fórmula TabLanBaixa no TOTVS Gestão Financeira que recebe dois parâmetros. Essa fórmula tem o objetivo retornar o valor do campo passado por parâmetro. A fórmula tem dois parâmetros. O primeiro parâmetro é o nome do campo que queira retornar o seu valor, e o segundo parâmetro é o tipo do campo passado no primeiro parâmetro.

Fórmula Valor de Bolsa Condicional Conforme Desconto Por AntecipaçãoFórmula Valor de Bolsa Condicional Conforme Desconto Por Antecipação

## **Fórmula Valor de Bolsa Condicional Conforme Desconto Por Antecipação *formuladescontoassociadobolsacond***

**VLRBOLSALANDESCANTPORDTBAIXA(‘ ’)**:

Essa fórmula tem o objetivo de  retornar o valor das bolsas condicionais processadas para o lançamento levando em consideração o desconto por antecipação que o aluno está ganhando ao efetuar a baixa, também será avaliado se existe alguma condicional de desconto por antecipação vinculada a bolsa que indica que o aluno poderá perder a bolsa.

Esta fórmula leva em consideração a “Data de Baixa” para identificar o desconto por antecipação que o aluno terá ou não.

Exemplo

Parcela: 1000.00

Desconto por antecipação:

* Pagamento até dia  05 => 50%
* Pagamento até dia  15 => 5%

Bolsa Condicional (Considera o desconto):

* Bolsa você merece => 10% (**Válida para pagamento até o dia 05**)
* Bolsa sindicato => 10%

Cenários:

* Se o aluno efetuar o pagamento no dia 05, o valor total de bolsa será de:

1000,00 (Vlr Parcela) - 500,00 (Desconto Antecipação) = **500,00 (Vlr pagamento)**

=> Bolsa você merece = 50,00 (Vlr Bolsa de 10%)

=> Bolsa sindicato = 50,00 (Vlr Bolsa de 10 %)

=> **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’) = 100,00**

* Se o aluno efetuar o pagamento no dia 15, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 50,00 (Desconto Antecipação) = **950,00 (Vlr pagamento)**

=> Bolsa você merece = 0,00 ( o aluno perde a bolsa, pois efetuou o pagamento dia 15)

=> Bolsa sindicato = 95,00 (Vlr Bolsa de 10 %)

=> **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’) = 95,00**

Observe que o valor da bolsa varia conforme o valor de pagamento que irá variar conforme o desconto por antecipação e neste caso a fórmula sempre traz o valor atualizado.

Ressaltamos que todo o comportamento é flexível e dependerá de parametrizações que relatamos neste documento.

Portanto, podemos concluir que esta fórmula retorna o valor de bolsa atualizado conforme a data da baixa do lançamento.

Se a função de fórmula for acionada sem nenhum parâmetro, por exemplo, **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’)** o sistema levará em consideração todas as bolsas processadas para o aluno durante a geração do lançamento.

Se desejar retornar o valor de uma bolsa específica, poderá passar, via parâmetro, o código das bolsas desejadas separadas por “;”, por exemplo: **VLRBOLSALANDESCANTPORDTBAIXA(‘35;01;10’)**.

**VLRBOLSALANDESCANT(' ', DATA DESEJADA) :** esta fórmula executa o mesmo comportamento da fórmula VLRBOLSALANDESCANTPORDTBAIXA(‘ ’), a diferença está somente na passagem de parâmetro.

Para esta fórmula o usuário poderá passar uma data em que o sistema considerará como data de baixa para que os cálculos sejam realizados.

Lembrando que caso o primeiro parâmetro esteja vazio o sistema levará em consideração todas as bolsas processadas para o aluno durante a geração do lançamento.

Se desejar retornar o valor de uma bolsa específica, poderá passar, via parâmetro, o código das bolsas desejadas separadas por “;”, por exemplo: **VLRBOLSALANDESCANT** (‘35;01;10’,’01/01/2017’).

Importante ressaltar que para os casos em que houver baixa parcial, devemos tratar na fórmula para que o valor de bolsa não seja processado na segunda baixa, pois a primeira baixa já processa o valor da bolsa.

Veja o exemplo abaixo:

Fórmula VALORBOLSALANFórmula VALORBOLSALAN

**Fórmula VALORBOLSALAN**

Durante o processamento da contabilização ou geração da nota fiscal é possível recuperar o valor da bolsa processado para o lançamento utilizando a fórmula VALORBOLSALAN.

**Declaração da fórmula:** ValorBolsaLan(int campoValor, int tipoBolsa, string codBolsa)

=>  int campoValor

0 = Será retornado o valor da bolsa

1 = Será retornado o valor da bolsa na baixa

2 = Será retornado o valor da bolsa sem considerar o valor do desconto por antecipação da parcela

3 = Será retornado o (valor da bolsa sem o desconto por antecipação - valor da bolsa (considerando o maior desconto por antecipação) )

=>  int tipoBolsa

    Escalável = 0,

    Especial = 1,

    Todas = -1

=>   string codBolsa

Pode passar o código da bolsa, se for passado vazio ou -1 indica que o sistema vai somar todas as bolsas.

Para geração de lançamento parametrizado com essa fórmula o valor da bolsa não irá variar conforme o desconto por antecipação e nem perder a bolsa, neste caso a fórmula sempre traz o valor da bolsa.

Contabilização

Na contabilização do lançamento quando o evento contábil estiver parametrizado para aplicar na “Bolsa”, a fórmula pode ser utilizada conforme o exemplo abaixo.

VALORBOLSALAN(0,-1,TABBOLSALAN('CODBOLSA','S'))

=>  TABBOLSALAN('CODBOLSA','S')  -  retorna o código da bolsa corrente, ou seja, que está sendo processada.

Fórmula SLANDESCOPONTUALPORDTBAIXAFórmula SLANDESCOPONTUALPORDTBAIXA

**Fórmula SLANDESCOPONTUALPORDTBAIXA(CAMPO):**

Fórmula responsável em recuperar o valor de um determinado campo da tabela SLANDESCPONTUAL do registro que compreenda a data da baixa do lançamento, ou seja, será carregado o desconto processado para o lançamento conforme a data da baixa.

**Exemplo:**

Data vencimento lançamento: 30/03

**Descontos processados para o lançamento:**

1º Desconto – Pagamento dia 05/03 – Valor para pagamento: 500,00

2º Desconto – Pagamento dia 10/03 – Valor para pagamento: 600,00

3º Desconto – Pagamento dia 20/03 – Valor para pagamento: 700,00

4º Desconto – Pagamento dia 30/03 – Valor para pagamento: 1000,00

Executando a fórmula **SLANDESCOPONTUALPORDTBAIXA(‘VALORPARAPAGTO’)** para uma baixa no dia 09/03, o resultado da fórmula será de 600,00.

Observação:

Se a data da baixa for maior que a data do vencimento do lançamento então será considerado o desconto por antecipação processado para o vencimento.

OrdemDescontoAplicOrdem de Aplicação do Desconto por Antecipação

O campo “Aplicar desconto por antecipação” define se o desconto por antecipação será aplicado “Antes do cálculo da bolsa” ou “Depois do cálculo da bolsa”. Uma vez aplicado (calculado) o desconto por antecipação, o mesmo não será calculado novamente, isto é, não será permitida a inserção de uma bolsa com o valor setado para “Depois do cálculo da bolsa” cuja ordem de aplicação dessa bolsa seja maior do que uma outra bolsa com o valor “Antes do cálculo da bolsa” pois o desconto já foi processado ao se calcular o valor da primeira bolsa.

OrdemAplicDescAntCadastroBolsasCadastro de Bolsas

Acréscimo do campo "Aplicar desconto por antecipação" que conterá o valor default "Antes do cálculo da bolsa". O preenchimento do campo "Aplicar desconto por antecipação" conterá o valor default para o cadastro de bolsas nos contratos, ou seja, a cada vez que uma bolsa for inserida no contrato do aluno, a mesma será inserida com o valor informado no cadastro da bolsa.

Tela do cadastro de bolsas com o novo campo:

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação de bolsa setado com o valor "Contrato"

BolsasContratoBolsas de Contratos

Acréscimo do campo "Aplicar desconto por antecipação" que buscará o valor default do valor informado para o respectivo campo do cadastro de bolsas. Esse campo também só ficará visível para o usuário se o parâmetro de aplicação de bolsa estiver setado com o valor "Contrato" conforme citado no tópico anterior.

Tela do cadastro de bolsas com o novo campo:

Validação de inclusão ou alteração de bolsas de contratos: O sistema validará o preenchimento do campo conforme o campo "Tipo da Bolsa" na edição do contrato e conforme registros de bolsas de contratos previamente cadastrados.

1. Tipo de Bolsa = "Aplicar bolsas em cascata": Quando o contrato estiver setado com esse tipo de bolsa, não será permitido se ter uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" com ordem menor ou igual à uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa". A mensagem será alterada dependendo da bolsa que estão sendo inserida / alterada.   
     
   Se estivermos inserindo uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa" e já tivermos uma bolsa no contrato com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" com ordem menor ou igual à bolsa que está sendo inserida ou alterada, o sistema exibirá a mensagem abaixo:  
     

   Se estivermos inserindo uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" e já tivermos uma bolsa no contrato com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa" com ordem maior ou igual à bolsa que está sendo inserida ou alterada, o sistema exibirá a mensagem abaixo:
2. Tipo de Bolsa = "Somar Bolsas" ou "Aplicar somente a maior bolsa": Quando o contrato estiver setado com esse tipo de bolsa, não será permitido se ter uma bolsa com o campo "Aplicar desconto por antecipação" com valor diferente de alguma bolsa de contrato previamente cadastrada pelo usuário, ou seja, para esse tipo bolsa, todas as bolsas deverão ter o mesmo valor informado no campo "Aplicar desconto por antecipação". Caso seja informada uma bolsa inconsistente, será exibida a seguinte mensagem para o usuário:

ConcessaoBolsasFuturasConcessão de Bolsas Futuras

No cadastro de concessão de bolsas futuras teve a criação do campo “Aplicar desconto por antecipação”. Esse campo tem o objetivo de informar se o valor do desconto por antecipação será calculado antes ou depois do cálculo do valor da bolsa inserida no contrato via a concessão de bolsas futuras.

No assistente de concessão de bolsas futuras também teve a criação do campo “Aplicar desconto por antecipação”.

O campo “Aplicar desconto por antecipação” nas telas de cadastro de concessão de bolsas futuras e no assistente de concessão de bolsas futuras terá o preenchimento padrão por “Antes do cálculo da bolsa”. Esse valor poderá ser alterado pelo usuário conforme desejado. E também será alterado automaticamente pelo mesmo valor presente no campo “Aplicar desconto por antecipação” no cadastro de bolsa quando a bolsa for informada em ambas as telas.

Na inclusão de parcela para o contrato do aluno, caso o aluno tenha uma concessão de bolsas futuras que contempla nos dados informados na parcela. A bolsa será incluída no contrato do aluno onde o campo “Aplicar desconto por antecipação” da bolsa do aluno terá o mesmo valor do campo “Aplicar desconto por antecipação” presente na concessão de bolsas futuras.

GeracaoSimulacaoGeração de lançamentos / Simulação de valores de parcelas

**Geração de lançamentos / Simulação de valores de parcelas**

Para Bolsas com comportamentos “Somar Bolsas” e “Aplicar bolsas em cascata”. Se o contrato tiver esse comportamento (tipo de bolsas), poderemos ter bolsas com comportamentos distintos em relação ao desconto por antecipação, ou seja, com o desconto calculado “Depois do cálculo da bolsa” e bolsas com o desconto calculado “Antes do cálculo da bolsa” desde que não tenhamos uma bolsa B de ordem maior que uma bolsa A com o desconto por antecipação para a B sendo calculado como “Depois do cálculo da bolsa” e o desconto por antecipação para a bolsa A setado para “Antes do cálculo da bolsa”

Se duas bolsas no contrato possuem comportamentos distintos na aplicação do desconto por antecipação, a geração de lançamentos ou simulação de valores de parcelas, considerará, primeiramente, as bolsas cujo desconto seja calculado “Depois do cálculo da bolsa”.

**Exemplos**:

(Exemplo 1 – Somar Bolsas)

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 300,00  
- Valor líquido: R$ 200,00

Os valores de bolsas e de desconto por antecipação não foram influenciados porque o campo “Afeta base de cálculo” não está marcado.

(Exemplo 1 – Aplicar bolsas em cascata)

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Bolsa A: R$ 100,00  
- Valor do desconto por antecipação: 450,00  
- Bolsa B: R$ 90,00  
- Total de Bolsas aplicado: R$ 190,00  
- Valor líquido: R$ 360,00

Os valores de bolsas e de desconto por antecipação foram influenciados pela ordem de cálculo visto que, para o comportamento “Aplicar bolsas em cascata”, a base de cálculo das bolsas ou do cálculo do valor do desconto por antecipação sempre é influenciado pela ordem de cálculo dos itens (bolsas ou descontos). O campo “Afeta base de cálculo” não aparece no cadastro de bolsas em cascata porque, para esse tipo de comportamento, a base de cálculo dos itens sempre é afetada.

Para Bolsas com comportamento “Aplicar Somente a Maior Bolsa”, todas as bolsas do contrato deverão ter o campo “Aplicar desconto por antecipação” com o mesmo valor, ou seja, ou todas as bolsas com o valor “Antes do cálculo da bolsa” ou todas as bolsas com o valor “Depois do cálculo da bolsa”

Exemplos:

(Exemplo 1 – Aplicar Somente a Maior Bolsa)

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado

=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 200,00  
- Valor líquido: R$ 300,00

Os valores de bolsas e de desconto por antecipação não foram influenciados porque o campo “Afeta base de cálculo” não está marcado.

Para Bolsas com comportamento “Aplicar bolsas em cascata” e com dois ou mais itens de desconto por antecipação o educacional vai considerar o maior desconto por antecipação independente da data que for efetuada o pagamento ao calcular o valor da bolsa de todos os vencimentos.

Exemplos:

(Exemplo 1 – Descontos por antecipação antes do cálculo da bolsa)

- Parcela 1: R$ 1000,00  
- Bolsa (Cascada): 50%  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Desconto por antecipação no 1º vencimento (até dia 10): 10% (maior desconto)  
- Desconto por antecipação no 2º vencimento (até dia 15): 5%

=> Após geração da parcela 1, teremos os seguintes valores:  
- Desconto por antecipação (10%) = R$ 100,00  
- Bolsa (Cascata) (50%) = R$ 450,00  
- Valor líquido a pagar = R$ 450,00

- Desconto por antecipação (5%) = R$ 50,00  
- Bolsa (Cascata) (50%) = R$ 450,00  
- Valor líquido a pagar = R$ 500,00

**Como no cálculo dos valores do tipo cascata o educacional considera o maior desconto por antecipação independente da data que for efetuada o pagamento****. Neste caso, o valor da bolsa do segundo desconto por antecipação está considerando o maior desconto por antecipação que corresponde aos 10% do primeiro desconto.**

(Exemplo 2 – Descontos por antecipação depois do cálculo da bolsa)

- Parcela 1: R$ 1000,00  
- Bolsa (Cascada): 50%  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Desconto por antecipação no 1º vencimento (até dia 10): 10%   
- Desconto por antecipação no 2º vencimento (até dia 15): 5%

=> Após geração da parcela 1, teremos os seguintes valores:  
- Desconto por antecipação (10%) = R$ 50,00  
- Bolsa (Cascata) (50%) = R$ 500,00  
- Valor líquido a pagar = R$ 450,00

- Desconto por antecipação (5%) = R$ 25,00  
- Bolsa (Cascata) (50%) = R$ 500,00  
- Valor líquido a pagar = R$ 475,00

**O calculo de bolsa retroativa com desconto por antecipação terá o mesmo comportamento quando é incluído uma bolsa corrente no contrato**

AfetaBaseCalculoAfeta Base de Cálculo do Desconto por Antecipação

A fim de afetar a base de cálculo para as próximas bolsas a serem processadas bem como a base para o cálculo do desconto por antecipação se o mesmo for calculado depois do cálculo da bolsa, foi criado o campo “Afeta base de cálculo” no cadastro de bolsas, no cadastro de bolsas de contratos dos alunos e no cadastro de concessão de bolsas futuras.

AfetaBaseCalculoDescAntCadastroBolsasCadastro de Bolsas

Acréscimo do campo "Afeta base de cálculo". O preenchimento do campo "Afeta base de cálculo" conterá o valor default para o cadastro de bolsas nos contratos, ou seja, a cada vez que uma bolsa for inserida no contrato do aluno, a mesma será inserida com o valor informado no cadastro da bolsa.

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação de bolsa setado com o valor "Contrato" e o campo "Aplicar desconto por antecipação" tem que estar setado com o valor "Depois do cálculo da bolsa". Seguem telas abaixo:

(Tela de bolsa)

(Parâmetros de sistema)

BolsasContratosAfetaBolsas de Contratos

Acréscimo do campo "Afeta base de cálculo". Ao selecionar uma bolsa, o valor default para o campo "Afeta base de cálculo" setado no cadastro da bolsa será preenchido no respectivo campo da bolsa do contrato, mas o mesmo poderá ser alterado normalmente. A geração de lançamentos / simulação de valores de parcelas considerará esse valor do campo na bolsa do contrato.

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação de bolsa setado com o valor "Contrato", o campo "Aplicar desconto por antecipação" tem que estar setado com o valor "Depois do cálculo da bolsa" e o campo "Tipo da Bolsa" do contrato tem que ser diferente de "Aplicar bolsas em cascata" pois o comportamento de aplicar bolsas em cascata sempre afeta a base de cálculo das entidades que serão calculadas posteriormente ao cálculo de uma determinada bolsa. Seguem telas abaixo:

(Tela de bolsa do contrato)

(Parâmetros de sistema)

  

(Tela de contrato)

ConcessaoBolFutAfetaConcessão de Bolsas Futuras

No cadastro de concessão de bolsas futuras teve a criação do campo “Afeta base de cálculo”. Esse campo tem o objetivo indicar quando marcado, que o sistema afetará base de cálculo para as próximas bolsas a serem processadas bem como a base para o cálculo do desconto por antecipação se o mesmo for calculado depois desta bolsa.

O campo fica disponível quando o campo “Aplicar desconto por antecipação” estiver configurado para depois do cálculo da bolsa.

No assistente de concessão de bolsas futuras também teve a criação do campo “Afeta base de cálculo”.

O valor desse campo será preenchido automaticamente pelo mesmo valor do campo “Afeta base de cálculo” presente no cadastro de bolsa.

Na inclusão de parcela para o contrato do aluno, caso o aluno tenha uma concessão de bolsas futuras que contempla nos dados informados na parcela. A bolsa será incluída no contrato do aluno onde o campo “Afeta base de cálculo” da bolsa do aluno terá o mesmo valor do campo “Afeta base de cálculo” presente na concessão de bolsas futuras.

GeracaoSimulacaoGeração de lançamentos / Simulação de valores de parcelas

**Geração de lançamentos / Simulação de valores de parcelas**

  

A geração de lançamentos priorizará as bolsas que afetam a base de cálculo e, posteriormente, processará as outras bolsas sendo que, se duas bolsas no contrato possuem comportamentos distintos na aplicação do desconto por antecipação, a geração de lançamentos ou simulação de valores de parcelas, considerará, primeiramente, as bolsas que afetam a base de cálculo e logo em seguida, as bolsas cujo desconto seja calculado “Depois do cálculo da bolsa”.

**Exemplos**:

(Exemplo 1 – Somar Bolsas)

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: **Desmarcado (Não visível)**  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 450,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 180,00  
- Total de Bolsas aplicado: R$ 280,00  
- Valor líquido: R$ 270,00

 (Exemplo 2 – Somente a Maior Bolsa)

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa B: **Desmarcado**

=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 0,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 200,00  
- Valor líquido: R$ 300,00

**HOW TO**

**1) Desconto por Antecipação Parte 1 - Cadastros**

**2) Desconto por Antecipação - Parte 2 Associações**

**3) Desconto por Antecipação Parte 3 - Simulação, Lançamento e Regras**

**4) Desconto por Antecipação Parte 4 - Baixa de Lançamento**

**5) Bolsas e Desconto por Antecipação - Parte 1**

**6) Bolsas e Desconto por Antecipação - Parte 2**

**7) Bolsas e Desconto por Antecipação - Parte 3**

**8) Bolsas e Desconto por Antecipação - Parte 4**

**9) Bolsas e Desconto por Antecipação - Parte 5**

**10) Controle da Perda do Desconto Por Antecipação na Baixa do Lançamento**
