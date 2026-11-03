---
article_id: 25171277532695
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 27d67601f918a71f2332a1d939a083e77f81868d24b47cbba82a81432aa9b4f3
fetched_at: '2026-06-28T22:38:55.559491+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP A261MOVICQ
type: support-article
updated_at: '2025-03-12T11:40:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25171277532695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-A261MOVICQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25171277514903) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Quando ocorre o erro **A261MOVICQ**, qual o processo a ser avaliado para correção do HELP apresentado?

"*AJUDA:A261MOVICQ*  
*O Estorno não poderá ser efetuado pois existem movimentaçöes em aberto no CQ.*"

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Transferências Mod II (MATA261)**

CQ - Não estorna Produto Destino com Movimentação no CQ  
- Procura na SD7 (Índice 3) pelo "Código do Produto Destino" + "Sequência (NumSeq)".  
- Se encontrar o produto na SD7, verifica: D7\_TIPO > 0 e D7\_ESTORNO = vazio.  
- Help(A261MOVICQ).

**Apontamento de Perdas por OP (MATA685)**  
- Se o D3\_LOCAL for o mesmo que MV\_CQ:  
- Pesquisa na SD7: Filial + D3\_COD + D3\_NUMSEQ.  
- Se encontrar, verifica: D7\_TIPO > 0 e D7\_ESTORNO = vazio.  
- Help(A261MOVICQ).

**Transferência entre Almoxarifados (MATA260)**  
- Verifica se o Local (MV\_CQ) é igual ao Local de destino (D3\_LOCAL) ou Local de origem (D3\_LOCAL).  
- Se sim, verifica na SD7: Filial + D3\_COD + D3\_NUMSEQ.  
- Se encontrar, verifica: D7\_TIPO > 0 e D7\_ESTORNO = vazio.  
- Help(A261MOVICQ).

**Digitação das Produções (MATA250)**  
- Verifica se o D3\_LOCAL = MV\_CQ.  
- Verifica na SD7: Filial + D3\_COD + D3\_NUMSEQ e D7\_ORIGLAN == 'PR'.  
- Busca por Filial + D7\_NUMERO + D7\_PRODUTO.  
- Se encontrar, valida: D7\_TIPO > 0 e D7\_ESTORNO = vazio.  
- Help(A261MOVICQ).

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
