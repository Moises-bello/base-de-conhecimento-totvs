---
content_hash: 840f2ff6dd2152ef62c9209fdcc4a7ae1544a99e5c6ac0ee105a42403fc00041
fetched_at: '2026-06-29T00:08:49.366346+00:00'
page_id: '330138250'
product: rm
source: tdn-rm
title: Inscrição do candidato através do responsável (Processo Seletivo Ensino Básico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330138250
version: 13
---

### **Essa funcionalidade está disponível a partir da versão 12.1.18**

Disponibilizada a possibilidade de inscrição de candidatos através do responsável. Esta opção é utilizada em Instituições que trabalham com processos seletivos que envolvem candidatos menores de 18 anos e precisam de um responsável para responder por eles.

Para a inscrição no Processo Seletivo no Ensino Básico,  além de inscrever o(s) candidato(s) que estará vinculado a ele, o responsável, também, poderá se candidatar a uma vaga em uma das áreas ofertadas. 

**Parametrização:**

* Alterar o contexto para o Ensino Básico e parametrizar para que o Processo Seletivo utilize o Novo portal de inscrições.
* No cadastro da Área de Interesse ofertada, deverá ser configurado a Matriz referente ao contexto Ensino Básico.

**Inscrição no Portal:**

* Ao acessar a URL do portal do Processo seletivo, o contexto deverá ser levando em consideração;

* Ao iniciar o processo de inscrição, será apresentado a pergunta (obrigatória) se ele é ou não o candidato da inscrição.

* Se a opção marcada for: NÃO, o formulário irá alterar a descrição do campo referente ao cadastro do Responsável, onde deverá informar os campos, onde os mesmo serão aproveitados no formulário principal.
* Se a opção marcada for: SIM , o formulário será alterado para as informações referente ao cadastro do candidato.

ATENÇÃO!!!

**A partir da versão 12.1.18.158**

Quando o parâmetro de utilizar o CPF para login estiver marcado e o candidato possuir responsável pela inscrição, esse terá o CPF obrigatório e o candidato não. Caso só exista o candidato esse passará a ter o CPF obrigatório.   
Durante a parametrização do processo seletivo, não é mais obrigado marcar o campo de obrigatório para o CPF do candidato e/ou responsável quando a opção de utilizar o CPF para login estiver selecionada.

Após ser redirecionando para o formulário principal, será exibido um mini formulário do Responsável da inscrição e mais a abaixo o do Candidato.

Os dados a serem solicitados devem ser os mesmos para todos os candidatos de acordo com o que foi parametrizado para o formulário do processo seletivo.

IMPORTANTE!!!

O responsável pela inscrição também poderá ser: Pai, Mãe, Resp. Acadêmico, Resp. Financeiro.

Para otimizar o processo de inscrição, o responsável poderá aproveitar os dados através da lista: ***Utilizar o responsável como xxxxxx:***

ATENÇÃO!!!

Quando a inscrição é realizada pelo responsável, o usuário e a senha criados após a finalização da inscrição serão do responsável. Os candidatos vinculados ao responsável não terão usuário e senha.

Após finalizar o processo de inscrição, o Responsável será redirecionado para o menu: Central do Candidato.

Através da Central do Candidato, o Responsável poderá:

* Alterar os dados do responsável;
* Alterar a senha para o acesso ao portal do processo seletivo;
* Inscrever um novo candidato;
* Alterar os dados pessoais do candidato vinculado ao responsável;
* Emitir o comprovante de inscrição, boleto e efetuar o pagamento com cartão referente a taxa de inscrição.

Além de toda a parametrização, o responsável pela IE poderá gerar a URL específica para o Nível de Ensino através:

**TOTVS Processo Seletivo | Parâmetros | Parâmetros do Sistema | (Guia) Serviços | Portal Processo Seletivo (Novo)**

Atenção

A partir da versão 12.1.28, não é mais necessário informar a porta na url, no local foi adicionado um caminho novo na url. Desta forma, ficando assim: http://SERVIDOR/FrameHTML/web/app/edu/PortalProcessoSeletivo/

Atenção

A partir da versão 12.1.33, poderá ser visualizada, pelo responsável da inscrição, uma lista com as inscrições dos dependentes e as informações vinculadas a eles.

##### **Listar informações dos Dependentes**

O usuário responsável pela inscrição, ao acessar a Central do Candidato, poderá visualizar a informações dos seus dependentes

**Acesso a Central do Candidato realizada pelos Dependente**

Os usuários dependentes, também, poderão acessar a Central do Candidato através da forma da forma de identificação parametrizada para o Processo Seletivo.

DEPENDENTE I - Geraldo Bryan de Paula

Realização de um acesso com o CPF e a data de nascimento do dependente “Geraldo Bryan de Paula”.

Na Central do Candidato serão exibidas apenas as informações referentes ao dependente que realizou o acesso, não permitindo a visualização das informações de outros dependentes do seu responsável.

Atenção

Caso o processo seletivo não esteja parametrizado para solicitar o nome do candidato ou não seja obrigatório e o mesmo não for informado no momento da inscrição, através do portal do Processo Seletivo, pelo responsável da inscrição, a Central do Candidato irá exibir a lista dos dependentes com uma numeração sequencial no lugar do nome em branco.

Os dependentes serão representados através de um número sequencial, de acordo com a sua ordem de inscrição, e poderão ser selecionados para a visualização de suas demais informações cadastradas:
