---
article_id: 360052995593
category: RH - FGTS / SEFIP
content_hash: 7913dd4c7b4853ec497781c419903f84ababee6c8d7852e452a0e3a84bb35cb1
fetched_at: '2026-06-28T22:43:41.430863+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Na geração da SEFIP não informa código de movimentação
  de retorno do afastamento temporário gerando inconsistência 320640 no validador
type: support-article
updated_at: '2025-08-14T18:28:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052995593-RH-Linha-Protheus-GPE-Na-gera%C3%A7%C3%A3o-da-SEFIP-n%C3%A3o-informa-c%C3%B3digo-de-movimenta%C3%A7%C3%A3o-de-retorno-do-afastamento-tempor%C3%A1rio-gerando-inconsist%C3%AAncia-320640-no-validador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34187279617559) Tempo aproximado para leitura: 00:01:30 min**  
**Dúvida**Na geração da SEFIP gera inconsistência 320640 no validador  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**

Para que o sistema entenda que o afastamento deve ter um código de movimentação no retorno é necessário que realize a seguinte configuração:

1 – Na tabela S046 preencha o campo código de retorno para os códigos de movimentos que possuem código de retorno.

![](https://tdn.totvs.com/download/attachments/351391115/image2018-4-11_11-20-36.png?version=1&modificationDate=1523456620000&api=v2)

2 – Em tipos de ausências acesse o cadastro da ausência cadastrada e informe o código de movimento que foi cadastrado na tabela S046.

![](https://tdn.totvs.com/download/attachments/351391115/image2018-4-11_11-22-9.png?version=1&modificationDate=1523456619000&api=v2)

3 – Calcule a folha para o funcionário e gere a SEFIP, desta forma o sistema irá levar o código de retorno para o txt e não haverá inconsistência 320640 no validador.

**Saiba mais:**

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
