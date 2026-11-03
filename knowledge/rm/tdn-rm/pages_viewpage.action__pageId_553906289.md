---
content_hash: 1365417a33db777b94ec990a30884a3097a7843e6a637a699639e582d6221121
fetched_at: '2026-06-29T00:10:46.114925+00:00'
page_id: '553906289'
product: rm
source: tdn-rm
title: Cobrança Terceirizada e Negativação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553906289
version: 202
---

A terceirização de cobrança é uma estratégia eficaz para garantir que a empresa receba os valores devidos, reduzindo a inadimplência e melhorando o fluxo de caixa. Isso é crucial para a saúde financeira da empresa, pois garante a liquidez necessária para cumprir com suas obrigações e investir no crescimento.

Nosso sistema integra com o **SPC Brasil** para **cobrança terceirizada e negativação.**

No menu Contas a Pagar/Receber | Cobrança Terceirizada foram disponibilizadas opções para cadastro e execução dos processos de Cobrança Terceirizada e Negativação.

Importante

Atendemos ao layout SPC Brasil versão 13.0, tanto para o serviço de Terceirização de Cobrança quanto para o de Negativação.

Para qualquer empresa que seguir este layout, será possível a integração de forma nativa.

Para dar início ao uso das funcionalidade de terceirização ou negativação, será preciso primeiramente cadastrar alguns dados.

Modelo de Negativação/Terceirização

Neste menu será definido qual modelo um determinado contrato irá seguir. Um modelo de contrato poderá ser usado para um ou para vários contratos de serviços. Este cadastro será utilizado tanto na negativação quanto na cobrança terceirizada.

Ex.: Modelo de Negativação SPC Brasil, Modelo de terceirização do escritório de advocacia XXXXX.

ModeloNegativaçãoAba\_identificacaoIdentificação

Modelo: Código sequencial do modelo de contrato, que será gerado pelo sistema.

Descrição: Descrição do modelo de contrato, campo livre conforme exemplo acima.

Aba\_negativacaoterceirizacaoNegativação/Terceirização

Neste local serão cadastrados dados importantes para que no momento da importação do arquivo de retorno o sistema identifique as posições corretas do arquivo e execute o processamento do retorno.

Exemplo:

Aba\_negociacaoNegociação

Nas abas internas "Header", "Corpo" e "Detalhe" serão preenchidos os respectivos campos, conforme a definição do layout correspondente à negociação.

Exemplo:

  

Aba\_pagamentoPagamento

Nas abas internas "Header" e "Detalhe" serão preenchidos os respectivos campos, conforme a definição do layout correspondente ao pagamento da cobrança terceirizada.

Exemplo:

 

Aba\_ocorrenciasretornoOcorrência de Retorno

Neste anexo serão inseridos os códigos de ocorrência para o processamento do retorno, podendo ser sucesso ou erro. Os códigos de ocorrência deverão obedecer ao manual de Negativação / Terceirização do SPC Brasil.

Id. Modelo: Código do modelo do qual a ocorrência faz parte.

Código da ocorrência: Código da ocorrência, encontrado no manual de layout de Negativação/Terceirização.

Descrição: Descrição da ocorrência, encontrada no manual de layout de Negativação/Terceirização.

|  |  |
| --- | --- |
| Código de Erro | Descrição |
| 00 | Operação bem-sucedida |
| 01 | Tipo de Registro inválido |
| 02 | Operação inválida |
| 03 | Data movimento inválida |
| 04 | Número remessa inválida |
| 05 | Entidade destino inválida |
| 06 | Código de destino inválido/associado |
| 07 | Sequencial do registro inválido |
| 08 | Praça de Concessão Não Informada/Inválida |
| 09 | Nome não informado |
| 10 | Nome inválido |
| 11 | Tipo de documento inválido |
| 12 | CPF/CNPJ inválido |
| 13 | RG inválida |
| 14 | Data nascimento inválida |
| 15 | Registro para menor de idade |
| 16 | Filiação inválida |
| 17 | Endereço inválido |
| 18 | Número endereço inválido |
| 19 | Complemento endereço inválido |
| 20 | Bairro inválido |
| 21 | CEP inválido |
| 22 | Cidade inválida |
| 23 | Uf inválida |
| 24 | DDD inválido |
| 25 | Telefone inválido |
| 26 | Comprador ou fiador deve ser C ou F |
| 27 | Data vencimento inválida |
| 28 | Data vencimento não informada |
| 29 | Data vencimento maior ou igual data atual |
| 30 | Contrato inválido |
| 31 | Contrato não informado |
| 32 | Valor debito inválido |
| 33 | Valor debito não informado |
| 34 | Data emissão do cheque inválida |
| 35 | Banco inválido |
| 36 | Agencia inválida |
| 37 | Número cheque inicial inválido |
| 38 | Número cheque final inválido |
| 39 | Alínea inválida |
| 40 | Valor cheque inválido |
| 41 | Registro já cadastrado anteriormente |
| 42 | Cancelado anteriormente |
| 43 | Total de registro inconsistente |
| 44 | Cheque não existe para exclusão |
| 45 | Cheque já existe no cadastro |
| 46 | Código de operação diferente de I ou E |
| 47 | Registro não encontrado para cancelar |
| 99 | Erro não previsto no processamento (Entrar em contato com a entidade) |
| 48 | Consumidor não encontrado |
| 49 | Data vencimento prescrita para cheque |
| 50 | Digito do cheque inicial não confere |
| 51 | Digito do cheque final não confere |
| 52 | Data vencimento prescrita para SPC |
| 53 | Data da compra inválida |
| 54 | Garantidor sem Tomador (Comprador) |
| 55 | Contrato não informado |
| 56 | Tentativa Incorreta de Baixa do Garantidor |
| 57 | Motivo da Liquidação/Baixa inválida |
| 58 | Natureza da Inclusão inválida |
| 60 | Impedimento por ordem judicial |
| 61 | Tamanho de linha inválido |
| 62 | Tentativa de incluir um registro antes de certo prazo determinado. A mensagem para esse erro é "registro somente poderá ser incluído após 'n' dias" |
| 63 | Número de conta corrente inválido |
| 64 | Nome divergente do que consta na Receita Federal. |
| 65 | Base externa inoperante |
| 98 | Erro de negócio. Indica qualquer erro - geralmente em validações - que não se encaixa nos códigos existentes e que não seja erro interno do sistema (99) |

Contrato de Serviço

Neste menu serão inseridas informações do contrato firmado e dados importantes que posteriormente serão usados no processo de Negativação/Terceirização, através da geração da remessa. Este cadastro será utilizado tanto na negativação quanto na cobrança terceirizada e também no processo de negociação.

Contrato ServiçoAba\_IdentificacaoIdentificação

Id. Contrato: Será gerado pelo sistema uma numeração em sequência a cada inclusão no cadastro.

Número do Contrato: Indica o número do contrato estipulado com a empresa do serviço de negativação/terceirização. Deve ser informado igual ao valor que consta no arquivo enviado pela empresa terceirizada. O código do contrato no contexto do SPC/Brasil é numérico, e deverá ser preenchido no cadastro com 8 dígitos (ex: 1234 → 00001234).

Entidade: Esse campo é alfanumérico e o código informado será usado no layout de remessa para identificação no processamento.

Tipo Contrato: Indica o tipo de contrato que a empresa irá trabalhar, com as opções "Negativação" ou "Terceirização".

Negativar: Esse campo só ficará habilitado quando o tipo de contrato selecionado for "Terceirização". Assim, borderôs com esse contrato de Terceirização poderão ser negativados e terceirizados.

Modelo de Negativação/Terceirização: Define qual modelo o contrato irá seguir.

Descrição: Descrição do contrato de serviço. Campo de preenchimento livre.

Cliente/Fornecedor: Define se esse contrato está atrelado a um fornecedor. Campo não obrigatório.

Aba\_remessaRemessa

Layout Remessa: Layout do Gerador de Saídas usado para geração da remessa de negativação/terceirização (inclusão ou exclusão). O layout "FINLAY0061 - Layout SPC BRASIL" pode ser obtido através do recurso "[TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027244414-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-realizar-o-download-de-Layout-do-gerador-de-sa%C3%ADdas-e-relat%C3%B3rios-Reports-padr%C3%A3o-do-book-do-sistema)". 

Diretório destino no FileServerPath: Diretório no servidor configurado no FileServerPath, onde serão gravados os arquivos gerados na execução do processo de remessa. O campo não é editável e preenchido automaticamente. Deve ter o seguinte formato: "CobrancaTerceirizada\NUMEROCONTRATO", sendo esta última parte substituída pelo número do contrato informado.

Mais informações em .

Nome do arquivo: Nome do arquivo a ser gerado pela remessa. Pode ser composto de uma parte fixa e uma parte variável.

Na parte variável pode ser usado:

*#* : caractere para definir o número sequencial da remessa, com zero a esquerda  
*ddMM, MMyyyy, ddMMyyyy, yyyyMMdd ou MMddyyyy* : informação da data de geração da remessa (observar as letras maiúsculas e minúsculas)  
*HHmm, mmss, ou HHmmss* : informação de hora da geração da remessa.

Extensão: Nesse campo está disponível dois tipos de extensão de arquivo que poderá ser .txt ou .rem.

Tipo da Comissão: Tipo de comissão cobrada pela empresa contratada para o processo de negativação ou cobrança terceirizada:

* Sem comissão: o contrato não tem controle de comissão.
* Valor: o controle da comissão é por valor para cada "transação" de negativação/terceirização. Neste caso, informar no campo "Valor da Comissão" qual o valor usado.
* Percentual: o controle da comissão é por um percentual aplicado sobre o valor da "transação" de negativação/terceirização. Neste caso, informar no campo "Valor da Comissão" qual o percentual usado.

Valor da Comissão: Valor ou percentual da comissão de acordo com o tipo selecionado.

Observação: Na execução do processo de remessa, os campos de comissão serão armazenados no borderô de negativação/terceirização, para manter o histórico de quais eram as condições da comissão no momento, já que, no contrato, os valores podem sofrer alterações.

Valor mínimo: Define o valor mínimo que o lançamento deve ter para que possa ser enviado para terceirização, visando minimizar gastos com o serviço com lançamentos de valores baixos a receber. Na geração do borderô, é feita a validação dos lançamentos selecionados pelo cálculo do valor líquido, utilizando como data de referência a data de cálculo informada na tela. Caso algum lançamento seja menor que o valor mínimo, ele é retirado do borderô sem abortar o processo. Serão apresentados no log os lançamentos que forem retirados.

Aba\_negociacaoNegociação

Template de Acordo: Nesse campo será informado o cadastro do Template de Acordo a ser utilizado no retorno da negociação. Serão exibidos somente os cadastros cujo tipo de efetivação seja 'Ao criar'. Não será permitida a alteração do tipo da efetivação e da aprovação caso o Template de Acordo esteja associado a algum contrato de serviço.

Aba\_pagamentoPagamento

Conta/Caixa: Código da conta/caixa que será utilizada na baixa dos lançamentos financeiros envolvidos.

Meio de Pagamento: Meio de pagamento que será utilizado na transação.

Valor de Integração para Juros: Valor de integração, cujo campo 'Ação' esteja definido como "Acrescenta", para tratar o valor dos juros.

Valor de Integração para Desconto: Valor de integração, cujo campo 'Ação' esteja definido como "Desconta", para tratar o valor de desconto.

Valor de Integração para Comissão: Valor de integração, cujo campo 'Ação' esteja definido como "Nada", para tratar o valor pertinente à comissão.

Valor de Integração para Tarifa: Valor de integração, cujo campo 'Ação' esteja definido como "Nada", para tratar o valor pertinente à tarifa.

Observação: os valores de integração irão compor os valores da baixa e são independente dos outros campos de valor já existentes.

Isenção de Terceirização e/ou Negativação de Cliente

Para os processos de Negativação e Terceirização, é possível controlar clientes isentos de cobrança terceirizada, onde os lançamentos de determinado Cliente isento num período não serão enviados para a empresa de cobrança e/ou negativação.

O controle será na filtragem dos lançamentos ao incluir um borderô de remessa. Caso o cliente esteja com isenção num determinado período (anexo “Isenção de Cobrança Terceirizada”) que abranja o vencimento do lançamento financeiro, ele não será considerado na geração do borderô de inclusão de Terceirização e/ou Negativação.

O motivo de isenção poderá ser inserido manualmente através do menu Cobrança Terceirizada | Mais | Motivo de Isenção.

Motivo de Isenção

Neste anexo serão inseridos os motivos de isenção que serão usados na inclusão de borderô tanto de negativação quanto de terceirização. O cadastramento dos motivos será manual e deverá seguir as instruções do manual da empresa terceirizada. Os campos pertinentes ao código e descrição do motivo da exclusão são de preenchimento obrigatório.

Código do Motivo: Código de identificação do Motivo, campo numérico que não permite repetição.

Descrição: Descrição do motivo da exclusão que deverá seguir o manual do SPC Brasil.

Cadastros previamente realizados, podemos dar início a criação e envio do borderô.

Inclusão de Borderô (Negativação/Terceirização)

A tela do processo de inclusão de borderô de negativação/terceirização tem como finalidade permitir que o usuário defina as condições em que deseja incluir ou excluir determinados lançamentos em uma negativação/terceirização, utilizando os recursos da tela de filtro padrão. Os lançamentos filtrados irão compor o borderô de negativação/terceirização.

Na sua interface estarão disponíveis as principais informações para identificação e conhecimento dos dados principais dos borderôs, bem como as informações da remessa em que o mesmo participou.

* Identificador do contrato a que o borderô foi vinculado;
* Tipo de Operação, podendo ser inclusão e exclusão da negativação/terceirização;
* Borderô para inclusão
  + Tem como objetivo a possibilidade de incluir lançamentos a borderôs existentes. Só serão listados borderôs com status de remessa pendente.
  + Os lançamentos serão adicionados ao borderô selecionado, mantendo os que já estavam nele.
  + Caso esse parâmetro não seja preenchido, então os lançamentos serão adicionados a um novo borderô.
  + Caso seja necessário excluir algum lançamentos do borderô, utilizar o processo "Remover lançamentos do borderô" na tela de "Borderô Negativação/Terceirização" | anexo "Lançamentos".
* Tipo de agrupamento utilizado, podendo ser 'Não Agrupar', 'Cliente/Responsável Financeiro' ou 'Responsável Financeiro e Aluno'.
* Descrição do borderô
* Data de Cálculo: data utilizada para o cálculo do valor líquido dos lançamentos.

Operações

**Inclusão**- Define que os lançamentos vinculados ao borderô de negativação/terceirização serão inseridos na cobrança terceirizada. Por padrão, será aplicado internamente o filtro somente para os lançamentos a receber que estejam vencidos, em aberto ou parcialmente baixados, e que o status de negativação/terceirização (cada status para o seu respectivo borderô) esteja como 'Não Remetido', 'Recusado' ou 'Devolvido'. Na filtragem, poderão ser selecionadas informações acadêmicas, como curso, período letivo, aluno, dentre outras.

 

**Exclusão** - Define os lançamentos inseridos no borderô de negativação/terceirização que serão removidos da cobrança terceirizada. Por padrão, será aplicado internamente o filtro somente para os lançamentos a receber da coligada corrente, vencidos e com o Status de Terceirização como 'Confirmado' ou 'Retirar Terceirização'/'Retirar Negativação'. Na filtragem, poderão ser selecionadas informações acadêmicas, como curso, período letivo, aluno, dentre outras.

 

Nessa interface não há a possibilidade de excluir lançamentos que por ventura foram selecionados e não serão remetidos, mas será possível visualizar aqueles retornados pelo filtro.

Os lançamentos retornados pelo filtro serão apresentados em forma de grid, onde haverá um campo para informar o "Motivo de Exclusão" individualmente para cada item, que será alterado pontualmente. Para mais itens será possível "Atualizar o motivo da exclusão" através do atalho, onde o mesmo motivo será aplicado para todos os itens selecionados.

Contrato Serviço: É o contrato de serviço a que o borderô irá pertencer.

Descrição: Campo livre para usuário definir uma descrição para o borderô a ser incluído.

Motivo de Exclusão: Os motivos estão cadastrados no sistema e estão de acordo com o layout padrão da SPC Brasil.

Filtro genérico: Tela de filtro padrão baseada nos campos de lançamentos, onde o usuário, através das condições, irá localizar os lançamentos que irão compor o borderô.

Obs: No retorno de borderô de exclusão, o processo irá alterar o status do lançamento para 'Não Remetido'.

Observações:

* A permissão de acesso ao menu e as opções de processamento do serviço de cobrança terceirizada terá acesso concedido no perfil associado ao usuário do sistema.
* Após passar por todas as validações, o borderô será salvo com status 'Pendente'. Os lançamentos financeiros vinculados ao borderô terão o campo 'Status de Terceirização' atualizado para 'Em Borderô'.
* Lançamentos que após o cálculo do valor líquido (utilizando a data de cálculo informada como data de referência) não atingirem o valor mínimo cadastrado no contrato de serviço, serão retirados do borderô sem abortar o processo. Os mesmos serão informados no log após o processo ser finalizado.
Exclusão de lançamento em borderô (Negativação/Terceirização)

**Exclusão de lançamento em borderô de cobrança Terceirizada (Negativação/Terceirização)**

Lançamentos vinculados a borderô de cobrança terceirizada poderão ser desvinculados, respeitando o status de processamento do borderô. Quando o "Status da Remessa" do borderô for igual a "Pendente" o lançamento poderá ser removido do borderô. Caso todos os lançamentos sejam removidos do borderô, ele também será excluído. Somente lançamentos com status negativação ou status terceirização igual a "Em Borderô" ou "Não Remetido" poderão ser removidos do borderô. 

Para execução do processo de remoção de lançamento em borderô, o usuário deverá acessar a visão de "Borderô de Negativação/Terceirização", anexo "Lançamentos do Borderô" e através do menu de Processos selecionar a opção "Remover Lançamento do Borderô de Cobrança Terceirizada".

Caso o borderô tenha sido criado com o tipo de agrupamento 'Cliente/Responsável Financeiro' ou 'Responsável Financeiro e Aluno', o processo somente irá permitir a exclusão de um lançamento do borderô se a soma dos valores líquidos dos lançamentos que permanecerem respeitar o valor mínimo definido no contrato.

Remessa (Negativação/Terceirização)

O processo de geração de remessa de inclusão ou exclusão de títulos negativados/terceirizados será realizado através da visão geral de Borderô de Negativação/Terceirização, no menu Processos | Remessa de Borderô. Assim, para os borderôs  selecionados, a remessa de dados em forma de arquivo será gerada conforme layout definido no contrato, considerando o tipo do borderô, a operação e os lançamentos do borderô, e posteriormente, enviada à empresa contratada. Os campos da tela de execução da remessa já terão seus campos principais preenchidos de acordo com os cadastros selecionados na inclusão do borderô. Importante ressaltar que a tela de processamento da remessa de dados a partir da versão 12.1.2306 é comum aos processos de Negativação e Terceirização. O layout da remessa de cessão de títulos (Cobrança Terceirizada) é igual ao da negativação.

A partir da versão 12.1.2402 é possível editar o campo Sequencial da remessa, tanto para a Terceirização quanto para a Negativação. O usuário poderá informar um valor diferente do sugerido pela aplicação, desde que esse valor não esteja atribuído a um borderô com status diferente de pendente e seja maior que zero.

Edição do sequencial da Remessa na Negativação

Para que a atualização reflita na remessa do processo de Negativação, deve ser importada a versão atualizada do layout  "FINLAY0061 - Layout SPC BRASIL" que deve ser obtido através do recurso "[TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027244414-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-realizar-o-download-de-Layout-do-gerador-de-sa%C3%ADdas-e-relat%C3%B3rios-Reports-padr%C3%A3o-do-book-do-sistema)", caso contrário o comportamento atual de incrementar o último valor de sequência gerado será mantido.

O arquivo será gerado de acordo com o diretório configurado no contrato e também será possível realizar o *download* em ambiente local marcando a opção "Salvar arquivo local" e informando um diretório válido que deverá ter permissão para escrita (somente para processo não agendado). 

Caso ocorra algum erro na geração do arquivo, um LOG será apresentado ao usuário, que poderá ser gravado para posterior análise. Ao concluir a geração do arquivo com sucesso, o processo atualizará o status do borderô para “Remetido”, o ele não poderá ser alterado ou excluído. Os lançamentos do borderô terão o Status de Negativação/Terceirização alterados para "Remetido". Além disso, caso os campos de comissão estejam informados no cadastro do contrato, os valores serão armazenados no borderô remetido.

Reenvio do borderô  
O arquivo de remessa gerado para um determinado borderô poderá ser gerado novamente para o mesmo borderô, com as mesmas informações do seu registro. No processamento, será apresentada mensagem informando que o arquivo já foi gerado. Caberá ao cliente e à empresa controlar o envio/recebimento em duplicidade do arquivo de remessa.

Observações

O arquivo gerado para o modelo SPC Brasil deve ter o padrão ASCII.

O número de telefone do cliente/fornecedor deve estar no formato (31)9999-9999, 319999-9999 ou 3199999999 para garantir a geração correta dos campos.

Cancelamento de Remessa (Negativação/Terceirização)

O processo de cancelamento de remessa de títulos negativados/terceirizados será realizado através da visão geral de Borderô de Negativação/Terceirização, no menu Processos | Cancelamento da Remessa de Borderô. Assim, para os borderôs selecionados que tenha status como "Remetido", a remessa será desfeita:

* Atualização do status da remessa do borderô para "Pendente" além de limpar o campo sequencial;
* Atualização do status de negativação e/ou terceirização do lançamento para "Em borderô".

Informações específicas de cada processo

Cobrança e Negativaçãocobranca\_terceirizadaCobrança Terceirizada

O TOTVS Gestão Financeira desenvolveu processos específicos para gerenciar títulos enviados para Cobrança Terceirizada, atendendo ao layout do SPC Brasil versão 13.0, no que diz respeito à remessa e retorno para cessão de títulos.

Borderô

Ao filtrar lançamentos do Modulo Educacional, não será permitida a inclusão de lançamentos de alunos diferentes que estiverem agrupados em um mesmo boleto.

**Obs:** Caso seja necessário enviar esses lançamentos, deve ser cancelado o boleto que está agrupando os lançamentos de alunos diferentes. Gerar novos boletos, um para cada aluno, e incluir os lançamentos no borderô.

Retorno Terceirização

O sistema irá processar o arquivo de retorno enviado pela empresa terceirizada contratada ou mesmo o órgão de proteção ao crédito SPC Brasil e fará o tratamento dos dados recebido. Neste processo será informado o contrato cadastrado anteriormente e o arquivo de retorno enviado pela contratada. O arquivo contém informação da validação de um conjunto de remessas enviadas, cada uma com seu código de retorno que indicam a Confirmação do recebimento e/ou Recusa/Rejeição da Remessa enviada anteriormente.

Para os lançamentos financeiros recusados em função de algum erro, será gerado um arquivo de LOG com as inconsistências, e caso ocorra algum erro durante o processamento dos arquivos de retorno, um LOG será apresentado ao usuário, podendo ser gravado para posterior análise.

A coluna "Status de Terceirização" na visão de lançamentos será preenchida de acordo com as movimentações de remessa e retorno de dados. São elas:

0 - Não Remetido  
1 - Em Borderô  
2 - Remetido  
3 - Confirmado/Registrado  
4 - Recusado  
5 - Devolvido  
6 - Retirar Terceirização  
7 - Baixa Conforme Negociado  
8 - Desconto divergente  
9 - Cobrança Finalizada  
10 - Acordo Não Cumprido

A coluna "Status da Remessa"  na visão de Borderô de Negativação/Terceirização será preenchida de acordo com as movimentações de remessa e retorno de dados. São elas:

1 - Pendente  
2 - Remetido  
3 - Confirmado

**Observação:**

* No retorno de terceirização de borderô, caso o título seja recusado pelo SPC Brasil, o status da remessa do borderô será alterado para "Confirmado" e o status de terceirização do título será alterado para "Recusado/Rejeitado".
Retorno Negociação

Uma vez que os lançamentos financeiros foram enviados para cobrança terceirizada, quando houver uma negociação (acordo) entre esta entidade e o devedor, o detalhamento da negociação será devolvido para tratamento no sistema através de um arquivo no formato txt (com a codificação 'UTF-8'), que deverá ser importado através do processo de retorno de Negociação, disponível no menu Contas a Pagar/Receber | Cobrança Terceirizada | Retorno | Negociação, mediante liberação da tag de menu do cadastro do Perfil do usuário, destacada na imagem abaixo:

Este arquivo é gerado pela empresa de cobrança terceirizada num layout específico. O modelo que hoje está homologado é o definido pela SPC Brasil. Para usá-lo, é necessário primeiro solicitar este serviço à mesma.

Ao importar o arquivo de retorno pertinente à negociação, o sistema irá identificar os lançamentos financeiros originais enviados para a terceirizada através da remessa do borderô de terceirização, e submeter automaticamente a um acordo, gerando novos lançamentos. Desta forma, os termos do acordo executado externamente pela empresa de cobrança terceirizada estarão identificados no sistema, seguindo as regras do Template de Acordo configurado no Contrato de Serviço.

Caso necessário, o processo pode ser desfeito através do cancelamento do acordo desde que os lançamentos origem tenham o campo Status de Terceirização como "Baixa Conforme Negociação" e os lançamentos gerados não incluídos em novo borderô.

Retorno Pagamento

Quando houver a liquidação dos títulos, os dados relacionados ao pagamento serão retornados para tratamento no sistema, via importação de arquivo no formato txt. A importação deste arquivo será realizada através do processo de retorno de Pagamento, disponível no menu Contas a Pagar/Receber | Cobrança Terceirizada | Retorno | Pagamento, mediante liberação da tag de menu do cadastro do Perfil do usuário, destacada na imagem abaixo:

Ao importar o arquivo de retorno, o sistema irá identificar os lançamentos financeiros para serem baixados. No caso dos lançamentos gerados por acordo através da negociação da terceirizada junto ao Cliente devedor, tais registros também serão baixados.

Observação: para o correto funcionamento do processo é necessário a configuração do pagamento no modelo de contrato de terceirização.

Lançamentos

Lançamentos em cobrança terceirizada (títulos cedidos a terceiros) terão os principais campos bloqueados para edição e processamento para que assim se garanta a integridade dos dados enquanto o título está com cobrança sob responsabilidade de uma empresa terceira.

Não será possível executar os seguintes processos (o sistema fará o bloqueio da execução):

* Alteração de Lançamento
* Cancelamento de lançamento
* Parcelamento de lançamento
* Inclusão de fatura
* Geração de acordo
* Baixa manual de lançamentos

O campo "Status de Terceirização" é que será validado pelo sistema e não permitirá a execução dos processos listados acima, quando o status do(s) lançamento(s) for:

* Em borderô
* Remetido
* Confirmado/Registrado
* Acordo não Cumprido
* Baixa conforme negociado
* Desconto divergente
* Cobrança finalizada.

Observações:

* Para lançamento(s) vinculado(s) a cobrança terceirizada, o sistema só permitirá baixa (quitação do título) através do processo de importação do arquivo de retorno de pagamento.

* Para lançamentos que apenas compõem o Borderô de terceirização, o sistema permitirá que sejam baixados normalmente através das interfaces (processo de baixa manual) do TOTVS Gestão Financeira.

Os principais campos do lançamento serão bloqueados para edição e alteração após a execução do processo de terceirização. Os campos que ficarão bloqueados são:

* Pagar/Receber
* Cliente/Fornecedor
* Data de Vencimento
* Valor Original
* Juros/Multa/Desconto
* Capitalização
* Valores Adicionais
Histórico de Cobrança Terceirizada

Na visão de Lançamentos Financeiros, Cliente/Fornecedor e Contrato de Serviços está disponível o anexo "Histórico de Cobrança Terceirizada". Nele são armazenadas informações referentes aos processos da cobrança terceirizada (Negativação e Terceirização), quando os lançamentos forem incluídos a um borderô, remetidos e quando for importado o arquivo retorno, tanto para operações de inclusão quanto para exclusão. Esses registros são essenciais para identificação do processo a que o registro foi submetido.

No anexo serão apresentados os seguintes campos, referente a cada cadastro:

Lançamento

* Id. Histórico: Sequencial gerado pelo sistema
* Referência do lançamento: lançamento que participou do processo
* Operação (Tipo): Inclusão ou Exclusão
* Número Remessa/Retorno: sequencial da remessa/retorno
* Código da Ocorrência: para processo de retorno de remessa traz o código lido do arquivo
* Data Ocorrência: data em que o processo foi executado
* Status Negativação: Em borderô/Remetido/Confirmado/Recusado
* Status Terceirização: Em borderô/Remetido/Confirmado-Registrado/Recusado-Rejeitado
* Observação: no caso de retorno com erro, será armazenado nesse campo o motivo do retorno.
* Número do Contrato: número do contrato atrelado ao processo
* Tipo do Contrato: Negativação ou Terceirização
* Empresa de Cobrança: Modelo contrato
* Coligada do Cliente/Fornecedor
* Código do Cliente/Fornecedor
* Nome do Cliente/Fornecedor
* CPF/CNPJ do Cliente/Fornecedor

Cliente/Fornecedor

* Empresa de Cobrança (Modelo contrato)
* Número do Contrato
* Operação (Tipo): Negativação
* Código Operação: Inclusão / Exclusão
* Número Remessa/Retorno
* Código da Ocorrência
* Data Ocorrência
* Status Negativação
* Observação: no caso de retorno com erro, será armazenado nesse campo o motivo do retorno.

Contrato de Serviços

* Empresa de Cobrança (Modelo contrato)
negativacaoNegativação

O módulo TOTVS Gestão Financeira proverá os serviços para inclusão e exclusão de Cliente/Fornecedor “Pessoa Física” e “Pessoa Jurídica” no cadastro de inadimplentes da SPC Brasil, atendendo ao layout do SPC Brasil versão 13.0, no que diz respeito à negativação de clientes inadimplentes.

Retorno de negativação/restrição

A importação do arquivo de retorno de negativação/restrição é a confirmação que o SPC Brasil retorna ao cliente, relatando se o processamento foi bem-sucedido ou se ocorreu alguma falha e qual o motivo da mesma.  
A remessa enviada anteriormente está vinculada ao processamento do retorno, ou seja, uma remessa enviada ao SPC aguarda o processamento do retorno dessa mesma remessa.

Até a versão 12.1.2306, o sistema não permitirá, segundo orientação do SPC Brasil, importar um retorno quando o retorno da remessa anterior ainda estiver pendente para importação. Estas são regras de envio e recebimento de dados definidos pelo SPC Brasil.

Gerada remessa xx1, xx2 e xx3.  
Até a versão 12.1.2306, a importação do retorno obedecerá essa sequência de geração da remessa enviada. Não sendo permitido que seja importado o retorno da remessa xx3, antes da importação do retorno das remessas xx1 e xx2.

A cada remessa criada, um sequencial será gerado e o mesmo validado pelo sistema no retorno. A partir desse sequencial, os lançamentos atrelados a remessa gerada serão identificados e seus status alterados de acordo com a ocorrência enviada pelo SPC Brasil.

O arquivo de retorno enviado pelo SPC Brasil poderá conter ocorrências que indicam a "Confirmação do recebimento" e a "Recusa/Rejeição da Remessa". Essa informação estará no registro do campo referente ao Código de Retorno.

Configuração de dados para importação

Para execução do retorno de negativação/restrição é necessário que a remessa tenha sido gerada no sistema e enviada ao SPC Brasil. Também é primordial que as configurações sejam feitas para que o arquivo seja lido e processado corretamente, sendo elas:

Contrato de Serviços:

O contrato de serviços definido no borderô remetido está atrelado a um "Modelo de Negativação/Terceirização" com informações inseridas na aba "Layout" e no anexo "Ocorrências de Retorno". Na aba Layout as posições configuradas na tela abaixo estão de acordo com o manual do SPC Brasil

Na aba layout as posições configuradas na tela abaixo estão de acordo com o manual do SPC Brasil e deve ser configurada dessa forma.

As ocorrências serão cadastradas nessa aba e ao importar o retorno o sistema fará a leitura do código gerado pelo SPC Brasil e informado no arquivo de acordo com sua posição.

Importação

Na interface de importação, será solicitado contrato de serviço, previamente configurado, e o arquivo de retorno enviado pelo SPC Brasil.

Ao executar o processo, as linhas do arquivo são lidas e a ação tomada de acordo com a ocorrência que o SPC Brasil retornou. Ao final, será gerado um log com o resultado da operação.

O status de negativação do lançamento será alterado para "Confirmado", quando sucesso, ou "Recusado", quando erro. Um lançamento, quando recusada a negativação (status "Recusado"), poderá ser inserido em um novo borderô e enviada uma nova remessa

Lançamentos

**Baixa**

Ao efetuar a baixa de um lançamento que teve a negativação remetida ou confirmada, o processo irá mudar o status de negativação desse lançamento para 'Retirar negativação'. O status 'Retirar negativação' sinaliza que esse lançamento deverá ser incluído em um novo borderô do tipo "Exclusão de negativação" e enviado para que seja removida a sua restrição.

Observação: caso a baixa de uma lançamento seja realizada após a remessa do borderô, o retorno poderá ser realizado normalmente, mas o status de negativação dos lançamentos com retorno "Confirmado" permanecerão como "Retirar negativação".

Para os lançamentos que foram inseridos em borderôs de negativação, e estes ainda não remetidos, ao executar o processo de baixa manual, o sistema fará a remoção automática destes lançamentos de seus respectivos borderôs e também excluirá o borderô se o mesmo ficar sem lançamentos vinculados. O status do lançamento baixado volta para o status de origem "Não remetido".

**Cancelamento de baixa**

Ao efetuar o cancelamento de baixa de um lançamento que foi marcado com o status "Retirar negativação", o processo irá voltar o status de negativação desse lançamento para "Confirmado", que era seu status antes de efetuar a baixa.

**Restrições**

Não será possível executar os seguintes processos (o sistema fará o bloqueio da execução):

* Alteração de Lançamento
* Cancelamento de lançamento
* Parcelamento de lançamento
* Inclusão de fatura
* Geração de acordo
* Baixa manual de lançamentos

O campo "Status de Negativação" será validado pelo sistema e não permitirá a execução dos processos listados acima quando o valor for:

* Em Borderô
* Remetido
* Confirmado
* Retirar Negativação

Os principais campos do lançamento serão bloqueados para edição e alteração após a execução do processo de terceirização. Os campos que ficarão bloqueados são:

* Pagar/Receber
* Cliente/Fornecedor
* Data de Vencimento
* Valor Original
* Juros/Multa/Desconto
* Capitalização
* Valores Adicionais

**Status de negativação do lançamento**

0 - Não remetido: status inicial no qual o lançamento não teve nenhuma movimentação do processo de negativação;  
1 - Em borderô: o lançamento foi incluído em um borderô de negativação;  
2 - Remetido: o borderô de negativação de que o lançamento faz parte já foi enviado para negativação;  
3 - Confirmado: o retorno da negativação informou que foi confirmada a inclusão do lançamento junto à empresa de negativação;  
4 - Recusado: o retorno da negativação informou que por algum motivo a empresa de negativação recusou a inclusão;  
6 - Retirar Negativação: o lançamento que estava como remetido ou confirmado foi baixado, sendo assim, marcado para retirar a negativação.

Observações:

* No processo de acordo, o lançamento negativado só irá alterar o seu status quando for baixada a primeira parcela do acordo, e não na efetivação do acordo.
* No retorno de negativação de borderô, caso o título seja recusado pelo SPC Brasil, o status da remessa do borderô será alterado para "Confirmado" e o status  de negativação do título será alterado para "Recusado".

Mudança no processo de retorno de Terceirização/Negativação na validação do código da Remessa

A partir da versão 12.1.2402, o sistema não mais realizará a validação da ordem de processamento dos arquivos, essa validação obrigava o usuário a realizar a importação dos arquivos de retorno seguindo a ordem do código de sequência da remessa e a partir dessa versão não será mais necessário realizar o processo dessa forma. Isso porque essa validação se trata de um processo interno do SPC Brasil. Retirando essa validação o TOTVS Gestão Financeira dá mais flexibilidade para o usuário que pode processar os retornos de negativação sem se preocupar com a ordem dos arquivos.
