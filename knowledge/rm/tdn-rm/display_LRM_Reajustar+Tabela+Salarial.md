---
content_hash: ae433a11021a814fa254086661f8b1a5f42bc774e3298d000da38db6dc642cc5
fetched_at: '2026-06-29T00:10:05.460232+00:00'
page_id: '452719294'
product: rm
source: tdn-rm
title: Reajustar Tabela Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajustar+Tabela+Salarial
version: 1
---

**Reajustar Tabela Salarial**

---

 O processo *Reajustar Tabela Salarial* é utilizado para reajustar os valores das tabelas salariais selecionadas de acordo com o percentual informado e com o intervalo de valores que se deseja alterar, dando a opção de arredondamento, podendo escolher qual expoente será arredondado e os modos de arredondamento.  
   
  
   
 O mesmo fica localizado no módulo *Gestão de Pessoas* em **Valorização | Tabelas Salariais | Processos.**  
Ao realizar o processo de reajustar tabela salarial, as alterações serão impactadas nos processos que possui essa vinculação.  
 Mais abaixo há o detalhamento de como utilizar o recurso Arredondamento.  
**Descrição dos campos**  
·         *Percentual*  
Neste campo é informado o percentual de reajuste para os valores dos níveis das tabelas selecionadas. É permitido o preenchimento apenas de números positivos.  
   
·         *Intervalo – Valor Inicial e Valor Final*  
 Os campos *Valor Inicial* e *Valor Final* definem o intervalo de valores que receberão o reajuste.  
 Atente de que os valores do campo estão inclusos no reajuste e de que o campo *Valor* *Inicial* deve ser maior que o *Valor* *Final*.  
   
·         *Arredondamento – Menor Expoente e Modo*  
 O campo *Menor* *Expoente* é utilizado para definir qual casa decimal será arredondada. Os valores permitidos são aqueles a partir de **-2**.  
 O campo *Modo* é para definir como será o arredondamento, se o mesmo será para o *Próximo* *Valor*, *Valor* *Anterior*, ou se *Padrão*, que é quando se a casa decimal for igual ou maior à metade da potência de 10, será arredondado para o próximo valor, senão, para a o anterior.  
   
Ø  **Dicas:**  
        i.            Para apenas arredondar a tabela salarial, deixe o campo *Percentual* com 0.  
      ii.            Para apenas reajustar sem arredondar, deixe o campo *Menor* *Expoente* com -2.  
   
 Exemplos no modo **Padrão** apenas arredondando:

|  |  |  |  |
| --- | --- | --- | --- |
| **Menor Expoente** | **Valor anterior** | **Novo valor** | **Resultado** |
| -2 | 100,11 | 100,11 | Arredonda a segunda casa decimal, se houver 3 casas decimais |
| -1 | 100,15 | 100,20 | Arredonda a primeira casa decimal para cima |
| 0 | 111,61 | 112,00 | Arredonda a casa das unidades para cima |
| 1 | 114,11 | 110,00 | Arredonda a casa das dezenas para baixo |
| 2 | 192,36 | 200,00 | Arredonda a casa das centenas para cima |

Exemplos no modo **Próximo** **Valor** apenas arredondando:

|  |  |  |  |
| --- | --- | --- | --- |
| **Menor Expoente** | **Valor anterior** | **Novo valor** | **Resultado** |
| -2 | 111,11 | 111,11 | Arredonda a segunda casa decimal, se houver 3 casas decimais para cima |
| -1 | 111,11 | 111,20 | Arredonda a primeira casa decimal para cima |
| 0 | 111,11 | 112,00 | Arredonda a **casa** das unidades para cima |
| 1 | 111,11 | 120,00 | Arredonda a casa das dezenas para cima |
| 2 | 111,11 | 200,00 | Arredonda a casa das centenas para cima |

Exemplos no modo **Valor** **Anterior** apenas arredondando:

|  |  |  |  |
| --- | --- | --- | --- |
| **Menor Expoente** | **Valor anterior** | **Novo valor** | **Resultado** |
| -2 | 111,11 | 111,11 | Arredonda a segunda casa decimal, se houver 3 casas decimais para baixo |
| -1 | 111,11 | 111,10 | Arredonda a primeira casa decimal para baixo |
| 0 | 111,11 | 111,00 | Arredonda a casa das unidades para baixo |
| 1 | 111,11 | 110,00 | Arredonda a casa das dezenas para baixo |
| 2 | 111,11 | 100,00 | Arredonda a casa das centenas para baixo |

 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Tabelas Salariais
