---
article_id: 1500002732362
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e22f6f5b163f1b9e971612b059f6e09a4018d1d1959b2d738f6344f73c88b4d9
fetched_at: '2026-06-28T22:38:33.109346+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - A rotina Limpeza Mensal (MATA580) pode impactar nos Saldos dos Produtos
  em Estoque?
type: support-article
updated_at: '2021-04-28T15:52:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002732362-MP-FAT-A-rotina-Limpeza-Mensal-MATA580-pode-impactar-nos-Saldos-dos-Produtos-em-Estoque
---

**Dúvida**A rotina Limpeza Mensal (MATA580) pode impactar nos saldos dos produtos no estoque?  
  
**Ambiente**Microsiga Protheus – Faturamento – A partir da versão 12  
  
**Solução**

Caso execute a **Limpeza Mensal** (**MATA580**) o sistema mantém os saldos, porém ao executar a rotina **Refaz Saldos** (**MATA300**) ele reprocessa os saldos levando em consideração as tabelas **SC9**, **SC6** e **SD2**.

Questionamos a área técnica quanto ao uso da rotina e eles informaram que a Limpeza Mensal (MATA580) era uma rotina utilizada quando os arquivos do sistema eram **.DBF**, que atualmente ela está para ser **descontinuada**.

**Não orientamos** que utilize a rotina Limpeza Mensal (MATA580) atualmente, caso necessite de manutenção nas tabelas, sugerimos que entre em contato com seu Administrador de Banco de Dados, ou com seu gerente de atendimento solicitando um analista in loco para este procedimento.
