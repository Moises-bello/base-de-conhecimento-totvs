---
content_hash: 4ca5662ebcaa9f37649db43711d078165fcb16cc3914d43e25f8b0c58a7a2215
fetched_at: '2026-06-29T00:10:27.622726+00:00'
page_id: '516629549'
product: rm
source: tdn-rm
title: Conciliação das transações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516629549
version: 21
---

## Com o objetivo de realizar a conciliação dos dados de pagamentos com cartão de crédito/débito foi disponibilizado no sistema a 'Conciliação do Cartão' onde serão exibidos todos os registros de conciliação da coligada, permitindo o uso de filtros para seleção.

Conciliação de cartão CielotrueIntroduçãoIntrodução

A conciliação de recebimentos com cartão visa verificar se a transação realizada via cartão foi paga pela operadora e compensar o extrato gerado por esse recebimento no momento da efetiva entrada do valor na conta corrente da empresa.  
Para realizar esse processo, o sistema irá confrontar os dados relacionados a baixa pelo meio de pagamento cartão contidas no TOTVS Gestão Financeira com o extrato eletrônico disponibilizado pelas operadoras de cartão.

* Permite a realização da conciliação financeira de forma automatizada
* Maior agilidade e eficiência operacional.

**Formato do arquivo CyberSource**

Os arquivos são gerados no formato CSV, e os campos devem ser separados por vírgula (","). Pode ser usado a integração com o SkylineWS disponibilizado pela Nexxera para fazer o download automático dos arquivos de conciliação.

Em relação ao conteúdo, o arquivo é formado pelos registros:

* 00 - Header de Grupo
* 02 - Header de Adquirente
* 04 - Header de Estabelecimento
* 10 - Detalhe de antecipação de recebíveis
* 11 - Detalhe de parcela creditada da venda
* 12 - Detalhe de ajuste
* 96 - Trailer de Estabelecimento
* 98 - Trailer de Adquirente
* 99 - Trailer de Grupo

Este documento técnico será dividido para melhor compreensão, apresentando os seguintes tópicos:

**Parametrização da conciliação**

**Interface da conciliação de cartão**

* Visão dos registros importados do arquivo de conciliação
* Visão das Operações de venda

**Importação do arquivo de conciliação**

**Dados da transação na baixa de lançamentos com meio de pagamento cartão**

Parametrização da conciliaçãoParametrização da conciliação

No parametrizador do Totvs Gestão Financeira em **Contas a Receber | Baixas | Cartão de Crédito/Débito**, deverá ser configurada a conta caixa de depósito do valor recebido da operadora, o diretório dos arquivos de conciliação e o evento contábil para as contabilizações dos extratos Saque Transferência e Saque Manual.

Caso a conta caixa da conciliação não esteja preenchida, então no momento da conciliação só sera gerado o extrato do saque da taxa da operadora.

**CyberSource - Skyline**

Os parâmetros Usuário, Senha e URL são fornecidos pela equipe de TechFin da Totvs e devem ser informados aqui quando o processo de conciliação da CyberSource for automatizado. Esses parâmetros são necessários para poder fazer o download dos arquivos automaticamente na Nexxera e sua conciliação dentro do RM.

**OBS: A partir das versões listadas abaixo, a conciliação dos arquivos gerados pela Nexxera/SkylineWS além de conciliar as transações que já são conciliadas normalmente, também irá conciliar transações do TEF (adquirente rede) que forem retornadas no arquivo de conciliação.**

* **12.1.31.273**
* **12.1.32.219**
* **12.1.33.146**
* **12.1.34**

**Adyen** 

Os parâmetros Usuário, Senha e HMAC são gerados no ambiente da Adyen e devem ser informados aqui quando o processo de conciliação da Adyen for automatizado. Esses parâmetros

são necessários para poder fazer o download do arquivo automaticamente na adyen e sua conciliação dentro do RM.

Para que a Contabilização dos extratos gerados da conciliação seja efetuada, o sistema irá respeitar a seguinte parametrização:

Interface da Conciliação de CartãoInterface da Conciliação de Cartão

Disponível em **Movimentações Bancárias** **| Cartão de Crédito/Débito | Conciliação.**

Nesta visão serão exibidas as conciliações existentes já realizadas / importadas. A partir desse ponto poderão ser chamados os processos de importação do arquivo de extrato eletrônico, de conciliação automática e conciliação manual.

**Visão dos registros importados do arquivo de conciliação**

Em **Perfil | Acesso a Menus**, será listado o menu [03.05.03.01] Excluir para habilitar o botão de 'Excluir' na visão de conciliação do cartão.

## **Operações de venda**

Em **Anexos | Operações de venda**, será listado as transações de venda e os processo de importação de Conciliação e Conciliação Automática. Não é possível editar os registros exibidos.

Importação do arquivo de conciliaçãoImportação do arquivo de conciliação

## **Importação do arquivo de conciliação**

Em **Perfil | Acesso a Menus**, será listado o menu [03.05.03.02] Importação do Arquivo de Conciliação para habilitar o acesso ao processo.

Em **Processos | Importação do Arquivo de Conciliação**, será exibido uma tela para a execução da importação do arquivo de conciliação da CyberSource. O resultado desta operação será possível visualizar na visão de Conciliação do Cartão e na visão de Operações de Venda.

Ao marcar a opção "Importar e conciliar automaticamente" após executado o processamento da importação dos arquivos de conciliação, o sistema automaticamente irá disparar o processo de "Conciliação Automática".

Nesta tela é possível selecionar as seguintes opções:

* Arquivo único - Deve ser informado o arquivo a ser importado.
* Múltiplos arquivos - O processo irá executar a importação de todos os arquivos identificados em função do formato disponibilizados no diretório indicado em "Pasta de leitura dos arquivos de importação". O arquivos de log de processamento por sua vez poderão ser salvos em pasta específica, desde que seja informado no diretório indicado em "Pasta onde o log será salvo (opcional)". Os arquivos processados poderão ter sua extensão renomeada com a extensão .old, caso seja marcada a opção para esta finalidade.
* Skyline - O processo irá fazer o download dos arquivos de conciliação disponíveis no Skyline WS. Essa opção é habilitada somente para o modelo CyberSource. Caso não seja informado um período para download dos arquivos, será realizado o download dos arquivos do dia anterior à execução.

Quando executado em ambiente configurado como "Três Camadas", o processo de importação de arquivo de conciliação poderá ser configurado para ser agendado para um horário determinado, assim como para ser executado de forma recorrente.

**CyberSource - Skyline**

Na importação dos arquivos de conciliação do Cybersource - Skyline, é necessário que o arquivo tenha o formato esperado ( TIPOEXTRATO\_CNPJ\_DATA\_CONTADOR.csv ), uma vez que o campo data é buscado a partir do nome do arquivo. 

**Adyen**

**Importação e conciliação automáticas dos arquivos**

A importação de arquivos e conciliação de transações proveniente da Adyen também pode ser realizada de maneira automática e para esta opção será iniciada a partir de notificações da Adyen.

Uma notificação da Adyen é gerada e com esta, através de uma espécie gatilho (webhook - uma url para um serviço que é cadastrado junto à notificação), é disparado um serviço no TOTVS RM.

Este serviço recebe, entre outras informações, uma assinatura HMAC e as URLs para download dos arquivos a serem processados.

O serviço se encarrega de validar o hmacSignature da notificação/mensagem contra um código/assinatura (HMAC) parametrizada no módulo financeiro (menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber | Baixas | Cartão de Crédito/Débito | Conciliação) a fim de garantir a autenticidade da notificação (que realmente foi enviada a pela pela Adyen). Uma vez confirmada a origem da notificação, o serviço, de maneira ASSÍNCRONA, recupera (na notificação/mensagem) os endereços (URLs) dos arquivos relativos às transações a serem processados. Na sequencia, ainda de maneira ASSÍNCRONA, ocorre o disparo do processo de importação de arquivos e conciliação de transações passando como parâmetro a lista de URLs do arquivos recuperados anteriormente. O processo disparado é o de "Importação do arquivo de conciliação" onde neste caso, disparo automático por uma notificação da Adyen, possui uma passo adicional que é o de efetuar o download dos arquivos (da lista recebida como parâmetro) antes de começar propriamente a importação e conciliação.

A Adyen do cliente deve estar parametrizado/habilitado para trabalhar com notificações e o serviço do TOTVS RM Financeiro verificará notificações cujo eventCode seja igual a "REPORT\_AVAILABLE". Abaixo dois exemplos de endpoint do serviço do TOTVS RM Financeiro que deverá ser cadastrado no módulo de notificações da Adyen:

* <https://getnet-app01.totvs.com.br/educamobile/api/financial/v1/conciliation/1|1/adyen/weblistener>
* <http://localhost:8052/api/financial/v1/conciliation/1|1/adyen/weblistener>

OBSERVAÇÕES: 

     1. A parte em negrito do endpoint variará conforme a publicação do serviço do TOTVS RM nos ambientes/servidores do cliente;   
     2. O cadastro do endereço do serviço do TOTVS RM a ser cadastrado no "webhook" da Adyen por vezes não aceitou digitarmos e salvar com o caracter "|" (pipe) então tivemos de fazer o "encode" de tal caracter e utilizamos tal valor - "%7C" - no endpoint e funcionou perfeitamente. Ficando como o exemplo a seguir: <https://getnet-app01.totvs.com.br/educamobile/api/financial/v1/conciliation/1%7C1/adyen/weblistener>

Processamento da conciliaçãoProcessamento da conciliação

**Descrição**

A conciliação poderá ser feita automaticamente, através das informações gravadas no extrato gerado pela baixa com meio de pagamento cartão ou pela transação via e-commerce (tabela FINTEGRACAOCARTAO).

Caso não seja encontrado um registro correspondente no sistema, será possível realizar a conciliação manualmente.

Caso a conciliação retorne as informações como "**agendado"**, "**enviado ao banco"**, "**a confirmar"**, "**captura"** e sem a confirmação do pagamento da transação, o **Status de Conciliação do Cartão** será alterado para **“Previsto”**. Se a conciliação trouxer as informações de pagamento da transação, o Status de Conciliação do Cartão será alterado para **“Pago”**. Se a transação retornar como **rejeitada** ou **cancelada** o Status de Conciliação do Cartão do extrato ficará como **“Rejeitado”.**

Para os registros pagos, o extrato será **compensado** e a data de compensação será a data do pagamento apresentada na tabela de conciliação. Além disso, serão gerados no sistema novos extratos de caixa vinculados ao extrato original, que contém o valor correspondente ao lançamento financeiro recebido. O primeiro será feito uma transferência do valor efetivo pago pela operação na venda (descontada a taxa) com um novo tipo **“Saque / Depósito Transferência na Conciliação com Cartão”,** gerando um extrato de saque na conta caixa do cartão (a mesma do extrato original) e um depósito na conta caixa de banco (conta caixa informada no processo de conciliação). O segundo será um saque na conta caixa cartão, criando um extrato com novo tipo **“Saque Taxas Adm. Cartão”** para o valor descontado como taxas e comissões sobre a operação.

Não será permitido cancelar a compensação dos extratos gerados na conciliação.

As transações existentes nos dados da conciliação que não forem conciliadas serão armazenadas na tabela criada para armazenar os dados importados e poderão ser conferidas pela empresa posteriormente.

Ao final do processo, será gerado um log com todos os itens conciliados com ou sem sucesso.

ConciliaçõestrueConciliação AutomáticaConciliação AutomáticaConciliação Automática

## Conciliação automática

## Procedimento para Implantação

Para disponibilizar o recurso, deve ser habilitado a opção **Conciliação Automática** no cadastro de perfil do usuário.

## Procedimento para Utilização

Acessar o menu Processos | Conciliação Automática na visão de Conciliação de Cartão.

Para que a conciliação automática ocorra, é necessário primeiro que o arquivo contendo os registros a serem conciliados, tenha sido importado anteriormente.

Conciliação ManualConciliação ManualConciliação Manual

## Conciliação manual

## Procedimento para Implantação

Para disponibilizar o recurso, deve ser habilitado a opção **Conciliação Manual** no cadastro de perfil do usuário.

## Procedimento para Utilização

Acessar o menu Processos | Conciliação Manual na visão de Conciliação de Cartão.

Para que a tela de processo da conciliação manual seja exibida, deve-se selecionar um registro da visão de Conciliação de Cartão.

A exibição dos registros na tela pode ser alterada através do combobox localizado na parte superior direita.

Selecionando um registro não-conciliado e posteriormente um extrato será criado um *card* respectivo com as dados de conciliação. A seleção poderá ser desfeita clicando no [X] do card.

Ao finalizar a criação dos *card's* para conciliação; é só prosseguir em 'Executar'.

Dados da transação na baixa de lançamentos com meio de pagamento cartãoDados da transação na baixa de lançamentos com meio de pagamento cartão

No caso de baixas realizadas através do **Portal Educacional** ou via **TEF** no módulo de caixa, as informações necessárias para a conciliação serão gravadas automaticamente pelo próprio sistema.

Para as baixas manuais, quando o Meio de Pagamento conter um dos seguintes Tipos Primitivos:

* **Cartão**
* **Cartão de Débito**

Para a informação destes dados o sistema disponibiliza a opção "Cartão", ao selecionar o meio de pagamento:

    

O usuário deverá informar alguns dados necessários para a conciliação:

* **Operadora do cartão;**
* **Bandeira do cartão;**
* **Número da Parcela;**
* **NSU (número sequencial único gerado no PDV ou POS);**
* **Código da autorização;**
* **TID;**
* **Código do Estabelecimento (a partir do patch 12.1.2410.117 e execução do RM.Atualizador - marcação 'FS.2024.11\_01').**

Essas informações serão armazenadas nos extratos gerados nas respectivas baixas. A baixa com o meio de pagamento cartão deverá ser realizada em uma conta caixa específica para esse meio de pagamento, para que seja transferida durante o processo de conciliação para a conta caixa onde o valor foi efetivamente recebido.

No extrato de caixa gerado após a baixa do lançamento, a aba "**Dados da Transação**" apresentará as informações inseridas manualmente, ou então inseridas automaticamente caso a baixa seja via **TEF** ou através do **Portal Educacional:**

**Importante**: O campo "Status de conciliação do cartão" representará o status da conciliação no extrato de caixa:

Previsto (0);

Pago (1);

Rejeitado (2).
