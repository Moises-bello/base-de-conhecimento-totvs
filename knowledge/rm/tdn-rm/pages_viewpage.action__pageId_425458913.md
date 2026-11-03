---
content_hash: 8d7e51c9c0fc356b3fca912b84a3c3060c099400dddc2d31c07ee654d2bc3b64
fetched_at: '2026-06-29T00:09:32.741734+00:00'
page_id: '425458913'
product: rm
source: tdn-rm
title: Criação de Parcelas do Plano de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458913
version: 7
---

---

As parcelas do plano de pagamento podem ser criadas manualmente, para isto, edite o plano em questão, acesse **Anexos | Parcelas do plano de pagamento** e faça a inclusão de cada parcela que irá compor o plano de pagamento.

Se preferir otimizar a criação das parcelas do plano, utilize o processo para criação, disponível em **Financeiro/Contábil | Formação de preços | Planos de pagamento | Processos | Criação de Parcelas**. Selecione o plano e execute-o.

Independe da forma de criação das parcelas do plano, manualmente ou pelo processo de criação, toda parcela deve possuir a identificação do serviço prestado, o número correspondente da parcela, o número de cotas, o tipo de parcela, o valor a ser pago, possíveis descontos e data de vencimento.

 Se a criação de parcelas for feita *manualmente*, inclua cada uma das parcelas que irão compor o plano de pagamento com estas informações.

Através do *processo*, pode-se otimizar a criação das parcelas, pois estas definições serão feitas uma única vez, e replicadas para o número de parcelas indicadas para serem criadas para o plano.

Pelo processo de criação de parcelas, indique primeiramente o(s) serviço(s) que farão parte do plano de pagamento. Na próxima etapa do assistente de criação de parcelas preencha todas as informações referentes ao primeiro serviço indicado.

**- Manter informações para todos os serviços selecionados**  
Essa opção quando marcada permite que os dados informados para o primeiro serviço sejam propagados para todos os outros serviços selecionados anteriormente para compor o plano de pagamento, evitando assim uma nova digitação dos dados por parte do usuário.

**- Substituir Parcelas Existentes no plano de pagamento para o serviço**  
Marcando esta opção o assistente substituirá as parcelas que porventura já existam para o serviço no plano de pagamento. Caso a opção não seja selecionada e já existam parcelas para o serviço as novas parcelas **não** serão geradas para o serviço em questão.

Em seguida, para cada serviço adicionado, indique o número de parcelas a serem criadas e número de cotas.

Também para cada serviço adicionado poderá definir o número inicial da parcela e da cota. Para isso basta marcar a opção "**Definir parcela inicial**" e preencher os campos "Parcela Inicial" e "Cota Inicial".

Identifique o tipo de parcela que será criada:

* Parcela do plano
* Parcela extra
* Parcela adicional

Informe a data de competência para a primeira parcela. Para as próximas parcelas o sistema irá incrementar o mês. Esta data também pode ser utilizada na contabilização do lançamento financeiro da parcela.

Se houver desconto para as parcelas, indique-o e indique também o tipo de desconto. Este desconto irá incidir na geração dos lançamentos financeiros, diminuindo o seu valor líquido.

Para encontrar o dia de vencimento das parcelas, o sistema irá verificar a opção aqui selecionada para o *'Dia de vencimento'* e, em alguns casos, verificará também a configuração utilizada para dia útil nos parâmetros deste sistema **(*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin Geral 4/4*)**, podendo ser:

****-**Fixo**: Será sempre o dia informado no campo *'Data de vencimento inicial'*, mudando-se apenas os meses seguintes para as próximas parcelas. Marcando esta opção o sistema ***não*** irá verificar nenhuma das configurações dos parâmetros do sistema referentes a dia útil, considerando sempre Fixo o dia da data informada para o vencimento das parcelas. Se o dia informado for maior que o último dia de algum mês, a parcela será criada no último dia deste mês.  
**Exemplo:** Data de vencimento inicial: 31/05/2017. A data de vencimento das parcelas será o dia 31 de cada mês, mas para os meses que não têm o dia 31, a data de vencimento será o último dia do mês. Então, conforme este exemplo, a data de vencimento para a parcela de Maio será 31/05/2017, mas para Junho será dia 30/06/2017, e assim sucessivamente.

******-****Útil**: O vencimento de cada parcela será no enésimo dia conforme o dia informado no campo *'Data de vencimento inicial'*, mudando-se apenas os meses seguintes para as próximas parcelas. Marcando esta opção o sistema ***irá*** considerar também as configurações definidas nos parâmetros do sistema referentes à validação de *Sábado* e *Domingo* para se encontrar o enésimo dia útil.  
**Exemplo:**Data de vencimento inicial: 02/06/2017. Sistema irá considerar o segundo dia útil de cada mês para a geração das parcelas. Primeira parcela = mês 06/2017 = data vencimento = 02/06/2017. Segunda parcela = mês 07/2017 = data vencimento = 04/07/2017 e assim sucessivamente.

******-****Último dia útil do mês**: A data de vencimento das parcelas será o último dia útil do mês da data que foi informada no campo *'Data de vencimento inicial'*, mudando-se apenas os meses seguintes para as próximas parcelas. Marcando esta opção o sistema ***irá*** considerar também as configurações definidas nos parâmetros do sistema referentes à validação de *Sábado* e *Domingo* para se encontrar o último dia útil.  
**Exemplo:** Data de vencimento inicial: 02/06/2017. Independente do dia informado neste campo (conforme este exemplo = dia 02), a data de vencimento das parcelas será o último dia útil de cada mês. Então, conforme este exemplo, a data de vencimento para a primeira parcela será 30/06/2017, mas para a segunda parcela será 31/07/2017, e assim sucessivamente.

Por último, se desejar que o valor das parcelas seja calculado em função do número de créditos informados nas disciplinas cursadas, marque a opção correspondente **'*Valor calculado pelo número de créditos****'* (esta opção estará disponível somente para o nível de ensino superior). Se esta opção ficar desmarcada, o valor das parcelas será calculado tomando como referência o valor informado no cadastro do Serviço utilizado.

Para que o sistema faça o cálculo pelo número de créditos é preciso, antes, preparar o sistema corretamente com todas as informações e dados necessários.
