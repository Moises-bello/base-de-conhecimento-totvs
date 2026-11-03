---
article_id: 360021793151
category: Financeiro - Baixas a Receber
content_hash: 14b9d11c081a4f1e3cfd6d2f034116cc478cadf1d4e1e48f0eab6b82d9ba52d6
fetched_at: '2026-06-28T22:37:43.706411+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Ao baixar
  um título apresentando Help: M010VLDI5 - Problema: FK4_NATURE - OBRIGAT - O campo
  Natureza (FK4_NATURE) não foi preenchido'
type: support-article
updated_at: '2025-07-30T16:43:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021793151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Ao-baixar-um-t%C3%ADtulo-apresentando-Help-M010VLDI5-Problema-FK4-NATURE-OBRIGAT-O-campo-Natureza-FK4-NATURE-n%C3%A3o-foi-preenchido
---

**Dúvida**Por que exibe tela de help M010VLDI5 na baixa de títulos com retenção de impostos na baixa?  
  
**Ambiente**Protheus – Financeiro – A partir da versão 12  
  
  
**1) Solução**

A tela de help M010VLDI5 é exibida nas baixas de título que tenham as retenções de seus impostosna baixa do título principal.  
A inconsistência relatada ocorre quando o campo "uso natureza(ED\_USO)", definido em algum dos parâmetros abaixo, esteja preenchido com o conteúdo diferente de "0 - Livre". Ou seja, todas as naturezas definidas nos parâmetros abaixo devem ter seu uso "livre"  
  
MV\_ISS = "ISS"     (Conteúdo Padrão entre aspas)  
MV\_INSS = "INSS" (Conteúdo Padrão entre aspas)  
MV\_IRF = "IRF"   (Conteúdo Padrão entre aspas)  
MV\_CSLL = CSLL  (Conteúdo Padrão sem aspas)   
MV\_COFINS = CONFINS (Conteúdo Padrão sem aspas)   
MV\_PISNAT = PIS (Conteúdo Padrão sem aspas)

**2) Solução**

Verificar o tamanho dos campos abaixo tanto no dicionário como também no banco de dados

FK4\_NATURE e ED\_CODIGO e entre outros campos  como SE1, SE2, SE5, FK1, FK2, FK5 que fazem parte das naturezas

Exemplo que pode apresentar o erro

Veja que o campo ED\_CODIGO no dicionário possui um tamanho de 10 caracteres

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19070499624599)](https://totvssuporte.zendesk.com/guide-media/01HF7PZAPJ3W23EGHAVK1J1M59)

Porém o campos ED\_CODIGO banco de dados (APSDU) o campo possui um tamanho de 11 caracteres

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19070499635735)](https://totvssuporte.zendesk.com/guide-media/01HF7Q2WVSN5G3RS3K22927WDX)

Com isso o sistema irá tentar gravar um conteúdo de 11 caracteres (ED\_CODIGO) em um campo de 10 caracteres FK4\_NATURE , com isso irá apresentar o HELP M010VLDI5
