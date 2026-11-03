---
article_id: 360026214172
category: Originação de Grãos (OG)
content_hash: a17b9b9672ba4ca3bb059f26010af00c59d7ec8f19b15eb881f3cbe03e9e7785
fetched_at: '2026-06-28T22:45:38.863436+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Contratos sem saldo são exibidos nos romaneios
type: support-article
updated_at: '2025-06-18T19:56:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026214172-Agro-Linha-Protheus-AGR-Contratos-sem-saldo-s%C3%A3o-exibidos-nos-romaneios
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20297592758935)*** Tempo aproximado para leitura: **00:00:55 min****Ocorrência**Nas rotinas de **Romaneio com Pesagem - OGA250** ou **Romaneio sem Pesagem -** **OGA251** são exibidos os contratos que não possuem saldo. Como proceder para que não sejam exibidos os contratos sem saldo.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Isso ocorre porque o parâmetro das outras ações na consulta personalizada do contrato está marcado para aparecer contratos sem saldo.  
  
**Solução**Para que sejam exibidos apenas os contratos que possuem saldo é necessário que por meio da rotina de Romaneio com ou sem Pesagem essa opção seja manipulada:  
1. É necessário pesquisar pelos contratos;

![CONT.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7569763028887)

2. Em Outras Ações clicar em Parâmetros;

![CONT1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7569748193687)

3. Selecionar **Sim** ou **Não**, para que sejam ou não exibidos os contratos **Sem Saldo**.

![CONT2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7569757129495)
