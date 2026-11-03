---
article_id: 40723934746519
category: Financeiro - Consultas / Relatórios
content_hash: 5e2cc7548de301f7ec12a75bf50b07a25ec27a5d5572c5b9c1a3b47d994e4e98
fetched_at: '2026-06-28T22:37:58.445015+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Ponto de entrada
  para alterar a ordem de exibição na consulta de Posição de Fornecedores (FINC030)
type: support-article
updated_at: '2026-05-25T18:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40723934746519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Ponto-de-entrada-para-alterar-a-ordem-de-exibi%C3%A7%C3%A3o-na-consulta-de-Posi%C3%A7%C3%A3o-de-Fornecedores-FINC030
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40723934727831)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Qual é o ponto de entrada utilizado para alterar a ordem de exibição dos registros das pastas "Títulos Pagos" e "Faturamento", na opção "Consultar" da rotina de Consulta de Posição de Fornecedores (FINC030)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

Para alterar a ordem de exibição do conteúdo nas pastas de consulta da rotina FINC030, deve-se utilizar o ponto de entrada FC030IND. Ele permite customizar a ordenação dos dados retornados nas abas de "Títulos Pagos" e "Faturamento".

##### **Parâmetros:**

| **Nome** | **Tipo** | **Descrição** |
| --- | --- | --- |
| **nPasta** | Numérico | Número da pasta em que se deseja alterar a ordem:  2 = **"Títulos Pagos"**  4 = **"Faturamento"** |
| **aCampos** | Vetor | Array contendo os campos exibidos na respectiva pasta selecionada. |

##### **Retorno:** **cCpoUser:** Variável do tipo Caracter que deve conter a expressão AdvPL utilizada para ordenar os dados na pasta correspondente.

```
#include "protheus.ch"

User Function FC030IND()                                      
    Local nPasta   := ParamIxb[1]
    Local aCampos  := ParamIxb[2]
    Local cCpoUser := ""
    Local nPos     := 0

    If nPasta == 2   // Pasta Títulos Pagos
        // Exemplo: Ordena os registros pela Data de Baixa
        nPos := aScan( aCampos, { |x| AllTrim( x[1] ) == "BAIXA" } )
        If nPos > 0
            cCpoUser := "DTOS( " + aCampos[ nPos, 1 ] + " ) "
        EndIf
    EndIf

    Return cCpoUser
```

**Saiba Mais:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Ponto de Entrada para ordenação de titulos abertos na rotina FINC030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40650715684375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Ponto-de-Entrada-para-ordena%C3%A7%C3%A3o-de-titulos-abertos-na-rotina-FINC030)

[FC030IND - Altera ordem de exibição da consulta](https://tdn.totvs.com/pages/releaseview.action?pageId=6071553)
