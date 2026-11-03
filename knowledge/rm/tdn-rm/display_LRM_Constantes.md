---
content_hash: e3d4787b7f0dc47779bc041c1778761c10e61be5ece573c31d264af43111be4c
fetched_at: '2026-06-29T00:09:25.868123+00:00'
page_id: '423938180'
product: rm
source: tdn-rm
title: Constantes
type: documentation
url: https://tdn.totvs.com/display/LRM/Constantes
version: 25
---

As constantes do sistema são caracteres simples ou numerais que são usados para representar o status de um movimento, cotação, produto ou outros registros no sistema, quando este é gravado no banco de dados. Em alguns casos uma mesma constante pode representar status distintos, dependendo da parametrização do recurso ou processo do sistema. Conhecer o significado de cada um dos status e quando eles são atribuídos é importante na execução de algumas tarefas, como ao criar um filtro, executar uma sentença ou gerar um relatório gerencial.

Constantes do Movimento - Tabela TMOV

* **Status do movimento**

Os status do movimento são gravados na tabela TMOV.STATUS e referem-se ao estado atual do movimento. Esses status são atribuídos conforme a parametrização utilizada no movimento ou após a execução de algum processo (como por exemplo o status 'Cancelado').

| Constante | Representação |
| --- | --- |
| A | Pendente / A Faturar |

**Pendente**: Em movimentos do tipo 1.1 significa que o movimento foi incluído e ainda não foi recebido ou faturado;

**A Faturar**: Em movimentos do tipo 2.1 significa que o movimento foi incluído e ainda não foi recebido ou faturado. Em outras palavras pode-se dizer que o movimento está apto a ser faturado. Em movimentos do tipo 1.2 ou 2.2, o status a faturar é atribuído quando o movimento usa integração com o TOTVS – Gestão Financeira e o parâmetro 'Fatura na Inclusão' está desabilitado. No momento em que o usuário gera o financeiro para movimentos com o status 'A Faturar' o status é atualizado para 'A Pagar' ("F").

| Constante | Representação |
| --- | --- |
| B | Bloqueado |

Em movimentos que utilizam controle orçamentário/financeiro o status 'Bloqueado' é atribuído quando o valor do movimento ultrapassa o valor do orçamento em determinado período e a parametrização do movimento determina que a ação ao exceder o valor orçado é bloquear.

| Constante | Representação |
| --- | --- |
| C | Cancelado |

Indica que o movimento foi cancelado pelo usuário.

| Constante | Representação |
| --- | --- |
| F | Recebido / Faturado / Rec / Desdobrado/A Pagar/A Receber |

**Recebido**: O movimento foi recebido completamente, ou seja, gerou movimento do tipo 1.2.

**Faturado**: O movimento foi faturado completamente, ou seja, gerou movimento do tipo 2.2.

**Rec / Desdobrado**: O movimento de compra foi Recebido parcialmente e sofreu um desdobramento. Nas versões migradas para o novo modelo Backoffice em que não existe mais o conceito de desdobramento, este status foi substituído pelo status 'Parcialmente Recebido'.

**Fat / Desdobrado**: O movimento de venda foi Faturado parcialmente e sofreu um desdobramento. Nas versões migradas para o novo modelo Backoffice em que não existe mais o conceito de desdobramento, este status foi substituído pelo status 'Parcialmente Faturado'.

**A Pagar / A Receber**: Indica um movimento que está integrado ao TOTVS – Gestão Financeira e os lançamentos financeiros já foram gerados. A descrição 'a pagar' ou 'a receber' vai depender da parametrização do movimento.

| Constante | Representação |
| --- | --- |
| G | Parcialmente Recebido / Parcialmente Faturado |

Os status 'Parcialmente Recebido' e 'Parcialmente Faturado' foram criados a partir da versão 11.0.0 para contemplar o recurso Faturamento Parcial no novo modelo Backoffice em substituição aos antigos status de desdobramento, sendo estes usados respectivamente no faturamento de movimentos de entrada e saída.

| Constante | Representação |
| --- | --- |
| N | Normal |

O status normal é atribuído aos movimentos que não poderão ser recebidos ou faturados segundo a parametrização do movimento e não tem integração com o TOTVS Gestão Financeira

| Constante | Representação |
| --- | --- |
| P | Parcialmente Quitado |

Indica que o movimento está integrado com o TOTVS Gestão Financeira sendo que um ou mais lançamentos financeiros estão em aberto e os restantes foram baixados.

| Constante | Representação |
| --- | --- |
| Q | Quitado |

O movimento gerou lançamentos financeiros e estes por sua vez foram totalmente baixados pelo TOTVS Gestão Financeira.

| Constante | Representação |
| --- | --- |
| R | Não Processado |

Os movimentos gerados com estado 'Não Processado' não modificam o estoque de produtos, não geram lançamentos financeiros e não são contabilizados.

| Constante | Representação |
| --- | --- |
| U | Em Faturamento |

No momento que se inicia um processo de faturamento (ou recebimento) de um movimento qualquer, seu status é temporariamente alterado para 'Em Faturamento'. Ao fim do processo, o movimento é alterado novamente para o seu status atual, normalmente diferente do inicial. Este procedimento é necessário, pois se alguma coisa que impeça a conclusão processo iniciado ocorrer, será possível rastreá-lo e tomar as devidas providencias para regularizar sua situação.

* **Status do Movimento (Integração TOTVS Manutenção )**

Movimentos integrados ao TOTVS Manutenção normalmente são incluídos através deste e recebem status referentes a situação da ordem de serviço que os gerou. Os possíveis status atribuídos à movimentos gerados a partir do TOTVS Manutenção são:

| Constante | Representação |
| --- | --- |
| O | Aguardando Análise |

Quando o movimento é incluído através do TOTVS Manutenção, este recebe o status 'Aguardando Análise'.

| Constante | Representação |
| --- | --- |
| Y | Não Iniciado |

A constante "Y" é atribuída às ordens de serviços aprovadas pelo cliente, mas que ainda não tiveram sua execução iniciada.

| Constante | Representação |
| --- | --- |
| E | Em Andamento |

O status 'Em Andamento' indica uma ordem de serviço que entrou em execução.

| Constante | Representação |
| --- | --- |
| Z | Terminado |

É atribuído às ordens de serviços concluídas.

* **Status do Movimento (Integração TOTVS Planejamento e Controle da Produção)**

O Status de programação do movimento é calculado pelo serviço do TOTVS Planejamento e Produção. Este cálculo é feito a partir da analise dos status de programação dos itens de movimento para determinar o status do movimento. O resultado pode ser um dos estados abaixo:  
*A programar*  
O pedido de venda foi incluído, mas nenhum de seus itens de venda foi associado a uma ordem de produção.  
*Programado*  
Todos os itens do pedido de venda foram associados a uma ordem de produção.  
*Parcialmente Programado*  
Pelo menos um item do pedido de venda foi associado a uma ordem de produção.  
*Parcialmente Finalizado*  
Pelo menos um item do pedido programado foi finalizado. ***Observação***: o status Parcialmente Programado prevalecerá caso algum dos itens não esteja associado a uma ordem de produção  
*Finalizado*  
Todos os itens tiveram sua produção finalizada.

* **Status do Movimento Cotado**

Os movimentos que entram em processo de cotação têm seu status gravado na coluna "TMOV.STSCOMPRAS" diferente dos status do movimento "TMOV.STATUS".

O status de cotação da solicitação pode ser visualizado através da visão de movimentos, habilitando a coluna 'Status do Mov. De Compras'.

Os possíveis status para a coluna "TMOV.STSCOMPRAS" (Status de Mov. de Compras**)** são:

| Status | Representação | Indicação |
| --- | --- | --- |
| C | Em Cotação | Indica que um o mais itens do movimento em questão entrou em processo de cotação. |
| P | Parcialmente Cotado | Indica que o movimento em questão foi cotado parcialmente. |
| T | Cotado | Indica que o movimento em questão teve todos os seus itens cotados. |
| G | Gerado por Cotação | Indica que o movimento em questão foi gerado a partir de uma cotação. |

**Exemplos:**

**Status "Em Cotação"**: Foi criado uma solicitação de compras contendo 3 itens. Em seguida, foi criado uma cotação para que seja realizado a compras de apenas 1 item deste movimento. Ao criar a cotação, o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** será preenchido com o valor **"C" (Em Cotação)** pois, 1 dos 3 itens do movimento entrou em processo de cotação.

**Status "Parcialmente Cotado":**Foi criado uma solicitação de compras contendo 3 itens. Em seguida, foi criado uma cotação para que seja realizado a compras de apenas 1 item deste movimento. Após realizar todo o processo de cotação para este item e finalizar gerando a ordem de compra,  o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** será preenchido com o valor **"P"** **(Parcialmente Cotado)**.

Existem outras situações onde o status permanecerá como **"Parcialmente Cotado"**,  por exemplo:

**Caso 1:** Em um movimento de 3 itens onde 2 foram cotados e 1 Estornado, o movimento será encerrado, ficando com o status de **"Recebido"** ou **"Faturado"** de acordo com a parametrização do tipo de movimento e o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** permanecera com o status **"P" (Parcialmente Cotado)**, ou seja, apenas parte do movimento foi cotado.

**Caso 2:** Em um movimento de 3 itens onde 2 foram cotados e 1 faturado direto para o movimento de Ordem de Compra sem passar pelo processo de cotação, o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** permanecera com o status **"P"** **(Parcialmente Cotado)**, ou seja, apenas parte do movimento foi cotado.

**Status "Cotado":** Foi criado uma solicitação de compras contendo 3 itens. Em seguida, foi criado uma cotação para que seja realizado a compras de todos itens deste movimento. Após realizar todo o processo de cotação para este movimento e finalizar gerando a ordem de compra, o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** será preenchido com o valor  **"T"** **(Cotado).**

**Status "Gerado por Cotação":**Geralmente este status será preenchido nos movimento de Ordem de Compra que são gerados a partir da cotação. Após realizar todo o processo de cotação e finalizar gerando a ordem de compra,  o campo **TMOV.STSCOMPRAS (Status de Mov. de Compras)** será preenchido com o valor **"G"** **(Gerado por Cotação)**.

* **Status da Separação**

Ao utilizar o recurso de separação o movimento passa a utilizar a coluna TMOV. STATUSSEPARACAO para gravar o status de separação do movimento. Da mesma forma que os status de cotação, para visualizar o status de separação do movimento é preciso habilitar a visualização da coluna no aplicativo. Os possíveis status para a separação são:

| Status | Representação | Indicação |
| --- | --- | --- |
| '' '" | Vazio | Quando o movimento é criado é não entrou em processo de separação seu status não é preenchido. |
| E | Em Separação | Indica que o movimento em questão esta em processo de separação. |
| N | Não Separado | Quando um movimento entra em separação e o processo 'Voltar Status Separação Anterior' é executado o status do movimento é setado como não separado. |
| S | Separado | Indica que o movimento em questão teve seu processo de separação finalizado com ou sem divergências. |

* **Status****Concluído**

Ao utilizar o processo de Concluir Pedidos o movimento passa a utilizar a coluna TMOV. STSCONCLUIDO para gravar o status de conclusão do movimento.  Os possíveis status são:

| Status | Representação | Indicação |
| --- | --- | --- |
| '' '" | Vazio | Quando não foi realizado o processo. |
| C | Concluído | Quando um movimento foi total concluído, ou seja, todos os itens com todas as quantidades |
| P | Parc. Concluído | Quando um movimento foi parcialmente concluído, ou seja,  parte de um item ou alguns itens do movimento. |

Constantes do Item de Movimento - Tabela TITMMOV

* **Status do Item de Movimento (Integração TOTVS Planejamento e Controle da Produção)**

O Status de programação do item é referente ao status da ordem de produção no TOTVS Planejamento e Controle da Produção. Os status de programação são enumerados de 0 a 6, representando as fases da ordem de produção e a descrição de cada uma pode ser personalizado de acordo com o desejo do usuário.

| Status | Representação |
| --- | --- |
| 0 | Criada |
| 1 | Aguardando Recurso |
| 2 | Pronto para iniciar |
| 3 | Parcialmente concluído |
| 4 | Interrompida |
| 5 | Concluída |
| 6 | Cancelada (RM Factor) / Indefinida (RM Nucleus) |

***Observação***: Quando a ordem de produção é cancelada no TOTVS Planejamento e Controle da Produção, o item de movimento fica o com status de programação "Indefinido", pois, a ordem de produção, perde o vínculo com o item de movimento.

Constantes de Relacionamento - Tabela TMOVRELAC

* **Tipos de Relacionamento do Movimento**

O tipo de relacionamento do movimento é gravado na coluna TMOVRELAC.TIPORELAC representando o motivo pelo qual o registro de relacionamento foi criado (Faturamento, Desdobramento, Exportação ou Devolução). Os valores possíveis para este campo são:

| Tipo de Relacionamento | Representação |
| --- | --- |
| P | Faturamento do Pedido |
| D | Distribuição |
| Q | Desdobramento do Faturamento |
| V | Devolução |
| E | Pedido Exportação |
| T | Estoque Terceiros |
| S | Substituição NFe |
| R | Cópia Simples com Relacionamento |
| C | CT-e |
| A | NF-e de Ajuste |
| O | NF-e de Ajuste - Estorno |
| L | NF-e Produtor Rural |
| G | Devolução de Consignado |
| M | Documento Eletrônico complementar |
| X | Remessa Parcelada Exportação |

Constantes da Cotação - Tabela TCCOTACAO

* **Status da Cotação**

Quando uma cotação é criada seu status é gravado no banco de dados como uma constante numérica. O status da cotação representa em qual o estágio (fases) do processo a cotação se encontra.

| Status | Representação |
| --- | --- |
| 1 | Em Composição |
| 2 | Aguardando Resposta do Fornecedor |
| 3 | Pronto para Cálculo (status interno) |
| 4 | Pronto para Calcular o Quadro Comparativo |
| 5 | Em Negociação |
| 6 | Pedido de Compra Gerado |
| 7 | Cancelada |
| 8 | Liberada |
| 9 | Cotação Exportada |

Constantes dos Itens da Cotação - Tabela TCCOTACAOITMMOV

* **Status da Cotação**

Quando os itens de uma cotação são criados, seu status é gravado no banco de dados como uma constante numérica. O status do item da cotação representa em qual o estágio (fases) do processo o item se encontra.

| Status | Representação |
| --- | --- |
| -1 | Excluído |
| 1 | Ativo |
| 2 | Ordem de Compra |
| 3 | Concluído |
| 4 | Estornado |

Constantes dos Itens da Cotação - Tabela TCITMORCAMENTO

* **Status do Item da Cotação**

Representa o status de cotação de cada item por Fornecedor.

| Status | Representação |
| --- | --- |
| 0 | Cotado |
| 1 | Fornecedor não Fornece o Produto |
| 2 | Não Cotado |
| 4 | Desqualificado |
| 5 | Indisponível |

Constantes do Produto - Tabela TPRODUTO

* **Tipo de Produto**

Na tabela de Produtos indica o tipo de produto cadastrado.

| Status | Representação |
| --- | --- |
| P | Produto |
| S | Serviço |

Constantes do XML de Entrada - Tabela TNFEENTRADA

* **Tipo de Status**

Na tabela de TNFEENTRADA indica STATUS do XML Importado.

| Status | Referência | Observação |
| --- | --- | --- |
| P | Pendente | Para os arquivos cadastrados e que ainda não foram  validados. |
| V | Validado | Para os arquivos cuja validação da SEFAZ está correta. |
| I | Inconsistente | Para os arquivos que por algum motivo ocorreram erros na transação, devendo ser ajustados e importados novamente. |
| R | Rejeitado | Para os arquivos cuja autenticidade não foi validada junto a SEFAZ. |
| F | Filial Pendente | Quando não há informação de filial ou do cliente/fornecedor no xml. |
| C | Cancelado | Para os arquivos cujo status é cancelado. |

Constantes da parametrização Aprovação Workflow (Fluig) - Tabela TITMMOVWFLUIG

* **Tipo de Aprovação - campo: TIPOAPROVACAOFLUIG**

| Status | Representação |
| --- | --- |
| 0 | Não Utiliza |
| 1 | Utiliza no Faturamento |
| 2 | Utiliza na Cotação |
| 3 | Utiliza em Ambos |

**Máscaras**

As Máscaras são utilizadas para formatar campos de códigos do sistema, como por exemplo: código do produto, número de série, fabricante e etc. As seguintes constantes podem ser utilizados na definição de uma máscara no sistema:

| Status | Representação |
| --- | --- |
| # | Somente números |
| I | Somente letras, converte para minúsculas as letras informadas |
| L | Somente letras, converte para maiúsculas as letras informadas |
| a | Letras e números, converte para minúsculo quando for letras |
| A | Letras e números, converte para maiúsculas quando for letras |
| Q | Qualquer caractere, exceto os separadores: dois pontos, ponto, vírgula, traço e barra. |

***Observação**:* Ponto (.) usado para definir níveis da máscara.
