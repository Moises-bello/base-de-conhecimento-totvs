---
content_hash: 358108a3485d539653a26cf8e14ec6d9d64d59a79ec3750ae43669452ce8c077
fetched_at: '2026-06-29T00:10:00.484009+00:00'
page_id: '452718573'
product: rm
source: tdn-rm
title: Código de calculo 329 - Férias Indenizadas Sobre Aviso Prévio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718573
version: 3
---

Evento Base de cálculo do tipo Valor e sem incidência.  
Este é calculado e lançado automaticamente na rescisão para atender exclusivamente o campo 71 do TRCT, conforme anexo I da portaria 1. 621 do Ministério do Trabalho do TRCT.   
Sendo necessário associar uma rubrica no evento que contém este código de cálculo.  
O valor deste código de cálculo é exatamente o valor correspondente aos avos que foram acrescentadas nos eventos Férias Indenizadas (cc24), Férias Proporcionais (cc25) e médias devido ao aviso indenizado.  
   
**Exemplo I:**  
Parâmetro 'Soma avos ref. aviso após o cálculo' desmarcado  
Período aquisitivo em: 18.01.2011 a 17.01.2012  
Demissão: 01.01.2012  
Aviso Prévio Indenizado: 02.01.2012 a 31.01.2012 (30 dias)  
Férias Indenizadas: 12/12 avos (18.01.2011 a 17.01.2012)  
Férias Proporcionais: 0 avo (18.01.2012 a 31.01.2012 = 14 dias)  
**Férias sobre Aviso Prévio Indenizado: Este evento não é lançado devido não ter adquirido avos com o Aviso Prévio Indenizado**  
   
**Exemplo II:**  
Parâmetro 'Soma avos ref. aviso após o cálculo' desmarcado  
Período aquisitivo em: 18.01.2011 a 17.01.2012  
Demissão: 02.01.2012  
Aviso Prévio Indenizado: 03.01.2012 a 01.02.2012 (30 dias)  
Férias Indenizadas: 12/12 avos (18.01.2011 a 17.01.2012)  
Férias Proporcionais: 1/12 avos (18.01.2012 a 01.02.2012 = 15 dias)  
**Férias sobre Aviso Prévio Indenizado: 1/12 avos (18.01.2012 a 01.02.2012 = 15 dias adquirido devido ao Aviso Prévio Indenizado)**  
   
**Atenção I:**  
Este evento é demonstrado sempre em avos, nunca em dias.  
   
**Atenção II:**  
Para que o sistema lance o valor da diferença deste código de cálculo na rescisão complementar, é necessário informar um evento no campo 'Evento de Diferença de Salário'.

Dica:

.
