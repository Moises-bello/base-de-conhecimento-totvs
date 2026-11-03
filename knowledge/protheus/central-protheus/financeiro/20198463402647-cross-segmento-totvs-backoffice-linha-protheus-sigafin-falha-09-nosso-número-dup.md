---
article_id: 20198463402647
category: Financeiro
content_hash: 798a2e3e7f7aaa93a297dc9ee03488f5506fb1f1aed1c3646f7af04d27bc516e
fetched_at: '2026-06-28T22:38:01.155902+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAFIN - FALHA: 09 - Nosso
  Número Duplicado'
type: support-article
updated_at: '2023-12-30T02:19:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20198463402647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FALHA-09-Nosso-N%C3%BAmero-Duplicado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20198463358487) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao receber retorno do Banco aparece o status: 09 - Nosso Número Duplicado  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINANCEIRO - Todas as versões  
  
**Solução**

Quando a empresa realiza emissão de boleto para o cliente, é necessário enviar o nosso número em cada título enviado ao banco.

O campo referente ao nosso número (E1\_NUMBCO) é preenchido conforme a configuração dos campos faixa início (EE\_FAXINI) , faixa fim (EE\_FAXFIM) e faixa atual (EE\_FAXATU) no cadastro de Parâmetros Bancos (FINA130).

No layout de remessa é necessário utilizar a função NOSSONUM() para que seja gerado o sequencial a partir do conteúdo do campo EE\_FAXATU. O nosso número será carregado quando o arquivo de remessa for gerado com a devida configuração.

Para correção será necessário tirar o titulo do borderô, excluir o ultimo titulo com o mesmo numero, atualizar a faixa atual para um sequencial posterior e após reenviar.
