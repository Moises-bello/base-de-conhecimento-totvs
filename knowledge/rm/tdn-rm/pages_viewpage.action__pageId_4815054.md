---
content_hash: 2702837986fbee671b7f979ccd9ca68ea8ff9391f76ddbe3fd65f8ccd6e219b0
fetched_at: '2026-06-29T00:10:19.534974+00:00'
page_id: '4815054'
product: rm
source: tdn-rm
title: Lançamentos - Cobrança por crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4815054
version: 143
---

---

Na matricula do aluno no período letivo ao criar um contrato podemos definir que a cobrança das disciplinas serão por crédito e não por parcelas fixas (parcelas com mesmos valores), abaixo itens que devemos configurar para esse comportamento.

Cadastro do Plano de Pagamento

Cadastrar o plano de pagamento, pois as parcelas deverão ser geradas com valores diferentes do fixo.

Acesse: Financeiro/Contábil / Planos de pagamento (cadastrar) / Anexo / Parcelas do Plano

* O parâmetro “Valor calculado pelo número de créditos” deve estar marcado em cada parcela do plano de pagamento.

Neste exemplo foi criado o plano de pagamento “PLANO – Plano de Cobrança por créditos”, com 6 parcelas que serão calculadas pelo número de créditos do aluno, para o período letivo 2019/2.

Obs: Quando estiver marcado "Valor calculado pelo número de créditos" o valor da parcela ficará como 0,00.

* É necessário indicar quais matrizes aplicadas poderão utilizar este plano de pagamento, as instituições podem criar um plano de pagamento para cada curso, se for de desejo da mesma.

Veja no exemplo abaixo, a matriz aplicada cadastrada no plano de pagamento.

Acesse: Financeiro/Contábil / Planos de pagamento / Anexo / Habilitações do Plano de pagamento.

Número e Valor do Créditos na Matriz Curricular

Devemos parametrizar nas disciplinas da Matriz Curricular, o número de créditos que cada disciplina possui e o valor de cada crédito.  
Acesse: Currículo e Oferta / Matrizes Curriculares / Anexos / Período / Anexos / Disciplinas da Matriz Curricular

As casas decimais do campo **N° de créditos para cobrança**obedecerá o parâmetro contido no **TOTVS Educacional | Parâmetros | Tesouraria | Geral 2/4 → Casas Decimais/Créditos Financ.:**, já as casas decimais do campo **Valor de crédito para cobrança** sempre obedecerá a parametrização definida no **TOTVS Gestão Financeira | Contas a Receber | Manutenção e Lançamentos | Lançamentos | Opções Gerais →****N° Casas Decimais**

Uma mesma disciplina pode estar contida em duas Matrizes Curriculares diferentes, com número de créditos e valores diferentes, por isso, essas informações são cadastradas por matriz curricular e não no cadastro da disciplina.

**Atualizar número e valor de créditos das disciplinas na Matriz Curricular**

Quando o cliente precisa realizar reajuste de valor de disciplina da matriz curricular é possível através do assistente, informando um % ou número e valor de crédito para mais detalhes, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=425459077)

**Sincronizar créditos Financeiros com a Matriz**

Após qualquer alteração realizada nas disciplinas da Matriz é possível através do processo de Sincronizar créditos Financeiro com a Matriz para mais detalhes do processo, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=729224362)

Situação de matricula

A situação de matrícula associada para o aluno nas disciplinas deve estar com o parâmetro “Conta como créditos financeiros (cobrança por crédito)” marcado.

Acesse: Currículo e Oferta / Situação de Matrícula / Aba “Status na disciplina”.

Parâmetro: Dividir valor de créditos entre parcelas do contrato

Utilizaremos o parâmetro “**Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato**” para que o sistema possa somar os créditos das disciplinas em que o aluno esta matriculado, multiplicar por seus respectivos valores e dividir entre as parcelas do contrato.

Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2

Matriculando nas disciplinas da matriz do aluno

Temos um aluno que foi matriculado nas 5 disciplinas do 1º período da **MATRIZ ALUNO**, a situação de matrícula nas disciplinas foi associada como “Matriculado”.

Neste exemplo, o aluno tem 5 disciplinas cadastradas com os mesmos números e valores de créditos e deverá pagar um total de R$ 2.500,00 para cursar as 5 disciplinas do 1º período.

**5 (Nº de Créditos por disciplina) x R$100 por 5 disciplinas inscritas = RS 2.500,00**

* Após matriculado nas disciplinas do período letivo podemos acessar o número do crédito, conforme abaixo:

Acesse: Currículo e Oferta / Alunos / Anexos / Matrícula no período letivo / Anexos / Matrícula em disciplinas

O número de créditos presentes na aba de dados adicionais da matrícula tem origem da matriz curricular da disciplina, o sistema sempre busca esse valor para matricula, salvo parametrizações em **casos de equivalência**.

Quando o aluno já está matriculado, o número de créditos presentes na aba de dados adicionais foi preenchido pela matricula e é esse que é utilizado para o cálculo nas parcelas do contrato.

Caso o mude a parametrização, número de créditos da matriz curricular ou equivalência, o número de créditos na aba de dados adicionais da matrícula deverá ser atualizado, manualmente ou via processo.

Atenção

Caso seja necessário desconsiderar o número de créditos financeiros presente na aba de dados adicionais na matrícula da disciplina do aluno. Será necessário configurar parâmetro "**Desconsiderar nº de créditos na matrícula da disciplina para geração e simulação de lançamento**".

Desta forma, o sistema irá desconsiderar o número de créditos financeiros presente na matrícula da disciplina do aluno calculado durante a matrícula. E irá calcular novamente o número de créditos financeiros para a matrícula da disciplina na geração e simulação do lançamento financeiro vinculado à parcela do contrato do aluno.

Acesse o parâmetro: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2.

Parâmetro disponível a partir dos patches: **12.1.2302.185 e 12.1.2306.130 ou superiores**

Acesse: Currículo e Oferta / Alunos / Anexos / Matrícula no período letivo / Anexos / Matrícula em disciplinas / Aba "Dados adicionais"

Caso um aluno esteja cursando uma disciplina em outra Matriz Curricular que possua um número de créditos e valores diferentes, é possível parametrizar para que o sistema busque na hora da matricula o crédito que desejar (da matriz do aluno ou da matriz que o aluno está cursando a disciplina).   
Para mais informações acesse a aba desse documento em **Parâmetros Crédito da Matriz do aluno**

No exemplo deste aluno, que está cursando a disciplina “Introdução a Ciência do Direito", irá pagar pela disciplina 5 x R$100 = R$500 cursando a disciplina na sua matriz.

* Após a matricula será criado o contrato e podemos então associar o “PLANO – Plano de Cobrança por créditos” no contrato do aluno para o período letivo 2019/2.

Observe que a Matriz Aplicada associada ao contrato é a mesma dos exemplos acima.

Acesse: Currículo e Oferta / Aluno / Anexo / Contratos

* Com o parâmetro “**Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato**” marcado, o sistema soma os créditos das disciplinas em que o aluno esta matriculado, multiplicar por seus respectivos valores e dividir entre as parcelas do contrato.

Temos o contrato com um plano de pagamento que terá um valor total de R$ 2.500 calculado, onde o mesmo deverá ser divido entre 6 parcelas, que foram cadastrados no plano de pagamento.

**5 (Nº de Créditos por disciplina) x R$100 x 5 (disciplinas) =****RS2.500 / 6 (parcelas)= R$ 416,67**

* Vamos gerar então a primeira parcela para esse plano de pagamento, onde ele deverá gerar um valor de R$ 416,67, conforme demonstrado acima.

Acesse: Currículo e Oferta / Aluno / Anexo / Contratos / Anexos / Parcelas / Processo / Gerar Lançamento**.**

Temos a parcela gerada com o valor de 416,67.

Podemos verificar também no cadastro do contrato do aluno, na coluna “Valor Simulado” o valor de cada parcela, antes mesmos de gerar as parcelas.

Obs: O valor real destas parcelas seria R$416,6666...7, porém o sistema arredondou para R$416,67, dando um valor total de R$2500,02, uma diferença de R$0,02. No momento de gerar a última parcela desse contrato, o sistema irá comparar o valor “ simulado” com o valor “real” do contrato, e caso tenha diferença entre os valores, esse valor será aplicado na parcela. O valor gerado da ultima parcela será de R$416,65.

Créditos da Matriz do Aluno

Funcionamento dos parâmetros: **Usar número de créditos financeiros da matriz curricular do aluno /****Usar valor do créditos financeiros da matriz curricular do aluno / **Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de crédito em caso de equivalência múltipla****

*Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2*

Mesma disciplina em matriz diferente

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for de outra matriz curricular e também estiver ofertada na matriz curricular do aluno deverão ser considerados o número de créditos da disciplina matriz do aluno.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for de outra matriz curricular e também estiver ofertada na matriz curricular do aluno deverão ser considerados o valor do créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Introdução a Ciência do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da sua matriz, mas essa disciplina pertence a outra grade.  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da outra grade   
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Disciplinas diferentes com equivalência

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada em outra matriz curricular e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o número de créditos da disciplina matriz do aluno.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada em outra matriz curricular e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o valor do créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Teoria Geral do Direito | 3  \*  150 = 450 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da outra grade que possui equivalência cadastrada com a disciplina da matriz da sua grade.

Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da outra grade   
**3 (Nº de Créditos por disciplina) x R$150 = RS450**

Disciplinas diferentes com equivalência múltipla

Se o parâmetro "**Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de crédito em caso de equivalência múltipla**", o comportamento do sistema deve ser o conforme descrito abaixo:

1. Matricula tem duas disciplinas com equivalência para uma da matriz: o sistema sempre irá considerar o número de crédito e valor do crédito da disciplina da matriz. 

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |  |
   | Português | 5  \*  100 | Redação | 5  \*  100 = 500 | Número de créditos e valor do crédito da disciplina de português |
   |  |  | Comunicação | 0 | A segunda disciplina ficará zerada, pois o valor foi considerado na primeira disciplina equivalente. |
2. Matricula tem uma disciplina com equivalência para duas da matriz: o sistema sempre irá considerar a disciplina com maior número de crédito e a disciplina com maior valor do crédito da matriz do aluno.

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplinas Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplina equivalente (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |  |
   | Redação | 5  \* 500 | Português | 6 \* 500 = 3.000 | Vai prevalecer o maior valor de crédito e o maior número de crédito de cada disciplina equivalente |
   | Comunicação | 6 \* 150 |

Quando os parâmetros para considerar o **n° de crédito e valor de crédito da matriz curricular do aluno** estiver marcado e o sistema não encontre a mesma disciplina na matriz curricular do aluno, ou se o valor da disciplina na matriz do aluno não estiver preenchido, o sistema irá considerar o valor da disciplina matriculada 

Exemplo:

| **Disciplinas Matriz do aluno** | **Nº Crédito x Valor do Crédito** | **Disciplina equivalente (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |  |
| --- | --- | --- | --- | --- |
| Português | 0 | Comunicação | 4 \* 100 = 400 | Mesmo com os parâmetros para considerar o **n° de crédito e valor de crédito da matriz curricular do aluno**, no momento da matrícula, será considerado o valor da disciplina "Comunicação", já que a disciplina "Português" está zerada. |

Faixa de Crédito

Funcionamento do parâmetro **Utilizar Faixa de Crédito e  Utilizar Faixa de Crédito | Usar número de créditos financeiros da matriz curricular do aluno**

Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2

**Utilizar Faixa de Crédito                                                                                                                                                 Utilizar Faixa de Crédito | Usar número de créditos financeiros da matriz curricular do aluno**

|  |  |
| --- | --- |

Mesma disciplina em matriz diferente

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for de outra matriz curricular e também estiver ofertada na matriz curricular do aluno deverão ser considerados o número de créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor da Faixa de Crédito** |  | **Mesma Disciplina (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 1  \*  500 = 500 | Introdução a Ciência do Direito | 3  \*  200 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da sua matriz, mas essa disciplina pertence a outra grade.

Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**1 (Nº de Créditos por disciplina) x R$500 (Valor de Crédito da Faixa de Crédito) = RS500**

Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da outra grade   
**3 (Nº de Créditos por disciplina) x R$200 = RS600**

Disciplinas diferentes com equivalência

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada em outra matriz curricular e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o número de créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor da Faixa de Crédito** |  | **Disciplinas equivalentes (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 1  \*  500 = 500 | Teoria Geral do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da outra grade que possui equivalência cadastrada com a disciplina da matriz da sua grade.

Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**1 (Nº de Créditos por disciplina) x R$500 (Valor de Crédito da Faixa de Crédito = RS500**

Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da outra grade   
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Disciplinas diferentes com equivalência múltipla

Se o parâmetro "**Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno em caso de equivalência múltipla**", o comportamento do sistema deve ser o conforme descrito abaixo:

1. Quando o parâmetro estiver desmarcado e o aluno matriculado a duas ou mais disciplinas equivalentes da disciplina da matriz o valor de crédito cobrado será por disciplina equivalente

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |  |
   | Português | 5  \*  100 | Redação | 5  \*  100 = 500 | Número de créditos e valor do crédito da disciplina de português |
   |  |  | Comunicação | 5  \*  100 = 500 | Número de créditos e valor do crédito da disciplina de português |
2. Quando o parâmetro estive marcado e o aluno matriculado a duas ou mais disciplinas equivalentes da disciplina da matriz o valor de crédito cobrado será somente em uma disciplina equivalente, e as demais terá seu valor de crédito zerado.

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |  |
   | Português | 5  \*  100 | Redação | 5  \*  100 = 500 | Número de créditos e valor do crédito da disciplina de português |
   |  |  | Comunicação | 0 | A segunda disciplina ficará zerada, pois o valor foi considerado na primeira disciplina equivalente. |

   ATENÇÂO

   Esse comportamento do parâmetro está disponível a partir do patch **12.1.28.303**

Para mais informações sobre o cadastro de Faixa de Crédito, [clique aqui.](http://tdn.totvs.com)

Disciplina Equivalência com número de créditos cadastrado como "Zero"

Para os casos em que a disciplina equivalente foi cadastrada como **"Zero"** no número de crédito

Se o parâmetro "**Usar número de créditos financeiros da matriz curricular do aluno**" ou "**Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno em caso de equivalência múltipla**", o comportamento do sistema deve ser o conforme descrito abaixo:

Este cenário se aplica para os casos de **Créditos da Matriz do Aluno ou Faixa de Crédito**:

* Mesma disciplina em matrizes diferentes
* Disciplinas diferentes com equivalência
* Disciplinas diferentes com equivalência múltipla

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina Equivalente** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 0  \*  200 = 0 | Introdução a Ciência do Direito | 3  \*  200 = 600 |

Com apenas um dos parâmetros marcados acima  
**0 (Nº de Créditos por disciplina) x R$200 (Valor de Crédito da Disciplina) = RS0**

Sem algum dos parâmetros marcado acima  
**3 (Nº de Créditos por disciplina)  x R$200 (Valor de Crédito da Disciplina) = RS600**

**Informações Adicionais**

1. **Aumento e Cancelamento de disciplinas**Na matricula do aluno é comum que alunos matriculem em disciplinas após o inicio do período letivo ou cancele a matricula de determinada disciplina, para explicar melhor o comportamento do sistema em relação ao calculo  acesso o documento, .
2. **Parcela fixa em contrato com parcelas calculadas por crédito**Na rematrícula dos alunos, é muito comum que as instituições não saibam em quantas disciplinas o aluno irá se matricular, porém a instituição já deve cobrar do aluno um valor para “garantir” essa rematrícula. Para isso, elas criam uma parcela fixa no contrato, com um determinado valor, e mandam para todos os seus alunos efetuarem o pagamento. Acesse o documento
3. ****Número e Valor de créditos no Currículo Individual e Turma Livre****Para saber sobre o calculo, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=590628080)
