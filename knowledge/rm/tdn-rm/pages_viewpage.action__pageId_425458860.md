---
content_hash: 84a3195a03e98d84a3112dcb3ce2ee432d83f79a43baf82e61fac991d534a67e
fetched_at: '2026-06-29T00:09:32.491874+00:00'
page_id: '425458860'
product: rm
source: tdn-rm
title: Incluir / Excluir bolsas retroativas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458860
version: 8
---

---

Bolsa Retroativa é um recurso oferecido pelo sistema para permitir que as instituições de ensino possam incluir ou excluir bolsas para os seus alunos após os lançamentos financeiros das parcelas dos alunos já terem sido gerados ou até mesmo após os respectivos boletos já terem sido baixados, permitindo assim que as instituições possam conceder ou retirar bolsas retroativamente à estas parcelas já processadas.  
  
O sistema disponibiliza dois modelos para se trabalhar com Bolsas Retroativas:   
  
**1**-   
   
Ao realizar a inclusão ou exclusão de uma bolsa retroativa o sistema *irá alterar* o lançamento financeiro no qual a bolsa está sendo incluída ou excluída, regerando-o para assim contemplar as novas informações, desta forma todos os procedimentos já realizados originalmente no lançamento financeiro, tais como baixa e contabilização serão refeitos.

Neste modelo, se o lançamento original ainda estiver *em aberto,* a bolsa simplesmente será incluída ou excluída no contrato do aluno e o respectivo lançamento financeiro será regerado automaticamente, recebendo ou retirando assim o valor da bolsa. mas se o lançamento já tiver sido *baixado*, por meio de pagamento diferente de PIX e cartão, o sistema utilizará os campos de valores opcionais destinados à *cobrança retroativa*, para receber os valores dos créditos ou dos débitos referentes às bolsas incluídas ou excluídas retroativamente sendo estes campos e valores utilizados na alteração da baixa do lançamento financeiro original e também irá atualizar automaticamente a conta corrente do aluno com os respectivos créditos ou débitos referentes às bolsas incluídas ou excluídas utilizando para isto estes mesmos campos e valores opcionais destinados à *cobrança retroativa*.

A parametrização prévia dos campos de valores opcionais destinados à *cobrança retroativa* está disponível em Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Vlrs. Opcionais/Integração. Para obter mais informações sobre esta parametrização, acesse o link: [Cobrança Retroativa - Como parametrizar](http://tdn.totvs.com/pages/viewpage.action?pageId=309397070).

Caso a baixa do lançamento tenha sido realizada pelos meios de pagamento PIX ou cartão, ocorrerá uma exceção na execução do processo, com a mensagem "Não é possível realizar o processo de inclusão/exclusão de bolsa retroativa, pois existem baixas realizadas por PIX ou Cartão".

Nesse cenário, só será possível incluir a bolsa retroativa com o segundo modelo, exemplificado no item a seguir, ativado quando marcado o parâmetro "Usar bolsa retroativa sem alterar parcelas já baixadas" em Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 1/3. Veja mais sobre estes parâmetros clicando [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425459541).

**2**-   
  
Neste modelo, as bolsas retroativas serão incluídas ou excluídas normalmente para o aluno, porém o lançamento financeiro original e os procedimentos já realizados originalmente *não* serão alterados, e neste caso, a inclusão ou exclusão de bolsas retroativas poderá seguir, por meio de parametrização específica, entre dois caminhos:

* Gerar *devoluções* com a inclusão automática dos respectivos lançamentos financeiros a pagar correspondentes aos valores dos créditos gerados pela inclusão de bolsa retroativa ou inclusão de novas parcelas nos contratos dos alunos correspondentes aos valores de novos débitos provenientes da exclusão de bolsa retroativa.

* Atualizar automaticamente a *Conta Corrente* do aluno com os respectivos valores de créditos ou débitos provenientes da inclusão ou exclusão das bolsas.

Neste modelo, os lançamentos originais não serão alterados e a inclusão ou exclusão de bolsa retroativa serão registradas separadamente, possibilitando assim uma melhor rastreabilidade das origens dos valores e operações.  
  
  
Para saber como parametrizar o sistema e obter mais informações sobre cada um dos modelos, acesse os respectivos links acima.  
  
**Atenção:**  
No TOTVS Educacional, quando são adicionadas bolsas no contrato do aluno cujo a soma do seu percentual ultrapassem 100% de descontos o sistema emite um alerta bloqueando a adição desta bolsa.  
 *Exemplo*  
Parcela: R$ 1000,00.  
Bolsa 1            50%                       
Bolsa 2            60%                
Total               110% de bolsa  
  
Ao tentar inserir a segunda bolsa de 60%, o sistema irá emitir um alerta pois o total de bolsas neste caso ultrapassa o valor permitido de 100%, sendo assim esta bolsa não é inserida no contrato. Para que essa regra surta efeito o sistema deve estar parametrizado para que a  esteja por "**contrato**" e o tipo de classificação seja igual a "**somar bolsas**". Veja mais sobre estes parâmetros clicando .   
  
Porém, existe uma exceção na regra para que as bolsas que contenham fórmula parametrizada não sejam levadas em consideração no somatório dos percentuais da bolsa, pois este percentual será customizado pela própria fórmula cadastrada na bolsa e nesse caso a regra estará na fórmula. Veja mais sobre bolsa por fórmula clicando [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=354469739).
