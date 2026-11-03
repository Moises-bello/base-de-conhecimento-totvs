---
article_id: 4413652354327
category: RH - Definições de Cálculo
content_hash: ba2478eee8258fb3d65c375b3bd8507b2d9a0bbf2c20afe15241ce5381b4c1be
fetched_at: '2026-06-28T22:43:22.551254+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Tratamento para valores negativos de periculosidade
  sobre verbas, criação do identificador 1869
type: support-article
updated_at: '2025-06-16T19:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413652354327-RH-Linha-Protheus-GPE-Tratamento-para-valores-negativos-de-periculosidade-sobre-verbas-cria%C3%A7%C3%A3o-do-identificador-1869
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32852438650135) Tempo aproximado para leitura: 00:01:30 min****Dúvida**Tratamento para valores negativos de periculosidade sobre verbas

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Situação:**Quando o funcionário recebe periculosidade que é configurada sobre salário mínimo + verbas e houve faltas no período, a periculosidade reajustada no dissídio acaba ficando menor que o valor do recibo devido à valorização das faltas, o que gera uma diferença negativa, que apesar de correta, não é gerada e declarada ao eSocial no evento S-1200.

**Solução:  
Ajuste no cálculo do dissídio quando funcionário recebe periculosidade com base sobre salário mínimo + verbas e houve falta,** situação em que a periculosidade calculada no dissídio será menor devido reajuste da falta, para que o sistema efetue desconto da diferença da insalubridade na verba vinculada ao ID 1869 ao invés de gerar diferença com valor negativo na verba de provento da periculosidade, uma vez que não ocorre geração e declaração de valor negativo ao eSocial no evento S-1200.

**-> Observação**A verba cadastrada para o **ID 1869** deve ser um **desconto**, pois refere-se a um valor que será descontado do funcionário. Como **sugestão**, copiar as incidências e demais **configurações da verba de ID 1281** (periculosidade sobre verbas).  
  
**Saiba mais:**  
[RH - Linha Protheus - GPE - Criação e cadastro dos Ids 1562, 1722 e 1723](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026461314-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-e-cadastro-dos-Ids-1562-1722-e-1723)  
[RH - Linha Protheus - GPE - Como cadastrar o ID de Cálculo 1732 - Diferença 13° Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042331013-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-de-C%C3%A1lculo-1732-Diferen%C3%A7a-13-Maternidade)  
[RH - Linha Protheus - GPE - Identificadores de cálculo 0671, 0672 e 0673](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056019014-RH-Linha-Protheus-GPE-Identificadores-de-c%C3%A1lculo-0671-0672-e-0673)  
[Documentação técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=631632586)
