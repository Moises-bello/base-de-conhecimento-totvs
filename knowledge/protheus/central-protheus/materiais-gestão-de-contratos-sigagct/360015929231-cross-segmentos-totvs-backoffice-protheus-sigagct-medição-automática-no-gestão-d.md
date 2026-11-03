---
article_id: 360015929231
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a5edd119704dd54ba1ff5bcc870439a772784ef59ffdaeb465db056b6a8dc9b7
fetched_at: '2026-06-28T22:37:19.732541+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT  - Medição Automática
  no Gestão de Contratos com Execução via Menu
type: support-article
updated_at: '2026-06-12T17:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015929231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-no-Gest%C3%A3o-de-Contratos-com-Execu%C3%A7%C3%A3o-via-Menu
---

A rotina CNTA260 permite a Medição Automática no módulo Gestão de Contratos do Protheus, gerando medições conforme cronogramas financeiros para contratos fixos. A execução pode ser via menu, JOB ou Schedule, respeitando parâmetros como MV\_ATUGCT e MV\_MEDDIAS. A medição automática não funciona para contratos com Condição de Pagamento Tipo 9 e possui limitações para filiais distintas. Customizações podem ser necessárias para ajustes específicos.

**Dúvida**

Medição Automática no Gestão de Contratos via Execução por Menu.

**Ambiente**

Cross Segmentos - Totvs Backoffice Protheus -   Gestão de Contratos  – A partir da versão 12

**Solução**

A rotina de Medição Automática (CNTA260) pode ser executada através do seu acesso via Menu do modulo de Gestão de Contratos através do caminho: "*Gestão de Contratos -> Miscelânea -> Processamento -> Gerar Medições (CNTA260)*":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9927465724695)

Ao acessar a rotina e confirmar o processamento das medições automáticas, o Sistema irá verificar através dos cronogramas financeiros quais parcelas tem data prevista de medição inferior ou igual a data base de execução da rotina. Para estas parcelas então, serão geradas as medições conforme valores previstos e programados nos cronogramas do contrato (financeiro e físico).

Importante: Ao executar a rotina CNTA260 via menu, quando as medições são geradas com sucesso, o sistema não dispara nenhuma mensagem, a rotina é finalizada e retorna ao menu.

A Medição automática tem sua execução apenas para contratos Fixos, com Cronograma Financeiro (Medição Eventual = Não), pois a data que o sistema verifica para buscar as medições pendentes é **Data Prevista Med. (CNF\_PRUMED) do Cronograma** que deve ser **a mesma que a data do Parãmetro  MV\_ATUGCT.**

**1-** Configurar um tipo de contrato com o campo CN1\_MEDAUT=1 assim ficara entendido que os contratos que possuem essa configuração do tipo de contrato estão aptos a serem medidos de forma automática.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6595690691863)**

**2- Parâmetros de configuração para o funcionamento da execução da Medição Automática (CNTA260):**

**MV\_MEDDIAS** - Indica a quantidade de dias (anteriores a data do **MV\_ATUGCT**) para pesquisa/busca das medições pendentes.

Para que sejam processadas as medições automáticas todos os dias, é recomendado o uso do parâmetro **MV\_MEDDIAS** com valor "0", dessa forma será executada a medição apenas para Medições com data prevista**(CNF\_PRUMED)** no Cronograma Financeiro igual a data do **MV\_ATUGCT**.

**Exemplo do Parâmetro MV\_MEDDIAS** diferente de **0** .

**MV\_MEDDIAS** Preenchido com **10**  dias  e o conteúdo do parâmetro **MV\_ATUGCT** esteja preenchido com  **20220715**,  a rotina vai se basear na data informada no parâmetro **MV\_ATUGCT** e verificar se existem medições  para ser gerada contando 10 dias para trás a partir do dia 15/07/2022,14/07/2022,13/07/2022,12/07/2022,11/07/2022,10//07/2022,09/07/2022,08/07/2022,07/07/2022,06/07/2022 data informada no parâmetro para busca de medições não realizadas para realizar automaticamente.

Conforme exemplo acima parâmetro **MV\_ATUGCT=20220715 e MV\_MEDDIAS =10** nesse exemplo para que o sistema possa realizar as Medições Automáticas logar no sistema com a mesma data do parâmetro MV\_ATUGCT= **20220715** .

A data que o sistema verifica para buscar as medições pendentes é a **Data Prevista Med.(CNF\_PRUMED) = 10/07/2022** do cronograma financeiro do Contrato nesse exemplo o sistema ia executar e gerar a medição automática.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7626605326359)

***Obs1:***

Caso o **MV\_MEDDIAS** esteja com valor "0", será executada a medição apenas para Medições com data prevista no Cronograma Financeiro igual a data do **MV\_ATUGCT**.

**MV\_ATUGCT** - Indica a data que o sistema considera para geração das Medições pendentes. Se houver o conteúdo do parâmetro **MV\_MEDDIAS,** considera também esse numero de dias pra trás da data do MV\_ATUGCT.

**MV\_MEDPEND** - Caso exista erro na criação das medições, esse parâmetro determina que o Sistema deve pesquisá-las e encerrá-las automaticamente. Ele é executado após a execução do JOB (quando existente), para que se possa criar as medições automáticas, e pode ser configurado como 1=Sim ou 2=Não.

**MV\_CT26021** - Gerar todas as medições automáticas pela rotina CNTA121 ? . T = Sim ***(Com a descontinuação da Medição pelo programa CNTA120, este parâmetro deve ser usado como T (Sim)***.

***Obs2:***

**A medição automática funciona somente na filial logada? O sistema gera Medição Automática para filiais diferentes ?**

A rotina CNTA260 tem uma limitação em relação as permissões de medição em filiais distintas a do contrato(**CN9\_FILCTR**), não realizando a inclusão em qualquer filial além da filial de origem do contrato. Essa limitação se deve há alguns fatores, listados abaixo:

* Para processamento das medições é realizada uma consulta SQL a diversas tabelas do SIGAGCT(CN9, CNA, CNF, CN1, CNL e CPD) que são todas filtradas pelo compartilhamento via xFilial de cada uma dessas tabelas. Em especial a CN1(Tipo de Contrato) e CNL(Tipo de Planilha) são essenciais para filtrar se o contrato em questão deve ou não ser medido de maneira automática, dessa forma seria necessário que a execução ocorresse na filial original para obter a informação correta ou que essas tabelas fossem compartilhadas;
* Hoje o sistema permite que o usuário dê permissão para que um contrato seja medido em um número indeterminado de filiais, dessa forma quando o sistema seleciona uma competência/parcela para ser medida não é possível tomar a decisão de maneira automática de em qual filial a medição deve ser realizada

Para realizar uma operação desse tipo seria necessário que as tabelas do SIGAGCT fossem compartilhadas, apenas em um ambiente configurado dessa forma seria possível o correto processamento e mesmo nesse cenário as medições seriam realizadas na filial *logada* no momento da execução do programa, desde que o contrato tivesse permissão para ser medido na filial em questão.

Maiores informações referente ao compartilhamento de tabelas do GCT:

[GCT0010 - Compartilhamento Tabelas SIGAGCT](https://tdn.totvs.com/display/PROT/GCT0010+-+Compartilhamento+Tabelas+SIGAGCT)

***Obs3:***

O processo de medição automática pode também ser configurado via JOB da seguinte forma:

**1-** No appserver.INI configurar o JOB de acordo com os exemplos abaixo:

**[ONSTART]**  
Jobs=MEDGCT

**[MEDGCT]**  
Main=CNTA260 ==> ROTINA  
Environment=PROTHEUSTOP ==> AMBIENTE  
nParms=3 ==> QTDE. DE PARAMETROS  
Parm1=99 ==> EMPRESA  
Parm2=01 ==> FILIAL

***Obs4:***

A rotina de medição automática pode também ser processada por agendamento via Schedule, neste caso, é possível realizar o agendamento da execução da rotina de Medições/Entregas automáticas. Para isto, basta que no Schedule seja cadastrada a rotina CNTA260. Assim, conforme agendamento cadastrado, a rotina descrita no item 1 será executada de forma automática, gerando assim as medições.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9370930966423)

Após a configuração da Schedule, se atentar a configuração da recorrência, no exemplo abaixo estou levando em consideração deixar a rotina processando o dia todo, sem data de termino:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9370932006807)

Para maiores informações Consulte o Artigo  - [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Medição Automática via Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25196624458903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-via-Schedule?source=search)

***Obs5:***

A rotina de Medição automática não contempla a execução de Contratos que possuem uso de Condição de Pagamento configurada com Tipo 9.

Dessa forma para contratos que usam este tipo de Condição de Pagamento, suas medições devem ser realizadas manualmente através da rotina CNTA121, onde conforme o uso da condição Tipo 9, devem ser inseridas as informações nos campos de "Data" e "Valor" das parcelas no cabeçalho da medição (tabela CND) na inclusão da medição.

Abaixo artigo do módulo Faturamento que informa os campos que também devem ser criados na tabela de CND do cabeçalho de medição para que possam ser informados **na inclusão manual da medição com Cond. Pagto. Tipo 9** (Análogos aos campos do Pedido de Vendas)..

[FAT0033 - Mensagem TMKTIP905 - A quantidade de parcelas não está compatível](http://tdn.totvs.com/pages/releaseview.action?pageId=225950783)

![](https://totvssuporte.zendesk.com/attachments/token/vLT0RaSmjR33x5f37aNrQTtL8/?name=image.png)

***Obs6:***

**Perg.:** No processamento da rotina de medição automática o campo de Emissão (C7\_EMISSAO) do pedido gerado fica com a informação da "data base" do sistema em que ela é processada. Existe alguma configuração para se alterar esta informação da Emissão (C7\_EMISSAO) do Pedido gerado ?

**Resp.:** Atualmente não há uma configuração para se alterar este comportamento padrão do sistema.

Caso deseje pode-se avaliar a possibilidade através de uma customização conforme a necessidade.

Segue abaixo artigo com os pontos de entrada disponíveis da rotina para que se possa avaliar algum que melhor possa atender conforme a necessidade.  
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260)  
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)

***Obs7:***

A funcionalidade de Medição Automática em seu padrão não contempla o uso da funcionalidade do campo de "Medição com quantidade Zerada" (CXN\_ZERO=Sim), onde este no padrão do módulo é contemplado apenas para uso pela rotina de Medição no processo manual (CNTA121).

Caso se deseje o uso o mudança do campo na Medição Automática, pode-se avaliar a possibilidade através de uma customização conforme a necessidade.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)

***Saiba Mais:***

[GCT0052\_Medição\_Automática](https://tdn.totvs.com/x/hjACE)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Medição Automática via Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25196624458903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-via-Schedule?source=search)

[MP - SIGAGCT - Como fazer para as Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição (CNTA121) ? - MV\_CT26021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034124234-MP-SIGAGCT-Medi%C3%A7%C3%B5es-autom%C3%A1ticas-geradas-n%C3%A3o-podem-ser-visualizadas-na-rotina-CNTA121-%C3%A9-apresentado-o-Help-Op%C3%A7%C3%A3o-indispon%C3%ADvel-para-medi%C3%A7%C3%B5es-realizadas-com-a-rotina-de-medi%C3%A7%C3%A3o-padr%C3%A3o-)

[MP - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-MP-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
