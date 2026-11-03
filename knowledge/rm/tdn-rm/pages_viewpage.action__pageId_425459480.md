---
content_hash: bcd47c438e68fac95b9ba338ef12ffa8b4c917a1a25dc7eb20ce1e263116df38
fetched_at: '2026-06-29T00:09:36.195007+00:00'
page_id: '425459480'
product: rm
source: tdn-rm
title: Concessão de bolsas futuras - Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459480
version: 10
---

A concessão de bolsa futura permite a instituição de ensino fazer o planejamento das [bolsas](http://tdn.totvs.com/display/LRM/Bolsas+-+Educacional) que serão disponibilizadas a determinados alunos de maneira a atender possíveis campanhas de matrícula e/ou regras próprias de negócio.  
Durante a inclusão de um novo  o sistema verifica se existem bolsas futuras planejadas para aquele aluno naquela habilitação e automaticamente inclui as bolsas previstas no seu contrato.

Ao cadastrar as concessões de bolsas futuras para cada aluno, indique a **Validade** para a sua aplicação através da indicação da *data inicial* e a *data final*. Assim, se a data de vencimento das parcelas estiver dentro desta Validade, a bolsa será concedida para tais parcelas. As informações sobre o **Desconto** serão apresentadas conforme definido no cadastro da bolsa, podendo ser alteradas neste momento desde que no cadastro da referida bolsa a opção *'Permite alterar valor'* esteja marcada.

Por default, ao cadastrar uma concessão de bolsa futura, a opção "**Todos os serviços**" virá *desmarcada*, restringindo assim a sua aplicação aos serviços que deverão ser associados em seguida acessando *'Anexos|Serviços da concessão de bolsas futuras'* e adicionando um a um os serviços presentes nos contratos que irão receber o benefício da bolsa. Se desejar incluir a concessão de bolsa futura com esta opção *marcada*, o sistema concederá as bolsas futuras cadastradas para todos os serviços presentes nos contratos dos alunos.

Além disso é primordial definir qual será a matriz aplicada correspondente, sem a definição da habilitação da concessão da bolsa futura não é possível o cadastro automático da bolsa no contrato do aluno. Para isto acesse *'Anexos|Habilitação da concessão de bolsas futuras'* e inclua as matrizes aplicadas.

A opção "**Concessão ativa**" por default será apresentada sempre *marcada*, indicando assim que as bolsas futuras previamente cadastradas serão sempre incluídas para os alunos no momento em que novos contratos forem incluídos ou mediante quaisquer alterações efetuadas no cadastro das  dos contratos, pois ao salvá-las o sistema sempre irá verificar antes se existe concessão de bolsa futura para o aluno em questão. Se esta opção estiver *desmarcada*, o sistema não realizará o cadastro automático da bolsa para o aluno no momento de inclusão do contrato nem nas manutenções, necessitando que o usuário informe a bolsa para o aluno de forma manual.

**Exemplo:**  
Aluno possui duas concessões cadastradas para a mesma bolsa com percentuais e período de validade diferentes e a opção "Concessão ativa" está marcada:  
-'Bolsa Diretoria' **(20%)** - serviço **Mensalidade** do período de **10/03/2017** a **10/04/2017** -'Bolsa Diretoria' **(50%)** - serviço **Mensalidade** do período de **10/05/2017** a **10/06/2017**   
Aluno realizou matrícula e contrato foi incluído com 6 parcelas para o serviço Mensalidade.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parcela | Valor | Vencimento | Bolsa | Valor lançamento gerado |
| 1 | R$ 1.000,00 | 10/01/2017 |  | R$ 1.000,00 |
| 2 | R$ 1.000,00 | 10/02/2017 |  | R$ 1.000,00 |
| 3 | R$ 1.000,00 | **10/03/2017** | Bolsa Diretoria(20%) | R$   800,00 |
| 4 | R$ 1.000,00 | 10/04/2017 | Bolsa Diretoria(20%) | R$   800,00 |
| 5 | R$ 1.000,00 | 10/05/2017 | Bolsa Diretoria(50%) | R$   500,00 |
| 6 | R$ 1.000,00 | 10/06/2017 | Bolsa Diretoria(50%) | R$   500,00 |

O desconto da bolsa foi concedido apenas à partir da 3ª parcela, já que o período da concessão não contempla as datas de vencimento da 1ª e 2ª parcela. Mesmo o contrato tendo sido assinado no dia 01/01/2017, o sistema irá levar em consideração a data de vencimento da parcela e não da assinatura do contrato para conceder a bolsa para a parcela. A **Bolsa** **Diretoria (20%)** foi concedida para a 3ª e 4ª parcela e a **Bolsa Diretoria (50%)** foi concedida para a 5ª e 6ª parcela.

É possível também definir a "Ordem de Aplicação do Desconto por Antecipação" no campo  durante o cadastro de uma concessão de bolsa futura. Esse campo tem o objetivo de informar se o valor do desconto por antecipação será calculado antes ou depois do cálculo do valor da bolsa inserida no contrato via concessão de bolsas futuras. Saiba mais acessando o documento técnico na guia "Ordem de Aplicação do desconto por Antecipação" na seção 'Concessão de Bolsas futuras'.

Ao setar o campo citado acima para ordem de aplicação do desconto por antecipação como "Depois do cálculo da bolsa, será habilitado o campo "Afeta base de cálculo" que indicará se a bolsa a ser inserida pela concessão de bolsa futura afetará a base de cálculo para as próximas bolsas a serem calculadas bem como para o desconto por antecipação a ser calculado posteriormente. Mais informações poderão ser acessadas na guia "Afeta Base de Cálculo do Desconto Por Antecipação" -> "Concessão de Bolsas Futuras" no TDN em [desconto por antecipação](http://tdn.totvs.com/pages/viewpage.action?pageId=325847718).

Como foi explicado, através do menu *Financeiro/Contábil | Bolsas | Concessão de bolsas futuras*, as bolsas futuras devem ser cadastradas uma a uma para os alunos, indicando-se entre outros dados, a validade, os serviços que receberão os benefícios e as matrizes aplicadas.

Para qualquer inclusão/alteração de parcelas no contrato, o sistema irá verificar se existe concessão para aquela parcela verificando se o vencimento da parcela está dentro do período da concessão.

**Atenção**As validades das concessões de bolsa futura são sempre atribuídas por **período**. Já as bolsas no contrato do aluno podem ser incluídas por **período** ou por **parcela**, então, sempre que uma parcela for alterada ou incluída, o sistema irá verificar se existe alguma concessão de bolsa futura cadastrada para o aluno no período correspondente ao da parcela e, caso exista, inclui a bolsa da concessão futura no contrato do aluno, mas antes verifica se no contrato do aluno esta bolsa já está incluída e, caso esteja, verifica a validade desta bolsa. Neste caso, se a bolsa no contrato foi atribuída por parcela, verifica a data de vencimento corresponde a esta parcela para somente então verificar se este período coincide ou não com o período da concessão, incluindo-a caso não coincida.

**Exemplo 1:** - Concessão de bolsa futura atribuída para a Bolsa X para o período de *01/01/2017 a 31/06/2017*. - Contrato do aluno possui 12 parcelas com vencimento para o 5º. dia de cada mês. - A mesma Bolsa X está atribuída no contrato do aluno somente para a Parcela 2 cuja data de vencimento = *05/02/2017*. =>Se esta **parcela 2** for alterada, a Bolsa futura X **não** será incluída pois apesar da data de vencimento da parcela 2 estar compreendida no período de validade da Bolsa futura X, no contrato do aluno já existe esta mesma Bolsa X cuja validade correspondente (*05/02/2017*=data de vencimento da parcela 2) está compreendida no período de validade da concessão (*01/01/2017 a 31/06/2017*).

**Exemplo 2:** - Concessão de bolsa futura atribuída para a Bolsa X para o período de *01/07/2017 a 31/12/2017*. - Contrato do aluno possui 12 parcelas com vencimento para o 5º. dia de cada mês. - A mesma Bolsa X está atribuída no contrato do aluno somente para a Parcela 2 cuja data de vencimento = *05/02/2017*. =>Se a **parcela 8** for alterada, a Bolsa futura X **será** incluída para o período de *01/07/2017 a 31/12/2017* pois a data de vencimento da parcela 8 (05/08/2017) está compreendida na data de validade da concessão e além disso, a Bolsa X que já existe no contrato do aluno corresponde a um período diferente da concessão (*05/02/2017*=data de vencimento da parcela 2).

Como facilitador, o sistema possui o processo de  que possibilita que o usuário faça a concessão da bolsa futura utilizando uma série de filtros, otimizando assim o cadastro.

**Observações:**

* Na inclusão de concessão da bolsa futura, quando o aluno possuir matrícula em mais de uma matriz curricular que esteja ativa ou quando a matriz curricular possuir mais de um turno associado, o usuário deverá selecionar a matriz desejada para a inclusão da bolsa futura.
* As bolsas futuras somente serão incluídas nos contratos dos alunos se no cadastro das referidas concessões houver a indicação da matriz aplicada à qual poderão ser vinculadas, assim como as referidas bolsas devem estar devidamente associadas ao período letivo dos alunos.
* Se houver uma concessão com o parâmetro  "Todos os serviços"  marcado, o sistema não permitirá inclusão de nova concessão, no mesmo período, com serviço definido em "Anexos >  Serviços da concessão de bolsas futuras".
* Na inclusão de concessão da bolsa futura, caso o período de competência contábil já estiver preenchido no cadastro da **Bolsa | Bolsas por período letivo**, ao realizar a matricula do aluno criando contrato será adicionada a bolsa já com o período de competência contábil.

Importante

* O filtro de matriz aplicada, disponível no anexo **"Habilitações da concessão de bolsas futuras"** e na etapa de detalhes da bolsa no processo **"Assistente de concessão de bolsas futuras"** exibirão sempre as matrizes do aluno com status "Ativa" e "Atual".
* É necessária a exibição dos dois status devido a necessidade de se lançar uma bolsa futura para um aluno que teve sua transferência interna para uma disciplina em uma turma que pertence a uma matriz antiga.

 Informações Complementares

---

Bolsas
