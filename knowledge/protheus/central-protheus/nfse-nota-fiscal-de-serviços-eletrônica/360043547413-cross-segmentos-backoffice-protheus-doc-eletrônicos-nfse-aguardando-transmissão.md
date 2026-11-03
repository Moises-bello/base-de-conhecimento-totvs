---
article_id: 360043547413
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 86c30a743ed288b8421221f341fdc98f11b9209ebc7f9e6e73047aaea870d7aa
fetched_at: '2026-06-28T22:39:56.288710+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Aguardando
  Transmissão do Lote (STATUS = 2)
type: support-article
updated_at: '2025-06-10T18:22:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043547413-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Aguardando-Transmiss%C3%A3o-do-Lote-STATUS-2
---

**Dúvida**Qual procedimento realizar quando a nota não sai do status **2 - Aguardando Transmissão do Lote?**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse status geralmente ocorre por dois problemas principais:  
  
**1. Certificado Digital (vencido por exemplo);**  
Nesse caso a orientação é que refaça o Wizard.cfg por completo, importando novamente o Certificado Digital válido e após isso apenas monitorar as notas.  
  
**2. Erros de POST com as URL's da prefeitura (bloqueio de rede: proxy, firewall, antivírus ou a URL estar fora do ar).**Deverá verificar no console.log do TSS e caso tenha algum erro de POST, realizar um teste tentando acessa-la através do navegador aonde o TSS está instalado. (Exemplo: Servidor)  
Lembrando que a URL deverá abrir normalmente, o qual indica que não à principio não há um bloqueio.  
  
Após esses dois passos verificados, monitore a RPS em questão e verifique se o status da nota é alterado.
