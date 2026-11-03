---
article_id: 1500005244601
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9e35358006776b7e862741ddec53d71299eaab9a8ead8af14ef2a880bd4b12b9
fetched_at: '2026-06-28T22:39:56.380199+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Como gerar
  o rastro (dbtrace) da rotina FISA022?
type: support-article
updated_at: '2025-07-14T21:26:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005244601-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Como-gerar-o-rastro-dbtrace-da-rotina-FISA022
---

**Dúvida**Como gerar o rastro contendo todas as queries realizadas no banco de dados através da rotina **FISA022**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para gerar o dbtrace (rastro) da rotina **FISA022**, deverão ser seguidos o passo-a-passo abaixo:**1.** Primeiramente deverá acessar o DBMonitor do ambiente:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007096422/mceclip0.png)  
  
  
**2**. Feito isso, deverá ir na aba Usuários, localizar o usuário que está acessando a rotina **FISA022** e seleciona-lo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007251681/mceclip1.png)  
  
  
**3.** Após isso, antes de clicar em rastrear, já deixar o processo que quer observar pronto (exemplo: *Transmissão, Monitoramento, Cancelamento, outros),* com isso evitando não gerar logs desnecessários, pois cada processo realizado dentro da rotina serão registrados em log.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007251721/mceclip2.png)  
  
  
**4.**  Uma vez preparado, basta apenas clicar em Rastrear e transmitir a nota (exemplo utilizado).  
  
**5.** Após isso poderá observar que serão gerados todas as queries disparadas pelo DBAccess no banco de dados.  
 **6.** Terminado o processo, poderá clicar em Salvar para guardar o trace realizado.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007097222/mceclip4.png)
