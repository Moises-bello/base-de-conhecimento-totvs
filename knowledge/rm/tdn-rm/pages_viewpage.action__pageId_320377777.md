---
content_hash: f55800ccd262cf7364bd00cd90eb6f03f09d329e81ba7e1c0359305a0d999411
fetched_at: '2026-06-29T00:08:47.830064+00:00'
page_id: '320377777'
product: rm
source: tdn-rm
title: 1276717 MATESTCNTFTOF01-661 DT Vincular Contrato com Solicitação de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320377777
version: 42
---

# VÍNCULO DE CONTRATO / MELHORIAS INTEGRAÇÃO COM SIGAMNT

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Vínculo de Contrato | CtrVincularContratoSolMntProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimentos | MovMovimentoAction | | Contratos | CtrCntAction | | Cancelar Movimento | MovCancelMovProcAction | | Estornar Item não Recebido | MovEstornoItemFatParcAction | | | |
| **Ticket:** | 1276717 | | |
| **Requisito (ISSUE):** | MATESTCNTFTOF01-661 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

Criação de funcionalidade para vinculação de contrato do TOTVS Gestão de Estoque, Compras e Faturamento à Ordem de Manutenção (OS) gerada pelo TOTVS Manutenção de Ativos (SIGAMNT), permitindo assim uma maior rastreabilidade dos movimentos e dos contratos de manutenção envolvidos.

## Definição da Regra de Negócio

Uma vez criada a Ordem de Manutenção (OS) no Manutenção de Ativos, juntamente com ela é criada uma Solicitação de Armazém (SA) ou uma Solicitação de Compra (SC). Caso exista um contrato com um fornecedor para prestação de serviço ou fornecimento de produtos referente aos itens da SA/SC, pode existir a necessidade de vinculação desse contrato com a SA/SC.

Para que esse vínculo seja feito, será criado um processo no Módulo de Contratos que permitirá ao usuário fazer esse vínculo.

O processo irá verificar os itens dos movimentos de SA/SC que estiverem **Pendentes** ou **Parcialmente Faturados** e que não estejam participando de um processo de **Cotação**para que o usuário faça o vínculo do item de solicitação com o item de contrato. É importante ressaltar que o movimento de SA/SC não pode estar parametrizado para trabalhar com **Faturamento Parcial por Valor.**

Após o vínculo, os itens da SA/SC que foram vinculados não ficarão mais disponíveis para faturamento, evitando assim que os itens já vinculados sejam faturados pelo processo de compra ou baixa de estoque. Ao gerar o faturamento do contrato o item vinculado será recebido e o movimento gerado pelo contrato poderá seguir com o processo normal de faturamento, até a geração da NF e a criação do movimento de baixa, através de cópia por referência, assim como é feito atualmente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de Integração | Envolvida | [Integração -> Mensagem Única -> Integrações -> Anexos Parâmetros de Integração ] | - |
| Movimentos | Envolvida | [Gestão de Estoque, Compras e Faturamento -> Estoque -> Requisição de Materiais] | - |
| Vínculo de Contrato com Solicitação de Manutenção | Criação | [Gestão de Estoque, Compras e Faturamento -> Contratos -> Manutenção de Contratos] | - |

Para atender a esta demanda foi necessário realizar a seguinte implementação:

**Vínculo de Itens de Contrato x Itens de Solicitação**

* Criado uma nova tabela de relacionamento entre o item de contrato e o item de movimento (TITMCNTMOV) para que seja gravado o vínculo.
* Criado um novo campo (STSCONTRATO) na TMOV para gravar o Status de Mov. Relacionado ao Contrato.
* O Status de Mov. Relacionado ao Contrato poderá assumir os seguintes valores:
  + "C" - Em Contrato
  + "P" - Faturado Parcialmente pelo Contrato
  + "T" - Faturado pelo Contrato
  + "G" - Gerado pelo Contrato (Esse status somente será visualizado no movimento de faturamento gerado pelo contrato)
  + "   " - Vazio
* Criado um novo processo, onde o usuário precisará executá-lo para fazer o vínculo com os itens de solicitação. 
  + Criado uma nova tag de segurança para este processo;
  + Este processo estará disponível na visão de Manutenção de Contratos;
  + O processo será exibido quando a integração TOTVS Manutenção de Ativos x BackOffice RM estiver ativa e o usuário possuir permissão para executar o processo.
* O processo irá apresentar ao usuário todos os itens de movimentos de SA/SC Pendentes ou Parcialmente Faturados (TMOV.STATUS IN ('A', 'G')) e que estejam associados a um item de OS gerada pelo Manutenção de Ativos (TITMMOV.INTEGRAAPLICACAO = 'N'). Ao recuperar os itens de movimentos deve-se considerar o tipo de movimento integrado ao SigaMNT (TTMVEXT.INTEGRASIGAMNT = 1 ) e que esteja definido nos parâmetros de integração (TMVSA e TMVSC).
  + Para melhorar a performance do processo, será listado somente os itens de solicitação que sejam iguais aos itens de contrato selecionados.
* Será verificado se o tipo de movimento parametrizado na integração TOTVS Manutenção de Ativos x BackOffice RM está definido por coligada. Caso esteja, será considerado o tipo de movimento da coligada, senão será considerado o da coligada 0 (zero).
* No término da execução do processo:
  + Deverá ser criado um registro na tabela TITMCNTMOV, preenchendo os seguintes campos:
    - CODCOLCNT: Coligada do Contrato;
    - CODCOLMOV: Coligada de Movimento da Solicitação;
    - IDCNT: Identificador do Contrato;
    - IDMOV: Identificador de Movimento da Solicitação;
    - IDSEQUENCIAL: Sequencial do Vínculo;
    - NSEQITMCNT: Número Sequencial do Item de Contrato;
    - NSEQITMMOV: Número Sequencial do Item de Solicitação;
    - QUANTIDADEORIGINAL: Quantidade Original Vinculada;
    - QUANTIDADE: Quantidade Vinculada. (Esta será atualizada sempre que um faturamento for realizado)
  + A Quantidade será convertida para a mesma unidade do Item de Solicitação, desde que a unidade do contrato e da solicitação tenham a mesma unidade base.
  + O movimento de solicitação (SA/SC) deve ter o seu Status de Mov. Relacionado ao Contrato alterado para "Em Contrato".
* Na mesma tela de processo será permitido cancelar o vínculo realizado (desvincular) e o movimento de solicitação (SA/SC) deve ter o seu Status de Mov. Relacionado ao Contrato alterado para nulo. O cancelamento do vínculo será permitido somente se não existir faturamento do item de contrato.

****Edição do Item do Contrato****

Não há nenhuma restrição para a edição do item de contrato, exceto para os campos **Produto** e **Unidade**, onde não será possível a sua alteração caso já tenha sido realizado algum vínculo.

Foi criado também uma nova aba na edição do item de contrato para que o usuário possa visualizar as vinculações existentes. Esta aba estará disponível em **Informações Adicionais** do item de contrato e **somente será apresentada se existir vinculações para o item**.

**Exclusão de Item do Contrato**

Não será permitido excluir os itens de contrato vinculados aos itens de solicitação da SA/SC.

**Cancelamento do Contrato**

Ao efetuar o cancelamento de um contrato que possui itens de contrato vinculados com itens de solicitação de manutenção, não será feita alteração no status do movimento de origem. Isso acontece pois o contrato pode ser “descancelado” e essa característica dificulta o tratamento do movimento de origem.

**Rastreabilidade do Movimento**

O rastreamento de movimento foi configurado para apresentar o contrato que está vinculado com os itens de um determinado movimento. O vínculo será apresentado na **aba Contrato** da **rastreabilidade de movimento**.

Como esta mesma aba é utilizada para apresentar os Contratos que foram gerados por um movimento de Ordem de Compra, foi criado uma nova coluna que irá identificar a **Origem** desse rastreamento, podendo ser **Ordem de Compra** ou **Vínculo Integração SigaMNT**.

**Tabelas Utilizadas**

* TMOV - Movimentos.
* TITMMOV - Itens de Movimento.
* TITMCNT – Cadastro de Itens de Contrato.
* TITMCNTMOV - Vínculo de Itens de Contrato x Itens de Solicitação.
* TITMCNTMOVGERADO - Quantidade Gerada do Item de Contrato.
* TMOVRELAC - Relacionamento entre Movimentos.
* TITMMOVRELAC - Relacionamentos entre Itens de Movimento.
* HCPARAMETROS - Parâmetros do RM Conector.
* HCINTEGRACAOID - Tabela de-para dos identificadores de cada integração.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch 12.1.20.23 ou posterior.

## Procedimento para Utilização

1. Acessar o TOTVS Gestão de Estoque, Compras e Faturamento | Contratos | Manutenção de Contrato | Filtrar o(s) contrato(s) a ser(em) selecionado(s) para vinculação.
2. Selecionar o(s) contrato(s) | Processos | Vincular Contrato com Solicitação de Manutenção | A tela abaixo será aberta:  
     
     
     
   2.1. Para realizar o vínculo, é necessário selecionar o Item de Contrato e o Item de Solicitação correspondente, indicado pelas respectivas setas na figura acima.  
   2.2. Para realizar o desvinculo ou reverter um desvinculo feito, é necessário selecionar um registro de "**Vínculo de Itens de Contrato x Itens de Solicitação**".  
   2.3. O botão para Executar o processo somente será habilitado após existir pelo menos um vínculo ou desvinculo a ser realizado no processo.
3. Após selecionado os itens que serão vinculados, é necessário clicar no botão **Vincular**. Após vincular, será gerado uma nova linha na visão de **Vínculo de Itens de Contrato x Itens de Solicitação**.  
     
     
     
   3.1. Durante a vinculação, a visão de **Vínculo de Itens de Contrato x Itens de Solicitação** irá listar todos os vínculos já realizados e gravados na base de dados e os novos vínculos.  
   3.2. Sendo assim, para um novo vínculo, se o processo não for executado, o vínculo não será efetivado e gravado na base de dados. O mesmo vale para o desvinculo, só é efetivado e gravado após o processo ser executado.  
   3.3. Veja também, que ao realizar o vínculo ou o desvinculo a coluna **Saldo** do Item de Contrato e a coluna **Quantidade** do Item de Solicitação é atualizada para que o usuário possa visualizar os Saldos para o vínculo.  
   3.4. Não será possível realizar vínculos cujo o **Saldo** e/ou a **Quantidade** estejam zerados.  
   3.5. Não será possível realizar vínculos de produtos diferentes.  
   3.6. Não será possível realizar desvinculo se a quantidade do vínculo for zero, já foi completamente faturada pelo contrato.  
   3.7. O desvinculo de um vínculo não processado e simplesmente removido, **Saldo** do item de Contrato e a coluna **Quantidade** do item de Solicitação são atualizadas com a devolução do valor que estava vinculado.  
   3.8. O desvínculo de um vínculo já processado deixa a quantidade do mesmo negativa, **Saldo** do item de Contrato e a coluna **Quantidade** do item de Solicitação são atualizadas com a devolução do valor que estava vinculado. A quantidade devolvida pode ser utilizada em novos vínculos.  
   3.9 Ao realizar o desvinculo de um vínculo onde nenhuma quantidade foi faturada, esse é completamente removido da tabela de vinculações. Se for parcialmente faturada, ao invés de remover o vínculo, a quantidade é zerada.
4. Clicar em **Executar** para efetivar o vínculo ou desvinculo a ser realizado.  
     
     
     
   4.1. Se não houver nenhuma inconsistência, o vínculo\desvinculo será realizado com sucesso e um Log completo com as informações para cada item será apresentado.
5. Acessar o Tipo de Movimento de SA/SC | Verificar que o **Status de Mov. Relacionado ao Contrato** foi alterado para **Em Contrato**.  
   Também poderia ter o status removido no caso de um desvinculo total.   
     
     
     
   5.1. Enquanto o **Status de Mov. Relacionado ao Contrato**estiver **Em Contrato** não será possível:  
      5.1.1. Realizar o Cancelamento do Movimento.   
      5.1.2. Faturar/Receber o Movimento.  
      5.1.3. Concluir Pedido.  
      5.1.4. Estornar Item não Recebido.  
      5.1.5. Editar/Excluir o Item de Solicitação vinculado ao Contrato.
6. Sempre que o processo de Vincular Contrato com Solicitação de Manutenção for acessado, o sistema irá listar os vínculos já realizados de todos os Itens de Contrato selecionados na visão.

## Faturamento do Contrato

Ao efetuar o faturamento de um item de contrato (periódico ou não periódico) ou de uma medição do item de contrato, o sistema irá verificar se o item possui vínculo, e no caso afirmativo, irá realizar o faturamento da solicitação vinculada no processo, considerando a quantidade do item de contrato (periódico ou não periódico) ou a quantidade da medição, para faturar a solicitação de acordo com a quantidade vinculada.

Para ficar claro o comportamento explicado acima, vamos à um exemplo prático.

1. Realizada duas operações de vinculação do item de contrato para a mesma solicitação. Inicialmente, tinha-se Quantidade = 9 no item de contrato, e foi realizado o vínculo dessa quantidade com a solicitação. Depois viu-se a necessidade de realizar mais uma operação de vínculo, aumentando a quantidade no item de contrato para atender por completo a solicitação.
2. O Item de Contrato em questão é de Medição. Com isso, foi criada uma medição com Quantidade = 1.
3. Selecionada a Medição e realizado o faturamento.  
     
     
     
   3.1 Uma vez que o faturamento foi realizado com sucesso, o sistema deverá ter os seguintes comportamentos:  
       3.1 A solicitação deverá ser faturada de acordo com a quantidade vinculada, tendo o seu **Status de Mov. Relacionado ao Contrato** atualizado de acordo com o faturamento realizado.  
       3.2 A tabela de vínculo (TITMCNTMOV) deverá ter o campo QUANTIDADE atualizado, consumindo o valor faturado. O consumo da quantidade será do registro que tiver o menor IDSEQUENCIAL na tabela, para maior.  
       3.3 Deverá ser criado o(s) registro(s) na tabela de Quantidade Gerada do Item de Contrato (TITMCNTMOVGERADO), com a Quantidade Gerada do faturamento realizado, de acordo com a quantidade vinculada.
4. Ao verificar o movimento de solicitação, podemos observar que nesse cenário, esse foi **Parc. Recebido** e o Status de Mov. Relacionado ao Contrato alterado para **Faturado Parcialmente pelo Contrato**.
5. Acessando a **Rastreabilidade do Movimento**, verificamos que o relacionamento com o movimento gerado pelo contrato foi efetivado.

## Observações

1. Para faturar a solicitação de SA/SC é necessário que tenha vínculo registrado, do contrário, o faturamento do item de contrato seguirá como é atualmente, ou seja, sem relacionamento.
2. No que diz respeito a quantidade a ser faturada, será considerada toda a quantidade do vínculo, até que este seja zerado. Caso seja realizado o faturamento de um item de contrato, cujo o seu vínculo esteja zerado, o sistema irá gerar movimento normalmente, mas sem relacionamento.

## Estornar Item não Recebido Vinculado ao Contrato

Ao realizar o processo de estorno de item não recebido de faturamento cujo status seja igual a "Gerado pelo Contrato", o sistema irá exibir uma mensagem de consistência informando que o movimento selecionado não possui item para ser estornado. Neste caso, apenas o cancelamento é permitido.

Segue abaixo imagem do processo de Estorno:

## Cancelamento de Movimento Vinculado ao Contrato

Ao realizar o processo de Cancelamento de faturamento cujo status seja igual a "Gerado pelo Contrato", o mesmo será processo processado normalmente e ainda irá atualizar o movimento de solicitação de acordo com os valores cancelados.

Movimento de Solicitação:

Vinculo entre os movimentos e o contrato:

Processo de cancelamento:

Movimento cancelado:

Solicitação com status atualizado:

## Observações

1. Uma vez que o cancelamento foi realizado com sucesso, o sistema deverá ter os seguintes comportamentos:
   1. O item da solicitação deverá ter sua quantidade estornada de acordo com o que foi faturado;
   2. A solicitação deverá ter o seu **Status** e **Status de Mov. Relacionado ao Contrato** atualizado de acordo com o cancelamento realizado.
   3. A tabela de vínculo (TITMCNTMOV) deverá ter o campo QUANTIDADE atualizado, estornando-se o valor faturado.
   4. A tabela de Quantidade Gerada do Item de Contrato (TITMCNTMOVGERADO) deverá ser atualizada ou apagada, de acordo com a quantidade que está sendo estornada.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

**Cadastro de Perfis**

1. No **RM.exe** acesse o Módulo de **Serviços Globais | Segurança | Perfis**
2. Selecione o sistema **Gestão de Estoque, Compras e Faturamento**:
3. Edite o **perfil do usuário** que será concedida a permissão para executar o processo | Acesso a Menus | 05 - Contratos | 05.01 - Gestão de Contratos | 05.01.07 Manutenção de Contratos | **05.01.07.14 Vincular Contrato com Solicitação de Manutenção**:

****Integração com Protheus****

1. No ****RM.exe****acesse o **Módulo de Integração | Mensagem Única | Integrações**
2. Edite a integração **Manutenção de Ativos x BackOffice RM** e verifique se a mesma se encontra **Ativa**:

### Fluxo do Processo
