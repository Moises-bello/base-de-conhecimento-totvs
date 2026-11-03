---
content_hash: 2ec227412620b64b2382a0d261d91c0c2c563bd01984c16e73fb0a038e3a314e
fetched_at: '2026-06-29T00:09:37.523321+00:00'
page_id: '425459630'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice) -  Transferência de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459630
version: 3
---

**Integração Folha | Logix – Transferência de Funcionário**

---

A Integração Folha x Logix de Transferência de funcionário tem o objetivo de enviar os dados de transferências visando integrar estas informações para utilização dos dados com o BackOffice Logix.  
Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

·          O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x Backoffice Logix:

* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Backoffice Logix

·          Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha Pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (SETEMPLOYEEBRANCHTRANFER 1.000) está mapeada.  
  
  
O processo de integração de transferência de funcionário será gerado por meio gatilhos internos. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML. (Caso tenha algum help de webservice seria interessante colocar um "Veja mais sobre webservice clicando aqui)

Dessa forma, a integração atenderá os seguintes objetivos:

* Transferência de Funcionário: a transferência de funcionário é realizada através do processo de rescisão onde, o tipo de rescisão deve ser (5- Transferência sem ônus p/ Cedente **ou** 6- Transferência com ônus p/ Cedente). Este processo será gerado no TOTVS Folha de Pagamento e enviado para o sistema LOGIX.

**Importante:**

O gatilho deve ser disparado somente se a transferência for para uma outra filial (CNPJ diferente).  
    
 Para verificar se a integração dos dados foi enviada corretamente para o Logix, após acionar os gatilhos citados acima acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas pesquisa, pesquise pelo registro com identificador "SETEMPLOYEEBRANCHTRANFER" e pela data de criação da mensagem | selecione a mensagem | clique em anexos Informação de execução de mensagem | selecione o registro e clique em editar:

·          No campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.
