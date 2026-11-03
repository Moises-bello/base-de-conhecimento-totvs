---
article_id: 32567506572055
category: Originação de Grãos (OG)
content_hash: 47c4fa100d7d8fe163098e7b8672f5686c8fd8f47d5447e7ca7324607f7681e2
fetched_at: '2026-06-28T22:45:43.037106+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para manipular Word para Impressão
type: support-article
updated_at: '2025-07-14T19:48:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32567506572055-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-manipular-Word-para-Impress%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32567477042583) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como funciona o Ponto de Entrada para manipular **Word para Impressão**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGR342 | Rotina de Integração com MS-Word | |
| **Ponto de Entrada:** | OGR342ADV |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.20 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para manipular o array de variáveis do word para impressão. |
| **Localização:** | Função de variáveis disponíveis para impressão. |
| **Programa Fonte:** | OGR342 |
| **Função:** | OGR342ADV |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aExp** | Array | Parâmetros enviados: {aExp} // Array contendo as variáveis para impressão | NÃO | |

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function OGR342ADV()  
  
    Local aExp := PARAMIXB[1]  // Array contendo as variáveis cadastradas  
  
    // Exemplo de customização  
    If (Len(aExp) > 0)  
  
    //Adicionar //VARIÁVEL PARA WORD , VARIÁVEL DE IMPRESSÃO , VARIÁVEL DE PICTURE ,DESCRIÇÃO VARIÁVEIS  
    aAdd( aExp, {'AGR\_CAMPOEXEMPLO' , NJR->NJR\_INSCPO , "NJR->NJR\_INSCPO" , "Inscrição de Campo" })  
  
    EndIf   
  
    Return (aExp)
