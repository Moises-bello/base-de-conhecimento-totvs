---
content_hash: 31f06329ae1223f6999a849142d15599564dd0619623cb7225a78b7c2374842e
fetched_at: '2026-06-29T00:10:03.833567+00:00'
page_id: '452719161'
product: rm
source: tdn-rm
title: Dados do Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719161
version: 4
---

Este modulo consiste em calcular a previsão de custo da folha de pagamento, envolvendo todos os movimentos futuros: Folha Mensal, Férias, 13º Salário, Encargos Sociais e de Provisões, além de estipular previsões de Admissões, Demissões, Transferências e projetar reajustes salariais.  
   
Para criar um orçamento, o usuário deverá ter conhecimento de alguns parâmetros essenciais para execução do orçamento:  
·         Intervalo de Competências (mês e ano inicial / me e ano final);  
·         Lotação de Pessoal – é o agrupamento previamente parametrizado que listará os funcionários, cadastrados na coligada, que serão elegíveis ao cálculo do orçamento;

A partir da versão **12.1.25**algumas modificações foram implementadas no módulo de orçamento.

* Agora é possível acessar todas as revisões de um orçamento, e não somente a ultima revisão.
* Foi implementado um controle de permissão para o cálculo e edição das revisões de orçamento, assim um determinando orçamento pode está bloqueado para cálculo ou para edição.
* Foi implementando um controle de filtro Seção x Função, assim de acordo com a parametrização do RM, só aparecerão nos *lookups* de função as funções das quais o usuário logado é chefe, caso o usuário logado não seja chefe de nenhuma seção, não aparecerão funções nesses lookups.
* Foi implementando um novo processo para bloqueio e desbloqueio das revisões de orçamento, este processo permite bloquear ou desbloquear várias revisões de um determinado orçamento de uma vez.

O primeiro passo, ao incluir o orçamento, é definir Código do Orçamento, Descrição, Competência (intervalo inicial / final), e a Lotação de Pessoal.  
   
Avançando a tela, são apresentados os menus relativos a Manutenção da Lotação:

* **Admissão**: é possível incluir Vagas de Admissão para executar no orçamento o custo das vagas. O sistema irá considerar todos os movimentos futuros a partir da data de admissão da vaga.

O usuário deverá informar o campo Código de Perfil que foi previamente cadastrado no módulo "Perfil de Admissão" ou informar a Chapa base e então o sistema irá carregar os parâmetros da vaga.

* **Promoção**: será possível incluir parametrização de promoção, onde o usuário irá determinar por grade de seleção, filtro, seção, os funcionários que futuramente terão promoção, além de informar fórmula, percentual ou "Valor Informado" para que os movimentos futuros sejam calculados de acordo com novo salário da promoção. Nos casos onde apenas o salário for alterado deve-se utilizar o processo de Reajuste Salarial.

Existe neste menu a opção de executar a funcionalidade sugerir. Bastando o usuário informar a quantidade de funcionários a serem transferidos, o sistema irá apresentar a seleção dos funcionários.

* **Transferência**: será possível parametrizar transferências para filiais e outras coligadas, de forma que movimentar os funcionários e assim prever o custo deles nos destinos. Os cálculos do movimento futuro serão realizados para a coligada/filial de origem até a data da transferência. A partir da data de transferências, os cálculos serão realizados para coligada/filial de destino.

O usuário deverá informar nova Coligada ou Seção, e parametrizar os motivos de transferências, nova função, salário, jornada e horário.  
Existe neste menu a opção de executar a funcionalidade sugerir. Bastando o usuário informar a quantidade de funcionários a serem transferidos, o sistema irá apresentar a seleção dos funcionários.   
**Observação:**  
Somente será possível fazer transferência para coligadas e seções que fazem parte da mesma lotação do orçamento   
O campo Nova Chapa só será habilitado quando selecionarmos uma chapa na seleção de funcionários.

* **Demissão**: será possível parametrizar demissões futuras, dos tipos "2 – Inc. Empregador sem justa causa" e "4 – Iniciativa do Empregado sem justa causa". O sistema irá simular o cálculo da rescisão do funcionário na data informada como demissão, para os funcionários que compreenderem a seleção ou a sugestão (funcionalidade sugerir).

Quando incluir parametrização de rescisão do tipo 2, o usuário deverá marcar o parâmetro "Tem Aviso Prévio Indenizado" para calcular Aviso Indenizado, ou não marcar este parâmetro, desta forma o cálculo será realizado considerando "Aviso trabalhado", ou seja, será calculado o Saldo de Salário.  
Para parametrizações de rescisão do tipo 4, o usuário poderá optar em marcar o parâmetro "Desconta Aviso Prévio", ou não marcar o parâmetro para que seja calculado apenas o Saldo de Salário.

* **Alteração de Seção**: será possível alterar movimentar funcionários para outras seções para que o custo seja totalizado na seção que o funcionário irá trabalhar.

* **Quadro de Vagas:**  Através do quadro de vagas será possível visualizar as vagas por seção com a quantidade de vagas por função. Neste menu o usuário poderá incluir nova parametrização de admissão (mesma funcionalidade do Menu Admissão), e também parametrizar Demissões, Transferências, Promoções e Alterações de Seção.

   
Avançando a tela, são apresentados os menus relativos a Reajustes:

* **Reajuste Salarial**: Será possível definir previsão de reajuste salarial no cálculo do orçamento. O orçamento considerará para os funcionários da parametrização o novo salário a partir da data da mudança estipulada. O valor do novo salário será projetado a partir da parametrização de uma fórmula, percentual, ou "Valor Informado".

   
Avançando a tela, são apresentados os menus relativos à Folha de Pagamento:

* **Eventos movimento anterior:** Neste menu será possível fazer o lançamento e a manutenção de eventos baseados no movimento anterior. Este processo deve buscar os eventos selecionados (Hora extra, adicional noturno etc) na ficha financeira e totalizar o valor de cada evento por tipo de evento (Hora, valor, Referencia)

Primeiro devemos executar o processo de lançamento de eventos do movimento anterior, onde o sistema deverá preencher a grid de valores realizados (competência anteriores calculadas pela folha)

* **Grupo de Eventos:** Neste menu deverá parametrizar por seleção de funcionários os grupos de eventos que serão calculados como movimento de folha. Os grupos poderão ser incluídos especificamente por intervalo de competências, e ser definidos com data de pagamento no mês ou no próximo do mês, relativo a previsão.

* **Eventos Adicionais:** Será possível incluir eventos adicionais para cálculo da folha, para parametrizações de seleções de funcionários e com possibilidade de informar o intervalo de competências que os eventos adicionais serão calculados.

   
Avançando a tela, são apresentados os menus relativos Férias:

* **Cálculo de Férias:** O usuário poderá incluir parametrização de previsão de férias por seleção de funcionários e também considerar férias já marcadas, acionando o botão "Importar férias marcadas". Desta forma o sistema irá relacionar os registros de todos os funcionários que possuem férias a ser gozadas dentro do intervalo de competências do orçamento.

* **Diferença de Férias:**  A diferença de férias será executada apenas para casos em que houver férias partidas. Por exemplo: Foi cadastrada férias em 15/04/2015 a 14/05/2015. O aumento salarial para este funcionário foi parametrizado com data 01/05/2015. Desta forma, o sistema processará a diferença dos 14 dias de férias do mês de maio.

**Se o aumento salarial tivesse sido parametrizado para 01/04/2015, as férias seriam calculadas com o novo salário e não haveria diferença de férias a ser calculada.**  
   
   
Avançando a tela, são apresentados os menus relativos ao 13º salário:

* **Cálculo de 13º Salário:** Neste menu o usuário incluirá a parametrização por seleção de funcionários onde será possível definir por competência de pagamento:

**1)**Pagamento de 1º Parcela com parâmetro "Ajusta 1ª Parcela" marcado ou desmarcado.  
**2)**Pagamento de 2º Parcela com parâmetro.  
        Na parametrização será possível definir "Lança Códigos Fixos" e "Lança Eventos Programados".  
Em cada parametrização deverá definir também Competência do Lançamento e período, dia e mês do pagamento.  
   
Avançando a tela, são apresentados os menus relativos à Provisões:

* **Histórico de Provisões**: No orçamento poderá ser definida a geração da provisão de Férias e/ou 13º Salário. Para todos os funcionários ou selecionando determinados funcionários.

O cálculo de provisões futuras de férias poderá considerar os parâmetros:  
- "Permite valores negativos" – Caso o funcionário antecipar o gozo das férias, ou seja, tiver avos negativos, será calculado o valor negativo;  
- "Abate o valor de férias no mês" – Considera férias integrais no mês;   
- "Abate o valor das diferenças das férias no mês" – Como a diferença de férias considera os funcionários com férias partidas que tiveram aumento salarial no mês subsequente ao do pagamento das férias e somente funcionários com férias integrais no mês são considerados por este parâmetro, o mesmo não estará disponível no orçamento;

* "Abate o valor das férias na rescisão do mês" – Considera férias pagas na rescisão;  
     
  O cálculo de provisões futuras de rescisão poderá considerar o parâmetro "Gera provisão com valor zero para demitido no mês" onde será definido se gera provisão com valor zerado no mês da demissão de funcionários (considerando a previsão de demissões).  
     
     
  Avançando a tela, são apresentados os menus relativos à Geração de Encargos:

* **Geração de Encargos:** O sistema apresentará como opção a geração dos encargos através dos encargos ativos. Os encargos ativos funcionam como uma espécie de agrupador de encargos (por categoria) para facilitar a seleção dos encargos que seja deseja calcular.

O usuário deverá ter conhecimento dos encargos que serão/deverão ser considerados no cálculo do orçamento. Atenção para os encargos: FGTS, INSS empresa, INSS terceiros, INSS segurados, INSS, IRRF.

**Processo de Bloqueio/Desbloqueio de revisões de orçamento**

Para acessar este processo na tela de Dados de Orlamento | Processos | Bloqueio e Desbloqueio de Revisões

Este processo tem dois grid, o grid superior é responsável por mostrar os orçamentos, os orçamentos são mostrados de acordo com a pesquisa realizada, serão retornados apenas os orçamento que tenham o seu período total dentro das competências pesquisadas. São apresentados o código do orçamento e quantidade de revisões que o orçamento possui, ao clicar no registro de um dos orçamento no grid inferior serão carregados todas as revisões deste orçamento, sendo apresentando também nas colunas | Bloquear Edição | Bloquear cálculo | o estado atual destas permissões, para alterar o estado basta apenas marcar ou desmarcar o respectivo *checkbox*, após isto basta apenas clicar em executar.

**Atenção:**Apenas as revisões de um orçamento podem ser alteradas por vez, caso o usuário clique em outro orçamento no grid superior, as alterações feitas serão perdidas.
