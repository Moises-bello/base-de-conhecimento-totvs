---
content_hash: 4f6dbfd4a1ef9d251eddc3c6b76b8955460236d6ee809e1d5e778f14f8abd2b2
fetched_at: '2026-06-29T00:10:04.799304+00:00'
page_id: '452719254'
product: rm
source: tdn-rm
title: Código de calculo 330 – Férias Proporcionais Sem Aviso Prévio Indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719254
version: 4
---

Evento Base de cálculo do tipo Valor e sem incidência.  
Este é calculado e lançado automaticamente na rescisão para atender exclusivamente o campo 65 do TRCT, conforme anexo I da portaria 1. 621 do Ministério do Trabalho do TRCT.   
Sendo necessário associar uma rubrica no evento que contém este código de cálculo.  
O valor deste código de cálculo é exatamente o valor correspondente aos avos das Férias Proporcionais e médias sem considerar a projeção dos dias do aviso prévio indenizado. Não é valor do código de cálculo '25-Férias Proporcionais' lançado na rescisão.  
   
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
**Férias Proporcionais sem Aviso Prévio Indenizado: 12/12 avos.**  
   
**Atenção I:**  
Observa-se que no **Exemplo I** SEM AVISO PRÉVIO INDENIZADO, o funcionário adquiriu 12/12 avos de férias proporcionais (cc25), e no **Exemplo II** na mesma situação porém **COM AVISO PRÉVIO INDENIZADO** o recebimento dos 12/12 avos de férias passam a ser lançados no evento de Férias Indenizadas (cc24), isso ocorreu devido o fim do aviso prévio ser posterior ao vencimento das férias.   
Com tudo, o valor lançado no evento Férias Proporcionais sem Aviso Prévio (cc330), é exatamente o valor do evento com cc25-Férias Proporcionais desconsiderando o recebimento do Aviso Prévio Indenizado, ou seja não é o valor do cc25 do exemplo II é o valor calculando no **Exemplo I** sem considerar o aviso prévio indenizado  
   
**Atenção II:**  
Este evento é demonstrado sempre em avos, nunca em dias.  
   
**Atenção III:**  
Para que o sistema lance o valor da diferença deste código de cálculo na rescisão complementar, é necessário informar um evento no campo 'Evento de Diferença de Salário'.  
 

Dica:

.
