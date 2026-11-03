---
content_hash: 080b3aadf9cfaf17bae69ed59b5fd7f57cab31752b975b497138753d6198aa19
fetched_at: '2026-06-29T00:10:25.400267+00:00'
page_id: '504807048'
product: rm
source: tdn-rm
title: Como identificar qual registro deu origem à Lotação Tributária?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504807048
version: 2
---

# Objetivo:

---

       O objetivo deste documento é informar quais validações devem ser realizadas para identificar o registro que deu origem à Lotação Tributária.

---

Lotação tem o conceito estritamente tributário e não físico e influi no método de cálculo da contribuição previdenciária para um grupo de segurados específicos, não refletindo, necessariamente, o local de trabalho do empregado. Identifica a classificação da atividade para fins de atribuição do código FPAS, a obra de construção civil, o contratante de serviço, ou uma condição diferenciada de tributação. A condição diferenciada ocorre quando uma determinada unidade da empresa possui um código de FPAS/Outras Entidades e Fundos distintos.

Desta forma, o sistema irá gerar lotações conforme abaixo:

LotaçãoEmpresas que não utilizam tomadores de serviços

A lotação tributária será somente uma visão do cadastro de seções centralizadoras de CNPJ e FPAS.  
  
Será gerado:

1 registro para cada **seção centralizadora** de CNPJ

Ou em caso de uso de quebra de FPAS:

1 registro para cada **seção** que se enquadre na **quebra de FPAS**

**Exemplos:**

Sem quebra de FPAS

- **Estrutura de seção** (centralizadoras)  
Neste caso, utilizamos o mesmo FPAS para todos as seções dentro da centralizadora, ou seja, as seções 01.01, 01.02, etc. possuem o mesmo FPAS da centralizadora 01. O mesmo se aplica as demais seções.

- Menu **Configurações | Parametrizador | eSocial | Lotação Tributária**

Além disso, no parametrizador foi indicado que não há quebra de FPAS.

- **Lotação tributária**

Ao gerar a lotação tributária, o sistema irá gerar um registro para cada centralizadora.

Com quebra de FPAS

- **Estrutura de seção**

Nesta estrutura, o FPAS da seção 01.02 é diferente da centralizadora: Centralizadora - FPAS 515 / Seção 01.02 - FPAS 574.

- Menu **Configurações | Parametrizador | eSocial | Lotação Tributária**

Como a quebra de FPAS é no último nível de seção, informamos o código de quebra com a mesma quantidade de caracteres deste nível.

- **Lotação tributária**

Note que na coluna FPAS é preenchida com os códigos de FPAS presentes em cada seção. A seção 01.02, por exemplo, possui FPAS diferente das demais.

Empresas que utilizam tomadores de serviços

Quando o FPAS não está somente na filial/seção onde o funcionário é alocado, ou seja, exitem também informações de tributos vinculados aos tomadores de serviços associados ao funcionário, será necessário criar uma máscara para que o sistema monte o código da Lotação.

Assim, será gerado:

1 registro para cada **seção centralizadora+tomador global** +   
1 registro para cada **seção centralizadora+tomador** em que houver tomador alocado para algum funcionário

Ou em caso de uso de quebra de FPAS:

1 registro para cada **seção+tomador global** +   
1 registro para cada **seção+tomador** em que houver tomador alocado para algum funcionário +   
1 registro para cada **seção** que se enquadre na **quebra de FPAS**

**Exemplos:**

Sem quebra de FPAS

- **Estrutura de seção** (centralizadoras)  
Neste caso, utilizamos o mesmo FPAS para todos as seções dentro da centralizadora, ou seja, as seções 01.01, 01.02, etc. possuem o mesmo FPAS da centralizadora 01. O mesmo se aplica as demais seções.

- Menu **Configurações | Parametrizador | eSocial | Lotação Tributária**

Além disso, no parametrizador foi indicado que não há quebra de FPAS.

- **Lotação tributária**

Ao gerar a lotação tributária, o sistema irá gerar um registro para cada **centralizadora+tomador global** e um registro para cada **centralizadora+tomador** que possua funcionário alocado em tomador.

Com quebra de FPAS

- **Estrutura de seção**

Nesta estrutura, o FPAS da seção 01.02 é diferente da centralizadora: Centralizadora - FPAS 515 / Seção 01.02 - FPAS 574.

- Menu **Configurações | Parametrizador | eSocial | Lotação Tributária**

Como a quebra de FPAS é no último nível de seção, informamos o código de quebra com a mesma quantidade de caracteres deste nível.

- **Lotação tributária**

Note que na coluna FPAS é preenchida com os códigos de FPAS presentes em cada seção. É gerado um registro para cada seção+tomador global e um registro para cada seção+tomador das seções em que tenham funcionários alocados em tomador.
