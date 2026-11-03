---
article_id: 6200688129559
category: RH - Contabilização
content_hash: 33f0900c6829984f3c195772c2c686e5333975def734c87a8833adc5b033d54b
fetched_at: '2026-06-28T22:43:46.016395+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP110QRY - Inclusão de Campo -
  Query
type: support-article
updated_at: '2025-07-28T20:07:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6200688129559-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP110QRY-Inclus%C3%A3o-de-Campo-Query
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33775964469015) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como utilizar o Ponto de Entrada GP110QRY - Inclusão de Campo - Query?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

**Solução****01. VISÃO GERAL**

Inclusão de campos que serão selecionados na query da tabela SRZ para utilização, por exemplo, nos lançamentos padrões.

**02. PROGRAMA FONTE**

GPEM110.PRX

**03. SINTAXE**

GP110QRY - Inclusão de Campo - Query ( ) --> aCpos

Retorno

**aCpos** (array\_of\_record)

* Array contendo os campos por "alias" que serão incluídos na query da tabela SRZ

**Observações:**

• Somente campos das tabelas SRV e SI3/CTT podem ser incluídos através deste ponto de entrada.

• Se todos os campos das tabelas SRV e CTT/SI3 utilizados nos lançamentos padrões forem incluídos através deste ponto de entrada, é possível utilizar os parâmetros MV\_CPOSSRV com conteúdo "N" e MV\_CPOSCC com conteúdo "2", de modo que não haverá posicionamento dessas tabelas a cada lançamento processado, onde há ganho de performance na rotina. Deve-se alterar, desse modo, os lançamentos padrões para que ao invés de buscar as informações das tabelas SRV ou CTT/SI3, buscar diretamente do alias SRZ (vide exemplo abaixo).

**Exemplos:**

1) Exemplo de utilização do ponto de entrada:User Function aGP110QRY()Local aCpos := {}aAdd( aCpos, { "SRV", { "RV\_COD", "RV\_DESC", "RV\_INSS", "RV\_IR", "RV\_FGTS", "RV\_INCORP" } } )aAdd( aCpos, { "CTT", { "CTT\_CUSTO", "CTT\_DESC01", "CTT\_DTEXIS" } } )Return(aCpos)2) Exemplo de redefinição do histórico do lançamento padrão quando utilizado o ponto de entrada e os parâmetros MV\_CPOSSRV com "N" e MV\_CPOSCC com "2":Conteúdo anterior: Alltrim(CTT->CTT\_CUSTO) + " - " + Alltrim(SRV->RV\_DESC) + " - " + StrZero( MONTH( DDATABASE ), 2 ) + "/" + StrZero( YEAR( DDATABASE ), 4 )Conteúdo ajustado: If( Type("aIncLog") # "U", Alltrim(SRZ->CTT\_CUSTO) + " - " + Alltrim(SRZ->RV\_DESC) + " - " + StrZero( MONTH( DDATABASE ), 2 ) + "/" + StrZero( YEAR( DDATABASE ), 4 ), "" )

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
