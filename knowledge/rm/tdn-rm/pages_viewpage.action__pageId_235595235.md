---
content_hash: f2dfaab269b38b7c181c49b1d83743292b075331f1e706c955cf0450be31fc87
fetched_at: '2026-06-29T00:08:05.437078+00:00'
page_id: '235595235'
product: rm
source: tdn-rm
title: DT_Solicitação_cadastro_empresa_parceira_e_funcionarios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235595235
version: 126
---

# Solicitação de cadastro de empresa parceira e seus funcionários

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Página pública para cadastro da empresa parceira e responsável | Página pública para cadastro da empresa parceira e responsável | | Fluxo para aprovação do cadastro da empresa parceira e responsável | Fluxo para aprovação do cadastro da empresa parceira e responsável | | Fluxo para cadastro de funcionários da empresa parceira já cadastrada | Fluxo para cadastro de funcionários da empresa parceira já cadastrada | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | Parâmetros Educacional | 15.09 - Geração de Usuários | 15.09.03 - Funcionário de Empresa Parceira |
| **Requisito (ISSUE):** | PCREQ-10620 |
| **País(es):** | *Todos* |
| **Tabelas Utilizadas:** | *SEMPRESA, SEMPRESAFUNCIONARIO* |

## Descrição

Permitir que empresas possam se cadastrar como parceiras através de uma página pública disponibilizada no Portal RM e que esse cadastro seja aprovado/reprovado através de fluxos do FLUIG.

## Procedimento para Utilização

Pré-requisitos para utilizar a funcionalidade de cadastro de empresa parceira

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução dos fluxos de cadastro de empresa parceira e cadastro de funcionário da empresa parceira. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **aprovador\_parcerias**| Descrição = **Aprovador de parcerias**
  + Código = **responsavel\_empresa\_parceira**| Descrição = **Responsável pela empresa parceira**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
  + É importante ter o usuário **mestre** criado em todas as empresas para que, ao executar a página pública, o sistema consiga validar o usuário que iniciará a solicitação.
* Importar os fluxos "Cadastro de Empresa Parceira" e "Cadastro de Funcionário da Empresa Parceira" para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos dos fluxos "Cadastro de Empresa Parceira" e "Cadastro de Funcionário da Empresa Parceira".  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

A nova solução permite que empresas interessadas em ser parceiras da instituição possam solicitar seu cadastro através de uma página pública da instituição, disponibilizada no Portal RM.

Parâmetros necessários:

* A funcionalidade permitirá a geração de usuários no RM e para isso novos parâmetros serão criados para permitir a criação automática desses usuários.
* Na etapa **15.09 - Geração de Usuários** será criada sub-etapa **15.09.03 - Funcionário de Empresa Parceira**.
* Nessa opção será permitido parametrizar se a geração será automática ao salvar um funcionário da empresa parceira e quais as regras deverão ser seguidas.

Arquivo "web.config": 

* Caso o usuário deseje, poderá fazer uso do reCAPTCHA do Google, para impedir a entrada de dados automatizada na página pública. Para configurar o uso do reCAPTCHA é preciso seguir os seguintes passos:
  + Acessar o arquivo web.config da pasta "Source/Edu-Educacional/Public/EmpresaParceira/" da instalação do portal para configurar a tag EXIBIR\_RECAPTCHA para "true".
  + Será necessário preencher também as tags SITE\_KEY e SECRET\_KEY, desse mesmo arquivo web.config, seguindo as orientações fornecidas pelo Google em <https://www.google.com/recaptcha/> para o correto funcionamento.
* Para o correto funcionamento da solução as tags PROCESSID e USERID, desse mesmo arquivo web.config, devem estar configuradas com "rm\_edu\_dgr\_empresa\_parceira" e "mestre" respectivamente. Essas informações definem qual fluxo (PROCESSID) deverá ser executado pelo webservice do FLUIG e qual usuário será responsável por iniciar a solicitação (USERID).

Funcionamento da solução: 

* Através da página pública, a empresa fará seu cadastro, disponibilizando informações necessárias tais como CNPJ, nome fantasia, e-mail, etc., e dados de uma pessoa responsável. Esse responsável será o contato entre empresa e instituição, e o primeiro usuário dessa empresa a ser cadastrado no Portal RM.
* Por padrão esta página pública estará com acesso restrito impossibilitando a utilização do cadastro, sendo necessário para os clientes que queiram utilizá-la, a parametrização do arquivo web.config (<allow users="\*"/>) e a disponibilização do link [http://PORTAL/Source/Edu-Educacional/Public/EmpresaParceira/EduEmpresaParceira.aspx,](http://portal_rm/Source/Edu-Educacional/Public/EduCadastroEmpresaParceira.aspx,) onde PORTAL é o endereço do Portal RM instalado e configurado no cliente.
* Após realizar o cadastro na página pública, essas informações serão encaminhadas para a instituição através de um fluxo do FLUIG (Cadastro de Empresas Parceiras). O sistema criará automaticamente a solicitação no FLUIG, permitindo que algum usuário, vinculado ao papel de **“aprovador\_parcerias”**, assuma essa solicitação e possa realizar a aprovação desse cadastro.
* Após aprovação ou rejeição do cadastro, o sistema deverá enviar e-mail à empresa indicando o status de sua solicitação. Esse status será enviado ao e-mail cadastrado para a pessoa responsável, definido na página pública e será feito através do FLUIG.

  O FLUIG utiliza templates para realizar o envio de e-mails personalizados, para mais detalhes acessar o link [Envio de e-mail personalizado](http://tdn.totvs.com/pages/viewpage.action?pageId=183730587#Personalizaçãodee-mail-EnviodeE-mailPersonalizado). Os nomes dos templates de e-mail utilizados pelos fluxos são:

  + solicitacao\_empresa\_parceira - enviado ao solicitar o cadastro da empresa
  + solicitacao\_empresa\_parceira\_aprovada - enviado ao aprovar o cadastro da empresa
  + solicitacao\_empresa\_parceira\_reprovada - enviado ao reprovar o cadastro da empresa
  + solicitacao\_funcionario\_empresa\_parceira - enviado ao solicitar o cadastro do funcionário
  + solicitacao\_funcionario\_empresa\_parceira\_aprovada - enviado ao aprovar o cadastro do funcionário
  + solicitacao\_funcionario\_empresa\_parceira\_reprovada - enviado ao reprovar o cadastro do funcionário
* Caso o cadastro seja aprovado e o parâmetro para geração automática de usuário esteja marcado (conforme parametrização descrita acima) o sistema fará a geração desse usuário para ser utilizado no Portal RM.  
    
  \*\*\*IMPORTANTE\*\*\*
* Se a instituição quiser permitir o acesso desse usuário ao FLUIG, deverá posteriormente realizar o sincronismo RM x FLUIG através da visão de usuários no RM e vincular esse usuário ao papel **“responsavel\_empresa\_parceira”**através do módulo de administração do FLUIG.
* O usuário criado, passa a ter acesso ao Portal RM para usufruir dos recursos relacionados ao portal de estágio e poderá também cadastrar novos funcionários para a empresa utilizando a funcionalidade disponibilizada no FLUIG, caso tenha acesso.
* Para cadastrar novo funcionário da empresa, o usuário responsável deverá:
  + Acessar o fluxo “Cadastro de Funcionários de Empresa Parceira” no FLUIG e gerar uma nova solicitação.
  + Após solicitar o cadastro do novo funcionário no FLUIG, essa solicitação deverá ser aprovada por um usuário vinculado ao papel **“aprovador\_parcerias”**.  O mesmo procedimento descrito acima, para geração de usuário RM, também acontecerá após aprovação dessa solicitação no FLUIG.

Campo "Nº processo FLUIG":

* Nas visões de "Empresas" e "Funcionários da empresa" será possível verificar se os registros foram gerados a partir do FLUIG, basta incluir o campo "Nº processo FLUIG" na lista de colunas.

divs
