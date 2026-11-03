---
article_id: 360017975092
category: RH - Rescisão
content_hash: f11f2e6ef7111fd66b46e0f01764d1615ccd40c3ed8a37a8e7f91c1acc2b14d2
fetched_at: '2026-06-28T22:43:49.724355+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de médias de férias sobre aviso prévio
  (ID 0252) na rescisão quando o funcionário não tem média de férias proporcionais
type: support-article
updated_at: '2025-07-14T19:06:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017975092-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-m%C3%A9dias-de-f%C3%A9rias-sobre-aviso-pr%C3%A9vio-ID-0252-na-rescis%C3%A3o-quando-o-funcion%C3%A1rio-n%C3%A3o-tem-m%C3%A9dia-de-f%C3%A9rias-proporcionais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33462348803479) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Gestão de Pessoal, o Sistema gera médias de férias sobre aviso prévio (ID 0252) na rescisão a partir do valor das médias de férias proporcionais, mas se não há médias de férias proporcionais, o sistema considera as médias de Aviso Prévio para compor as médias de férias sobre aviso.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da Versão 12.1.17.  
  
**Causa**Por **padrão**, o sistema usa as **médias de férias proporcionais para realizar o pagamento das médias de férias sobre aviso**. Contudo, se tais médias são 0, utilizará as médias sobre aviso.  
  
**Solução**Criação do mnemônico **P\_LUSAMDAV** para verificar se deseja considerar as médias do aviso prévio indenizado para realizar o pagamento das médias de férias sobre aviso, caso as médias de férias proporcionais sejam 0.  
  
Mnemônico **P\_LUSAMDAV** (usa média do aviso prévio para calcular media férias sobre aviso). Conteúdo pode ser **.T.** ou **.F.**Caso esse mnemônico esteja configurado com **.T.**, o sistema **continuará** utilizando as **médias de aviso prévio** para pagamento da média de férias sobre aviso prévio, mas somente se as médias de férias proporcionais forem 0.

Caso o mnemônico esteja configurado com **.F.**, o sistema **não utilizará** as **médias de aviso prévio** para o pagamento das médias de férias sobre aviso. Nesse caso, não será gerada a verba de id0252, visto que as médias de férias proporcionais é 0.  
  
  
**Saiba mais:**

[RH- Linha Protheus - GPE - Cálculo de médias 13º sobre aviso e médias férias sobre aviso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026383053-MP-GPE-C%C3%A1lculo-de-m%C3%A9dias-13%C2%BA-sobre-aviso-e-m%C3%A9dias-f%C3%A9rias-sobre-aviso)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
