---
article_id: 1500012284562
category: Financeiro - Conciliação de Vendas
content_hash: 1136304dba8d5716e345e614bd725046ec5c2a4774af257d01492e593790994e
fetched_at: '2026-06-28T22:37:26.216123+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA918 - Help A910NOFIELDS
  ao Acessar a Rotina de Conciliação de Pagamentos
type: support-article
updated_at: '2026-02-04T13:20:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012284562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA918-Help-A910NOFIELDS-ao-Acessar-a-Rotina-de-Concilia%C3%A7%C3%A3o-de-Pagamentos
---

**Ocorrência**  
Ao acessar a rotina Conciliação de Pagamentos FINA918, apresenta o Help A910NOFIELDS   
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Financeiro - A partir da versão 12

**Causa**  
A falta dos campos reservados (MSFIL), que precisam conter em todas as tabelas FIF, MEP e SE1  
  
**Solução**  
No **Configurador** (SIGACFG) acesse **Base de Dados**>**Dicionarios**>**Base de Dados**.  
Localize e posicione na tabela **SE1.** Edite a tabela.   
Clique em “**Campos**” e no botão **“Campos reservados”**.   
Marque o campo “**Filial de Inclusão**” e clique no botão “**Finalizar**” criando assim o campo.   
Confirme a criação ao sair da tabela.

Repita o processo para as tabelas **FIF E MEP**
