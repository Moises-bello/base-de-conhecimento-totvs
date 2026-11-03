---
article_id: 18727391205271
category: Quírons
content_hash: efe459425d2aeb002aa6b0cb4e505e80248e35bd6b58bc6aab58757ffe4d612a
fetched_at: '2026-06-28T22:42:52.207085+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - MDT - Quírons - O que é, e como funciona a integração
  Protheus x Quírons
type: support-article
updated_at: '2025-07-09T15:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727391205271-RH-Linha-Protheus-MDT-Qu%C3%ADrons-O-que-%C3%A9-e-como-funciona-a-integra%C3%A7%C3%A3o-Protheus-x-Qu%C3%ADrons
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18727376639767) Tempo aproximado para leitura: **00:10:00 min****Dúvida**O que é, e como funciona a integração de envio de dados Protheus x Quírons?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução****Protheus** é um sistema **ERP** (Software de Gestão Empresarial) e **Quírons** é um software **destinado à Saúde e Segurança do Trabalho**. A integração entre os dois produtos têm como papel principal, permitir o **compartilhamento de dados comuns entre os sistemas**, especialistas em cada função, utilizando um mesmo cadastro de Funcionário, por exemplo.  
  
As integrações entre os **dois produtos (Quírons e Protheus)** ocorrem através de **API's**. As informações existentes no **Protheus utilizam as API's do Quírons** para atualizar suas informações e as informações no **Quírons utilizam as API's do Protheus** para se atualizarem.  
  
**API's** são **funcionalidades** disponibilizadas por **cada produto**, que podem ser **executados** por **outros serviços**, desta forma **a API executa** funções **dentro do próprio produto**, para **retornar** com as **informações** que serão **enviadas de volta** ao serviço solicitante.  
  
Um serviço **API é uma comunicação entre serviços**, ocorrida diretamente via **web**. Este tipo de comunicação possui alguns**tipos de mensagens padrões de erro**, conforme detalhado abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Codigos de erros HTTP mais comuns](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045402233-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Codigos-de-erros-HTTP-mais-comuns)  
  
As API's de cada produto podem ser encontradas nos seguintes caminhos:  
**Protheus**: disponibilizado em seu servidor, através do serviço REST, como apresentado em [Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793)  
**Quírons**: disponibilizado o link específico para seu ambiente, após contratação do serviço, mas a documentação de cada API pode ser acessada em: <https://app.swaggerhub.com/apis/jacksjm/quirons/1.0.0>  
Para habilitar esta integração entre os produtos, são necessários alguns passos, conforme enumerados abaixo (recomendável realizar os passos na mesma ordem exemplificada). Esta documentação haverá a apresentação **somente** da parte **Protheus**:

1. Atualização do Repositório (fontes) e Dicionário de Dados com o pacote de Expedição Contínua do RH mais recente disponível: [RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282-RH-Linha-Protheus-MEU-RH-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente?source=search)  
   Esta atualização garantirá que as API's do Protheus utilizadas na integração estejam em sua última versão homologada e que todos os campos nas tabelas do RH envolvidas estejam criados e com as propriedades corretas. Como haverá atualização de dicionário, isso implica na execução do processo de UPDDISTR com os arquivos contidos no pacote listado acima: [MP - FIS - Como Processar o UPDDISTR para atualização de dicionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152)
2. Criação dos campos de LOG (de Inclusão e Alteração) necessários para a integração, nas tabelas que são atualmente utilizadas, conforme apresentado na tabela abaixo, seguindo o exemplo documentado em [MP - FRAME - Rotinas de Log e Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024872752-MP-FRAME-Rotinas-de-Log-e-Auditoria):  

   |  |  |
   | --- | --- |
   | **Dados** | **Tabela** |
   | Tipos de Abono | SP6 |
   | Centro de Custo | CTT |
   | Turno de Trabalho | SR6 |
   | Funções | SRJ |
   | Tipos de Ausência | RCM |
   | Tipos de Estabilidade | RCC |
   | Tipos de Treinamento | RA2 |
3. Criação de serviço Webservice REST EXCLUSIVO para utilização desta integração, seguindo as chaves recomendadas de criação, como detalhado em: [Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292);
4. Criação/disponibilização dos seguintes itens no Menu no módulo 07 - Gestão de Pessoal:  

   |  |  |
   | --- | --- |
   | **Nome da Rotina** | **Código/Nome da Função Protheus** |
   | Carga Inicial | GPEM925 |
   | Parâmetros | GPEM926 |
   | Monitor | GPEM924 |

     
   Para criação de itens no Menu do Protheus, caso os itens acima não existam, pode seguir conforme a documentação [MP - FRAME - Personalização de Menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-MP-FRAME-Personaliza%C3%A7%C3%A3o-de-Menus).
5. Habilitar/alterar o conteúdo do parâmetro **MV\_RHNG** para o valor **.T.**  
   Para alterar o conteúdo de parâmetros, pode realizar no módulo de Configurador (SIGACFG), na rotina de Parâmetros, conforme documentado em [Parâmetros (CFGX017 - SIGACFG)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=306857908)
6. Acessar a rotina "Parâmetros", adicionada ao Menu no passo 4, para preenchimento dos dados de acesso e endereço do Quírons, como o exemplo abaixo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19344550637335)  
     
   As informações devem ser preenchidas da seguinte forma:  

   |  |  |
   | --- | --- |
   | **Campo** | **Descrição** |
   | URI | Endereço da página web cujo utiliza para acessar o sistema Quírons |
   | Usuário | Usuário administrador do Quírons |
   | Senha | Senha do Usuário Administrador do Quírons |
7. Criar um novo agendamento/schedule no Configurador, para a rotina GPEM923, responsável por realizar o envio das informações na Fila de Processamento ao Quírons. O agendamento deve ser criado da seguinte forma:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19344550639767)  
     
   Para criar um agendamento, é necessário acessar o módulo do Configurador (SIGACFG), na rotina de Schedule, conforme documentado em [Schedule (CFGA010 - SIGACFG)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=306855653)  
     
   Obs.: A recorrência, horário de execução e vezes de execução por dia podem ser configurados da forma que melhor atender as necessidades da empresa.
8. Acessar a rotina "Carga Inicial" criada no passo 4, para escolher quais dados serão lidos no Protheus e enviados para o Quírons, conforme a tela de seleção abaixo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19344599883927)  
     

   |  |  |  |  |
   | --- | --- | --- | --- |
   | **Parâmetro** | **Valor de Exemplo** | **Obrigatório** | **Descrição** |
   | Filial De:? | D MG 01 | Não | Inicio da relação de filiais. |
   | Filial Até:? | D MG 01 | Não | Final da relação de filiais. |
   | Cadastro de Funcionários | Selecionado | Não | Informa que será enviado na carga inicial a relação de funcionários. |
   | Cadastro de Dependentes | Selecionado | Não | Informa que será enviado na carga inicial a relação de funcionários. |
   | Matrícula De:? | 000001 | Não | Início da relação de matrículas de funcionários ou dependentes. |
   | Matrícula Até:? | 999999 | Não | Final da relação de matrículas de funcionários ou dependentes. |
   | Cadastro de Pessoas | Selecionado | Não | Informa que será enviado na carga inicial a relação de funcionários. |
   | Participante De:? | 000001 | Não | Início da relação de códigos de participantes. |
   | Participante Até:? | 999999 | Não | Final da relação de códigos de participantes. |
   | Log de Processamento | Selecionado | Não | Informa se deseja gerar um relatório com o LOG da carga de dados. |

**Avaliação de inconsistências**Como mencionado no início deste documento, o processo de integração entre os dois sistemas (Protheus e Quírons) podem ser de dois tipos:

1. **Protheus x Quírons:**Os dados existem inicialmente na Base de Dados Protheus e utilizam as API's do Quírons para incluir/alterar/excluir o referido dado na Base de Dados do Quírons;
2. **Quírons x Protheus:**Os dados existem inicialmente na Base de Dados Quírons e utilizam as API's do Protheus para incluir/alterar/excluir o referido dado na Base de Dados do Protheus.

Deste modo, para uma correta avaliação de qualquer tipo de inconsistência, é primordial compreender qual foi o tipo de integração dos dados.  
Abaixo seguirá alguns passos que podem ser executados para aprofundar a análise de cada um dos tipos de integração.  
  
Para integrações do Tipo 1 (Protheus x Quírons):As integrações oriundas do Protheus seguem o seguinte fluxo de movimentação: os dados são manipulados na base de dados (Protheus), através de inclusões, alterações ou exclusões, como a admissão/inclusão de um novo Funcionário, na tabela SRA. Este dado, por sua vez, cria um registro na tabela de Fila de Processamento (RJP), que possui um "status", para sinalizar se o dado foi transferido à base de dados do Quírons com sucesso ou não. O agendamento/schedule criado no passo 7 desta documentação tem como função, buscar na tabela RJP todos os itens ainda pendentes de envio. Após identificar na tabela RJP que algum item precisa ser enviado ao Quírons, o agendamento segue com sua segunda parte da execução, em que ele utiliza o conteúdo chave gravado na tabela RJP, para buscar efetivamente o registro que precisa ser enviado, diretamente na tabela original, como por exemplo, procurar na tabela SRA, o registro do funcionário recém-admitido. Com o registro devidamente localizado na tabela, o agendamento segue seu processamento, montando um arquivo JSON (formato de arquivo que pode ser anexado durante a integração com API's) com os dados coletados na tabela e utilizando a API do Quírons responsável por aquela informação. Em suma, as API's do Quírons utilizadas, por registro do Protheus são como demonstradas na tabela abaixo:

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Descrição** | **API Quírons** |
| RD0 | Cadastro de Pessoas | person |
| SRA | Funcionários | employee |
| SR7 | Histórico Funcional/Alterações Salariais | functionalHistory |
| SRB | Dependentes | dependant |
| SRE | Histórico Funcional/Transferências | functionalHistory |
| RA4 | Treinamentos | trainingHistory |
| SQB | Departamentos | department |
| SQ3 | Cargos | position |

Dado o fluxo desta integração, para avaliar com maior profundidade casos de inconsistência nesse tipo de integração, é importante notar que eles podem ocorrer em diferentes momentos, como:

* No momento da manipulação do dado, ele não é replicado/gravado na tabela de Fila de Processamento (RJP);
* O agendamento/schedule pode não ter executado no momento agendado ou não foi configurado uma recorrência para o agendamento ou ainda o horário da recorrência ainda não ocorreu;
* A chave gravada na tabela RJP não corresponde à nenhum item da tabela do registro, não encontrando nenhum dado para enviar;
* A montagem do arquivo JSON com os dados do registro podem possuir dados incorretos (tipos de campos, tamanho, campo obrigatório não preenchido);
* A API do Quírons pode retornar com algum código de erro, indicando problemas no arquivo enviado.

Independente de qual ocorrência gerou a inconsistência nesta integração, é possível acessar a rotina "Monitor", criada no item 4, para que sejam listados todos os itens da tabela de Fila de Processamento (RJP), para identificar qual registro não foi devidamente enviado e, em alguns casos, o campo de "Retorno da Integração" apresenta uma mensagem mais detalhada do erro que impediu a integração, como no exemplo demonstrado abaixo: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19344961104151)**  
Lembrando que a mensagem apresentada neste campo "Retorno da Integração" SEMPRE será a mensagem retornada da API do **QUÍRONS**, de acordo com a "mensagem" (dados) enviados pelo Protheus.  
  
Deste modo, caso a integração tenha alguma inconsistência, gerando um retorno não decifrável diretamente da API do Quírons, é necessário, através de *debug* da rotina/função de agendamento (GPEM923) para identificar como a função monta o arquivo JSON que é enviado à API, pois algum dado pode ter sido capturado ou utilizado incorretamente. Nestes casos, a equipe de Suporte Técnico avalia se o problema é causado devido ao registro gravado incorretamente e precisa de correção na base de dados ou à função que captura o dado indevidamente e precisa de correção do fonte.  
  
Para integrações do Tipo 2 (Quírons x Protheus):  
As integrações oriundas do Quírons seguem o seguinte fluxo de movimentação: os dados são manipulados na base de dados (Quírons), através de inclusões, alterações ou exclusões, como a inclusão de um novo Tipo de Abono. Este dado, por sua vez, ao mesmo tempo que é gravado na base de dados do Quírons, é enviado ao Protheus, através do uso das API's do Protheus. Caso haja qualquer inconsistência na API do Protheus, que impeça a gravação corretamente do dado no Protheus, a ação é também cancelada no Quírons.  
Tendo em vista este fluxo e que esta documentação irá se aprofundar na análise por parte Protheus, pode-se levantar algumas causas comuns de inconsistências, como:

* Serviço REST indisponível ou inacessível por questões de infraestrutura (bloqueio de portas, firewall, anti-vírus, ou até mesmo endereço inválido de acesso ou visível somente em rede local);
* Serviço REST compartilhado com outra aplicação ou aplicativo, como o Meu RH;
* Serviço REST com configuração incorreta/diferente do padrão recomendado para o uso dessa integração;
* Problemas com os dados enviados na API do Protheus, que não correspondam corretamente com os dados gerais existentes no Protheus, como código do Grupo de Empresa ou Filial, código do registro, etc.;
* Problemas na execução da API do Protheus, quando um determinado conjunto de informações é enviado.

Neste tipo de integração, a análise por parte do Protheus concentra-se na funcionalidade/acessibilidade do serviço REST e da API que o Quírons tentou utilizar, de acordo com o tipo de registro que foi tentado ser incluído/alterado/excluído, conforme mapeado abaixo:

|  |  |
| --- | --- |
| **Tipo de Registro** | **Nome da API Protheus** |
| Tipos de Abono | allowanceTypes |
| Centro de Custo | payrollCostCenter |
| Cadastro de Turnos de Trabalho | workingShift |
| Cadastro de Funções | positions |
| Cadastro Tipos de Ausência | leaveOfAbsenceType |
| Tipos de Estabilidade | stabilityType |
| Tipos de Treinamentos | classes |
| Insalubridade e Periculosidade | additional |
| Estabilidade Funcional | stabilityControl |
| Marcação de Horas | AllowanceControl |
| Necessidade de Treinamento | trainingNecessity |
| Afastramentos/Ausências | leaveOfAbsenceControl |

Nestes cenários, faz-se necessário a avaliação de acessibilidade do serviço REST do Protheus e validar sua disponibilização, se está correta e acessível normalmente e de acordo com os padrões de implementação apresentados.  
Alguns erros à nível de serviço (REST) podem ser verificados com um maior detalhamento em [https://centraldeatendimento.totvs.com/hc/pt-br/articles/17189279659159](RH%20-%20Linha%20Protheus%20-%20MDT%20-%20Qu%C3%ADrons%20-%20Como%20avaliar%20mensagens%20de%20erro%20durante%20a%20integra%C3%A7%C3%A3o).  
Caso o serviço esteja devidamente acessível e as API's listadas corretamente, é necessário validar se a API aceita os dados de inclusão/alteração/exclusão conforme o padrão estabelecido e documentado em [DI Protheus X NG - Integração de Movimentos - Medicina e Segurança - RH](https://tdn.totvs.com/pages/releaseview.action?pageId=529308420).  
  
Para realização de testes de API's do Protheus, é possível utilizar qualquer ferramenta terceira para desempenhar o papel do Quírons, que utiliza as API's. Comumente utiliza-se a ferramenta ***Postman*** para estes testes internos, onde é possível seguir conforme a documentação acima, na construção do Arquivo JSON, Tipo de Comunicação, para cada uma das API's, para testar sua funcionalidade.  
  
Nestes casos, caberá a equipe de Suporte Técnico, avaliar se a inconsistência mapeada pode ser causada por algum ponto de desatualização, dado incorreto ou serviço REST errado que deverá ser corrigido ou se originada de erro não previsto durante a execução da API, dependente de algum cenário não mapeado e deverá ter correção no fonte.  
  
**Atualizações**  
[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282-RH-Linha-Protheus-MEU-RH-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente?source=search)  
[MP- BD - Procedimento para atualizar Lib no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007717731-MP-BD-Procedimento-para-atualizar-Lib-no-Protheus)  
[Cross Segmentos - Backoffice Linha Protheus - Framework - Atualização de arquivos do Protheus 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024983272-Cross-Segmentos-Backoffice-Linha-Protheus-Framework-Atualiza%C3%A7%C3%A3o-de-arquivos-do-Protheus-12) **Saiba Mais**[Integração | Protheus SIGAGPE x Quírons](https://tdn.totvs.com/pages/releaseview.action?pageId=793200883)[Documentações sobre Quírons](https://tdn.totvs.com/pages/releaseview.action?pageId=529308420)  
[Artigos sobre Quírons](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9033517492119-Qu%C3%ADrons)
