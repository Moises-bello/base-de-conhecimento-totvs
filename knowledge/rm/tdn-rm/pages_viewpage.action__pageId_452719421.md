---
content_hash: 91bac0efe95919f7fa2fc882adbe647e8eac6b1a06ae36246018371cd18baad3
fetched_at: '2026-06-29T00:10:07.715619+00:00'
page_id: '452719421'
product: rm
source: tdn-rm
title: Histórico Provisões - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719421
version: 2
---

O processo de geração do histórico de provisões serve para gerar os dados relativos às provisões mensais (férias e 13º salário) e estes dados são armazenados no histórico de provisões do cadastro do funcionário. Os dados desse histórico são importantes para a emissão de relatórios de provisões e para a geração dos encargos contábeis.  
    
 *Essa geração é obrigatória sempre para a liberação de competência.*   
    
 **Provisão de Férias**  
    
 **Observação:**  
 As informações de NROAVOSVENCFERDEC (No avos férias vencidas decimais) e NROAVOSPROPORDEC (No avos férias proporcionais decimais) respectivamente serão em valores baseados em avos decimais.  
    
 **Exemplo de avos decimais:**  
 Férias vencidas: 18 dias de saldo de férias corresponde a 7,2 avos férias vencidas. O valor da provisão é calculado sobre 7,2, portanto neste caso deverá constar no "campo Número Avos ferias vencidas" 7,2 e não 7.  
 (18 dias / 2,5) = 7,2   
 Cada 2,5 dias correspondem a 1/12 avos = (30 dias /12 meses ao ano = 2,5)   
     
 A data de vencimento das férias será informada com a data existente no campo "Vencimento" do cadastro de férias, no momento da geração da provisão.  
    
 Os Avos Vencidos será a quantidade de avos vencidos de férias no último dia do ano e mês da geração da provisão.  
    
 Os Avos Proporcionais será a quantidade de avos proporcionais de férias, considerando no último dia do ano e mês da geração da provisão.  
    
 **Atenção:**  
 Para os avos vencidos e proporcionais as faltas somente serão consideradas caso o parâmetro "Ignora faltas em férias normais" no cadastro de sindicato estiver desmarcado.  
    
 O valor das médias das férias vencidas facilita a emissão de relatórios com médias discriminadas e já está embutido no campo "Valor da Provisão Férias".  
    
 O valor das médias das férias proporcionais facilita a emissão de relatórios com médias discriminadas e já está embutido no campo "Valor da Provisão Férias".  
    
 **Atenção:**  
 A informação do valor da provisão de férias abatendo férias no mês ou não, conforme parametrizado pelo usuário no campo "Provisão abate o valor das férias do mês" no momento da geração do histórico de provisões não trata a multa resultante de férias vencidas em dobro. O valor calculado neste caso é o valor nominal de férias referente a cada período aquisitivo.  
    
 Quando o parâmetro **"Inibe reversão de valores na provisão mensal de férias"** existente nos parâmetros do sistema estiver marcado o sistema disponibilizará os campos abaixo:

* **Provisão (com abatimento no mês):** Valor da provisão com abatimento das férias do mês.
* **Provisão (sem abatimento no mês):** Valor da provisão sem abatimento das férias do mês.
* **Valor pago de férias no mês:** Valor da provisão sem abatimento das férias do mês menos o valor da provisão com abatimento das férias do mês.

O Valor Provisão Férias Proporcionais totalizará o valor correspondente aos avos de férias proporcionais.  
    
 O Valor Provisão Férias Vencidas totalizará o valor correspondente aos avos de férias vencidas.  
    
 **Provisão de 13º Salário**  
    
 Os Avos 13º Salário será a quantidade de avos de 13º salário, considerando o último dia do ano e mês da geração da provisão.  
    
 O valor das Médias 13º Salário facilita a emissão de relatórios com médias discriminadas e já está embutido no campo "Valor Provisão 13º Salário".   
    
 Para o funcionário demitido, no valor total da provisão de 13º salário será considerado a parametrização feita pelo usuário no campo "Gera provisão com valor zero para demitidos no mês", no momento da geração do histórico de provisões.  
    
 **Observação:**  
 Se o funcionário trabalhar no mínimo 15 dias no mês, este terá direito a um avo de 13º salário.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
