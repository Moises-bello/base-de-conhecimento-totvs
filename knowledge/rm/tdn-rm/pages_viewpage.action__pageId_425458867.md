---
content_hash: 52d6f0eca2f1f0d768bc21e1f01cf4b01e13f00792839e265cef361cebfc513e
fetched_at: '2026-06-29T00:09:32.528496+00:00'
page_id: '425458867'
product: rm
source: tdn-rm
title: Competência Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458867
version: 8
---

---

A competência contábil é a data que indica o período em que os serviços prestados aos alunos serão realmente realizados e contabilizados. Ela indica também o número de meses que os serviços serão prestados. Este número é utilizado para se calcular o valor a ser apropriado mensalmente.

A forma de pagamento dos alunos aos serviços prestados pelas instituições de ensino pode sofrer inúmeras variações, podendo ser, por exemplo, a vista ou a prazo em determinado número de parcelas. Este número de parcelas nem sempre é corresponde ao período contratado para a prestação do serviço, como no caso de cursos de curta duração ou cenários de pós-graduação, onde o valor do contrato pode ser dividido em um número de parcelas menor ou maior que a duração do curso. Esta variação se refere à *forma de pagamento* firmada entre o aluno e a instituição de ensino, e pode ser assim contabilizada a cada recebimento sendo reconhecida como contabilização por **regime de caixa**. A contabilização dos serviços prestados aos alunos pode ser feita, porém, pelo **Regime de Competência**, ou seja, independentemente da forma de pagamento adotada e da efetivação ou não destes recebimentos a contabilização será realizada sempre no período em que o serviço estiver realmente sendo prestado.

Para a realização da contabilização por competência, precisamos indicar para o sistema o período de competência em que os serviços serão prestados, conhecido como 'data contábil' ou 'período de competência contábil'. Esta data pode ser indicada em alguns locais no sistema, possibilitando às instituições de ensino uma flexibilização maior quanto à data informada para contabilização. O local escolhido pela instituição de ensino deve ser indicado nos parâmetros do sistema, *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade,* podendo ser no cadastro do '**Período Letivo**', na '**Parametrização por Curso**' ou no '**Contrato e Plano de Pagamento**'.

Se o local escolhido for:

**1 - Período Letivo**  
Dentro do cadastro do Período Letivo será habilitada uma aba chamada 'Contabilização', onde devemos informar o período de competência contábil, ou seja, o período em que os serviços serão prestados neste período letivo, preenchendo o mês/ano da competência inicial e o mês/ano da competência final.

**Atenção:**  
Dentro do cadastro do 'Período Letivo', devemos definir também se o período letivo está encerrado ou não para contabilizações, marcando ou não a opção "*Período Letivo encerrado para Contabilização*".   
Mesmo que o local indicado nos parâmetros do sistema para verificar o período de competência contábil seja o cadastro de '*Parametrização por Curso*' ou '*Contrato e Plano de Pagamento*', todas as vezes em que o processo de contabilização por competência for acionado, independentemente do local parametrizado, o sistema sempre irá validar esta opção, gerando contabilização apenas para os contratos cujos períodos letivos ***não*** estejam encerrados para contabilização.

Se o contrato tiver somente contabilização de provisão ou contabilização de provisão e apropriação, o sistema não possibilitará a modificação da data de competência contábil.

**2 - Parametrização por Curso**Dentro do cadastro da Parametrização por Curso será habilitada uma aba chamada 'Contabilização', onde devemos informar o período de competência contábil, ou seja, o período em que os serviços serão prestados para esta parametrização, preenchendo o mês/ano da competência inicial e o mês/ano da competência final.

Se o contrato tiver somente contabilização de provisão ou contabilização de provisão e apropriação, o sistema não possibilitará a modificação da data de competência contábil.

**3 - Contrato e Plano de Pagamento**  
Dentro dos cadastros do *Contrato* e do *Plano de Pagamento* será habilitada uma aba chamada 'Contabilização', sendo que escolhendo esta opção devemos informar o período de competência contábil em pelo menos um destes dois cadastros e o sistema irá proceder da seguinte forma:

− Se o período de competência contábil for informado dentro do *Plano de Pagamento*, todo novo Contrato vinculado a este plano de pagamento receberá este mesmo período de competência como default. Porém, se a contabilização por competência ainda não tiver sido realizada para o Contrato e, no perfil associado ao usuário, a opção "*Permite alteração de data contábil do contrato*" estiver habilitada, o período de competência contábil do Contrato poderá ser alterado, prevalecendo sempre neste caso o período contábil informado dentro do Contrato.

Se o sistema estiver parametrizado para verificar a competência no cadastro de **'Contrato e Plano de Pagamento'** e se o período de competência contábil ainda não estiver definido dentro destes cadastros, ao realizar processos no sistema, tais como algum dos processos de matrícula/rematrícula, alteração de situação de matrícula e etc, que utilizam contrato do aluno/plano de pagamento, o período de competência será solicitado no momento da realização de tais processos.

O período de competência, como falado inicialmente, além de indicar o período em que os serviços serão prestados, realizados e contabilizados, indica também o **número de meses** em que o serviço contratado será prestado, sendo ele igual ao número de meses existentes entre a data inicial e a data final que foi indicada na competência contábil.

Este número é de suma importância, pois será utilizado para se encontrar o valor a ser apropriado mensalmente, exceto quando a '**Data do contrato**' for posterior ao mês inicial da competência contábil. Veja o exemplo abaixo:

Competência - Mês/Ano Inicial: 01/2015  
Competência - Mês/Ano Final  : 12/2015  
Data do Contrato: **03/03/2015**  
Valor do contrato a ser contabilizado: 12.000,00

Neste caso, os serviços serão prestados em um período de **10 meses** (mês da Data do contrato até o Mês/Ano Final da competência | mês **03** até mês 12 = 10 meses), sendo então o valor contratado de 12.000,00 dividido e contabilizado em 10 meses ou 10 competências. Neste exemplo, o primeiro mês a ser contabilizado será referente à competência **03/2015** e será no valor de 1.200,00 (12.000,00 / 10 meses) e, à medida que os serviços forem sendo realizados, deverá ser executada a contabilização para as próximas competências que serão realizadas no valor de 1.200,00 cada até o final do período contábil.

**Observações**− Se a 'Data do contrato' estiver em *branco* ou for *menor* que o Mês/Ano inicial da competência, a data inicial indicada na competência contábil é que será considerada para os cálculos e para a contabilização.  
− Se a 'Data do contrato' for *maior* que o Mês/Ano final da competência, significa que este contrato não poderá ser contabilizado pelo sistema, pois o período de realização da prestação dos serviços contratados já finalizou.

Na versão 2310 ou superiores

O sistema permite alterar a data de competência inicial para uma data superior ou igual a data da contabilização de provisão do contrato. No entanto, caso a data considerada seja menor do que a data da contabilização de provisão do contrato, não será possível alterar a data e a mensagem "A data da competência inicial *Data de Competência Inicial* é menor do que a data da provisão *Data de Provisão da Contabilização do Contrato*" com as informações consideradas da data será exibida.

Se o contrato tiver contabilização de provisão e apropriação, o sistema não possibilitará a modificação da data de competência contábil.
