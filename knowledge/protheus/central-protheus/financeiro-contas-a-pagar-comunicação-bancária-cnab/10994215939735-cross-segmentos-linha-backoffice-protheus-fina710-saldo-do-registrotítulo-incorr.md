---
article_id: 10994215939735
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 476110f29f03aa86fafb4359878e8f5a3429b7fbd5b186659b086decd65d1d14
fetched_at: '2026-06-28T22:37:56.481304+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - FINA710 - Saldo do registro/título
  incorreto - Como atualizar os registros da F76/F75 sem alterar o MV_TFCJOBT
type: support-article
updated_at: '2023-11-27T19:43:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10994215939735-Cross-Segmentos-Linha-BackOffice-Protheus-FINA710-Saldo-do-registro-t%C3%ADtulo-incorreto-Como-atualizar-os-registros-da-F76-F75-sem-alterar-o-MV-TFCJOBT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19363737682199) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como atualizar os registros da F76/F75 sem alterar o **MV\_TFCJOBT**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro a partir da Release 12.1.33  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

O parametro **MV\_TFCJOBT**irá ler as informações do campo **S\_T\_A\_M\_P\_** que é visivel somente no banco de dados das tabelas **SC6/SC7/SE1/SE2**, caso o campo **S\_T\_A\_M\_P\_** esteja com data maior que o parametro, ao rodar o JOB ira atualizar as informações dos registros nas tabelas **F76 - ( Pedidos de Vendas / Compras )** e **F75 ( Contas a Receber / Contas a Pagar ).**  
  
Para corrigir um registro que tem seu saldo incorreto no Novo Gestor Financeiro, deve alterar alguma informação do registro **( Exemplo: Alterar a informação de Historico do titulo E2\_HIST/E1\_HIST ou algum campo que não irá impactar nos saldos ou contabilização )** para que o campo **S\_T\_A\_M\_P\_** grave a **data/hora** da alteração e ao rodar o JOB novamente, seja atualizado as informações do **Pedido/Titulo** 

Títulos que houveram baixa e apresentam saldo no NGF, deve se excluir a baixa, baixar novamente e aguardar o processo de agendamento, atualizar os dados do novo com o correto saldo do titulo.

Quando o título no Financeiro é baixado integralmente os campos **F75\_VLTIT, F75\_SALDO** são zerados, neste caso, se a carga de dados não alterar após baixa os campos referente aos títulos, deve ser feito o ajuste manual dos campos.

**A manipulação da base de dados não é contemplada em nosso escopo de atendimento de Suporte Técnico, esse tipo de procedimento é efetuado apenas por analista in loco.**

**Confira nosso Escopo -  <https://tdn.totvs.com/pages/releaseview.action?pageId=547876496>**

Saiba mais  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047)  
[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=611007335)
