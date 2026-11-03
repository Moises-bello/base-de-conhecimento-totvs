---
article_id: 360040971653
category: Financeiro - Caixinha
content_hash: c22bc297e257bbd5477be0c7b448131fd739ebd4bcd4a241d7a84f49e8e52364
fetched_at: '2026-06-28T22:37:53.894614+00:00'
product: protheus
section_id: 1500001550702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA560 - Help FA560BAIXA
  Caixinha não deixa estornar prestação de contas
type: support-article
updated_at: '2024-05-14T14:51:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040971653-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA560-Help-FA560BAIXA-Caixinha-n%C3%A3o-deixa-estornar-presta%C3%A7%C3%A3o-de-contas
---

**Ocorrência**Como proceder no caso de um lançamento de prestação de contas incorreto, com devolução do adiantamento e fechado?

![](https://totvssuporte.zendesk.com/attachments/token/x5TBYxIfVQST0k6lUMcyYEkpH/?name=Caixinha.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA560 – A partir da versão 12.0  
  
**Causa**Quando o parâmetro **MV\_PCTCAIX**não está ativo e baixa errado.

**Solução**  
Atualmente no padrão do Protheus não tem nenhum procedimento/processo/parâmetro para estorno  de Prestação de Contas incorreto, com devolução do adiantamento fechado. O sistema verifica se o status da **Prest. de Contas do adiantamento**, caso estiver com status vermelho não tem como retornar sendo necessário estar com saldo.  
  
**Importante:**  
Existe o parâmetro **MV\_PCTCAIX** , porém não é para tratar o cancelamento da **Prest. Contas** quando esse estiver com status vermelho de movimento baixado 100% e somente quando há saldo.  
  
**Saiba mais:**  
Este Ponto de Entrada **F560DEL** define a permissão para exclusão/cancelamento de movimentos do caixinha, como por exemplo a permissão de cancelar um adiantamento, para que o valor do mesmo volte (ou não) ao saldo do caixinha sem a prestação de contas.  
<https://tdn.totvs.com/pages/releaseview.action?pageId=649323624>
