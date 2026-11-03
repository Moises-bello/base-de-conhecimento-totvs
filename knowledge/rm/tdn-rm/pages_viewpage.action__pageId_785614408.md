---
content_hash: 75b4e97d4e7c9965b01cf1dfec70fe63b0465d6e9a48c9247ee939a63d4ce994
fetched_at: '2026-06-29T00:11:38.866477+00:00'
page_id: '785614408'
product: rm
source: tdn-rm
title: Integração RM X Feedz
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=785614408
version: 117
---

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Parametrização**

## **01. VERSÕES**

falseA partir dos patches:


* [Como realizar a integração da Feedz com o RM?](https://ajuda.feedz.com.br/pt-BR/articles/9210130-como-realizar-a-integracao-da-feedz-com-o-rm)


* [DT - Integração RM x Feedz - Chefe/Supervisor Externo](https://tdn.totvs.com/pages/viewpage.action?pageId=860243746)
* [DT - Integração RM x Feedz - Utiliza token por filial](https://tdn.totvs.com/pages/viewpage.action?pageId=868233301)
* [DT - Integração RM x Feedz - Concatenação de Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=873232738)
* [DT - Integração RM x Feedz - Filial utilizar o NOMEFANTASIA ao invés do NOME](https://tdn.totvs.com/pages/viewpage.action?pageId=873232869)
* [DT - Integração RM x Feedz - Concatenação de Coligada - Inclusão campo Matricula](https://tdn.totvs.com/pages/viewpage.action?pageId=918389806)
* [DT - Integração RM x Feedz - Concatenação de Coligada - Inclusão do separador (-)](https://tdn.totvs.com/pages/viewpage.action?pageId=918390035)

* [DT - Integração RM x Feedz - Log Integração](https://tdn.totvs.com/pages/releaseview.action?pageId=1012526447)
* [DT - Integração RM x Feedz - Utiliza token por Seção do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=1045007554)

## **02. VISÃO GERAL**

Ter uma funcionalidade nativa que automatize a carga e integração dos dados pessoais dos funcionários no sistema Feedz. Isso garantirá sincronização automática para processos como avaliação de desempenho e PDI, agilizando as operações e proporcionando maior integração entre os sistemas.

## **03. EXEMPLO DE UTILIZAÇÃO**

Será possível realizar a carga e integração de forma online dos dados contratuais dos funcionários que estão no ERP para o sistema Feedz.

Os dados abrangidos na integração incluem:

* + Registros Auxiliares: Departamento, Cargo e Unidade
  + Pessoas: Gestor direto e Colaborador

    - Nome
    - Nome Social
    - E-mail
    - Data de admissão
    - Nascimento
    - Data de demissão
    - Tipo/Motivo de demissão

**OBSERVAÇÃO:**

Para garantir o envio correto da tag <managerIntegrationId>, é fundamental que o chefe/supervisor associado à estrutura da seção tenha informações registradas na tabela PFUNC.

## **04. PARAMETRIZAÇÃO**

 

11ParametrizaçãoParametrização

1) Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 01.05.01 - TOTVS RH | Avaliação e Desempenho

2) Acesse RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.10 - TOTVS RH | Avaliação e Desempenho selecione a opção Feedz e cadastre os dados para a integração.

**Utiliza token por Filial**: Com esse parâmetro será possível fazer com que o RM transmita as informações do funcionário conforme sua filial cadastrada para o ambiente vinculado da feedz correspondente (conforme Token indicado), marcando o parâmetro, o sistema irá habilitar a Aba **Token X Filiais** para possibilitar as vinculações. Veja mais detalhes no link [DT - Integração RM x Feedz - Utiliza token por filial](https://tdn.totvs.com/pages/viewpage.action?pageId=868233301)

**Utiliza token por Seção**: Com esse parâmetro será possível fazer com que o RM transmita as informações do funcionário conforme sua seção cadastrada para o ambiente vinculado da feedz correspondente (conforme Token indicado), marcando o parâmetro, o sistema irá habilitar a Aba **Token X Seções** para possibilitar as vinculações. Veja mais detalhes no link [DT - Integração RM x Feedz - Utiliza token por Seção do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=1045007554).

       

**Concatenar Descrição do Cargo (Descrição + Código)**: Ao selecionar esse parâmetro, o sistema irá combinar a descrição da função com o seu código correspondente.

Por exemplo, se o código da função for "0001" e a descrição for "Gerente", após ativar esse parâmetro, o sistema enviará para a Feedz a informação "Gerente 0001". 

Importante ressaltar que, caso o parâmetro não esteja marcado e houver Cargos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

**Concatenar Descrição do Departamento (Descrição + Código)**: Ao selecionar esse parâmetro, o sistema incluirá tanto a descrição da seção quanto o seu código correspondente.

Por exemplo, se o código da seção for "01.01" e a descrição for "Administrativa", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "Administrativa 01.01".

Importante ressaltar que, caso o parâmetro não esteja marcado e houver Departamentos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

**Concatenar Descrição da Unidade (Descrição + Código)**: Ao selecionar esse parâmetro, o sistema incluirá tanto a descrição (GFILIAL.NOME) da filial quanto o seu código correspondente.

Por exemplo, se o código da filial "1" e a descrição for "TOTVS - Filial Belo Horizonte", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "TOTVS - Filial Belo Horizonte1".

Importante ressaltar que, caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

**Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula****:**Ao selecionar esse parâmetro, o sistema adicionará o código da Coligada (GCOLIGADA.CODCOLIGADA) seguido de um separador (- ) nos campos "Name" e "IntegrationId" dos registros auxiliares de Cargo (Função), Departamento (Seção) e Unidade (Filial), e também do campo "Registration" (Chapa do funcionário).

**Exemplo I:**

* + Código de Coligada = 8
  + Código da Filial = 1
  + Descrição da Filial = TOTVS - Filial Belo Horizonte
  + Parâmetro "**Concatenar Descrição da Unidade (Descrição + Código)**" marcado

Com o parâmetro "**Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula**" MARCADO, o retorno será:

* + Name: 8-TOTVS - Filial Belo Horizonte1
  + Integrationld = 8-1

Com o parâmetro "**Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula**" DESMARCADO, o retorno será:

* + Name: TOTVS - Filial Belo Horizonte1
  + Integrationld = 1

**ATENÇÃO:** Caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, sistema da Feedz irá sobreescrever as informações a cada coligada enviada. Isso acontece devido à descrição ser um elemento-chave na Feedz.

**Exemplo II:**

* + Código de Coligada = 2
  + Chapa: 101020

Com o parâmetro "**Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula**" MARCADO, o retorno será:

* + registration = 2-101020

Com o parâmetro "**Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula**" DESMARCADO, o retorno será:

* + registration = 101020

**Considerar Nome Fantasia para a Unidade:** Ao selecionar esse parâmetro, o sistema incluirá a descrição (GFILIAL.NOMEFANTASIA) no envio da Unidade (Filial).

**ATENÇÃO:** Caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

ATENÇÃO:

A partir dos patches (12.1.2406.241, 12.1.2410.178, 12.1.2502.105 e superiores), ao preencher o token, o produto marcará automaticamente todos os parâmetros de concatenação, sendo eles:

* Concatenar Descrição do Cargo (Descrição + Código)
* Concatenar Descrição do Departamento (Descrição + Código)
* Concatenar Descrição da Unidade (Descrição + Código)
* Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula

Isso evitará problemas de duplicidade de códigos na Feedz.

**Enviar Chefe/Supervisor Substituto:**

Permite definir se os chefes e supervisores com a flag **“Chefe/Supervisor Substituto”**, disponível no menu Administração de Pessoal | Chefes e Supervisores, devem ser incluídos no envio de dados na integração entre a Folha de Pagamento e o

🔔 **Atenção:** Por regra de negócio, este parâmetro virá **desmarcado por padrão** na atualização do release.

Mais detalhes e os patches de liberação desse parâmetro estão disponíveis no link:

PONTOS IMPORTANTES DA INTEGRAÇÃO:

* No campo de descrição, a presença de caracteres especiais [`, ', ", =, <, >]  resultará em erro.
* Sempre que o funcionário for enviado novamente, ele será substituído na FEEDZ.
* Quando há mais de um chefe ou supervisor na mesma seção, é considerado o chefe com a menor chapa.
* São considerados tanto o chefe quanto o supervisor. O supervisor é enviado apenas se não houver chefe na seção ou na hierarquia.
* **Mais informações acesse:** [Como realizar a integração da Feedz com o RM?](https://ajuda.feedz.com.br/pt-BR/articles/9210130-como-realizar-a-integracao-da-feedz-com-o-rm)
3De/ParaDe/Para3De/ParaDe/Para

**1 - PESSOAS**

**1.1 - DADOS ENVIADOS NO ENDPOINT DE PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o Feedz | PFUNC.CODPESSOA |
| name | Nome | PPESSOA.NOME |
| socialName | Nome de preferência | PPESSOA.NOMESOCIAL |
| email | Email | PPESSOA.EMAIL |
| admissionDate | Data de admissão | PFUNC.DATAADMISSAO |
| lastRaiseDate | Data de último aumento | PFHSTSAL.DATAMUDANCA |
| birthDate | Data de aniversário | PPESSOA.DTNASCIMENTO |
| demissionDate | Data de demissão | PFUNC.DATADEMISSAO |
| experienceEndDate | Data do fim do período de experiência | PFUNC.FIMPRAZOCONTR |
| dismissalType | Tipo de demissão: 1 - Pedido de desligamento 2 - Sem justa causa 3 - Com justa causa   | DE RM | PARA FEEDZ | | --- | --- | | 3 - Inic.Empregado com justa causa | 1 - Pedido de desligamento. | | 4 - Inic.Empregado sem justa causa | 1 - Pedido de desligamento | | 2 - Inic.Empregador sem justa | 2 - Sem justa causa | | 1 - Inic.Empregador com justa causa | 3 - Com justa causa | | Valores <> dos citados acima | 2 - Sem justa causa | | PFUNC.TIPODEMISSAO |
| hiringTypeIntegrationId | Identificador único de integração do regime de contratação | PFUNC.CODTIPO |
| departmentIntegrationId | Identificador único de integração da área da pessoa | PFUNC.CODSECAO |
| positionIntegrationId | Identificador único de integração do cargo da pessoa | PFUNC.CODFUNCAO |
| positionLevelIntegrationId | Identificador único de integração do nível cargo da pessoa | PFUNC.CODNIVELSAL |
| facilityIntegrationId | Identificador único de integração da unidade da pessoa | PFUNC.CODFILIAL |
| managerIntegrationId | Identificador único de integração do líder imediato da pessoa | Código da Pessoa do chefe imediato, verificando a estrutura de Chefe/Supervisor  ou Hierarquia por Posição (quando ativada). |
| registration | Chapa do funcionário | PFUNC.CHAPA |
| cpf | CPF do funcionário | PPESSOA.CPF |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.1 - DADOS ENVIADOS NO ENDPOINT DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o Feedz | PFUNCAO.CODIGO |
| name | Nome | PFUNCAO.NOME |
| positionGroupIntegrationId | Identificador único de integração do grupo de cargo do cargo | PFUNCAO.CARGO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.2 - DADOS ENVIADOS NO ENDPOINT DE UNIDADES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o Feedz | GFILIAL.CODFILIAL |
| name | Nome | GFILIAL.NOME |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.3 - DADOS ENVIADOS NO ENDPOINT DE DEPARTAMENTO**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem | PSECAO.CODIGO |
| name | Nome | PSECAO.DESCRICAO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

4Erros de validação e seus códigosErros de validação e seus códigos3De/ParaDe/Para

**Lista de erros de validação e seus códigos**

Alguns erros podem acontecer durante o processamento do lote enviado ou durante a validação dos itens do lote enviado, sendo eles:

|  |  |  |
| --- | --- | --- |
| Código | Mensagem | Detalhes |
| Sem código | Nenhum Funcionário atende a seleção. | O erro acontece quando a Função à qual o funcionário está alocado não possui o cargo registrado em seu cadastro, ou o funcionário está com históricos incompletos. Para solucionar o erro acesse o [Link.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28206773411095-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Feedz-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o) |
| 500 | Ocorreu um problema ao tentar conectar a plataforma da Feedz. | 1) Verificar se o cliente possui bloqueio de firewall e, caso positivo, liberar os endereços necessários.  2) Garantir que os seguintes endereços estejam liberados para conexões externas:   * + Produção: <https://integrations.feedz.com.br>   + Sandbox: <https://integrations.feedz.dev>   Se o erro persistir e não estiver relacionado a essas configurações, acionar o suporte da Feedz. |
| 0100 | Ocorreu um erro inesperado! > Não foi possível salvar o colaborador. | Ocorre quando o e-mail enviado no colaborador ou líder já existe na base da Feedz. Por se tratar de um campo pessoal, este e-mail não será listado na mensagem. |
| 4998 | Id do processo não encontrado | Significa que o processId informado na requisição de consulta de lotes está incorreto. |
| 4999 | Ocorreu um erro inesperado! | Representa erros genéricos ou inesperados que podem acontecer no servidor ou que podem ser gerados por algum aspecto incorreto não previsto do lote enviado. |
| 5000 | Token inválido ou expirado! / Bearer token não informado. | Isso indica que o token não foi informado na requisição ou informado não é válido. É necessário conferir se o token informado é igual à chave API na plataforma Feedz. Em caso afirmativo, é necessário gerar outra chave. |
| 5000 | Body vazio | Significa que foi enviada uma requisição para gravar um lote, mas sem nenhum dado. |
| 5001 | O total de itens enviados no corpo da requisição excede o limite de 100 registros. Todos os registros foram ignorados no processamento. | Ocorre ao enviar um lote com mais de 100 registros. |
| 5003 | A pessoa NPE (IntegrationId = IDN) está referenciando um gestor que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um gestor que ainda não foi cadastrado. |
| 5004 | A pessoa NPE (IntegrationId = IDN) está referenciando ela mesmo como chefe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando ela mesma como gestora (integrationId = managerIntegrationId). |
| 5005 | A pessoa NPE (IntegrationId = IDN) está referenciando um departamento que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um departamento que ainda não foi cadastrado. |
| 5006 | A pessoa NPE (IntegrationId = IDN) está referenciando uma unidade que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a uma unidade que ainda não foi cadastrada. |
| 5008 | A pessoa NPE (IntegrationId = IDN) está referenciando um cargo que não existe. Essa pessoa não será importada. | Esse erro ocorre ao tentar cadastrar um colaborador, vinculando a um cargo que ainda não foi cadastrado. |
| 5009 | O ID de integração (IntegrationId) é obrigatório e não foi informado para a Pessoa NPE. Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar se id de integração. |
| 5011 | O nome (Name) é obrigatório e não foi informado para a Pessoa (IntegrationId = IDN). Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar seu nome. |
| 512 | O e-mail (Email) é obrigatório e não foi informado para a Pessoa 'NPE' (IntegrationId = IDN). Essa pessoa não será importada. | Ocorre ao enviar uma pessoa e não informar seu e-mail. |
| 5013 | A pessoa 'NPE' (IntegrationId = IDN) possui o mesmo e-mail de outra pessoa da lista de pessoas enviadas ou da base. Essa pessoa não será importada. | Essa validação existe para evitar cadastrar pessoas duplicadas na base. Assim não é possível cadastrar dois e-mails iguais para integrationIds diferentes e vice versa. |
| 5014 | A pessoa 'NPE' (IntegrationId = IDN) deve ter o nome digitado somente com caracteres com nome, sobrenome e apenas 1(um) espaço entre eles. | Esse erro ocorre ao informar um nome inválido. |
| 5015 | A pessoa 'NPE' (IntegrationId = IDN) não pode ter o apelido igual ao nome. | Ocorre quando o name é igual ao socialName. |
| 5016 | O email fornecido 'EML' para a pessoa 'NPE' (IntegrationId = IDN) não está em um formato válido. | Ocorre ao enviar uma pessoa com o e-mail em formato inválido. |
| 5017 | O registro com o nome 'NRA' não foi salvo durante o processamento porque o campo 'IntegrationId' não foi informado." | Ocorre ao enviar qualquer registro auxiliar e não informar o integrationId. |
| 5018 | O registro com o código 'IDN' não foi salvo durante o processamento porque o campo 'Name' não foi informado. | Ocorre ao enviar qualquer registro auxiliar e não informar o nome. |
| 5030 | Quando informado a data de demissão deve ser também informado o motivo (dismissalType). | Ocorre ao enviar data de demissão e não informar o motivo. |
| 5031 | Deve ser informado o motivo da demissão (dismissalType) apenas quando for informado a data de demissão. | Ocorre ao enviar motivo da demissão e não informar a data de demissão. |
| 5032 | A data de admissão não pode ser maior que a data de demissão. | Ocorre ao enviar uma data de admissão posterior à data de demissão. |
| 5048 | O ID de integração do líder (managerIntegrationId = MII) informado para a pessoa (personIntegrationId = IDN) não existe. | Ocorre ao tentar vincular pessoa e líder pela rota persons-bind e não ter esse líder cadastrado previamente na plataforma. |
| 5049 | O ID de integração da pessoa (personIntegrationId = IDN) informada não existe. | Ocorre ao tentar vincular pessoa e líder pela rota persons-bind e não ter esse colaborador cadastrado previamente na plataforma. |
| 5050 | Uma pessoa (personIntegrationId = IDN) não pode ser líder de sí próprio | Ocorre ao tentar vincular uma pessoa a ela mesma como líder (personIntegrationId = managerIntegrationId) através da rota persons-bind. |

true4IntegraçãoIntegração

Através do menu Administração de Pessoal  TOTVS RH | Avaliação e Desempenho é possível realizar a integração dos dados dos funcionários de forma nativa no produto, utilizando os filtros disponíveis na tela.

Na tela acima, é possível parametrizar para enviar os **Funcionários e Cadastros Auxiliares** ou realizar a **Associação de Líderes**. É obrigatório escolher uma das duas opções.

Ao selecionar **Funcionários e Cadastros Auxiliares**, o sistema gerará todos os funcionários de acordo com a parametrização de **Quebra de Seção** e **Seleção de Funcionários**. Além disso, serão gerados os cadastros de **Função/Cargo**, **Filiais/Unidades** e **Seções/Departamentos** que estão relacionados aos funcionários selecionados.

Ao marcar somente a flag **"Fazer Associação de Líderes"**, o sistema associará automaticamente os chefes parametrizados nas seções do cadastro de Chefe/Supervisor aos subordinados alocados nessas mesmas seções. Se em um mesmo nível de seção, estiverem cadastrados tanto um chefe quanto um supervisor, por regra será priorizado o chefe.   
  
Marcando a flag **"Fazer Associação de Líderes"** e **"Prioriza chefe master no envio"** o sistema passará a validar a flag "Master" no cadastro de chefe/supervisor.

**Exemplo:**

* + Supervisor e Chefe com o master desmarcado: Será priorizado o envio do Chefe.
  + Supervisor e Chefe com o master marcado: Será priorizado o envio do Chefe.
  + Supervisor com o master marcado e Chefe desmarcado: Será priorizado o envio do Supervisor.
  + 2 Chefes no mesmo nível de seção com o master desmarcado: Será enviado o Chefe com a menor chapa.
  + 2 Chefes no mesmo nível de seção com o master marcado: Será enviado o Chefe com a menor chapa.

**ATENÇÃO****:** Na plataforma Feedz, por motivos estruturais, não é possível associar um líder de uma base de dados a um funcionário de outra base dados. Por exemplo, o líder/chefe da filial 01 (RM), cadastrado na base 01 (Token 1 Feedz) não pode ser vinculado a um subordinado da filial 02 (RM), cadastrado na base 02 (Token 2 Feedz).

Com o recurso de **Agendamento** de tarefas, você pode programar integrações de entidades para ocorrerem automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

  

**ATENÇÃO**: Para evitar impacto na performance, recomenda-se que o agendamento seja programado para, no máximo, duas vezes ao dia.
