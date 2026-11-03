---
article_id: 11333824146327
category: esocial - Processos
content_hash: b6bb7b4d60ef185ce3acd27d38cd8b69794c8038a454be00ad2ea5e013edac83
fetched_at: '2026-06-28T22:47:08.402713+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware - Certificado Digital A3 '
type: support-article
updated_at: '2025-01-30T12:29:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11333824146327-RH-RM-FOP-eSocial-Middleware-Certificado-Digital-A3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como configurar Certificado Digital A3 no Middleware?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O Certificado A3 são armazenados em dispositivo portátil inviolável do tipo*smart card*ou*token*, que possuem um chip com capacidade de realizar a assinatura digital.

* Por premissa o certificado A3 deve ser instalado e configurado junto a máquina física onde encontra-se instalado o TSS.
* O certificado A3 é um *hardware* que geralmente tem como porta de comunicação um *USB*, desta forma exige uma máquina física para ser instalado e configurado.
* Por motivo de segurança, o A3 deve ficar sobe posse da empresa e não deve ser passado à terceiros.

 Paraconfigurar o Certificado Digital A3, siga os passos abaixo:

1. Acesse o menu **Folha de Pagamento | Configurações| Parametrizador | eSocial**;
2. Avance até a etapa **Integração com Middleware**;
3. Na aba **Certificado Digital**, deverá selecionar tipo do Certificado **A3 - *HSM (Hardware Security Module*)** para que os campos para cadastro das informações sejam habilitados;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11542784333847)

         4 . Após preencher, clique no botão **Atualizar Certificado TSS** e avance até a conclusão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11547395235351)

**Observação:**  
Nos casos em que o TSS esteja instalado em ambiente **Cloud** ou **Servidores Virtuais** não é possivel configurar o **certificado A3**. Para mais informações acesse:    
     - [É possível configurar certificado A3, em ambiente Cloud e Servidores Virtuais?](https://tdn.totvs.com/pages/releaseview.action?pageId=329023719)

**Saiba mais**  
Para mais informações acesse:

* [Middleware - Certificado Digital](https://tdn.totvs.com/display/public/LRM/Middleware+-+Certificado+Digital)
* [Integração com Middleware](https://tdn.totvs.com/pages/releaseview.action?pageId=566479573)
