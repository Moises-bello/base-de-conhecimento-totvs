---
content_hash: 20246f0f5fec263aad26d7bb0fbc0b1b986704b7c27efe973298d5ff0a55b996
fetched_at: '2026-06-29T00:09:34.507333+00:00'
page_id: '425459174'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice) – Pagamento de Autônomos Externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459174
version: 7
---

**Integração RM Folha de Pagamento x Logix – Pagamento de Autônomos Externos**

---

A Integração RM Folha Pagamento x Logix - Pagamentos de Autônomos Externos tem o objetivo de receber os dados de INSS dos autônomos, para calcular e demostrar os valores de INSS provenientes de outros BackOffices, nos processo: Geração SEFIP, Guia de INSS, Folha Analítica.   
 Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

* No módulo de Integração deve estar configurado a integração Folha de Pagamento RM x Logix:
* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x Outros BackOffice Autônomos.
* Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha Pagamento RM x Outros BackOffice Autônomos | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1015 (EXTERNALAUTONOMOUSPAYMENT 1.000) está mapeada.
* O De-Para da integração deve ser criado conforme exemplo abaixo:
  + Tabela RM: GFILIAL
  + Chave Primária RM: CODCOLIGADA|CODFILIAL
  + Valor Chave Primária RM: **1|1**
  + Sistema Integrado: LOGIX
  + Valor Chave Integração: **01|01**

O processo de integração de Pagamento de Autônomos Externos será gerado no Logix onde o RM recebe as informações. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML. Os dados serão salvos no RM Folha de Pagamento | Encargos | Autônomos Externos.  
 Dessa forma, a integração de Pagamentos de Autônomos Externos atenderá os seguintes processos da Folha de Pagamento, responsáveis por gerar os valores de INSS do Autônomos:

* **Guia de INSS:** Para gerar a Guia de INSS, com os valores de pagamento para os Autônomos Externos, acesse Encargos | Guia de INSS, selecione a coligada, clique em adicionar parâmetros à coligada, depois, marque o campo 'Importar Autônomos Externos (integrados de Outros *BackOffices*)' e continue o processo. O valor pagos aos Autônomos Externos será informado no campo Autônomos Não Cad. e, o valor pago pelos Autônomos referente a contribuição de INSS será informado no campo INSS Aut. (M. P. 83) da aba valores da Seção.
* **SEFIP:** Para gerar a SEFIP, com os valores de pagamento para Autônomos Externos, acesse Encargos | SEFIP | SEFIP,  selecione a coligada | clique em adicionar parâmetros à coligada, e na aba integrações marque o campo 'Importar Autônomos Externos (Integrados de Outros *BackOffices*)' e continue o processo.
* **Folha Analítica**: Para Gerar a Folha Analítica, com os valores de pagamento para Autônomos Externos, acesse Folha Mensal | Folha Analítica, na interface Seleção de Funcionários marque o campo 'Importar Autônomos Externos (Integrados de Outros *BackOffices*)' e continue o processo.

**Observação**

Quando marcado o parâmetro 'Importar Autônomos Externos (Integrado de Outros BackOffices)' nos processos acima, o sistema desabilita o parâmetro 'Importar Autônomos do RM Fluxus / RM Nucleos', pois eles são excludentes.   
 Para verificar se a integração dos dados foi enviada corretamente do Logix para o RM Folha de Pagamento, acesse o módulo Integração | Mensagem Única | Fila de Mensagens Únicas. Pesquise pelo registro com identificador "EXTERNALAUTONOMOUSPAYMENT" e pela data de criação da mensagem. Selecione a mensagem e  clique em Anexos | Informação de execução de mensagem. Selecione o registro e clique em editar. No campo "Status da Mensagem" é possível ver o status da integração dos dados se teve sucesso ou erro.

---

**Informações Complementares**

Informações sobre Web Service
