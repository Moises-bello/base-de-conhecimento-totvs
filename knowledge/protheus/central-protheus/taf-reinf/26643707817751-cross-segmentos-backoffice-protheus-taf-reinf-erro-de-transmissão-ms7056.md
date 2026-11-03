---
article_id: 26643707817751
category: TAF - REINF
content_hash: b117752e1288b5aae9209a68271cb33002e805236a64aa911de35ba2349de20d
fetched_at: '2026-06-28T22:41:33.344913+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro de transmissão MS7056
type: support-article
updated_at: '2024-09-26T16:08:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26643707817751-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-transmiss%C3%A3o-MS7056
---

**Ocorrência**

Ao realizar a transmissão de um evento ocorre a seguinte rejeição:

Código:  
MS7056  
Descrição  
Prezado contribuinte, a partir de 22/07/2024 a transmissão dos eventos R-1000, R-1070, R-3010 e dos eventos da série R-2000 não pode ser efetuada no modo com processamento síncrono. A partir dessa data, todos os eventos deverão ser transmitidos exclusivamente usando a API de recepção com processamento assíncrono, conforme divulgado no portal SPED em http://sped.rfb.gov.br/pagina/show/7400.

**Ambiente**

TAF - SIGATAF - A partir da versão 12.1.33

**Causa**

  O incidente ocorre por falta de atualização do TSS ou versão do leiaute utilizada.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Atualize o RPO do seu TSS.

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

2.  Realize a correção do parâmetro MV\_TAFVLRE : 2\_01\_02.

[RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - Configurador - Como acessar os parâmetros do sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-Configurador-Como-acessar-os-par%C3%A2metros-do-sistema)

3. Reinicie o seu ambiente exclua a apuração inconsistente, apure e transmita novamente o evento.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente)
