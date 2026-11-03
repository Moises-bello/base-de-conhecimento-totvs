---
content_hash: a85666be99bee72f797f63cfab616ffe29491b8a7ddab48f0c2d03ec45bde8e3
fetched_at: '2026-06-29T00:09:36.810782+00:00'
page_id: '425459524'
product: rm
source: tdn-rm
title: Incluir / Excluir Bolsa Retroativa – Criando lançamentos de devolução / Movimentando
  a Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459524
version: 43
---

---

A Inclusão/Exclusão de Bolsa Retroativa é um recurso oferecido pelo sistema para permitir que as instituições de ensino possam incluir ou excluir bolsas para os seus alunos após os lançamentos financeiros das parcelas dos alunos já terem sido gerados ou até mesmo após os respectivos boletos já terem sido baixados, permitindo assim que as instituições possam conceder ou retirar bolsas retroativamente às parcelas já processadas.  
   
O sistema disponibiliza dois modelos para se trabalhar com Bolsas Retroativas. Aqui falaremos somente sobre o modelo em que os lançamentos originais ***não*** serão alterados e a inclusão ou exclusão de bolsa retroativa serão registradas separadamente, possibilitando assim um histórico dos fatos ocorridos.



Para que o sistema considere este modelo como padrão primeiramente é necessário **marcar** a opção **'Usar bolsa retroativa sem alterar parcelas já baixadas'** disponível no menu *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 1/3*. Esta opção **marcada** indicará a utilização deste modelo e, caso esteja desmarcada, indicará que a instituição de ensino estará utilizando o outro modelo que altera o próprio lançamento já baixado para incluir ou excluir as bolsas retroativas. C[lique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425459541), para saber mais informações sobre os parâmetros.   
  
Após a indicação de utilização deste modelo marcando a opção anterior, ao incluir ou excluir uma bolsa pelo processo de Bolsa Retroativa, aplicada em parcelas cujos lançamentos financeiros já tenham sido gerados, o sistema poderá seguir entre dois caminhos distintos para registrar os valores destas bolsas: ele poderá incluir lançamentos financeiros para devolver ou para cobrar os valores referentes às bolsas incluídas ou excluídas retroativamente ou então poderá atualizar automaticamente a Conta Corrente dos alunos com estes valores.

Escolha a forma desejada de utilização optando entre as duas opções a seguir:

* **Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)\***
* **Utilizar a movimentação em conta corrente\***
* **Usar devoluções pendentes após término de contrato nos próximos contratos\***

Uma vez já definido se ao incluir/excluir bolsas retroativamente o sistema irá criar os respectivos lançamentos a pagar ou a receber para registrar as bolsas ou se irá atualizar automaticamente a Conta Corrente do aluno, agora é necessário definir a forma que o sistema irá adotar para devolver efetivamente os créditos ou cobrar os débitos referentes às bolsas incluídas ou excluídas retroativamente.

Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)

Caso tenha optado anteriormente por utilizar a opção '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**' serão incluídos lançamentos financeiros para registrar a devolução ou a cobrança. Será necessário agora definir a forma como o sistema irá aproveitar os créditos gerados com a inclusão de bolsas retroativas e também definir a forma de cobrança dos débitos gerados com a exclusão de bolsas aplicadas retroativamente:

Criar devolução de créditoCriar devolução de créditoInclusão de bolsaInclusão de bolsaInclusão de bolsa

A inclusão de uma bolsa retroativa aplicada em parcela que já possui lançamento gerado irá resultar na inclusão de lançamentos financeiros de devoluções a pagar com o valor da bolsa incluída retroativamente. No contrato do aluno, na parcela e na bolsa concedida serão incluídos registros para consultas futuras com as informações da inclusão da bolsa, indicando, entre outras informações, o valor total dos créditos gerados e, à medida que o crédito for efetivamente devolvido este valor será atualizado sendo apresentado o valor ainda pendente (restante) dos créditos (tela de cadastro do Contrato e Bolsa do contrato, aba '*Valores de crédito/débitos gerados'*). Além disso, para cada movimentação realizada serão incluídos também registros com informações de rastreabilidade que poderão ser acessadas nos caminhos:  
(*Contrato | Anexos | Rastreabilidade de bolsa retroativa)*  
(*Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa*)  
(*Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa*)  
  
Agora será necessário definir os dados a serem utilizados na inclusão destes lançamentos financeiros de devolução criando uma configuração padrão e também direcionar a forma como o sistema irá fazer o aproveitamento destes créditos. Estas opções estão disponíveis em *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 2/3 – aba Parâmetros gerais*.  
  
Escolha entre uma das três formas disponibilizadas para o aproveitamento do crédito. A forma aqui escolhida será adotada como default (padrão) quando o processo de *'Inclusão de Bolsa Retroativa'* for executado, podendo, no entanto, conforme permissão especial, ser alterada durante a sua execução.

**- Aplicar devolução no lançamento da primeira parcela em aberto**  
**- Dividir devolução pela quantidade de parcelas restantes**  
**-****Devolver em espécie**

**Importante:**  
Foi criada uma permissão especial no cadastro de Perfil do usuário (*Perfil | Anexos | Parâmetros educacionais | <<aba>> Financeiro/Bolsa Retroativa | **Alterar parâmetros de comportamento padrão na geração de devoluções***) que ficará disponível caso a opção escolhida para se trabalhar com Bolsa Retroativa seja '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**'. Se esta permissão for marcada nos perfis, no momento da execução do processo de *'Inclusão de Bolsa Retroativa'* as opções previamente definidas nos parâmetros do sistema serão apresentadas na tela do processo, dando a você a oportunidade de confirmar ou alterar a forma de aplicação dos créditos gerados.

**Observações**− Ao executar o processo '*Incluir Bolsa Retroativa*' o sistema irá verificar se as parcelas indicadas no processo possuem lançamentos financeiros gerados e, caso haja lançamentos gerados será aplicada uma Bolsa Retroativa, caso não, será aplicada uma Bolsa normal e, no cadastro das bolsas aplicadas nos contratos, será gravada a informação com a origem da bolsa.  
− As regras para inclusão de bolsas em contratos serão mantidas, não sendo permitida a inclusão de bolsas em contratos *Cancelados* e em contratos gerados por *Acordo*.  
− As parcelas com lançamentos já gerados não serão alteradas. Na inclusão de Bolsas Retroativas para esses casos, serão calculados os valores a serem devolvidos e um lançamento a pagar, de *devolução* de crédito, será criado.  
− Os créditos criados pela inclusão de Bolsa Retroativa, de acordo com a parametrização realizada para aproveitamento do crédito, poderão ser aproveitados através da inclusão de *'Vínculos'* criados nos lançamentos financeiros das parcelas que tiverem status 'Em aberto', assim estes lançamentos terão um crédito vinculado.  
− A inclusão e Bolsa Retroativa em parcelas que possuem lançamentos financeiros com status 'Baixado' irão gerar normalmente os lançamentos financeiros de *devolução*, porém estes lançamentos de crédito não poderão ser vinculados aos lançamentos financeiros destas parcelas pois o *'Vínculo'* somente pode ser feito em lançamentos financeiros ainda 'Em aberto'. Outro ponto que vale ressaltar: nos casos que a parcela possuir algum lançamento originário de uma bolsa de outro sacado, esses lançamentos não serão considerados na geração de lançamento para devolução, mesmo se estiverem com status 'Baixado'.   
−  Na baixa e no cancelamento da baixa do valor não vinculado do lançamento financeiro de devolução criado pela bolsa retroativa (novo modelo), será atualizado o valor restante do crédito no contrato. Na baixa do valor não vinculado do lançamento de devolução o valor da baixa estará preenchido e o valor vinculado será igual a zero. Quando baixamos o valor vinculado, o valor da baixa é igual a zero e o valor vinculado é preenchido. Desta forma, o serviço irá receber o valor vinculado e o valor baixado.

**Importante:**  
No cadastro do **'Serviço'** existe uma opção que define se os lançamentos financeiros referentes a estes serviços poderão aproveitar ou não os valores de crédito/débito originados de Bolsa Retroativa através da inclusão de *'Vínculos'* nos lançamentos envolvidos, possibilitando que este valor possa ser abatido do valor original do lançamento da parcela. Se desejar que o sistema ***não*** aproveite estes valores nos lançamentos financeiros de determinado serviço, edite o cadastro do respectivo serviço e *marque* a opção .

Exclusão de bolsaExclusão de bolsaExclusão de bolsa

A exclusão de bolsa retroativa aplicada em parcela que já possui lançamento gerado irá resultar na inclusão de novas parcelas nos contratos dos alunos para gerar as cobranças referentes aos valores não cobrados. No contrato do aluno e na bolsa serão incluídos registros para consultas futuras com as informações da exclusão da bolsa e dos débitos e também informações com a rastreabilidade das movimentações com Bolsa Retroativa.   
  
É necessário agora definir os dados a serem utilizados na inclusão destas parcelas de cobrança criando uma configuração padrão e também direcionar a forma como o sistema irá fazer a cobrança destes débitos. Estas opções estão disponíveis em *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 3/3 – aba Parâmetros gerais.*  
  
Escolha entre uma das duas formas disponibilizadas para cobrança do crédito devolvido. A forma aqui escolhida será adotada como default (padrão) quando o processo de *'Exclusão de Bolsa Retroativa'* for executado, podendo, no entanto, conforme permissão especial atribuída no cadastro de Perfil do usuário, ser alterada durante a sua execução.

**- Gerar uma única parcela para o pagamento**  
**- Dividir pela quantidade de parcelas restantes****Importante:**− Se a exclusão de Bolsa Retroativa estiver sendo aplicada em parcela que ainda não possui lançamento financeiro gerado, o sistema irá somente 'Inativar' a bolsa.  
− Se a bolsa que estiver sendo excluída retroativamente for uma *bolsa de crédito*, o lançamento financeiro referente ao crédito do outro sacado será cancelado.  
− Não será permitida a exclusão de *bolsa de crédito* que possuir *Repasses* cadastrados.

Exclusão da parcela criada por exclusão de bolsa retroativaExclusão da parcela criada por exclusão de bolsa retroativaExclusão da parcela criada por exclusão de bolsa retroativa

Na exclusão de uma bolsa retroativa, o sistema cria uma ou mais parcelas no contrato do aluno com a finalidade de se cobrar bolsas excluídas de lançamentos já gerados (baixados ou não) que fizeram com que o valor a ser pago pelo aluno fosse menor do que deveria.

Havendo necessidade de exclusão dessa parcela de cobrança, foi criado o processo de exclusão da parcela criada por exclusão de bolsa retroativa. A exclusão dessas parcelas geradas pela exclusão da bolsa retroativa não são tratadas como exclusão de parcelas comuns tendo em vista a necessidade de se desfazer todo o processo de exclusão de bolsa retroativa que deu origem à(s) mesma(s).

Não será permitida a exclusão de uma parcela com lançamento gerado. Esse comportamento é o mesmo comportamento da exclusão de uma parcela comum. Para que prossigamos com a exclusão da parcela, o(s) respectivo(s) lançamento(s) deverão ser excluídos.

Após o cancelamento e exclusão do lançamento financeiro deve ser excluída a parcela do contrato originada por exclusão de bolsa retroativa, concluída a exclusão a bolsa retroativa será reativada.

**Importante:**O lançamento financeiro de bolsa de crédito que foi cancelado pelo processo de exclusão de bolsa, deve ser regeradas novamente para que o lançamento de bolsa seja recriado.

ATENÇÃO

A contabilização gerada pelo cancelamento da exclusão de bolsa retroativa, para excluir a parcela gerada pela exclusão de bolsa retroativa, sugerimos que seja realizado o estorno de toda a contabilização.

Utilizar a movimentação em conta corrente

Caso tenha optado anteriormente pela opção **'Utilizar a movimentação em conta corrente'**, as demais opções do parametrizador sobre Bolsa Retroativa ficarão desabilitadas, pois adotando esta forma de utilização dos valores referentes às bolsas incluídas ou excluídas retroativamente, aplicadas em parcelas que já possuem lançamentos financeiros gerados, não haverá inclusão de lançamentos financeiros de *devolução*, e os créditos ou débitos gerados através da inclusão ou exclusão de Bolsas Retroativas serão lançados automaticamente na Conta Corrente dos alunos.   
  
Os lançamentos financeiros originais continuarão *não* sendo alterados.  
  
Os valores lançados automaticamente na Conta Corrente dos alunos referentes à Bolsa Retroativa poderão ser aproveitados futuramente, seja na geração do lançamento financeiro da próxima parcela do contrato, incluindo um  valor a menor ou a maior ou na execução do processo específico que aproveita estes valores através da inclusão direta de lançamentos financeiros a pagar ou a receber, conforme a natureza dos valores, mas para que a Conta Corrente dos alunos possa ser manipulada desta forma, os parâmetros referentes à *'**[Cobrança Retroativa](http://tdn.totvs.com/pages/viewpage.action?pageId=309397070)**'* deverão estar também devidamente configurados. Se necessitar de maiores detalhes sobre esta parametrização e a sua utilização, favor consultar o help do sistema referente à .

Importante

Lembramos mais uma vez que após a inclusão ou exclusão de alguma bolsa pelo processo de Bolsa Retroativa, esta opção ficará desabilitada, não sendo mais possível mudar a forma de trabalho!

   Recursos Adicionais

---

[Passo a Passo - Inclusão e Exclusão de Bolsas Retroativas](http://tdn.totvs.com/pages/viewpage.action?pageId=317301097)

[Fórmula para contabilização de lançamento - TOTVS Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=555850129)
