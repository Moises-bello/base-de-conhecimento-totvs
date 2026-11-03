---
content_hash: 347370363bf6f7fb881237422a0cc94b431235ed577e338a7eb3548a49766cfb
fetched_at: '2026-06-29T00:09:32.515479+00:00'
page_id: '425458864'
product: rm
source: tdn-rm
title: Mensagens de Notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458864
version: 96
---

As mensagens de notificação, permitem a configuração de um texto padrão para possibilitar o envio da notificação via e-mail, Fluig e eduCONNECT, para alunos, professores e demais usuários.

Essas mensagens de notificação são definidas em **dois tipos: fixas ou temporais**. As **fixas** são mensagens enviadas no momento em que alguma alteração ou processo é executado. Já as **temporais** são enviadas através de um processo específico (Para saber mais, acesse ). Esta informação é somente para visualização não pode ser alterada.

Não será possível cadastrar mais de uma mensagem com o mesmo objetivo informado.

Formato da mensagem

A mensagem de notificação poderá ser no formato do e-mail, em HTML ou Texto padrão. Ao selecionar HTML, o usuário poderá estruturar o texto através de recursos de formatação e poderá utilizar recursos como imagens, vídeos, tabelas etc.

Notificação para Fluig

Para o envio de notificação via FLUIG é necessário que o sistema esteja parametrizado, assim, além de ativar o envio de notificação via FLUIG, é importante criar uma conta de comunicação e cadastrar as credencias do FLUIG. Para mais informações, acesse o documento técnico. Para que o usuário possa receber a notificação via FLUIG, ele precisa estar cadastrado no FLUIG com um usuário e e-mail válidos.  
A mensagem de notificação para o FLUIG só será enviada para os usuários, caso o tamanho da mensagem não ultrapasse 254 caracteres. Essa informação está descrita na tela de parametrização das mensagens para o FLUIG.

Tags disponíveis

Ao cadastrar a mensagem, poderão ser utilizadas tags predefinidas através do botão "Tags disponíveis", que serão substituídas por seus respectivos valores no momento do envio do e-mail.

Tags disponíveis em Consultas SQL 

Para que as tags disponíveis sejam corretamente utilizadas, nas mensagens encaminhadas com o uso de **Consultas SQL**, é importante que as colunas da **Consulta SQL** sejam apelidadas (alias) como a mesma grafia das tags disponíveis.

Exemplos:

Select NOME AS 'NOMEALUNO' FROM PPESSOA - habilita a substituição da tag [NOMELAUNO] pelo valor retornado do campo NOME.

Select NOME AS 'NOMEPROFESSOR' FROM PPESSOA - habilita a substituição da tag [NOMEPROFESSOR] pelo valor retornado do campo NOME.

**Atenção:** se o alias utilizado não for igual ao nome da tag disponível, a substituição não ocorrerá e a mensagem será formatada com o texto fixo da tag utilizada.

Exemplo:

Permissão para selecionar público alvo

Para poder selecionar um público alvo, é necessário que o usuário logado possua permissão especial . **Para saber mais acesse**

Os tipos de objetivos das mensagens de notificações:

Grupo: Secretaria

* Confirmar reserva de recursos;
* Confirmar reserva de instalação.
Grupo: Estágio

* Informar ao aluno que houve alguma alteração na vaga de estágio para a qual ele está inscrito;
* Informar ao aluno que ele foi selecionado para a vaga de estágio na qual está inscrito;
* Informar ao aluno que ele não foi selecionado para a vaga de estágio na qual está inscrito;
* Informar ao aluno sobre aprovação do plano de atividades do estágio;
* Informar ao aluno sobre reprovação do plano de atividades do estágio;
* Informar para o participante que ele foi convidado para a banca;
* Informar inscritos sobre alteração do endereço da empresa;
Grupo: FinanceiroBoleto próximo ao vencimento

Permite processar os boletos próximo ao vencimento (informação que será indicada no processo de envio da mensagem) e enviar um comunicado.

Para enriquecer o conteúdo da mensagem do objetivo "Boleto próximo ao vencimento", foram disponibilizadas TAGS no cadastro de mensagens relacionadas ao lançamento e campos opcionais/integração.

No módulo Educacional o cadastro está disponível no menu "TOTVS Gestão Educacional → Atividades acadêmicas → Central de Comunicações → Mensagens".

TAGS:

* **Registro acadêmico:** Registro acadêmico referente ao lançamento gerado.
* **Nome do aluno:** Nome do aluno referente ao lançamento gerado.
* **Nome do destinatário:** Nome da pessoa destinada a receber a mensagem do lançamento gerado.
* **Data vencimento:** Data de vencimento do lançamento gerado.
* **Valor:** Valor do lançamento gerado.
* **IPTE:** Código da linha digitável associado ao lançamento gerado.
* **Serviço:** Nome do serviço utilizado para geração do lançamento.
* **Parcela:** Número da parcela do lançamento gerado.
* **Cota:** Número da cota do lançamento gerado.
* **Competência:** Mês/Ano de competência do lançamento.
* **Juros:** Valor de juros do lançamento.
* **Multa:** Valor de multa do lançamento.
* **Desconto:** Valor de desconto do lançamento.
* **Acréscimo de acordo:** Valor de acréscimo de acordo no lançamento.
* **Juros do acordo:** Valor de juros do acordo no lançamento.
* **Desconto do acordo:** Valor de desconto do acordo no lançamento.
* **Bolsa condicional (Valor opcional/integração):** Valor do campo opcional/integração utilizado para bolsa condicional no lançamento.
* **Bolsa incondicional (Valor opcional/integração):** Valor do campo opcional/integração utilizado para bolsa incondicional no lançamento.
* **Acréscimo cobrança retroativa (Valor opcional/integração):** Valor de acréscimo de cobrança retroativa no lançamento.
* **Desconto cobrança retroativa (Valor opcional/integração):** Valor de desconto de cobrança retroativa no lançamento.
* **Pagamento via cartão - SOMENTE APP:** Link para pagamento via cartão de crédito do lançamento gerado.
* **Pagamento via pix - SOMENTE APP:** Link para pagamento via PIX do lançamento gerado.

Importante

A partir da versão **12.1.2506**, prevista para o segundo semestre de 2025, estarão disponíveis as tags **"PAGTOCARTAO" (Pagamento via cartão)** e **"PAGTOPIX" (Pagamento via PIX)**.  
  
Essas tags terão efeito exclusivamente na nova versão do **Meu eduCONNECT** e permitirão o pagamento do lançamento gerado por **cartão de crédito** ou **PIX**.  
  
Vale ressaltar que as mensagens enviadas por e-mail **não oferecerão a funcionalidade** de pagamento via cartão de crédito ou PIX.

Para mais informações sobre valores de integração financeira, favor acessar o documento  "[DT Cadastro de Valores de Integração Financeira](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=320376755)".

Boletos agrupados

Regra aplicada a partir da versão 12.1.34.153.

Caso o boleto esteja agrupando informações de parcelas distintas ou alunos diferentes, as TAGS abaixo poderão demonstrar mais de uma  informação.

**[RA], [NOMEALUNO], [NOMESERVICO], [PARCELA], [COTA], [DTCOMPETENCIA].**

Por exemplo:

Se for um boleto agrupando duas parcelas com serviços distintos, sendo:

Parcela 1 – Mensalidade

Parcela 2 – Alimentação

O resultado será:

**[NOMESERVICO]** => Mensalidade, Alimentação

**[PARCELA]** => 1,2

A mensagem não será enviada quando o publico alvo selecionado for "Enviar para Aluno" e boleto estiver agrupando informações de alunos distintos.

Será apresentado no log uma mensagem conforme o exemplo abaixo :

***Não foi possível enviar a mensagem para o aluno “ ES-00292 - Anthony José Sales - anthony-sales@gmail.com.br ”, pois seu boleto esta agrupando informações de outro aluno.***

Parâmetros de mensagem de Vencimento de Boleto

Para listar corretamente os boletos que serão incluídos na mensagem informativa, é necessário especificar a quantidade de dias para o vencimento do boleto, contando a partir da data atual.

Com base no número de dias fornecido, o sistema enviará a mensagem para todos os boletos que vencem entre a data de hoje e a data resultante da soma do número de dias especificado.

Usuário do responsável financeiro

À partir da versão **"12.1.2502"**, será necessário que o responsável financeiro tenha um usuário associado para que o sistema consiga identificar seus boletos.

O campo "Usuário de acesso", na aba "Dados Adicionais", no cadastro de Cliente/Fornecedor, deverá ser preenchido com o usuário que será utilizado pelo responsável financeiro. Caso o responsável financeiro seja o próprio aluno, pode-se colocar o mesmo usuário do aluno.

Importante - Consulta por SQL

Na utilização de consulta por SQL, o campo **"CODUSUARIO"**, da consulta, deverá representar o código de usuário, do responsável financeiro do boleto, associado ao campo **"CODUSUARIOACESSO"** da tabela **"FCFO"**, conforme mostrado na imagem acima.

Resultado da avaliação do fiadorImportante

Esse tipo de mensagem estará disponível a partir das versões "**12.1.33.220**" e "**12.1.34.131**".

#F5F5F5#FFFFF9

* Fiadores ativo e com status de aprovado ou reprovado:
  + Serão considerados apenas alunos que possuírem fiadores ativos e com status de aprovado ou reprovado;
  + Serão considerados todos os documentos dos fiadores independente do status, porém, os documentos devem está relacionados com os documentos exigidos dos fiadores na parametrização do curso;
  + Para as mensagens com esse objetivo estão disponíveis as tags:
    - RA - Registro acadêmico;
    - NOMEALUNO - Nome do aluno;
    - NOMECURSO - Nome do curso;
    - NOMEHABILITACAO - Nome da habilitação;
    - CODPERLET - Código do período letivo;
    - DETALHEFIADORES- Lista de Fiadores com seu respectivo status;
    - DETALHEFIADORESCOMDOCUMENTOS - Lista de Fiadores com seu respectivo status, nome do documento e o status do documento. Para os documentos rejeitados, deverão ter a descrição da informação do motivo da rejeição. Os documentos listados devem está relacionados na lista de documentos do fiador e a lista de documentos do fiador na parametrização por curso do aluno.
* Público-alvo:
  + Aluno;
  + Responsável financeiro;
  + Fiador.

* Log do processo:
  + Todos os usuários que possuem fiadores ativo, aprovado e não forem classificados nessas regras serão listados com o seguinte texto: ***"Não foi possível encontrar resultado da avaliação do fiador com os parâmetros informados".***

* **Observação importante**:
  + Esta mensagem não terá a opção de notificação para o FLUIG.
Grupo: Matrícula e Avaliação

* Pendências financeiras do aluno

#F5F5F5#FFFFF9

* Lançamentos vencidos:
  + A data de vencimento utilizada na pesquisa considera a data corrente acrescida do número de dias de carência parametrizado nos parâmetros da Tesouraria.
  + As pendências serão verificadas em todas as coligadas, caso o parâmetro para verificação de débitos em outras coligadas esteja marcado, nos parâmetros da Tesouraria.
  + Serão considerados pendentes, todos os lançamentos que não forem baixados por acordo e que possuam a data de vencimento menor que a data de vencimento calculada.
  + Serão considerados no filtro apenas lançamentos que estão vinculados a serviços que possuem a parametrização para validação de inadimplência no processo de matrícula.
  + Serão considerados, também, lançamentos vencidos com boletos cancelados.
* Conta corrente:
  + Será verificado o valor da conta corrente e se o saldo ultrapassa o valor de carência parametrizado nos parâmetros da Tesouraria.
  + Caso o valor seja negativo e ultrapasse a carência, o usuário entrará na lista de notificação.

* Log do processo:
  + Todos os usuários que possuem lançamentos vencidos ou débitos em conta corrente e não forem classificados nessas regras serão listados com o seguinte texto: ***"Não é necessário encaminhar notificação para o usuário"***

* Cadastro de ocorrência para o aluno;

* Frequência do aluno próximas do limite ou excedido

#F5F5F5#FFFFF9

* O envio irá ocorrer apenas quando houver a execução do processo **Agendamento/envio de mensagens** (disponível em: Atividades acadêmicas | Central de Comunicações | Agendamento/envio de mensagens), deve-se levar em consideração que, o processo só estará apto para ser executado quando o percentual de faltas do aluno na disciplina atingir  o regra seguindo o [Cálculo para definir o limite de faltas por etapa ou por frequência diária.](https://tdn.totvs.com/x/Ce36E)

**Observações importantes**:

* A aula deve estar liberada para visualização.
* Deve-se ter o número de aulas dadas informado no cadastro de faltas da tela de Frequência Diária.

Para a mensagem de notificação: **Frequência do aluno próximas do limite ou excedido** (Disponível em: Atividades acadêmicas | Central de comunicações | Mensagens)

A Tag: **PERCLIMITEFREQUENCIA** só será levada em consideração se a Instituição de Ensino usar o limite de faltas parametrizado nas configurações gerais do sistema, isso é, o parâmetro: ***Utilizar a etapa da turma/disciplina para consultar a frequência*** mínima **DESMARCADO** e com o valor informado no campo: **%Limite de faltas.**

* Pendências de matrícula (Financeira, Documentos, Biblioteca);

#F5F5F5#FFFFF9

* As mensagens de notificações com o objetivo de avisar sobre as pendências de matrícula poderão conter informações sobre documentos obrigatórios pendentes, empréstimos da biblioteca em atraso, pendências financeiras na biblioteca e pendências financeiras do aluno em atraso.
* Poderão ser selecionados os públicos alvos: alunos, pais e responsáveis.
* Para as mensagens com esse objetivo estão disponíveis as tags:
  + DOCUMENTOSPENDENTES - Documento pendentes do aluno
  + BIBLIOPENDENCIA - Pendências na biblioteca
  + DEMONSTRATIVODEBITO - Pendências financeiras do aluno
  + RA - Registro acadêmico
  + NOMEALUNO - Nome do aluno
  + NOMECURSO - Nome do curso
  + NOMEHABILITACAO - Nome da habilitação
  + CODPERLET - Código do período letivo
  + NOMEDESTINATARIO - Nome do destinatário
  + NOMEPAI - Nome do pai
  + NOMEMAE - Nome da mãe
  + NOMERESPACADEMICO - Nome do responsável acadêmico
  + NOMERESPFINANCEIRO - Nome do responsável financeiro

* Pendências da biblioteca
  + A tag "***BIBLIOPENDENCIA***" será substituída pelas informações de empréstimos com o status "*Atrasado*" e pendências financeiras da biblioteca.
  + A validação de informações da biblioteca será realizada com a parametrização do Educacional:
    - *15.05 - Integração | 15.05.06 - biblioteca | Biblioteca 1/5 | "Bloqueio de matrícula/mudança de status no período letivo" | "Alunos com empréstimos em atraso na biblioteca" e/ou "Alunos com débitos na biblioteca"*

* Documentos pendentes
  + A tag "**DOCUMENTOSPENDENTES**" será substituída pela lista de documentos obrigatórios, do período letivo, que não foram entregues ou estão recusados.
  + Documentos destinados a ingressos poderão ser notificados, também, desde que o sistema esteja parametrizado para sua validação.
  + Parâmetro: *15.03 - Matrícula | Movimento 2/4 | "Considerar documentos do tipo ingresso mesmo que não seja a primeira matrícula"*

* Demonstrativo financeiro
  + A tag "**DEMONSTRATIVODEBITO**" será substituída pela informação de débitos financeiros, em atraso, de contratos e/ou contas correntes do aluno.

Obs.: Alunos que não tiverem nenhuma pendência de matrícula não serão notificados, assim, como seus responsáveis.

* Liberação ou digitação de etapa de nota;
* Liberação ou digitação de etapa de falta;
* Liberação ou digitação de notas de avaliação;
* Liberação de materiais;
* Liberação de materiais do Plano de Aula da turma/disciplina;
* Informar sobre documentos dos alunos recusados

  Durante a conferência dos documentos enviados pelos alunos, é comum que alguns sejam recusados por estarem ilegíveis, incorretos ou inválidos. Sempre que um documento receber o status **“Recusado”**, o sistema enviará automaticamente um e-mail ao Aluno/Responsável por meio da Central de Notificações. Conforme a configuração definida, essa notificação também poderá ser enviada através do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens).

  Tags disponíveis para utilização na composição da mensagem:

  + RA - RA do aluno
  + NOMEALUNO - Nome do aluno
  + DOCUMENTOSRECUSADOS - Lista de todos os documentos com status **Recusado** (incluindo o documento recém recusado) e seus respectivos motivos de recusa.
  + CODPERLERT - Período Letivo
  + NOME DE DESTINATÁRIO -  Informa de destinatário

  A validação do documento recusado pode ser realizada por meio de [Inteligente Artificial](https://tdn.totvs.com/display/public/LRM/Cadastro+de+Documentos), de forma [manual](https://tdn.totvs.com/display/LRM/Documentos+solicitados) ou através do processo de .

  **Obs.** Funcionalidade disponível a partir da versão 12.1.2506.128.
Grupo: Mensagens eventuaisImportante

A partir das versões "***12.1.27.298***", "***12.1.28.210***" e "***12.1.29.134***" será possível informar o **Tipo de Remente** que será utilizado no envio do E-mail: Usuário, Coligada, Coligada global, Parâmetros globais e Personalizado.

* **Enviar por e-mail:**  
  Nesta opção o usuário precisa informar o "Assunto do e-mail" e o "Tipo de Remente".

  Como opções de remetente, poderão ser selecionados:

1. Usuário logado no sistema;  
2. Coligada atual;  
3. Coligada global;  
4. Parâmetros globais (parametrização padrão de envio de mensagens definido na tela de parâmetros de Globais na aba Envio E-mails);  
5. Personalizado: o usuário poderá informar um e-mail e nome do remetente a ser identificado. Serão exibidos, somente, endereços de e-mails configurados nos parâmetros da secretaria em ***15.01 - Parâmetros | Secretaria | Geral 7/7***.

Envio de E-mail:

* **Enviar mensagens eventuais para e-mail, FLUIG ou eduCONNECT;**

Para que o sistema possa enviar mensagens eventuais aos "Alunos, Pais, Responsáveis Acadêmicos e Financeiros", o(s) aluno(s) precisa(m) estar matriculado(s) no período letivo com a situação de matrícula que indica "**Aluno ativo**" (Parâmetro "Aluno ativo" marcado, disponível em TOTVS Educacional | Currículo e Oferta | Acadêmico | Situação de matrícula | Aba Status no período letivo | Parâmetro Aluno ativo).

**Observação:** *Para permitir o envio de mensagens eventuais ao eduCONNECT, os usuários selecionados como destinatários (Alunos, Pais e Responsáveis) precisam ter um **usuário** associado, caso contrário o processo poderá indicar que não houveram registros no escopo selecionado.*

Importante

A partir da versão "***12.1.2205***" será possível utilizar as *TAGs* **"RA(Registro acadêmico)", "NOMEALUNO(Nome do aluno)" e "NOME(Nome do destinatário)"** através do botão "Tags Disponíveis" do [cadastro de mensagens](https://tdn.totvs.com/x/QGqlGw) para o objetivo "Enviar mensagens eventuais para e-mail, FLUIG ou eduCONNECT".

As novas *TAGs* **"RA(Registro acadêmico)" e "NOMEALUNO(Nome do aluno)"**estarão disponíveis apenas para o público-alvo de responsáveis do aluno (Pais, Responsável Acadêmico e Responsável financeiro), e não serão exibidas caso seja marcado o público-alvo "Coordenador e/ou Professor", pois são *TAGs* direcionadas apenas aos alunos dos responsáveis.

Em contrapartida, a *TAG* **"NOME(Nome do destinatário)",**será exibida quando for selecionado mais de um público-alvo, facilitando a criação de uma única mensagem para vários público-alvo diferentes.

Foi disponibilizado um parâmetro no processo de Agendamento/envio de mensagens com o intuito de possibilitar que sejam enviadas mensagens de notificações para os alunos que se encontram com a situação de matrícula de aluno inativo, no período letivo. O mesmo é aplicado aos pais e responsáveis do aluno, que serão notificados seguindo a mesma regra.

O sistema irá filtrar as situações de matrícula com o parâmetro "Aluno ativo" desabilitado, quando o parâmetro "Considerar situações de matrícula que não definem 'Aluno ativo' no período letivo" estiver selecionado.

Importante

O parâmetro "Considerar situações de matrícula que não definem 'Aluno ativo' no período letivo" está disponível a partir das versões: "12.1.28.169" e "12.1.29.100".

Público alvo Coordenadores e Professores

###### **Coordenadores:**

Para que o coordenador seja identificado como um alvo para o envio de mensagens, é necessário que ele esteja cadastrado na comissão coordenadora com a função "Coordenador". É necessário, também, que o período de atividade do seu mandato esteja ativo ou não tenha uma data para término. Caso seja realizado um filtro, no processo, que compreenda uma ou mais matrizes em que o período de seu mandato já tenha sido concluído, ele não entrará na lista de pessoas que receberão a notificação.

###### **Professores:**

Para que um professor de uma turma seja identificado como um alvo para o envio de mensagens, é necessário que o período de atividade em suas turmas estejam ativos ou não tenham uma data para término. Caso seja realizado um filtro, no processo, que compreenda uma ou mais turma em que o período de suas atividades já tenha sido concluído, ele não entrará na lista de pessoas que receberão a notificação.

Importante!

A partir da versão 12.1.2306, mensagens destinadas aos pais dos alunos maiores de 18 anos, somente serão enviadas, caso esse aluno tenha dado permissão de visualização aos seus dados.

Para mensagens com categoria "Financeiro" a permissão "dados financeiros" deve estar marcado na filiação.

Para qualquer mensagens que **não seja** categoria "Financeiro" a permissão "dados acadêmicos" deve estar marcado na filiação.

Veja Também

---

[TOTVS eduCONNECT - Cadastro de Mensagens](https://tdn.totvs.com/x/QGqlGw)
