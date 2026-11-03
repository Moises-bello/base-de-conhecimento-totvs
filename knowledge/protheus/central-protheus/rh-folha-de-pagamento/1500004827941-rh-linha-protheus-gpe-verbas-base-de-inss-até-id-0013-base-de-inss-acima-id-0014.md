---
article_id: 1500004827941
category: RH - Folha de Pagamento
content_hash: 6f578b0dcd9f2b52656baaf3069ab25a9aec79e83e8123b7afeed3edbe1d8fa4
fetched_at: '2026-06-28T22:44:16.428821+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas Base de INSS até (ID 0013), Base de INSS
  acima (ID 0014) e Base de IRRF (ID 0015) não são calculadas na folha de pagamento
type: support-article
updated_at: '2024-09-13T18:53:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004827941-RH-Linha-Protheus-GPE-Verbas-Base-de-INSS-at%C3%A9-ID-0013-Base-de-INSS-acima-ID-0014-e-Base-de-IRRF-ID-0015-n%C3%A3o-s%C3%A3o-calculadas-na-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26357987499927)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao calcular a folha de pagamento as verbas Base de INSS até ou Salário Contribuição até Limite (ID 0013), Base de INSS acima ou Salário de Contribuição acime Limite (ID 0014) e Base de IRRF (ID 0015) não são apresentadas.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - A partir da versão 11.80  
  
**Causa**Esse incidente ocorre pois as verbas de INSS (ID 0064) e IRRF (ID 0066) foram informadas manualmente no cálculo do funcionário  
  
**Solução**O sistema calcula automaticamente estes valores validando as verbas e a tabela de INSS (S001) cadastrada. Se por algum motivo estas verbas forem informadas manualmente, as verbas de base também deverão ser informadas.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
