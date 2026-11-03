---
content_hash: 5b0e4d1379ae559901047e4709fc796925301c77147550f58efb3eac87ffa48f
fetched_at: '2026-06-29T00:09:36.798030+00:00'
page_id: '425459522'
product: rm
source: tdn-rm
title: Solicitação de Cadastro Empresa Parceira e Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459522
version: 3
---

---

Esta funcionalidade tem como objetivo permitir que empresas interessadas em ser parceiras da IE, possam solicitar se cadastro através de uma página pública disponibilizada no Portal RM e que esse cadastro seja aprovado/reprovado através dos fluxos: Cadastro de Empresa Parceira e cadastro de Funcionário da Empresa Parceira do FLUIG.

**Procedimento para utilização:**

Ter o FLUIG devidamente instalado e configurado conforme documentação:

* Instalação: [{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=144409653)<http://tdn.totvs.com/pages/viewpage.action?pageId=144409653+>
* Configuração: [{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=144409655)<http://tdn.totvs.com/pages/viewpage.action?pageId=144409655+>

Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.

* Instalação: [{+}](http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7c+Developer+Studio)<http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio+>
* Configuração: [{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=73078179)<http://tdn.totvs.com/pages/viewpage.action?pageId=73078179+>

Criar no FLUIG os papéis necessários para a execução dos fluxos de cadastro de empresa parceira e cadastro de funcionário da empresa parceira. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).

* Código = aprovador\_parcerias | Descrição = Aprovador de parcerias
* Código = responsável\_empresa\_parceira | Descrição = Responsável pela empresa parceira

Em seguida, associar os usuários aos respectivos papéis cadastrados.

É importante ter o usuário **mestre** criado em todas as empresas para que, ao executar a página pública, o sistema consiga validar o usuário que iniciará a solicitação.

Importar os fluxos "Cadastro de Empresa Parceira" e "Cadastro de Funcionário da Empresa Parceira" para a ferramenta TOTVS Developer Studio (TDS).  
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig

* Configuração:[{+}](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf)<http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf+>

Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos dos fluxos "Cadastro de Empresa Parceira" e "Cadastro de Funcionário da Empresa Parceira".

* Configuração:[{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=189313846)<http://tdn.totvs.com/pages/viewpage.action?pageId=189313846+>

**Parametrização necessária:**

Geração de Usuários da Empresa Parceira

A funcionalidade permitirá a geração de usuários no RM e para isso novos parâmetros foram criados para permitir a criação automática desses usuários.  
Cadastro: TotvsEducacional | Educacional | Configurações | Parâmetros | Geração de usuários | Funcionários da Empresa Parceira

Nessa opção será permitido parametrizar se a geração será automática, e quando parametrização será seguida.  
Caso a geração esteja configurada como automática, após a aprovação do Fluxo do FLUIG: "Aprovar o Cadastro da Empresa Parceira", o funcionário vinculado ao cadastro da Empresa Parceira, seguirá a regra definida pelo usuário.

**Arquivo "web.config":**  
Caso o usuário deseje, poderá fazer uso do reCAPTCHA do Google, para impedir a entrada de dados automatizada na página pública. Para configurar o uso do reCAPTCHA é preciso seguir os seguintes passos:

* Acessar o arquivo web.config da pasta "Source/Edu-Educacional/Public/EmpresaParceira/" da instalação do portal para configurar a tag EXIBIR\_RECAPTCHA para "true".
* Será necessário preencher também as tags SITE\_KEY e SECRET\_KEY, desse mesmo arquivo web.config, seguindo as orientações fornecidas pelo Google em <https://www.google.com/recaptcha/> para o correto funcionamento.

Para o correto funcionamento da solução as tags PROCESSID e USERID, desse mesmo arquivo web.config, devem estar configuradas com "rm\_edu\_dgr\_empresa\_parceira" e "mestre" respectivamente. Essas informações definem qual fluxo (PROCESSID) deverá ser executado pelo webservice do FLUIG e qual usuário será responsável por iniciar a solicitação (USERID).

**Descrição do Processo:**  
Através da página pública, a empresa fará seu cadastro, disponibilizando informações necessárias tais como CNPJ, nome fantasia, e-mail, etc., e dados de uma pessoa responsável na empresa. Esse responsável será o contato entre empresa e a IE, e o primeiro usuário dessa empresa a ser cadastrado no Portal RM, onde posteriormente terá o papel para cadastrar os demais funcionários da empresa.  
Por padrão esta página pública estará com acesso restrito impossibilitando a utilização do cadastro, sendo necessário para os clientes que queiram utilizá-la, a parametrização do arquivo web.config (<allow users="\*"/>) e a disponibilização do link [http://PORTAL/Source/Edu-Educacional/Public/EmpresaParceira/EduEmpresaParceira.html](http://PORTAL/Source/Edu-Educacional/Public/EmpresaParceira/EduEmpresaParceira), onde PORTAL é o endereço do Portal RM instalado e configurado no cliente.  
Após realizar o cadastro na página pública, essas informações serão encaminhadas para a IE e através de um fluxo do FLUIG (Cadastro de Empresas Parceiras). O sistema criará automaticamente a solicitação no FLUIG, permitindo que algum usuário, vinculado ao papel de "aprovador\_parcerias", assuma essa solicitação e possa realizar a aprovação desse cadastro.  
Após aprovação ou rejeição do cadastro, o sistema deverá enviar e-mail à empresa indicando o status de sua solicitação. Esse status será enviado ao e-mail cadastrado para a pessoa responsável, definido na página pública e será feito através do FLUIG.  
O FLUIG utiliza templates para realizar o envio de e-mails personalizados, para mais detalhes acessar o link Envio de e-mail personalizado. Os nomes dos templates de e-mail utilizados pelos fluxos são:

* solicitacao\_empresa\_parceira - enviado ao solicitar o cadastro da empresa
* solicitacao\_empresa\_parceira\_aprovada - enviado ao aprovar o cadastro da empresa
* solicitacao\_empresa\_parceira\_reprovada - enviado ao reprovar o cadastro da empresa
* solicitacao\_funcionario\_empresa\_parceira - enviado ao solicitar o cadastro do funcionário
* solicitacao\_funcionario\_empresa\_parceira\_aprovada - enviado ao aprovar o cadastro do funcionário
* solicitacao\_funcionario\_empresa\_parceira\_reprovada - enviado ao reprovar o cadastro do funcionário

Caso o cadastro da Empresa Parceira seja aprovado e o parâmetro para geração automática de usuário esteja marcado (conforme parametrização descrita acima) o sistema fará a geração desse usuário para ser utilizado no Portal RM.  
  
**\* Informação Importante \***  
Se a instituição quiser permitir o acesso desse usuário ao FLUIG, deverá posteriormente realizar o sincronismo RM x FLUIG através da visão de usuários no RM e vincular esse usuário ao papel "responsavel\_empresa\_parceira" através do módulo de administração do FLUIG.

Para realizar o sincronismo RM x Fluig:

* Cadastro: TotvsEducacional | Educacional | Atividades Acadêmicas | Acadêmico | Empresas | Anexo |Funcionários da Empresa | 'Editar' o registro do usuário | Processos | Sincroniza Usuários do Corpore com o GED

O registro da Empresa Parceira e do funcionário, poderá ser visualizada através do menu:

* Cadastro: TotvsEducacional | Educacional | Atividades Acadêmicas | Acadêmico | Empresas

O usuário criado, passa a ter acesso ao Portal RM para usufruir dos recursos relacionados ao Portal de Estágio e a visualização do Curso da Instituição. Além disso este funcionário poderá também cadastrar novos funcionários para a empresa utilizando a funcionalidade disponibilizada no FLUIG, caso tenha acesso.

Antes de cadastrar o funcionário responsável o usuário poderá

Para cadastrar novo funcionário da empresa, o usuário responsável deverá:

* Acessar o fluxo "Cadastro de Funcionários de Empresa Parceira" no FLUIG e gerar uma nova solicitação.
* Após solicitar o cadastro do novo funcionário no FLUIG, essa solicitação deverá ser aprovada por um usuário vinculado ao papel "aprovador\_parcerias".  O mesmo procedimento descrito acima, para geração de usuário RM, também acontecerá após aprovação dessa solicitação no FLUIG.

Com o objetivo de diferenciar se o cadastro foi realizado através das páginas públicas, nas visões de "Empresas" e "Funcionários da empresa" será possível verificar se os registros foram gerados a partir do FLUIG, foi criado o "Nº processo FLUIG" na lista de colunas.  
  
Para visualizar o fluxo completo, segue abaixo o diagrama de atividades com o objetivo de ter uma visão mais clara do processo descrito.  
  
Fluxo: Aprovar/Reprovar o Cadastro da Empresa Parceira  
  
  
  
  
ð Fluxo: Aprovar/Reprovar o Cadastro de Novos Funcionários da Empresa  
  
  
  
  
  
 Informações Complementares

---

[Documento Técnico - Solicitação de cadastro de empresa parceira e seus funcionários](http://tdn.totvs.com/pages/viewpage.action?pageId=235595235)

  Veja Também

---

[Solicitação de cadastro de empresa parceira e seus funcionários](http://tdn.totvs.com/pages/viewpage.action?pageId=235595235)

[Personalização de e-mail Fluig](http://tdn.totvs.com/pages/releaseview.action?pageId=183730587#Personaliza%c3%a7%c3%a3odee-mail-EnviodeE-mailPersonalizado)
