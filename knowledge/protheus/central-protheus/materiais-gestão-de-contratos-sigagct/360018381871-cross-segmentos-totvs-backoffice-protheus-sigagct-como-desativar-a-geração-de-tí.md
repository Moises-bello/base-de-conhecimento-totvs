---
article_id: 360018381871
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 969f5e277ee221c473553f98c2b0f1bf54a8d62d03684ec4d8cfa91adf543a22
fetched_at: '2026-06-28T22:37:21.476153+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como desativar a geração
  de títulos provisórios na mudança de situação do contrato ?
type: support-article
updated_at: '2025-02-27T11:47:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018381871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-desativar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-provis%C3%B3rios-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-do-contrato
---

**Dúvida**Como desativar a geração de títulos provisórios (PR) na mudança de situação do contrato ?  
  
**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução**Nos contratos cadastrados com Cronograma Financeiro, ao realizar a mudança de situação do contrato para "Vigente" via rotina Manutenção (CNTA300), por padrão, são gerados títulos provisórios (PR) nas tabelas Contas a Pagar (SE2) ou Contas a Receber (SE1) referentes às parcelas do Cronograma Financeiro incluído no contrato, porém é possível desativar a geração desses títulos.Para desativar a geração desses títulos "PR", realize os seguintes passos:  
  
1. Acesse o módulo Configurador (SIGACFG);  
2. Acesse as opções Base de Dados - Dicionário - Base de Dados;  
3. Acesse a opção Parâmetros;  
4. Localize o parâmetro **MV\_CNPROVI** e configure como N (Não).

***Saiba Mais:***  
[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
