---
article_id: 32568657679767
category: Originação de Grãos (OG)
content_hash: 71dd6dd2d447c9c388dc18c4a87dd53f9cb09d7d3af734e858e7227231bd7d04
fetched_at: '2026-06-28T22:45:42.914991+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Documento de Entrada
type: support-article
updated_at: '2025-06-04T19:41:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32568657679767-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32568671070615) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O Ponto de Entrada para **Documento de Entrada**. Como funciona?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGX009 | Geração do Documento de Entrada | |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.15 |

**Descrição:**Ajustes nos fontes para a chamada de **Pontos de Entrada**.  
  
**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | **Validação antes de confirmar o contrato.** |
| **Localização:** | Geração do Documento de Entrada |
| **Eventos:** | Ao confirmar o Romaneio |
| **Programa Fonte:** | OGX009 |
| **Função:** | OGX009NF()  Exemplo do PE #include '[protheus.ch](http://protheus.ch/)' #include '[parmtype.ch](http://parmtype.ch/)'  User Function OGX009NF() Local aCab := aClone(PARAMIXB[1]) Local aItens := aClone(PARAMIXB[2]) Local aRet := {} //Customizações do usuário  Local nPMenNf :=  aSCAN(aCab, {|aCab| aCab[1] == "F1\_MENNOTA" })  IF nPMenNf > 0 // Ja stá no array aCab[nPmenNf,1] += 'Mensagem do PE OGX009NF' // Else // Ainda n. se encontra no Array Adicionar aAdd( aCab, { "F1\_MENNOTA" , 'Mensagem do PE OGX009NF' } ) EndIF  aRet := {aCab,aItens}  Return aRet |
