---
content_hash: 5ce203b2f75d8228f41b40b74f233aad4253a818bbda974af400582c3a389887
fetched_at: '2026-06-29T00:10:07.757725+00:00'
page_id: '452719430'
product: rm
source: tdn-rm
title: Código de Cálculo 314 - Arredondamento de Desconto Base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719430
version: 5
---

Evento Base de Cálculo e sem incidência.  
   
Quando o parâmetro 'Lança desconto de arredondamento (código de cálculo 21)' existente em Opções | Parâmetros | RM Labore | Param. 13º Salário está Desmarcado o sistema lança o evento com código de cálculo 314 para armazenar o valor do arredondamento (cc21), para que o mesmo seja descontado no próximo período.   
   
Já no caso de o parâmetro 'Lança desconto de arredondamento (código de cálculo 21)' existente em Opções | Parâmetros | RM Labore | Param. 13º Salário esteja Marcado o sistema lança o evento com código de cálculo 21 para armazenar o valor do arredondamento (cc21).  
   
Este tratamento foi implementado para o sistema não descontar o evento com código de cálculo '21-Arredondamento Descontos' no lançamento do 13º Salário. E atender a 1º e 2º parcela do 13º Salário.  
**Exemplo:**  
No período 1 foram realizados os seguintes lançamentos:  
   
**Cod.     Descrição                    Valor**           **Prov/Desc/Base**  
0008     Desconto de faltas                     1.000,00           Desconto  
0020     Arredondamento                        1.000,00           Provento  
**Liquido: 0,00 (zero)**  
   
No período 2 foi processado o lançamento da 1º parcela com o parâmetro 'Lança desconto de arredondamento (código de cálculo 21)' MARCADO:  
**Cod.     Descrição                      Valor        Prov/Desc/Base**  
0009     1ª Parcela 13º                                500,00           Provento  
0314     Base Arredondamento(cc314)    1.000,00           Base  
**Liquido: 500,00**  
   
Se for realizado um lançamento para o funcionário no período 3 é descontado o arredondamento.  
**Cod.   Descrição                        Valor        Prov/Desc/Base**  
9999     Provento                                      1.300,00            Provento  
0021     Arredondamento Desc.(cc21)      1.000,00           Desconto  
**Liquido: 300,00**

Foi inserida uma melhoria no Log de Cálculo, para que passe a exibir a origem dos valores e o período considerado nos códigos de cálculo 314. Mais informações: [DT - Códigos de Cálculo 21/314/419 - Melhoria do Log de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=917132275)

*Exemplo da melhoria no Código de Cálculo 314*                                                       

**Observação:** Esse código de cálculo também poderá ser lançado em competências e períodos que não sejam do pagamento de 13º salário, porém esse lançamento deverá ser feito de forma manual.  
 

**Códigos de Cálculo**
