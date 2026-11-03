---
content_hash: bcd6e2fce816e57bf61b32ce9683cbc662624498c6f39214738c95f4f5bd0d1c
fetched_at: '2026-06-29T00:11:23.154227+00:00'
page_id: '707372662'
product: rm
source: tdn-rm
title: Funções de Fórmulas TAA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=707372662
version: 27
---

RetNAOREPASSAAs fórmulas são compostas por funções e podem ser vinculadas nas etapas, para executar processos nos atendimentos, como por exemplo, alterar valor de um campo, avançar etapas, repassar atendimento, entre outros.  As funções são as ações que serão executadas nas fórmulas, e podem conter um ou mais parâmetros para execução.

Funções TAA

**ABS**

Retorna o valor absoluto de um número.

**ADICIONARDISCUSSAO**  
Atualiza o campo discussão do atendimento(do contexto) com o texto informado como parâmetro, adicionando novo texto.

PAR. 1 - Novo texto a ser gravado/adicionado [texto].

**ADICIONARDISCUSSAOATENDIMENTO**  
Adiciona um determinado texto à discussão do atendimento passado como parâmetro.

PAR. 1 - Coligada do atendimento [inteiro]  
PAR. 2 - Localidade do atendimento [inteiro]  
PAR. 3 - Código do atendimento [inteiro]  
PAR. 4 - Texto a ser adicionado à discussão do atendimento [texto]

**ADICIONARSOLICITACAO**  
Atualiza o campo solicitação do atendimento(do contexto) com o texto informado como parâmetro, adicionando novo texto.

PAR. 1 - Novo texto a ser gravado/adicionado [texto].

**ADICIONARSOLUCAO**  
Atualiza o campo solução do atendimento(do contexto) com o texto informado como parâmetro, adicionando novo texto.

PAR. 1 - Novo texto a ser gravado/adicionado [texto].

**AGENDADORESPONDIDO**  
Altera o status de um atendimento para Agendado Respondido.

**AGENDARARESPONDER**  
Altera o status de um atendimento para Agendado a responder.

PAR. 1 - Data de despertamento [data];  
PAR. 2 - Prazo limite [data];  
PAR. 3 - Motivo do repasse [inteiro];  
PAR. 4 - Justificativa [texto]

Exemplo: AGENDARARESPONDER("10/10/2006", "20/10/2006", -1 , '' )

**ALTERARCAMPOATENDIMENTO**  
Altera um ou mais campos ou parâmetros (segundo o tipo de atendimento) do atendimento. Sem espaços e aspas para campos texto.  
Pares de valor: CAMPO1=VALOR1; CAMPO2=VALOR2;PARAMETRO1.<nome doparametro>=VALORPAR1; CAMPO3=VALOR3;PARAMETRO2.<nome do parametro>=VALOR4;...

PAR. 1 - Campos e valores [texto]

Exemplo: ALTERARCAMPOATENDIMENTO('CODCATEGORIAGERAL=9;PARAMETRO.Nome Atendente = Vivian')

**ALTERARCLIENTEATENDIMENTO**  
Altera o cliente do atendimento

PAR. 1 - Coligada do cliente [inteiro]  
PAR. 2 - Código do cliente [texto]  
PAR. 3 - Tipo do cliente podendo ser 'P' para Pessoa, 'C' para Cliente, 'T' para Prospect, 'A' para  
Aluno ou 'R' para Professor [texto]

**ALTERARPARAMETROATENDIMENTO**  
Altera o valor de um parâmetro de um atendimento (de acordo com o tipo de atendimento). Deve ser informado o nome do parâmetro e o seu valor.

PAR. 1 - Nome do parâmetro [texto]

PAR. 2 - Valor do parâmetro [texto]

**ANALISAR**  
Interrompe a execução e exibe ao usuário as 4 variáveis passadas como parâmetro separadas por espaço

PAR. 1 - variaval1 [texto]  
PAR. 2 - variaval2 [texto]  
PAR. 3 - variaval3 [texto]  
PAR. 4 - variaval4 [texto]

**ANODT**  
Retorna o ano de uma data

PAR. 1 - Data [data]

**APROVARENTENDIMENTO**  
Para o atendimento do contexto, aprova o entendimento mais recente que esteja não aprovado ou aguardando aprovação/desaprovação. Retorna 1 (um) caso efetue a aprovação com sucesso ou 0 (zero) gere algum erro ou não encontre um entendimento a ser aprovado.

**ARRED**  
Arredonda um valor sem casas decimais

PAR. 1 - Valor [decimal]

**ARREDONDA**  
Arredonda um valor com casas decimais

PAR. 1 - Valor [decimal]  
PAR. 2 - Valor [decimal]

**ARREDVALOR**  
Arredonda um valor com casas decimais(Para Labore, Vitae e Chronus retorna o maior múltiplo de valor2 mais próximo e maior que o valor1)

PAR. 1 - Valor [decimal]  
PAR. 2 - Valor [decimal]

**ASCII**  
Retorna o valor que representa um determinado caractere na tabela ASCII

PAR. 1 - Valor [texto]

**AVANCARETAPAATENDIMENTO**  
Avança/Posiciona o atendimento para a etapa informada como parâmetro.

PAR. 1 - Código da etapa a avançar [inteiro]

**CALLWEBSERVICE**  
Chama um webService de acordo com os parâmetros usados

PAR. 1 - Endereço de acesso do webService [texto] (Ex. <http://abc.defgh/webService.asmx>)  
PAR. 2 - NameSpace da action/metodo do webService que erá utilizado [texto] (Ex. <http://namespace.com>)  
PAR. 3 - Nome da Action/Método [texto]  
PAR. 4 - Parametro [texto]

**CAMPOSATENDENTE**  
Retorna qualquer campo do atendente informado como parâmetro.

PAR. 1 - Código do atendente [inteiro]

PAR. 2 - Campo a ser retornado [texto]

**CAMPOSATENDIMENTO**  
Retorna qualquer campo ou parâmetro (segundo o tipo de atendimento) de um atendimento. Para buscar o valor de um parâmetro deve-se usar o campo no formato PARAMETRO.<nome do parâmetro>.

PAR. 1 - Campo [texto]

Exemplo:

Retornar um campo: CAMPOSATENDIMENTO('CODSTATUS')

Retornar um parâmetro: CAMPOSATENDIMENTO('PARAMETRO.PARAMETRO\_OBSERVACAO)

**CAMPOSATENDIMENTOTIPADO**  
Retorna qualquer campo ou parâmetro (segundo o tipo de atendimento) de um atendimento (caso o tipo retornado for uma data ele será do tipo DateTime).Para buscar o valor de um parâmetro deve-se usar o campo no formato PARAMETRO.<nome do parametro>

PAR. 1 - Campo do atendimento cujo valor deseja-se retornar [texto]

**CAMPOSPROXIMATAREFA**  
Retorna um determinado campo da próxima tarefa do atendimento do contexto

PAR. 1 - Campo da tarefa à ser retornado [texto]

**CAMPOSTAREFAATUAL**  
Retorna um determinado campo da tarefa atual do atendimento do contexto

PAR. 1 - Campo da tarefa à ser retornado [texto]

**CANCELAR**  
Executa a função de Cancelar um atendimento.

**CHEFEIMEDIATOATENDENTE**  
Retorna a coligada e código do atendente (no formato valor;valor) do chefe imediato do atendente informado como parâmetro (coligada do atendente, código do atendente).

PAR. 1 - Coligada do atendente [inteiro]

PAR. 2 - Código do atendente [inteiro]

**CHEFEIMEDIATORESPATENDIMENTO**  
Retorna a coligada e código do atendente (no formato valor;valor) do chefe imediato do atual atendente responsável pelo atendimento

**CHR**  
Retorna o caractere representado pelo número

PAR. 1 - Valor [decimal]

**CODATENDENTECONTATOCOMCLIENTE**  
Retorna o código do atendente responsável pelo contato com o cliente.

**CODATENDENTERESPONSAVEL**  
Retorna o código do atendente responsável pelo atendimento.

**CODIGOCLIENTE**  
Retorna o código do cliente do atendimento.

**CODIGODETALHEPRODUTO**  
Retorna o código do detalhe do produto do atendimento.

**CODIGOPRODUTO**  
Retorna o código do produto do atendimento.

**CODIGOPRODUTOPAI**  
Retorna o código do produto pai (no RMNucleus).

**CODIGOREPRESENTANTE**  
Retorna o código do representante do cliente do atendimento.

**COLIGADACORRENTE**  
Retorna a coligada corrente

**COLOCAREMANDAMENTO**  
Altera o status de um atendimento colocando-o Em Andamento.

**CONCAT**  
Concatena as strings a e b

PAR. 1 - string1 [texto]  
PAR. 2 - string2 [texto]

**CONCAT2**  
Concatena as strings a e b com um espaço entre elas

PAR. 1 - string1 [texto]  
PAR. 2 - string2 [texto]

**CONCATENA**  
Concatena dois valores (parâmetros um e três) usando um separador (parâmetro dois)

PAR. 1 - Valor a se concatenado [object]  
PAR. 2 - Separador [object]  
PAR. 3 - Valor a ser concatenado com o primeiro parâmetro [object]

**CONCLUIDOCONFIRMADO**  
Executa a função de Concluído confirmado para o atendimento.

**CONCLUIDOCONFIRMADOCOMEMAIL**  
Executa a função de Concluído confirmado para um atendimento enviando email para o cliente

**CONCLUIDOCONFIRMADOSEMEMAIL**  
Executa a função de Concluído confirmado para um atendimento sem enviar email para o cliente

**CONCLUIDORESPONDIDO**  
Executa a função de Concluído Respondido para um atendimento.

**CONCLUIDORESPONDIDOCOMEMAIL**  
Executa a função de Concluído Respondido para um atendimento enviando email para o cliente

**CONCLUIDORESPONDIDOSEMEMAIL**  
Executa a função de Concluído Respondido para um atendimento sem enviar email para o cliente

**CONCLUIRARESPONDER**  
Executa a função de Concluir a Responder para o atendimento.

**CONTEMVALOR**  
Procura um determinado valor em um conjunto de valores.

PAR. 1 - Conjunto de valores [texto]  
PAR. 2 - Valor a procurar [object]  
PAR. 3 - Tipo [texto]

**COTACAOMOEDA**  
Cotação de uma moeda

PAR. 1 - Símbolo [texto]  
PAR. 2 - Data [data]

**CRIARCOPIAATENDIMENTO**  
Cria cópia de um atendimento para o atendente responsável pelo atendimento original. O atendimento original deve ser informado via parâmetro, se não informado, o atendimento original será o atendimento do contexto. Retorna o código do atendimento gerado.

PAR. 1 - Localidade do atendimento a se copiar [inteiro];  
PAR. 2 - Coligada do atendimento a se copiar [inteiro];  
PAR. 3 - Código do atendimento a se copiar [inteiro];  
PAR. 4 - Lista de campos e valores a serem alterados no atendimento criado [texto].  
 Formato: Sem espaços e aspas para campos texto.  
Pares de valor: (CAMPO1=VALOR1; CAMPO2=VALOR2;PARAMETRO1.<nome do parametro>=VALORPAR1; CAMPO3=VALOR3;PARAMETRO2.<nome do parametro>=VALOR4;...);  
PAR. 5 - Indicativo se é para relacionar o novo atendimento com o original (0=Não Relacionar, 1=Relacionar) [inteiro]

**CRIARNOVOATENDIMENTO**  
Cria um atendimento em branco para o atendente responsável pelo atendimento do contexto e preenche o assunto e a solicitação deste novo atendimento como sendo o texto informado nos parâmetro (nesta ordem, assunto e solicitação)! Retorna o número do atendimento criado.

PAR. 1 - Novo assunto [texto]

PAR. 2 - Nova solicitação [texto]

**DATAALARME**  
Calcula a data de alarme de um atendimento. Os parâmetros indicam de qual atendimento será calculado a data de alarme, se informados valores menores que zero será calculado a data de alarme do atendimento do contexto. Retorna a data formatada como texto (dd/mm/yyyy)!

PAR. 1 - Localidade do atendimento a se copiar [inteiro];  
PAR. 2 - Coligada do atendimento a se copiar [inteiro];  
PAR. 3 - Código do atendimento a se copiar [inteiro];

**DATAALARMEDT**  
Calcula a data de alarme de um atendimento. Os parâmetros indicam de qual atendimento será calculado a data de alarme, se informados valores menores que zero será calculado a data de alarme do atendimento do contexto. Retorna a data.  
PAR. 1 - Localidade do atendimento a se copiar [inteiro]  
PAR. 2 - Coligada do atendimento a se copiar [inteiro]  
PAR. 3 - Código do atendimento a se copiar [inteiro]

**DATANULA**  
Retorna a data mínima do sistema

**DECANO**  
Subtrai um número de meses de um mês/ano e retorna o ano do resultado

PAR. 1 - Mês [inteiro]  
PAR. 2 - Ano [inteiro]  
PAR. 3 - Quantidade [inteiro]

**DECMES**  
Subtrai de um mês (1 a 12), um número de meses

PAR. 1 - Mês [inteiro]  
PAR. 2 - Quantidade [inteiro]

**DEFINECONTAOCLIENTE**  
Define o atendente contato com o cliente como sendo o atendente informado como parâmetro.

PAR. 1 - Novo contato com cliente [inteiro]

**DESAPROVARENTENDIMENTO**  
Para o atendimento do contexto, desaprova o entendimento mais recente que esteja aprovado. Retorna 1 (um) caso efetue a desaprovação com sucesso ou 0 (zero) gere algum erro ou não encontre um entendimento a ser desaprovado.

**DESCRICAODETALHEPRODUTO**  
Retorna a descrição do detalhe do produto.

**DESCRICAOPRODUTOPAI**  
Retorna o nome do produto pai (no TOTVS Gestão de Estoque, Compras e Faturamento)

**DIADT**  
Retorna o dia de uma data

PAR. 1 - Data [data]

**DIASEMANA**  
Retorna o dia da semana de uma data

PAR. 1 - Data [data]

**ENVIAEMAIL**  
Permite enviar e-mail quando a fórmula é executada e registra\* na discussão do atendimento a mensagem enviada.  
\*registra = No campo discussão serão apresentadas as informações: De (From), Para (To), Cópia (CC), Data, Assunto, Mensagem.  
Caso o email for do tipo HTML e tiver a palavra chave [ACOESDOATENDIMENTO] em seu corpo, serão incluídos links cada uma das possíveis ações do atendimento no contexto da tarefa atual.

PAR. 1 - Informar o endereço de e-mail do remetente [texto].  
PAR. 2 - Informar o endereço de e-mail do destinatário [texto].  
PAR. 3 - Informar o endereço de e-mail que receberá uma cópia do e-mail [texto].  
PAR. 4 - Informar o assunto do e-mail [texto].  
PAR. 5 - Informar o corpo do e-mail [texto].  
PAR. 6 - Informar o formato do e-mail (True caso for HTML e false caso for Texto) [Bool].

Exemplo: ENVIAEMAIL('teste@[teste.com.br](http://teste.com.br)','teste@[teste.com.br](http://teste.com.br)','teste@[teste.com.br](http://teste.com.br)','Assunto Teste',A função permite enviar o e-mail e registra a mensagem na discussão do atendimento para maior controle das informações. Até Breve!',True)

**ENVIAEMAILABERTURA**  
Envia email de abertura para o cliente do atendimento

**ENVIAEMAILIMEDIATAMENTE**  
Envia um email imediatamente. Caso o email for do tipo HTML e tiver a palavra chave [ACOESDOATENDIMENTO] em seu corpo, serão incluidos links ao corpo do email para cada uma das possíveis ações do atendimento do contexto para sua tarefa atual.

PAR. 1 - Endereço de email do remetente [texto]  
PAR. 2 - Endereço de email do destinatário [texto]  
PAR. 3 - Endereço de email ao qual será enviada uma cópia do email [texto]  
PAR. 4 - Assunto do email [texto]  
PAR. 5 - Corpo do email [texto]  
PAR. 6 - Formato do email (true caso for HTML e false caso for texto) [bool]

**ENVIAEMAILREPASSE**  
Envia um email de repasse para o endereço informado.

PAR. 1 -Endereço de email do remetente [texto]  
PAR. 2 -Endereço de email do destinatário [texto]  
PAR. 3 -Endereço de email ao qual será enviada uma cópia do email [texto]  
PAR. 4 -Atendente ao qual o repasse será realizado, lembrando que isso será apenas para informações do email, não definirá de fato quem receberá o atendimento[texto]

**ENVIAEMAILREPASSEIMEDIATAMENTE**  
Envia imediatamente um email de repasse para o endereço informado.

PAR. 1 - Endereço de email do remetente [texto]  
PAR. 2 - Endereço de email do destinatário [texto]  
PAR. 3 - Endereço de email ao qual será enviada uma cópia do email [texto]  
PAR. 4 - Atendente ao qual o repasse será realizado, lembrando que isso será apenas para informações do email, não definirá de fato quem receberá o atendimento [texto]

**ENVIASMS**  
Envia um SMS para o telefone destinatário informado no parâmetro.

PAR. 1 - Usuário do serviço de SMS [texto]  
PAR. 2 - Senha do serviço de SMS [texto]  
PAR. 3 - Remetente [texto]  
PAR. 4 - Telefone destino [texto]  
PAR. 5 - Mensagem [texto]

**ESCREVELOG**  
Escreve uma mensagem no Log.

PAR. 1 - Log [texto]

**EXECSQL**

Executa uma sentença SQL previamente cadastrada.

PAR. 1 - Código da sentença SQL previamente cadastrada que será executada

**EXECUTARRELATORIOENVIAREMAIL**  
Executa o relatório no contexto do atendimento e envia para o(s) e-mail(s) passados como parâmetro.

PAR. 1 - Coligada do Relatório [inteiro]  
PAR. 2 - Id do Relatório [inteiro]  
PAR. 3 - Assunto do E-mail [texto]  
PAR. 4 - Endereço de E-mail do Destinatário [texto]  
PAR. 5 - Endereço de E-mail do ReplyTo [texto]  
PAR. 6 - Endereço de E-mail ao qual será enviada uma cópia do e-mail [texto]  
PAR.7 - Endereço de E-mail ao qual será enviada uma cópia oculta do e-mail [texto]

Exemplo: EXECUTARRELATORIOENVIAREMAIL(1,5,'Teste da Função de Fórmula','[teste@teste.com.br](mailto:teste@teste.com.br)','[teste@teste.com.br](mailto:teste@teste.com.br)','[teste@teste.com.br](mailto:teste@teste.com.br)','[teste@teste.com.br](mailto:teste@teste.com.br)')

**FOR**  
Executa uma fórmula

PAR. 1 - Código da fórmula [texto]

**FRAC**  
Retorna a parte fracionada de um valor

PAR. 1 - Valor [decimal]

**GERARLANCAMENTO**  
Gera um lançamento financeiro no TOTVS Gestão Financeira.

PAR. 1 - Coligada do cliente [inteiro]  
PAR. 2 - Código do cliente [texto]  
PAR. 3 - Código da filial [inteiro]  
PAR. 4 - Tipo do documento [texto]  
PAR. 5 - Data do vencimento [data]  
PAR. 6 - Tipo contábil [texto]  
PAR. 7 - Tipo pagar ou receber [texto]  
PAR. 8 - Valor [texto]

**GERARLANCAMENTOCAMPOSEXTRAS**  
Gera um lançamento financeiro no TOTVS Gestão Financeira com campos extras.

PAR. 1 - Coligada do cliente [inteiro]  
PAR. 2 - Código do cliente [texto]  
PAR. 3 - Código da filial [inteiro]  
PAR. 4 - Tipo do documento [texto]  
PAR. 5 - Data do vencimento [data]  
PAR. 6 - Tipo contábil [texto]  
PAR. 7 - Tipo pagar ou receber [texto]  
PAR. 8 - Valor [texto]  
PAR. 9 - Lista Campos [texto]  
PAR. 10 - Lista Valores [texto]

**GETIDDAREQUISICAO**  
Retorna o ID da requisição baseado nos dados do atendimento.

**GRUPOATENDENTECAMPOCOMPLEMENTAR**  
Retorna qualquer campo complementar do grupo de atendente informando os parâmetros.

PAR. 1 - Código do grupo de atendente [inteiro];  
PAR. 2 - Campo complementar cujo valor deseja-se retornar, esta função permite operações de soma [texto].

**HIERARQUIARHDESTINOREQUISICAO**  
Retorna a hierarquia do Gestão de Pessoas destino da requisição.

**HIERARQUIARHORIGEMREQUISICAO**  
Retorna a hierarquia do Gestão de Pessoas origem da requisição.

**HOJE**  
Retorna a data de hoje

**INCANO**  
Adiciona um número de meses a um mes/ano e retorna o ano do resultado

PAR. 1 - Mês [inteiro]  
PAR. 2 - Ano [inteiro]  
PAR. 3 - Quantidade [inteiro]

**INCMES**  
Adiciona a um mês (1 a 12), um número de meses

PAR. 1 - Mês [inteiro]  
PAR. 2 - Quantidade [inteiro]

**INSERIRAPONTAMENTO**  
Cria um novo apontamento para o atendimento do contexto.

PAR. 1 - Data de início da atividade[data];  
PAR. 2 - Hora de início da atividade[texto no formato 00:00 ou 0,00 ou 0.00];  
PAR. 3 - Número de horas gastas na atividade[texto no formato 00:00 ou 0,00 ou 0.00];  
PAR. 4 - Data de término da atividade[data];  
PAR. 5 - Hora de término da atividade[texto no formato 00:00 ou 0,00 ou 0.00];  
PAR. 6 - Percentual de completude da atividade[inteiro]  
PAR. 7 - Comentário sobre o apontamento[texto]  
PAR. 8 - Código do atendente do qual o apontamento será gerado[inteiro]

**INT**  
Trunca um valor

PAR. 1 - Valor a truncar [decimal]

**INTERROMPE**  
Interrompe o processamento da fórmula e exibe a mensagem passada no parâmetro.

PAR. 1 - Mensagem exibida ao final do processo. [texto]

**INTTOSTRFORMAT**  
Converte um valor inteiro para string (texto) preenchendo com zeros

PAR. 1 - Valor [inteiro]  
PAR. 2 - Zeros [inteiro]

**MAX**  
Retorna o maior número

PAR. 1 - valor1 [decimal]  
PAR. 2 - valor2 [decimal]

**MESDT**  
Retorna o mês de uma data

PAR. 1 - Data [data]

**MIN**  
Retorna o menor número

PAR. 1 - Valor1 [decimal]  
PAR. 2 - Valor2 [decimal]

**MTDATA**  
Monta uma data a partir do dia, mês e ano

PAR. 1 - Dia [inteiro]  
PAR. 2 - Mês [inteiro]  
PAR. 3 - Ano [inteiro]

**NOMEATENDENTERESPONSAVEL**  
Retorna o nome do atendente responsável pelo atendimento.

**NOMECLIENTE**  
Retorna o nome do cliente.

**NOMECONTATOCLIENTE**  
Retorna o nome do contato do cliente

**NOMECONTATOCLIRPR**  
Retorna o nome do contato do cliente ou representante (nesta ordem).

**NOMECONTATOREPRESENTANTE**  
Retorna o nome do contato do representante.

**NOMEPRODUTO**  
Retorna o nome do produto.

**NOMEREPRESENTANTE**  
Retorna o nome do representante.

**PAR**  
Variável genérica. Utilizada também para validação de campos complementares.

**PARAMETROSATENDIMENTO**  
Busca o valor de um parâmetro de um atendimento (de acordo com o tipo de atendimento).

PAR. 1 - Código do parâmetro [inteiro]

**POTENCIA**  
Retorna a potência

PAR. 1 - Base [decimal]  
PAR. 2 - Expoente [inteiro]

**PRODUTOCAMPOCOMPLEMENTAR**  
Retorna qualquer campo complementar do produto informando os parâmetros 'PAR. 1 - Código do produto [inteiro]; '+'PAR. 2 - Campo complementar cujo valor deseja-se retornar [string]. Esta operação permite operações de soma.

PAR. 1 - Código do produto [inteiro]

PAR. 2 - Campo [texto]

**PROXREGSQL**  
Avança um registro na Consulta SQL executada.

PAR. 1 - Código sentença SQL [texto]

**RAIZ**  
Retorna a raiz quadrada de um valor

PAR. 1 - Valor [decimal]

**REPASSARATENDIMENTO**  
Repassar o atendimento a outro Atendente/Grupo.

PAR. 1 - Código do atendente [inteiro];  
PAR. 2 - EMailRepasse [texto];  
PAR. 3 - Motivo do repasse [inteiro];  
PAR. 4 - Discussão [texto];  
PAR. 5 - EMailCopia [texto]

**REPASSARATENDPARAGRUPO**  
Repassa o atendimento do contexto para um determinado grupo de atendentes.

PAR. 1 - Código do grupo de atendentes que o atendimento será repassado [inteiro]  
PAR. 2 - Código do motivo de repasse [inteiro]  
PAR. 3 - Justificativa do repasse [texto]  
PAR. 4 - Endereço de email para o qual será encaminhada uma cópia do email de repasse [texto]

**REPASSARDEVOLTA**

Repassa o atendimento de volta para o atendente anterior

PAR. 1 - Código do motivo de repasse [inteiro]

PAR. 2 - Justificativa do repasse [texto]

**RESULTSQL**

Acessa o resultado de uma sentença SQL previamente executada pela função **EXECSQL**

PAR. 1 - Código da sentença SQL previamente executada pela função **EXECSQL** [texto]

PAR. 2 - Campo da sentença SQL que se deseja retornar o valor, havendo mais de um registro, sempre será retornado o primeiro. [texto]

Exemplo:

SE EXECSQL( '\_AUT.ESP.SQL' ) = VERDADE ENTAO   
  SETVAR( CODETP, RESULTSQL(  '\_AUT.ESP.SQL', 'CODTAREFADESTINO' ));   
FIMSE; 

**RETIRACARACTERES**  
Retira do texto todas as ocorrências dos caracteres da string chars

PAR. 1 - Caracteres à retirar [texto]  
PAR. 2 - Texto [texto]

**RetNAOREPASSA**  
Retorno não repassa o atendimento, NÃO atualiza histórico, NÃO atualiza etapa no atendimento, NÃO executa fórmula do fluxo.

**Importante**: Essa função somente tem efeito em fórmulas que um de seus caminhos faça sentido que nenhuma das ações mencionadas seja executada, segue um exemplo:

SE EXECSQL( 'SQL\_DECISAO' ) = VERDADE

ENTAO   
  CONCATENA(COLIGADACORRENTE, 5, ';');  
SENAO

  **RetNAOREPASSA;**  
FIMSE; 

**RetNAOREPASSAATULIZARESTANTE**  
Retorno não repassa o atendimento, atualiza histórico, atualiza etapa no atendimento, executa fórmula do fluxo.

**Importante**: Essa função somente tem efeito em fórmulas que um de seus caminhos faça sentido que nenhuma das ações mencionadas seja executada, segue um exemplo:

SE EXECSQL( 'SQL\_DECISAO' ) = VERDADE

ENTAO   
  CONCATENA(COLIGADACORRENTE, 5, ';');  
SENAO

  **RetNAOREPASSAATULIZARESTANTE;**  
FIMSE; 

**RETORNAATENDENTEHIERARQUIARH**  
Retorna o atendente da hierarquia do Gestão de pessoas que foi informada.

PAR. 1 - Texto contendo coligada e ID da hierarquia separados por ; [texto]

**RETORNAHIERARQUIARHATUALREQ**  
Retorna a hierarquia do Gestão de Pessoas do atendente atual.

**RETORNAPROXIMAHIERARQUIARH**

Retorna a coligada e código da hierarquia superior a que foi passada como parâmetro e respeitando o numero de níveis informado, no caso, é a hierarquia do RH, ou seja, tabela VHIERARQUIA

PAR. 1 - Número de níveis a buscar [inteiro]

PAR. 2 - Texto contendo coligada e ID da hierarquia separados por ; [texto]

Exemplo: RETORNAPROXIMAHIERARQUIARH(1, '1;2')

Nesse exemplo, foi solicitado a hierarquia imediatamente superior (1 no primeiro parâmetro) a hierarquia de código 2 da coligada 1, supondo que a hieraquia imediatamente superior a de código 2, for da coligada 1 e código 3, o retorno será: '1;3'

**RETORNAPROXIMOATENDENTEHIERARQUIARH**

Retorna o atendente da próxima hierarquia da requisição que está associado ao atendimento de acordo com o número de níveis informado como parâmetro. Para usar essa fórmula, é necessário que o atendimento esteja associada a um requisição do RH.

PAR. 1 - Número de níveis a buscar [inteiro]

Exemplo RETORNAPROXIMOATENDENTEHIERARQUIARH(1)

Nesse exemplo, foi solicitado o atendente da hierarquia imediatamente superior a requisição associada ao atendimento, supondo que esse atendente seja da coligada 1 e de código 5, o retorno será: '1;5'

**RETORNAPROXIMOCHEFEHIERARQUIASECAOLABORE**  
Retorna o código do Chefe do atendente atual da requisição, se baseando na hierarquia de seções do TOTVS RH (Linha RM). Esta função de fórmula não reconhece Chefe de outra coligada.

PAR. 1 - Retornar somente chefe (1 sim, 0 não) [inteiro]

**RETORNAPROXIMOCHEFESECAOLABORE**  
Retorna o código do atendente do chefe pelo atendente responsável pelo atendimento utilizando a hierarquia de seções do RMLabore.

PAR. 1 - CodSecao - Código da Seção em que o funcionário deve ser chefe.  
PAR. 2 - CodFuncao - Código da Função que este funcionário deve ter.

**RETPROXIMOCHEFEINTERNOSECAOLABORE**  
Retorna o código de atendente do chefe interno do atendente responsável pelo atendimento utilizando a hierarquia de seções do RMLabore.

É importante observar que serão listados somente chefes internos.

PAR. 1 - Nível - Número de níveis de chefia a ser verificado em relação ao atendente responsável pela abertura do atendimento.

**RETPROXIMOCHEFESECAOLABORE**  
Retorna o código de atendente do chefe do atendente responsável pelo atendimento utilizando a hierarquia de seções do RMLabore.

É importante observar que a prioridade serão os chefes externos, somente depois de todos os chefes externos das hierarquias superiores à do atendente responsável pelo atendimento, serão listados os chefes internos.

PAR. 1 - Nível - Número de níveis de chefia a ser verificado em relação ao atendente responsável pela abertura do atendimento.

**SECAOORIGEMREQUISICAO**  
Retorna o código de seção de origem da requisição.

PAR. 1 - Código da coligada da requisição [inteiro]  
PAR. 2 - Identificador (ID) da requisição [inteiro]

**SECAOPAI**  
Busca a seção pai a partir de uma seção de referência em uma quantidade de níveis solicitado.

PAR. 1 - Código da coligada da seção [inteiro]  
PAR. 2 - Código da seção de referência [texto]  
PAR. 3 - Nível para buscar a seção pai [inteiro]

**SETVAR**  
Atribui um valor a uma variável

PAR. 1 - Variável [var]  
PAR. 2 - Valor [object]

**STATUSCONCLUSAOETAPA**  
Retorna o status (texto) de conclusão da etapa. Só funciona se usada em uma fórmula dentro da etapa.

**STR**  
Retorna número de acordo com máscara informada

PAR. 1 - Valor  
PAR. 2 - Mascará

**STRLEFT**  
Copia o lado DIREITO de um string (texto) um número de caracteres (quantidade)

PAR. 1 - Texto [texto]  
PAR. 2 - Quantidade [inteiro]

**STRRIGHT**  
Copia o lado ESQUERDO de um string (texto) um número de caracteres (quantidade)

PAR. 1 - Texto [texto]  
PAR. 2 - Quantidade [inteiro]

**SUBSTR**  
Copia a partir da posição início um número de caracteres de texto

PAR. 1 - Texto [texto]  
PAR. 2 - Início [inteiro]  
PAR. 3 - Quantidade [inteiro]

**SUBTRAIDATAS**  
Retorna a subtração entre duas datas

PAR. 1 - Data1 [data]  
PAR. 2 - Data2 [data]

**TABCOLIGADA**  
Retorna o valor de uma Coluna da tabela GCOLIGADA da coligada corrente que o usuário tem acesso na GPERMISS    TABCOLIGADA

PAR. 1 - Coluna [texto]  
PAR. 2 - Sistema [texto]

**TAMSTR**  
Retorna o tamanho da string

PAR. 1 - Texto [texto]

**TETO**  
Retorna o valor truncado mais um

PAR. 1 - Valor [decimal]

**TIPOATENDENTE**  
Retorna o tipo do atendente que foi informado como parâmetro.

PAR. 1 - Código do atendente [inteiro]

**TIPOCLIENTE**  
Retorna o tipo do cliente do atendimento. Os possíveis tipos de retorno são:'P', 'C', 'T', 'A' ou 'R' para respectivamente Pessoa, Cliente, Prospect, Aluno ou Professor.

**TRUNCVALOR**  
Trunca um valor com casas decimais

PAR. 1 - Valor [decimal]  
PAR. 2 - Casas [inteiro]

**ULTDIAMES**  
Retorna o último dia do mês de uma data

PAR. 1 - Data [data]

**USUARIOCORRENTE**  
Usuário logado no sistema.

**VAL**  
Converte um string para valor

PAR. 1 - Valor [texto]

Exemplos de Fórmulas

**Define qual grupo receberá o atendimento dependendo de um parâmetro do atendimento**  
   
SE CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "Delphi Win32" ENTAO  
  215  
SENAO  
  193  
FIMSE

**Executa uma SQL**  
   
Decl Texto;  
SE EXECSQL('03.000047') = VERDADE ENTAO  
  SETVAR(b,RESULTSQL ( '03.000047' , 'Texto'))  
FIMSE;

**Envia um atendimento para um usuário específico**  
   
CodColigada;Codatendente.  
 Ex.: "1;215"

**Conclui um Atendimento:**  
   
SE CAMPOSATENDIMENTO ( 'CODSTATUS' ) <> 'R' ENTAO  
  CONCLUIRARESPONDER  
FIMSE;  
   
CONCLUIDORESPONDIDO

**Repassar atendimento para atendente anterior**  
   
REPASSARDEVOLTA ( 10 )

**Definir Etapa do atendimento na abertura do mesmo**  
   
SE TIPOATENDENTE ( CODATENDENTERESPONSAVEL ) = 4 ENTAO  
  AVANCARETAPAATENDIMENTO(1); /\* STE \*/  
SENAO  
  AVANCARETAPAATENDIMENTO(2); /\* PDE \*/  
FIMSE;  
RetNAOREPASSA  
Repassa para a etapa anterior  
AVANCARETAPAATENDIMENTO ( CAMPOSATENDIMENTO ( 'CODTAREFAANTERIOR' )  )

**Etapa Abertura**  
   
FOR('06.00015');  /\* ATUALIZAÇÃO DE CAMPOS DEFAULT \*/  
   
SE (CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00017") ENTAO /\* TEC-DOCUMENTAÇÃO \*/  
  AVANCARETAPAATENDIMENTO(167) /\* teste funcional \*/  
SENAO  
  SE TIPOATENDENTE ( CODATENDENTERESPONSAVEL ) = 14 ENTAO /\* EQUIPE DO MSCRM \*/  
    AVANCARETAPAATENDIMENTO ( 164 ) /**Etapa de Entendimento PDE**/  
  SENAO  
    SE (CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "WebForms.NET" OU CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "WinForms.NET") E   
       (CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00002" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00047" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00048" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00049" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00025" ) ENTAO  
      AVANCARETAPAATENDIMENTO ( 164 ) /**Etapa de Entendimento PDE**/  
    SENAO /\* SE FOR PORTUGAL E MELHORIA OU IMPLEMENTAÇÃO \*/  
      SE (CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00002" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00047" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00048" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00049" OU CAMPOSATENDIMENTO('CODCLASSIFICACAO')= "00025" ) E  FOR("W.T.29") = "Sim" ENTAO  
        AVANCARETAPAATENDIMENTO ( 164 ) /**Etapa de Entendimento PDE**/  
      SENAO  
        SE TIPOATENDENTE ( CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )  ) = 6 E (FOR("05.00031") = VERDADE ) ENTAO /\* QUALQUER ATENDIMENTO ABERTA PELO QSW \*/  
          AVANCARETAPAATENDIMENTO(167) /\* teste funcional \*/  
        SENAO  
          SE TIPOATENDENTE ( CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )  ) = 6 E (FOR("05.00032") = VERDADE) ENTAO /\* QUALQUER ATENDIMENTO ABERTA PELO QSW \*/  
            AVANCARETAPAATENDIMENTO(356) /\* HELP \*/  
          SENAO  
            SE CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00044"  ENTAO /\* Caso de Teste \*/  
              AVANCARETAPAATENDIMENTO(223) /\* Caso de Teste \*/  
            SENAO  
              AVANCARETAPAATENDIMENTO ( 161 ) /**Etapa de Entendimento STE**/  
            FIMSE  
          FIMSE  
        FIMSE  
      FIMSE  
    FIMSE  
  FIMSE  
FIMSE;  
   
SE (TIPOATENDENTE ( CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )  ) = 4) OU (TIPOATENDENTE ( CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )  ) = 5) OU (CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )   = 2738 ) OU /\* USUARIO AGILIS \*/ (TIPOATENDENTE ( CAMPOSATENDIMENTO ( 'CODATENDENTERESP' )  ) = 18) ENTAO  
  DEFINECONTAOCLIENTE ( CODATENDENTERESPONSAVEL )  
FIMSE;  
   
RetNAOREPASSA

**Etapa Implementação**  
   
for("06.00050"); /\* verifica se a classificacao está ativa \*/  
for("07.00104"); /\* Campos defaults do First \*/  
for("05.00008"); /\* Exige preenchimento do percentual de conclusão \*/  
for("06.00007"); /\* Não permite o repasse de oc TEC-HOMOLOGAÇÃO \*/  
for("06.00022"); /\* Valida preenchimento de campos \*/  
for("06.00026"); /\* Valida o prazo limite com o prazo da versão \*/  
for("05.00007"); /\* Cria ocorrência de caso de teste \*/  
for("06.00046"); /\* Caso não seja bug, valida campos \*/  
for("03.00806"); /\* Atribui a e espec. necess como sim, caso seja oc de .net \*/  
for("07.00106"); /\* Valida se a ocorrência é de melhoria futura \*/  
   
/\* Avança etapa da ocorrência filha para a mesma etapa da oc PAI \*/  
SE for("06.00042") = VERDADE ENTAO  
  RetNAOREPASSA   
SENAO  
  SE ((CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "WebForms.NET" OU CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "WinForms.NET" OU CAMPOSATENDIMENTO ( 'PARAMETRO.Tipo de Requisito' ) = "Delphi Win32") E  
      CAMPOSATENDIMENTO ( 'CODTAREFA' ) <> 242 e CAMPOSATENDIMENTO ( 'CODTAREFA' ) <> 173 E CAMPOSATENDIMENTO ( 'CODTAREFA' ) <> 174) E CAMPOSATENDIMENTO ( 'Parametro.Especificação Necessária') = "Sim" ENTAO   
    AVANCARETAPAATENDIMENTO ( 173 )   /\*ETAPA DE ESPECIFICAÇÃO \*/  
  SENAO  
    SE EXECSQL ( '03.000054' ) <> VERDADE E CAMPOSATENDIMENTO ( 'Parametro.Script') = "Sim" ENTAO  
      INTERROMPE ( 'Favor cadastrar uma ocorrência de criação de script vinculada a esta!' )  
    SENAO /\* SE O REQUISITO IMPACTAR EM LOCALIZAÇÃO ENTAO ENVIA PARA ETAPA DE PROP. LOCALIZAÇÃO \*/  
      SE FOR("06.00025") = VERDADE E CAMPOSATENDIMENTO ( 'CODTAREFA' ) <> 242 ENTAO  
        AVANCARETAPAATENDIMENTO ( 242 )  
      SENAO /\* caso já exista alguém definido na aba parametro, a preferência é dele \*/  
        SE concatena(CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Implementação'),'','') <> '' ENTAO  
          CONCATENA('1',CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Implementação'),';')  
        SENAO  
          "" /\*ATENDENTE CORRENTE \*/  
        FIMSE  
      FIMSE  
    FIMSE  
  FIMSE  
FIMSE

**Admissão**  
 

Etapa Inicial  
Decl a, b, c, d;  
   
SETVAR ( a, '' );  
SETVAR ( b, '' );  
SETVAR ( c, '' );  
SETVAR ( d, 'Relações Humanas - Workflow Admissão ' );  
   
SE EXECSQL ( '03.000150' ) = VERDADE  
      ENTAO SETVAR ( a, RESULTSQL ( '03.000150' , 'email' ) )  
FIMSE;  
SE EXECSQL ( '03.000151' ) = VERDADE  
      ENTAO SETVAR ( b, RESULTSQL ( '03.000151' , 'mensagem' ) )  
FIMSE;  
SE EXECSQL ( '03.000152' ) = VERDADE  
      ENTAO SETVAR ( c, RESULTSQL ( '03.000152' , 'funcionario' ) )  
FIMSE;  
ENVIAEMAIL ( 'rh@[rm.com.br](http://rm.com.br)' , a , '' , concat ( d, c ), b ,  1 );  
"1307"  
–  
DECL USUARIO;  
   
CONCLUIRARESPONDER;  
   
SE EXECSQL('03.000154') = VERDADE ENTAO  
  SETVAR(USUARIO,RESULTSQL ( '03.000154' , 'CodAtendente' ));  
  REPASSARATENDIMENTO ( USUARIO, '' , 10 , '' , '' )  
FIMSE;  
   
RetNAOREPASSAATULIZARESTANTE  
–  
ALTERARCAMPOATENDIMENTO ( "CODCOLIGPRD=1;CODPRODUTO=140" );  
decl a, b;  
   
setvar ( a, '' );  
setvar ( b, '' )  
–  
Decl a, b, c, d;  
   
SETVAR ( a, '' );  
SETVAR ( b, '' );  
SETVAR ( c, '' );  
SETVAR ( d, 'Relações Humanas - Workflow Admissão ' );  
   
SE EXECSQL ( '03.000150' ) = VERDADE  
      ENTAO SETVAR ( a, RESULTSQL ( '03.000150' , 'email' ) )  
FIMSE;  
SE EXECSQL ( '03.000151' ) = VERDADE  
      ENTAO SETVAR ( b, RESULTSQL ( '03.000151' , 'mensagem' ) )  
FIMSE;  
SE EXECSQL ( '03.000152' ) = VERDADE  
      ENTAO SETVAR ( c, RESULTSQL ( '03.000152' , 'funcionario' ) )  
FIMSE;  
ENVIAEMAIL ( 'rh@[rm.com.br](http://rm.com.br)' , a , '' , concat ( d, c ), b ,  1 );  
   
Decl x;  
SETVAR(x, '');  
SE EXECSQL('03.000155') = VERDADE ENTAO  
  SETVAR(x,RESULTSQL ( '03.000155' , 'mensagem'))  
FIMSE;  
   
ENVIAEMAIL ( 'rh@[rm.com.br](http://rm.com.br)' , 'patricia.almeida@[totvs.com.br](http://totvs.com.br); [juliane.paula@totvs.com.br](mailto:juliane.paula@totvs.com.br)' , '' , 'WorkFlow Admissão - Dados do Novo Usuário' , x ,  1)

**Etapa Cria atendimento de documentação**  
   
DECL H, A, P, V, R;  
SETVAR(A,0);  
SETVAR(P, 357);  
SETVAR(V, CONCATENA(';PARAMETRO.Versão de liberação=', CAMPOSATENDIMENTO ( 'PARAMETRO.Versão de liberação'),''));  
SETVAR(R, CONCATENA(';PARAMETRO.Requisito=', CAMPOSATENDIMENTO ( 'PARAMETRO.Requisito'),''));   
SE CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Homologação' ),'','') <> '' ENTAO  
  SETVAR(A, CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Homologação' ) )  
FIMSE;  
   
/\* BUSCA O ATENDENTE DO GRUPO PARA REPASSAR OCORRÊNCIA \*/  
SE EXECSQL('03.000298') = VERDADE E A < 1 ENTAO  
  SETVAR(A, RESULTSQL('03.000298', 'CODATENDENTEFIXO'))  
FIMSE;  
   
SE A = 0 ENTAO  
  SETVAR(A,CODATENDENTERESPONSAVEL)  
FIMSE;  
   
SETVAR(H,CONCATENA('CODTIPOATENDIMENTO=62;CODCLASSIFICACAO=00050;CODCFO=007622;

                                        IDCONTATO=;CODTAREFAANTERIOR=;CODATENDENTERESP=',A,''));  
SETVAR(H,CONCATENA(H, P, ';CODTAREFA='));  
SETVAR(H,CONCATENA(H, V, ''));  
/\*Concatenando o código do Requisito \*/  
SETVAR(H,CONCATENA(H, R, ''));  
   
/\*cria uma cópia do atendimento do contexto se não tiver outra criada \*/  
SE  EXECSQL('03.000299') = FALSO ENTAO  
  CRIARCOPIAATENDIMENTO (   CAMPOSATENDIMENTO ( 'CODCOLIGADA' ),  CAMPOSATENDIMENTO ( 'CODLOCAL' ) , CAMPOSATENDIMENTO ( 'CODATENDIMENTO' ), H,  1)  
FIMSE;

**Etapa Solucionado com Versão Específica**  
   
Decl a, b, t;  
   
/\* Impede a continuidade da ocorrênica se a classificação for igual TEC-A CLASSIFICAR \*/  
SE CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00000" ENTAO  
  INTERROMPE ("Favor alterar a classificação da ocorrência!" )  
FIMSE;  
   
SETVAR(a, '');  
SETVAR(b, '');  
SETVAR(t, Concatena('Sr. Analista, favor criar nova ocorrência baseada na de número ', CAMPOSATENDIMENTO ( 'CODATENDIMENTO' ), '' ) );  
   
SE EXECSQL('03.000069') = VERDADE ENTAO  
  SETVAR(a, RESULTSQL ( '03.000069' , 'email'))  
FIMSE;  
   
SE EXECSQL('03.000070') = VERDADE ENTAO  
  SETVAR(b, RESULTSQL ( '03.000070' , 'email'))  
FIMSE;  
   
AVANCARETAPAATENDIMENTO ( 177 ) ;  
   
ENVIAEMAIL('[suporte.rm@totvs.com.br](mailto:suporte.rm@totvs.com.br)' , CONCATENA(a,b,',') , '' , 'Finalização de ocorrência Solucionada com Versão Específica' ,t ,  1) ;

**Etapa Apresentar Proposta de Entendimento**  
   
/\* VERIFICA SE O CAMPO ENTENDIMENTO ESTÁ  PREENCHIDO \*/  
SE EXECSQL("03.000090") = VERDADE E RESULTSQL("03.000090", "QTD") = 0 ENTAO  
  INTERROMPE("Favor preencher o entendimento!")  
FIMSE;  
   
CONCATENA ( 1 , CODATENDENTECONTATOCOMCLIENTE , ';' )

**Etapa Não aceitar Agendamento e voltar etapa**  
   
COLOCAREMANDAMENTO;  
/\*devido a problemas no .net, não pode usar avançaretapa \*/  
ALTERARCAMPOATENDIMENTO  
 ( concatena('CODTAREFA=',CAMPOSATENDIMENTO ( 'PARAMETRO.CODTAREFAANTERIOR' ),'' ) );  
REPASSARATENDIMENTO ( CAMPOSATENDIMENTO ( 'PARAMETRO.CODATENDENTEANTERIOR' ) , '' , 20 , '' , '' );  
   
RetNAOREPASSA

**Retorna Superior Imediato**  
   
CHEFEIMEDIATORESPATENDIMENTO

**Retorna Grupo PDE**  
   
DECL N;  
   
SE (CAMPOSATENDIMENTO ("CODCLASSIFICACAO") = "00005") ENTAO /\* INT - INSTALACAO DO APLICATIVO \*/  
  SETVAR(N,"253") /\* GROSSI \*/  
SENAO  
  SE (CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduPS.11" OU CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduPS.9" OU CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduWf.Sel" OU CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduEb.Sel") ENTAO  
    SETVAR(N,"221") /\* EDUARDO BELO **/ /** PROCESSO SELETIVO\*/  
  SENAO  
    SE (CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduEB.014" ou CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "Edu.013" ou CAMPOSATENDIMENTO ( 'CODITEMPRD' ) = "EduES.014") E (CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00000" OU CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00001" OU CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00003") ENTAO   
      SETVAR(N,"235") /\* Luiz Antonio \*/  
    SENAO  
      SE (CAMPOSATENDIMENTO ( 'CODPRODUTO' ) = 39 OU CAMPOSATENDIMENTO ( 'CODPRODUTO' ) = 43) E CAMPOSATENDIMENTO ( 'CODITEMPRD' ) <> "EduEb.014" E CAMPOSATENDIMENTO ( 'CODITEMPRD' ) <> "EduEs.014" E (CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00000" OU CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00001" OU CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00003") ENTAO  
        SETVAR(N,"35") /\* SADE \*/  
      SENAO   
        SE (CAMPOSATENDIMENTO ( 'CODPRODUTO' ) = 39 OU CAMPOSATENDIMENTO ( 'CODPRODUTO' ) = 43 OU CAMPOSATENDIMENTO ( 'CODPRODUTO' ) = 50) ENTAO  
          SETVAR(N,"36") /\* RAFAEL \*/  
        SENAO   
          SE CAMPOSATENDIMENTO ( 'CODITEMPRD' )  =  "Fop.1.4.1.91" ENTAO  
            SETVAR(N,"258") /\* Eliane \*/  
          SENAO   
            SE CAMPOSATENDIMENTO ( 'CODITEMPRD' )  =  "Fop.1.4.1.92" ENTAO  
              SETVAR(N,"312") /\* Guilherme \*/  
            SENAO  
              SETVAR(N, FOR("05.00028"))  
            FIMSE  
          FIMSE  
        FIMSE  
      FIMSE  
    FIMSE  
  FIMSE  
FIMSE;  
   
SE N = '0' ENTAO  
  SETVAR(N,"")  
FIMSE;  
   
N

**Agenda Atendimento**  
   
DECL Motivo;  
   
SETVAR(Motivo, FOR("06.00005") ); /**Motivo de Repasse**/  
   
SE CONCATENA(CAMPOSATENDIMENTO ( 'AGENDADOPARA' ),'','') = '12:00:00 AM' E (CAMPOSATENDIMENTO  ( "PARAMETRO.Tipo de Lib. de Versão" ) = "Específica" ou CAMPOSATENDIMENTO  ( "PARAMETRO.Tipo de Lib. de Versão" ) = "Patch") ENTAO  
  AGENDARARESPONDER (CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Data para Despertar' ),'',''), CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Data Prazo Limite'),'',''), Motivo , CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Motivo de Agendamento'),CAMPOSATENDIMENTO  ( "PARAMETRO.Tipo de Lib. de Versão" ),'-' ) )  
SENAO  
  SE CONCATENA(CAMPOSATENDIMENTO ( 'AGENDADOPARA' ),'','') = '' ou CONCATENA(CAMPOSATENDIMENTO ( 'AGENDADOPARA' ),'','') = '12:00:00 AM' ENTAO  
    AGENDARARESPONDER (CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Data para Despertar' ),'',''), CONCATENA(FOR("06.00004"),'',''), Motivo , CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.Motivo de Agendamento'),'Normal','-') )  
  FIMSE  
FIMSE;

**Etapa Confirmar Agendamento e enviar para Etapa Anterior**  
   
for("06.00049"); /\* agenda o atendimento, caso não tenha sido feito ainda \*/  
   
SE CAMPOSATENDIMENTO ( 'CODSTATUS' ) = 'G' ENTAO  
  AGENDADORESPONDIDO  
FIMSE;  
   
SE CONCATENA(CAMPOSATENDIMENTO ( 'AGENDADOPARA' ),'','') = '' ENTAO  
  COLOCAREMANDAMENTO;  
  INTERROMPE('Favor cadastrar a data de despertamento')  
FIMSE;  
   
SE CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.CODTAREFAANTERIOR' ),'','') = '215' OU CONCATENA(CAMPOSATENDIMENTO ( 'PARAMETRO.CODTAREFAANTERIOR' ),'','') = '172' ENTAO  
  COLOCAREMANDAMENTO;    
  INTERROMPE('Erro de agendamento, favor procurar o Juliano!')  
FIMSE;  
   
ALTERARCAMPOATENDIMENTO ( 'CODSTATUS=A' );  
ALTERARCAMPOATENDIMENTO ( concatena('CODTAREFA=', CAMPOSATENDIMENTO ( 'PARAMETRO.CODTAREFAANTERIOR' ), '') );  
SE (CONCATENA( CAMPOSATENDIMENTO ( 'PARAMETRO.CODATENDENTEANTERIOR' ),'','') <> '') ENTAO  
  REPASSARATENDIMENTO ( CAMPOSATENDIMENTO ( 'PARAMETRO.CODATENDENTEANTERIOR' ) , '' , -1 , '' , '' )  
FIMSE;  
    
ALTERARCAMPOATENDIMENTO ( 'CODSTATUS=E' ); /\* devido a falha  no .net, obraga-se \*/  
   
RetNAOREPASSA

**Obriga o preenchimento do campo percentual**  
   
/\* verifica se na etapa atual foi apontado 100 % de conclusão \*/  
DECL T, Q, B, ETAPA;  
SETVAR(T, 0);  
/\* retorna % de completude \*/  
SE EXECSQL( '03.000057' ) = VERDADE ENTAO  
  SETVAR(T, RESULTSQL ( '03.000057' , 'VALOR' ) )  
FIMSE;  
   
/\* retorna o total apontado\*/  
SE EXECSQL( '03.000073' ) = VERDADE ENTAO  
  SETVAR(Q, RESULTSQL ( '03.000073' , 'VALOR' ) )  
FIMSE;  
   
/\* retorna o total apontado nas etapas de entedimnto, implementação, especifcação e planejamento\*/  
SE EXECSQL( '03.000107' ) = VERDADE ENTAO  
  SETVAR(B, RESULTSQL ( '03.000107' , 'VALOR' ) )  
FIMSE;  
   
SETVAR(ETAPA, "NAO");  
/\* Impede a continuidade da ocorrênica se a classificação for igual TEC-A CLASSIFICAR \*/  
SE CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00000" ENTAO  
  INTERROMPE ("Favor alterar a classificação da ocorrência!" )  
FIMSE;  
   
/\* Verifica se a etapa atual necessidade de apontamento na tabela dinâmica e não é bug(Retirado por Juliano o teste se é Bug\*/  
SE  T < 100 E EXECSQL('03.000063') = VERDADE E ETAPA <> "SIM" ENTAO  
  INTERROMPE ("Para avançar de etapa é necessário apontar 100% de conclusão da mesma!" )  
FIMSE;  
   
/\* Verifica se a etapa atual necessidade de apontamento na tabela dinâmica \*/  
SE  /**CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) <> '00001' Juliano e**/ Q <= 0 E EXECSQL('03.000063') = VERDADE ENTAO  
  INTERROMPE ("Favor apontar a quantidade de horas gastas na ocorrência (não pode ser 0)!" )  
FIMSE;  
   
/\* Verifica na saída da implementação, se ocorreu algum apontamento nas etapas de especf., impl., planejamento e entendimento\*/  
SE  CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = '00001' e B <= 0 E CAMPOSATENDIMENTO ( 'CODTAREFA' ) = 166 ENTAO  
  INTERROMPE ("Favor apontar a quantidade de horas gastas na ocorrência (não pode ser 0)!" )  
FIMSE;

**Retorna analista do campo Responsável pela Implementação**  
   
DECL A;  
SETVAR(A, "");  
   
/\* caso já exista alguém definido na aba parametro, a preferência é dele \*/  
SE concatena(CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Implementação'),'','') <> '' ENTAO  
  SETVAR(A, CONCATENA('1',CAMPOSATENDIMENTO ( 'PARAMETRO.Responsável pela Implementação'),';'))  
SENAO  
  SETVAR(A, FOR("05.00002") )  
FIMSE;  
   
A

**Retorna Próximo Chefe**  
   
DECL CODPROXCHEFE;  
   
SETVAR(CODPROXCHEFE,  RETPROXIMOCHEFESECAOLABORE ( 1 ));  
SE CODPROXCHEFE = '-1' ENTAO  
  AVANCARETAPAATENDIMENTO ( 303 )  
SENAO  
  CODPROXCHEFE  
FIMSE

**Repassar chefe seção destino**  
   
DECL PRIMEIRAETAPA;  
   
SETVAR (PRIMEIRAETAPA, CAMPOSATENDIMENTO('CODTAREFA'));  
SE PRIMEIRAETAPA = 0 ENTAO  
  DECL CODSECAO;  
  EXECSQL ('VISQL01' );  
  SETVAR(CODSECAO,resultsql('VISQL01','CODSECAO'));  
  RETORNAPROXIMOCHEFESECAOLABORE ( CODSECAO ,'-1' )  
SENAO  
  DECL CODPROXCHEFE;  
  SETVAR(CODPROXCHEFE,  
  RETPROXIMOCHEFESECAOLABORE ( 1 ));  
  SE CODPROXCHEFE = '-1' ENTAO  
    AVANCARETAPAATENDIMENTO ( 348  )  
  SENAO  
    CODPROXCHEFE  
  FIMSE  
FIMSE

**Conclusão**  
   
FOR("03.00507");  
   
SE EXECSQL ( '03.000052' ) <> VERDADE ENTAO  
  INTERROMPE ( 'Preencha o campo Solução!' )  
FIMSE;  
   
SE CAMPOSATENDIMENTO ( 'CAIXAPOSTAL' ) > 0 ENTAO  
  INTERROMPE ( 'Ainda existem mensagens na sua caixa postal de voz. Caso já as tenha ouvido, zere o valor do campo Caixa Postal.' )  
FIMSE;  
   
ALTERARCAMPOATENDIMENTO ( 'CODSTATUS=R' ) ;  
   
CONCLUIDORESPONDIDO

**Solucionar Atendimentos**  
   
FOR("03.00507");  
SE CAMPOSATENDIMENTO ( 'CODTIPOATENDIMENTO' ) <> 29 e CAMPOSATENDIMENTO ( 'CODTIPOATENDIMENTO' ) <> 23 E  CAMPOSATENDIMENTO ( 'CODCLASSIFICACAO' ) = "00000" ENTAO  
  INTERROMPE ( 'Não é possível concluir atendimento com a classificação: "A Classificar"' )  
SENAO  
  CONCLUIRARESPONDER  
FIMSE

**Repassar para o Contato com o Cliente**  
   
REPASSARATENDIMENTO (CODATENDENTECONTATOCOMCLIENTE , '' , 9 , '' , '' )

**Exemplos** **de fórmulas complexas de repasse**  
   
**Etapas:**  
            (Código - descrição - para quem esta repassando)  
   
            32 - Enviar para RH --> grupo  
33 - Enviar para Chefe Imediato ou solicitante --> formula tstAume2  
34 - concluir --> formula VIFRM02  
35 - reprovar --> formula VIFRM02  
36 - chefe imediato --> formula tstAumen  
56 - solicitante --> formula tstSolic  
   
   
**Fluxos:**  
            Enviar para RH --> Em Análise --> Enviar para RH  
            Enviar para RH --> Recusada --> Enviar para Chefe Imediato ou solicitante  
            Enviar para RH --> Cancelada --> Reprovar  
            Enviar para RH --> Aprovar --> Chefe Imediato  
            Chefe Imediato --> Aprovar -->  Chefe Imediato  
            Chefe Imediato --> Reprovar --> Reprovar  
            Enviar para Chefe Imediato ou solicitante --> Aprovar --> Chefe Imediato  
            Enviar para Chefe Imediato ou solicitante --> Reprovar --> Reprovar  
            Concluir --> Concluir em definitivo --> Concluir  
            Solicitante --> Aprovar --> Enviar para Chefe Imediato ou solicitante  
            Reprovar --> Reprovar --> Reprovar  
   
**Fórmulas utilizadas nas etapas:**  
           **tstAume2:**  
        se execsql('AumentoQuadro3') = verdade entao  
          /**interrompe(resultsql('AumentoQuadro3','ATENDENT'));**/  
          REPASSARATENDIMENTO ( resultsql('AumentoQuadro3','ATENDENT') , '' , 3 , '' , '' )  
        senao  
          execsql('AumentoQuadro1');  
          RETORNAPROXIMOCHEFESECAOLABORE (resultsql('AumentoQuadro1','CODSECAO'), '-1')  
        fimse  
   
 **tstAumen:**  
        se execsql('AumetoQuadro2') = verdade entao  
          AVANCARETAPAATENDIMENTO ( 34 )  
        senao  
          execsql('AumentoQuadro1');  
          RETORNAPROXIMOCHEFESECAOLABORE (resultsql('AumentoQuadro1','CODSECAO'), '-1')  
        fimse  
   
 **VIFRM02:**  
        DECL CODATENDCONTATOCLIENTE;  
        SETVAR(CODATENDCONTATOCLIENTE, CODATENDENTECONTATOCOMCLIENTE);  
   
        DECL COLIGADAATENDENTE;  
        SETVAR(COLIGADAATENDENTE, CAMPOSATENDENTE(CODATENDCONTATOCLIENTE, 'CODCOLIGADA' ));  
   
        DECL TXTUPDCOLIGADA;  
        SETVAR(TXTUPDCOLIGADA, CONCATENA('CODCOLIGADARESP=',  COLIGADAATENDENTE, ''));  
   
        DECL TXTUPDCODATENDENTE;  
        SETVAR(TXTUPDCODATENDENTE, CONCATENA('CODATENDENTERESP=',  CODATENDENTECONTATOCOMCLIENTE, ''));  
   
        ALTERARCAMPOATENDIMENTO ( CONCATENA(TXTUPDCOLIGADA, TXTUPDCODATENDENTE, ';') );  
   
        CONCLUIDORESPONDIDO  
 **tstSolic:**  
        DECL CODATENDCONTATOCLIENTE;  
        SETVAR(CODATENDCONTATOCLIENTE, CODATENDENTECONTATOCOMCLIENTE);  
   
        DECL COLIGADAATENDENTE;  
        SETVAR(COLIGADAATENDENTE, CAMPOSATENDENTE(CODATENDCONTATOCLIENTE, 'CODCOLIGADA' ));  
   
        DECL TXTUPDCOLIGADA;  
        SETVAR(TXTUPDCOLIGADA, CONCATENA('CODCOLIGADARESP=',  COLIGADAATENDENTE, ''));  
   
        DECL TXTUPDCODATENDENTE;  
        SETVAR(TXTUPDCODATENDENTE, CONCATENA('CODATENDENTERESP=',  CODATENDENTECONTATOCOMCLIENTE, ''));  
   
        ALTERARCAMPOATENDIMENTO ( CONCATENA(TXTUPDCOLIGADA, TXTUPDCODATENDENTE, ';') )  
   
   
**SQLs - AumentoQuadro3, AumentoQuadro1, AumetoQuadro2**  
 **AumentoQuadro3:**  
        --> Verifica se o atendente é ponto de aprovação.  
        SELECT HATENDENTE.CODATENDENTE AS ATENDENT  
        FROM  VREQAUMENTOQUADRO  
              LEFT JOIN PFUNC ON (VREQAUMENTOQUADRO.CODCOLREQUISICAO = PFUNC.CODCOLIGADA AND VREQAUMENTOQUADRO.CHAPAREQUISITANTE = PFUNC.CHAPA)  
              LEFT JOIN HATENDENTE ON (PFUNC.CODCOLIGADA = HATENDENTE.CODCOLIGADA AND PFUNC.CODPESSOA = HATENDENTE.CODPESSOA)  
              LEFT JOIN PFCOMPL ON (VREQAUMENTOQUADRO.CODCOLREQUISICAO = PFCOMPL.CODCOLIGADA AND VREQAUMENTOQUADRO.CHAPAREQUISITANTE = PFCOMPL.CHAPA)  
        WHERE     PFCOMPL.SIMNAO = '01'  
              AND VREQAUMENTOQUADRO.IDREQ = :FRM\_VIFRM04  
   
 **AumentoQuadro1:**  
        --> retorna o chefe imediato  
        SELECT PSUBSTCHEFE.CODSECAO  
        FROM   VREQAUMENTOQUADRO, PSUBSTCHEFE  
        WHERE      VREQAUMENTOQUADRO.IDREQ                     =  :FRM\_VIFRM04  
               AND VREQAUMENTOQUADRO.CODCOLREQUISICAO =  PSUBSTCHEFE.CODCOLIGADA  
               AND PSUBSTCHEFE.CODSECAO                             <> VREQAUMENTOQUADRO.CODSECAO  
               AND PSUBSTCHEFE.CODSECAO NOT IN (SELECT CODSECAO FROM PSUBSTCHEFE WHERE CHAPASUBST = VREQAUMENTOQUADRO.CHAPAREQUISITANTE)  
               AND SUBSTRRING(VREQAUMENTOQUADRO.CODSECAO,1,LEN(PSUBSTCHEFE.CODSECAO)) = PSUBSTCHEFE.CODSECAO  
               AND PSUBSTCHEFE.CHAPASUBST  NOT IN (SELECT PFUNC.CHAPA  
                                                              FROM  PFUNC  
                                                                    LEFT JOIN HATENDENTE ON (PFUNC.CODPESSOA = HATENDENTE.CODPESSOA AND PFUNC.CODCOLIGADA = HATENDENTE.CODCOLIGADA)  
                                                              WHERE HATENDENTE.CODATENDENTE = :FRM\_tstAtend)  
        ORDER BY LEN(PSUBSTCHEFE.CODSECAO) DESC  
   
     **AumetoQuadro2:**  
        -->  
        select 1 as pontoaprovacao:  
        from VREQAUMENTOQUADRO A  
             join HATENDIMENTOEXT B on (B.CODCOLIGADA = A.CODCOLREQUISICAO and B.CODATENDIMENTO = A.CODATENDIMENTO)  
             join HATENDENTE C on (C.CODCOLIGADA = B.CODCOLIGADA and C.CODATENDENTE = B.CODATENDENTERESP)  
             join PFUNC D on (D.CODCOLIGADA = C.CODCOLIGADA and D.CODPESSOA = C.CODPESSOA)  
             join PFCOMPL E on (E.CODCOLIGADA = D.CODCOLIGADA and E.CHAPA = D.CHAPA)  
        where  
                IDREQ = :FRM\_VIFRM04  
                AND C.CODATENDENTE = :FRM\_tstAtend  
                AND E.SIMNAO = '01'  
   
:FRM\_VIFRM04 --> GETIDDAREQUISICAO  
:FRM\_tstAtend --> CODATENDENTERESPONSAVEL
