---
content_hash: 34ea0065e16454e45366bea3e263ff0c1ae75f63804add8631114c2db4cec92e
fetched_at: '2026-06-29T00:11:32.133122+00:00'
page_id: '744487371'
product: rm
source: tdn-rm
title: Recebimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Recebimentos
version: 58
---

Para que um lançamento possa ser recebido através da sessão de caixa o operador deverá primeiramente realizar a [Pesquisa de Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=745132012) e selecionar os registros que serão pagos. Avançando para a tela de recebimento, poderá negociar juros, multas e descontos e irá definir uma ou mais formas de pagamento cadastrados/ativos.

Caso selecione um valor inferior ao total a ser recebido, será apresentado automaticamente o valor restante até o valor ser zerado.

## Negociação de juros, multa e desconto

Funcionalidade disponível a partir da release 12.1.2510.

Antes de escolher as formas de pagamento, o operador de caixa poderá revisar e negociar os valores de juros, multa e desconto dos títulos selecionados para o recebimento. Para habilitar essa funcionalidade, é necessário que o parâmetro *Permite alterar os valores do lançamento na baixa via a Sessão de Caixa*esteja marcado, em: Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a receber | Baixas | Baixa 1/6.

Serão exibidos os valores totais de juros, multa e desconto dos títulos selecionados. O operador poderá ajustar esses valores e o sistema recalculará automaticamente os valores dos títulos e o valor total a receber.

Os juros e as multas serão aplicados apenas em lançamentos vencidos. Já o desconto dependerá da configuração do parâmetro *Ignorar valor do desconto em lançamentos vencidos (Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a receber | Baixas | Valor líquido):* quando marcado, permite aplicar desconto em lançamentos vencidos e quando desmarcado, aplica o desconto apenas em lançamentos a vencer.

Quando o recebimento envolver mais de um lançamento, os valores negociados serão rateados entre os títulos, conforme definido no parâmetro *[Forma do Rateio dos Valores na Baixa](https://tdn.totvs.com/display/LRM/Recebimentos#recebimento-rateio-valores-baixa)*.

Observações sobre a aplicação de desconto

* O total a receber não pode ser igual a zero. Por isso, não será permitido aplicar um desconto que elimine o valor de todos os títulos selecionados;
* Quando o pagamento envolver mais de um título e o parâmetro de rateio dos valores estiver configurado como *Ordem dos lançamentos por Referência*, pode ocorrer de o desconto zerar o valor líquido de algum título. Nessa situação, o título será baixado e o item de baixa será gerado com valor zero, vinculado à conta/caixa da sessão, mas sem forma de pagamento.
Demonstração

## Recebimento

A seguir vamos detalhar o comportamento das formas de pagamento disponíveis, considerando os tipos primitivos.

recebimento0Recebimento com Dinheiro e Outros

Nesse ponto será demonstrado o comportamento para recebimento em dinheiro e outros meios com tipo primitivo ***diferentes*** de cartão, cheque ou PIX.

Após a seleção dos lançamentos a receber e adicionar as formas de pagamento com os tipos mencionados anteriormente, o operador deve acionar a opção "*Confirmar Pagamento*". Nesse momento o sistema irá realizar a baixa e atualizará as informações do lançamento.

Registro do Troco para pagamento em Dinheiro

Quando o recebimento for em dinheiro e o valor apresentado ao Operador for maior que o valor do lançamento, o valor de troco será exibido na tela e também no log da Sessão do Caixa.

2Recebimento com PIX

A partir da integração com o TOTVS Pagamento Digital é possível realizar recebimentos do contas a receber com PIX. 

Para realizar o recebimento com PIX, ao abrir a sessão de caixa deve ser marcado o parâmetro ***Habilitar PIX***, e ao fazer a baixa deve ser selecionado um meio de pagamento cadastrado com o tipo primitivo ***Pagamento Instantâneo (PIX)***.

TOTVS Pagamento Instantâneo/Pagamento Digital

Para que seja possível realizar o pagamento com PIX é necessário que tenha sido realizada a [Parametrização do TOTVS Pagamento Instantâneo / TOTVS Pagamento Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=611627231).

3Configurações SiTef

Para facilitar o recebimento de parcelas a receber, a Sessão de Caixa foi integrada com a solução SiTef da Software Express, validando a baixa de lançamentos a receber com cartões de Crédito e Débito, com transações através do SiTef em integração com PinPad, permitindo a emissão de comprovantes não fiscais.

Para utilizar esse tipo de pagamento, é necessário que o estabelecimento utilize a solução SiTef, comercializada pela [Bematech](http://www.bematech.com.br/), integrada a um PinPad, conectado ao terminal para realizar as transações.

Importante

A comunicação com o pinpad é realizada exclusivamente via conexão com fio.

A instalação do SiTef e as DLLs de interface de integração do SiTef para utilizar o Pinpad, são de responsabilidade da Software Express. As DLLs de interface de integração devem ser inseridas dentro da pasta onde o RM.exe se encontra.

**Observação:** Deve se atentar aos terminais para se inserir as DLLs, pois as configurações podem ser de 32 e 64 bits.

Para ver as parametrizações específicas do PinPad e do TEF acesse a página onde está a [Parametrização do Novo Módulo de Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#parametros-gerais) e veja as orientações que estão em *Etapa | TEF e TEF Filial*.

Configuração com Terminal Server

Para possível utilização do SITEF com Terminal Server, é necessário que seja realizado configurações na conexão da Área de Trabalho Remota, compartilhado as configurações dos dispositivos e recursos locais de porta, para que o RM realize a comunicação com o PinPad.

**Importante:**

As dlls e drive do PinPad e o drive da impressora devem estar no ambiente 'Client'.

A impressão dos comprovantes não fiscais emitidos na baixa com SiTef foram homologadas nas impressoras:

* Térmica: Bematech MP-4200 TH;
* Matricial: Bematech MP-20 MI.

O PinPad homologado para a transação:

* Gertec PPC900 LCM12 1 SAM SBLT USB GR.
* Com todas as características e exigências internacionais para pin pads seguros, o PPC 900 trabalha com diversos tipos de criptografia e está homologado pelas operadoras de cartão de crédito e débito no Brasil para o TEF.

Além dessas configurações, é possível configurar as opções de parcelamento com Cartão de Crédito.

Configurações de Parcelamento

O pagamento com a solução SiTef, possibilita o parcelamento dos lançamentos, permitindo definir o Valor mínimo de Parcela e o Número máximo de Parcelas, de acordo com a parametrização do sistema. Esta opção está disponível nos parâmetros do Financeiro: Ambiente | Parâmetros | TOTVS Gestão Financeira | Etapa 02.02.02.01 - Manutenção de Baixas / Aba Baixa a Receber.

*Valor mínimo por parcela* - Define o valor mínimo por parcela ao informar um meio de pagamento com cartão de crédito.

*Número máximo de parcelas* - Define o número máximo de parcelas ao informar um meio de pagamento com cartão de crédito.

Serão exibidas apenas as opções de parcelamento em que o valor da parcela seja maior que o valor mínimo permitido. Caso o valor a receber pelo cartão de crédito seja menor que o valor mínimo parametrizado, será apresentada apenas a opção de recebimento com uma parcela.

Para lançamentos baixados com cartão de crédito parcelado, a baixa cria Itens de baixa na quantidade de parcelas selecionadas no processo.

cartaoRecebimento com Cartão

Nesse ponto será demonstrado o comportamento para recebimento com cartão, podendo ser Débito ou Crédito.

Após a seleção dos lançamentos a receber o operador deve adicionar as formas de pagamento, no caso de pagamentos por Cartão de Crédito ele pode informar o parcelamento.

ParcelamentoPara o pagamento com o ***Cartão de Crédito*** através do Módulo de Caixa serão considerados os parâmetros informados nesse mesmo documento na aba *Configurações SiTef | Configurações de Parcelamento*. Lembrando que, a opção de parcelamento não está habilitada para a opção ***Cartão de Débito.***

Para os recebimentos por Cartão de Débito, o processo é similar ao de pagamento em dinheiro ou outros, pois não há a seleção de parcelas. Após adicionar as formas de pagamento, o operador deve selecionar a opção "*Confirmar Pagamento*".

Caso esteja parametrizada a integração com o SiTef o sistema fará a comunicação com o PinPad e iniciará o processo de integração, a seguir veremos como se dá o processo de baixa com essa integração e também como é que é feita a baixa com cartão sem ela.

Integração SiTef

Para Configurar o TEF veja a documentação de [Parametrização do Novo Módulo de Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#parametros-gerais) tanto os *Parâmetros Gerais | TEF*, como os *Parâmetros da Sessão de Caixa | Permissão* definidos em sua abertura.

Verificação do PinPad

A partir da release **12.1.2510**, a comunicação do **SiTef** com o **PinPad** deixa de ser feita na ativação da sessão de caixa e passa a ocorrer na seleção de meio de pagamento que integre via TEF, quando:

* o meio de pagamento utilizado é registrado pelo SiTef; e
* a sessão está configurada para **Habilitar TEF**.

Se houver falha na verificação do PinPad, o sistema exibirá mensagem de falha na comunicação. Para solução das falhas de comunicação, verifique a mensagem apresentada e certifique de que a integração com o SiTef está correta para novas tentativas.

#### Comportamento conforme os parâmetros do Caixa:

* **Usa TEF obrigatório**:

  + O sistema exibirá uma mensagem informando que **não foi possível realizar a integração**.
  + O operador deverá **escolher outro meio de pagamento** ou **verificar o motivo do erro de comunicação** para prosseguir com o recebimento.
* **Usa TEF (não obrigatório)**:

  + O sistema exibirá uma mensagem informando que **não foi possível realizar a integração**.
  + O operador poderá prosseguir utilizando uma **máquina de cartão externa** e, posteriormente, registrar os dados da transação manualmente no sistema, na tela de recebimento.
* **Não Usa TEF**:

  + Nenhuma comunicação com o PinPad será realizada.
  + O operador deverá registrar manualmente os dados da transação no sistema.
Recebimento com Integração com o SiTef

Vamos apresentar uma demonstração do recebimento com a integração com o SiTef e a comunicação com o PinPad.

Detalhamento sobre a comunicação com o PinPad

Iniciada a transação, são enviadas informações referentes ao pagamento, exibindo as mensagens retornadas pelo SiTef para o operador do caixa, e visualizadas na tela de comunicação com o PinPad. Na conclusão da transação de cartão, o processo de baixa será finalizado, efetivando os pagamentos realizados com cartão. Ao fim da baixa o sistema armazena os seguintes campos referente ao SiTef:

* Identificador de transação (TID);
* Bandeira do cartão;
* Data e hora da transação;
* Status da transação;
* Código do estabelecimento;
* Meio de pagamento;
* Número de parcelas do pagamento;
* Código da coligada;
* Modelo Transação;
* NSU do SiTef;
* NSU adquirente;
* [Código da rede autorizada](https://tdn.totvs.com/pages/viewpage.action?pageId=360448615);
* [Código autorização emissor de cartão](https://tdn.totvs.com/pages/viewpage.action?pageId=360448615).

Em caso de Erro na Transação

Caso ocorra algum erro no processo de baixa do lançamento financeiro, a transação SiTef não será mais cancelada e o erro será registrado no histórico da transação, no anexo "Histórico de Transações" localizado no menu "Movimentações Bancárias - Transações". Neste caso, o pagamento será efetivado junto a operadora e o lançamento financeiro ficará com o campo BAIXAPENDENTE igual a 'Pendente Sitef' até que a ocorrência exibida no log da baixa seja resolvida. Ao corrigir o problema que impediu a baixa do lançamento, será necessário executar o processo [Ajustar Transação](https://tdn.totvs.com/pages/viewpage.action?pageId=421388533), localizado no menu "Movimentações Bancárias - Transações", para que a baixa seja realizada com sucesso e o status da transação relacionada atualize de "Pagamento confirmado" para "Pagamento Concluído". Vale ressaltar que, considerando que o ambiente esteja configurado em N camadas, o processo de ajuste de transação pode ser agendado, evitando a intervenção do usuário para tal.

Nos lançamentos bloqueados por "Pendente Sitef", no processo de alteração, serão permitidos modificar os campos Departamento, Centro de Custo, Tabelas Opcionais, Data de Competência, Rateio por centro de custo, Rateio por departamento e Campos complementares.

Os comprovantes da transação serão impressos após o processo, e após a [autenticação mecânica](https://tdn.totvs.com/pages/viewpage.action?pageId=744487540) caso esteja [parametrizado](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#parametros-sessao-permissao).

Recebimento sem Integração com o SiTef

Vamos apresentar uma demonstração do recebimento quando não há a integração com o SiTef e a comunicação com o PinPad.

chequeRecebimento com Cheque

No Novo Módulo de Caixa o recebimento com cheque pode ser executado selecionando os meios de pagamento Cheque ou Cheque Pré-datado na nova tela de recebimentos como demonstrado a seguir:

Para essas opções ao escolher a opção "Confirmar Pagamento" o sistema apresentará a mesma tela de recebimento com cheque que é exibida no processo de Baixa.

Lançamento(s) com recebimento/pagamento via cheque

Não será possível realizar a baixa de lançamento(s) com recebimento/pagamento via cheque através do Novo Módulo de Caixa. Logo, esse(s) lançamento(s) não serão exibidos na tela de pesquisa quando forem pesquisados.

Nova tela de Recebimento com Cheque

A funcionalidade de recebimento com cheque realizada através do novo modulo de caixa tem previsão de migração para PO-UI nas próximas releases.

outros-modulosRecebimento em outros módulos

Para tornar o processo de recebimento mais fluido, é possível utilizar a tela de recebimento do *Novo Módulo de Caixa* através da visão de lançamentos integrada aos módulos da Linha RM.

Para o usuário que tenha uma *Sessão de Caixa aberta*, quando o mesmo acessar a visão de lançamentos integrada aos módulos da Linha RM ele verá um novo ícone  que permite realizar os recebimentos.

Quando temos a listagem de lançamentos financeiros na visão de lançamentos, é possível selecionar mais de um registro, ao clicar no ícone "Recebimento de Pagamento" é aberta uma janela com o processo de recebimento da Sessão de Caixa, onde o usuário deve selecionar os meios de pagamento, adicioná-los e ao final usar a opção *Confirmar Pagamento*. O processo será iniciado de acordo com o meio selecionado, como demonstrado nas abas desse documento.

No exemplo a seguir temos a demonstração do recebimento do financeiro de um movimento do TOTVS Gestão de Estoque, Compras e Faturamento, bem como, da tela final confirmando o recebimento com sucesso.

Para refletir o status do recebimento no lançamento, após o recebimento o usuário deve clicar no ícone (atualizar), então o lançamento terá o status atualizado.

Integração com SiTef

Para quem utiliza a integração com o SiTef, é importante que após abrir uma nova sessão, antes de realizar os recebimentos via sessão de caixa através das telas de outros módulos, realize o acesso ao "Meu Caixa".

integracao-contabilIntegração Contábil

A integração da contabilização dos recebimentos pelo Novo Módulo de Caixa é feita de forma que as intercorrências não gerem uma paralisação no processo do recebimento, a partir dessa nova versão ao realizar um recebimento em que houver diferença na contabilidade, a baixa será realizada e a contabilização será feita posteriormente.

Essa alteração foi feita considerando que o Operador do Caixa na maioria das vezes não é o mesmo responsável por avaliar a contabilização dos lançamentos e que o cliente que está efetivando o pagamento não pode ser afetado por qualquer intercorrência no processamento das integrações que são feitas posteriores à baixa sistêmica.

Por isso, quando há uma falha na contabilização o processo é finalizado na ponta do Operador e do Cliente, mas o sistema faz novas tratativas que permitem o ajuste posterior dessa contabilização:

* O primeiro tratamento feito é que o lançamento tem seu tipo contábil alterado para "Baixa a Contabilizar" e pode ser contabilizado através do processo "Contabilizar lançamentos baixados".
* O sistema cria automaticamente um job para a contabilização a ser executado logo em seguida, esse job pode ser verificado através da visão de Jobs (menu Ambiente | Processos | Gerenciamento de Jobs).

* Ao encerrar a nova sessão de caixa através da tela da própria sessão no Novo Módulo de Caixa, é exibida uma mensagem informando que alguns lançamentos não tiveram suas baixas contabilizadas.
* No log da sessão de caixa visível através do Gerenciar Caixas também haverá um registro informando que alguns lançamentos não tiveram suas baixas contabilizadas.

DICA

**Como acompanhar e realizar a contabilização das baixas que apresentaram problemas ?**

* Contabilizar

Para contabilizar as baixas e visualizar a necessidade de ajuste contábil é necessário executar o processo [Contabilizar Itens de Baixa](https://tdn.totvs.com/display/LRM/FIN+-+Contabilizar+Itens+de+Baixa).  
Este processo pode ser agendado conforme a necessidade da empresa, com a possibilidade de informar uma lista de emails que será notificada quando o mesmo for executado.

* Acompanhar

Na tela de [Baixas realizadas de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388647), é possível realizar filtros por período de data conforme a necessidade de acompanhamento, e por tipo contábil que representam que a contabilidade de baixa ainda não foi realizada.

rateio-valores-baixaRateio Valores na Baixa

Quando mais de um lançamento é selecionado para pagamento, é possível definir como os valores serão distribuídos entre os títulos. Essa configuração afeta tanto os meios meios de pagamento quanto os valores de juros, multa e desconto negociados no recebimento.

Para configurar, acesse o Assistente de Implantação de Processos, em: Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a receber | Caixa | Módulo de Caixa, opção *Forma do Rateio dos Valores na Baixa.*

As opções disponíveis são:

* Proporcional ao Valor Líquido: os valores (meios pagamento, juros, multa e desconto) serão rateados de forma proporcional ao valor líquido de cada lançamento.
* Ordem dos lançamentos por Referência: os valores (meios pagamento, juros, multa e desconto) serão consumidos a partir do lançamento com menor referência (identificador do lançamento) para o de maior. A ordem de aplicação dos meios de pagamentos informados é: Sitef, cartão manual, dinheiro, Pix, cheque.
0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517)
