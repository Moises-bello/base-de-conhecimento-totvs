---
article_id: 32319592663703
category: Originação de Grãos (OG)
content_hash: ecb3c72a3b7ed48f2924367283c5bf46f17f50ce9984dde092e3f8fdb956b304
fetched_at: '2026-06-28T22:45:43.045634+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para NF de Complemento - Compra
type: support-article
updated_at: '2025-07-14T19:48:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32319592663703-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-NF-de-Complemento-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32319549815703) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Para que serve um **Ponto de Entrada para NF de Complemento - Venda**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA430B | Geração do Nota Fiscal de Complemento | |
| **País(es):** | Todos |
| **Versões/Release:** | 12.1.20 |

**Descrição:**  
Ponto de entrada criado para manipulação das informações (aCab e aItens) antes de gerar a **NF** de **Complemento - Compra**.  
  
**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | **Ponto de entrada criado para manipulação das informações (aCab e aItens) antes de gerar a NF de Complemento (Compra)** |
| **Localização:** | Geração do NF de Complemento (Compra) |
| **Eventos:** | Geração de NF de Complemento |
| **Programa Fonte:** | OGA430B |
| **Função:** | OGA430B2()  Exemplo do PE #include '[protheus.ch](http://protheus.ch/)' #include '[parmtype.ch](http://parmtype.ch/)'  User Function OGX009NF() Local aCab := aClone(PARAMIXB[1]) Local aItens := aClone(PARAMIXB[2]) Local aRet := {} //Customizações do usuário  Local nPos :=  aSCAN(aCab, {|aCab| aCab[1] == "F1\_ESPECIE" })  IF nPos > 0 // Ja stá no array aCab[nPos,1] += 'SPED' Else // Ainda n. se encontra no Array Adicionar aAdd( aCab, { "F1\_ESPECIE" , 'SPED' } ) EndIF  aRet := {aCab,aItens}  Return aRet |
