---
content_hash: 4325c9fe070c9be4abfed16a8feaf63a998a872f435f2e1ed2860d2921795050
fetched_at: '2026-06-29T00:09:31.847729+00:00'
page_id: '425458749'
product: rm
source: tdn-rm
title: Cancelamento do Contrato x Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458749
version: 19
---

---

Modelos de Contabilização1° Modelo ContabilizaçãoCancelamento de Contrato no 1° Modelo de Contabilização

Ao cancelar um contrato já contabilizado os seguintes procedimentos serão realizados:

**Se os lançamentos ainda estiverem no Lote N:**

* O lançamento referente à contabilização da provisão de contrato será estornado e contabilizado novamente na soma dos valores já apropriados, as apropriações mensais já contabilizadas serão mantidas.

Vejam a seguir a exemplo de contabilização:

Lançamento referente à contabilização do valor do contrato com 12 competências:as lançamentos inversos.

D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

 - Em **Julho** o aluno cancelou o contrato, com as sete competências do contrato já contabilizadas, a provisão do contrato será estonada e contabilizada com o valor das apropriações já realizadas.

Lançamento do valor atual do contrato:  
D – 1.1.2.04.01.001 – 7.000,00  
C – 2.1.7.01.01.001 – 7.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

**Observação:**Caso seja necessário cancelar o contrato sem manter as contabilizações já realizadas e não integradas ao lote 0, primeiramente estorno o contrato para depois cancelar.   
O sistema não permitirá a **exclusão** de um contrato, se a ele estiver vinculado algum lançamento contábil, mesmo que esta contabilização esteja '*Cancelada'.*

**Se os lançamentos já tiverem sido integrados ao lote oficial da contabilidade – Lote 0:**

* Os lançamentos do lote 0 (zero) referentes à contabilização terão seu status alterado para 'I = Incorreto.'
* No lote parametrizado no sistema para receber os lançamentos de estorno, serão gerados lançamentos inversos ou de estorno, sendo que estes lançamentos terão status 'E = Estorno'.

Vejam a seguir a exemplo de contabilização:

Lançamento referente à contabilização do valor do contrato com 12 competências:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

 - Em **Julho** o aluno cancelou o contrato, com as sete competências do contrato já contabilizadas, a provisão do contrato será estonada e contabilizada com o valor das apropriações já realizadas.

Estorno do lançamento referente à contabilização do valor do contrato:  
D – 2.1.7.01.01.001 - 12.000,00   
C – 1.1.2.04.01.001 - 12.000,00

Lançamento do valor atual do contrato:  
D – 1.1.2.04.01.001 – 7.000,00  
C – 2.1.7.01.01.001 – 7.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

**Observação:**  
O sistema não permitirá a **exclusão** de um contrato, se a ele estiver vinculado algum lançamento contábil, mesmo que esta contabilização esteja '*Cancelada'*, ou seja, se a contabilização de um contrato tiver sido realizada e integrada ao lote oficial da contabilidade – Lote 0, mesmo que esta contabilização seja cancela o contrato não poderá ser excluído, pois ainda existirão lançamentos contábeis, *Incorretos* e de *Estorno*, vinculados a ele.

2° Modelo ContabilizaçãoCancelamento de Contrato no 2° Modelo Contabilização

Ao cancelar um contrato já contabilizado os seguintes procedimentos serão realizados:

* O sistema irá avaliar o valor do contrato e deduzir as apropriações mensais realizadas e será contabilizado o valor da diferença com os lançamentos inversos.
* Os lançamentos referentes à contabilização de cancelamento terão seu status = 'C = Correto.' e Origem 'C = Cancelamento'.
* No cancelamento de contrato a data de contabilização será conforme abaixo:   
  - Ao informar a 'Data de cancelamento de contrato' o sistema irá gerar contabilização conforme o mês/ano informado (sempre considerando o último dia do mês).  
  - Não informando a 'Data de cancelamento de contrato', o sistema continuará considerando o mês/ano, porém do mês corrente para compor a data de contabilização

Vejam a seguir a exemplo de contabilização:

Lançamento referente à contabilização do valor do contrato com 12 competências:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

 - Em **Julho** o aluno cancelou o contrato com as sete competências do contrato já contabilizadas, será gerado uma contabilização de provisão de estorno no valor não contabilizado do contrato e as contabilização da provisão e apropriações serão mantidas.

Estorno do lançamento referente à contabilização do valor do contrato:  
D – 2.1.7.01.01.001 - 5.000,00   
C – 1.1.2.04.01.001 - 5.000,00

Lançamento do valor atual do contrato:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Sete lançamentos referente à contabilização de competência do contrato (mês 01 á mês 07):  
D – 2.1.7.01.01.001 – 1.000,00  
C – 3.1.1.01.01.001 – 1.000,00

**Observação:**O sistema não permitirá a **exclusão** de um contrato, se a ele estiver vinculado algum lançamento contábil, mesmo que esta contabilização esteja '*Cancelada'.*
