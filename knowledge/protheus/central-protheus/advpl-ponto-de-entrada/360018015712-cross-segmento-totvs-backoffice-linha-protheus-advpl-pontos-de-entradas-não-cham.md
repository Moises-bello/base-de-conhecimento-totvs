---
article_id: 360018015712
category: ADVPL - Ponto de Entrada
content_hash: 2b4a35128e9a68095e0e5b5ac7f3582d8634418bee873143824621f02233aa89
fetched_at: '2026-06-28T22:40:12.835926+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entradas
  não chamados em consulta padrão '
type: support-article
updated_at: '2021-12-30T17:02:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018015712-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entradas-n%C3%A3o-chamados-em-consulta-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar uma consulta padrão**(F3)** de uma determinada tabela, os pontos de entradas da rotina responsável pelo cadastro não são chamados.

Ex.: Utilizo a **FINA050**, e seleciono a consulta padrão**(F3)** no campo Fornecedor(**MATA020**), os pontos de entrada da **MATA020** não são chamados 

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A utilização da consulta padrão serve para buscar incluir, selecionar e visualizar registros de tabelas dentro do sistema. Quando usamos o botão "**INCLUIR**", é chamada a função **AxInclui(),** que permite, por meio de uma interface, que o usuário inclua as informações de um arquivo de dados, conforme a necessidade da aplicação, e por esse motivo os pontos de entrada da rotina responsável pelo cadastro não são chamados.
