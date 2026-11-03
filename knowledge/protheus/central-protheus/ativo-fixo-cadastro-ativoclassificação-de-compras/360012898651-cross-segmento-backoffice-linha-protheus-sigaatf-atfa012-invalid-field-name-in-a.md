---
article_id: 360012898651
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 04ec6e3b6c9e9ac1734fad77b0b85111417a4bd0e6ce4252b2ad45c09f6c9fb8
fetched_at: '2026-06-28T22:41:48.291062+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF  - ATFA012 invalid field
  name in Alias SN1->N1_TPCTRAT on ATF012WHEN
type: support-article
updated_at: '2023-11-30T15:12:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012898651-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-invalid-field-name-in-Alias-SN1-N1-TPCTRAT-on-ATF012WHEN
---

**Ocorrência**Ao alterar um bem do ativo imobilizado, sistema apresenta o error log:  
invalid field name in Alias SN1->N1\_TPCTRAT on ATF012WHEN  
  
**Ambiente**Protheus – Ativo Fixo – A partir da versão 12.1.17  
  
**Causa**   
Esse incidente ocorre, pois a configuração dos campos na SX3 está incorreta.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o campo existe na base e se esta na posição 68.

![](https://totvssuporte.zendesk.com/attachments/token/yUKF6o7j3snIzjklsYAcOAPxT/?name=inline1622716003.png)

2.  Se o tópico 1 estive ok, verifique se a SX3 esta conforme padrão do sistema.

![](https://totvssuporte.zendesk.com/attachments/token/0B71naJ9BRUUyNnMuO7VqPxs1/?name=inline2145094780.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/6On2NqvX6jh1Hpcy2ymWgStod/?name=inline1289632979.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/b8dN0duITyaEGratWN2s8uIZY/?name=inline194089690.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/TgCWRukw0u3BXaWd5MYZpalEG/?name=inline1727714086.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/lyXptrip9SpD8i1VmkQU3ef98/?name=inline888432256.png)

Recomendamos que seja realizado a atualização do ambiente com a execução do UPDDISTR, para evitar erros em outras rotinas e processos.

Procedimento deve ser feito por um analista de confiança da empresa.
