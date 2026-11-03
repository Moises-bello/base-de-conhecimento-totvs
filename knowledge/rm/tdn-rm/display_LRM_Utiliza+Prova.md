---
content_hash: 663660dd7502841f9e893aa3bb9f415ec49b3a45f0b9ec72721989828fb8691a
fetched_at: '2026-06-29T00:10:32.886724+00:00'
page_id: '528450656'
product: rm
source: tdn-rm
title: Utiliza Prova
type: documentation
url: https://tdn.totvs.com/display/LRM/Utiliza+Prova
version: 39
---

|  |  |
| --- | --- |
| Descrição | Processo Seletivo |
| Observações | Seleção de candidato por meio de Prova |

---

---

Esta página se destina à explicação detalhada do processo de seleção de alunos por meio da utilização de provas no modulo Avaliação e Pesquisa.

# Identificação

 Caminho: **Módulo Processo Seletivo > Cadastro > Processo Seletivo > Aba: Identificação**:

**Campos "Código"** - Preenchido após salvar a tela inicial do processo seletivo e ele é sequencial.

**Campo "Nome do Processo Seletivo"** - Ele é preenchido com o nome que deseja dar ao Processo Seletivo

**Campo “Instituição”** - Ele só será preenchido quando o processo seletivo for realizado para terceiros (empresas que queiram utilizar o módulo Processo Seletivo para selecionar candidatos para determinado curso ou atividade).

**Se o campos INSTITUIÇÃO for preenchido em outra situação NÃO conseguiremos executar o processo até o final. Fazendo-se necessário criar um novo Processo Seletivo**

**Campo “Máximo de Inscrições por Candidato”**- Especifica o número de vezes que uma mesma pessoa poderá se inscrever no Processo Seletivo. Podem existir Processos Seletivos nos quais uma mesma pessoa concorrerá em uma ou mais vagas.

**Campo “Valor da inscrição”** - Define um valor de inscrição padrão para o Processo Seletivo. Ao incluir uma Área de Interesse Ofertada, automaticamente ela irá assumir esse valor como taxa de inscrição, no entanto, será possível definir taxas específicas para cada uma das áreas de interesse do Processo Seletivo.

# Informações Complementares

Caminho: **Módulo Educacional> Processo Seletivo > Cadastro > Processo Seletivo > Aba: Informações Complementares**:

**Campo “Questionário”**: Deve ser selecionado para este campo uma prova do tipo “Pesquisa de Opinião”, criada no Módulo Avaliação e Pesquisa. Caso utilizada esta opção, os candidatos que realizaram a inscrição através do Portal, devem responder o questionário socioeconômico no momento da inscrição. Essa opção deve ser utilizada, no caso de vestibulares com a necessidade de preenchimento do questionário socioeconômico no ato da inscrição.

**Campo "Nome do Questionário"**: Permite personalizar o nome do questionário a ser respondido na inscrição do Portal. Se não for configurado nenhum nome, o padrão será “Questionário socioeconômico”. Esta configuração será utilizada apenas se for definido algum questionário para o Processo Seletivo.

**Campo “Comprovante de inscrição NOVO GERADOR”** - Deve ser selecionado para este campo um relatório do “Book De Relatórios” preparado especificamente para o comprovante de inscrição. O relatório selecionado é utilizado para emissão do comprovante de inscrição através do Portal.

**Campo "Fórmula para classificação geral":** Definida uma fórmula a ser utilizada pelo processo  [Gerar/Cancelar classificação geral](#processo_gerarcancelar_classificacao_ger) . As fórmulas disponíveis para seleção devem ser criadas previamente através do cadastro de fórmulas. Se uma fórmula for configurada, ela será aplicada no momento em que o processo for computar a nota do candidato para enquadrá-lo na classificação geral.

**Campo "Utiliza controle de vagas"** - Este recurso pode ser utilizado quando houver a necessidade de realizar um Processo Seletivo com controle de vagas. Quando esta opção for utilizada, o usuário deve escolher o tipo do controle de vagas;

**Campo "Tipo do controle de vagas"** - Deve ser configurado a forma como o controle de vagas gerencia as inscrições. Existem duas opções: “Não permitir novas inscrições” e “Permitir novas inscrições, mas os candidatos ficarão como excedentes”.

Quando uma área ofertada for escolhida por um candidato na inscrição, sendo Processo Seletivo parametrizado para utilizar controle de vagas e este estiver com as vagas desta área esgotadas, o Sistema disponibilizado duas opções de acordo com a configuração escolhida:

* “Não permitir novas inscrições”, a inscrição é interrompida e o usuário será notificado que as inscrições estão encerradas por falta de vagas;
* “Permitir novas inscrições, mas os candidatos ficarão como excedentes”, o usuário será notificado que não há mais vagas para a área ofertada, no entanto, o Sistema oferecerá duas opções para o mesmo: prosseguir com a inscrição e permanecer como “excedente” (informando o número de excedentes) ou desistir da inscrição.

Quando o Processo Seletivo utiliza a opção de “Controle de Vagas”, as “Áreas Ofertadas” oferecidas pelo mesmo, não podem ter áreas opcionais, pois a classificação de Processos Seletivos com “Controle de Vagas” é feita, somente, por ordem de inscrição. Sendo assim, a classificação em uma área opcional iria afetar a ordem de candidatos classificados pelo número de inscrição

# Calendário

Caminho: **Módulo Educacional> Processo Seletivo > Cadastro > Processo Seletivo >Aba: Calendário**

Nessa aba são definidos os três períodos que um Processo Seletivo deve ocorrer:

* Período de inscrições;
* Período de seleção;
* Período de divulgação de resultados.

Para cada um dos três períodos, devem ser definidas a data de início e a de término.  Os períodos podem se sobrepor desde que respeitem as regras a seguir:

* Início da seleção tem que ser maior ou pelo menos igual ao da inscrição.
* Início do resultado tem que ser maior ou pelo menos igual ao da seleção.
* Final da inscrição tem que ser menor ou no máximo igual ao da seleção.
* Final da seleção tem que ser menor ou no máximo igual ao do resultado.

As definições de calendário são fundamentais no decorrer dos Processos Seletivos, pois afetam diversos serviços. O Portal, por exemplo, baseia-se no calendário para exibir corretamente os Processos Seletivos e fornecer as informações certas aos visitantes e candidatos. Com base no calendário o Sistema permite que sejam feitas inscrições somente no período de inscrições, etc

Portaria

Caminho: **Módulo Processo Seletivo > Cadastro > Processo Seletivo >Aba: Portaria**

Essa aba possui um único campo que deve ser preenchido com o texto da portaria que autorizou a realização do Processo Seletivo. Esse conteúdo, quando preenchido, é exibido no detalhamento do Processo Seletivo no Portal.

---

# Informações Financeiras

Caso o Processo seletivo tenha taxa de inscrição, deve-se seguir as  informações abaixo para sua parametrização.

Caminho: **Módulo Processo Seletivo > Cadastro > Processo Seletivo >Aba: Informações Financeiras**

Pagamento de Profissionais Inscrições -Geral 1

Nesta aba são configuradas diversas informações utilizadas na integração com o Módulo Gestão Financeira. Os serviços do Módulo Gestão Financeira são necessários para inclusão de lançamentos financeiros, servindo de base para emissão e baixa de boletos da inscrição. Os lançamentos financeiros também são realizados para o pagamento de Fornecedores que tenham trabalhado em um determinado Processo Seletivo.

O campo “nosso número” pertencente ao lançamento e será gerado com base no *Id Boleto* (Código sequencial utilizado para gerar o campo nosso número).

Na opção “Informações Financeiras – Inscrições”, devem ser definidos os parâmetros para geração dos lançamentos e boletos de inscrição por meio da integração com o Módulo Gestão Financeira.

**Cliente/Fornecedor** - Deve ser selecionado um registro de cliente a partir do cadastro de clientes/ fornecedores. Esse registro compõe o lançamento financeiro de cada uma das inscrições, evitando a necessidade de se criar uma entrada no cadastro de clientes/fornecedores para cada um dos candidatos.

**Conta/Caixa -** Identifica a conta corrente utilizada no processo de recebimento dos boletos. Ex: “Caixa Econômica Federal”.

**Tipo de Documento -** Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Uma das funções de um registro de “Tipo de Lançamento” é parametrizar o lançamento a ser feito, informando se ele é um lançamento “A pagar” ou “A Receber”. Para os lançamentos de inscrição devem ser usados tipos de registro a “A Receber”. Ex: “Recebimento de Taxas”.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar documentos.

**Moeda -** Moeda corrente utilizada na geração dos boletos. Ex: “Real”.

**Histórico:** Informação textual que compõe o campo histórico dos lançamentos.

**Testar geração de lançamento -** Através deste recurso, é possível simular uma geração de lançamento para a inscrição, verificando se os parâmetros financeiros configurados são válidos, segundo as regras do Módulo Gestão Financeira. Após a simulação do lançamento, uma mensagem informará se a configuração é válida ou se houve algum erro, informando o motivo.

**Disponibilizar pagamento de cartão de crédito no portal** - Este parâmetro tem como objetivo, permitir que os candidatos do processo seletivo possam efetuar o pagamento da inscrição através do portal utilizando cartão de crédito. O pagamento ficará disponível nos serviços de Impressão após a inscrição do candidato e em 2ª via de boleto e será exibido um ícone, possibilitando ao usuário clicar na tela para informação dos dados de cartão de crédito, caso o processo seletivo esteja configurado. Caso contrário, será exibido somente o código IPTE do boleto e a opção de impressão do boleto.

* Importante: Para realizar o pagamento da inscrição via cartão de crédito é preciso que seja parametrizado no RM Fluxus as configurações do cartão de crédito.

**Gerar lançamentos /boletos com registro online** - Este parâmetro tem como objetivo permitir aos candidatos a impressão do boleto de inscrição registrado.

**Apresentar boleto de cobrança registrada ainda não registrado no Portal** - Este parâmetro tem como objetivo permitir que os boletos provenientes de convênios com cobrança registrada sejam impressos, mesmo que os boletos não tenham sido registrados.

Geral 2

**Campo “Filial do lançamento”** – Filial (Unidade Operacional) responsável pelos lançamentos.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar Documentos.  
Esse campo, fica visível após “salvar” todo o cadastro do processo seletivo.

**Campo “Departamento do lançamento”** - Departamento da filial (Unidade Operacional) responsável pelos lançamentos.  
**Campo “Centro de Custo”:** Identifica o centro de custo que é o responsável pela receita gerada com as inscrições.  
**Campo “Tipo Contábil**” - Define o status contábil do lançamento que será criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”.  
**Campo “Evento Contábil de inclusão”** - Identifica o registro contábil que será gerado em decorrência do lançamento de inscrição.

Opcionais

**Campo “Tabelas opcionais”** - Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira.  
**Campo: “Campos alfa”** - Permite que seja informado o valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.  
Na opção “**Informações Financeiras - Pagamento de Profissionais - Cliente/Fornecedor”**, são definidos os parâmetros para geração dos lançamentos “A pagar”, que devem ser efetuados para pagamento dos fornecedores durante a execução do processo Gerar Pagamento de Profissionais.  
**Campo “Conta/Caixa”:** Identifica a conta corrente utilizada no processo de pagamento do fornecedor.  
**Campo “Pessoa Física/Pessoa Jurídica - Tipo de Documento”** - Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Esse tipo de documento irá compor os lançamentos de pagamento dos fornecedores, logo, deve ser selecionado o tipo “A pagar”. A parametrização deste campo é diferenciada de acordo com o tipo de fornecedor: pessoa física ou jurídica. Ex: “NF RPA - RPA”.

 Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar Documentos.  
Campo “Pessoa Física/Jurídica - Código de Receita” - Deve ser preenchido se o respectivo “Tipo de Documento” possuir no Módulo Gestão Financeira, as classificações  
“Gerar IRRF” ou “Gerar IRRF e INSS”.

**Campo “Moeda”** - Moeda corrente que será utilizada na geração dos lançamentos de pagamento;

Se o código de receita não for preenchido e o tipo de documento é um tipo parametrizado para reter imposto de renda sobre o lançamento, o serviço de integração não fará o lançamento de pagamento, será gerado um erro.   
  
**Campo “Centro de custo”** - Identifica qual centro de custo é o responsável pela despesa gerada com o pagamento dos profissionais;  
**Campo “Histórico”** - Informação textual que compõe o campo histórico dos lançamentos;  
**Campo “Filial do lançamento”** - Filial (Unidade Operacional) responsável pelos lançamentos;  
**Campo “Departamento do lançamento”** - Departamento da Filial (Unidade Operacional) responsável pelos lançamentos;  
**Campo “Data do lançamento”** - Define a data dos lançamentos que são criados para pagamento dos profissionais;  
**Campo “Tipo Contábil”** - Define o status contábil do lançamento que é criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”;  
**Campo “Evento Contábil”** - Identifica o registro contábil que é gerado em decorrência do lançamento de inscrição .  
**Campo “Tabelas opcionais”** - Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira;  
**Campo “Campos alfa”** - Permite que seja informado valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.

A aba “Teste de geração de lançamento” permite que as configurações feitas para geração de lançamento de pagamento de profissionais sejam testadas. Ao clicar em “Testar geração de lançamento”, o Sistema realiza uma simulação de inclusão de lançamento a pagar conforme a parametrização feita nas abas anteriores, sendo necessário informar um “Cliente/Fornecedor” (Pessoa Física ou Jurídica) no campo correspondente.Pagamento de ProfissionaisCliente/Fornecedor Geral 1

**Conta/Caixa:** Identifica a conta corrente utilizada no processo de pagamento do fornecedor.

**Pessoa Física/Pessoa Jurídica - Tipo de Documento** - Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Esse tipo de documento irá compor os lançamentos de pagamento dos fornecedores, logo, deve ser selecionado o tipo “A pagar”. A parametrização deste campo é diferenciada de acordo com o tipo de fornecedor: pessoa física ou jurídica. Ex: “NF RPA - RPA”.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar [Documentos](#Tabela_Auxiliar_Documentos).

**Pessoa Física/Jurídica - Código de Receita -** Deve ser preenchido se o respectivo “Tipo de Documento” possuir no Módulo Gestão Financeira, as classificações “Gerar IRRF” ou “Gerar IRRF e INSS”.

Se o código de receita não for preenchido e o tipo de documento é um tipo parametrizado para reter imposto de renda sobre o lançamento, o serviço de integração não fará o lançamento de pagamento, será gerado um erro.Geral 2

**Moeda** - Moeda corrente que será utilizada na geração dos lançamentos de pagamento;

**Centro de custo** - Identifica qual centro de custo é o responsável pela despesa gerada com o pagamento dos profissionais;

**Histórico** - Informação textual que compõe o campo histórico dos lançamentos;

**Filial do lançamento** - Filial (Unidade Operacional) responsável pelos lançamentos;

**Departamento do lançamento** - Departamento da Filial (Unidade Operacional) responsável pelos lançamentos;

**Data do lançamento** - Define a data dos lançamentos que são criados para pagamento dos profissionais;

**Tipo Contábil** - Define o status contábil do lançamento que é criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”;

**Evento Contábil** - Identifica o registro contábil que é gerado em decorrência do lançamento de inscrição.

Opcionais

**Tabelas opcionais -** Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira;

**Campos alfa** - Permite que seja informado valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.

Teste de Geração de Lançamento

 A aba “**Teste de geração de lançamento**” permite que as configurações feitas para geração de lançamento de pagamento de profissionais sejam testadas. Ao clicar em “Testar geração de lançamento”, o Sistema realiza uma simulação de inclusão de lançamento a pagar conforme a parametrização feita nas abas anteriores, sendo necessário informar um “Cliente/Fornecedor” (Pessoa Física ou Jurídica) no campo correspondente.

---

# E-mail

Nesta aba deve ser parametrizado o envio de e-mail por Processo Seletivo, definindo e-mail de confirmação de inscrição dos candidatos.

 Esse cadastro só será utilizado para o antigo portal. Para o novo portal, o cadastro será realizado conforme demonstrado no menu “Mensagens de Notificação”.

**Enviar e-mail de confirmação da inscrição** – Se selecionado, o Sistema envia um e-mail com a confirmação da inscrição;

**Utilizar texto de e-mail personalizado (Confirmação de inscrição)** - Se a opção de envio de e-mail correspondente for utilizada, esse parâmetro ficará ativo e irá determinar o conteúdo do e-mail;

* Se desmarcado, é utilizado o texto de e-mail interno e fixo do Sistema;
* Se marcado, o usuário deve utilizar um texto personalizando, inserindo os parâmetros/descrição no campo "Texto do e-mail personalizado”.

**Texto do e-mail (Confirmação de cadastro e Confirmação de inscrição)** - Permite definir um texto de e-mail personalizado se a opção de “Utilizar texto de e-mail personalizado?”  estiver selecionada. O Sistema permite utilizar ***tags*** no corpo do texto, para serem substituídas pelos dados dos candidatos na hora do envio do e-mail;

Para utilizar envio de e-mail para confirmação de inscrição do candidato, algumas regras devem estar parametrizadas:

* Estar habilitado como visível e obrigatório o campo e-mail na configuração de “campos de candidato” em parâmetros do Sistema (Portal/ Pessoa/ Dados básicos). Uma vez que o campo e-mail não for habilitado no cadastro do candidato, o Sistema não enviará e-mails para o mesmo;
* Caso estiver habilitado o parâmetro "Utilizar responsável por candidato na inscrição" ao invés de "campos de candidato", deve-se validar os "campos de responsáveis";
* O campo e-mail de remetente do Processo Seletivo também deve ser preenchido.

# Parâmetros

**Módulo Educacional>  Processo Seletivo > Cadastro > Processo Seletivo >Parâmetros > Flag “Utiliza novo portal de inscrições”**: para que o processo seletivo realize a inscrição pelo novo portal, esse parâmetro deve ser habilitado para que as configurações sejam realizadas.

---

ParâmetrosInformações 1/2

Nome do portal de inscrições do processo seletivo: utilizado para descrever como será visualizado o nome do processo seletivo na área pública do Portal de Inscrição.

Utiliza senha para login do portal de inscrições: indica se o usuário quando acessa a área de inscrição irá informar uma senha. A utilização deste parâmetro impacta nos seguintes pontos:

* Cadastro de candidato: se o parâmetro “senha” estiver habilitado, então o sistema exigirá o preenchimento do campo senha e confirmação de senha. No e-mail de confirmação de cadastro será enviada a senha informada pelo candidato. Se o parâmetro estiver desabilitado, então os campos de senha não aparecerão no formulário de cadastro e o e-mail de confirmação irá com uma senha aleatória gerada pelo sistema.
* Login do sistema: se o parâmetro “senha” estiver habilitado, então será exigido a “Senha” cadastrada. Se o parâmetro estiver desabilitado, será exigido a “Data de Nascimento” como senha.
* Esqueci a senha / Alterar Senha: se o parâmetro “senha” estiver habilitado estes serviços estarão disponíveis.

Formas de Identificação: determina quais serão os dados disponibilizados para identificação do candidato. Podem ser CPF, Carteira de Identidade, Código do Usuário e/ou E-mail.

Na inscrição do candidato, se a opção "**Aproveitar dados do cadastro de Pessoa**" estiver marcada o sistema aplicará internamente a busca de candidatos nos cadastros de usuário do TOTVS Processo Seletivo e também no cadastro de **Pessoa.**

A pesquisa utilizará o mesmos critério de unicidade parametrizado no processo seletivo (para saber mais sobre critério de unicidade [clique aqui](https://tdn.totvs.com.br/pages/viewpage.action?pageId=284884269)).

Esta funcionalidade tem como objetivo agilizar o processo de inscrição uma vez que os dados do candidato já fazem parte da base de dados do RM, e também manter os dados atualizados conforme o cadastro de **Pessoas**.

**Por exemplo**

Um funcionário ou aluno da instituição que já esta cadastrado como Pessoas e não possui registro no cadastro de usuário no TOTVS Processo Seletivo realiza a inscrição em um determinado processo seletivo, neste exemplo se a opção "**Aproveitar dados do cadastro de Pessoa**" estiver marcada, o sistema identificara seu registro no cadastro de **Pessoas**e apresentará no portal a tela abaixo:

A mensagem acima será sempre será apresentada se um candidato já possuir cadastro no TOTVS Processo Seletivo (se estiver parametrizado para utilizar critério de unicidade), mesmo que o usuário não seja encontrado no cadastro de pessoa. 

No momento em que esta mensagem é apresentada o **TOTVS Processo Seletivo** realiza a importação do cadastro de **Pessoas** para o cadastro de usuários.

**Regras da opção "Aproveitar dados do cadastro de Pessoa":**

* Se não for localizado nenhum registro no cadastro de usuário do TOTVS Processo Seletivo será aplicada a mesma busca no cadastro de **Pessoas**, caso seja localizado um registro, o cadastro da Pessoa será importado para o cadastro de usuário do TOTVS Processo Seletivo.
* Quando recuperado os dados do Cadastro de Pessoas, caso existam **Filiações** **associadas a esta pessoa**, os dados das **Filiações** existentes também serão recuperados e aproveitados no cadastro de usuários do TOTVS Processo Seletivo mantendo os relacionamentos existentes. (Por exemplo: Se no cadastro de Pessoas uma determinada pessoa possui uma Filiação do Tipo Pai, esta filiação será importada para o cadastro de usuários do Processo Seletivo como uma Filiação/Responsável do candidato do Tipo Pai)
* Se o candidato já possuir um cadastro no TOTVS Processo Seletivo mesmo assim o sistema realizará a busca das informações no cadastro de **Pessoas,**caso seja localizado um registro no cadastro de **Pessoas** iremos copiar os dados do cadastro de Pessoa **sobrescrevendo** os dados no Cadastro do Usuário.

Para que o CPF, Carteira de Identidade e E-mail sejam utilizados é necessário que estes campos estejam visíveis e obrigatórios na aba “Visibilidade/Obrigatoriedade de campos.Informações 2/2

Texto da Área de Informações:  É possível configurar um texto para ser visualizado na área de informações do Portal. Neste campo pode ser inserido hiperlinks, imagens, textos e tabelas.

Inscrições

Texto da Área de Inscrições:  É possível configurar um texto para ser visualizado na área de inscrições do Portal. Neste campo pode ser inserido hiperlinks, imagens, textos e tabelas.

Geral 1/3

Utilizar responsável por candidato na inscrição: essa opção é indicada para Instituições que possuem processos seletivos com menores de 18 anos e precisam de um responsável para responder por eles. É possível que a inscrição do candidato seja realizada através do responsável. Assim, é importante que disponibilize em campos do candidato o Responsável Financeiro, Dados do Pai e Dados da Mãe.

Texto do campo Treineiro: este parâmetro fica visível na tela de inscrições do Portal. Quando vazio a mensagem padrão será: *“Após a divulgação dos resultados você NÃO estará com o 2º grau concluído? Ou seja, você é Treineiro?”*.

Exigir preenchimento do sobrenome: este campo é utilizado para não permitir que o candidato escreva seu nome sem sobrenome. Se desmarcado poderá ter somente o nome do cadastro.

Gravar dados em letras maiúsculas:  se marcado este parâmetro, independente de como os dados foram digitados, serão gravados em letras maiúsculas.

É possível definir qual responsável (Pai, Mãe, Responsável Financeiro ou Responsável Acadêmico) será utilizado na inscrição. Para cada um deles pode ser marcado para desconsiderar a obrigatoriedade de todos os campos.

Critérios de busca por candidato existentes: a busca pelos dados dos candidatos já existentes pode ser realizada por meio do Nome, data de nascimento, estado natal, naturalidade, CPF, passaporte, registro geral e e-mail.

Critério - E/ OU: marcar a flag de acordo com o que deseja buscar

Tipo de filiação obrigatório: deverá ser marcada a opção que melhor encaixa na realidade do DR naquele processo seletivo**.**

Geral 2/3

Tipo de boleto/comprovante: indica qual a plataforma em que os relatórios serão visualizados pelo candidato. Poderão ser exibidos na plataforma “PDF” ou “HTML”. Os serviços do Portal que exibem estes relatórios são “2ª via de Comprovante de Inscrição” e “2ª via de Boleto”.

Texto do comprovante de inscrição: é possível configurar um texto personalizado que irá compor o comprovante de inscrição do candidato. Através deste campo será possível realizar tal configuração.

Geral 3/3

Existem algumas configurações para que seja possível o processo seletivo receber inscrição de candidatos e responsáveis estrangeiros:

* Obrigar o preenchimento de um dos campos (CPF, Passaporte ou Registro geral): se na inscrição o candidato escolher um País diferente do cadastrado na nacionalidade do processo seletivo, esses três campos ficaram obrigatórios, mas a partir do momento em que preencher um dos três campos, os outros ficaram como opcionais. Se marcado este parâmetro, é necessário que os campos “CPF”, “Passaporte” ou “Registro geral” estejam marcados como visíveis na aba “Visibilidade/Obrigatoriedade de campos”.
* Utilizar parametrização dos campos do grupo “Documentos” sem exigir obrigatoriedade: determina se o sistema irá exibir os campos de documentos que foram definidos para serem visualizados nos cadastros de responsáveis e de candidatos, porém, se algum destes campos forem obrigatórios, exclusivamente para estrangeiros não serão obrigatórios.  Se desabilitado, os campos continuam obrigatórios mesmo para candidatos estrangeiros.

Nacionalidade: campo destinado a definir qual a  nacionalidade do processo seletivo. Caso esteja parametrizado para Brasil, e o candidato selecionar México,  o sistema irá considerar que este usuário é estrangeiro.

Serviços disponibilizados na inscrição do portal: são links úteis para o candidato que já está inscrito no processo seletivo. Caso o usuário não esteja logado no browser, será redirecionado para a tela de login e logo após para o serviço solicitado.

Visibilidade/Obrigatoriedade de Campos

Nesta aba é possível determinar quais  os campos de usuário nos serviços de candidato serão visíveis e/ou obrigatórios no momento da inscrição.

Resultado 1/2

Este campo é destinado às informações que irão constar na área de Resultados. Podem ser cadastrados textos, imagens, tabelas e hiperlinks.

Resultado 2/2

Mostrar Número de vagas em Inscrições /Resultados: determina se a informação que contém o número de vagas da área ofertada será exibida no serviço do Portal “Inscrições/Resultados”.

Mostrar os campos a seguir em Resultados por Área Ofertada e Inscrições/Resultados:

* Classificação: determina se o serviço de “classificação por área” estará disponível para consulta no Portal.
* Pontuação: determina se a informação que contém a pontuação do candidato será exibida nos serviços do Portal “Divulgação de resultados” e “Inscrições/Resultados”.
* Número de Inscrição: determina se a informação que contém o número de inscrição do candidato será exibida nos serviços do Portal “Divulgação de resultados” e “Inscrições/Resultados”.
* Situação Atual: determina se a informação que contém a situação atual do candidato será exibida nos serviços do Portal “Divulgação de resultados” e “Inscrições/Resultados”.

Mostrar resultado por área ofertada: resultados exibidos para os candidatos por área ofertada.

Mostrar na lista também os candidatos desclassificados: determina se candidatos desclassificados serão incluídos na listagem de resultados gerais. É importante ressaltar que este parâmetro terá efeito no Portal somente se os parâmetros “Mostrar classificação geral” e/ou “Mostrar classificação por área” estiverem habilitados.

Mostrar classificação geral: exibe a listagem de classificação por processo seletivo.

Mostrar lista de chamadas: exibe a listagem dos candidatos chamados em uma área ofertada.

Serviços disponibilizados na inscrição do portal: são links úteis para o candidato que já está inscrito no processo seletivo. Caso o usuário não esteja logado no browser, será redirecionado para a tela de login e logo após para o serviço solicitado.

Redes Sociais

Na tela do Novo Portal é possível disponibilizar os links de acesso às redes sociais da instituição. Basta informar o endereço e no campo de Whatsapp informar o número de contato.

Arquivos

Os arquivos do candidato, tais como documentos, fotos pode ser salvos no Novo Portal, para isso é necessário que seja configurado os locais onde serão armazenados. Poderá ser feito em base de dados ou em algum diretório da rede. É possível restringir o tamanho dos arquivos bem como as suas extensões

Campos Complementares

Em Campo complementar é possível vincular os campos cadastrados e vinculados na filial com Visibilidade igual a “Ambos” ou “Portal”. Cada campo complementar deve ser habilitado a um Grupo onde será exibido no formulário de inscrição no Novo Portal.

Central do Candidato 1/2 e Central do Candidato2/2

As abas de Central do Candidato, possuem campos que são editáveis conforme a necessidade da Instituição para comunicar com os candidatos no portal do processo seletivo

Integração Rubeus e Prova Fácil

**Rubeus**

A aplicação de Integração Rubeus foi desenvolvida com o objetivo de melhorar a integração de informações relacionadas ao **Educacional**, **Financeiro** e **Processo Seletivo do TOTVS RM**através de sentenças SQL desenvolvidas e cadastradas no TOTVS.

Através dela, há mais facilidade para enviar dados ao mesmo tempo que é possível agendar periodicamente a execução de sentenças.

Saiba mais:

[Integração com a plataforma Rubeus](https://crmrubeus.zendesk.com/hc/pt-br/articles/360040751291-TOTVS-Integra%C3%A7%C3%A3o-com-a-Plataforma-Rubeus)

[Criação do processo seletivo unificado](https://crmrubeus.zendesk.com/hc/pt-br/articles/360015484351-TOTVS-Cria%C3%A7%C3%A3o-do-Processo-Seletivo-Unificado)

,

**Prova Fácil**

Para realizar a integração entre o TOTVS Processo Seletivo e o Prova Fácil, siga as informações da documentação abaixo:  
  
Saiba mais: [Integração com prova fácil](https://tdn.totvs.com/pages/releaseview.action?pageId=602816857)

Matrícula

---

# Forma de inscrição

Caminho: **Módulo Educacional> Processo Seletivo > Cadastro > Processo Seletivo > Aba: Forma de inscrição**

Nessa aba pode ser configurada uma ou mais formas de inscrição para o Processo Seletivo. A possibilidade de definir várias formas de inscrição em um Processo Seletivo agrega uma enorme flexibilidade para a instituição realizadora. Citando alguns exemplos:

* Configurar descontos diferenciados para determinados tipos de candidatos;
* Configurar descontos para inscrições feitas somente em determinados períodos;
* Especificar prazos de vencimentos diferentes para os boletos de inscrição;
* Oferecer condições específicas para inscrições feitas pela Internet;
* Limitar as datas em que será possível fazer inscrições pela Internet;
* Configurar “tipos de indicações” para determinados tipos de candidatos.

Para cada uma das formas de inscrições cadastradas em um Processo Seletivo é necessário detalhar uma série de informações.

**Data do início/Data do término** - Define o período no qual o Sistema permite que sejam realizadas as inscrições do tipo. Quando o período definido expirar, o Sistema deixa de exibir essa forma inscrição tanto do formulário de inscrição Web (Portal) como via Sistema;

**Número de dias para vencimento** - Permite que seja especificado dentro de quantos dias o boleto de inscrição deve vencer a partir da sua emissão;

**Data limite de vencimento** - Limita o parâmetro “Número de dias para vencimento”, fixando uma data máxima para o vencimento. Isso possibilita que seja dado um prazo para que o candidato efetue o pagamento do boleto desde que esse prazo não extrapole determinada data. Por exemplo, pode ser definido que o boleto vencerá dentro de um período de quatro dias após a emissão, porém a sua data de vencimento não poderá extrapolar o término do período de inscrições;

**% Desconto** - Permite que seja configurado um valor de desconto para as inscrições feitas dentro da forma que está sendo criada. Quando for feita uma inscrição desse tipo, o desconto deve ser aplicado com este percentual sobre o valor da taxa de inscrição da área de interesse escolhida. Por exemplo, se for informado para este campo um valor de 50% e o candidato se inscrever em uma área cuja taxa de inscrição seja de R$60,00, o boleto será gerado para ele com o valor de R$30,00;

**Indicação de aluno** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informado o número de registro do aluno que estuda na instituição e indicou o Processo Seletivo para o candidato;

**Indicação de funcionário/professor** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informada a chapa do funcionário/professor que trabalha na instituição e indicou o Processo Seletivo para o candidato;

**Indicação de cliente/fornecedor** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informado o número de registro de algum cliente/fornecedor da instituição que tenha indicado o Processo Seletivo para o candidato.

**Disponível na Internet** - Se essa opção estiver marcada os candidatos podem optar por ela ao se inscreverem pelo Portal.

Todas as formas de inscrição estão disponíveis via Sistema independentemente dessa opção estar ou não marcada.

**Obrigatório ENEM** - Se essa opção estiver marcada e a área ofertada permitir utilizar o ENEM, é obrigatório o preenchimento dos parâmetros de ENEM (Número de inscrição e Ano de referência). Se essa opção estiver marcada e a área ofertada não permitir, o Sistema não deixará concluir a inscrição, solicitando a troca da forma de inscrição.

# Área de interesse ofertada

---

Área de interesse ofertada 

Nesta opção é detalhado o cadastro do “Processo seletivo”, sendo possível incluir e alterar a configuração das áreas de interesse ofertadas.

Selecionar - "Área de interesse ofertada" na aba "Cadastros"

Clicar em "Incluir" para cadastrar uma área de interesse ofertada ou 'Editar' para alterar uma já cadastrada.

Identificação

***Identificação:*** Compreende informações básicas que identificam uma área de interesse ofertada em um processo seletivo.  
Área de interesse: deve ser selecionada uma área de interesse a ser ofertada que exista na tabela auxiliar "Área de Interesse Disponível". Nº de vagas: é o número de vagas do processo seletivo, caso o processo seletivo utilize controle de vagas, este será o valor que o sistema irá utilizar para validar a quantidade de vagas da área de interesse ofertada para permitir ou não mais inscrições ou se irá considerar os candidatos como excedentes caso o número de vagas seja preenchido.

**Observação**: caso o processo seletivo utilize controle de vagas excedentes e o número de vagas for alterado para um valor menor que o número de candidatos inscritos já existente, o sistema irá emitir um alerta sobre a impossibilidade da redução do número de vagas. Á partir da versão 12.1.34 será permitido criar uma área ofertada com 0 vagas, neste caso, todas as inscrições serão excedentes e somente serão alteradas para inscritos quando o número de vagas for incrementado.

***Itinerário Formativo:*** Os itinerários formativos são o conjunto de disciplinas, projetos, oficinas, núcleos de estudo, entre outras situações de trabalho, que os estudantes poderão escolher no ensino médio.

Portanto, poderá ser parametrizado quais itinerários formativos serão ofertados na inscrição do candidato.

A funcionalidade ficara disponível apenas para o processo seletivo do ensino básico, que esteja com o parâmetro "utiliza novo portal de inscrições" habilitado.

Os itinerários serão exibidos se estiverem cadastrados no curso/serie/ turno de acordo com a parametrização informada na área de interesse. Para mais informações sobre itinerário formativo, acesse: [Itinerário Formativo](https://tdn.totvs.com/pages/viewpage.action?pageId=547240322).

Os campos mínimo e máximo refere-se a quantidade de itinerários que o candidato pode selecionar para realizar a inscrição.

Informações Complementares

Compreende as informações adicionais relevantes na definição de uma área de interesse ofertada.

**Idiomas Oferecidos** - Nº Máximo e Nº Mínimo - Definem a quantidade mínima e máxima de idiomas que um candidato pode escolher caso defina esta área de interesse como sua primeira opção;

**Incide desconto** - Se estiver marcada, as configurações de desconto que forem parametrizadas na forma de inscrição escolhida serão aplicadas. Se não estiver marcada, a taxa de inscrição definida na guia identificação será cobrada integralmente independente da forma de inscrição escolhida;

**Utiliza ENEM** - Se esta opção estiver marcada, a nota de ENEM do candidato, quando for de sua vontade, será utilizada na classificação. A utilização de ENEM também impacta no serviço de inscrição do Portal, caso esteja marcada, estará disponível para preenchimento;

**Utiliza controle de faixa etária** - Permite que seja definida uma faixa etária para limitar a idade dos candidatos que podem se inscrever na área. Quando for marcado, os campos idade mínima e máxima serão habilitados para a entrada. Nesse caso a idade máxima deve ser maior que a idade mínima;

**Fórmula para cálculo de pontuação** - Permite que seja definida uma fórmula para ser aplicada no cálculo da pontuação durante o processo de classificação. Sempre que este campo estiver preenchido, a fórmula indicada será utilizada no lugar do cálculo padrão do Sistema.

Informações Financeiras

Esta aba possui um único campo utilizado para configuração da conta/caixa que deve ser informada na geração do lançamento no momento da inscrição. A conta/caixa, de maneira geral, consiste nas informações referentes à conta, agência e banco que receberão as movimentações financeiras geradas nas inscrições do Processo Seletivo.

Esse campo é opcional na área de interesse ofertada. Caso não seja preenchido, o Sistema utilizará a informação cadastrada na conta caixa, localizada nas informações financeiras do Processo Seletivo.

O botão “**Testar geração de lançamento**” é similar ao encontrado no cadastro de Processo Seletivo, no qual, realiza um teste de geração de lançamento com as informações financeiras cadastradas no Processo Seletivo, substituindo a conta/caixa caso esta esteja cadastrada na área ofertada. Caso não exista conta/caixa configurada na área ofertada, o teste será idêntico ao encontrado no Processo Seletivo daquela área ofertada.

Termo de Aceite

Neste campo deve ser informado o corpo do “termo de aceite”, com o qual, os candidatos devem concordar no ato da inscrição.

Distribuir ProvaMatrículaDocumentos Exigidos

Permite que o usuário defina um ou mais documentos que os candidatos devem apresentar para concorrer a área. Os candidatos podem visualizar os documentos exigidos e/ou os que estão pendentes a entrega através do Portal. Para cada documento é necessário informar:

**Documento** - Tipo de documento a partir da lista existente na tabela auxiliar [Documentos](#Tabela_Auxiliar_Documentos);

**Obrigatório** - Se a opção estiver marcada, esta informação afetará o processo “[Alocar Candidatos em Locais de Provas](#processo_alocar_candidatos_locais_prova)”.  O processo não aloca os candidatos com pendência de documentos obrigatórios, exceto quando sinalizado/marcado na configuração do [Processo Seletivo](#Cadastros_Processo_Seletivo), o campo “Aloca sem documentação exigida”.

Idioma Ofertado

Nessa aba deve ser informado os idiomas que são disponibilizados para escolha dos candidatos que optarem por essa área ofertada.  A quantidade de idiomas incluídos depende do valor informado para o campo “Idiomas oferecidos - Nº mínimo” da aba “Informações Complementares”.

Etapas

Nesta aba é possível parametrizar a fase de seleção para cada uma das áreas de um Processo Seletivo. As etapas ocorrem durante o período de seleção de um Processo Seletivo. Cada etapa pode acontecer em diversos horários ao longo de um ou mais dias, em cada horário de uma etapa deve ser aplicado um conjunto de provas.

Etapas>Identificação >Horários

De acordo com as definições acima, para cada etapa é necessário definir um nome e configurar cada um dos horários em que ela deve ocorrer. A ordem das etapas é definida automaticamente na medida em que elas são criadas ou excluídas.

Para cada um dos horários de uma etapa, além da sua data, hora de início e término, deve ser incluída uma lista das provas a serem aplicadas. Cada prova deve receber configurações únicas. A mesma prova não pode ser incluída mais de uma vez em um horário, nem mesmo em horários diferentes de uma mesma etapa.

A figura abaixo ilustra como seria a lista de provas de um horário hipotético pertencente à etapa “Prova”.

Horários>Identificação >Provas da Etapa

Para cada prova devem ser feitas as seguintes configurações ao longo das guias “Identificação” e “Configuração da Prova”. Para acessar a configuração da prova, o usuário deve clicar duas vezes sobre a descrição da prova ou selecionar a prova e clicar em “Editar”.

**Coligada da prova** - Coligada onde a prova foi criada no cadastro de provas do Módulo Totvs Avaliação e Pesquisa;

**Prova** - Deve ser informada uma prova previamente cadastrada e configurada no cadastro de provas do módulo Avaliação e Pesquisa para a coligada selecionada.

**Ordem no caderno** - Para cada horário de prova dentro de uma etapa, deve ser informado em qual posição a prova será impressa no caderno de provas;

**Prova de redação** - Deve estar marcado se a prova em questão for uma prova de redação;

**Idioma associado à prova (para provas de Língua Estrangeira)** - Faz a ligação entre uma prova e um dos idiomas incluídos na lista de idiomas da área ofertada a qual a prova pertence;

**Desclassifica por nota zerada** - Se for marcado, o processo “[Classificar Candidatos](#processo_classificar_candidatos)”, desclassifica os candidatos que não marcarem nenhum ponto na prova;

**Desclassifica por nota abaixo da mínima** - Se for marcado, o processo de classificação vai confrontar a nota obtida pelo candidato com a nota mínima configurada para prova no Módulo Avaliação e Pesquisa. O processo desclassifica o candidato que não atingir a pontuação mínima.

**Configurações de desempate** - Informar qual o peso da prova e a sua prioridade no desempate. Sendo assim, ao realizar a classificação, o Sistema considera o peso da prova ao calcular a nota total obtida. Quando ocorrer um empate entre candidatos, o processo de classificação seleciona o candidato que obteve a maior nota na prova com a maior prioridade.

---

# Locais Disponíveis

• **Módulo Processo Seletivo >Cadastro > Processo Seletivo > Anexos > Locais Disponíveis**

Quando o Processo Seletivo estiver integrado com o Módulo Totvs Educacional, a tela de “Local de Processo Seletivo” exibe somente os locais que pertençam a Processos Seletivos da Filial (Unidade Operacional) do contexto e também de Processos Seletivos que são visíveis para todas as Filiais (Unidades Operacionais). Os locais que podem ser incluídos em um Processo Seletivo, são provenientes da tabela auxiliar Local.

Todas as formas de inscrição estão disponíveis via Sistema independentemente dessa opção estar ou não marcada.

Caso a instituição opte por **não** **cadastrar a prova** completamente no Avaliação e Pesquisa, é **obrigatório** que haja, no mínimo, a inclusão de uma **prova vazia (sem questões).**

Para cada local disponibilizado para o Processo Seletivo, devem ser realizadas as seguintes configurações

# Grupo de Arquivos

É possível criar grupos de arquivos para classificar arquivos vinculados por processo seletivo, esse grupo determina onde os arquivos serão exibidos no Novo portal de inscrições. Temos duas opções de Categoria no grupo de arquivo:

* **Informações** - utilizado para arquivos gerais como editais, manuais de candidatos e outros arquivos de conteúdo informativo.  
  Os arquivos vinculados a esse grupo, serão exibidos na área de Informações para o Processos seletivo que estiver na fase de Inscrição.
* **Resultados** - utilizado para arquivos como gabaritos, cadernos de provas para download, etc.  
  Os arquivos vinculados a esse grupo, serão exibidos na área de Resultados para o Processos seletivo que estiver na fase de Divulgação de Resultados.

**TOTVS Processo Seletivo| Cadastros| Grupo de arquivo| Incluir>Novo**

Para vincular os arquivos a cada processo seletivo, basta seguir o passo abaixo:

**TOTVS Processo Seletivo| Cadastros| Processos Seletivos| Anexos| Arquivos Anexos**

# Geração de link do Portal do Processo Seletivo

**Caminho: TOTVS Processo Seletivo| Parâmetros| Parâmetros do Sistema**

**Caminho: TOTVS Processo Seletivo| Parâmetros | Parâmetros do Sistema| Serviços**

Neste momento  iremos gerar a URL para ser o Link do site do Processo Seletivo

Em portal Processo Seletivo (NOVO), onde esta a frase informe o endereço físico do site até o diretório Portal Processo Seletivo deveremos apagar a palavra Exemplo: e substituir o servidor e a porta que iremos utilizar.

Escolhermos o Processo Seletivo que criamos ;

# 

Marcaremos o Nível de Ensino ;

Clicaremos em Gerar URL

Selecionaremos a URL gerada para link do site

Por fim, copiaremos o link que foi gerado ( Exemplo criado : <http://bh-dev-cni.sp01.local/FrameHTML/web/app/Edu/PortalProcessoSeletivo/?c=2&f=1&ps=16#/eb/informacoes>) nesta URL que foi gerada, salvaremos. Após salvar aparecerá a tela de parâmetro salvos com sucesso.

Agora abriremos uma pagina da internet para abrirmos a pagina que criamos para o processo seletivo.

# Inscrição do candidato (via sistema e via portal)

## Via Portal de inscrições

O candidato ira preencher as informações solicitadas conforme parametrizado no Processo Seletivo;

e ao final da página deverá clicar em Continuar, devendo preencher todas as informações que foram solicitadas, deve-se preencher as abas  **DADOS BÁSICOS, RESPONSÁVEIS E DADOS DO CURSO, QUESTIONÁRIO**

## Via secretaria

O funcionário designado ao atendimento ao candidato deve seguir o seguinte caminho

**Caminho: Módulo Educacional| Processo Seletivo| Inscrição |Inscrição de Candidato| Incluir**

* Informar o Processo Seletivo
* informar Pessoa (Novo Portal)
* Informar a Forma de Inscrição
* Informar o Local de realização

Na tela abaixo , devera ser informado se o candidato fara a prova como Treineiro;

Informar se o candidato possui alguma necessidade especial;

Para que o processo Seletivo aceite candidatos com Necessidades Especiais é necessário cadastrar também, locais com acessibilidade.

Informar se o aluno foi indicado por um aluno, por cliente/ fornecedor ou funcionário professor (\*caso necessite informar);

Informar a área de interesse do candidato;

Caso a prova seja ofertada em mais de um idioma o aluno deverá selecionar qual será o que ele fará a prova.

Neste exemplo não foi parametrizado idiomas, portanto a prova será e português.

Termo de Aceite

Informar se o candidato esta vindo de alguma empresa com indicação, se o aluno está solicitando taxa de isenção e qual é a justificativa;

Clicar em salvar e a inscrição estará realizada.

# Confirmar inscrições

**Caminho: TOTVS Processo Seletivo |Selecionar o Processo Seletivo desejado |Anexo>Candidato Inscrito**

Existem três status possíveis para uma inscrição, são eles: Inscrito (pendente de confirmação de pagamento), Candidato (inscrição confirmada) e Inscrição cancelada.

Quando uma inscrição for realizada o status inicial da mesma será “Inscrito”. Porém, se o valor da inscrição for zero ou a forma de inscrição aplicar 100% de desconto, o status da inscrição passará a ser “Candidato”.  
Durante o período de inscrições de um Processo Seletivo, os bancos conveniados com a instituição de ensino, ou seja, os que estão habilitados a receberem os boletos de pagamento de taxa de inscrição deverão enviar o arquivo CNAB. Ao receber o arquivo CNAB, a instituição deverá utilizar o Módulo Gestão Financeira para baixar os lançamentos pagos pelos candidatos.  
Após a baixa, basta executar este processo que todos os candidatos que estiverem com o status do lançamento igual a “Quitado” passarão a ter o status de inscrição igual a “Candidato”.

# Enviar E-mails

•**Caminho: Módulo Educacional| Processo Seletivo| Cadastro| Processo Seletivo | Processos | Enviar E-mails**

 Confirmação de inscrição   **Executar > Fechar.**

O mesmo processo deverá ser realizado para informar o Local de prova do candidato.

# Alocar profissionais

• **Módulo Processo Seletivo > Cadastro > Processo Seletivo > Processos > Alocar profissionais\***

\*Caso seja necessário

# Alocar Candidatos

**• Módulo Processo Seletivo > Cadastro > Processo Seletivo > Processos > Alocar candidatos**

Este processo é executado a partir da tela de “Processos Seletivos”. Todo candidato ao realizar sua inscrição em um Processo Seletivo, escolhe um local para realizar a prova dentre os locais disponíveis. A partir deste local escolhido pelo candidato, o processo em questão, define em qual cidade, campus e sala o mesmo fará as provas de seleção.

Para que os candidatos de uma área ofertada sejam alocados, é preciso que estejam cadastrados os horários para a(s) etapa(s) desta área.

Neste processo é possível definir quatro configurações que determinam como será realizada a alocação dos candidatos, conforme definição a seguir:

Quando um candidato for alocado em um local, significa que ele ocupará o lugar ao longo de todo o dia para o qual ele foi alocado. Mesmo que sua área ofertada possua um horário de seleção somente na parte da manhã, será considerado que esse candidato ocupará o local também na parte da tarde.

Em um local que suporte uma ou mais necessidades especiais, serão alocados somente os candidatos portadores delas. Nunca serão mesclados em um mesmo local candidato portadores de deficiência com candidatos não portadores.

# Distribuir Caderno de Prova

• **Caminho: Módulo Educacional| Processo Seletivo | Cadastro | Processo Seletivo | Processos | Distribuir caderno de prova**

O processo serve para estabelecer o vínculo entre os candidatos já alocados em uma sala e as respectivas provas que ele deve realizar.

O processo é também responsável por ligar os candidatos às respectivas provas, criadas no Módulo Avaliação e Pesquisa, relativas à sua área de interesse. Esse vínculo é necessário para que os processos, correção e classificação sejam executados.

# Registrar Presença de candidatos

• **Caminho: Módulo Educacional| Processo Seletivo| Cadastro | Processo Seletivo | Processos | Registrar Presença de candidatos**

Este processo permiti registrar a presença e falta dos candidatos que se inscreveram em um Processo Seletivo.

Sistema exibe todos os candidatos que foram alocados nela. Os candidatos que estiverem com o sinal de marcado, estão registrados no Sistema como presentes e os desmarcados como ausentes.  
Se a área ofertada em que um candidato se escreveu possuir mais de uma etapa, ao clicar no sinal de mais (+), aparecerão todos os dias destas etapas, sendo possível registrar a presença ou falta por etapa. Os candidatos presentes ficarão com o ícone na cor verde e os ausentes na cor vermelha.

# Classificação Manual

A “Classificação Manual” é uma forma de classificação altamente flexível na qual o usuário é o responsável por digitar o status, a classificação e as notas dos candidatos. Quando o usuário optar por essa forma de classificação, o assistente exibirá o passo “Classificação Manual”. Veja a ilustração a seguir:

Nessa interface, o usuário deve fornecer os dados de cada candidato para cada uma das áreas ofertadas que deseja classificar. Seguem os passos para classificar manualmente uma área ofertada:

1. **a) Selecionar a área ofertada** - Após selecionar uma área ofertada na lista, o grid exibe todos os candidatos pertencentes a ela. No grid será apresentado todos os candidatos da área ofertada cuja inscrição não tenha sido cancelada. Os candidatos que já foram classificados anteriormente e já foram convocados em alguma chamada aparecerão desabilitados para edição.
2. **b) Classificar todos os candidatos ­**- A classificação de um candidato deve ser feita diretamente no grid. O primeiro passo é alterar o status do candidato. Ao posicionar na coluna “Status” serão exibidos os status de classificação possíveis. De acordo com o status selecionado, os campos “Classificação” e “Pontuação” serão habilitados/desabilitados. Por exemplo, quando for selecionado um dos possíveis status de “desclassificação”, o campo “Classificação” será desabilitado. Esse comportamento visa garantir que a classificação de cada candidato seja feita de forma coerente. Os status disponíveis na lista de status possíveis de serem usados são todos os que tiverem o valor "Sim" para o campo "Disponível para classificação manual” na tabela auxiliar [Status da Opção](#Tabela_Auxiliar_Status_Opcao).
   1. **c) Validar os dados preenchidos para a área ofertada** - Após classificar/desclassificar todos os candidatos, a classificação para a área ofertada deve ser validada. Para isso o usuário deve clicar no botão “Validar” localizado na barra de ferramentas logo acima do grid. A classificação feita para uma área ofertada será considerada válida quando:
   * O campo “Classificação” foi preenchido para todos os candidatos classificados como “Classificado para chamada” ou “Classificação pendente”.
   * Não existirem candidatos com o mesmo valor preenchido para o campo “Classificação”;
   * Existirem candidatos que não foram mantidos como inscritos no grid, mas o usuário optar por considerar a classificação da área válida mesmo assim. O Sistema exibirá uma mensagem de confirmação nesse caso;
   * Existirem intervalos na sequência de classificação, mas o usuário optar por considerar a classificação da área válida mesmo assim. O Sistema exibirá uma mensagem de confirmação nesse caso.
3. Quando a classificação for válida, o Sistema informa ao usuário e o ícone indicador de status será alterado do símbolo de alerta na cor amarela para o símbolo de validado na cor verde.

   A interface ainda disponibiliza para os usuários os botões “Limpar”, “Classificações” e “Ocultar/Exibir candidatos chamados”. O primeiro permite que o usuário retorne o valor do status de todos os candidatos para “Inscrito para Seleção”. Ele permite também que todos os valores preenchidos para “Classificação” e “Pontuação” sejam excluídos. O botão “Classificação” permite que a “Classificação” de cada candidato seja preenchida automaticamente de três formas:

   * “De acordo com a ordenação do Grid”- Primeiramente os candidatos que estiverem com o status “Inscrito para seleção” terão o status alterado para “Classificado para chamada”. Em seguida todos os candidatos com que estiverem com o status “Classificado para chamada” terão a “Classificação” preenchida de acordo com a posição do candidato no grid.
   * “De acordo com a pontuação” - Todos os candidatos que tiverem “Pontuação” terão o campo “Classificação” preenchido. O preenchimento da “Classificação” ocorrerá da maior para a menor “Pontuação”. Dessa forma, o candidato melhor classificado será o que tiver maior pontuação. Caso existam candidatos com a mesma pontuação, o Sistema definirá aleatoriamente quem será mais bem classificado.
   * “De acordo com o número de inscrição - Primeiramente os candidatos que estiverem com o status “Inscrito para seleção” terão o status alterado para “Classificado para chamada”. Em seguida estes candidatos serão classificados de acordo com a ordem de inscrição. Ou seja, candidatos que se inscreveram primeiro serão os melhores colocados.

   Todas as três opções de preenchimento automático irão considerar se já foi rodada a classificação anteriormente. Caso tenha sido, o preenchimento iniciará a sequência de classificação a partir do último colocado nas classificações anteriores. Será considerado também se o Processo Seletivo foi configurado para utilizar controle de vagas. Nesse caso, o preenchimento automático, mesmo existindo mais candidatos, somente classificará um número de candidatos igual ao número de vagas disponíveis na área ofertada.

   Além dos comandos para preenchimento automático, o botão “Classificação” disponibiliza também o menu “Sugerir próximo número de classificação”.  Quando essa opção estiver selecionada, sempre que o usuário posicionar o cursor no campo “Classificação”, se este estiver habilitado e
4. ainda não tiver sido preenchido, será mostrado um menu de contexto sugerindo a próxima classificação, conforme a ilustração abaixo:

# Classificar Candidatos

• **Caminho: Módulo Educacional| Processo Seletivo | Cadastro | Processo Seletivo|  Processos | Classificar  candidatos>Consultar (ou Não) o Registro de Presença**

# Chamada de Candidato Aprovado

• **Caminho: Módulo Educacional| Processo Seletivo | Cadastro | Processo Seletivo | Processos | Chamada de candidato aprovado**

Após a Chamada o Candidato, o mesmo está apto para a matricula (Status do candidato = EM CHAMADA). O Sistema possibilita o envio de e-mail para os candidatos aprovados, convocados para matricula.

# Enviar e-mails

• **Caminho: Módulo Educacional | Processo Seletivo| Cadastro| Processo Seletivo| Processos | Enviar E-mails**

 E-mail de convocação para matrícula

## Registrar Comparecimento em chamadas

• **Caminho: Módulo Educacional| Processo Seletivo | Cadastro | Processo Seletivo | Processos | Registrar comparecimento em chamadas**
