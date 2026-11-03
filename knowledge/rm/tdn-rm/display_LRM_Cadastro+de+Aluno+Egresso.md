---
content_hash: cab874c12d2f171123c4dd5a7c071fcf5ab446ab376551c507199d78dc1a3e4a
fetched_at: '2026-06-29T00:09:34.072177+00:00'
page_id: '425459133'
product: rm
source: tdn-rm
title: Cadastro de Aluno Egresso
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Aluno+Egresso
version: 2
---

---

Esta funcionalidade tem como objetivo permitir que alunos egressos que não estão na base RM possam solicitar seu cadastro através de uma página pública e que esse cadastro seja aprovado/reprovado através do fluxo: Cadastro de Aluno (fluig).

**Procedimento para utilização:**

Ter o FLUIG devidamente instalado e configurado conforme documentação:

* Instalação:[{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=144409653)<http://tdn.totvs.com/pages/viewpage.action?pageId=144409653+>
* Configuração:[{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=144409655)<http://tdn.totvs.com/pages/viewpage.action?pageId=144409655+>

Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.

* Instalação: [{+}](http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7c+Developer+Studio)<http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio+>
* Configuração: [{+}](http://tdn.totvs.com/pages/viewpage.action?pageId=73078179)<http://tdn.totvs.com/pages/viewpage.action?pageId=73078179+>

Criar no FLUIG o papel necessário para a execução do fluxo de cadastro de aluno. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar o papel).

* Código = aprovador\_egresso | Descrição = Aprovador de egresso

Em seguida, associar os usuários ao respectivo papel cadastrado.

Importar o fluxo "Cadastro de aluno" para a ferramenta TOTVS Developer Studio (TDS).  
Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig

* Configuração:[{+}](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf)<http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf+>

**Parametrização necessária:**  
  
Cadastro: TotvsEducacional | Educacional | Configurações | Parâmetros | Matrícula | Geral 2/2  
Nessa opção será permitido parametrizar o sistema para que seja indicado qual status de matrícula deve ser inserido no status de resultado final na matricula do curso do aluno, após a aprovação da solicitação.

**Descrição do Processo:**  
Através da página pública, o Aluno fará seu cadastro, disponibilizando informações necessárias tais como Nome, Sobrenome, Apelido, Nome Social, Data Nascimento, Sexo, Estado Civil, Estado Natal, Naturalidade, E-mail, Cpf, Cep, Tipo de rua, Rua, Numero, Complemento, Tipo de bairro, Bairro, País, Estado, Cidade, Telefone Residencial, Telefone Celular, Telefone 3, Fax, Curso/Habilitação. Após o preenchimento a solicitação será encaminhada para o usuário associado ao papel "Aprovador Egresso" no fluig, onde irá realizar a confirmação que o Aluno estudou ou não na Instituição. Caso o aluno não tenha estudado na instituição a solicitação será reprovada e arquivada. Caso contrário o usuário informará o turno que o aluno estudou e realizará a aprovação da solicitação. Ao aprovar os dados este Aluno é cadastrado automaticamente na base oficial RM.
