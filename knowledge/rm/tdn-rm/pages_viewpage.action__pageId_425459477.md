---
content_hash: 5b28f3e81f4e037d55f321c2d4dbcbf1ce7526c2ca16c2604a483a9325141a70
fetched_at: '2026-06-29T00:09:36.173613+00:00'
page_id: '425459477'
product: rm
source: tdn-rm
title: Contabilização por Competência - Parametrizações necessárias no TOTVS Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459477
version: 7
---

---

Ao gerar a contabilização, os fatos ocorridos e registrados no TOTVS Educacional serão levados para o sistema contábil através dos lançamentos contábeis gerando assim uma integração entre o sistema educacional e o sistema contábil. Para que isto seja possível é necessário parametrizar o sistema educacional para a geração dos lançamentos preenchendo alguns parâmetros e indicando a utilização de alguns dados do sistema contábil.

**− Serviços\***Os serviços são cadastrados no menu *Financeiro/Contábil | Formação de preço | Serviços*. Somente os serviços que tiverem a opção "Compõe contabilização por competência" marcada em seus cadastros serão considerados na contabilização do contrato e na apropriação mensal.

Esta opção é necessária, uma vez que nem todos os serviços devem ser tratados por competência. Um exemplo pode ser o serviço 'Carteirinha', que é um produto, mas não é considerado como um serviço prestado e que portanto, não deverá ser considerado na contabilização por competência.

**Observação:**   
A opção "*Tipo contábil*" presente no cadastro dos serviços não tem relação nenhuma com a contabilização por competência, esta informação é utilizada somente para a contabilização dos lançamentos financeiros (regime de caixa).

Dentro do cadastro do serviço podemos ainda cadastrar o *Default Contábil* que consiste basicamente na indicação das contas contábeis que serão utilizadas na geração dos lançamentos contábeis. Os defaults contábeis serão utilizados quando o evento contábil, responsável pelo direcionamento da contabilização, estiver parametrizado para utilizar as informações da tabela default.

**− Bolsas\***As bolsas são cadastradas no menu *Financeiro/Contábil | Formação de preço | Bolsas* e serão contabilizadas conforme o evento contábil utilizado para a contabilização por competência.

No **primeiro** modelo de contabilização, se os eventos contábeis determinarem a contabilização das bolsas, *todas* as bolsas presentes nos contratos dos alunos serão computadas e consideradas na contabilização do contrato e na apropriação mensal.

Já no **segundo** modelo de contabilização, *somente* as bolsas que tiverem a opção *"Compõe contabilização por competência"**marcada* em seus cadastros serão consideradas na contabilização do contrato e na apropriação mensal.

A contabilização de bolsas ocorrerá de forma análoga à contabilização dos serviços, onde é possível definir no evento contábil um item de evento com contas específicas para receber a contabilização dos seus valores ou ainda definir um item de evento que busque as contas contábeis diretamente do cadastro de cada bolsa, através do *Default Contábil* de cada bolsa.

**Observação:**  
As bolsas Condicionais (aquelas que dependem de determinadas condições para serem atribuídas financeiramente) não serão contabilizadas pelo regime de competência.

**− Situação de Matrícula\***As situações de matrículas são cadastradas no menu *Curriculo e Oferta | Acadêmico | Situação de Matrícula*.

Somente os contratos de alunos cuja *situação de matrícula* estiver com a opção "Gera contabilização por competência" marcada, serão contabilizados.

Vamos supor que na situação de matricula 'Matriculado' a opção "Gera contabilização por competência" esteja marcada e que na situação de matrícula 'Pre-matriculado' esta opção esteja desmarcada. Ao mandar contabilizar, por exemplo, todos os contratos dos alunos de determinado curso, somente os contratos dos alunos que estiverem com a situação de matrícula igual à 'Matriculado' serão considerados para a contabilização.

**− Eventos Contábeis\***

Eventos Contábeis são cadastros utilizados para mapear e determinar as regras da contabilização de processos realizados dentro do sistema. Eles devem ser cadastrados no menu *Financeiro/Contábil | Geração | Eventos Contábeis*.

Se a forma adotada para a contabilização por competência, indicada nos parâmetros deste sistema, for o *primeiro* modelo de contabilização, onde somente a opção '*Utiliza contabilização por competência'* estiver marcada, dois eventos contábeis devem ser cadastrados no TOTVS Educacional: um para realizar a contabilização dos valores totais do C*ontrato*, com seus serviços, bolsas e/ou descontos e outro para realizar a contabilização da apropriação *Mensal* do serviço prestado.

Se a forma adotada para a contabilização por competência, indicada os parâmetros deste sistema,  for o *segundo* modelo de contabilização, onde a opção *'Utiliza contabilização por competência'* e também a opção *'Registra separadamente contabilizações de cancelamento e aumento'* estiverem marcadas, além dos dois eventos contábeis citados anteriormente, devem ser cadastrados mais dois eventos para registrar possíveis diminuições ou *Cancelamentos* nos valores dos serviços prestados, bolsas e/ou descontos e mais dois eventos para registrar possíveis *Aumentos* nestes valores prestados.

No momento da criação do evento contábil devemos indicar em qual situação ou *processo* ele será utilizado (contabilização do valor total do *contrato* ou de suas apropriações *mensais*, ou ainda para registrar *cancelamentos* ou *aumentos*), além disso, devemos preencher corretamente todas as informações necessárias para a realização da contabilização. Para maiores detalhes quanto à criação de eventos contábeis .

Sempre que mandarmos gerar a contabilização de um contrato para determinado mês/ano, ou precisarmos cancelar um contrato, ou estorná-lo, ou ainda, contabilizar alterações nos valores dos serviços contratados, bolsas e/ou descontos, estes eventos serão consultados e, conforme parametrizados, irão determinar a contabilização destes fatos.

****−**Defaults contábeis\***

Os defaults contábeis são cadastros onde informamos as contas contábeis que sempre serão utilizadas por determinadas entidades (tabelas ou cadastros) dentro do sistema. As contas contábeis, por sua vez, são utilizadas nos lançamentos contábeis, sendo que estes são formados necessariamente por uma ou mais partidas a débito e por uma ou mais partidas a crédito. O(s) valore(s) lançado(s) no débito *sempre* deve(m) fechar em 100% com o(s) valore(s) lançado(s) no crédito.

Os defaults contábeis podem ser cadastrados em algumas entidades dentro do sistema, podendo ser estas entidades indicadas para serem utilizadas nos eventos contábeis, nos dando assim a possibilidade de diversificarmos a contabilização dos fatos, utilizando o mesmo evento contábil.

*Por exemplo*: queremos um evento que contabilize em contas distintas conforme o *serviço* utilizado no contrato. Para que isto ocorra, ao criarmos o evento contábil, devemos parametrizá-lo de forma que utilize o *default contábil* da entidade 'Serviço'. Então, vamos supor que o evento esteja assim parametrizado e que no cadastro do serviço *Mensalidade* a conta contábil **A** esteja indicada em seu default contábil e no cadastro do serviço *Apostila* a conta contábil **B** esteja indicada em seu default. Ao realizar a contabilização por competência, o valor do serviço *Mensalidade* será contabilizado na conta contábil **A** e, se houver serviço de *Apostila* no contrato, este será contabilizado na conta contábil **B** com o seu respectivo valor.

Outro exemplo de utilização dos defaults contábeis na contabilização é a possibilidade de se controlar separadamente os valores para cada *Bolsa* que possa ser concedida aos alunos através da indicação de contas contábeis específicas no default contábil de cada Bolsa. Da mesma forma, através da utilização dos defaults contábeis, é possível utilizar contas contábeis distintas para cada *Matriz Aplicada*, obtendo da mesma forma controles específicos.

******−****** **Parâmetros de Integração | Contabilidade,** [clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=425459120).
