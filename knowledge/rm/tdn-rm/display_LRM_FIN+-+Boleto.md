---
content_hash: 87f1a0eb15595410e64c63860951238e4c5b43faa139c3a8a674b7e517ee8290
fetched_at: '2026-06-29T00:09:18.071394+00:00'
page_id: '421388657'
product: rm
source: tdn-rm
title: FIN - Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Boleto
version: 54
---

O Boleto representa uma estrutura de dados, que permite estabelecer o histórico de Boletos por Lançamento sem restrição por segmento, ou seja você poderá selecionar Lançamentos gerados por quaisquer segmentos da linha RM e gerar Boletos, desde que este Lançamento seja compatível com o processo.

Em consonância com o novo modelo de Baixas, um Lançamento baixado parcialmente não gera um novo Lançamento. Logo, se um Boleto for baixado parcialmente, este Lançamento poderá gerar um novo Boleto com um novo Nosso Número, Código de Barra e IPTE. Além disto, o sistema permite que sejam inseridos novos Lançamentos ao Boleto em aberto e que ainda não tenha o código de Barras/IPTE gerados. 

Os Boletos serão gerados a partir da visão de Lançamentos | Processos. Para garantir maior flexibilidade, o sistema disponibiliza as seguintes opções:

Um Boleto para cada Lançamento

Esta opção permite que seja gerado um boleto para cada Lançamento Financeiro selecionado.

Um Boleto para cada Cliente/Fornecedor

Nesta opção será gerado um Boleto pelo valor total dos Lançamentos a receber agrupados pelo Cliente/Fornecedor.

Um Boleto para cada Cliente/Fornecedor e data de vencimento

Esta opção permite que sejam agrupados vários Lançamentos a receber do mesmo Cliente/Fornecedor e data de vencimento em um único boleto. A data de vencimento do Boleto será a mesma data de vencimento dos Lançamentos selecionados. Neste caso, o valor do boleto (agrupado por Cliente/Fornecedor e data) será a soma dos valores líquidos dos Lançamentos na data do vencimento.

**Observações:**

* O valor do Boleto será calculado na geração do Código de Barras porque o sistema permite que outros Lançamentos compatíveis sejam agregados ao Boleto. Para gerar o código de barras acesse o menu: Contas a Pagar | Receber | Boletos | Processos. Após a geração do Código de Barras nenhum dado que afete o valor líquido do Boleto poderá ser alterado.
* Para informar o campo de Vencimento no processo de inclusão de boleto é preciso que o perfil "Permitir Informar Data de Vencimento na Inclusão de Boleto" esteja habilitado para o usuário.
* Os campos de Usuário de criação, data de criação, usuário de alteração e data de alteração estão disponíveis na visão geral de boleto e podem ser usados na montagem do filtro da visão.
* O menu de Boleto está disponível também para integração com TOTVS Educacional x BackOffice Protheus quando ativa.

Validações para o processo de inclusão de Boletos

* Os lançamentos não podem ter um Boleto Em Aberto;
* Os lançamentos devem ter a mesma Conta Caixa;
* A conta caixa deve estar ativa;
* Os lançamentos devem ter o mesmo Convênio;
* O convênio deve estar ativo;
* A conta caixa deve ser compatível com o Convênio;
* Os lançamentos devem estar Em Aberto;
* Os lançamentos não podem ter sido faturados;
* Os lançamentos não devem estar vinculados com Cartão de Crédito;
* Os lançamentos não podem estar bloqueados;
* Os lançamentos não podem ser Previsões;
* Os lançamentos não podem ser Baixas Pendentes;
* Os lançamentos não podem ser do tipo Crédito de Adiantamento;
* Os lançamentos devem ter moeda Real, exceção para boletos gerados a partir do TOTVS Educacional com valor zero (neste caso o boleto é apenas um agrupador).
Inclusão de boleto com valores Juros, Juros ao Dia, Multa, Multa ao Dia, Desconto e Carência Juros

Na inclusão do boleto os campos Juros, Juros ao Dia, Multa, Multa ao Dia, Desconto e Carência Juros são preenchidos de acordo com os valores dos respectivos campos informados no lançamento. Os valores dos campos Juros, Multa e Desconto na inclusão do boleto para mais de um lançamento, são somados e informados nos campos Juros, Multa e Desconto respectivos do boleto gerado, podendo ser recalculados caso os valores forem alterados nos lançamentos relacionados. Estes não poderão ser alterados após inclusão do boleto, se registrado online, só será permitido alterar o valor de Juros e Multa de Lançamentos vinculados a Boleto Não Registrado. 

Ex:

|  |  |  |
| --- | --- | --- |
| Lançamento 1 | Lançamento 2 | Lançamento 3 |
| Juros ao Dia(Taxa): 5 | Juros ao Dia(Taxa): 5 | Juros ao Dia(Taxa): 5 |
| Multa ao Dia: 2 | Multa ao Dia: 2 | Multa ao Dia: 2 |
| Carência Juros: 1 | Carência Juros: 1 | Carência Juros: 1 |

Ao gerar boleto para lançamentos com diferentes valores de Multa ao Dia, Juros ao Dia e Carência Juros, os respectivos campos do boleto serão preenchidos com os "Valores Default" informados no Convênio do lançamento aba "Cobrança Bancária".

Ao gerar boleto para lançamentos com valores iguais ao de Multa ao Dia, Juros ao Dia e Carência Juros, os respectivos campos do boleto serão preenchidos com os valores informados nos lançamentos.

Ao gerar boleto para lançamentos com diferentes valores de Multa ao Dia, Juros ao Dia e Carência Juros é o convênio não possuir o cadastro dos Valores default o boleto será gerado com os respectivos campos zerados.

Para Juros ao Dia, caso as opções Taxa% e Valor estiverem divergentes entre os lançamentos, o boleto irá buscar o Valor default informado no Convênio.

**Observação importante para inclusão:**

Estas regras não se aplicam apenas quando o campo "Valor código de barras" na aba Dados Adicionais do convênio for Zero.

Desconsiderar lançamentos que utilizem fórmula para o cálculo de juros, multa ou desconto, pois as fórmulas não poderão ser agrupadas por proporcionarem valores variáveis. 

Utilizar conta caixa e convênio do lançamento

Ao marcar a opção "Utilizar conta caixa e convênio do lançamento" o boleto será incluso utilizando a Conta/Caixa e convênio do lançamento, desmarcando essa opção é permitido escolher Conta/Caixa e convênio na inclusão do boleto. 

Nosso Numero e Código de Barras/IPTE

Durante o processo de geração de Boletos, o NOSSO NUMERO será gerado automaticamente, conforme definições no cadastro do Convênio. Já o Código de Barras e o IPTE deverão ser gerados através da visão de Boleto, Processos/ Geração de Código de Barras. Esta opção foi criada porque antes da geração do código de barras/IPTE o sistema permite que outros Lançamentos sejam inseridos ao Boleto. Após a geração do Código de Barras e IPTE não será permitida nenhuma alteração que afete os dados do Boleto.

**Observações**

Para boleto do tipo Débito Automático não será possível gerar código de barras, com isso ao editar o boleto o botão de geração do código de barras estará desabilitado.

A geração de código é permitida somente para boletos de cobrança e será chamada durante a remessa de cobrança caso não tiver sido gerada manualmente. No caso de ocorrer um erro na geração, aquele lançamento não será enviado para a remessa e a informação será registrada no log para que o usuário tenha conhecimento.

A remessa de cobrança não irá gerar o código de barras automaticamente se no convênio estiver configurado para o nosso número ser gerado pelo banco. 

**Processos que envolvem boleto**

Cancelamento de boleto

Não será possível realizar o cancelamento de boleto caso exista uma transação de cartão de crédito/débito ou de PIX para o mesmo com os seguintes status de transação:

* Pagamento Pendente;
* Leitura de Pagamento Efetuado;
* Leitura de Pagamento Confirmado;
* Pagamento Confirmado;
* Pagamento Concluído;
* Pagamento Autorizado;
* Cancelamento Pendente;
* Cancelamento Negado.
Baixa de Lançamentos com Boleto

Para Lançamentos que tenham Boleto não será permitida a baixa pelos Lançamentos. A baixa deverá ser realizada através do respectivo Boleto (menu: Contas a Pagar / Receber | Boletos), podendo ser parcial ou total, manual ou por importação de arquivos de retorno.

Baixa parcial de Boleto

Ao fazer uma baixa parcial de Boleto, o sistema irá gerar outro Boleto com o valor restante em aberto do (s) Lançamento (s) do Boleto. Este novo Boleto poderá ser submetido a remessas ou a novas baixas. O cancelamento da baixa do Boleto deverá ser pela última baixa realizada para o Boleto.

Cancelamento da Baixa de Lançamento com Boleto

Ao incluir dois lançamentos que possuam "um boleto para cada lançamento" logo em seguida realizado a baixa com extrato agrupado e informando dois meios de pagamento "dinheiro e cheque por exemplo", ao cancelar a baixa de um dos dois lançamentos com a flag "Não gerar outro boleto para o lançamento após a baixa parcial" desmarcada o sistema deverá:

1. Cancelar as duas baixas do lançamento selecionado, e a baixa em cheque do outro lançamento deverá ser cancelada pois a mesma estava agrupada. Deixar o lançamento que não foi selecionado, parcialmente baixado.
2. Ao cancelar a baixa do lançamento o sistema deixa o boleto "Em Aberto". O outro lançamento que está parcialmente baixado deixa um boleto com STATUS "Baixado" e deve ser criado um outro boleto com o STATUS "Em Aberto" com o restante do valor.
3. O lançamento deve possuir somente um extrato de caixa referente ao item de baixa.

**Observação**:

O boleto com o status "Em aberto" somente será criado quando a flag "Não gerar outro boleto para o lançamento após a baixa parcial" estiver desmarcada. Caso a Flag esteja MARCADA o sistema irá alterar o status do boleto criado de "Baixado" para "Baixado parcialmente".

Baixa Pendente ocorre em duas situações

Quando o Aluno paga sua parcela no portal Educacional, o status do Lançamento é alterado para "Baixa Pendente" e permanece desta forma até que se finalize o processo de validação e posterior baixa pelo Gestão Financeira.

Consistência de Baixa Pendente para Lançamentos Financeiros gerados através do Totvs Gestão Fiscal: Ao definir que uma Guia que gerou um lançamento financeiro será uma Guia de Débito no processo de Compensações de Tributos Federais do Totvs Gestão Fiscal, não será possível Editar, Baixar, Emitir/Receber Cheque, gerar Acordo ou Remeter para banco este Lançamento Financeiro. Esses processos só serão permitidos novamente para o lançamento após a execução do processo "Finalização do Cálculo da Compensação" do Gestão Fiscal. 

Boleto de Contra Apresentação 

Criado campo "Contra Apresentação" no processo de inclusão de boleto e o atributo CONTRAAPRESENTACAO na tabela FBOLETO.  
Ao marcar a opção "Contra Apresentação" na inclusão de boleto será gerado código de barras com zeros (0000) na posição referente a data de vencimento.  Se a conta/caixa utilizada no lançamento for HSBC, o cálculo do "Nosso Número" será realizado considerando zeros (0000) na variável data de vencimento utilizada. Obs.: FBOLETO.VENCIMENTO continuará gravando a data de vencimento do boleto independente se o boleto for de contra apresentação ou não. Esse campo é utilizado para geração de relatórios e na impressão de boletos pelo TOTVS Educacional.

Impressão de Boletos

Para impressão do boleto, de convênio com tipo de Cobrança Registrado, o boleto deverá estar com "Status Registrado", conforme a regra imposta pela Febraban. Os Portais do Educacional/Processo Seletivo e Bibliotecário, também foram ajustados para atender esta norma. Caso seja necessário imprimir o boleto antes de registrar, o convênio deve estar com o tipo de Cobrança Não Registrado.

Na impressão pela visão de boletos é possível definir gerar um arquivo para cada boleto. Os arquivos serão gerados no servidor, e por isso não podem ser usados relatórios RM Reports que tenham parâmetros para preenchimento na tela. Ao final do processo será feito download para o diretório padrão de geração informado.

**Relatórios disponíveis para impressão**

Os relatórios estão disponíveis na pasta Objetos Gerenciais.

* FINREL0036 - Boleto Santander
* FINREL0037 - Boleto Bradesco
* FINREL0038 - Boleto Caixa
* FINREL0040 - Boleto Crefisa
* FINREL0041 - Boleto Cecred
* FINREL0042 - Boleto Banco do Brasil
Adequação das Fórmulas

As fórmulas que contém informações relacionadas ao boleto foram alteradas de acordo com a reformulação do boleto registrado. O contexto de lançamento deixará de ser utilizado, dando lugar para o contexto de boleto.  
As fórmulas são:

* ACEITE;
* CARTEIRA;
* NOSSONUMERO;
* CONTACAUCAO;
* DADOSPAGAMENTOBRADESCO (Informar o parâmetro INFORMACOESCOMPLEMENTARES e depois DATALIMITEPARADESCONTO); CODBARRABOLETO e IPTEBOLETO.

**Observações:**

Na tela de identificação do Boleto, o campo "Ref. Forma Pagamento" será preenchido automaticamente pela forma de pagamento do Lançamento (pasta Integração Bancária) apenas na geração de boleto para Débito Automático.

Após a remessa do Boleto, o STATUS.CNAB do(s) Lançamento(s) do Boleto será alterado para "Remetido"  e o STATUS da remessa no Boleto será alterado para Remetido. 

Envio de e-mail

Este processo permite enviar e-mail aos clientes com texto configurável e adição de arquivos anexos (boleto de cobrança, relatório de registros em aberto, etc). É possível selecionar qual relatório será utilizado para o texto do e-mail e qual será anexado. Para iniciar o uso deste processo é necessário validar a [Configuração do Servidor](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM) que será utilizado para envio. Em seguida, no cadastro de cliente é necessário informar o (s) e-mails Principal, Pagamento e/ou Entrega. Opcionalmente é possível inserir um e-mail no cadastro de contatos do cliente, ficando todos os endereços disponíveis para seleção no processo de envio do e-mail. Importante ressaltar que caso seja selecionado contatos com mesmo endereço de e-mail será enviado um único e-mail para cada boleto.

O sistema possibilita realizar o envio de e-mail dos boletos através da visão de boletos (o usuário que seleciona os registros desejados para submeter ao processo) e em lote (serão submetidos ao processo os registros que retornarem no filtro definido pelo usuário na tela dos parâmetros do processo). No caso do envio de e-mail em lote dos boletos o sistema possibilita realizar o agendamento e o fracionamento da execução do processo em vários jobs para obtenção de ganho de performance, caso o ambiente esteja parametrizado em N camadas. Além de utilizar esta arquitetura na instalação do sistema, é necessário acessar o menu 'Ambiente - Segurança de Jobs Fracionáveis' e inserir um novo registro com a classe "FinLanEnvioEmailLoteProcess", definindo o número mínimo e máximo de frações e ativando as opções 'Departamento Ativo" e "Agendável".

Para garantir mais segurança no acesso ao arquivo enviado no anexo do e-mail, o sistema dispõe da opção 'Proteger o boleto com os 5 primeiros dígitos do CPF/CNPJ do cliente' no processo de envio de e-mail com o objetivo de gerar o arquivo **pdf** protegido com senha, sendo necessário informar os 5 primeiros dígitos do CPF/CNPJ do sacado (Cliente/Fornecedor) do boleto para acessar o pdf enviado.

Além disso, para facilitar o controle de boletos enviados por E-mail, existe na visão de boletos a coluna "Status de envio de E-mail" com três valores possíveis: Não enviado, Enviado, e Reenviado. No momento do processamento do envio de E-mail o assistente permite elaborar um filtro (seja na visão de boletos ou nos parâmetros de envio no processo em lote) complementar utilizando de um ou mais destes status:

* **Não enviados** - serão selecionados apenas os boletos ainda não enviados, ao final do processo terão o seu status modificados para "Enviado".
* **Enviados** - serão selecionados apenas os boletos que já tenham sido enviados uma vez, ao final do processo terão o seu status modificados para "Reenviado".
* **Reenviados** - serão selecionados apenas os boletos que tenham sido enviados e reenviados pelo menos uma vez, o status não é modificado ao final do processo.

Observações:

* A ferramenta não valida e-mails incorretos, pois o servidor de e-mail leva um tempo para retornar que não conseguiu fazer a entrega.
* O processo de envio de boleto em lote (localizado no botão abaixo da opção de acesso a visão de Boleto) está disponível a partir da release 12.1.2310.
* A partir da release 12.1.2310 é possível utilizar, simultaneamente, um relatório para preenchimento das informações no corpo do e-mail e outro relatório para ser enviado como anexo.
Alterar Data de Vencimento

Mais informações sobre alteração da data de vencimento on-line:  

 Veja Também

 

 Informações Complementares

[Boleto via Web Service](https://tdn.totvs.com/display/LRM/Boleto+via+Web+Service)
