---
content_hash: 748d82e37544069e08632b97ce7b53e282de0b97596d151cb36a98bdf9d04d2e
fetched_at: '2026-06-29T00:11:38.289484+00:00'
page_id: '784209752'
product: rm
source: tdn-rm
title: TCGI - Comissão - Conversor de Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784209752
version: 28
---

A partir do Release 12.1.2310 ao acessar o menu de *Comissões* (antigo), o sistema irá executar o **Conversor de Comissão**, atualizando estes registros para as ***[Comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766)*** com novas funcionalidades***.***

Para que esta conversão ocorra com sucesso é preciso que o sistema atenda aos seguintes pré-requisitos:

* A base deve estar no [Reajuste Revitalizado](https://tdn.totvs.com/pages/viewpage.action?pageId=546260610);
* Para clientes que possuem [Portal de Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=435105077), PI, é preciso que esta base esteja [convertida](https://tdn.totvs.com/pages/viewpage.action?pageId=770956085) para a base RM; e
* A base está no modelo antigo de [Comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=435105285).

Para as comissões que são pagas a funcionários diretamente na Folha de Pagamento, utilizando a integração com o , caso o parâmetro *[Gerar Código Sequencial do Cliente/Fornecedor](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)* esteja desmarcado, será preciso cadastrar manualmente estes funcionários como [Cliente/Fornecedor](https://tdn.totvs.com/pages/releaseview.action?pageId=421388786), para que este conversor consiga realizar o De-Para destas entidades corretamente. Caso este parâmetro já esteja marcado, esta etapa será realizada de forma transparente, sem nenhuma intervenção do usuário.

Caso ocorra o cenário acima, ao executar o conversor, será exibida uma exceção informando quais *Códigos de Funcionários* será preciso incluir manualmente no cadastro de Cliente/Fornecedor.

Pode-se utilizar o processo para , acessível através do menu de Processos da tela de Cadastro de Funcionários.

Características do Modelo de Comissões Antigo

É possível de se identificar se a base está no modelo antigo de comissões, pelas seguintes características:

* na **Interface**:

Na interface do TCGI, são apresentados o menu de *Vendedores* e o menu de *Comissões*, apresenta apenas opções *Gerar Parcela de Comissão* e *Parâmetro Financeiro Comissão*, conforme demonstrado na imagem abaixo:

Atendidas as condições acima, ao clicar no menu de Comissões, o TCGI apresentará ao usuário uma mensagem com a seguinte mensagem:

*"Atenção usuários do TOTVS Construção Gestão de Imóveis (TCGI)*

*Informamos que a partir da versão 12.1.2310, o antigo módulo de comissão será descontinuado e a conversão para a Comissão com novas funcionalidades será disponibilizada.*

*Esta atualização vale para o módulo do TCGI (Venda).*

*Obs.: Sugerimos realizar um backup da base de dados antes de executar o "Conversor de Comissão".*

*Deseja executar o “Conversor de Comissão”, agora?*

*Obs.: Se o conversor não for executado o módulo de comissão do TCGI apresentará esta mensagem até a execução do conversor.*

*Para mais informações, favor entrar em contato com a central de atendimento TOTVS.*

*Links TDN*

*Conversor de Comissão: <https://tdn.totvs.com/x/WBe_Lg> "*

Ao clicar em *Não*, o sistema dá acesso ao dados da Comissão antiga, para serem realizados os ajustes e validações que se fizerem necessários.

Ao clicar em ***SIM***, o sistema apresenta a tela do Conversor de Comissão, com a opção para criar e migrar os campos complementares da Tabela XCOMISSAOCOMPL para a Tabela XCOMISSOESCOMPL, sendo preciso ter muita atenção neste momento pois caso estes campos não sejam migrados neste momento, eles não poderão se migrados posteriormente:

Importante!

Ao migrar os Campos Complementares das comissões antigas para as Comissões com novas funcionalidades, é imprescindível que estes Campos Complementares que serão criados, tenham o mesmo ***Nome da Coluna*** e o mesmo ***Tipo de Campo*** dos que contém as informações que serão migradas.   
Assim o conversor realizará o DE-PARA destes dados corretamente.

A Ordem destes Campos Complementares não interfere na migração destes dados.

Após clicar em executar o sistema executará um loop em todos os Vendedores e respectivas Comissões, considerando as [Regras de Conversão](https://tdn.totvs.com/pages/viewpage.action?pageId=784771213),  para criar novos registros nas tabelas da Comissão com novas funcionalidades e ao término deste processo, será apresentado um log com os registros convertidos.

Faça Isto!

Para acessar os menus das Comissões com novas funcionalidades, deverá deslogar do TCGI, logar novamente e dar Permissão de Acesso aos itens do Menu 01.01.03 - Comissões, que forem pertinentes a cada Perfil de Usuários:

Após esta ação, será preciso refazer o login no TCGI para ter acesso os menus da **[Comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766)**:

Na conversão são migrados também as seguintes informações:

* Parâmetros de Integração;
* Campos [Complementares da Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=435105285);

Atenção!

Caso haja alguma comissão antiga, parametrizada para utilizar a integração com o TOTVS Gestão de Estoque, Compras e Faturamento e nesta integração, o Centro de Custo esteja em branco, ou seja, não informado, o Conversor irá migrar esta comissão e será necessário editá-la posteriormente, informando o Centro de Custo nos [Parâmetros de Integração do Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=773518203) associado à ela.

Importa ressaltar que as Comissões migradas pelo conversor não poderão ser editadas e recalculadas após esta conversão.

Este comportamento é justificado devido ao fato que qualquer alteração de valor, quantidade ou pessoas envolvidas neste tipo de comissão pode gerar uma divergência no recálculo, quando realizado no novo modelo.

As informações dos ***Campos Complementares*** do ***Vendedor*** não serão migrados pelo conversor caso queira preservar estas informações insira-as manualmente nos Campos Complementares da Comissão. Importa ressaltar que estas informações permanecerão gravadas na tabela de campos Complementares desta Entidade.

Duvidas sobre Conversão da Comissão

***Levando em consideração a seguinte situação na qual em um cliente em produção, onde o banco de dados do PI está separado do banco de dados do RM, deve-se realizar o processo de conversão de comissões neste momento ou seria mais apropriado realizar esta conversão apenas após a consolidação dos bancos de dados?***

A conversão das comissões deve ser realizada apenas após a consolidação dos bancos de dados. Isso ocorre porque o novo modelo de comissão é compatível somente com o novo modelo do Portal de Imóveis. Portanto, consolidar os bancos de dados primeiro garante que o processo de conversão funcione corretamente e sem interrupções.

***Após convertermos as comissões para o novo modelo, é necessário configurar todas as comissões para todos os empreendimentos imediatamente, ou podemos configurar um empreendimento de cada vez, sem pressa?***

Assim que a conversão for realizada, é essencial configurar as comissões imediatamente, pois o sistema começará a aplicar as novas regras de geração de comissões. Sem essas configurações, as comissões não serão geradas.

***Temos relatórios (RM Report) e cubos customizados, desenvolvidos internamente, que utilizam as tabelas e processos atuais de comissão (via módulo de Compras). Qual será o impacto dessa conversão nas tabelas e processos atualmente usados para esses relatórios e cubos?***

Se os relatórios e cubos personalizados utilizam alguma tabela de comissão do TCGI, será necessário revisá-los, pois a nova comissão emprega tabelas diferentes. A leitura dos dados deverá ser ajustada para essas novas tabelas.

Recomendamos revisar os relatórios desenvolvidos no Smart View, o novo gerador de relatórios da TOTVS, que já apresentam os dados de comissão no novo modelo. Esses relatórios podem fornecer as informações necessárias.

Para mais detalhes, consulte a ***[documentação da TOTVS](https://tdn.totvs.com/pages/viewpage.action?pageId=745143772)[.](https://tdn.totvs.com/pages/viewpage.action?pageId=745143772)***

***Caso possamos realizar a parametrização após a conversão sem pressa, será necessário desenvolver novos relatórios e cubos para os empreendimentos já convertidos, enquanto mantemos os empreendimentos ainda não convertidos utilizando os relatórios e cubos antigos?***

A conversão para o novo modelo de comissões, assim como a unificação da base de dados para o novo Portal de Imóveis, é realizada para toda a base de dados e não por coligada individualmente. Assim que a conversão for concluída, todas as coligadas passarão a operar com o novo modelo simultaneamente.

***Existe algum site da TOTVS que forneça detalhes sobre as alterações, criações e remoções de tabelas e views que ocorrem durante o processo de conversão das comissões?***

Para responder a esta questão, é importante consultar a documentação da TOTVS, onde são detalhadas todas as alterações que ocorrerão durante o processo de conversão das comissões. Na documentação, você encontrará informações sobre:

* As tabelas que deixarão de ser utilizadas no novo modelo de comissão.
* As novas tabelas de dados de comissão que substituirão as antigas.

Esses detalhes são essenciais para entender quais mudanças específicas serão feitas nas estruturas de dados e como adaptar seus relatórios e processos atuais para se alinhar ao novo modelo.

Após executar as ações acima, pode-se  utilizar o [Configurador de Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=787854626), para facilitar a criação dos cadastros necessários ao uso da Comissão.
