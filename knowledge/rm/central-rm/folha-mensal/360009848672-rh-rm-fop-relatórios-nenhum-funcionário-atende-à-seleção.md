---
article_id: 360009848672
category: Folha Mensal
content_hash: 4a812a384e72afa344a387d4c24ee19b52c5b0ba023e98fcee1b883f00b1f60e
fetched_at: '2026-06-28T22:47:00.312139+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Relatórios: Nenhum funcionário atende à seleção'
type: support-article
updated_at: '2025-03-07T14:52:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009848672-RH-RM-FOP-Relat%C3%B3rios-Nenhum-funcion%C3%A1rio-atende-%C3%A0-sele%C3%A7%C3%A3o
---

**Ocorrência**No Totvs Folha de Pagamento, ao tentar realizar a geração de relatórios do sistema, alguns funcionários não aparecem em relatórios de competências anteriores, mesmo com todos os filtros parametrizados corretamente. Nestes casos o aviso é apresentado: **NENHUM FUNCIONÁRIO ATENDE À SELEÇÃO.**  
  
![ERRO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008308551/ERRO.png)  
  
**Ambiente**RM - Folha de pagamento - Todas as versões  
  
**Causa**O aviso ocorre pois para que o funcionário seja considerado nos relatórios do sistema em competências anteriores, é obrigatório o preenchimento dos cinco históricos citados abaixo, no cadastro do funcionário:  
  
- Histórico de situação;  
- Histórico de seção;  
- Histórico salarial;  
- Histórico de função;  
- Histórico de horários.  
 **Solução** Para solucionar este aviso é preciso verificar se os cadastros estão corretos nos históricos de situação, seção, salarial, função e de horários, no cadastro do funcionário.  
  
Uma ferramenta para simplificar esta busca é a **validade da base de dados**, que está disponível em **Folha Mensal | Validações**. Esta rotina localiza possíveis erros na base de dados dos funcionários, inclusive nos cadastros dos históricos. Execute a validação e corrija os erros relativos aos históricos do funcionários.
