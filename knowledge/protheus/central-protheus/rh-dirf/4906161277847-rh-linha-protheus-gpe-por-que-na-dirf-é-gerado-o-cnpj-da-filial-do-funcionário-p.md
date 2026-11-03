---
article_id: 4906161277847
category: RH – DIRF
content_hash: ff759dd82611b166669cd63d7d478d5b6c6aa864d17b7e3bccab62d8e4930076
fetched_at: '2026-06-28T22:44:07.916548+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Por que na DIRF é gerado o CNPJ da filial do funcionário
  para o plano de saúde
type: support-article
updated_at: '2025-08-18T18:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4906161277847-RH-Linha-Protheus-GPE-Por-que-na-DIRF-%C3%A9-gerado-o-CNPJ-da-filial-do-funcion%C3%A1rio-para-o-plano-de-sa%C3%BAde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34270152833559) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que na DIRF é gerado o CNPJ da filial do funcionário para o plano de saúde ao invés do CNPJ do fornecedor?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Geralmente isso ocorre quando o desconto do plano de saúde é lançado diretamente na folha do funcionário, sem usar as rotinas padrões de cálculo e integração de plano de saúde, dessa forma, o sistema não tem como validar o fornecedor do plano de saúde e carrega o CNPJ da filial do funcionário.

Neste caso, é necessário realizar manutenção em Informações Complementares para informar o CNPJ do fornecedor de plano de saúde e demais informações que não são carregadas de forma automática quando o plano de saúde é lançado manualmente.

Para esse ajuste, siga a documentação [RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)

**Saiba mais**  
[RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde, coparticipação e reembolso para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972)
