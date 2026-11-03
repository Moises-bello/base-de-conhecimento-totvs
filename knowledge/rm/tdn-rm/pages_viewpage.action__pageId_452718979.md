---
content_hash: fc93acb9ea8a6771240e8a3b18c06717304dd1d70e960611a109139e8a18713a
fetched_at: '2026-06-29T00:10:02.615938+00:00'
page_id: '452718979'
product: rm
source: tdn-rm
title: Intervalo de Tolerância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718979
version: 7
---

Além da tolerância por batida no cadastro de horários é possível definir tolerâncias em Parâmetros Sindicato| Intervalo de Tolerância. Tolerâncias de sindicato serão aplicadas ao cálculo de ocorrências apenas quando não houver nenhuma tolerância definida no horário do funcionário.

**Observação:** Quando no horário está cadastrado o limite de refeição, a tolerância do sindicato não é aplicada a atrasos ou extras.  
Para tolerar estes intervalos, deve ser considerado a carência diária ou a tolerância do limite de refeição diretamente no cadastro do horário.

As tolerâncias são cadastradas definindo a ordem das batidas (campo Batidas) e a natureza.

**Tolerância:**

* **Antes:**Tempo em minutos que será tolerado caso a batida seja realizada antes do planejado;
* **Abate a Tolerância antes da Batida:**Quando marcado, indica que quando a batida for executada antes da tolerância, o tempo da ocorrência gerada terá os minutos da tolerância abatidos de seu tempo total;
* **Depois:** Tempo em minutos que será tolerado caso a batida seja realizada depois do planejado;
* **Abate a Tolerância após a Batida:**Quando marcado, indica que quando a batida for executada depois da tolerância, o tempo da ocorrência gerada terá os minutos da tolerância abatidos de seu tempo total;

**Exemplo:**Funcionário tem que executar a batida no início da jornada às 08:00. E no sindicato existe tolerância cadastrada indicando 00:10 de tolerância. Se a batida for feita às 07:45 e a opção para abater a tolerância não estiver marcada, será gerada extra de 00:15, e se estiver, extra de 00:05 (00:15 - 00:10).

**Observação:**É importante observar que as tolerâncias serão sempre cadastradas alternadamente seguindo a sequência de Entrada e Saída consecutivamente.

**Exemplo:**

Tolerâncias cadastradas:

 Aplicação de tolerâncias nas batidas do dia: 

                    |  Entrada 1 | Saída 1 | Entrada 2 | Saída 2| Entrada 3 |  
-------------------------------------------------------------------------------------------

Batidas          | 20:00     
                      |                  00:00           01:12       06:00       20:00  
                      |                  00:00           01:12       06:00       20:00  
-------------------------------------------------------------------------------------------

Tolerâncias aplicadas

Antes             | 00:10       00:05           00:05       00:10       00:10  
Depois           | 00:10       00:05           00:05       00:10       00:10    

-------------------------------------------------------------------------------------------

**Observação:**Como pode ser observado, as tolerâncias de sindicato serão aplicadas considerando a ordem e natureza das batidas realizadas em cada dia. No exemplo acima o dia 02/05 a primeira batidas é uma saída, portanto a batida executada às 20:00 será considerada para tolerância como  entrada -3.
