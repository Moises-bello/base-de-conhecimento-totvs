---
content_hash: af68535e825c5fdce833cd828fc49d26de7f13072c9214f54c3b28130ead41d4
fetched_at: '2026-06-29T00:09:18.756323+00:00'
page_id: '421388780'
product: rm
source: tdn-rm
title: Conciliação das transações com cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388780
version: 62
---

**Introdução**

A conciliação de recebimentos com cartão tem o objetivo de verificar se a transação realizada via cartão foi paga pela operadora e compensar o extrato gerado por esse recebimento no momento da efetiva entrada do valor na conta corrente da empresa. Para realizar esse processo, o sistema irá confrontar os dados relacionados à baixa pelo meio de pagamento "Cartão" contidas no TOTVS Gestão Financeira com o extrato eletrônico disponibilizado pelas operadoras de cartão.

**Está disponível para os modelos de pagamento por cartão de crédito realizados pelo gateway Cybersource. Esse modelo de pagamento está disponível somente** **pela solução eduCONNECT Pay (somente para o Segmento Educacional).****Para operações realizadas via Portal Educacional com a operadora Cielo com os modelos disponíveis (BuyPage e Checkout ), a funcionalidade está em processo de piloto. O download dos arquivos é feito direto no site da Cielo e o Dash de  Acompanhamento ainda não foi homologado para a mesma.**

* Permite a realização da conciliação financeira de forma automatizada;
* Oferece maior agilidade e eficiência operacional.

Layouts homologados

Cielo - versão 14

**Parametrização do processo de conciliação**

No parametrizador do TOTVS Gestão Financeira em Contas a Receber | Baixas | Cartão de Crédito/Débito, deverá ser configurada a conta/caixa de depósito do valor recebido da operadora, bem como o diretório dos arquivos de conciliação.

Na etapa "Conciliação", poderá ser definida uma conta/caixa de depósito padrão e/ou por bandeira para a coligada. Essa definição poderá ser realizada também por filial na etapa "Configurações por filial", na aba "Conciliação".

Caso exista uma conta/caixa definida para determinada bandeira na configuração por filial, ela será considerada com prioridade. Na ausência desta, será considerada a conta/caixa padrão na configuração por filial. Não havendo nenhuma conta/caixa configurada por filial, será considerada a conta/caixa definida para determinada bandeira por coligada. Na ausência desta, será considerada a conta/caixa padrão por coligada.

Baixa de lançamentos com meio de pagamento cartão: No caso de baixas realizadas através do Portal Educacional ou do TEF pelo módulo de caixa, as informações necessárias para a conciliação serão gravadas automaticamente pelo próprio sistema. Para as baixas manuais com esses meios de pagamento, o usuário deverá informar alguns dados necessários para a conciliação:

* Bandeira do cartão;
* NSU (número sequencial único gerado no PDV ou POS);
* Código da autorização;
* Número da parcela.

Essas informações serão armazenadas nos extratos gerados nas respectivas baixas. A baixa com o meio de pagamento cartão deverá ser realizada em uma conta/caixa específica para esse meio de pagamento, para que seja transferida durante o processo de conciliação para a conta/caixa onde o valor foi efetivamente recebido.

**Interface da conciliação**

Disponível emMovimentações Bancárias | Cartão de Crédito/Débito | Conciliação.

Nesta visão serão exibidas todas as conciliações existentes da coligada, permitindo o uso de filtros para seleção. Vinculado a esta tela, existe o anexo com as operações de venda e os processo de importação de conciliação, conciliação automática, conciliação manual e desfazer conciliação.

Tabelas envolvidas:

FCONCILCARTAO: Conciliação de operações de vendas com cartão de crédito  
FCONCILIACAOGRPOPER: Resumo de Operações de venda

**Importação dos dados para Conciliação**

***CyberSource:*** O processo de conciliação irá tratar os arquivos de Extrato de Transação, Extrato Financeiro, Extrato de Ajuste e Extrato de Antecipação, disponibilizados pela Nexxera.

Extrato de Transação: Extrato de cartões onde são demonstradas todas as vendas efetuadas pelo estabelecimento e enviadas à Nexxera no log de vendas, em uma determinada data de referência.

Extrato Financeiro: Extrato de cartões onde são demonstradas todas as confirmações de pagamentos referentes a vendas já capturadas e demonstradas anteriormente pelas administradoras, para todos os estabelecimentos de um determinado grupo, em uma determinada data de referência.

Extrato de Ajuste: Extrato de cartões onde são demonstradas todas as ocorrências de ajustes realizados pelas administradoras, sendo estes referentes a vendas ou não, para todos os estabelecimentos de um determinado grupo, em uma determinada data de referência.

Extrato de Antecipação: Extrato de cartões onde são demonstradas todas as vendas efetuadas pelo estabelecimento e enviadas à Nexxera no log de vendas, em uma determinada data de referência. Para operadoras que trabalham com conceito de Resumo de Vendas, o registro é referente à liquidação antecipada do resumo ou parcela de resumo. Para operadoras que não trabalham com conceito de resumo, o registro será referente à venda antecipada, ou parcela de venda antecipada.

Os arquivos são gerados no formato CSV, e os campos devem ser separados por vírgula (","). Pode ser usada a integração com o SkylineWS, disponibilizado pela Nexxera para fazer o download automático dos arquivos de conciliação, mediante configuração nos parâmetros da coligada. Caso sejam configurados os parâmetros por filial, as configurações da filial prevalecerão sobre as configurações da coligada.

***Adyen*:**O processo de conciliação irá tratar os arquivos de extrato de transação (*received\_payments\_report*),  extrato financeiro (*settlement\_detail\_report*) e extrato de antecipação (*advancements\_report*), que são disponibilizados na área do cliente no portal da Adyen.

Extrato de Transação: O *received rayment report* é um relatório gerado diariamente e contém todas as transações recebidas e processadas em uma determinada *merchant account*. Com ele, é possível saber tudo que foi autorizado ou recusado, o motivo de recusa e o código de autorização.

Extrato Financeiro: O *settlement detail report* contém todas as transações que estão sendo liquidadas para a sua conta bancária pela Adyen, assim como informa todos os débitos e créditos que compõem o lote de liquidação. Ele é gerado sempre que fechamos um batch (lote) de liquidação. Este relatório especifica, em nível de transação, o valor bruto e líquido de capturas, estornos, *chargebacks* (quando presentes), total de taxas, correções de depósito, e o valor total sendo liquidado para a sua conta bancária. Ele também informa a data que o valor a ser creditado em sua conta corrente será efetivamente pago, assim como em qual conta esse crédito irá ocorrer.

Extrato de Antecipação: O *advancements report* especifica o valor bruto, taxa de antecipação, custo total e valor liquido que foi antecipado, por código de antecipação, em determinado dia por *merchant account*.

Os arquivos são gerados no formato CSV, e os campos devem ser separados por vírgula (",").

***TOTVS Pagamento Instantâneo*****:** O processo de conciliação irá tratar os arquivos de extrato financeiro (Baixa) das transações PIX liquidadas junto ao banco Original, que são disponibilizados através da integração com o Webservice.

Extrato Financeiro: O extrato de baixa contém as transações que estão sendo liquidadas para a sua conta bancária, com informações de taxa, data e valor de depósito que será efetivamente pago em sua conta corrente.

É importante ressaltar que a data da liquidação localizada no arquivo de conciliação está no formato da UTC, portanto, para fins de repasse (geração dos extratos de caixa de depósito e saque transferência), a mesma será ajustada para o fuso horário local.

Os arquivos são gerados no formato .JSON.

Caso a data da liquidação ocorra no final de semana ou em feriado nacional (devidamente cadastrado no calendário oficial dos parâmetros do sistema), a data do repasse será o próximo dia útil.

Para que isso ocorra corretamente o Tipo de Feriado deve estar configurado corretamente, contendo o Código e a Descrição correta para a modalidade de feriado ou recesso. Isso é muito importante para que o sistema reconheça o tipo de feriado e faça a compensação de forma correta.

Verificando o Tipo de Feriado:

TOTVS – Linha RM/ Serviços Globais

Tabela Dinâmica

Localize Tipo de Feriado em Tabelas de Domínio

Em Anexos/ Item de Tabela Dinâmica, irá aparecer o Código e a Descrição do Tipo de Feriado, por exemplo, para Feriados Nacionais, o código deve ser NA.

Essa configuração é de extrema importância para que o RM valide o Tipo de Feriado.  
  
Vale ressaltar que o Feriado cadastrado no Calendário deve estar configurado com o Tipo de Feriado correto. Por exemplo, o Feriado Nacional abaixo (Dia do Trabalho), deve estar configurado como Tipo do Feriado **Nacional**.

***Integração com TOTVS Web Services:***

1) Se selecionada a opção para conciliação diária, o processamento pode ser agendado para execução diária, considerando como Data de Liquidação sempre "Hoje - 1 dia", sendo esta, portanto, a opção recomendada.

2) Caso **não** seja selecionada a opção para conciliação diária, são disponibilizadas duas opções de filtros para importação dos extratos, sendo elas: o Período dos Extratos (Data Inicial e Data Final) e a Data de Liquidação (que pode ser desabilitada). Caso a Data Inicial e a Data Final não sejam informadas, será considerado como período o intervalo entre o número de dias parametrizados para busca retroativa e a data atual. Caso a Data de Liquidação seja informada, deve estar dentro do intervalo entre a Data Inicial e a Data Final. Caso a Data de Liquidação **não** seja informada, será considerada como sendo "Hoje - 1 dia".

3) A configuração das credenciais pode ser feita por coligada e/ou por filial. Quando configurada na coligada, sempre será executada, mesmo que exista configuração por filial. Existindo mais de uma filial configurada, todas serão executadas.

**Importante**:

Em Perfil | Acesso a Menus, será listado o menu "[03.05.03.01] Importação do Arquivo de Conciliação" para habilitar o acesso ao processo.

Somente será permitido importar o mesmo arquivo caso o conteúdo do arquivo seja alterado.

**Processo de Conciliação**

A conciliação poderá ser feita automaticamente através das informações gravadas no extrato gerado pela baixa com meio de pagamento cartão. Caso não seja encontrado um registro correspondente no sistema, será possível realizar a conciliação manualmente. Se a transação de venda (CV) retornar como rejeitada, o campo "Status de Conciliação do Cartão" no extrato ficará como "Rejeitado". Do contrário, caso a conciliação retorne o status do pagamento como "Agendado", "Enviado para o Banco" ou "A Confirmar", o campo "Status de Conciliação do Cartão" será alterado para "Previsto". Caso venha como "Pago", o Status de Conciliação do Cartão será alterado para "Pago".

Para os registros pagos, o extrato será compensado e a data de compensação será a data prevista de pagamento informada no registro de RO (Resumo das Operações). Além disso, serão gerados no sistema novos extratos de caixa vinculados ao extrato original que contém o valor correspondente ao lançamento financeiro recebido. O primeiro será uma transferência do valor efetivo pago pela operação na venda (descontada a taxa) com um novo tipo "Saque / Depósito Transferência na Conciliação com Cartão", gerando um extrato de saque na conta caixa do cartão (a mesma do extrato original) e um depósito na conta caixa de banco (conta caixa informada nos parâmetros da conciliação). O segundo será um saque na conta caixa cartão, criando um extrato com novo tipo "Saque Taxas Adm. Cartão" para o valor descontado como taxas e comissões sobre a operação.  As transações existentes nos dados da conciliação que não forem conciliadas serão armazenadas na tabela FCONCILCARTAOe poderão ser conferidas pela empresa posteriormente. Ao final do processo, será gerado um log com todos os itens conciliados com ou sem sucesso.

**Observações:**

O extrato gerado pela conciliação de cartão sempre irá gerar extratos com o número do documento gerado a partir da referência do extrato, desobrigando a habilitação do parâmetro "Copiar ref. para o número do documento".

As informações de parcelas devem estar discriminadas nos registros para que a importação seja realizada sem erros, assim o TID pode se repetir na importação.

É possível consultar a execução dos processos "Cobrança recorrente com cartão de crédito" e "Conciliação das transações com cartão" através do monitor de jobs e no "Dashboard Financeiro de recebíveis" verificar a data de última execução com sucesso de tais processos: [Gestão de Recebíveis e Conciliação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=540881707) / [DT Dashboard Financeiro - Visão Geral](https://tdn.totvs.com/display/LRM/DT+Dashboard+Financeiro+-+Visao+Geral).

Arquivos sem Operações de Venda serão importados com o Status de **Conciliado**.

**Conciliação na mesma conta caixa do cartão**

É possível conciliar as transações de pagamento com cartão na mesma conta caixa do cartão, sem a necessidade de uma conta caixa do banco.

A conciliação gera um único extrato de caixa descontando o valor da taxa da transação.

**Agendamento de Conciliação**

O processo de importação  e conciliação de arquivos poderá ser configurado para ser agendado para um horário determinado, assim como para ser executado de forma recorrente.

**Conciliação Manual**

Para a correta execução do processo, é necessário que uma importação de arquivo de conciliação tenha sido realizada previamente.

Para os extratos não conciliados automaticamente, o processo de conciliação manual permitirá ao usuário selecionar o registro de conciliação já importado, para que o sistema exiba os extratos ainda não conciliados.

Para a execução do processo, basta selecionar um registro na visão de conciliação. Na interface de conciliação manual, localizada em Movimentações Bancárias | Cartão de Crédito/Débito | Conciliação | Processos | Conciliação Manual, serão apresentados todos os extratos ainda não conciliados, conforme os arquivos selecionados.

O sistema possui uma flexibilização de filtros, disponibilizando também três modelos de visão além da visualização padrão. O usuário deve selecionar os itens correspondentes e solicitar a conciliação.

O usuário pode também vincular vários registros e conciliar somente ao final do processo, facilitando a operação com vários extratos ao mesmo tempo.

O processo de conciliar os registros selecionados manualmente pelo usuário obedecerá todas as regras da conciliação automática.

**Contabilização do processo de conciliação**

Ao realizar o processo de conciliação dos extratos de caixa com os dados do cartão, existe a possibilidade de realizar a contabilização dos extratos gerados de Saque Transferência e também para o extrato referente ao saque manual da taxa.  Será necessário que nos parâmetros de Integração Contábil, na etapa Contab. Extrato, o campo 'Default Contábil no Extrato' esteja configurado como 'Contábil'.   
Para definir o evento, deve-se acessar os parâmetros do financeiro | Contas a Receber | Baixas | Cartão de Crédito/Débito, na etapa Conciliação, definindo o campo 'Evento contábil default para extratos da conciliação'.

**Processo de Desfazer Conciliação**

Para desfazer uma conciliação é necessário selecionar um registro de conciliação na visão de 'Conciliação do Cartão' que esteja com status 'Conciliado' e executar o menu 'Processos' => 'Desfazer Conciliação'. Quando o processo é executado com sucesso, o status da conciliação muda para 'Não conciliado'.

Extrato Financeiro

O processo de desfazer conciliação tem como objetivo descompensar e cancelar os extratos criados pela conciliação, garantindo que a movimentação das contas/caixas envolvidas seja desfeita. Também serão cancelados todos os extratos gerados na baixa do lançamento que foi compensado à conciliação.

Extrato de Vendas

O processo de desfazer conciliação tem como objetivo voltar o status de conciliação das transações para "Não conciliado".

**Processo de Desfazer Conciliação Parcial**

Para desfazer uma conciliação parcialmente é necessário selecionar um ou mais registros de operações de vendas de alguma conciliação na visão de 'Conciliação do Cartão' que esteja com status 'Conciliado' ou 'Em conciliação' e executar o menu 'Processos' => 'Desfazer Conciliação' na aba de operações de venda . Quando o processo é executado com sucesso, caso tenha sido realizada o processo em todos as operações conciliadas, o status da conciliação muda para 'Não conciliado', mas se o processo de desfazer conciliação não tenha sido executado para todas as operações de venda, o status da conciliação continua como 'Em conciliação'.

**Cadastro de Taxas**

As taxas poderão ser cadastradas para validação no processo de conciliação. Mais informações em 

  Informações Complementares

* [DT - Conciliação Cartão](https://tdn.totvs.com/pages/viewpage.action?pageId=516629549)
* [DT - Agendamento de Conciliação](http://tdn.totvs.com/x/uj01Gg)
