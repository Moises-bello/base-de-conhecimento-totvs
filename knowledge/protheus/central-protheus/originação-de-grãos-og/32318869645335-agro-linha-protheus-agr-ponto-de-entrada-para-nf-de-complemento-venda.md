---
article_id: 32318869645335
category: Originação de Grãos (OG)
content_hash: db8dc44b0be44078f5ddcab448f2ab3ee4a9fe46ff73cb00c441bde2b5cbdc32
fetched_at: '2026-06-28T22:45:43.054628+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para NF de Complemento - Venda
type: support-article
updated_at: '2025-07-14T19:49:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32318869645335-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-NF-de-Complemento-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32318869631767) Tempo aproximado para leitura: **00:01:30 min**  
  
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
Ponto de entrada criado para manipulação das informações (aCab e aItens) antes de gerar a **NF** de **Complemento - Venda**.  
  
**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | **Ponto de entrada criado para manipulação das informações (aCab e aItens) antes de gerar a NF de Complemento (Venda)** |
| **Localização:** | Geração do NF de Complemento (Venda) |
| **Eventos:** | Geração de NF de Complemento |
| **Programa Fonte:** | OGA430B |
| **Função:** | OGA430B1()  Exemplo do PE #include '[protheus.ch](http://protheus.ch/)' #include '[parmtype.ch](http://parmtype.ch/)'  User Function OGA430B1() Local aCab := aClone(PARAMIXB[1]) Local aItens := aClone(PARAMIXB[2]) Local aRet := {} //Customizações do usuário  Local nPos :=  aSCAN(aCab, {|aCab| aCab[1] == "C5\_NATUREZ" })  IF nPos > 0 // Ja stá no array aCab[nPos,1] += 'COFINS' Else // Ainda n. se encontra no Array Adicionar aAdd( aCab, { "C5\_NATUREZ" , 'COFINS' , nil} ) EndIF  aRet := {aCab,aItens}  Return aRet |
