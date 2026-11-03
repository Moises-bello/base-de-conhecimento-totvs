---
content_hash: 6bc180070b488b2f04be1817f6840ce189bc69bf4fc71dfd20b6e40af0d634a2
fetched_at: '2026-06-29T00:11:43.988508+00:00'
page_id: '808011306'
product: rm
source: tdn-rm
title: Configurações do TEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808011306
version: 8
---

Para utilizar o pagamento pelo Módulo de Caixa, é necessário que o estabelecimento utilize a solução SiTef comercializado pela [Bematech](http://www.bematech.com.br/), integrado a um PinPad, conectado ao terminal para realizar as transações.

A instalação do SiTef e as dlls de interface de integração do SiTef para utilizar o Pinpad, é de responsabilidade da Software Express. As dlls de interface de integração devem ser inseridas dentro da pasta onde o RM.exe se encontra.

**Observação:**

Deve se atentar aos terminais para inserir as dlls, pois as configurações podem ser de 32 e 64 bits.

O pagamento com a solução SiTef, possibilita o parcelamento dos lançamentos, permitindo definir o Valor mínimo de Parcela e o Número máximo de Parcelas, de acordo com a parametrização do sistema. Esta opção está disponível nos parâmetros do Financeiro: Menu 'Ambiente | Parâmetros | TOTVS Gestão Financeira | Etapa 02.02.02.01 - Manutenção de Baixas / Aba Baixa a Receber', onde:

* Valor mínimo por parcela

Define o valor mínimo por parcela ao informar um meio de pagamento com cartão de crédito;

* Número máximo de parcelas

Define o número máximo de parcelas ao informar um meio de pagamento com cartão de crédito.

Para lançamentos baixados com cartão de crédito parcelado, a baixa cria itens de baixa de acordo com a quantidade de parcelas definidas durante o processo do recebimento (baixa).

É possível realizar a validação do CNPJ do estabelecimento a partir da parametrização no ambiente TEF, onde sé passado para validação o CNPJ cadastrado na coligada ou filial de acordo com a parametrização do sistema RM. **Necessário ativar validação no ambiente TEF.**

**Parametrização do PinPad:**

A configuração para integração do SiTef com o PinPad, é realizada nos parâmetros do Financeiro: Menu 'Ambiente | Parâmetros | TOTVS Gestão Financeira |etapa 02.02.05.01 / Módulo de Caixa / TEF'.

Os campos a seguir devem ser preenchidos corretamente para a comunicação:

* Endereço IP: Define o endereço IP do servidor SiTef;
* Código da Loja (SiTef): Este código é de controle do estabelecimento definido junto a operadora do SiTef na instalação do PinPad;
* Porta Default: Define a porta default de comunicação do PinPad;
* Mensagem Padrão: Define uma mensagem padrão no visor do PinPad;
* Liberar o estorno com senha do supervisor: Define se o estorno de uma baixa que foi realizada no SiTef será liberado com a senha do supervisor ou usuário autorizado.

Dentre as opções para utilização do TEF estão disponíveis outras opções para que a integração do TEF seja obrigatória nos recebimentos via sessão de caixa. A configuração das opções será através dos parâmetros do Financeiro, assim a configuração de abertura da sessão de caixa respeitará essa parametrização: Menu 'Ambiente | Parâmetros | Contas a Receber | Caixa | Módulo de Caixa | TEF. São elas:

* Usa

Define se o TEF será habilitado no módulo de caixa, ao configurar essa opção o usuário poderá definir na abertura da sessão de caixa, se a opção "Habilita TEF" será usada ou não, marcando ou desmarcando a opção.

* Não Usa

Define que o TEF não será usado na sessão de caixa e ao abrir uma nova sessão de caixa a opção "Habilita TEF" será apresentada desmarcada e o sistema não permitirá alteração.

* Uso obrigatório

Define que o uso do TEF será obrigatório, a opção "Habilita TEF", na abertura da sessão será apresentada marcada e não permitirá que o usuário altere a configuração definida nos parâmetros do sistema.

**Observação:**

As opções de uso da TEF também estão disponíveis para o TEF por Filial, o sistema respeitará a configuração definida nos parâmetros do Financeiro. Menu 'Ambiente | Parâmetros | Contas a Receber | Caixa | Módulo de Caixa | TEF por Filial.

**TEF por Filial**

Ao informar os dados do TEF para determinada Filial, o sistema carregará esses dados para as transações do TEF, essa configuração será através dos parâmetros do Financeiro. Menu 'Ambiente | Parâmetros | *Contas a Receber | Caixa | TEF por filial*.  
Na abertura da sessão de caixa, ao marcar a opção "Habilita TEF", o sistema busca nos parâmetros do sistema a configuração definida.

**Observação:**

Ao configurar o sistema para utilizar o TEF por filial, na abertura da sessão de caixa o sistema segue a prioridade buscando a configuração da filial, caso não exista irá buscar por coligada. Para que o sistema considere a parametrização da coligada, não deve existir um cadastro por filial.

**SITEF - Configuração do Terminal Server**

Para possível utilização do SITEF com Terminal Server é necessário que seja realizado configurações na conexão da Área de Trabalho Remota, compartilhado as configurações dos dispositivos e recursos locais de porta, para que o RM realize a comunicação com o PinPad.

**Importante:**

As dlls/drive do PinPad e o drive da impressora devem estar no ambiente 'Client'. **Observação:** Importante que o estabelecimento mantenha uma boa conexão de rede para que não haja perda de comunicação no momento da transação.

A impressão dos comprovantes não fiscais emitidos na baixa com SiTef foram homologadas nas seguintes impressoras:

* Térmica: Bematech MP-4200 TH;
* Matricial: Bematech MP-20 MI.

O PinPad homologado para a transação:

* Gertec PPC900 LCM12 1 SAM SBLT USB GR.
* Com todas as características e exigências internacionais para pinpads seguros, o PPC 900 trabalha com diversos tipos de criptografia e está homologado pelas operadoras de cartão de crédito e débito no Brasil para o TEF.

Para utilizar o SiTef no processo de pagamento no módulo de caixa, deve selecionar a opção "Habilita TEF" na abertura do caixa. Além disso, a comunicação exibe no visor do PinPad, a mensagem padrão cadastrada nos parâmetros, caso seja definida.

Descontinuação do Módulo de Caixa 1.0

A partir da release 12.1.2510, o **Módulo de Caixa 1.0** será descontinuado e deixará de estar disponível no TOTVS Gestão Financeira.

A partir dessa versão, a solução oficial e suportada pela TOTVS para os processos de recebimento via Sessão de Caixa será exclusivamente o **Módulo de Caixa 2.0**, já disponível e que oferece mais recursos, melhor performance e maior aderência às boas práticas de mercado.

Recomendamos que as empresas realizem a migração para o **Módulo de Caixa 2.0** o quanto antes, garantindo continuidade operacional, suporte técnico e acesso às inovações da solução.

Para mais informações sobre a nova funcionalidade, consulte a [documentação nesse link](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517).
