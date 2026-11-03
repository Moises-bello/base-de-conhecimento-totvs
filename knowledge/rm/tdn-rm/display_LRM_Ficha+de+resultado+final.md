---
content_hash: 62e506be2ed57ff6fea4b01b4b81b02e8ce2dfa19985387ec8833cccda14aec4
fetched_at: '2026-06-29T00:08:58.428429+00:00'
page_id: '359475446'
product: rm
source: tdn-rm
title: Ficha de resultado final
type: documentation
url: https://tdn.totvs.com/display/LRM/Ficha+de+resultado+final
version: 5
---

### Visão geral

O Provider de dados "**Ficha de Resultado Final**" tem como objetivo a disponibilização de informações para a listagem dos alunos matriculados em uma turma e seus status e notas definidos como resultados finais para um relatório.

Através do link [Ata de Resultado Final](http://tdn.totvs.com/pages/releaseview.action?pageId=190518508&preview=/190518508/190746729/EDUREL0008%20-%20Ata%20de%20Resultado%20Final.pdf) é possível visualizar um exemplo do relatório de ata de resultado final, disponibilizado no Book, que utiliza o Provider.

A partir das versões **12.1.2205.222, 12.1.2209.168 e 12.1.2302** o provider passa a ter o campo de faltas, que passa a incorporar no book de relatórios,  e veja o novo relatório.

### Informações disponibilizados pelo Provider

O Provider espera receber as seguintes informações de entrada:

* Código da coligada
* Código da filial
* Id. do Período Letivo
* Código da turma

Através dessas informações, será disponibilizada uma lista com todos alunos matriculados nas turmas/disciplinas da turma do período letivo informado, com as seguintes informações:

* Número no diário
* Registro acadêmico
* Nome do aluno
* Id. da Turma/Disciplina
* Id. do Período Letivo
* Código da turma
* Código da filial
* Código da disciplina
* Nome da disciplina
* Código do status de resultado da matrícula no período letivo
* Nome do status de resultado da matrícula no período letivo
* Código do status de resultado da disciplina
* Nome do status de resultado da disciplina
* Valor da nota/conceito da etapa
* Valor da falta da etapa (somente a partir das versões **12.1.2205.222, 12.1.2209.168 e 12.1.2302**).

### Condições para disponibilização do resultado

* Serão listados todos os alunos matriculados em turma/disciplinas da turma informada no Provider.
* Os campos de código/nome do status de resultado serão exibidos, caso os campos de **Resultado** da matrícula no período letivo e/ou na disciplina estejam definidos.
* Os valores das notas/conceitos serão exibidas quando a nota/conceito for lançada em uma **etapa final de nota**.
* Os valores das faltas serão exibidas quando a falta for lançada em uma **etapa final de falta** (somente a partir das versões **12.1.2205.222, 12.1.2209.168 e 12.1.2302**).
* O Provider disponibiliza uma lista de até 29 disciplinas de uma mesma turma, para composição do relatório. ( O relatório de Ata de Resultado Final do Book é disponibilizado com uma composição de 14 disciplinas )
* As casas decimais das notas serão formatadas conforme parametrização realizada:
  + Nível de ensino básico
    - Quantidade de casas decimais definida no cadastro de disciplina da grade.
  + Nível de ensino superior
    - Quantidade de casas decimais definida no cadastro de disciplina da turma/disciplina
  + Caso não seja informada a quantidade de casas decimais, os valores serão apresentados com 4 casas decimais.
