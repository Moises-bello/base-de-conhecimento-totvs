---
content_hash: c7e46e459cf91bbf3e71eeebaf16ab23ee7fd37014cb5f17f210ca984d5d9bbc
fetched_at: '2026-06-29T00:05:59.362310+00:00'
page_id: '190513411'
product: rm
source: tdn-rm
title: Faturamento Parcial X Desdobramento
type: documentation
url: https://tdn.totvs.com/display/LRM/Faturamento+Parcial+X+Desdobramento
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Processo** | **:** | Faturamento Parcial |
| **Subprocesso** | **:** | Desdobramento X Faturamento Parcial |
| **Versão** | **:** | 11.82 |
|  |  |  |

**Faturamento Parcial**

Com a migração do movimento para .NET, estamos substituindo o conceito de Desdobramento pelo Faturamento Parcial.

O Desdobramento consiste em gerar um novo movimento quando o movimento original não tem a quantidade de seus itens totalmente recebida ou faturada. Este novo movimento é gerado com o mesmo número do movimento original, porém com a série acrescida de um sequencial que identifica o número de vezes que o movimento foi recebido ou faturado parcialmente e a quantidade do item pendente de recebimento ou faturamento.

Dependendo do processo de cada cliente, este modelo aumenta significativamente o número de movimentos na base de dados, o que ainda dificulta a montagem de consultas e relatórios demonstrando a rastreabilidade entre os movimentos.

No Faturamento Parcial não será gerado um novo movimento com a diferença de quantidade pendente de recebimento ou faturamento. A quantidade pendente será atualizada no campo de quantidade do próprio movimento. O status do movimento será alterado para Parcialmente Recebido ou Faturado.

O movimento será recalculado com base na nova quantidade.

Os valores originais do movimento serão armazenados em campos específicos.

Os benefícios do Faturamento Parcial em relação ao Desdobramento são:

Do ponto de vista do desenvolvimento, temos a facilidade para manutenção do aplicativo.

Já os clientes ganham com a melhoria na rastreabilidade dos movimentos facilitando a integração com outros aplicativos. Melhoria também na rastreabilidade dos movimentos que utilizam lote, número de série e grade. Outro ganho é o histórico dos lançamentos financeiros dos movimentos faturados parcialmente, onde todos os lançamentos financeiros são visualizados em uma única tela (Lançamentos – Financeiros).

**Visualização do Movimento**

Os itens totalmente recebidos ou faturados terão a quantidade e os valores zerados.

Um movimento totalmente recebido ou faturado terá os valores zerados.

Os campos zerados no recebimento / faturamento parcial do movimento serão:

* Valor Bruto, Valor Outros, Valor Liquido e Valor a Ratear para o Financeiro (TMOV)
* Valor Bruto Item (TITMMOV)
* Valor Rateio Centro de Custo do Movimento (TMOVRATCCU)
* Valor Rateio Departamento do Movimento (TMOVRATDEP)
* Valor Rateio Centro de Custo do Item de Movimento (TITMMOVRATCCU)
* Valor Rateio Departamento do Item de Movimento (TITMMOVRATDEP)

Observe nesta representação de um recebimento parcial, que o primeiro item foi recebido totalmente, ficando com a quantidade e o valor zerado. O movimento é recebido novamente, sendo recebido o segundo item totalmente. Agora o movimento ficou com todos os itens com quantidade e os respectivos valores zerados. Esta será mais uma forma de identificarmos que o movimento foi totalmente recebido, além do status que continuará sendo alterado para Recebido ou Faturado.

**Atenção**:

* No Faturamento Total ou Parcial de um movimento, quando no movimento destino o item for alterado, o sistema irá considerar que o item relacionado no movimento origem foi totalmente recebido ou faturado parcialmente. Será exibida uma mensagem alertando ao usuário quanto a este procedimento.

Caso o usuário queira que o item original permaneça pendente de recebimento, ele deverá ser excluído no momento do faturamento e em seguida incluído o novo item.

**Log de Faturamento**

Para armazenar um histórico dos faturamentos/recebimentos de um movimento, criamos um Log de Faturamento que é composto pelas seguintes tabelas:

**TMOVLOGFAT** à Log dos Faturamentos

**TMOVRATCCULOGFAT** à Log dos Rateios de Centro de Custo

**TMOVRATDEPLOGFAT** à Log dos Rateios de Departamento

**TTRBMOVLOGFAT** à Log dos Tributos do Movimento

**TITMMOVLOGFAT** à Log dos Itens de Movimento

**TITMMOVRATDEPLOGFAT** à Log dos Itens – Rateio Departamento

**TITMMOVRATCCULOGFAT** à Log dos Itens – Rateio Centro de Custo

Além dessas tabelas, na TITMMOV criamos os campos: VALORBRUTOITEM (que nas versões anteriores, era apresentado e calculado somente na tela como ‘Valor Item’), o campo VALORBRUTOITEMORIG (na tela: Valor Original do Item) e o campo de QUANTIDADETOTAL (que apresenta a quantidade original, a ultima quantidade do item antes do mesmo ser faturado pela primeira vez)

Através dessas tabelas e desses novos campos da TITMMOV será possível identificar os valores iniciais de um movimento, bem como os diversos faturamentos parciais que possam ter ocorrido.

**Atenção:**

* O Campo ‘Cancelado’  nessas novas tabelas serve para indicar que o movimento destino do faturamento/recebimento foi cancelado ou excluído.
* Na conversão da base de dados para a versão 10.80, os movimentos com status Pendente e A Faturar (status = A) terão os novos campos da TITMMOV,  VALORBRUTOITEM e VALORBRUTOITEMORIG alterados somente quando o movimento sofrer alguma alteração, isto porque o Valor Bruto do Item não era gravado na base. Não consideramos viável a execução de um script para atualização desses campos, pois dependendo do volume de dados da base o mesmo poderia travar na execução.
* Os movimentos incluídos na versão 10.80 ou incluídos em versões anteriores que estejam com status Pendente ou A Faturar (status = A), terão os campos de valores originais do item (VALORBRUTOITEMORIG e QUANTIDADETOTAL) atualizados assim que forem salvos. Esses campos só deixaram de ser atualizados no primeiro faturamento ou recebimento parcial do movimento, quando seu status passar para ‘G’ – Parcialmente Faturado ou Recebido.

**Valores Originais**

Para que o cliente possa consultar os Valores Originais do movimento e o Log de Faturamento, foi disponibilizado na interface do movimento, no grupo Consultas, o subgrupo ‘Valores Originais’.

Por esta interface será possível consultar os detalhes de todos os faturamentos do movimento.

Na parte superior temos os valores totais do Movimento: Valor Bruto, Valor Outros, Valor Liquido e Valor Lançamento Financeiro. Já na parte inferior temos o histórico dos faturamentos.

Na interface do item de movimento, os Valores Originais serão apresentados no Grupo Identificação, Sub Grupo Cabeçalho.

**Atenção**:

* Esses Valores somente serão apresentados se o Movimento estiver com status ‘G’ – Fat/Rec Parcialmente ou ‘F’ – Faturado / Recebido.
* Chamamos atenção para o processo de ‘Gerar Movimento à partir de Movimento Selecionado’ quando o mesmo tiver como movimento origem um movimento que foi Parcialmente Faturado ou Totalmente Faturado (status Recebido), pois as quantidades estarão zeradas. Este processo foi modificado para que nesta situação,  seja copiado para o campo de quantidade do movimento destino (o que está sendo criado) o conteúdo do campo Quantidade Total do item de movimento origem.

**Status do Movimento**

O movimento Faturado Parcialmente terá um status diferenciado: foi criado o Status ‘G’ – Parcialmente Faturado / Recebido.

No modelo do Desdobramento, o movimento ‘Recebido / Desdobrado’ ou ‘Faturado / Desdobrado’ não possuia um status específico. Para apresentar esta descrição na visão do movimento, o sistema consistia se o status do movimento era Faturado ou A Pagar (letra F) e o campo IDMOVPEDDESDOBRADO não estava nulo.

**Status do Movimento**

Houve uma alteração no filtro de movimentos para adequação ao processo de Faturamento Parcial. Na interface fixa (parte superior do filtro) no campo de status foram criadas duas novas opções e o status Pendente foi modificado.

Status novos:

Parcialmente Recebido ou Parcialmente Faturado à irá selecionar os movimentos com status = G (Parcialmente Faturado ou Recebido);

Não Recebido ou Não Faturado à irá selecionar os movimentos com status = A (movimentos que não foram parcialmente faturado/recebido nem faturado/recebido totalmente);

O status Pendente agora irá selecionar os movimentos com status = A e os movimentos com status = G.

**Impacto nos Relatórios**

Para auxiliar na montagem de relatórios, consultas e fórmulas, foi criada uma nova função de fórmula, KQTTOTAL ‘Quantidade Total do Item de Movimento’ que retorna a quantidade inicial do item de movimento.

Para que seja possível analisar os diversos faturamentos de um determinado movimento, foram criados os seguintes relatórios:

* Relatório de Rastreamento: Mostrando toda a árvore, ou a partir de um movimento saber qual e a origem e/ou destino que foi gerado.
* Relatório de Quantidade por Status: Teremos os dois campos de quantidade, Quantidade e Quantidade Total.
* Relatórios de Pedidos Pendentes: Considerando status A e G, retornando o campo quantidade filtrando por tipo de movimento.
* Relatório de Quantidade Pedida e Recebida, esse relatório trará a quantidade dos itens que foram solicitadas em um pedido e o que foi atendido, para isso será necessário buscar a quantidade do movimento de origem e a quantidade dos movimentos de destino.
* Relatório de Quantidades, esse relatório trará a Quantidade Total (desconsiderando o faturamento parcial).

Todos esses relatórios estão disponíveis no book de relatórios e sugerimos que sejam importados na base de dados dos clientes.

**Observação:** Consideramos que as informações constantes nestes relatórios são as essenciais para análise do faturamento dos movimentos. Se algum cliente necessitar de mais alguma informação devido ao seu processo, o mesmo deverá dar manutenção no relatório conforme suas necessidades.

**Parâmetros Alterados**

O parâmetro ‘Efeito Pedido’ que no modelo do desdobramento define se o movimento origem será desdobrado, desdobrado automaticamente ou não será desdobrado, teve as descrições das opções alteradas para atender o modelo de Faturamento Parcial.

Onde se lia: Desdobrar, lê-se agora ‘**Faturar Parcialmente**’, Não Desdobrar, lê-se ‘**Não Faturar Parcialmente**’ e Desdobrar Automático, lê-se ‘**Faturar Parcialmente Automático.**

A finalidade desse parâmetro permanece semelhante ao do Desdobramento.

Escolhendo: **Faturar Parcialmente** será apresentada uma mensagem com as opções: SIM, NÃO e AUTOMÁTICO, onde o usuário deverá optar por uma delas. Optando por SIM, será apresentada a tela para edição do movimento origem que está sendo faturado (esta opção só estará disponível para movimentos que não tenham sido originados de agrupamento). Optando por NÃO, o movimento origem será baixado (concluído) independente de estar sendo faturado parcialmente. Já a opção AUTOMÁTICO, o movimento origem será faturado parcialmente automaticamente.

Escolhendo: **Não Faturar Parcialmente**, o movimento origem será baixado (concluído) independente de estar sendo faturado parcialmente.

Escolhendo: **Faturar Parcialmente Automático**, o movimento origem será faturado parcialmente automaticamente, fechando a tela de edição do movimento origem.

**Parâmetros Alterados**

Impacto Financeiro:

Outro parâmetro que também foi alterado é o ‘Lançamento Pedido Desdobrado’ que teve a descrição alterada para ‘**Lançamento Pedido Faturado Parcialmente**’. O mesmo continua definindo se será gerado um lançamento financeiro para o movimento faturado parcialmente.

No modelo de Desdobramento,  tínhamos as opções: Não Gerar, Gerar e Copiar.

No modelo de Faturamento parcial, temos as opções: Não Gerar e Gerar.

A opção ‘Copiar’ foi **desabilitada**.

**Parâmetros Alterados**

A funcionalidade da opção ‘Copiar’  tem o mesmo efeito de marcar a opção Não gerar, juntamente com a opção Nenhum do Parâmetro ‘**Lançamentos no Faturamento após Geração do Mov.**’.

**Impacto Contábil**

No modelo do Desdobramento, se um tipo de movimento estava parametrizado para gerar contabilização e o movimento fosse desdobrado, era gerado contabilização para o movimento original e para o desdobrado, sendo que a contabilização do desdobrado era referente somente ao valor pendente.

No modelo do Faturamento Parcial, a contabilização ocorrerá somente para o movimento original, ou seja, NÃO será gerado contabilização para o valor pendente.

**Impacto no Estoque**

Houve uma mudança no comportamento do estoque com o Faturamento Parcial.

No modelo de Desdobramento, quando um movimento que afeta estoque (qualquer saldo), seja aumentando ou diminuindo, é desdobrado e o parâmetro ‘Afeta Estoque Após Faturado / Recebido’ esta marcado, o estoque considera a quantidade do movimento original **mais** a quantidade do movimento desdobrado.

Caso o parâmetro ‘Afeta Estoque Após Faturado / Recebido’ não esteja marcado, o estoque é refeito considerando somente a quantidade do movimento desdobrado.

**Impacto no Estoque**

Agora, com o Faturamento Parcial...

Para movimento Faturado ou Recebido Parcialmente que afeta estoque, seja aumentando ou diminuindo, cujo parâmetro ‘Afeta Estoque Após Faturado / Recebido’ esteja marcado, o estoque NÃO será refeito, continuará refletindo a quantidade original do movimento.

Caso o parâmetro ‘Afeta Estoque Após Faturado / Recebido’ não esteja marcado, o estoque será refeito considerando a nova quantidade do movimento após o faturamento parcial.

**Conversão de Dados**

Para facilitar a conversão dos dados dos clientes que trabalham com o modelo de desdobramento, foi criado um wizard que irá converter, filtros de movimento, filtros de relatórios, filtros de usuários, atualização de relatórios, atualização de consultas SQL e atualização de fórmulas com as novas informações do modelo de Faturamento Parcial.  A execução desse wizard de conversão deverá ser executado pelo cliente, pois ele deverá analisar os cadastros que deverão poderão ser alterados.

Para realizar esta conversão, seguimos os seguintes critérios:

**Atualização dos Filtros (de Movimentos, Relatórios e Usuários)**

* Será criada uma consulta SQL na base de dados do cliente para retornar os movimentos com status ‘Pendente’ e ‘Parc. Faturado/Recebido’ (consulta: MOVSQL01)
* Filtros que são aplicados na tabela ‘TMOV’:
  + utilizam o campo STATUS = PENDENTE à serão atualizados para STATUS IN MOVSQL01
  + utilizam o campo STATUS <> PENDENTE à serão atualizados para STATUS NOT IN MOVSQL01

**Atualização das Consultas SQL**

* STATUS = ‘A’ à STATUS IN (‘A’, ‘G’)
* STATUS = ‘F’ à STATUS IN (‘F’, ‘G’)
* QUANTIDADE à QUANTIDADETOTAL

**Atualização dos Relatórios**

* QUANTIDADE à QUANTIDADETOTAL

**Atualização das Fórmulas**

* STATUS = ‘A’ à STATUS IN (‘A’, ‘G’)
* STATUS = ‘F’ à STATUS IN (‘F’, ‘G’)
* QUANTIDADE à QUANTIDADETOTAL
* KQT à KQTTOTAL

Para mais informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx).

**Comunidade** @*materiais*

**Canais de Atendimento:**

* Chamado: através do portal TOTVS [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/).
* Telefônico: 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM) ...

   

  *.*
