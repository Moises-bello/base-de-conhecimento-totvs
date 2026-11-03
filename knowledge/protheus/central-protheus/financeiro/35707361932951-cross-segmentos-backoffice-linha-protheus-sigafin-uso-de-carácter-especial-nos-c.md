---
article_id: 35707361932951
category: Financeiro
content_hash: 8bdb3216d05a6eb1c1fc0e1d1b3077fdab7bda581635e685886d887bdc514ea2
fetched_at: '2026-06-28T22:38:04.138800+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Uso de carácter especial
  nos cadastros
type: support-article
updated_at: '2025-10-17T18:35:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707361932951-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Uso-de-car%C3%A1cter-especial-nos-cadastros
---

Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Existe um padrão recomendado pela TOTVS para os cadastros em geral?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões

**Solução:**

Como boa prática de uso, a TOTVS **recomenda não utilizar caracteres especiais** em nenhum campo de **cadastros** do sistema Protheus.

As aspas (simples ou duplas) são utilizadas para encadear uma string (um ou mais caracteres), sendo ela uma variável ou não.

Quando utilizadas em campos de cadastro — como o **A2\_NOME** (cadastro de fornecedores) — podem causar **falhas no processamento**, **erros de execução** ou **inconsistências na montagem de queries.**

Para garantir a integridade dos dados e evitar inconsistências em rotinas ou relatórios, **não utilize caracteres especiais** (como aspas, barras, cerquilhas, sinais matemáticos, etc.) nos campos de cadastro.  
Prefira sempre **letras, números e espaços simples**.

**Saiba Mais:**

[**TDN - Caracteres especiais nos campos de cadastros gerais**](https://tdn.totvs.com/display/public/PROT/FIN0013_Uso_de_caracteres_especiais_nos_cadastros)
