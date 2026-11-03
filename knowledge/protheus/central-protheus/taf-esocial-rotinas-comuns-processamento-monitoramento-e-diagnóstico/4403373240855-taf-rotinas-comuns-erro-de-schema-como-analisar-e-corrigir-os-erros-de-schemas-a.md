---
article_id: 4403373240855
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 4af1a4e1fa84c834ce74a847a69258e8f3bc94fd563dfe835f61cd7e092185b5
fetched_at: '2026-06-28T22:45:21.109174+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: TAF - Rotinas Comuns - Erro de Schema- Como analisar e corrigir os erros de
  Schemas apresentados pelo sistema
type: support-article
updated_at: '2022-08-24T14:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403373240855-TAF-Rotinas-Comuns-Erro-de-Schema-Como-analisar-e-corrigir-os-erros-de-Schemas-apresentados-pelo-sistema
---

**Dúvida**Como analisar e corrigir os erros de Schemas apresentados pelo sistema, ao tentar transmitir um evento no TAF.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Monitoramento - Todas as versões  
  
**Solução**

Os erros de Schemas geralmente são causados devido ao preenchimento incorreto dos campos. Sempre serão apresentados indicando o campo e o motivo da falha, segue exemplos:

**Ex.1) S-2200**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403371153047/mceclip0.png)**

1. Verifique qual o campo está ocorrendo a inconsistência, no nosso exemplo, está no campo *"fonePrinc"* do evento de admissão;

2. Se tiver dúvidas sobre o campo e/ou preenchimento do mesmo, orientamos consultar o leiaute do e-social, pode ser realizado o download ou consulta da documentação técnica, pelo link: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>

3. Após informa o campo que apresenta erro, a mensagem informa o que identificou no campo, neste nosso exemplo ele informa que foi preenchido duas ('2') posições e o esperado são oito ('8') posições, veja:

*\*\*The value has a length of **'2**', this underruns the allowed minimum length of **'8'**.*

*4.*Seguindo a leitura do erro de Schema, o mesmo informa o valor encontrado no campo *"fonePrinc",* neste caso, "11". Entendemos que foi somente inserido o DDD no campo, e não foi preenchido o numero do telefone.

**Ex.2) S-1000**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403372031255/mceclip1.png)

1. Neste exemplo, o campo que apresenta erro, é o campo *"indEtt",* do evento S-1000.

2. A mensagem informa que não é esperado que o campo esteja vazio (sem preenchimento);

*\*\*The value **' ' is not accepted** by the pattern '[N/S].*

3. No caso a empresa não é Entidade Educativa, porém, mesmo assim é solicitado o preenchimento do campo, pois as demais informações **relacionadas** foram preenchidas, veja:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403375044375/mceclip2.png)

4. Foi selecionada a opção "0", porém, como a empresa não é Entidade Educativa, deve-se deixar as duas opções em branco.

As mesmas análises devem ser realizadas para os demais eventos, pois identificando o local e motivo do erro, a correção torna-se mais fácil.
