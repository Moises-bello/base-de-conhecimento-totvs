---
content_hash: 7028371037d4d10392199c245a0ad701e120abde4af7649b83a0981e9a12cb9c
fetched_at: '2026-06-29T00:09:36.123972+00:00'
page_id: '425459470'
product: rm
source: tdn-rm
title: Conta Corrente do aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Conta+Corrente+do+aluno
version: 21
---

---

A *Conta Corrente* do aluno é o local utilizado para armazenar os lançamentos de **'crédito'** (gerados por pagamentos efetuados a maior ou por inclusão de bolsa retroativa executada em lançamentos já baixados) e também os lançamentos de **'débitos****'** (gerados por pagamentos efetuados a menor ou por exclusão de bolsa retroativa executada em lançamentos já baixados) que o aluno possui para serem utilizados futuramente.

Você poderá visualizá-la acessando o Anexo ***'Conta corrente do aluno',***disponível dentro do cadastro do aluno.

Créditos e Débitos na conta correnteCrédito na conta corrente

**- Pagamento efetuado a maior** = gera um Crédito em conta corrente: O pagamento a maior é quando um determinado aluno possui um lançamento (boleto) e este realiza o pagamento com um valor superior ao solicitado.   
**- Inclusão de Bolsa Retroativa em lançamento já Baixado** = gera um Crédito em conta corrente: Se o lançamento já estiver baixado, o valor da bolsa incluída retroativamente será lançado como um crédito na conta corrente.  
  
O valor do Crédito, registrado na baixa do lançamento financeiro, é feito no campo de  que deverá ter sido criado previamente e especificamente para registrar **'Pagamento a maior'**, com Ação = '*Acrescenta'* e posteriormente indicado nos parâmetros do sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 1/3*).

Obs: Após a Baixa, na conta corrente do aluno será incluído automaticamente um registro com este mesmo valor, cuja natureza será = Crédito.

Débitos na conta corrente

**- Pagamento efetuado a menor** = gera um Débito em conta corrente: O pagamento a menor é quando um determinado aluno possui um lançamento (boleto) e este realiza o pagamento com um valor inferior ao solicitado.   
**- Exclusão de Bolsa Retroativa em lançamento já Baixado** = gera um Débito em conta corrente: Se o lançamento já estiver baixado, o valor da bolsa excluída retroativamente será lançado como um débito na conta corrente.  
  
O valor do Débito, registrado na baixa do lançamento financeiro, é feito no campo de  que deverá ter sido criado previamente e especificamente para registrar **'Pagamento a menor'**, com Ação = '*Desconta'* e posteriormente indicado nos parâmetros do sistema (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 1/3*).

Obs: Após a Baixa, na conta corrente do aluno será incluído automaticamente um registro com este mesmo valor, cuja natureza será = Débito.

Para que o sistema consiga atualizar automaticamente a Conta Corrente do aluno com os créditos (valores pagos à maior ou valores das bolsas incluídas retroativamente em lançamentos já baixados) ou com os débitos (valores pagos à menor ou valores das bolsas excluídas retroativamente em lançamentos já baixados), vimos que primeiramente é necessário criar os campos de valores opcionais ou de integração que irão controlar estes valores e posteriormente associá-los nos parâmetros do *TOTVS Educacional* em **'Pagamento a maior'** e **'Pagamento a menor'** respectivamente (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 1/3*). Se optar por utilizar *campos de valores opcionais* para o controle destes valores, estes deverão ser criados no próprio sistema *TOTVS Gestão Financeira*, mas se optar por utilizar *campos de valores de integração* para o controle destes valores, estes deverão ser criados no próprio sistema *TOTVS**Educacional*.  
  
Pronto, vimos como a Conta Corrente dos alunos pode ser atualizada automaticamente, agora, continuando a parametrização referente à *Cobrança Retroativa*, é necessário indicar que comportamento o sistema deverá adotar com os possíveis valores de débitos e créditos encontrados na conta corrente dos alunos. A instituição de ensino poderá escolher entre **'Não efetuar operação'** ou **'Efetuar operação com valor total na próxima mensalidade'**. Estas opções estão disponíveis e devem ser definidas na parametrização do sistema destinados à Cobrança Retroativa (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 2/3*).

Exclusão de baixa que originou a conta corrente:

No *TOTVS Gestão Financeira* ao cancelar a baixa do lançamento que teve pagamento a maior ou menor e consequentemente a originou a conta corrente, o sistema irá remover da conta corrente os valores relativos ao débito ou crédito correspondente a baixa. 

A inclusão ou exclusão de Bolsa Retroativa em lançamentos já baixados irá atualizar automaticamente a Conta Corrente dos alunos com os valores de crédito ou de débitos referentes à estas bolsas, mas atenção, se a instituição de ensino utilizar o segundo modelo de Bolsa Retroativa (aquele que ***não*** altera os lançamentos financeiros originais) e desejar que a Conta Corrente do aluno seja atualizada automaticamente com estes valores é preciso que sistema esteja devidamente parametrizado para tal: acesse *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Fin - Bolsa Retroativa 1/3* e marque a opção *'Utilizar a movimentação em conta corrente'*.

Como aproveitar os valores existentes na conta corrente do aluno

Os valores da conta corrente do aluno podem ser aproveitados de duas maneiras:

1- Automaticamente, ao gerar a próxima mensalidade

Se desejar aproveitar automaticamente os valores existentes na conta corrente do aluno ao gerar a próxima parcela do contrato, nos parâmetros de Cobrança Retroativa deve-se marcar a opção **'Efetuar operação com valor total na próxima mensalidade'**, assim, no momento da geração da próxima parcela, estes valores serão retirados da conta corrente do aluno e irão automaticamente acrescentar (caso exista débito) ou diminuir (caso exista crédito) o valor do lançamento da próxima parcela gerada. O sistema sempre aproveitará o valor máximo possível na geração da parcela e, caso ainda fique um saldo na conta corrente, este valor será aproveitado na geração da próxima parcela e assim sucessivamente. Os valores que forem aproveitados da conta corrente serão registrados no lançamento financeiro da próxima parcela no campo de Valor Opcional ou Valor de Integração que deverão ter sido criados previamente e especificamente para esta finalidade, sendo que o campo criado para registrar ***'Valor opcional/integração de acréscimo'*** deverá ter Ação = '*Acrescenta*' e para ***registrar 'Valor opcional/integração de desconto'*** deverá ter Ação = *'Desconta'* e ambos, após criados, devem ser devidamente associados nos parâmetros do sistema *(Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 2/3*).   
  
A indicação de um **'Valor mínimo'** nos parâmetros do sistema destinados à Cobrança Retroativa para ser descontado ou acrescentado nas próximas parcelas é de caráter *opcional*, porém se indicado, o sistema somente aproveitará os valores da Conta Corrente se o montante for no mínimo o valor indicado.  
  
**Atenção**:

* Caso opte por aproveitar automaticamente o valor existente na Conta Corrente ao gerar a próxima parcela, os **'Serviços'** utilizados nas próximas parcelas que serão geradas, também deverão estar devidamente autorizados para receber tal ação marcando-se a opção **"Aproveita valores da conta corrente do aluno na geração de lançamento"**. Esta opção está disponível dentro do cadastro dos Serviços, assim, somente os Serviços que tiverem esta opção marcada poderão aproveitar os valores existentes na conta corrente ao ser gerada a próxima parcela.  
    
  Ao aproveitar um **Crédito** da conta corrente do aluno na próxima parcela a ser gerada, o sistema irá lançar este valor de crédito no respectivo campo de Valor Opcional ou Valor de Integração do lançamento financeiro, indicado nos parâmetros de sistema destinados à Cobrança Retroativa para registrar *'**Valor opcional/integração de desconto**'*. O valor original do lançamento será o mesmo valor da parcela, porem o valor líquido do lançamento será calculado, **descontando-se** o valor do crédito retirado da conta corrente e, neste caso, o valor líquido do lançamento ficará menor que o original.  
    
  **Observação:**
* Na R*egeração* de lançamentos financeiros, o sistema confere, caso haja, o valor aproveitado da Conta Corrente, refazendo todos os cálculos dos valores do lançamento e, caso seja necessário, irá voltar com o valor, anteriormente aproveitado, para a Conta Corrente do aluno.  
  **Exemplo:**  
  Vamos supor que ao gerar o lançamento financeiro de uma parcela de 1200,00, o sistema tenha aproveitado **500,00** de crédito da Conta Corrente do aluno, transformando o valor líquido do lançamento em 700,00. Se após esta geração, for incluído um desconto de 1000,00 no lançamento financeiro e a parcela for *regerada*, o sistema irá recalcular os valores do lançamento e chegará à conclusão que deverá devolver 300,00 de crédito para a Conta Corrente do aluno, pois 1200,00 de valor original – 1000,00 de desconto = 200,00. Assim o valor máximo que poderá ser aproveitado da Conta Corrente neste lançamento será 200,00, então será feita a devolução de um crédito de 300,00 para a Conta Corrente do aluno (500,00 – 200,00 = 300,00).  
    
  Ao aproveitar um **Débito** da conta corrente do aluno na próxima parcela a ser gerada, o sistema irá lançar este valor de débito no campo de Valor Opcional ou Valor de Integração do lançamento financeiro, indicado nos parâmetros do sistema destinados à Cobrança Retroativa para registrar *'**Valor opcional/integração de acréscimo**'*. O valor original do lançamento será o mesmo valor da parcela, porem o valor líquido do lançamento será calculado, **acrescentando-se** o valor do débito retirado da conta corrente e, neste caso, o valor líquido do lançamento ficará maior que o original.
2- Executando o processo Aproveitar valores em conta corrente

Se desejar que os valores existentes na conta corrente **NÃO** sejam aproveitados automaticamente ao gerar a próxima parcela, nos parâmetros do sistema destinados à Cobrança Retroativa deve-se marcar a opção **'Não efetuar operação'**. Neste caso os valores existentes na conta corrente somente serão aproveitados com a execução manual do processo **'*Aproveitar valores em conta corrente*'**. Este processo pode ser acionado dentro do anexo de Conta Corrente existente no cadastro do Aluno ou através do menu *Financeiro/Contábil | Assistentes*.  
  
**Atenção:**

* O processo 'Aproveitar valores em conta corrente' não poderá ser executado simultaneamente para registros com tipo de natureza diferentes. Deve-se processar separadamente selecionando-se somente os Débitos ou somente os Créditos.  
    
  Se o aluno tiver um **Crédito** na conta corrente e o processo *'Aproveitar valores em conta corrente'* for executado, será incluído diretamente no sistema financeiro um lançamento **a pagar** para o responsável financeiro do crédito, atribuindo este valor diretamente ao valor original do lançamento. Neste caso não haverá vínculo algum com contrato nem serviço e, como será incluído um lançamento a pagar para o responsável financeiro indicado no crédito, este responsável financeiro deverá estar classificado como *Ambos* (cliente e/ou fornecedor) no sistema financeiro.  
    
  Se o aluno tiver um **Débito** na conta corrente e o processo *'Aproveitar valores em conta corrente'* for executado, o usuário deverá indicar um contrato e um serviço, pois ao contrato indicado será incluída uma *parcela extra* neste valor com o seu respectivo lançamento financeiro atribuído ao responsável financeiro indicado no débito da conta corrente. No lançamento financeiro gerado, este valor será lançado diretamente no Valor Opcional ou Valor de Integração indicado para registrar *'**Valor opcional/integração de acréscimo**'* e, neste caso, o valor original deste lançamento será zero.  
    
  **Observações:**
* As fórmulas criadas no sistema para se calcular os valores para a realização da contabilização devem levar em consideração a possibilidade de utilização de valores opcionais ou de valores de integração. No caso específico de lançamentos gerados pelo aproveitamento de *débitos* da conta corrente, o valor aproveitado é lançado diretamente no Valor Opcional ou Valor de Integração, neste caso a fórmula utilizada não poderá levar em consideração somente o valor original do lançamento, pois neste caso específico este lançamento é gerado com o valor original zerado.
* Ao realizar o processo de *Transferência Interna* para alunos que possuírem débitos ou créditos na conta corrente e que optarem por *cancelar* o contrato antigo (original) e gerar um novo contrato, o sistema atualizará automaticamente a matriz aplicada dos registros da Conta Corrente dos alunos com a informação da matriz aplicada utilizada como destino neste processo, assim os registros da Conta Corrente do aluno estarão sempre vinculados a contratos ativos.
* Na visão da Conta Corrente do aluno o usuário poderá alterar manualmente a indicação da matriz aplicada destes registros, sendo possível selecionar entre as matrizes do aluno que estiverem vinculadas a contratos *ativos*, ou seja, contratos que não estiverem cancelados. A permissão para *edição* da matriz aplicada pela visão da Conta Corrente é atribuída no *Perfil* do usuário (*Serviços Globais | Segurança | Perfis | Educacional | Educacional >> 01.01.01.12.01 - Editar matriz aplicada no registro da conta corrente*).
* Nos parâmetros do sistema destinados à Cobrança Retroativa *(Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Vlrs Opcionais/Integração 2/3*), **especificamente para o nível de ensino *Básico***, existe a opção '*Aplicar valores em conta corrente nos lançamentos a serem gerados independente da matriz aplicada'* que ao ser marcada, fará com que o sistema ignore as diferentes matrizes aplicadas e acrescente ou diminua o valor do próximo lançamento a ser gerado. Se a opção não estiver marcada, somente serão considerados os registros de mesma matriz aplicada.
Exclusão de lançamento que aproveitaram os valores existentes na conta corrente do aluno:

* Os lançamentos do TOTVS Gestão Financeiro que aproveitaram valores da conta corrente do aluno e foram excluídos na ordem do aproveitamento, o sistema voltara para a conta corrente o valor com uma linha correspondendo ao crédito ou debito.  
  Ex: Conta Corrente de R$400, aproveitou crédito na parcela 2 á 5 de R$100, ao excluir os lançamentos na seguinte ordem parcela 5,4 e 3 o sistema manterá uma linha correspondente ao saldo no valor de R$300.
* Os lançamentos que aproveitaram a conta corrente do aluno e foram excluídos independente da ordem do aproveitamento (de forma aleatória), o sistema voltara para a conta corrente uma linha separada correspondendo ao crédito ou debito referente ao cancelamento de cada lançamento.  
  Ex: Conta Corrente de R$400, aproveitou crédito na parcela 2 á 5 de R$100, ao excluir os lançamentos da parcela 2 e 3 o sistema criará duas linhas na conta corrente no valor de R$100 cada.

Lançamentos de Acordo

No *TOTVS Gestão Financeira* quando for necessário cancelar uma baixa de um lançamento originado de acordo e para essa baixa foi realizado um pagamento a maior ou menor, que consequentemente gerou valores em conta corrente e existirem lançamentos desse mesmo acordo que foram regerados aproveitando os respectivos valores da conta corrente, será aplicado a seguinte regra: (Somente se for acordo e os lançamentos que aproveitou os valores forem do mesmo acordo)

* O saldo existente na conta corrente correspondente o lançamento de acordo e que foi baixado será zerad
* O sistema reverterá para conta corrente do aluno os valores aproveitados pelos lançamentos do mesmo acordo que foram regerados, se for um pagamento a maior reverte o valor como pagamento a menor ou vice e versa.

Ex: No exemplo ao cancelar a baixa do acordo, será revertido o valor de R$200 como pagamento a menor na conta corrente do aluno, pois os valores foram aproveitados nos lançamentos L2 e L3, caso a acordo seja excluído esses valores serão zerados da conta corrente do aluno.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Valor | Pgto a maior | Desconta Liquido | Liquido |
| L1 | 100,00 | 200,00 |  | 300,00 |
| L2 | 100,00 |  | 100,00 | 0,00 |
| L3 | 100,00 |  | 100,00 | 0,00 |

   Recursos Adicionais

---
