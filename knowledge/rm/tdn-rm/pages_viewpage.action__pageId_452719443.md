---
content_hash: 5276b89db133240f94a2bada016a76aaf0aa589b1f576a9212c09f018b6faefc
fetched_at: '2026-06-29T00:10:07.808455+00:00'
page_id: '452719443'
product: rm
source: tdn-rm
title: Cálculo 13° Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719443
version: 2
---

A gratificação natalina, conhecida como 13º salário é paga em duas parcelas a todos os empregados urbanos, rurais e domésticos.   
 A primeira parcela é paga entre os meses de fevereiro e novembro de cada ano, e a segunda, até o dia 20 de dezembro. Dependerá da convenção coletiva da empresa. Se na convenção coletiva, nada for citado, prevalecerá o pagamento em duas parcelas. Neste menu você poderá lançar o pagamento da primeira e/ou segunda parcela.   
 **Primeira parcela:** Marque este campo se a empresa está processando a primeira parcela para o pagamento.  
 **Ajustar primeira parcela:** Este campo vem marcado default sempre que for lançada a 1ª parcela.   
 O parâmetro funciona da seguinte forma: Suponhamos que foi realizado o adiantamento do 13º salário no mês de Julho/16, para um funcionário que tem o salário de R$ 1000,00. Em Novembro/16 ele recebeu um aumento salarial e passou a receber R$1500,00.  
 Para que o ajuste referente a alteração salarial seja efetuado ao lançar novamente a 1ª parcela, o parâmetro "Ajustar 1ª Parcela" deverá ser marcado. Desse modo, os seguintes eventos referentes a 13º serão lançados:

* 1ª Parcela de 13º Salário (Código de Cálculo 9) no valor de R$ 750,00 (Provento);
* Adiantamento de 13º Salário (Código de Cálculo 35) no valor de R$ 500,00 (Desconto).  
   Onde a diferença referente ao aumento salarial corresponde a R$ 250,00.  
   Se este parâmetro não estiver marcado, o sistema verificará que o evento de 1ª Parcela de 13º Salário já foi lançado (Código de Cálculo 009) e não fará o lançamento do ajuste.  
      
   **Segunda parcela:** Marque este campo se a empresa for processar a 2ª parcela de 13º salário.   
      
   Podemos lançar juntamente com as parcelas do 13 salário os códigos fixos e os eventos programados cadastrados nos anexos do funcionário que possuem o tipo 13º Salário.   
      
   Maiores Detalhes sobre parametrizações do 13 veja no documento "Como fazer".  
    

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  [Parametrizações 13° Salário](http://tdn.totvs.com/pages/releaseview.action%3bjsessionid=46C24773CEE8B1A8073FD4A270F6AAE4?pageId=207357578)
