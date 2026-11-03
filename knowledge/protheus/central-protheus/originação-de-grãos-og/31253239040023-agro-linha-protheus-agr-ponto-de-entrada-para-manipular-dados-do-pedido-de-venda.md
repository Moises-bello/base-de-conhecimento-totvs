---
article_id: 31253239040023
category: Originação de Grãos (OG)
content_hash: 8862cee1c7e45fbab87cf715ef9921e11c49becfa4d95ea449c8fe39f5101061
fetched_at: '2026-06-28T22:45:43.007335+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para manipular dados do Pedido
  de Venda
type: support-article
updated_at: '2025-08-11T13:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31253239040023-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-manipular-dados-do-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31253217779223) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**O que é que indica a tabela **Ponto de Entrada para manipular dados do Pedido de Venda**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA300 | Acordo de Troca | |
| **Ponto de Entrada:** | AG300APVAC |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.20 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar Acordo de Troca. |
| **Programa Fonte:** | OGA300 |
| **Função:** | Permitir manipular dados do Pedido de Venda do Acordo de Troca. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **AG300APVAC** | Nenhum | Envia como parâmetro array do cabeçalho e itens do Pedido de Venda | Não | |

****Exemplo:****

#include '[protheus.ch](http://protheus.ch/)' #include '[parmtype.ch](http://parmtype.ch/)' 

user function AG300APVAC ()

    Local oModel := aClone(PARAMIXB[1])  
    Local aCab := aClone(PARAMIXB[2])  
    Local aItens := aClone(PARAMIXB[3])  
    Local aRet := {} //Customizações do usuário

aAdd( aCab, {"C5\_MEUCAMPO"  , 'Valor'       , Nil } )

 

aRet := {aCab,aItens}

Return aRet
