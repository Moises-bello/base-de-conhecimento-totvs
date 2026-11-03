---
content_hash: d22899aff9dc9558ef56da6f22b819df43a33373e03f00b6ca21517c89e8547d
fetched_at: '2026-06-29T00:09:35.504601+00:00'
page_id: '425459372'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x TOTVS e-Learning Management SUITE (LMS) - Cadastro
  de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459372
version: 2
---

**Cadastro de Usuários**

---

**Mensagem**  
    
 A mensagem "user" é gerada na integração de Alunos entre o TOTVS Gestão de Pessoas e o TOTVS LMS nos processos de matricula no TOTVS Gestão de pessoas, sendo uma mensagem síncrona. Esta mensagem é enviada apenas quando é realizado uma matricula ou então através de uma formula visual. Ela pode mandar um novo usuário, e pode também alterar um usuário já existente no TOTVS LMS  
    
 O TOTVS LMS recebe as mensagens "user" via EAI, processando-as e realizando as ações necessárias na sua base de dados. Para saber mais sobre EAI clique aqui.  
    
 Dados que devem ser enviados pelo TOTVS Gestão de Pessoas na mensagem "user":

* InternalID: será armazenado como ExternalID no LMS e usado para identificar o usuário integrado
* Nome completo
* Usuário
* E-mail
* Código do Perfil

**Cadastro**  
 O aluno é cadastrado como Usuário com perfil Passado pelo RM no TOTVS LMS. Os usuários cadastrados via integração somente podem ser alterados pelo TOTVS Gestão de Pessoas. No TOTVS LMS é permitido alterar os campos não enviados pelo TOTVS Educacional.  
 Ao cadastrar o Usuário, o TOTVS LMS gera uma senha automática para esse. O usuário e senhas de acesso são enviados por e-mail, conforme cadastrado.  
 Campos obrigatórios para que o cadastro seja efetuado com sucesso no TOTVS LMS:

* Nome
* Sobrenome
* Usuário
* E-mail do aluno
* Perfil

**Observações:**

1.     Os campos Idioma e Fuso horário são obrigatórios no cadastro de Usuário, porém, não são enviados na mensagem de "user". Esses campos são preenchidos conforme definido no cadastro da Instância Virtual à qual o Usuário está sendo vinculado.  
 2.     Usuários cadastrados diretamente no TOTVS LMS não são integrados ao TOTVS Gestão de Pessoas.
