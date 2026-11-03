---
content_hash: c28428f6eb1852d18877cc2c02f321d2cf4a4dfcb24ce496d9073ad6d12ee16d
fetched_at: '2026-06-29T00:10:08.497436+00:00'
page_id: '452719525'
product: rm
source: tdn-rm
title: Código de Cálculo 373 – 13º Rescisão Licença Maternidade Provento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719525
version: 2
---

Evento Provento e do tipo valor.   
 O sistema buscará o valor calculado do 13° de rescisão (CC48), dividirá pelo número de meses trabalhados no ano, dividirá por 30 e multiplicará pelo número de dias de afastamento por licença maternidade no ano.  
    
 Após feito esse cálculo, será calculado novamente o evento CC48, reduzindo o valor original pelo valor calculado neste.  
    
 **Atenção:** O evento com Código de Cálculo 373 deve ter Prioridade maior que o evento com Código de Cálculo 48.  
 **Observação:** O As incidências de FGTS 13 e INSS 13 devem obrigatoriamente estar iguais as incidências do evento de Código de Cálculo 48.  
    
 **Exemplo de cálculo:**  
    
 **Funcionário com licença maternidade terminando no dia 28 de janeiro e demissão em novembro:**  
 **1º cálculo do 13º salário rescisão sem média**  
               **Calculando evento: 0373 -** 13º RESCISÃO LICENÇA MATERNIDADE PROVENTO  
               Código de Cálculo 373 - Prioridade 2  
                 
                      Dias de Licença Maternidade durante o ano: 28  
 **Valor pago no evento 0048, CC 48: 751,695000**  
                      Valor referente ao período: 751,695000 / 9 / 30 \* 28 = 77,950000  
 **Valor do evento: 77,95**  
    
 **2º cálculo com valores de médias sendo que tem valor de média no grupo 0 também**  
               **Calculando evento: 0373 -** 13º RESCISÃO LICENÇA MATERNIDADE PROVENTO  
               Código de Cálculo 373 - Prioridade 2  
                 
                      Dias de Licença Maternidade durante o ano: 28  
                      Valor pago no evento 0088, CC 48: **154,330000**  
                      Valor referente ao período: 154,330000 / 9 / 30 \* 28 = **16,000000**  
 **Valor pago no evento 0048, CC 48: 784,345000**  
                      Valor referente ao período: 784,345000 / 9 / 30 \* 28 = **81,340000**  
                      **Valor do evento: 97,34**  
    
 **Valores dos eventos:**   
    
 \*\*\*\*\*\*\*\*\*\*\*\*\***0373           13º RESCISÃO LICENÇA MATERNIDADE PROVENTO**  
    
 81,34 + 16,00 = **97,34**  
    
 \*\*\*\*\*\*\*\*\*\*\*\*\***0088           MEDIA HORA EXTRA 13º RESCISAO = 138,30**  
    
 **Valor no log de média**  
 Proporcionaliza média do grupo 1 para 10 avo(s) de 13o.Salário: 205,77 / 12 \* 10 = 171,475000  
 Valor referente a 1 avo(s) de 13o.indenizado: 17,15             
    
 **Média sem 13o.indenizado: 17,15**  
 171,475 – 17,15 = **154,325**  
    
               Calculando evento: 0088 - MEDIA HORA EXTRA 13º RESCISAO  
               Código de Cálculo 48 - Prioridade 0 - Evento de Média  
                 
                      **Valor do evento: 138,330000**  
                      Valor referente ao período de Licença Maternidade, lançado no evento de CC 373**: 16,00**  
                      Total de 13o. rescisão pago ao funcionário: **154,33**  
    
 \*\*\*\*\*\*\*\*\*\*\*\*\***0048           13º SALARIO RESCISAO**  
    
 784,35 – 81,34 = 703,01  
               Calculando evento: 0048 - 13º SALARIO RESCISAO  
               Código de Cálculo 48 - Prioridade 1  
                 
                      **Valor do evento: 703,010000**  
                      Valor referente ao período de Licença Maternidade, lançado no evento de CC 373: **81,34**  
                      Total de 13o. rescisão pago ao funcionário: 784,35

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
