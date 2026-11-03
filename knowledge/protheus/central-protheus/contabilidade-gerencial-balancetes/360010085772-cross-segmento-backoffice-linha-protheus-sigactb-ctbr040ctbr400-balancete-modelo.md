---
article_id: 360010085772
category: Contabilidade Gerencial - Balancetes
content_hash: fd868083b057c7a8bd0244c1cb374d143c6b26232aa0410527f46594ffe4083c
fetched_at: '2026-06-28T22:41:04.144187+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR040/CTBR400  Balancete
  Modelo 1 ou Razão Contábil com saldo incorreto.
type: support-article
updated_at: '2024-03-01T20:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010085772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-CTBR400-Balancete-Modelo-1-ou-Raz%C3%A3o-Cont%C3%A1bil-com-saldo-incorreto
---

**Ocorrência**

Emissão do relatório não exibe valor do saldo atualizado correto.  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

- Imprima os períodos comparando com o relatório razão contábil, até chegar em uma data em que ambos estejam iguais, se necessário a partir do primeiro movimento quando o saldo anterior deve ser = 0 em ambos.  
- Verifique a pergunta [**Posição antes de L/P?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061200054-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Relat%C3%B3rios-Pergunta-Posi%C3%A7%C3%A3o-antes-de-L-P-?source=search) ela define se a impressão irá considerar ou não a apuração de resultado.   
- Localizando o período execute o reprocessamento de saldo até a data atual.  
- Se permanecer a inconsistência reduza o período que ocorre a diferença até achar o dia.  
- Depois faça filtro por lotes, por natureza da conta até chegar no movimento que ocorre o erro.  
- Sempre compare o Razão com o balancete.

Segue link com informações referente ao relatório balancete modelo 1.  
<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctbr040_balancete_modelo_1.htm>
