---
article_id: 40886548534423
category: TAF - REINF
content_hash: 99bfcca5d3513d27e4182901f5a9dd0a961e7c3fd1b163b63d7bb668ccd93790
fetched_at: '2026-06-28T22:41:33.353071+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1476
type: support-article
updated_at: '2026-06-01T21:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40886548534423-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1476
---

**Ocorrência**  
  Ao transmitir o evento R-4010 ou R-4020 ocorre a rejeição abaixo.

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40886548521239)  
  
**Ambiente**  
  Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Causa**  
  Este incidente ocorre devido à Receita Federal do Brasil (RFB) identificar a ausência do evento R-1050, relacionado ao cadastro de FCI/SCP para a operação realizada.

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40886626595863)  
**Solução**  
  Para solucionar esse erro é necessário que seja realizada a transmissão do evento R-1050 vinculado aos dados do participante utilizado no Pagamento.

***Exemplo de R-1050 (cadastro de FCI/SCP) com vínculo de participante.***

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40887225726359)

  Feito o vínculo no cadastro de FCI/SCP, deve ser realizada ***a apuração e transmissão do R-1050 no painel REINF.***

  Importante: Deve ser utilizado o mesmo participante do cadastro de FCI/SCP (R-1050) no pagamento dentro da rotina de Pagamentos/Recibos (TAFA535).

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40887650739607)

  Após ter o evento R-1050 autorizado, exclua a apuração (R4010 ou R-4020) inconsistente conforme documentação abaixo.

* [Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente)

Feita exclusão, apure e transmita novamente os eventos do R-4010 e R-4020.
