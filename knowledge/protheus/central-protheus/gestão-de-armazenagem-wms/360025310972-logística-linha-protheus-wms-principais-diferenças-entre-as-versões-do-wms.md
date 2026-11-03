---
article_id: 360025310972
category: Gestão de Armazenagem (WMS)
content_hash: 15ebd08b44fd3516f0e4805f2e93200eb1408fb79c2b8148e9de7656c9f2ec15
fetched_at: '2026-06-28T22:45:48.083778+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Principais diferenças entre as versões do
  WMS
type: support-article
updated_at: '2021-12-10T18:57:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025310972-Log%C3%ADstica-Linha-Protheus-WMS-Principais-diferen%C3%A7as-entre-as-vers%C3%B5es-do-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais as principais diferenças entre as versões do **WMS - Warehouse Management System**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 12.1.17  
  
**Solução**O **WMS** teve uma grande evolução de negócio e foi reescrito para atender novas funcionalidades.  
  
Algumas regras que se aplicam a ambas as versões, **WMS** atual e novo **WMS**, tiveram suas funcionalidades alteradas, porém mantiveram o mesmo objetivo final do processo.  
  
Dentre as principais diferenças para a nova versão temos:

* A separação das tabelas de estoque e movimentações;
* Produtos que controlam **WMS** não podem mais ser movimentados por rotinas de **Materiais**;
* O estoque por endereço passa a controlar as entradas e as saídas previstas;
* Todas as movimentações de estoque que foram efetuadas gerarão uma movimentação reversa ao serem estornadas;
* Todas as movimentações de estoque deverão ser finalizadas de forma posterior, mesmo quando não utilizada radiofrequência;
* Todas as movimentações **WMS** que já tiverem movimentado estoque permanecerão com situação igual a **0-Estornada**, ao serem estornadas;
* Todas as movimentações de **WMS** que efetuam transferência entre endereços dentro de um mesmo armazém não gerarão **SD3 - Movimentações Internas**;
* Uma movimentação de requisição gerará uma tabela auxiliar - **DH1 - TODOS**, que será utilizada para gerar a reserva de estoque para posteriormente efetivar a movimentação;
* A geração de saldo a classificar passou a ser parametrizável, sendo gerado apenas se estiver informado o parâmetro **MV\_WMSBLQE - Bloqueia saldo até encerramento do endereçamento?**;
* Alterada a forma de execução das ordens de serviço de expedição que dependem de reabastecimento.

**Saiba mais**Para visualizar todas diferenças entre as versões do **WMS**, acesse o *link*: [Principais Diferenças Entre as Versões do WMS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=317302807)
