---
content_hash: 52345729b31f866687e20cb33926a459ce07bb1aca80a09b0c6d1670c2b78100
fetched_at: '2026-06-29T00:09:34.688912+00:00'
page_id: '425459222'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice)  – Pagamento de Comissões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459222
version: 8
---

**Integração Folha de Pagamento x Logix – Pagamento de Comissões**

---

A Integração Folha de Pagamento x Logix - Pagamento de Comissões tem o objetivo de receber pagamentos de Comissões do *BackOffice* Logix para que os mesmos sejam lançados no Envelope de Pagamento do Totvs Folha de Pagamento.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

* O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x Backoffice Logix:
* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Backoffice Logix
* Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha Pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (MONTHLYPAYROLL 1.000) está mapeada.

O processo de integração de Pagamento de Comissões será gerado no Logix onde o RM recebe as informações. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML.O pagamento de comissões vindo do Logix será salvo no RM Folha de Pagamento | Folha Mensal | Consulta | Consulta Movimento da Integração, com a origem do evento igual a *Connector*.

**Observação**

É necessário informar no *BackOffice* Logix o código o evento que será usando para lançamento de pagamento de comissão e o código de evento para estorno de pagamento de comissão. Não é feita a integração de cadastro de Eventos entre os sistemas, sendo o mesmo configurado manualmente no *BackOffice* Logix.  
 É necessário integrar o funcionário que irá receber o lançamento de pagamento de comissão com o *BackOffice*Logix.   
 Caso a base do Folha de Pagamento não esteja parametrizada para usar Cálculo por Centro de Custo, e o *BackOffice* Logix enviar um pagamento de comissão informando o Centro de Custo, o mesmo será desconsiderado, não preenchendo o campo referente ao centro de custo na tabela da Consulta Movimentação Integração.  
 Os pagamentos serão enviados por competência e irão sobrescrever os antigos enviados pela integração, caso sejam da mesma competência, Chapa e Origem da integração.

Dessa forma, a integração atenderá os seguintes objetivos:

* Para lançar grupo de eventos para os movimentos integrados, será necessário marcar o campo 'Lançar eventos da integração com outros aplicativos' nos parâmetros de grupo de eventos. Feita a parametrização o usuário clica em 'Lançar', o sistema busca na base de dados os movimentos integrados conforme parâmetros informados. Caso exista, o movimento é lançado.

Para verificar se a integração dos dados foi enviada corretamente do Logix para o RM Folha de Pagamento, acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas. Pesquise pelo registro com identificador "MONTHLYPAYROL" e pela data de criação da mensagem. Selecione a mensagem e  clique em Anexos | Informação de execução de mensagem. Selecione o registro e clique em editar. No campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.

---

**Informações Complementares**

Informações sobre Web Services
