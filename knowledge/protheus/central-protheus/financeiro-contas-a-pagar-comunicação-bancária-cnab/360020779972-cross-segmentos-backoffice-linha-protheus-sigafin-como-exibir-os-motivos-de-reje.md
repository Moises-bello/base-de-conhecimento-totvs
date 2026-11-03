---
article_id: 360020779972
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: f585b8a4af829987dad31dd4471a0319aa47cea07f8a79b2de91dd1bddb01852
fetched_at: '2026-06-28T22:37:55.384245+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como exibir os motivos
  de rejeições no relatório do arquivo de retorno SISPAG
type: support-article
updated_at: '2022-06-24T17:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020779972-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-exibir-os-motivos-de-rejei%C3%A7%C3%B5es-no-relat%C3%B3rio-do-arquivo-de-retorno-SISPAG
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00min  
  
Dúvida**Como exibir os motivos de rejeições no relatório do arquivo de retorno SISPAG  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Para que os motivos de rejeições sejam exibidos no Relatório do arquivo de retorno SISPAG, é necessário a utilização do parâmetro **MV\_TABREJ** e a criação de uma tabela de código de rejeições na SX5 (Tabelas genéricas), adicionando nos itens, as descrições das ocorrências informadas no layout do banco.

Neste parâmetro indique o código criado para que o sistema imprima a descrição conforme o código retornado pelo banco.
