---
article_id: 360018818292
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8aacc6c2c8c61f7187461818828edb4bcfc58e70d25de316db896a05a2d64300
fetched_at: '2026-06-28T22:38:41.268832+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP- FAT- Rastrear no tracker não é exibe o número da nota
type: support-article
updated_at: '2021-04-28T15:51:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018818292-MP-FAT-Rastrear-no-tracker-n%C3%A3o-%C3%A9-exibe-o-n%C3%BAmero-da-nota
---

**Ocorrência**

Rastrear no tracker não é exibe o número da nota.

**Ambiente**

Microsiga Protheus - a partir da versão 11.  
  
**Causa**

O campo **CK\_NUMPV** estava armazenando o número do orçamento (**SCJ**) ao invés do número do pedido efetivado (**SC5**).   
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a tabela **SCK**, via Apsdu.

2. Verifique se o campo **CK\_NUMPV** está com o número do pedido efetivado.

3. Caso não esteja, ajuste a informação correta no campo **CK\_NUMPV** com o número do pedido efetivado.

4. Certifique-se que o ambiente esteja devidamente atualizado com os pacotes de expedição continua de Faturamento e não haja uso de pontos de entrada na efetivação do orçamento, para garantir a integridade de gravação do pedido e registro do pedido no orçamento.

**Obs: O ajuste deverá ser efetuado por um analista que detenha conhecimentos de estrutura Protheus e banco de dados, efetuando o devido backup da tabela e ambiente para realização do procedimento.**
