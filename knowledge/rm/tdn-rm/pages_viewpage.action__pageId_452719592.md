---
content_hash: 7d571b456545f68927a0475a543f2cb8abdc8a5c1a23bd658f99391b9c517c9f
fetched_at: '2026-06-29T00:10:08.842129+00:00'
page_id: '452719592'
product: rm
source: tdn-rm
title: fórmulas / funções – R
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719592
version: 2
---

**Função R**  
 Retorna salário total dos empregado(s).  
 R  
    
 **Atenção:**  
 As variáveis de fórmula que são relativas a movimentação do funcionário, como a **R**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
    
    
 **Função RAIZ**  
 Calcula retorna a raiz quadrada de um valor dado.  
 RAIZ (VALOR)  
    
    
 **Função RANT**  
 Retorna salário em uma data.  
 RANT (DATA)  
    
 **Função RC**  
 Retorna salário nominal (base).  
 RC  
    
 **Função REEMBVALETR**  
 Retorna o valor a reembolsar de vale transporte do funcionário.  
 O cálculo é feito considerando o valor no campo "Dias Úteis Restantes" existente em Funcionários | Parâmetros, multiplicado pela diferença entre a tarifa atual e a tarifa anterior da linha cadastrada para o funcionário que tenha vigência no mês.  
    
 **Exemplo:**  
 Dias Úteis Restantes = 5  
 Competência = 07/2015  
 Linhas cadastradas para o funcionário

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Linha | Desc. da Linha | Data de Início | Data Final | Valor da Tarifa | Nro. Viagens |
| 3001 | Viação Santa Amália | 02/01/1991 |  | 1,85 | 2 |
| SC01 | Viação Central | 02/01/1991 |  | 1.35 | 2 |
| 5506 | Viação Horto | 02/01/1991 | 30/09/2015 | 2,20 | 2 |

Valores anteriores das tarifas:  
 Linha     Valor  
 3001      1,65  
 SC01     1,25  
 5506      2,00  
    
 O cálculo será 5 \* ( (1,85 – 1,65) + (1,35 – 1,25) ) = R$1,50   
    
 **Função REFCODCALCULO**   
 Retorna a referência do código de calculo   
 REFCODCALCULO (VALOR)  
 Onde   
 Valor – Código de calculo   
    
   **Exemplo:**  
 REFCODCALCULO (1)  
 Retorna a referência do Código de cálculo 1 no movimento do funcionário.  
  Caso o evento com código de cálculo 1 não estiver lançado no movimento do funcionário retorna a jornada cadastrada no funcionário.   
  REFCODCALCULO(2)   
  Retorna referência do Código de cálculo 2 no movimento do funcionário.  
  Caso o evento com Código de cálculo 2 não esteja lançado no movimento do funcionário retorna 30.  
  REFCODCALCULO(8)  
  Retorna a referência do código de cálculo 8 do movimento do funcionário.    
    
    
 **Função RETIRACARACTERES**  
 Retira caracteres de uma ou mais palavras.  
 RETIRACARACTERES (String, String)  
 Onde  
 **String**- Chars  
 **String**- Texto     
    
 **Exemplo:**  
 RETIRACARACTERES ('A', FNOMEMAE)  
    
 **Acompanhamento da Execução.**  
 Constante literal A  
 Variável FNOMEMAE IOLANDA MENDES DA SILVEIRA  
 Chamada a função RETIRACARACTERE A IOLANDA MENDES DA SILVEIRA  
 Resultado da função RETIRACARACTERE IOLND MENDES D SILVEIR  
 Resultado da formula IOLND MENDES D SILVEIR
