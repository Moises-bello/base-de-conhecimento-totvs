---
content_hash: bb1dc07560976a74e7c229e03c7a6a52559a7c26a8f00137bcbd20311cc850d5
fetched_at: '2026-06-29T00:10:44.515412+00:00'
page_id: '552598291'
product: rm
source: tdn-rm
title: Fórmulas / Funções V
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552598291
version: 9
---

**VALORFUNC (STRING, DATA1, DATA2)**

Retorna o somatório dos valores associados aos funcionários, considerando o período entre duas datas.

**Exemplo:**

**Valores Associados de funcionário cadastrados:**

Criado a fórmula **VALORFUNC('01','01/04/2006','30/06/2006')**:

**VALORFUNC('01','01/04/2006','30/06/2006')**

**1 - STRING '1':**Informar o código do valor associado que deseja resgatar;

**2 - DATA 1 '01/04/2006':** Informar a data de início do período que deseja resgatar;

**3 - DATA 2 '30/06/2006':**Informar a data de fim do período que deseja resgatar.

**Valor retornado na fórmula: 120,00 (único valor associado informado dentro do período solicitado).**

**VALORSEC (STRING, DATA1, DATA2)**

Retorna o somatório dos valores associados a seção do funcionário, considerando o período entre duas datas.

**Exemplo:**

**Valores Associados de seção cadastrados:**

 Criado a fórmula **VALORSEC('01','01/09/2011','30/09/2011')**:

**VALORSEC('01','01/09/2011','30/09/2011')**

**1 - STRING '1':**Informar o código do valor associado que deseja resgatar;

**2 - DATA 1 '01/09/2011':** Informar a data de início do período que deseja resgatar;

**3 - DATA 2 '30/09/2011':**Informar a data de fim do período que deseja resgatar.

**Valor retornado na fórmula: 150,00 (único valor associado informado dentro do período solicitado com o código 1).**

**VALORSIND (STRING, DATA1, DATA2)**

Retorna o somatório dos valores associados aos sindicato do funcionário, considerando o período entre duas datas.

**Exemplo:**

**Valores Associados de sindicato cadastrados:**

Criado a fórmula **VALORSIND('02','01/09/2011','30/09/2011')**:

**VALORSEC('02','01/09/2011','30/09/2011')**

**1 - STRING '02':**Informar o código do valor associado que deseja resgatar;

**2 - DATA 1 '01/09/2011':** Informar a data de início do período que deseja resgatar;

**3 - DATA 2 '30/09/2011':**Informar a data de fim do período que deseja resgatar.

**Valor retornado na fórmula: 0,30 (único valor associado informado dentro do período solicitado com o código 02).**

**VALENCARGOM (1º Parâmetro)**

Retornar o valor calculado em memória de um encargo com 'Ordem de Cálculo' maior.  
1º Parâmetro: Deverá informar o código do encargo de deseja obter o valor calculado em memória;

**Exemplo:**  
VALENCARGOM('0001')

O sistema irá retornar o valor calculado em memória do encargo '0001'.

Encargo 0001 - Encargo 0001

Fórmula de valor:  RC \* 0,08

Ordem de cálculo: 1

Encargo 0009 - Encargo 0009

Fórmula de valor: VALENCARGOM('0001') + 100

Ordem de cálculo: 2

**Observação:** Neste caso a 'Ordem de Cálculo' do encargo 'Encargo 0001' deverá ser menor que a 'Ordem de cálculo' do encargo 'Encargo 0009' e a 'Fórmula de valor' do encargo 'Encargo 0009' deverá conter a variável VALENCARGOM para recuperar o valor.

**Atenção: O campo 'Ordem do cálculo' somente estará disponível para encargos do tipo 'A - Valor calculado através de fórmula'.**

**VALENCARGO e VALPROVISAO13**

Para provisionar os valores de encargos de INSS de 13º salário referente ao período desonerados, foi criado duas funções de fórmulas, a saber:

VALENCARGO(MES, ANO, 'CodEncargo'): essa função retorna o valor de um encargo em uma data competência para o funcionário corrente;

VALPROVISAO13(MES, ANO): essa função retorna o valor da provisão do 13º salário somado à média de 13º salário para o funcionário corrente.

Mais informações:  [Função de Fórmula Encargos Reoneração](https://tdn.totvs.com/pages/releaseview.action?pageId=279164590)

**VFER**

Retorna o valor de um evento que se encontra no recibo de férias já cálculado.

sintaxe: VFER('Código do evento')

Retorno: Valor

Exemplo: VFER('0009') + VFER('0038')

Caso a variável de fórmula VFER seja utilizada no processo de cálculo de férias, é considerado o valor calculado em memória, e quando utilizada em qualquer outro processo, é considerado o valor do evento gravado no banco de dados, inclusive na provisão.  
Quando a variável é utilizada fora do cálculo de férias, são considerados os valores do recibo com a maior data de pagamento anterior ao último dia de competência atual.
