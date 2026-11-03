---
article_id: 36385800389527
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 39bcc2a2bf35175eda3b0b33c06ba1b7494cf02740081c29f8b2779e9062ff85
fetched_at: '2026-06-28T22:38:54.295856+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao realizar a geração
  de um documento de entrada, não está gerando na SD3 o movimento RE5 referente ao
  retorno de Beneficiamento.
type: support-article
updated_at: '2025-11-24T18:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36385800389527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-realizar-a-gera%C3%A7%C3%A3o-de-um-documento-de-entrada-n%C3%A3o-est%C3%A1-gerando-na-SD3-o-movimento-RE5-referente-ao-retorno-de-Beneficiamento
---

Ao realizar o retorno de um produto industrializado por terceiros via rotina MATA103 no TOTVS Protheus, não está sendo gerado o registro RE5 na tabela SD3. A correção foi implementada e está disponível nos pacotes de atualização para as versões 12.1.2210, 12.1.2310, 12.1.2410 e 12.1.2510, garantindo o registro correto do movimento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36385807720343) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como corrigir ao realizar o retorno de um produto industrializados por terceiros de beneficiamento através da rotina **MATA103**não está gerando registro **RE5**na tabela **SD3**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ao realizar o retorno de um produto industrializados por terceiros de beneficiamento através da rotina MATA103 não esta gerando registro RE5 na tabela SD3.

Realizamos o ajuste para que o movimento seja gerada corretamente.  Atualizando em ambiente de homologação o pacote de correção abaixo:

**12.1.2310:**[**https://r.totvs.io/p/1221638**](https://r.totvs.io/p/1221638%20)

**12.1.2410:**[**https://r.totvs.io/p/1221636**](https://r.totvs.io/p/1221636)

**12.1.2510:**[**https://r.totvs.io/p/1221639**](https://r.totvs.io/p/1221639)

**OBS**: Sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
