---
content_hash: b99c37e8223cb12ba49a57cc2a397917241b79b3c47e0eefcc04662080c99122
fetched_at: '2026-06-29T00:09:34.485698+00:00'
page_id: '425459168'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice) – Turno e Escala de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459168
version: 9
---

**Integração Folha | Logix – Turno e Escala**

---

A Integração Folha x Logix de Turno e Escala tem o objetivo de enviar os dados de Automação de Ponto visando integrar estas informações para utilização dos dados com o backoffice Logix.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

* O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x Backoffice Logix:
* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Backoffice Logix
* Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha Pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (SCHEDULEWORK 1.000) está mapeada.
* De-Para da integração deve ser criado e informado o código da coligada e o código do horário. Este cadastro deve ser feito por coligada e por código de horário (caso haja necessidade).

O processo de integração de turno e escala será gerado por meio gatilhos internos. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML.  
  
Dessa forma, a integração atenderá os seguintes objetivos:

* Criar Jornada Planejada: jornada planejada será gerada no TOTVS Folha de Pagamento ou no TOTVS Automação de Pontos e enviado para o sistema LOGIX.
* Configurar Jornada Planejada: a configuração de jornada planejada é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Copiar Jornada Planejada: a cópia de jornada planejada é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Exclusão de horário (caso tenha jornada planejada cadastrada): a exclusão de horário será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Cópia de horário (caso tenha jornada planejada cadastrada): a cópia de horário será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Cópia de horário entre coligadas (caso tenha jornada planejada cadastrada): a cópia de horário entre coligadas será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Importar horário: a importação de horário será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Horário por jornada: o horário por jornada será gerado no TOTVS Automação de Pontos e enviado para o sistema LOGIX.
* Incluir Índice de jornada: a inclusão de índice de jornada será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Alterar Índice de jornada: a alteração de índice de jornada será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Exclusão de Índice de jornada: a exclusão de índice de jornada será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Cópia de índice de jornada: a cópia de índice de jornada será gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.

Para verificar se a integração dos dados foi enviada corretamente para o Logix, após acionar os gatilhos citados acima acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas. Pesquise pelo registro com identificador "SCHEDULEWORK" e pela data de criação da mensagem. Selecione a mensagem e clique em anexos Informação de execução de mensagem. Selecione o registro e clique em editar, no campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.

---

**Informações Complementares**

Informações sobre Web Service
