---
article_id: 360023371471
category: ADVPL - Classe e Função
content_hash: bfd5b8c3d11048a5e208b0099fb74c78664fcbc321deeeb7dbe28ff9fb52fcec
fetched_at: '2026-06-28T22:40:18.197158+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilizar a MSGALERT()
  via gatilho ou fazer com que através da uma ação no campo dispare uma tela informativa
type: support-article
updated_at: '2022-08-01T12:11:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023371471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utilizar-a-MSGALERT-via-gatilho-ou-fazer-com-que-atrav%C3%A9s-da-uma-a%C3%A7%C3%A3o-no-campo-dispare-uma-tela-informativa
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Na versão 11.8 estávamos utilizando a função MSGALERT() via gatilho, depois que a versão mudou para 12.1.17 essa função não funciona mais via gatilho.   
Aliás, nenhuma função mais parece funcionar via gatilho na nova versão.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Com relação a necessidade o melhor jeito de ser feito o processo, seria criando uma função de usuário que verifique o código digitado onde será verificado o status do cliente e retornado uma tela informativa através do ALERT() ou MSGALERT(), e essa função pode ser validada no campo do código digitado através de uma Validação do Usuário dessa forma terá o retorno desejado.
