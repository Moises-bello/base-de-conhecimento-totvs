---
article_id: 8188819482135
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 20dee1993bf4bf361ed68c352b3e45c65c15657f15c8b095a1f65658a428051e
fetched_at: '2026-06-28T22:39:57.400659+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element
  ''serierps'':" is not a valid, na transmissão de rps normal '
type: support-article
updated_at: '2022-08-15T18:36:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8188819482135-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-serierps-is-not-a-valid-na-transmiss%C3%A3o-de-rps-normal
---

**Dúvida**Ao transmitir um rps ocorre o erro: *Element 'serierps': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'*.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**O Erro "*Element 'serierps': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'* " ocorre na transmissão da nota, quando o documento de saída é gerado sem série ou com série em branco. O documento de saída é gerado com a espécie correta RPS, mas no momento da transmissão ocorre a mensagem de erro.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8188413886231/mceclip0.png)

No schema do xml a série do rps é obrigatória, seja ela numérica ou alfanumérica, e a falta dela causa esta mensagem.  
  
Para correção, faça o correto cadastro da série e número na tabela 01 da SX5.
