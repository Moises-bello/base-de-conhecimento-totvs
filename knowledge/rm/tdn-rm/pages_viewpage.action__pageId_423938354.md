---
content_hash: 4cc4b51bab7fb0eaa6f13e0a29976d35c1e170403b35f87290b555392ec49cfe
fetched_at: '2026-06-29T00:09:26.670178+00:00'
page_id: '423938354'
product: rm
source: tdn-rm
title: Plano de Contas Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938354
version: 67
---

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

Plano de Contas Contábeis é o conjunto de contas, previamente estabelecido, que norteia os trabalhos contábeis de registro de fatos e atos inerentes à empresa, além de servir de parâmetro para a elaboração das demonstrações contábeis.

A montagem do Plano de Contas é personalizada, por empresa, já que os usuários das informações podem necessitar de detalhamentos específicos, que um modelo de Plano de Contas geral pode não compreender. As contas contábeis devem ser expressas com títulos em conformidade com os atos e fatos administrativos provocados. Uma conta deve representar facilmente a operação realizada pela empresa.

Antes de se iniciar a inclusão do Plano de Contas Contábil, deve-se definir a máscara do plano, ou seja, para cada grupo de contas devem-se definir os níveis hierárquicos para suas contas e subcontas, assim como a quantidade de dígitos para cada nível. A definição da máscara do plano de contas é feita no Menu Parâmetros/Plano de Contas.

A inclusão das contas deve obedecer aos níveis hierárquicos, assim como a correta classificação das contas em sintéticas e analíticas, sendo as contas do último nível sempre classificadas como analíticas. As contas contábeis podem ser cadastradas como conta **Global**. Uma conta cadastrada como Global pode ser usada também em outras coligadas. Para isto o sistema deve estar parametrizado para tal, devendo as coligadas que acessarem contas Globais possuírem máscaras idênticas, além disto, as contas de níveis superiores à que se está cadastrando já devem existir nestas coligadas.

**Plano de Contas sem máscara**

O sistema permite Planos de Contas Contábeis sem o uso de máscara, para isso utilize a opção "Não utiliza máscara nas contas" que está disponível no Menu Parâmetros/Plano de Contas.

No caso da não utilização de máscara o sistema irá se orientar a partir dos números das contas Sintéticas e do número de caracteres para montar a hierarquia das contas.

**Atenção:** É imprescindível que sejam respeitadas as regras hierárquicas, sendo assim, contas de tipo Analítica serão aquelas com o maior número de caracteres e seguindo o padrão numérico das demais contas cadastradas.

ImagemfalseOrientações para preenchimento dos camposa,b,c,d,e,faIdentificação

**Conta Estorno**

Só será possível incluir uma conta de estorno quando a estrutura das contas for idêntica. Se a conta a ser incluída for "Global", a conta de estorno deverá ser "Global". Se a conta contábil possuir "Rateio", a conta de estorno também deverá possuir "Rateio".

Além disso, o sistema só permitirá alterar o campo Rateio se não existir conta de estorno associada à conta contábil.

**Rateio**

Habilite o campo se desejar que uma distribuição gerencial seja registrada nos valores movimentados na Conta Contábil. Desta forma, todas as vezes que uma conta contábil, cujo campo Rateio esteja ativado em seu cadastro for utilizada em um lançamento, a distribuição gerencial do valor contábil será exigida para a complementação do lançamento, devendo ser informadas as contas gerenciais que receberão o rateio.

Com esta opção marcada será exibida a aba **Distribuição Gerencial** onde pode ser informado, **de forma opcional**, um rateio padrão. Assim, em todos os lançamentos cadastrados com essa conta contábil, o rateio será automaticamente cadastrado nas contas gerenciais informadas como default, podendo ser alterado se desejar, ou confirmado.

**Observações**

* Sendo informada uma ou mais contas gerenciais para o rateio padrão, o total rateado entre as gerenciais deverá obrigatoriamente fechar em 100%.
* Para contas contábeis Globais que tiverem distribuição gerencial, apenas contas gerenciais Globais poderão ser utilizadas no cadastro do rateio padrão (default), pois este padrão será usado nos lançamentos de todas as coligadas que acessarem contas Globais, portanto, as gerenciais também têm que ser Globais, não podendo ser utilizadas no default gerenciais específicas de uma coligada apenas. Já no cadastro dos lançamentos, pode-se informar qualquer gerencial (global ou não global) para o rateio de uma conta contábil global.
* Em caso de alteração do rateio padrão informado no cadastro da conta contábil, o sistema altera automaticamente todos os lançamentos que tiverem utilizando esta conta. **Um filtro opcional** poderá ser utilizado para agrupar e/ou classificar as contas nos relatórios criados através do Gerador de Relatórios. O agrupamento/classificação poderá ser realizado seguindo-se o pequeno roteiro abaixo:

1. No "Filtro Opcional" do cadastro das contas desejadas, digite um número;
2. Acesse o Gerador de Relatórios, Menu Formatação e selecione o relatório desejado;
3. Através da opção Inserir Campo da Base de Dados, selecione a tabela Contas Contábeis e inclua o campo "Campo Opcional" em um dos Grupos (LD - Linha de Detalhes, por exemplo) do relatório acessado - Formatação do Gerador de Relatórios;
4. Através da janela Selecionar Registros (Seleção - Filtros Fixos), selecione no item Campo, a opção "Campo Opcional" e defina demais opções.

Seguindo estes passos as contas serão agrupadas de acordo com o número informado no Campo Opcional. Uma **Conta de Estorno** poderá ser associada à conta contábil, basta incluí-la no campo apropriado. Desta forma, ao efetuar um estorno contábil no TOTVS Gestão Financeira ou no TOTVS Gestão Fiscal será feita a substituição pela conta de estorno aqui informada. Caso não exista a conta de estorno associada continua sendo utilizada a própria conta contábil.

**Natureza da conta para emissão do SPED**

Para gerar o SPED Contábil, todas as contas, desde as sintéticas até as analíticas, devem ser classificadas de acordo com a sua natureza, sendo que as contas de nível superior deverão ter a mesma natureza das suas subcontas.

No caso de existir alguma conta que não deve ser enviada para o SPED Contábil, esta deverá ser classificada como "Não informada". Assim esta conta e todas as suas movimentações contábeis não serão consideradas na geração do SPED.

Ao gerar o SPED o sistema cria um arquivo digital com vários registros, separados conforme as naturezas aqui classificadas, confrontando, entre outras informações, os valores dos grandes grupos contábeis. Desta forma, uma conta classificada incorretamente pode fazer com que o arquivo digital gerado pelo SPED não seja validado.

**Eliminar valores nas consolidações**

Marcando este campo: as movimentações da conta contábil serão consideradas como eliminações na geração das demonstrações contábeis consolidadas.  
Desmarcando este campo: Caso existam lançamentos contábeis com dados de eliminação preenchidos e vinculados a esta conta, esses dados permanecerão gravados, porém não serão mais exibidos nas partidas, uma vez que a conta contábil deixará de estar parametrizada para essa finalidade.

bInformações

**Data de Inclusão**

Na inclusão da conta contábil, a data corrente será sugerida como Data de Inclusão, podendo neste momento, antes de se salvar a inclusão, modificá-la. Depois de incluída a conta, a Data de Inclusão não poderá mais ser modificada. Esta data será utilizada na geração do SPED Contábil.

* Não será possível gerar o SPED Contábil caso haja alguma conta em que a Data de Inclusão esteja em branco.
* As contas contábeis que tiverem datas de inclusão maiores que a data final da escrituração gerada para o SPED Contábil não serão enviadas para o registro I050 do arquivo digital, porém,  se para estas mesmas contas existirem movimentações no período da escrituração, estas contas serão enviadas normalmente para o registro I050 com suas respectivas datas de inclusão assim como suas movimentações e, neste caso, como as datas de inclusão destas contas são maiores que a data final da escrituração, serão apresentadas Advertências ao validar o arquivo digital no PVA (Programa Validador do SPED Contábil).

Os campos **Usuário Inclusão**, **Data Alteração** e **Usuário Alteração** não podem ser editados e servem para controle das alterações dos registros.

cCampos Complementares

Está aba só será apresentada caso haja algum Campo Complementar cadastrado para a Entidade de Plano de Contas.

Os Campos Complementares de **Contas Contábeis** existentes e ativos na base de dados ficarão disponíveis dentro desta aba para preenchimento.

Os Campos Complementares de **Lançamentos** existentes e ativos na base de dados ficarão disponíveis dentro do cadastro da conta contábil se o parâmetro do sistema 'Usa amarração c.complementar' estiver marcado. Se assim estiver, pode-se selecionar e associar os campos complementares de lançamentos à conta contábil. Desta forma, ao incluir um lançamento, os campos complementares de lançamentos vinculados à conta contábil utilizada ficarão disponíveis na tela do lançamento para serem utilizados como queiram.

dConversão multimoedas

**Tipo de conversão multimoeda**

Este atributo será utilizado no momento da conversão de valores do lançamento (ao criar ou atualizar um lançamento) entre as moedas previamente definidas nos parâmetros do sistema. Através de tal parâmetro será definido como, para cada conta, será recuperada a cotação, índice, etc a ser utilizado para o cálculo na conversão de valores entre tais moedas que estiverem configuradas para o sistema (parâmetros do sistema).

Este campo é de seleção exclusiva, isto é, não é permitido múltipla seleção e disponibiliza as opções abaixo:

* **Taxa histórica** - Nesta opção a conversão para as demais moedas deve ocorrer utilizando a taxa de câmbio do dia imediatamente anterior à data da transação (fato contábil)

No nosso exemplo, considera-se a taxa de câmbio registrada para o dia 17/01/X0;

* **Taxa média histórica** - Já nesta opção, a conversão ocorre utilizando a média da taxa de câmbio considerando todo o mês da data da ocorrência do fato contábil

No nosso exemplo, utiliza-se a taxa de câmbio encontrada pela soma de todas as taxas de câmbio registradas para o mês/ano 01/X0, dividida pela quantidade de registros encontrados no mês de janeiro;

* **Taxa de fechamento** - Aqui, utiliza-se a última taxa de câmbio registrada no mês da data da ocorrência do fato contábil

No nosso exemplo, utiliza-se a taxa de câmbio registrada para o dia 31/01/X0;

* **Fixa** - Neste caso, o valor convertido será informado pelo usuário e não deve ser atualizado pelo sistema;
* **Não se aplica** - Neste caso não haverá a conversão para outras moedas.

gConciliação

**Fórmula valor financeiro para conciliação**

Fórmula do módulo financeiro responsável por calcular/retornar o valor em aberto correto de maneira a ser utilizado na conciliação.

O TOTVS RM permite uma flexibilidade para os clientes trabalharem os valores dentro do módulo Financeiro no que tange a composição do valor financeiro em aberto então a fórmula acima representa o cálculo deste valor que será utilizado na conciliação.

O preenchimento da fórmula é opcional e estará disponível apenas para contas contábeis analíticas.

A lista de fórmulas apresentadas para seleção contemplam apenas as fórmulas do financeiro que sejam da coligada do contexto (onde o usuário está logado) e/ou as fórmulas globais.

Mais detalhes sobre fórmulas pode ser encontrado em: [Cadastro de fórmulas](https://tdn.totvs.com/pages/viewpage.action?pageId=403746924) ou [Fórmulas em VB.NET](https://tdn.totvs.com/pages/viewpage.action?pageId=66126694)

**Data última conciliação** 

Apresenta a data que ocorreu a última conciliação para tal conta.

Este campo, neste cadastro, é meramente informativo pois o mesmo é/será valorado e utilizado nas rotinas .

eDistribuição Gerencial

Esta aba será habilitada somente para as Contas Contábeis que estiverem com o campo **Rateio** marcado.

Utilize essa estrutura para definir o rateio default da Conta Contábil  que será utilizado de forma automática na inclusão do Lançamento Contábil.

Consumo via API

A integração com o Plano de Contas está disponível também através de APIs. No [Guia de APIs da TOTVS](https://api.totvs.com.br/) são descritas todas as APIs disponíveis, suas características e funcionalidades. Assim como as visões, a API também pode ser configurada para retornar somente um número X de registros ao ser consultada. Essa configuração é feita no  com a parametrização do Número Máximo de Registros. No caso da API de Plano de Contas o DataServer a ser utilizado é o **CtbAccountingPlanDataApi**.

Definição de API

      API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web. A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos".

      Uma API é criada quando uma empresa de software tem a intenção de que outros criadores de software desenvolvam produtos associados ao seu serviço. Existem vários deles que disponibilizam seus códigos e instruções para serem usados em outros sites da maneira mais conveniente para seus usuários.

      Através das APIs, os aplicativos podem se comunicar uns com os outros sem conhecimento ou intervenção dos usuários. Elas funcionam através da comunicação de diversos códigos, definindo comportamentos específicos de determinado objeto em uma interface. A API liga as diversas funções em um site de maneira que possam ser utilizadas em outras aplicações. De modo geral, a API é composta de uma série de funções acessíveis somente por meio de programação.

      Recentemente, a utilização das APIs tem se espalhado nos plugins, que complementam a funcionalidade de um determinado programa. Os desenvolvedores de um programa principal criam uma API específica e fornecem a outros criadores, que desenvolvem plugins para aumentar o potencial e as funcionalidades do programa.

      Os sistemas operacionais também possuem suas APIs com as mesmas funções descritas acima. Por exemplo, o Windows possui APIs como a Telephony API, Win16 API e Win32 API. Quando um usuário executa um programa que envolva algum processo do sistema operacional, é bem provável que o Windows faça uma conexão entre o software e alguma de suas APIs.

Anexos

* [Histórico de Inativação / Ativação de Contas Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938472)
* [Histórico de Alteração da Conta p/ SPED Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938477)
* [Associação com Plano(s) Paralelo(s)](http://tdn.totvs.com/pages/viewpage.action?pageId=423938647)
* [Subcontas](http://tdn.totvs.com/display/LRM/Subcontas)
Processos

* [Alteração do Tipo da Conta Contábil (Analítica / Sintética)](http://tdn.totvs.com/pages/viewpage.action?pageId=423938640)
* [Alteração do Código de Contas Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938662)
* [Alteração do Campo "Tem Distribuição Gerencial"](http://tdn.totvs.com/pages/viewpage.action?pageId=423938661)
* [Copiar Contas Contábeis entre Coligadas](http://tdn.totvs.com/pages/viewpage.action?pageId=423938678)
* [Inativação / Ativação de Contas Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938467)
* [Atualização da Data de Inclusão](http://tdn.totvs.com/pages/viewpage.action?pageId=423938652)
* [Classificação Automática da Natureza da Conta para emissão do SPED](http://tdn.totvs.com/pages/viewpage.action?pageId=423938622)
