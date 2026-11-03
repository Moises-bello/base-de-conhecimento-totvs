---
content_hash: 181ad97a444538ab3854a6a74268eb6bdd7c738ae4c42470dbbb26abfdeec62b
fetched_at: '2026-06-29T00:09:37.385033+00:00'
page_id: '425459600'
product: rm
source: tdn-rm
title: TOTVS Folha de Pagamento x BackOffice Logix - Cadastro de Seção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459600
version: 9
---

**Integração Folha | Logix – Cadastro de Seção**

---

A Integração Folha x Logix de Cadastro de Seção tem o objetivo de enviar os dados de seções visando integrar estas informações para utilização dos dados com o backoffice Logix.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

1. O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x Backoffice Logix:  
     
         Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Backoffice Logix

* Feito o processo acima, acesse o menu Integração | Gestão | Fórmula Visual | Fórmula Visual | Processos | Importação     de Fórmula Visual e importa o pacote (FOPWKF0002 - Department.TotvsWF).

                   O pacote deverá ser disponibilizado no instalador, dentro da pasta "Objetos gerenciais/Fórmulas Visuais"

* O sistema exibe tela de processo para importação da fórmula visual, selecione a categoria | marque a opção "Importar Gatilhos" e execute o processo. Para verificar se os gatilhos foram importados corretamente, selecione a fórmula visual (DEPARTMENT 2.000) | clique em editar | na aba Gatilhos procure pelo gatilho "FOPSECAODATABR".
* Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (DEPARTAMENT 2.000) está mapeada.

O processo de integração de seção da folha de pagamento será gerado por meio gatilhos por fórmula visual que serão disparados ao incluir/alterar ou excluir seções, reestruturação de seção e ao trocar código da seção. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML. (Caso tenha algum help de webservice seria interessante colocar um "Veja mais sobre webservice clicando aqui)  
   
Dessa forma, a integração atenderá os seguintes objetivos:

* Incluir seção: o cadastro de seção é gerado no TOTVS Folha de Pagamento e enviado para o sistema LOGIX.
* Alteração de seção: a alteração de seção é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Exclusão de seção: a exclusão de seção é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Trocar código da seção: o processo de troca de código de seção é gerado no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.   
  Reestruturação de seção: o processo de reestruturação de seção é gerado no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.

**Observação**

* Ao fazer a integração da Seção com o *BackOffice* Logix é necessário verificar se o Centro de Custo informado é um Centro de Custo integrado do *BackOffice* Logix. O processo faz a consistência do campo e caso o centro de custo não foi integrado, retornar erro que pode ser verificado na informação da execução da mensagem.
* Quando é feito a alteração da filial da Seção, é disparado o gatilho de alteração de cadastro do funcionário, alterando o mesmo no *BackOffice* Logix.
* Para verificar se a integração dos dados foi enviada corretamente para o Logix, após acionar os gatilhos citados acima acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas pesquisa, pesquise pelo registro com identificador "DEPARTAMENT" e pela data de criação da mensagem | selecione a mensagem | clique em anexos Informação de execução de mensagem | selecione o registro e clique em editar: No campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.

---

**Informações Complementares**

[Informações sobre Web Service](http://tdn.totvs.com/pages/viewpage.action?pageId=425459227)
