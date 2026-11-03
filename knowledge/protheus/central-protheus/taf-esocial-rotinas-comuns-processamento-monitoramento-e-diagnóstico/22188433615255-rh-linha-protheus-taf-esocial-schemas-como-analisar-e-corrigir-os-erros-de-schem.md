---
article_id: 22188433615255
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 3ca00dea0b35414c1411db84d80b85e8b0b9c05326263d5249655e918a43672b
fetched_at: '2026-06-28T22:45:21.065234+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Schemas - Como analisar e corrigir os
  erros de Schemas apresentados pelo sistema
type: support-article
updated_at: '2026-06-26T12:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22188433615255-RH-Linha-Protheus-TAF-eSocial-Schemas-Como-analisar-e-corrigir-os-erros-de-Schemas-apresentados-pelo-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22188475465367) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como analisar e corrigir os erros de Schemas apresentados pelo sistema, ao tentar transmitir um evento no TAF.

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**

Os erros de Schemas geralmente são causados devido ao preenchimento incorreto dos campos.

Sempre serão apresentados indicando o campo e o motivo da falha, segue exemplos:

**Ex.1) S-2200**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22188433595287)**

1. Verifique qual o campo está ocorrendo a inconsistência, no nosso exemplo, está no campo "fonePrinc" do evento de admissão;

2. Se tiver dúvidas sobre o campo e/ou preenchimento do mesmo, orientamos consultar o leiaute do e-social, pode ser realizado o download ou consulta da documentação técnica, pelo link: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>

3. Após informa o campo que apresenta erro, a mensagem informa o que identificou no campo, neste nosso exemplo ele informa que foi preenchido duas ('2') posições e o esperado são oito ('8') posições, veja:

\*\*The value has a length of '2', this underruns the allowed minimum length of '8'.

4. Seguindo a leitura do erro de Schema, o mesmo informa o valor encontrado no campo "fonePrinc", neste caso, "11". Entendemos que foi somente inserido o DDD no campo, e não foi preenchido o numero do telefone.

**Ex.2) S-1000**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22188433596183)**

1. Neste exemplo, o campo que apresenta erro, é o campo *"indEtt",* do evento S-1000.

2. A mensagem informa que não é esperado que o campo esteja vazio (sem preenchimento);

*\*\*The value **' ' is not accepted** by the pattern '[N/S].*

3. No caso a empresa não é Entidade Educativa, porém, mesmo assim é solicitado o preenchimento do campo, pois as demais informações **relacionadas** foram preenchidas, veja:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22188433597719)

4. Foi selecionada a opção "0", porém, como a empresa não é Entidade Educativa, deve-se deixar as duas opções em branco.

As mesmas análises devem ser realizadas para os demais eventos, pois identificando o local e motivo do erro, a correção torna-se mais fácil.
