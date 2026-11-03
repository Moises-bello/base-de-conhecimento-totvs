---
content_hash: fad990cdbfcfab061436390b88e533ddd27b300fde940122e8916e0a98da010a
fetched_at: '2026-06-29T00:10:04.807674+00:00'
page_id: '452719256'
product: rm
source: tdn-rm
title: Código de cálculo 331 – Férias vencidas sem Aviso Prévio Indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719256
version: 3
---

Evento Base de cálculo do tipo Valor e sem incidência.  
Este é calculado e lançado automaticamente na rescisão para atender exclusivamente o campo 66 do TRCT, conforme anexo I da portaria 1. 621 do Ministério do Trabalho do TRCT.   
Sendo necessário associar uma rubrica no evento que contém este código de cálculo.  
O valor deste código de cálculo é exatamente o valor correspondente os avos das Férias Vencidas e médias sem considerar a projeção dos dias do aviso indenizado. Não é exatamente o valor do evento com código de cálculo '24-Férias Indenizadas'.  
   
**Exemplo I:**  
Parâmetro 'Soma avos ref. aviso após o cálculo' desmarcado  
SEM AVISO PREVIO INDENIZADO  
Período aquisitivo em: 18.01.2011 a 17.01.2012  
Demissão: 02.01.2012  
Férias Indenizadas: 0 avo (18.01.2011 a 02.01.2012 = Não possui férias vencidas. Vencimento = 17/01/2012)  
Férias Proporcionais: 12/12 avos (18.01.2011 a 02.01.2012 = 30 dias)  
**Férias Proporcionais sem Aviso Prévio Indenizado: 12/12 avos**  
   
**Exemplo II:**  
Parâmetro 'Soma avos ref. aviso após o cálculo' desmarcado  
COM AVISO PRÉVIO INDENIZADO: 03.01.2012 a 01.02.2012 (30 dias)  
Período aquisitivo em: 18.01.2011 a 17.01.2012  
Demissão: 02.01.2012  
Férias Indenizadas: 12/12 avos (18.01.2011 a 17.01.2012)  
Férias Proporcionais: 1/12 avos (18.01.2012 a 01.02.2012 = 15 dias)  
**Férias Vencidas sem Aviso Prévio Indenizado: 0 avo**  
   
**Atenção I:**  
Observa-se que no **Exemplo I** SEM AVISO PRÉVIO INDENIZADO, o funcionário adquiriu 12/12 avos de férias proporcionais (cc25), e no **Exemplo II** na mesma situação porém **COM AVISO PRÉVIO INDENIZADO** o recebimento dos 12/12 avos de férias passam a ser lançados no evento de Férias Indenizadas (cc24), isso ocorreu devido o fim do aviso prévio ser posterior ao vencimento das férias.   
Mesmo existindo o evento Férias Indenizadas (cc24) o sistema não lançou o evento Férias Vencidas sem Aviso Prévio Indenizado (cc331), isso porque sem a projeção do aviso prévio indenizado, o funcionário teria direito as férias proporcionais, ou seja, o valor calculando no **Exemplo I.**  
   
**Atenção II:**  
Este evento é demonstrado sempre em dias .  
   
**Atenção III:**  
Para que o sistema lance o valor da diferença deste código de cálculo na rescisão complementar, é necessário informar um evento no campo 'Evento de Diferença de Salário'.

Dica:

.
