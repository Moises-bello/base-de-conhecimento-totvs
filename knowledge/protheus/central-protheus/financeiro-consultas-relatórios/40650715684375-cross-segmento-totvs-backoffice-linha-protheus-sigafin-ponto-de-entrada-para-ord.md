---
article_id: 40650715684375
category: Financeiro - Consultas / Relatórios
content_hash: 9ccc8bb99c9264bc20327a20267a718da194f9467f6d38dc25a78461d2665a4b
fetched_at: '2026-06-28T22:37:58.450238+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Ponto de Entrada
  para ordenação de titulos abertos na rotina FINC030
type: support-article
updated_at: '2026-05-22T20:38:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40650715684375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Ponto-de-Entrada-para-ordena%C3%A7%C3%A3o-de-titulos-abertos-na-rotina-FINC030
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40650760460311)** Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Existe um ponto de entrada no Protheus para ordenar os campos de títulos em aberto ou pagos na consulta de posição de fornecedor (FINC030)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as Releases

**Solução**

Está disponível o ponto de entrada **FC030ORD**, que permite customizar a cláusula **ORDER BY** utilizada na consulta de posição de fornecedor.

Com esse ponto de entrada, é possível alterar a ordenação dos títulos em aberto e dos títulos pagos exibidos na rotina, conforme a necessidade do processo.

Estrutura do ponto de entrada:

```
#include "protheus.ch"
#include "rwmake.ch"

User Function FC030ORD()

Local cEstrut := ParamIxb[1] // Contém os campos que podem ser utilizados na cláusula ORDER BY
Local cOrdAtu := ParamIxb[2] // Contém a cláusula ORDER BY padrão do sistema
Local nOpProc := ParamIxb[3] // Corresponde à visualização de títulos em aberto (1) ou pagos (2)
Local cRet    := ""

Alert("Ponto de entrada para ordenar os títulos " + IIf(nOpProc == 1, "em aberto.", "pagos."))

cRet := "E2_EMISSAO"

Return cRet
```

No exemplo acima, a consulta será ordenada pelo campo **E2\_EMISSAO**.

Importante reforçar que o ORDER BY pode utilizar apenas os seguintes campos:

* E2\_FILIAL
* E2\_FILORIG
* E2\_PREFIXO
* E2\_NUM
* E2\_PARCELA
* E2\_TIPO
* E2\_FORNECE
* E2\_LOJA
* E2\_EMISSAO
* E2\_VENCTO
* E2\_VENCREA
* E2\_BAIXA
* E2\_VALOR
* E2\_SALDO
* E2\_FATURA
* E2\_NATUREZ
* E2\_NUMBCO
* E2\_MOEDA
* E2\_VALJUR
* E2\_PORCJUR
* E2\_TXMOEDA
* E2\_IRRF
* E2\_ISS
* E2\_INSS
* E2\_HIST
* E2\_ACRESC
* E2\_DECRESC
* E2\_SDACRES
* E2\_SDDECRE

Qualquer campo fora dessa estrutura não será reconhecido na customização da com este PE de ordenação.

**Importante 📢️**  
Para a visualização da tela "**Títulos Pagos****"**, caso o PE **FC030IND** esteja aplicado no RPO irá  ser priorizado, sobrepondo a aplicação do PE **FC030ORD** desta documentação.

Saiba Mais:

[FC030ORD - Ordena títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6071594)
