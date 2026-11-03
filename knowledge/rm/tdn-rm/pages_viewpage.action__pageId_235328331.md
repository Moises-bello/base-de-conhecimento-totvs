---
content_hash: 3a016861737859e21b347d514c5253692423ab48dcd6ca51cf8a297926cd14ad
fetched_at: '2026-06-29T00:08:03.892550+00:00'
page_id: '235328331'
product: rm
source: tdn-rm
title: ER_PCREQ-10571_Recebimento_com_cartão_no_módulo_de_caixa_TEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235328331
version: 33
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_CTB005 | **IRM** | PCREQ-8624 |
| **Requisito** | PCREQ-10571 | **Subtarefa** | PDR\_EDU\_CTB007-2 |
| **País** | (x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

Implementar a integração da solução SiTef da Software Express, no recebimento de lançamentos a receber com cartão de crédito ou débito no módulo de caixa através de um PinPad, sem a emissão de cupom fiscal.

## Definição da Regra de Negócio

Será implementada a integração com o software SITEF da empresa Software Express, que será responsável pela comunicação com as operadoras (adquirentes).

Para possibilitar o funcionamento, será necessário que a empresa possua um contrato com pelo menos um adquirente onde o SITEF seja homologado, como, por exemplo, Cielo, Rede, Stone e GetNet.

Serão tratados os pagamentos de serviços que não exigem a emissão de um cupom fiscal, ou seja, o sistema não emitirá o cupom fiscal nem trabalhará com uma impressora fiscal. Não deve ser feito o pagamento de produtos para os quais a lei exige a emissão de um cupom fiscal através de cartão pelo módulo de caixa. Para isso, deverá ser usado um sistema de PDV.

**1 - Parametrização:**

1.1 - Os seguintes parâmetros deverão ser criados, na etapa 02.02.05.01 - Módulo de Caixa, para permitir o uso do TEF:

* Usa TEF
* Endereço IP do SiTef - define o endereço IP do servidor SiTef
* Código da Empresa (SiTef) - define o código da empresa no SiTef
* Porta Default PinPad - define a porta default de comunicação do PinPad
* Mensagem Padrão PinPad - define uma mensagem padrão no visor do PinPad
* Liberar o estorno com senha do supervisor - define se o estorno de uma baixa que foi realizada no SiTef será liberado com a senha do supervisor ou usuário autorizado.

1.2 - Os seguintes parâmetros deverão ser criados, na etapa 02.02.02.01 - Manutenção de Baixas - Baixa a Receber, para pagamento com cartão de crédito:

* Valor mínimo por parcela - define o valor mínimo por parcela ao informar um meio de pagamento com cartão de crédito
* Número máximo de parcelas - define o número máximo de parcelas ao informar um meio de pagamento com cartão de crédito

1.3 - Ao abrir a sessão de caixa, serão acrescentados os seguintes parâmetros, caso o parâmetro "Usa TEF" esteja habilitado.

* Habilita TEF - define se a sessão de caixa habilita o pagamento de cartão de crédito ou débito via SiTef, caso o parâmetro Usa TEF estiver marcado.
* Porta PinPad - define a porta onde o PinPad está configurado. Campo será habilitado caso o Habita TEF estiver marcado.
* Porta Impressora - define a porta onde a impressora está configurada para impressão dos comprovantes do SiTef. Campo será habilitado caso o parâmetro Saída de Impressão seja "Porta LPT1".

**2 - Processos**

2.1 - Ativar Sessão de Caixa

Ao ativar a sessão de caixa o SiTef deverá ser configurado, se o parâmetro "Habilita TEF" foi marcado na abertura do caixa. Além disso, será verificada a presença do PinPad e escrito a mensagem padrão caso seja definida.

Funções a serem utilizadas:

* + ConfiguraIntSitefInterativoEx - configura o Sitef. Deverá ser chamado com os seguintes parâmetros: endereço ip, código da empresa, id do terminal e porta pinpad. O id do terminal deverá ter o formato XXNNNNNN, onde XX corresponder a dois caracteres alfabéticos que no caso deverá ser CX e NNNNNN seis números que no caso deverá ser o número sequencial IDTERMINALSITEF controlado pela GAUTOINC. Se o retorno da função for 0 significa que foi configurado com sucesso, caso contrário deverá ser apresentado para o usuário a mensagem de erro de acordo com a tabela abaixo e a sessão não deverá ser ativada.

    |  |  |
    | --- | --- |
    | **Valor** | **Descrição** |
    | 0 | Não ocorreu erro |
    | 1 | Endereço IP inválido ou não resolvido |
    | 2 | Código da loja inválido |
    | 3 | Código de terminal inválido |
    | 6 | Erro na inicialização do Tcp/Ip |
    | 7 | Falta de memória |
    | 8 | Não encontrou a CliSiTef ou ela está com problemas |
    | 9 | Configuração de servidores SiTef foi excedida |
    | 10 | Erro de acesso na pasta CliSiTef (possível falta de permissão para escrita) |
    | 11 | Dados inválidos passados pela automação |
    | 12 | Modo seguro não ativo (possível falta de configuração no servidor SiTef do arquivo.cha). |
    | 13 | Caminho DLL inválido (o caminho completo das bibliotecas está muito grande). |
* VerificaPresencaPinPad - verifica se existe um PinPad conectado. Caso não exista um PinPad conectado a sessão não deverá ser ativada.
* EscreveMensagemPermanentePinPad - escreve a mensagem padrão definida no visor do PinPad.

2.2 - Baixa de Lançamentos 

Na tela de meio de pagamento quando o usuário informar um meio de pagamento com o tipo primitivo "Cartão" e o tipo de transação "Crédito" deverá ser apresentado ao usuário uma opção de parcelamento com o parâmetro de número máximo de parcelas e valor mínimo por parcela.

Durante a baixa de lançamentos pela sessão de caixa ativada e habilitado o TEF, quando o meio de pagamento tiver o tipo primitivo “Cartão” ou "Cartão de Débito", deverá ser iniciada uma transação no SiTef.

Transação do SiTef:

Deverá ser criado uma tela para visualização do operador de caixa, onde serão mostradas as mensagens de comunicação com SiTef .

Para iniciar a transação no Sitef deverá ser utilizada a função IniciaFuncaoSitefInterativo, passando os seguintes parâmetros:

* Função - seleciona a forma de pagamento, de acordo com o meio de pagamento informado no momento da baixa. Com as opções de 2 para débito e 3 para crédito.
* Valor - valor a ser pago contendo o separador decimal (","). Deve sempre ser passado com duas casas decimais após a virgula.
* Operador - identificação do operador de caixa
* ParamAdic - parâmetros adicionais. Permite que o aplicativo limite o tipo de meio de pagamento. Caso seja uma transação de cartão de débito deverá ser passado os códigos [17;18;19;3031;], para crédito a vista os códigos [24;27;28;29;36;] e para crédito parcelado os códigos [24;26;28;29;36;].

Após iniciada a transação deverá ser utilizada a função ContinuaFuncaoSitefInterativo, onde serão enviadas as informações referentes ao pagamento. A partir desse envio, serão apresentadas informações enviadas pelo SiTef para o operador e solicitadas informações, se necessário, dependendo da parametrização do SiTef.

Caso ocorra algum problema na transação do SiTef será exibida uma mensagem para o operador do caixa se deseja continuar com o processo de baixa normalmente.

Caso a transação com SiTef seja concluída com sucesso, o processo de baixa será chamado e se for também realizado com sucesso a transação com SiTef será finalizada confirmando as transações realizadas. Caso no processo de baixa ocorra algum erro, a transação SiTef será finalizada não confirmando as transações realizadas.

Para finalizar a transação pelo SiTef deverá ser utilizada a função FinalizaFuncaoSitefInterativo.

Os comprovantes do SiTef serão impressos após o processo de baixa, e após a autenticação mecânica caso esteja parametrizado. Caso o parâmetro Saída de Impressão seja "Impressora Windows", no momento da impressão dos comprovantes o operador de caixa deverá selecionar a impressora, caso contrário serão impressos na impressora configurada na Porta Impressora definida na sessão de caixa.

Quando a transação e a baixa forem concluídas com sucesso, os dados das transações SiTef serão armazenados no sistema para futura conciliação, nas seguintes tabelas:

**FINTEGRACAOCARTAO** - dados da transação

* + IDPROCESSO: NSU do autorizador (tipocampo 134)
  + BANDEIRA: bandeira do cartão (tipocampo 131 e 132)
  + DATAHORA: data e hora da transação (tipocampo 105)
  + IDSTATUS: status da transação
  + CODAFILIACAO: código do estabelecimento (tipocampo 157)
  + MEIOPAGTO: meio de pagamento (cartão de credito ou débito)
  + NUMPARCELAS: número de parcelas do pagamento
  + CODCOLIGADA: código da coligada
  + IDMODELO: 3 (SiTef)
  + NSUSITEF: NSU do SiTef (tipocampo 133)

**FINTEGRACAOXCX** - extratos de caixa referente a cada transação

* CODCOLIGADA - código da coligada
* IDTRANSACAO - identificador da transação
* CODCOLXCX - coligada do extrato
* IDXCX - ref. do extrato

Obs: No processo de baixa quando tiver alguma transação com SiTef e o parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa" estiver marcado o mesmo deverá ser desconsiderado.

2.3 - Cancelamento de transações

Ao estornar a baixa de lançamentos realizadas pelo SiTef, caso o parâmetro "Liberar estorno com senha do supervisor" estiver marcado deverá ser solicitado a senha do usuário supervisor ou usuário com permissão.

Será criado um item de segurança "Liberar estorno transação SiTef" no Cadastro de Perfil, em Serviços Globais | Perfis | Acesso a Menus | Gestão Financeira / [4] Caixa / [04.01] Sessão de Caixa / [04.01.05] Perfis / [04.01.05.03] Liberar estorno transação SiTef, para permitir usuários a liberar o estorno de transações SiTef.

Para realizar a transação de cancelamento no SiTef deverá ser chamada a função IniciaFuncaoSitefInterativo passando o código da função 210 para cancelamento de cartão de crédito e 211 para cancelamento de cartão de débito. O SiTef solicitará os seguintes dados que estarão gravados na tabela FINTECRACAOCARTAO e que deverão ser enviados ao SiTef: data da transação, número do documento (NSU do autorizador ou NSU SiTef) e o valor da transação.

Para o cancelamento é solicitado a inserção do cartão no PinPad. 

Caso a transação seja realizada com sucesso pelo SiTef e processo de baixa ocorra algum erro, o estorno da baixa deverá ser feito normalmente novamente.

## Fluxo do Processo

## Dicionário de Dados

**Arquivo ou Código do Script:** FS.2016.06\_02
