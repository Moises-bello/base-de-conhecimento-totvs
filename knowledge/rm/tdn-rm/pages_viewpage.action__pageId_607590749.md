---
content_hash: 086a2d49d198ae86f13a7548fef27e69cdaef0481ecd73f025813abe5d49a8f3
fetched_at: '2026-06-29T00:10:58.910315+00:00'
page_id: '607590749'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Definições e Parametrizações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607590749
version: 27
---

Definições

A integração entre o sistema TOTVS Folha de Pagamento com o TOTVS Assinatura Eletrônica permite o gerenciamento de assinatura de documentos que necessitam serem assinados eletronicamente por um ou mais destinatários. A integração permite que relatórios RptReports do sistema TOTVS Folha de Pagamento possam ser enviados automaticamente para assinatura, com base em critérios previamente definidos.

Atualmente é possível integrar relatórios que utilizem a tabela de funcionários (PFUNC) como base do relatório ou utilizem os parâmetros de coligada e chapa. Estão disponibilizados então 3 opções de geração de relatórios

* **Aviso de Férias**

O sistema enviará para assinatura os avisos de férias de funcionários que possuírem férias marcadas não iniciadas.

**Atenção:** Legalmente o aviso de férias tem que ser enviado com 30 dias de antecedência do início das férias. Não será permitido enviar um aviso de férias pagas ou finalizadas.

* **Recibo de férias**

O sistema enviará para assinatura os recibos de férias de funcionários que possuírem férias calculadas.

* **Outros**

O sistema enviará para assinatura o relatório gerado com base nas regras do relatório.

Para definir a utilização dos tipos acima descritos o usuário terá acesso a uma tela para configurar as regras de geração, integração e assinatura dos relatórios, possibilitando assim maior flexibilidade na configuração da integração.

Além do envio dos documentos para assinatura no portal TOTVS Assinatura Eletrônica o sistema permite o acompanhamento do status das assinaturas através de uma tela que permite filtrar registros segundo as necessidades do usuário. Através dessa tela o usuário poderá consultas os status, aprovar documentos que necessitem de aprovação e excluir documentos não finalizados.

Requisitos para integração

Para funcionamento da integração o usuário necessitará realizar algumas configurações iniciais para que a integração possa ser realizada, sendo elas:

1 – Contratação de um plano de assinaturas através da TOTVS Store, que pode ser acessada através do endereço abaixo:

**[TOTVS Assinatura Eletrônica - Trial](https://partner.totvs.store/br/produto/catalog/product/view/id/911/s/totvs-assinatura-eletronica-trial/)**

2 – Criação dos usuários que realizarão as integrações através do TOTVS Folha de Pagamento.

Importante

A criação desses usuários é necessária pois eles possuirão permissões especiais para envio de documentos, consulta de status, exclusão de documentos e destinatários e também a criação de usuários. Esses usuários serão utilizados no sistema durante a execução do processo, sendo eles identificados no portal TOTVS Assinatura Eletrônica como autores dos documentos enviados para assinatura.

3 – Parametrização do sistema para realização da comunicação com TOTVS Assinatura Eletrônica.

Parametrização inicial

Após a contratação do plano o usuário deverá acessar o sistema RM, e abrir a tela de Parâmetros Globais, disponível através do menu “Ambiente | Parâmetros | Parâmetros Globais” na aba “TOTVS Assinatura Eletrônica” preencher os campos:

URL de autenticação:

Informe o endereço <https://totvssign.totvs.app/identityintegration>

URL da API de integração:

Informe o endereço <https://totvssign.totvs.app>

URL de login via formulário web:

Informe o endereço <https://totvssign.totvs.app/webapptotvssign/#/auth/login?external=true>

Campo **Atualizar situação das assinaturas dos documentos ao carregar visão**

Este campo define o comportamento da atualização do status dos documentos enviados para assinatura ao abrir a tela de monitoramento dos dados. Caso este campo esteja marcado, ao abrir a tela de visão de monitoramento de documentos enviados para integração o sistema consultará os documentos que estão pendentes de assinatura e verificará se os mesmos sofreram alteração no seus status. Caso tenham sofrido alteração o sistema atualizará o status no RM. Caso o campo não seja marcado a atualização de status deverá ser feita através de um processo disponibilizado na tela de monitoramento.

Configuração de acesso

Os usuários que poderão realizar a integração de documentos com o TOTVS Assinatura Eletrônica deverão ter seus perfis de acesso ajustados para permitir o acesso às telas responsáveis pela integração. Para isso acesse o cadastro de perfil e conceda acesso às opções de Assinatura Eletrônica, do sistema TOTVS Folha de Pagamento.

Recursos disponíveis

Os recursos para realização da integração com o sistema TOTVS Assinatura Eletrônica estão disponíveis no sistema TOTVS Folha de Pagamento através do menu “Assinatura Eletrônica”.

**Tipos de relatórios**

Configuração dos relatórios a serem integrados.

**Processo de integração de relatórios**

Processo responsável por gerar o relatório e realizar o envio do mesmo para o portal TOTVS Assinatura Eletrônica.

**Monitor de relatórios**

Tela para acompanhar o status dos relatórios integrados.

Ao ser realizada a integração de um relatório o sistema TOTVS Folha de Pagamento verificará as regras definidas para cada tipo de relatório para realizar a integração, como:

* Quem assinará o documento?
* Se o usuário destinatário não possuir cadastro no sistema TOTVS Assinatura Eletrônica será possível cadastrar o mesmo automaticamente no portal?
* Posso validar o relatório gerado antes de realizar a sua integração?
* Posso definir prazos para assinatura?

Essas e outras particularidades poderão ser tratadas através da configuração do tipo de relatório.

Tipos de relatórios

Através dessa tela o usuário deverá realizar o cadastro dos tipos de relatórios que serão integrados. O preenchimento das informações dessa tela possibilitará a geração do relatório, a identificação dos destinatários e o envio do documento para assinatura.

**Grupo**

Informe um código para identificar grupo de relatórios.

**Descrição**

Informe uma descrição para o grupo de relatórios.

**Tipo de relatório**

Selecione o tipo de relatório. Os tipos disponíveis são:

* Aviso de Férias
* Recibo de Férias
* Outros

**Criação do Documento para assinatura**

**Remetente assina**

Marque essa opção caso deseje que o usuário responsável pela execução do processo (usuário do sistema) seja um dos assinantes do documento. Com isso ele passará a figurar na lista de destinatários do documento para assinatura. Será considerado para isso o e-mail do usuário do cadastro de Usuários (GUSUARIO).

Atenção

Caso o remetente seja um dos assinadores, será possível realizar a assinatura pelo portal TOTVS Assinatura Eletrônica ou através do processo "Assinar documento" da tela de monitoramento, após validação do documento.

**Criar usuário no TOTVS Assinatura eletrônica caso não exista (usuário do destinatário)**

Ao marcar essa opção, durante o processo de integração do documento será verificado se o destinatário existe no sistema TOTVS Assinatura Eletrônica. Caso ele não exista será então realizado um cadastro inicial para o usuário, considerando seu nome, CPF e e-mail do cadastro de pessoa. O usuário então receberá um e-mail informando da criação do usuário, ativação da conta e criação da sua senha.

**Requer aprovação (integra somente após validação do relatório)**

Essa opção permite a geração do relatório para posterior conferência e envio para integração. Assim o relatório será gerado e um registro será gravado na tela de monitoramento, com o status “Pendente de aprovação”. O usuário deverá acessar a tela de monitoramento para visualizar o relatório e realizar sua aprovação, momento em que ocorrera o seu envio para o portal TOTVS Assinatura Eletrônica.

Observação

Ao utilizar essa opção não será possível usar a opção de criação de usuário, visto que o processo de monitoramento não está preparado para tratar essa regra.

**Utilizar e-mail pessoal caso o e-mail principal não esteja preenchido**  
Essa opção permite que o usuário utilize o e-mail pessoal cadastrado em "Endereço Principal" , no cadastro de funcionário.

**Configuração de prazos**

**Utiliza prazo para validação/assinatura do documento e cancela se não assinado no prazo.**

Ao marcar essa opção o usuário poderá definir o prazo (dias) em que o documento ficará disponível para aprovação/assinatura.   
Caso o documento não esteja assinado até a data limite informada, o usuário poderá excluir este através do processo "Exclusão de Documentos Integrados" existente no módulo "Monitor de Documentos Enviados para Assinatura".

**Observação:**  
Este processo somente permite a exclusão do documento que não teve a assinatura realizada.  
O documento que teve a assinatura realizada após o prazo, terá seu status alterado para "Fora do prazo de assinatura".

**Opções de envio do aviso/recibo de férias**

Essas opções estão disponíveis apenas para os relatórios dos tipos Aviso de Férias e Recibo de Férias.

**Enviar no dia do aviso/pagamento de férias (se dia não útil antecipar para o dia útil)**

Ao marcar essa opção o sistema somente integrará os avisos de férias com data de aviso na data da execução do processo ou a data de pagamento no dia da execução do processo.

Exemplo

Data atual da execução: 01/04/2021

**Aviso de férias**

Funcionário 001: data do Aviso de férias: 01/04/2021 (quinta-feira)

Funcionário 002: data do Aviso de férias: 02/04/2021 (sexta-feira feriado)

Funcionário 003: data do Aviso de férias: 05/04/2021 (segunda-feira)

Ao executar o processo enviará o aviso do funcionário 001 pois o dia do aviso é igual a data de execução. Será enviado também o aviso do funcionário 002, pois o dia 02 é um feriado, então essa comunicação será antecipada para o dia útil.

A mesma regra será usada para o recibo de férias, porém considerando a data de pagamento das férias.

**Enviar com X dias de antecedência**

Essa opção permite o envio do documento a X dias do seu início (data do aviso ou data de pagamento).

Exemplo

**Recibo de férias:**

Data atual da execução: 31/03/2021

Dias de antecedência: 02

Funcionário 001: data de pagamento das férias: 02/04/2021 (sexta-feira)

Funcionário 002: data de pagamento das férias: 09/04/2021 (sexta-feira)

Será considerado o funcionário 001, pois a data atual com acréscimo de 2 dias é igual a data do pagamento.

**Não validar essa regra**

Não serão validadas as datas de aviso e pagamento de férias, sendo considerado os funcionários retornados pela seleção durante a execução do processo.

**Utilizar tabela de chefes/supervisores**

Ao marcar essa opção os chefes/supervisores poderão fazer parte dos destinatários do documento como um assinante, um validador ou testemunha.

Utilizar hierarquia de posição

É possível ativar essa funcionalidade, acessando o  **Gestão de Pessoas | Parametrizador | Gerenciamento de Hierarquia | Hierarquia**e Habilitar funcionalidades da Hierarquia.  
  
Através dessa funcionalidade será possivel que seja enviado o email de assinatura para o superior imediato na hierarquia de posição  
  

**Configuração hierárquica**

**Tipo de participação da chefia**

Indica se a participação no documento será como um assinador, um validador ou uma testemunha.

**Configuração de assinatura para chefes/supervisores**

Poderá ser utilizada uma das configurações: inclui apenas o chefe como destinatário, inclui apenas o supervisor como destinatário ou inclui ambos como destinatários.

**Utilizar equipe**

Caso seja incluído o superviso como um dos destinatários poderá ser definido que será considerar apenas o supervisor com a mesma equipe do funcionário.

**Regras para geração do nome do arquivo**

Regras para geração do nome do arquivo PDF, que poderá conter dentre as opções disponíveis a inclusão do nome ou chapa do funcionário.

**Ativo**

Essa campo indica se o tipo de relatório está ativo para integração. Caso ele esteja desmarcado não será possível realizar a integração desse grupo.

**Aba Relatórios**

Através dessa aba deverão ser informados os relatórios a serem utilizados na integração. Caso seja informado mais de um relatório será gerado um documento para assinatura para cada um dos relatórios. Esses relatórios deverão possuir a tabela de funcionários (PFUNC) como uma das fontes de dados ou receber parâmetros como: CHAPA, CODCOLIGADA, CODSECAO, DTPAGTOFERIAS, DTFENCFERIAS, DTAVISOFERIAS.

**Atenção:**  Ao realizar uma modificação no relatório que altere os parâmetros do relatório, como por exemplo 'Visível em todas as coligadas', será necessário informá-lo novamente na Aba de Relatórios do Tipo de relatório, antes de realizar o Processo de Integração de relatórios.

Será permitido também a inclusão de relatórios do SmartView, para isso incluímos a função de "Usa Recurso SmartView", **Sim** são para relatórios utilizados no SmartView e **Não** para relatórios do RM Reports.  
A coluna relatório será alimentada com valores negativos para recursos SmartView e positivos para recursos do RM Reports, como no exemplo da imagem abaixo:

* Para o relatório de aviso de férias serão tomados como base os relatórios:

FOPREL00180 - Aviso de Férias - ORACLE

FOPREL00030 - Aviso de Férias (esse relatório considera apenas os campos da PFUNC)

FOPREL00030 - Aviso de Férias-MSSQL (neste relatório é considerado o período aquisitivo associado na PFUNC.FIMPERAQUIS)  
  
FOPTRP0001 - Aviso de Férias (esse relatório é um recurso SmartView) - ORACLE e SQL

No monitoramento os campos chave serão gravados como: “CODCOLIGADA| CHAPA|FIMPERAQUIS|DATAPAGTO” e os valores chave serão os valores dos referidos campos.

* Para o relatório de recibo de férias serão tomados como base os relatórios:

FOPREL00112 - Recibo de Férias (considera dados da tabela PFUFERIASRECIBO filtrados pelos campos da PFUNC e filtro)

FOPREL00190 - Recibo de Férias RM Portal (considera dados da tabela PFUFERIASRECIBO filtrados pelos campos da PFUNC e filtro)  
FOPTRP0007- Recibo de Férias RM Portal (esse relatório é um recurso SmartView) - ORACLE e SQL

No monitoramento os campos chave serão gravados como: “CODCOLIGADA| CHAPA|FIMPERAQUIS|DATAPAGTO” e os valores chave serão os valores dos referidos campos.

* Para o relatório do tipo “Outros”, no monitoramento os campos chave serão gravados como: “CODCOLIGADA| CHAPA” e os valores chave serão os valores dos referidos campos.

Atenção

Caso a base de dados não possua relatório para o tipo definido (Aviso de férias ou Recibo de férias), pode-se realizar a importação do relatório do book de relatórios.

**Aba destinatários fixos**

Através dessa aba podem ser definidos destinatários fixos para o relatório, como por exemplo uma pessoa que seja o responsável pelo Departamento Pessoal que deva assinar o relatório, mesmo não pertencendo a estrutura de chefia ou não seja o remetente do relatório.

Vídeo

### **Parametrização**

80%80%

### **Tipos de relatórios**

80%80%
