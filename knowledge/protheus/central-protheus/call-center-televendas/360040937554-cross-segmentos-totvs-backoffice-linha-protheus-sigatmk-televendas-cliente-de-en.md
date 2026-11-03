---
article_id: 360040937554
category: Call Center - Televendas
content_hash: b75b46b3233c05c0830a4b5a8bf4f741bdc1453e2b2c24bb8f324cce7757570b
fetched_at: '2026-06-28T22:41:30.383398+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK -Televendas - Cliente
  de Entrega e Condição de Pagamento Tipo 9
type: support-article
updated_at: '2022-06-22T19:14:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040937554-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Televendas-Cliente-de-Entrega-e-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-9
---

**Ocorrência**

Tratamento de Cliente de Entrega no modulo SIGATMK (Rotina de Televendas)  

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- A partir da versão 12.1.17   
  
**Causa**

1- Criação dos campos de Cliente e Loja de entrega (**UA\_CLIENT** e **UA\_LOJAENT**) no **Atendimento Televendas**, para que considere o cliente de entrega para atualização do CFOP, assim considerando os impostos corretamente, caso por exemplo o cliente de entrega seja de um estado diferente do cliente da venda.

2- Condição de pagamento**tipo 9**não está respeitando os campos (**E4\_IPI** e **E4\_SOLID**), quando forem configurados igual a **Junta,**no**Atendimento TeleVendas.**

**Solução**

1- Foram criados os campos (**UA\_CLIENT** e **UA\_LOJAENT) na Tabela SUA** conforme configurações abaixo:

2- Efetuado ajuste para condição de pagamento**tipo 9**, para quando utilizado a regra da mesma em porcentagem(**%**), assim respeitando os campos (**E4\_IPI** e **E4\_SOLID**), quando forem configurados igual a **Junta**.

**Para correção da Situação :**

1. Não haverá a expedição de pacote de dicionário específico para a criação deste campo. A criação automática deste campo ocorrerá apenas na próxima expedição oficial dos dicionários da release prevista para **Fevereiro/2020**;
2. Caso necessite, o campo poderá ser criado via Configurador (**SIGACFG**). Para tanto, siga os procedimentos conforme instrução :  <https://tdn.totvs.com/pages/releaseview.action?pageId=527846712>

1. Além da criação do novo campo, para que esta funcionalidade esteja disponível em seu ambiente, é necessária a aplicação do patch de atualização deste requisito, contendo os programas fontes envolvidos, download disponível no endereço: 12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=887678> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=887677> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=887676> ;
