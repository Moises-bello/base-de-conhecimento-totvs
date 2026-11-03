---
content_hash: a256ea71b18f5a985bebd6f59a124c287b43c0aaf29071edc73d24b956e69fe2
fetched_at: '2026-06-29T00:09:37.376348+00:00'
page_id: '425459596'
product: rm
source: tdn-rm
title: TOTVS Folha de Pagamento x BackOffice Logix - Cadastro de Função
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459596
version: 5
---

**Integração Folha | Logix – Cadastro de Função**

---

A Integração Folha x Logix de Cadastro de Função tem o objetivo de enviar os dados de funções visando integrar estas informações para utilização dos dados com o backoffice Logix.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

· O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x Backoffice Logix:

* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Backoffice Logix

· Feito o processo acima, acesse o menu Integração | Gestão | Fórmula Visual | Fórmula Visual | Processos | Importação de Fórmula Visual e importa o pacote (FOPWKF0002 - Role.TotvsWF).

* O pacote deve ser disponibilizado no instalador, dentro da pasta "Objetos gerenciais/Fórmulas Visuais"

·          O sistema exibe tela de processo para importação da fórmula visual, selecione a categoria | marque a opção "Importar Gatilhos" e execute o processo. Para verificar se os gatilhos foram importados corretamente, selecione a fórmula visual (Role \_1\_000) | clique em editar | na aba Gatilhos procure pelo gatilho "FOPFUNCAODATA".  
  
·  Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (ROLE 1.000) está mapeada.  
  
O processo de integração de função da folha de pagamento será gerado por meio gatilhos por fórmula visual que serão disparados ao incluir/alterar ou excluir funções e ao realizar a Cópia de função entre coligadas. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML. (Caso tenha algum help de webservice seria interessante colocar um "Veja mais sobre webservice clicando aqui)  
   
Dessa forma, a integração atenderá os seguintes objetivos:

* Incluir função: o cadastro de função é gerado no TOTVS Folha de Pagamento e enviado para o sistema LOGIX.
* Alteração de função: a alteração de função é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Exclusão de função: a exclusão de função é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Cópia de função entre coligadas: a cópia de função é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.

Para verificar se a integração dos dados foi enviada corretamente para o Logix, após acionar os gatilhos citados acima acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas pesquisa, pesquise pelo registro com identificador "ROLE" e pela data de criação da mensagem | selecione a mensagem | clique em anexos Informação de execução de mensagem | selecione o registro e clique em editar:

·  No campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.
