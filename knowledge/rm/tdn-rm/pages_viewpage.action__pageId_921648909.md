---
content_hash: 3fe46d411d06a89f90c378659afc8c07970fd5a3427913908e9aeb202681b486
fetched_at: '2026-06-29T00:12:07.206710+00:00'
page_id: '921648909'
product: rm
source: tdn-rm
title: Geração de Lançamento - Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=921648909
version: 100
---

---

As versões homologadas, são: **12.1.2506.253** ou superior; **12.1.2510.176** ou superior; **12.1.2602.1** ou superior. Este documento detalha o processo definição do preço durante a geração do lançamento financeiro para instituições que utilizam a Funcionalidade de Tabela de Preço -

No curso/habilitação do aluno estiver associado uma tabela de preço, o sistema irá utilizar essa tabela de preço para buscar os valores de créditos financeiros para a geração dos lançamentos. Caso não tenha uma tabela de preço associada ao curso/habilitação do aluno o sistema irá verificar a data de corte.

Data de corte para utilizar a Tabela de Preço

O parâmetro da data de corte será utilizado quando no curso/habilitação do aluno não tiver uma tabela de preço associada e o parâmetro "Utilizar tabela de preço" estiver marcado.

* Quando a data de corte for maior ou igual que a data de criação do curso/habilitação, o valor será considerado da tabela de preço.
* Quando a data de corte for menor que a data de criação do curso/habilitação, o valor de crédito será considerado do crédito da Matriz Curricular ou da Faixa de Crédito

Com a parametrização para habilitar o  será possível visualizar a data de criação do curso/habilitação do aluno para saber se está dentro da data de corte.

Se a Tabela de Preço estiver dentro da regra da data de corte e não estiver associada ao curso/habilitação, ou parametrizada para associar no momento da matricula. No processo de matrícula de alunos ingressantes com o sistema parametrizado para gerar lançamento na matrícula, ou na geração de lançamento do contrato será exibida a mensagem de validação "Não é possível gerar o lançamento porque nenhuma tabela de preço foi associada."

**Configurações Obrigatórias da Matriz:**

Antes da validação da tabela de preço, o sistema verifica a consistência dos dados da matriz. Para garantir o cálculo correto:

* O Curso/Habilitação deve possuir um **Plano de Pagamento** devidamente associado. É necessário garantir que, nas configurações deste plano, as parcelas sejam geradas com base no **valor de crédito**;
* Nas propriedades da Disciplina da Matriz Curricular, certifique-se de que o campo **"Nº de créditos para cobrança"** esteja devidamente preenchido. O campo **"Valor do crédito"** não é obrigatório na matriz, pois o sistema utilizará o valor definido na **Tabela de Preço**.
Valor de Crédito da Tabela de PreçoDisciplina da Matriz do Aluno

Na matrícula do aluno em disciplinas da sua matriz curricular com parâmetro **Usar valor do créditos financeiros da matriz curricular do aluno** desmarcado ou marcado, sempre será utilizado o valor da Tabela de Preço.

Exemplo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Valor do Crédito na Matriz do Aluno** |  | **Valor do Crédito na Tabela de Preço** |
| Introdução ao Direito | R$100 | R$190 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da sua matriz o comportamento não terá impactado e utilizará o valor da Tabela de Preço.

Mesma disciplina em matriz diferente

* **Usar valor do créditos financeiros da matriz curricular do aluno:** Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for de outra matriz curricular e também estiver ofertada na matriz curricular do aluno deverá ser considerado o valor do crédito da Tabela de Preço

Exemplo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Valor do Crédito da Matriz do Aluno** |  | **Mesma Disciplina  (fora da grade do aluno)** | **Valor do Crédito da Mesma Disciplina (fora da grade do aluno)** |  | **Valor do Crédito da Tabela de Preço** |
| Introdução ao Direito | R$100 | Introdução ao Direito | R$150 | R$190 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da sua matriz, mas essa disciplina pertence a outra grade.

Disciplinas diferentes com equivalência

* **Usar valor do créditos financeiros da matriz curricular do aluno:** Se o sistema estiver com este parâmetro marcado, e se a disciplina for ofertada em outra matriz curricular e equivaler alguma disciplina na matriz curricular do aluno, deverá ser considerado o valor do crédito da Tabela de Preço

Exemplo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Valor do Crédito da Matriz do Aluno** |  | **Disciplina equivalente (fora da grade do aluno)** | **Valor do Crédito da Disciplina equivalente** |  | ****Valor do Crédito da Tabela de Preço**** |
| Introdução ao Direito | R$100 | Teoria Geral do Direito | R$160 | R$190 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da outra grade que possui equivalência cadastrada com a disciplina da matriz da sua grade.

Disciplinas diferentes com equivalência múltipla

* **Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de crédito em caso de equivalência múltipla:** Se o sistema estiver com parâmetro marcado, o comportamento do sistema deve ser o conforme descrito abaixo:

1° Matricula tem duas disciplinas com equivalência para uma da matriz: o sistema irá considerar o valor do crédito da Tabela de Preço na primeira disciplina matriculada e na segunda ficará zerada

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Valor do Crédito da Matriz do Aluno** |  | **Disciplinas equivalentes** **(fora da grade do aluno)** | **Valor do Crédito da Disciplina equivalente** |  | ****Valor do Crédito da Tabela de Preço**** |  |
| Direito Civil - I | R$110 | Teoria Geral do Direito | R$140 | R$190 | 1° disciplina com valor da Tabela de Preço |
|  |  | Teoria Geral do Direito II | 0 | 0 | 2° disciplina ficará zerada, pois o valor foi considerado na 1° disciplina equivalente. |

2° Matricula tem uma disciplina com equivalência para duas da matriz: o sistema irá considerar o valor do crédito da Tabela de Preço na disciplina matriculada

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Disciplinas Matriz do aluno** | **Valor do Crédito da Matriz do Aluno** |  | **Disciplina equivalente** **(fora da grade do aluno)** | **Valor do Crédito da Disciplina equivalente** |  | ****Valor do Crédito da Tabela de Preço**** |
| Direito Civil - I | R$110 | Teoria Geral do Direito | R$140 |  | R$190 |
| Direito Civil - II | R$110 |

Turma Livre

Quando os parâmetros **Usar valor do créditos financeiros da matriz curricular do aluno** e **Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de crédito em caso de equivalência múltipla** estiverem marcados, os cenários abaixo terão o mesmo comportamento das regras acima.

* Mesma disciplina em matriz diferente
* Disciplinas diferentes com equivalência
* Disciplinas diferentes com equivalência múltipla

Se os parâmetros estiverem desmarcados o valor do crédito buscará da Turma Livre.

Faixa de Crédito

Quando o parâmetro **Faixa de Crédito** estiver marcado, na matrícula do aluno em disciplinas da sua matriz curricular será utilizado o valor da Tabela de Preço.

Exemplo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Valor do Crédito da Faixa de Crédito** |  | **Valor do Crédito da Tabela de Preço** |
| Introdução ao Direito | R$200 | R$190 |

Caso o aluno estiver matriculado em uma disciplina que estiver associada a uma outra matriz curricular que não seja a dele, o valor do crédito considerado deve ser o informado na disciplina da matriz fora da grade.

Reajuste de Valores

Nos casos que se utiliza uma tabela de preço que houve reajuste no valor das disciplinas, a aplicação do valor das disciplinas no lançamento será feita conforme os critérios de aplicação do reajuste da parcela:

* O sistema irá verificar o período letivo associado ao contrato do aluno para aplicar o reajuste, ou seja, reajustes feito posteriormente não serão considerados. O valor a ser aplicado será buscado na tabela de preço no valor de crédito vigente correspondente àquele período letivo ou ao último reajuste feito até aquele período letivo;
* Para consideração de aplicação dos reajustes em período letivos anteriores, é necessário que o campo **Período letivo anterior** seja preenchido no cadastro de períodos letivos;
* Contratos já firmados antes do período letivo de vigência de um reajuste não vão ter alteração retroativa.

Para mais informações sobre o reajustes acessar o link [Reajuste de Valores na Tabela de Preço](https://tdn.totvs.com/pages/viewpage.action?pageId=1042910853).

Tabela de Preço não será aplicada:

* **Curriculo Individual:** Quando um aluno possui Currículo Individual esse será considerado a matriz oficial do aluno, parametrizando a Tabela de Preço os valores de crédito continuaram considerando a do Curriculo Individual.
* **Parcela Fixa:** Para cobrança por parcela fixa, a tabela de preço não será considerada, mesma regra do calculo por crédito
* **Disciplinas fora da grade:** Quando o aluno estiver matriculado em disciplinas que estiver associada a uma outra matriz curricular o valor do credito não será da Tabela de Preço. Exceção quando se trata da mesma disciplina ou equivalência com os parâmetros marcados **Usar valor do créditos financeiros da matriz curricular do aluno** e **Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de crédito em caso de equivalência múltipla**
