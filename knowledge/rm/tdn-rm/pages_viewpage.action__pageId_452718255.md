---
content_hash: 6ffd7d4005f7feee2697ca44407879e0a692e63d526312ac0dc98b50d83fafce
fetched_at: '2026-06-29T00:09:58.941925+00:00'
page_id: '452718255'
product: rm
source: tdn-rm
title: Fórmulas / Funções – G
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718255
version: 2
---

**Função G**  
 Retorna valor correspondente a anuênio, biênio, etc.   
  **1** equivale a anuênio;   
  **2**, a biênio, etc…  
              G ( VALOR )  
    
 **Exemplo:**  
 Como calcular o triênio  
 **S**E G(3) >= 1 ENTAO MIN ((RC + C("0084")) \* 0.01, 151) SENAO 0 FIMSE  
    
 **Função GDT**  
 Retorna a quantidade de anuênio, biênio, etc na data informada na fórmula, considerando os afastamentos que estornam o tempo de serviço.  
 GDT (VALOR, DATA)   
 Onde o valor poderá ser:   
 **1**= anuênio,   
 **2**= biênio,   
 **3**= triênio etc  
    
 **Exemplo:**  
 GDT (3, '01/12/20013') – Retorna a quantidade de triênio do funcionário em 01/12/2013.
