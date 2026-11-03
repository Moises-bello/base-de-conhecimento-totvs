---
content_hash: b30a60eaa553ecd80fcbf574d34244a437fc6eb43cb13244d0e1923d4f4cb2e4
fetched_at: '2026-06-29T00:09:58.939612+00:00'
page_id: '452718254'
product: rm
source: tdn-rm
title: Fórmulas / Funções - J
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718254
version: 2
---

**Função J**  
 Retorna a jornada mensal.  
   J  
    
 **Função JORSALCOMP**  
 Retorna a jornada do evento.  
    
 **Observação:**  
 Será retornado o valor total da jornada para este evento, caso o evento seja dividido em mais de um centro de custo será retornado a soma das jornadas de todos os centros de custos.  
    
 **Exemplo:**  
  JORSALCOMP('0001')  
    
    
 **Função JORSALCOMPCC**  
 Retorna o valor da jornada do evento por centro de custo.  
 JORSALCOMPCC (String, String)  
    
 **Exemplo:**  
 JORSALCOMPCC ('0002', '01.1')  
              Onde:  
              0002 = (Código de um evento)  
              01.1 =( centro de custo )
