---
content_hash: 66b4d3c09817f9b086bf203f32cdb62231b2b2c8be288fcc11c086dfa46193e4
fetched_at: '2026-06-29T00:10:08.885015+00:00'
page_id: '452719601'
product: rm
source: tdn-rm
title: RM Portal - Banco de Talentos e Mensagens Automáticas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719601
version: 3
---

**RM Portal - Banco de Talentos e Mensagens Automáticas**   
   
**Banco de Talentos (Currículo)**

Considerar esta coligada e estes parâmetros como padrão para currículos na web

Marcando este parâmetro, o sistema considera a coligada atual e os parâmetros definidos nesta para as definições no Banco de Talentos. Caso contrário, não permite o acesso ao Banco de Talentos porque não existe definida uma coligada padrão informada.

Transformar letras dos campos alfanuméricos para maiúsculas

Marcando este parâmetro, todas as informações inseridas no Banco de Talentos com letras minúsculas serão convertidas para maiúsculas.  
   
Validar usuário por CPF, permitindo alteração cadastral para funcionário

Marcando este parâmetro, quando um funcionário do sistema, efetuar um novo cadastro pelo Banco de Talentos, será validado o seu CPF e Nome, caso ele ainda não tenha nenhum usuário do mesmo, será feita a sua atualização cadastral e seu cadastro será realizado.

Se o cadastro do funcionário estiver sendo realizado agora, ao salvar os dados, caso a validação esteja ok, será criado um usuário do RM Portal já diretamente ligado ao dados do funcionário.  
   
Limites para definição de pretensão salarial

Campo para definição do intervalo de valores de salários que serão validados no momento do cadastramento do currículo.

Número máximo de vagas ativas a que um candidato pode se candidatar

Campo para definição da quantidade máxima de vagas a qual o candidato poderá se candidatar.  
   
Número máximo de caracteres para campos descritivos

Campo para definição da quantidade máxima de caracteres que serão possíveis para fazer uma descrição.

Questionário padrão

Campo para definição do questionário que será padrão para todos os candidatos que preencherem os currículos independentemente da vaga.

**Observação:** Os questionários são cadastrados pelo menu Planejamento e Captação| Questionários| Questionários.

Códigos de outros questionários a serem exibidos (separar por vírgula)

Campo para definição de outros questionários que poderão ser exibidos juntamente ou não com o Questionário Padrão.

Usar requisitos de acesso em Idiomas

Marcando o parâmetro, no cadastro de Idiomas (Planejamento e Captação| Tabelas Auxiliares| Idiomas) habilita os campos de requisito para escrita/leitura/conversação e no Banco de Talentos consequentemente aparece os requisitos de acesso.

Usar área de conhecimento

Marcando este parâmetro, em Perfil| Formação Acadêmica é possível informar a área de conhecimento do candidato.  
   
Consistir preenchimento mínimo do currículo na candidatura de vagas

Marcando este parâmetro, o Banco de Talentos vai exigir o preenchimento mínimo do currículo para que o candidato possa se candidatar a uma vaga.  
Painéis que podem restringir a candidatura:  
   
·         Dados Pessoais  
   
·         Formas de Contato  
   
·         Perfil Profissional  
   
·         Informações Adicionais  
   
   
Painéis que podem emitir mensagem de aviso:  
   
·         Experiência profissional  
   
·         Formação Acadêmica  
   
·         Formação Adicional  
   
·         Idiomas  
   
·         Qualificações  
   
**Observação:**

Quando este parâmetro estiver marcado, serão validados os campos que foram configurados como obrigatórios para os painéis. Estes campos podem ser configurados no  na aba Planejamento e Captação do modulo Gestão de Pessoas da MDI.

Os campos que são do tipo marcação, por exemplo, os do tipo de deficiência, são sempre considerados preenchidos pois eles existem para saber se o candidato possui a característica ou não então eles não são validados para esse parâmetro.

Considera o questionário como obrigatório para se candidatar a vaga

Parâmetro marcado: Na vaga disponível no Banco de Talentos, aparecerá um botão de "Pré-Candidatura", quando existir questionários obrigatórios. E somente após o preenchimento do questionário obrigatório, a candidatura se concretiza.  
   
Parâmetro desmarcado: Na vaga disponível no Banco de Talentos, aparecerá um botão de "Candidatar" e a candidatura se concretiza, sem validação de preenchimento de questionários.  
   
**Observação:**

Quando este parâmetro estiver marcado, no processo "Iniciar Processo de Seleção/Executar Triagem" serão considerados na triagem somente os candidatos que responderam os questionários obrigatórios e que se enquadrem nas demais regras da triagem.

**Mensagens automáticas**

Receber aviso por e-mail após o cadastro de um novo candidato

Marcando este parâmetro, sempre quando um candidato realizar o cadastro do seu currículo no Banco de Talentos, o sistema enviará um e-mail ao usuário informado no menu Configurações| Parametrizador| E-mail.

Receber aviso por e-mail após atualização do currículo de funcionário

Marcando este parâmetro, sempre quando um funcionário atualizar o seu currículo, o sistema enviará um e-mail para a chefia imediata do funcionário. Caso o funcionário seja chefe da sua própria seção, o sistema enviará o e-mail para o chefe da seção imediata superior.

Usuário para agendamento de mensagens

Campo para definição do usuário que será responsável pelo envio das mensagens.

**Observação:**

Serão visualizados somente usuários cadastrados como supervisores.

Formatação de mensagens

Campo para definição de mensagens customizadas previamente cadastradas para o envio de mensagens.

Boas Vindas

- Deve ser informada uma mensagem customizada de Boas Vindas para o Banco de Talentos. Caso não tenha informação neste campo, será enviado ao candidato a mensagem padrão do sistema.   
Lembrete de Senha

- Deve ser informada uma mensagem customizada de Lembrete de Senha para o Banco de Talentos. Caso não tenha informação neste campo, será enviado ao candidato a mensagem padrão do sistema.
