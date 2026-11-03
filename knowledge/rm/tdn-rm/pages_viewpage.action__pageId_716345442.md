---
content_hash: e25014587678b6731c26a2b268b6fde8c82eb57006cd0b0e0c0f2cd3e9191595
fetched_at: '2026-06-29T00:11:26.309344+00:00'
page_id: '716345442'
product: rm
source: tdn-rm
title: Regras Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716345442
version: 21
---

Regra de cálculo do desconto por antecipaçãoRegra de cálculo do desconto por antecipaçãoCálculo do desconto por antecipaçãoPrioridade do Desconto por Antecipação

Somente serão considerados os lançamentos do Educacional que estão sendo gerados ou lançamentos já gerados e não vencidos com status "Em Aberto".

Sistema buscará descontos por antecipação no Educacional na seguinte ordem de prioridade:

1. Descontos por antecipação no contrato
2. Descontos por antecipação no campus/polo da matriz aplicada (Anexo da matriz aplicada)
3. Matriz aplicada

Se o sistema encontrar descontos por antecipação em qualquer entidade citada acima (contrato / campus\_polo / matriz aplicada) obedecendo a ordem de prioridade, essa entidade é que será considerada para o cálculo não havendo buscas em outra entidade.

Exemplo:

- Se houver um desconto por antecipação cadastrado no contrato do aluno, mesmo que o valor do desconto calculado seja zero, o sistema não buscará descontos por antecipação no campus/polo da matriz aplicada ou na matriz aplicada.  
- Se não houver um desconto por antecipação cadastrado no contrato, o sistema busca no campus/polo da matriz aplicada (somente para o Ensino Superior) e, somente se não encontrar registros no campus/polo e que o sistema buscará descontos por antecipação cadastrados na matriz aplicada.

Vigência do Desconto por Antecipação

O sistema considera as vigências cadastradas nos descontos por antecipação, os campos "Data início de vigência" e "Data final de vigência" definirão um período válido para a escolha do desconto por antecipação a ser utilizado.

O que define se uma parcela está compreendida dentro da vigência de um desconto é a data de vencimento da parcela, e no momento da baixa se a data de baixa do lançamento estiver dentro das datas limite do desconto por antecipação.

Os campos de vigência podem aceitar o valor nulo indicando que, caso esse campo seja nulo, o mesmo sempre será válido, ou seja, caso seja a data início de vigência nula, todas as datas a serem comparadas com ela serão maiores que a mesma, da mesma forma que, caso o campo data final de vigência seja nulo, todas as datas a serem comparadas com ela serão menores.

Seguem abaixo alguns exemplos:

a) Desconto com data de início e data final de vigência preenchidas

* + Data início de vigência: 01/01/2018
  + Data final de vigência : 31/01/2018  
    => Significa que o desconto por antecipação só será aplicado se a data de vencimento da parcela e no momento da baixa, a data de baixa estiver dentro do período de vigência explicitamente especificado.

b) Desconto com data de início nula e data final de vigência preenchida

* + Data início de vigência: NULA
  + Data final de vigência : 31/01/2018  
    => Significa que o desconto por antecipação só será aplicado se a data de vencimento da parcela e no momento da baixa, a data de baixa for menor ou igual à data final de vigência

        c) Desconto com data de início preenchida e data final de vigência nula

* + Data início de vigência: 01/01/2018
  + Data final de vigência : NULA  
    => Significa que o desconto por antecipação só será aplicado se a data de vencimento da parcela e no momento da baixa, a data de baixa for maior ou igual à data inicial de vigência

        d) Desconto com data de início e data final de vigência nulas

* + Data início de vigência: NULA
  + Data final de vigência :  NULA  
    => Significa que o desconto por antecipação será válido para qualquer data de vencimento da parcela

A data da data da baixa do lançamento é utilizada para se definir a qual desconto por antecipação (agrupamento de itens de descontos) que o lançamento financeiro estará associado, conforme a vigência do desconto por antecipação. Uma vez o lançamento financeiro gerado e associado ao desconto por antecipação, o item de desconto considerado irá variar conforme a data da baixa, em caso de baixa do lançamento, ou conforme a data do valor líquido, em caso do cálculo do valor líquido.   

Quando o cliente informa um período de vigência no cadastro do desconto por antecipação, essa data é validada no momento da geração e baixa do lançamento, exemplo abaixo:

* Cadastro do desconto por antecipação: Data inicio de vigência: 01/01/2020 — Data final de vigência: 31/06/2020
* Parcela com data de vencimento 15/01/2020 (dentro do periodo de vigência)

No momento de baixar informo a data 15/12/2016 (data anterior ao período de vigência), nesse caso o desconto não será aplicado.

Só é considerado o desconto que esteja compreendido dentro do período de vigência no cadastro do desconto por antecipação.  
  
Pensando no cenário acima foi implementado o parâmetro "Considerar a data de vencimento do lançamento na regra de validação da vigência" **(****Configurações | Parâmetros| Integração| Financeiro | Conta a receber | Baixas | Manutenção  de baixas | Desconto por Antecipação), [clique aqui.](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)**

Para que o parâmetro seja reconhecido na base siga os passos abaixo:

Com esse parâmetro marcado ao realizar uma baixa com data de vencimento inferior a vigência do cadastro do desconto por antecipação, esse desconto será aplicado.   
Será validado a data de vencimento do lançamento e não a data de baixa, então se a data de vencimento do lançamento estiver compreendida dentro da vigência será aplicado o desconto.

Cálculo dos valores dos itens de desconto

Após a seleção do desconto por antecipação a ser utilizado serão verificados os itens de descontos a serem utilizados.

Os itens de desconto a serem verificados dependerão do processo que estará calculando o valor do desconto por antecipação, pois o processo poderá considerar todos os itens de desconto independente do dia limite (Ex.: Geração de lançamentos do Educacional) ou poderá considerar apenas o item de desconto com a menor data limite calculada entre os itens de desconto cujo valor é maior ou igual à data base a ser considerada. (Ex.: Baixa de lançamentos e Valor líquido)

Para se fazer a comparação com a data base a ser utilizada, o dia (fixo ou útil) configurado no item de desconto será transformado internamente em uma data limite calculada no seguinte formato: (<dia do item de desconto calculado> / <mês da data de vencimento do lançamento> / <ano da data de vencimento do lançamento>)

Os itens serão ordenados pela data limite calculada e o desconto será concedido sempre para a menor data limite calculada maior ou igual à data do processo que está sendo considerado.

Se a data base para o cálculo for maior que a data limite do item de desconto de maior valor, devemos calcular o item de desconto cuja data limite calculada seja maior ou igual à data base. Se a data base para o cálculo for menor ou igual à data limite do item de desconto de maior valor, o valor do desconto resultante assumirá o maior de desconto calculado.

Caso sejam selecionados dois descontos com o mesmo dia de vencimento calculado, o sistema considerará o maior valor de desconto calculado.

Dia do item de desconto calculado

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

Quando o sistema for processar o desconto por antecipação que estiver parametrizado como dia fixo será respeitado para a data limite do vencimento do desconto por padrão o primeiro dia útil posterior. Respeitando o calendário do sistema se o dia fixo for correspondente a sábado, domingo ou feriado, o sistema irá considerar o próximo dia útil, exceto se o sábado estiver com o parâmetro marcado: Considerar Sábado como dia útil em *TOTVS TOTVS Gestão Financeira => Contas a Receber / Manutenção de Lançamento / Lançamento - Calendário Oficial.*

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

Caso não tenha calendário especificado na filial, o sistema buscará o calendário oficial parametrizado no *TOTVS TOTVS Gestão Financeira* (Parâmetro "Calendário Oficial -> Calendário Oficial") e considerará sábado como dia útil se o parâmetro "Calendário Oficial -> Considerar sábado como dia útil" estiver marcado.

Valor calculado para o item de desconto

O valor calculado dependerá do tipo de desconto setado no item de desconto.

Os valores de tipos de desconto poderão ser:

* "**Valor**": Indica que o valor informado é um valor fixo. Caso o valor informado seja maior do que o valor original do lançamento, o valor calculado para o desconto por antecipação será igual ao valor original do lançamento.
* "**Percentual**": Indica que o valor informado trata-se de um percentual sobre o valor original do lançamento.

Os Descontos por Antecipação quando associados serão calculados sobre o *valor original* do lançamento, exceto quando o contrato estiver parametrizado para "*Aplicar bolsas em cascata*". Para saber como .

Cálculo dos valores de bolsas Cálculo dos valores de bolsas Cálculo dos valores de bolsas

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

Durante a geração ou regeração do lançamento financeiro do Educacional o sistema passará a gravar na tabela SBOLSALAN o campo VALORSEMDESCPONTUAL, ou seja, o mesmo será sempre preenchido na geração de lançamentos que contém bolsas.

Este campo é responsável por guardar o valor calculado para a bolsa do aluno considerando o valor da bolsa na data de vencimento do lançamento e, como regra, o desconto por antecipação não é processado para o lançamento se a baixa do mesmo ocorrer na data do vencimento ou posterior.

Conforme citado anteriormente dependendo da parametrização do sistema o valor da bolsa vai ser processado considerando o valor do desconto por antecipação, e em alguns cenários podem haver a necessidade de obter o valor da bolsa sem o desconto por antecipação e que posteriormente poderá ser recuperado através de fórmula para ser utilizado na contabilização ou geração de notas.

Atenção

O campo VALORSEMDESCPONTUAL terá o seu valor zerado no caso de bolsas condicionadas a uma determinada data de vencimento com vencimento da parcela superior à data citada.

**Exemplo:**

Parcela 4 com vencimento  no valor de R$ 1000,00.

Bolsa condicional "22" de 10% com um item de desconto por antecipação em anexo dia fixo de vencimento igual a 20.

Após a geração de lançamentos, os valores dos campos da tabela SBOLSALAN estarão conforme abaixo:

  - SBOLSALAN.VALOR = R$ 100,00  
  - SBOLSALAN.VALORSEMDESCPONTUAL = R$ 0,00

**OBSERVAÇÃO:**  
O cálculo da bolsa no exemplo acima foi feito com o campo "Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s) desmarcado"

Fórmula

Veja no tópico “Fórmula VALORBOLSALAN” como utilizar a fórmula VALORBOLSALAN para retornar o valor da bolsa desconsiderando o valor do desconto por antecipação (valor da bolsa na data do vencimento).
