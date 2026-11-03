---
content_hash: ce68b0208d6500b1cfdd56d79b275cdca96afa15905b18a340f4734db49c658d
fetched_at: '2026-06-29T00:10:13.173102+00:00'
page_id: '454843946'
product: rm
source: tdn-rm
title: Reajuste de Preços (Contratos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454843946
version: 8
---

O processo de reajuste de contratos será realizado através do processo "Reajuste de Preço" localizado em "Manutenção de contrato | Processos → Reajuste de Preço".

O processo de "Reajuste de Preços" tem como premissa a utilização de uma fórmula de reajuste, essa fórmula pode ser a IUR ou IUR2, a única diferente entre elas é que na IUR2 o campo "Data do Reajuste" também pode ser preenchido por uma função de fórmula além de valor fixo.

Na fórmula IUR ou IUR2 deve ser informando os seguintes parâmetros:

* Data do reajuste
* Índice base utilizado para o reajuste do contrato ("Obrigatório que seja utilizado um índice").
* Número de meses para o reajuste
* Defasagem da moeda
* Dia da cotação do índice base

Exemplos de fórmula:

* IUR ( ‘01/09/2010’, 'IPCA' , 6 , 0 , 11)
* IUR2 (DAT , 'IGPM' , 3 , 0 , 1), (nesta fórmula  a variável DAT é a data de hoje)
* IUR ( ‘20/09/2017’, 'SELIC' , 6 , 0 , 11)

O processo irá reajustar as parcelas de cada item do contrato de acordo com os dados informados na fórmula e realizará a atualização do preço de arrendamento de acordo com os novos valores.

#### Histórico de Reajustes:

Todos os reajustes realizados para cada item de contrato pode ser verificado na tela ‘Reajustes’ na aba de ‘Informações adicionais’ do item de contrato:

**Importante**: O campo "Data Último Reajuste" é preenchido automaticamente através do processo "Reajuste de Preço", e indica até onde o contrato já foi reajustado. No entanto esse campo também pode ser preenchido manualmente para desconsiderar reajuste até a data determinada ou para permitir novo reajuste em intervalo já reajustado.

**Observação**: Se o campo "Data Último Reajuste" for preenchido com a mesma data de reajuste do processo "Reajuste de Preço" nenhum reajuste vai ser efetivado.

## **IUR e IUR2 - Entendimento detalhado do comportamento da fórmula de reajuste:**

**Parâmetro (Data do reajuste):**

A data do reajuste é utilizada para determinar um ponto de intersecção, desse ponto para frente determina-se o que falta faturar como valor reajustável do contrato.

**Índice base utilizado para o reajuste do contrato ("Obrigatório que seja utilizado um índice"):**

Se for utilizado uma moeda não vai ocorrer reajuste pois o fator de reajuste só é calculado com base em índice.

O índice é utilizado para calcular o fator de atualização, o fator é determinado sempre utilizando o índice do mês de referência e o mês anterior.

Exemplo:

Considerando a tabela acima, se a data de referência for "01/07/2022" o fator de atualização vai ser calculado entre os índices 4,05 e 4,06

**Número de meses para o reajuste:**

Considerando um reajuste sendo realizado com a fórmula IUR ( ‘01/08/2022’, 'IPCA' , 2 , 0 , 1) os dois meses de reajuste seriam 08/2022 e 07/2022

Sempre considera a data de referência do reajuste e volta o número de meses definido como reajuste.

Em cada data de reajuste, neste caso 01/08/2022 e 01/07/2022 é calculado um fator de reajuste

* + 01/08/2022 → Vai calcular o fator considerando a diferença de índice entre 01/07/2022 e 01/08/2022.
  + 01/07/2022 → Vai calcular o fator considerando a diferença de índice entre 01/06/2022 e 01/07/2022.

A cada mês considerado neste processo, o fator de reajuste é aplicado ao valor a faturar do contrato, neste caso iriamos calcular e aplicar o fator duas vezes.

**Defasagem da moeda:**

A defasagem da moeda desloca o mês de referência do cálculo do índice em uma quantidade de meses igual a defasagem.

Com uma defasagem igual a zero (0) e mês de referência igual a 01/08/2022 → Vai calcular o fator considerando a diferença de índice entre 01/07/2022 e 01/08/2022.

Com uma defasagem igual a três (3) e mês de referência igual a 01/08/2022 → Vai calcular o fator considerando a diferença de índice entre 01/04/2022 e 01/05/2022.

**Dia da cotação do índice base:**

Indica em relação aos meses em que o reajuste de preço vai ser feito em qual dia do mês ele vai pesquisar o índice.

**Permissões**:

O processo de "**Reajuste de Preços**", conta com recurso de segurança e seu acesso precisa ser liberado através de permissão no perfil associado ao usuário.
