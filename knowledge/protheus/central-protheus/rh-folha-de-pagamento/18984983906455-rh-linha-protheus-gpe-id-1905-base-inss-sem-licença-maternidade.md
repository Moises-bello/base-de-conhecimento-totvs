---
article_id: 18984983906455
category: RH - Folha de Pagamento
content_hash: ffb6b80a47409c3e161816cbb6a0e381487e520dd6f39ba272af1e59fd9c9efd
fetched_at: '2026-06-28T22:44:14.985229+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - ID 1905 - Base INSS sem Licença Maternidade
type: support-article
updated_at: '2024-09-05T18:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18984983906455-RH-Linha-Protheus-GPE-ID-1905-Base-INSS-sem-Licen%C3%A7a-Maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18984974307607) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a finalidade da criação do ID 1905 - Base INSS sem valor da Licença Maternidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.33.  
  
**Solução**Ao calcular a Folha, o sistema irá gerar a verba criada (ID 1905) com o valor da diferença entre o Salário de Contribuição (Base INSS ID 0013 + ID 0014) e da verba de Licença Maternidade (ID 0040) e outras verbas com Cd. Inc. CP (RV\_INCCP) = 21 ou 22 (Base Calculo da Contr. Previd. para Sal. Maternidade)

O novo ID deve ser cadastrado como tipo de verba = 3 - Base Provento

**Exemplo:**

Verba 703 (ID 0013) 3.800,00 - Verba 121 (ID 0040) 2.406,67 = **1.393,33 Verba 870 (ID 1905)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18985007163799)

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
