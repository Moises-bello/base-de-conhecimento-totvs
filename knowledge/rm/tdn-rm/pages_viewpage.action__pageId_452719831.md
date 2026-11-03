---
content_hash: d33986a6a637381bffad46ba931efdc6bfb13568cfb202c59346c578b7d68b7a
fetched_at: '2026-06-29T00:10:10.411071+00:00'
page_id: '452719831'
product: rm
source: tdn-rm
title: Tipos de Ocorrência do Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719831
version: 14
---

Os tipos de ocorrências são os códigos usados pelo Totvs Automação de Ponto para realizar seus cálculos . O sistema dispõe de alguns tipos de ocorrências internos que são inalteráveis visando a estabilidade do produto. Há a flexibilidade do usuário criar seus próprios tipos de ocorrência para utilizar de maneira customizada atendendo assim a necessidade de acordo com o escopo da empresa. O cadastro dos Tipos de Ocorrência encontram-se em Totvs Automação de Ponto| Configurações| Tipos de ocorrência.

Importante

* Os campos em negrito são de preenchimento obrigatório. Para os tipos de ocorrência criados pelo usuário, o Código do Tipo de Ocorrência será precedido do prefixo "#" (cerquilha).
* Ao cadastrar um tipo de ocorrência, *em "Anexos | Tipo de Ocorrência compensação de cálculo", os Tipos de Ocorrência selecionados devem ter naturezas financeiras opostas. **É recomendado** vincular um Tipo de Ocorrência de **crédito** a um Tipo de Ocorrência de **débito**.*"

**Definir se a ocorrência é abonável (Abonável):** este parâmetro faz com que o Tipo de Ocorrência em questão seja abonada. Caso este parâmetro não esteja marcado, ao ser produzido ocorrência em questão não será abonado.   
**Definir se a Ocorrência é Compensável (Compensável):** informar neste campo a ocorrência correspondente que irá realizar a compensação.  
Exemplo:  
Tipo de Ocorrência criada: Hora Extra Fixa  
Tipo de ocorrência que irá compensar: Atraso de Hora Extra Fixa  
Para o tipo de ocorrência Hora Extra Fixa vincular o Atraso de Hora Extra Fixa no campo Anexos|Tipo de ocorrência compensação cálculo. É possível definir também a ocorrência gerada após a compensação informando essa ocorrência a ser gerada em "Tipo gerado após compensação"    
**Tipo de Ocorrência é tolerado(Tolerável):** marque este parâmetro para definir uma tolerância para presença/ausência desse tipo no horário planejado do funcionário. Neste caso, o sistema gera, automaticamente, o Tipo de Ocorrência tolerado tanto para leitura do horário quanto para o cálculo. Atenção! A ocorrência gerada na tolerância pode ser definida pelo usuário, por padrão, o sistema colocará o código do tipo de ocorrência mais o sufixo "T", porém, pode ser alterado.  
Os tipos de ocorrência são vinculados aos eventos a serem calculados pela Automação de Ponto, porém, os tipos criados pelo usuário só podem ser vinculados ao código de cálculo 0043. Lembrando que, para que o evento seja lançado para o movimento ou banco de horas, é preciso que esteja vinculados ao sindicato do funcionário.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Código de Cálculo 0043
