---
content_hash: 61b478d085006e7f231c568e16589d7445af41885b39a4bd6db924f2afe65eed
fetched_at: '2026-06-29T00:10:32.846450+00:00'
page_id: '527855582'
product: rm
source: tdn-rm
title: MIT021 -  SCAE
type: documentation
url: https://tdn.totvs.com/display/LRM/MIT021+-++SCAE
version: 31
---

inicio

|  |  |
| --- | --- |
| Descrição | SCAE |
| Observações | Documentação para detalhar os critérios e regras aplicadas na ferramenta para extração de informações do SGE – Sistema de Gestão Escolar para importação no sistema SCAE.  Versão 27 |

---

4circlepipe

---

# CONSIDERAÇÕES:

Os dados serão gerados mensalmente através do Gerador de Saídas do SGE. O usuário irá informar o mês e ano para extração da produção (mês de referência).   
O critério utilizado para extração dos dados a serem exportados leva em consideração:

1. A **data de início da turma** **menor ou igual ao mês de referência**;
2. Data de **matrícula menor ou igual ao mês de referência**;
3. Data fim da **turma maior o igual ao mês de referência**, quando a situação for (Matriculado ou Inscrito);
4. **Data da mobilidade (Data de Alteração de Matrícula no Período Letivo) maior ou igual ao mês de referência**.

Não serão enviados no arquivo de carga alunos com as situações de matricula na turma iguais a:

* Pré-Matrícula / Pré-Matrícula Online / Pré-Inscrito
* Matricula indeferida (Negada)
* Dependência
* Cancelado\*

Se o mês indicado na data da movimentação da matricula na turma para a situação de Cancelado for igual ou posterior ao mês de início da mesma, a matricula será enviada no arquivo com \*comando de Exclusão.

Modalidade 99 - Ações Educativas

Foi criado a **modalidade 99 – Ações Educativas** no cadastro de curso para ser vinculada em qualquer curso que **NÃO** seja da Educação Básica e nem da Educação Continuada.

*Exemplo:*

* Cursos da SSI
* Cursos de Lazer
* Cursos Extra Curriculares
* Outros

Os cursos, turmas e matriculas que estiverem vinculados a esta modalidade 99 não será gerado nenhuma informação para o SCAE.

Após este filtro inicial é feito uma tratamento especifico para cada informação extraída do SGE. Neste documento estão detalhadas como são extraídas do SGE cada uma das informações geradas no arquivo extraído para reporte ao SCAE.

---

# CONTROLE DE VERSÃO

As atualizações de evolução/correção que ocorrem no extrator são registradas na tabela ZVERSAOSCAE. É possível consultar as atualizações aplicadas no menu *Educacional | Gestão | Gerador de Saída | Anexos | Consultas SQL.*

# ***Novo!*** PAINÉIS DE CENÁRIOS

Os Painéis de Cenários do SCAE são acessados através do módulo Educacional, menu “Gestão | Painéis de Cenários (clicar no ícone)”. Esses cenários apresentam informações de alguns campos da produção histórica enviada para o SCAE. Durante a execução do extrator,  a tabela ZSCAEPRODMES é alimentada com os dados referente ao Mês/Ano de produção.

# HORA-ALUNO

As **matrículas serão enviadas todos os meses** até que tenha uma situação que indique uma saída. Ou seja, independente se houve, ou não, mobilidade, alteração nos campos complementares da matrícula ou alteração na turma, os alunos irão constar na carga. Isso garante que, todos os meses, sejam enviados os dados do novo indicador **Hora-Aluno**.   
A diretriz determina que: para cada aluno, será enviado o **total de horas do mês de referência** de acordo com a soma das **Horas** das disciplinas que ele está matriculado.   
Todos meses as horas dos alunos serão enviadas até que ele tenha uma situação de saída.

* Para o contexto da Nova EJA e EJA Profissionalizante a situação *Em Processo*, *Trancado* e *Transferido de Turma* não caracteriza uma saída do aluno, ele continuará a aparecer na carga até o termino da turma ou que conclua ou seja *Evadido*, *Desistente*, *Falecido* ou *Transferido* *Interno* ou *Externo*.
* Os alunos do ensino regular que a situação de matrícula for *Transferência de Turma* não serão contabilizadas suas horas.
* Para a Hora-Aluno dos "Eventos" (Educação Continuada), o aluno matriculado em algum curso do tipo "Evento" será enviado a Carga Horária da disciplina no mês referente a data final da turma/disciplina. Apenas para alunos com situação "Inscrito" e/ou resultado "Concluinte".
* Para os alunos com matrículas no período letivo com situação “Reconhecimento de Saberes” não será enviado as horas destinadas, somente após o mês em que a situação de matrícula no período letivo for alterada para “Matriculado”.

---

# APURAÇÃO DE RESULTADOS

Com o objetivo de otimizar os esforços no processo de fechamento anual, promovendo a integridade dos registros apurados pelo DN, recomendamos que a apuração de resultados do aluno (indicação das situações das matriculas como Aprovado, Concluinte ou Reprovado), deve ser realizada até o último dia do ano letivo, sendo este, correspondente ao ano de execução da turma. Essa ação garantirá que o status final das situações das matrículas sejam encaminhadas automaticamente no último arquivo de carga para o Sistema SCAE.   
Caso a orientação acima não seja seguida e a apuração de resultado seja executada após o último dia do ano letivo, o Regional deverá submeter duas cargas (Dezembro e prévia de Janeiro). Essa ação no entanto, impactará em esforço adicional na interpretação de críticas no mês de fevereiro (carga de janeiro do ano seguinte), já que a geração dessa carga incluirá informações de matrículas do exercício anterior.

---

# REGRAS PARA EXTRAÇÃO DAS INFORMAÇÕES

Baseado nas regras de importação e análise dos dados do SCAE foram definidas regras para extração dos dados dentro do SGE. Abaixo seguem as orientações para preenchimento das informações e execução das rotinas no SGE tendo como foco, a exportação das informações para o SCAE.

## **Curso:**

Para o SCAE é enviado como curso a junção dos três cadastros no SGE que compõem a Estrutura Curricular 'Curso / Série / Matriz Curricular'. Desta forma, sempre que é criada uma nova Série ou Matriz Curricular dentro da estrutura de um curso, no momento do envio para o SCAE é gerado um novo Código de Curso. (Limitado em 28 caracteres)

## **Unidade:**

Os dados referentes a Unidade de Ensino são extraídos no SGE do cadastro de Filial. Para cada Unidade existe um código que deve ser informado no campo 'Campo Livre 1'. Este código, corresponde ao que já está cadastrado e foi enviado anteriormente ao SCAE pelo regional.   
Caminho para preenchimento do campo***: Filial | Dados Fiscais | Dados Adicionais | Campo Livre 1'***

## **Turma:**

No SGE a Turma vinculada a 'Matricula do Aluno no Período Letivo' é sempre enviada para o SCAE como a turma correspondente a matricula na qual está associada.

* As datas de Início e fim da turma devem sempre ser preenchidas no SGE.
* O nome da Turma no SGE é enviado para o SCAE. É importante que este campo seja preenchido para facilitar a identificação das turmas. Não existe um padrão definido para o preenchimento.
* A Modalidade correspondente será informada na Turma. No SGE a informação deverá ser preenchida no campo 'Tipo de Mediação'. Neste campo deve ser informado se o tipo de modalidade do Curso / Turma ofertada será: Presencial, Semipresencial ou a Distância. É um campo obrigatório e o valor de cada modalidade foi disponibilizado pelo DN. Caminho para preenchimento do campo***: Currículo e Oferta | Oferta | Turma | Tipo de Mediação***

## **Matrícula:**

No SGE para cada registro de Matrícula do Aluno no Período Letivo em uma determinada Turma é contabilizado e enviado para o SCAE um registro novo de matrícula.

Nova EJA e EJA Profissionalizante

Como os “segmentos” de NOVAEJA (Ensino Fundamental Anos Finais e Ensino Médio) e EJAProfissionalizante (Ensino Fundamental Anos Finais e Ensino Médio) foram estruturados no SGE em curso/série para cada matricula do aluno no Período Letivo em uma determinada Turma também será contabilizado e enviado para o SCAE um novo registro de matrícula.

Para os cursos das modalidades EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3), após a atualização do extrator em fevereiro de 2019, a contabilização da matrícula passa a ser baseada na Matrícula de Referência que corresponde a primeira turma que em que o aluno foi matriculado no curso (campo Complementar da Matrícula do Período Letivo que deverá estar preenchido).

Matrículas já enviadas para o SCAE antes da atualização não precisam do campo preenchido.

### **Data da Efetivação da Matricula:**

Para envio da data de efetivação da Matricula temos quatro cenários distintos:

1. Se a data de Matricula for anterior ou igual a data de início da turma: Será enviada como Data de Efetivação da Matricula a Data início da Turma.
2. Para os alunos que tiveram a situação de matricula alterada de 'Reconhecimento de Saberes' para 'Matriculado' e a data de alteração for anterior ou igual a data de início da turma: Será enviada como Data de Efetivação da Matricula a Data início da Turma.
3. Se a data de Matricula for posterior a data de início da turma: Será enviada como Data de Efetivação da Matricula a data informada no campo 'Data da Matricula' na tela de matricula no período letivo.
4. Para os alunos que tiveram a situação de matricula alterada de 'Reconhecimento de Saberes' para 'Matriculado' e a data de alteração for posterior a data de início da turma: Será enviada como Data de Efetivação da Matricula a data de alteração registrada no log de matricula no período letivo.

EJA

Devido a matricula de referência, para os cursos das modalidades EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3), após a atualização do extrator em fevereiro de 2019, a data da efetivação será extraída da matrícula de referência.

### **Data da Mobilidade do Estudante:**

Sempre que há uma alteração na Situação de Matricula do Aluno, ao gerar o arquivo para envio da produção no mês em que a alteração foi realizada, será enviado ao SCAE a Data de Mobilidade do Estudante respeitando os seguintes critérios:

**Situações de Resultado: Aprovado / APL / AEP / Reprovado / EPI / Concluinte**

Será reportado como Data da Mobilidade do Estudante a Data de Alteração registrada no log da matrícula do período letivo quando for menor que a Data Final da Turma que está vinculada a Matrícula do Aluno no Período Letivo. Caso contrário, será enviado a Data Final da Turma.

EJA

Devido a matricula de referência, para as modalidades EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3), a situação de *Aprovado* será verificado se o aluno possui matrícula em todas as séries associadas ao curso e se estas estão com status de resultado final *Aprovado*. Este status e a data da mobilidade serão extraídas da matrícula vinculada à última série associada ao curso. Lembrando que para a Data Final da Turma é considerado o campo complementar SMATRICPLCOMPL.DTTERMINO conforme mencionando anteriormente.

**Situações de Matricula: Evadido / Desistente / Transferência**

Será reportado como Data da Mobilidade do Estudante a Data exata em que a alteração da Situação de Matricula foi executada no SGE (informação extraída do Log de Movimentação do aluno) ou, do campo complementar 'Data da Mobilidade do Estudante' caso o mesmo esteja preenchido.

EJA

Devido a matricula de referência, para as modalidades EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3), a situação de *Transferência de Turma* (31) não é enviada como uma mobilidade para a matrícula do aluno.

Atenção

O campo Data da Mobilidade do Estudante tem por objetivo possibilitar que o regional faça a correção da informação gerada pelo log de movimentação, em casos onde o usuário responsável na escola fez a mudança da Situação de Matrícula no sistema SGE em uma data divergente a que de fato aconteceu.

### **Situações de Matrícula:**

Abaixo segue uma tabela com a Situação de Matrícula no SGE e a Situação Correspondente no SCAE:

***Nível de Ensino: Educação Básica***   
**Situação de Matrícula Aplicada a Matrícula na Turma (Matrícula no Período Letivo)**

|  |  |
| --- | --- |
| ***Código - Situação de Matrícula SCAE*** | ***Código - Situação de Matrícula SGE*** |
| 1 – Matriculado | 2 - Matriculado |
| 5 – Trancamento | 5 - Trancado |
| 9 – Evasão | 7 - Evadido |
| 11 – Promoção/Aprovação | 9 - Aprovado |
| 13 – Reprovado | 10 - Reprovado / 11 – Reprovado por Frequência |
| 18 – Transferência Externa | 3 - Transferência Externa / 33 – Transferência Externa (Somente PR) |
| 19 – Transferência Interna | 30 - Transferência Interna (PR não entra) / 32 – Transferência Escola (Somente PR) |
| 20 – Transferência de Turma | 31 - Transferência de Turma |
| 21 – Desistente | 6 - Desistente |
| 22 – Falecido | 45 – Falecido / 30 – Falecido (Somente PR) |
| 23 – Reclassificado | 32 - Reclassificado / 78 - Reclassificado (Somente PR) |
| 24 – Reconhecimento de Saberes | 70 - Reconhecimento de Saberes |
| 53 - APL | 123 - APL |
| 54 - AEP | 124 - AEP |
| 55 - EPI | 125 - EPI |

Novo Ensino Médio

Situações de Resultado no Período Letivo especificas para o Novo Ensino Médio:

* APL - Aprovado no Ano Letivo
* AEP - Aprovado no Ano Letivo, mas Em Processo
* EPI - Em Processo no mesmo ano, com intervenção permanente

  \***Situação de Matricula Aplicada a Disciplina (NOVA EJA e EJA Profissionalizante)**

|  |  |
| --- | --- |
| ***Código - Situação de Matricula SCAE*** | ***Código - Situação de Matricula SGE*** |
| 1 – Matriculado | 2 - Matriculado |
| 12 – Concluinte | 9 - Aprovado |
| 26 – Competência Certificada | 72 - Competência Certificada |
| 27 – Dispensado | 14 - Dispensado |

EJASerá enviada ao SCAE a situação dos alunos nas disciplinas apenas para os cursos da NOVA EJA e da EJA Profissionalizante. As disciplinas dos demais cursos não serão reportadas.ImportantePara as modalidades EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3) após a atualização do Extrator em fevereiro de 2019, a situação *Matriculado* será identificada a partir da matrícula de referência do aluno.

***Nível de Ensino: Educação Continuada***

|  |  |
| --- | --- |
| ***Código - Situação de Matricula SCAE*** | ***Código - Situação de Matricula SGE*** |
| 1 – Matriculado | 39 - Matriculado |
| 9 – Evasão | 67 - Evadido |
| 12 – Concluinte | 42 – Concluinte |
| 13 – Reprovado | 43 - Reprovado |
| 17 – Participante | 66 - Inscrito |
| 18 – Transferência Externa | 68 - Transferência Externa |
| 19 – Transferência Interna | 69 - Transferência Interna |
| 20 – Transferência de Turma | 46 - Transferência de Turma |
| 21 – Desistente | 41 - Desistente |
| 22 – Falecido | 73 - Falecido |

### **Competências/Disciplinas da NOVA EJA e EJA Profissionalizante**

As informações de mobilidade (Situação de Matrícula aplicada a Disciplina) e Tipo de Avaliação referente as competências/disciplinas associadas as matrículas dos cursos da NOVA EJA e da EJA Profissionalizante serão reportadas para o SCAE. Os seguintes pontos de atenção devem ser considerados:

* As matrículas com situação igual a 'Reconhecimento de Saberes' serão enviadas ao SCAE de acordo com a matrícula de referência.
* Serão reportadas todas as Competências/Disciplinas do aluno no mês de mobilidade da matrícula e quando atingir a situação de *Aprovado* ou *Competência Certificada*.
* Para cada Competência/Disciplina, será enviado o Tipo de Avaliação Correspondente:
  + Para matrículas em disciplinas com situação: Competência Certificada
    - Tipo de Avaliação = 2
  + Para matrículas em disciplinas com situação: Matriculado / Aprovado
    - Tipo de Avaliação = 1

As disciplinas serão enviadas apenas se houver o preenchimento do campo complementar '*Código Disciplinas SCAE'* dentro da Disciplina da Matriz Curricular.

### **Retorno de Alunos na Educação Continuada – Matrícula Isolada**

No processo de Matrícula existem casos de alunos/participantes que retornam no mesmo período letivo para se matricular no mesmo Curso/Evento. Para estas situações de retorno deve ser cadastrada no SGE uma Matrícula Isolada permitindo que o aluno/participante se inscreva/matricule novamente na mesma Ação Educativa. Neste caso onde a Matrícula Isolda é realizada no SGE um novo registro de Matrícula é incluído no arquivo pelo Extrator para envio ao SCAE.

Neste cenário seguem os pontos de especificidade que diferem dos demais cenários:   
***Data de Efetivação da Matrícula:***

1. Se a data de Matrícula for anterior ou igual a data de início da turma: Será enviada como Data de Efetivação da Matrícula a Data início da Turma.
2. Se a data de Matrícula for posterior a data de início da turma: Será enviada como Data de Efetivação da Matrícula a data informada no campo 'Data da Alteração' na tela de Matrícula Isolada (Aba: Dados Adicionais), caso não esteja preenchido será enviado a data do campo 'Data da Matrícula'.

***Data da Mobilidade do Estudante e Código da Situação:*** A data da mobilidade e o código da situação serão extraídos do histórico de alterações da Matrícula Isolada. O extrator irá identificar a última movimentação realizada no mês que está sendo passado no parametro para geração do arquivo.

**Turma:** A turma enviada será a associada a turma disciplina onde o aluno está matriculado.

**Demais informações preenchidas nos campos complementares da Matrícula:** A informações tais como: EBEP, Vira Vida, Categoria... serão extraídas da matrícula no período letivo associada ao mesmo período letivo / curso / série da matrícula isolada.

ImportanteA Matrícula Isolada so deve ser criada no SGE quando a Matricula no Período Letivo correspondente já tiver sido finalizada.

### **Pontos de Atenção da Matrícula**

Utilização de algumas das situações de matrícula disponíveis devem ser utilizadas no SGE:

* + *Situação Cancelado:* A Matrícula do aluno deve ser colocada como cancelada se o cancelamento for feito antes do início da turma. Após o primeiro dia de aula registrado no SGE, em caso de o aluno formalizar a interrupção do curso este, deve ser colocado como desistente.

* + *Situação Desistente:* O Aluno deve ser colocado no SGE como desistente quando a saída dele durante o andamento do curso for formalizada.

* + *Situação Evadido:* A situação de evadido deve ser aplicada quando os responsáveis (Professores e Coordenadores) tiverem certos de que o aluno saiu do curso sem formalizar e que não irá retornar por isso, a orientação que esta atualização de situação seja feita no encerramento da Turma.

ImportanteA Mobilidade do aluno é extraída do 'log de movimentação da matrícula. O Extrator identifica se houve e qual a movimentação do aluno no mês da carga e faz o envio no arquivo ressaltando que, no SGE não é possível manipular a informação gerada pelo log (a data em que a alteração foi realizada ou a exclusão do registro da alteração). É enviado sempre situação correspondente a última movimentação (Situação de Matrícula) identificada no mês da carga.

* + *Dependência:* As matrículas registradas no SGE onde o aluno está cumprindo Dependência não serão reportadas para o SCAE. Para identificar estas matrículas o campo Situação De Matrícula no Período Letivo deve estar com a Situação de Matricula '**Dependência'**.

Todos os campos que são obrigatórios para o Reporte de Produção ao SCAE, listados no documento ***'Checklist SCAE - Campos para preenchimento SGE\_V2'*** devem ser preenchidos no momento em que a matricula do aluno é realizada no SGE.

## **Hora-Aluno**

Para que o indicador de HORA-ALUNO seja exportado, é necessário que as turmas/disciplinas que o aluno esteja matriculado tenha o tipo de turma definido como presencial, semipresencial ou a distância.

20%

**Tipo Presencial:**   
As horas serão extraídas por meio do plano de aula da turma/disciplina, apuradas mensalmente, até a saída do aluno.

40%

**Tipo Semipresencial**:   
Carga horária presencial: As horas serão extraídas por meio do plano de aula da turma/disciplina, apuradas mensalmente, até a saída do aluno.   
+ (mais)  
Carga horária à distância: As horas a distância serão extraídas no último mês da turma/disciplina. Nesse último mês será calculada a carga horária total da disciplina e subtraído da carga horária presencial geral (soma do plano de aula)   
Para o aluno cuja saída foi registrada antes do término da turma/disciplina, somente as horas presenciais realizadas até o mês apurado devem ser consideradas.

40%

**Tipo A distância (100% EAD):**   
As horas serão extraídas a partir do rateio da carga horária total da (s) disciplina (s) que o aluno está matriculado nos meses de duração da disciplina, durante o período que o aluno estiver em andamento. A partir do registro de saída, somente as horas das disciplinas realizadas até o mês apurado devem ser consideradas.   
Caso o aluno conclua a disciplina antes do prazo da turma/disciplina, a carga horaria integral da disciplina deverá ser considerada.

Para os tipos de ação "Eventos" (Educação Continuada), o extrator enviará a carga horária total da disciplina no último mês da Turma/ Disciplina

.

# CAMPOS COMPLEMENTARES CRIADOS PARA ATENDER AO SCAE

Importante

Os campos complementares cuja origem dos dados não é proveniente de uma **tabela referencial disponibilizada pelo Departamento Nacional** estarão no SGE em branco para que o usuário no regional preencha a informação solicitada

| Tabela | Campo | Descrição |
| --- | --- | --- |
| **SHABILITACAOCOMPL** | CODSERVICOSCAE | Tabela Dinâmica.  O objetivo deste campo é identificar o código do Produto/Serviço (SCAE). O preenchimento deste campo é obrigatório para Cursos e Açõ{es Educativas (Cursos e Eventos Educativos). Tabela referencial disponibilizada pelo Departamento Nacional. |
| CODTIPOPORTFOLIO | Tabela Dinâmica.  Este campo foi criado com o objetivo de identificar se a Ação Educativa (Curso ou Evento Educativo), pertence a um Portfólio (Nacional ou Regional) ou não.  Se enviar 1 - pertence ao Portfólio.  Se enviar 2 - não pertence ao portfólio. |
| TIPOPORTIFOLIO | Tabela Dinâmica.  Este campo foi criado com o objetivo de identificar se a Ação Educativa (Cursos e Eventos Educativos) pertence ao portfólio Nacional ou Regional Homologado. Este campo será utilizado como filtro para determinar se o extrator de dados para envio da produção irá buscar o código do campo: CODPORTIFOLION ou CODPORTIFOLIOR.  ***Atenção:*** *Esta informação não será enviada ao SCAE.* |
| CODPORTIFOLION | Tabela dinâmica  Para Ações Educativas (Cursos e Eventos Educativos) cujo portfolio é do tipo Nacional, este campo deve ser preenchido informando o código no Portfólio Nacional de acordo com a tabela referencial disponibilizada pelo Departamento Nacional. A informação (Código) será enviada ao SCAE exatamente como inserida pelo usuário no SGE. |
| CODPORTIFOLIOR | Para Ações Educativas (Cursos e Eventos Educativos) cujo portfolio é do tipo Regional, este campo deve ser preenchido informando o código no Portfólio Regional de acordo com uma tabela que deve ser alimentada pelo Departamento Regional. A informação (Código) será enviada ao SCAE exatamente como inserida pelo usuário no SGE. |
| CODCURSOSCAE | Este campo foi criado para identificar os cursos que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCAE. Para estes cursos anteriormente enviados, o Código do Curso no SCAE deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado. Para os novos Cursos e Ações Educativas (Cursos e Eventos Educativos) o campo não deve ser preenchido. |
| **SDISCGRADECOMPL** | DISCEJA | O campo dispõe de uma tabela dinâmica criada para identificar os códigos das disciplinas de acordo com a tabela de referência do Departamento Nacional. Sendo necessário apenas para os cursos das modalidades Nova EJA (8) e EJA Profissionalizante (7). |
| **STURMACOMPL** | EMPRESAP | Neste campo deve ser informada a instituição parceira. O campo dispõe de uma tabela dinâmica onde devem ser cadastradas pelo regionais as empresas informando: CNPJ + Nome da Empresa |
| CODTURMASCAE | Este campo foi criado para identificar as turmas que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCAE. Para estas turmas anteriormente enviadas, o campo código da turma no SCAE deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCAE. Para as turmas que se iniciaram o reporte para o SCAE via SGE o campo deve estar vazio |
| **SMATRICPLCOMPL** | EBEP | Neste campo deve ser informado se a matricula corresponde a um curso articulado entre SESI e SENAI (Educação básica e profissional). (0 - não; 1 - sim) |
| TEMPOINTEGRAL | Neste campo deve ser informado se a matricula é de tempo integral ou não. (0 - não; 1 - sim) |
| VIRAVIDA | Este campo é utilizado para informar se a Matricula / Aluno fazem parte do programa Vira Vida. (0 - não; 1 - sim) |
| CODFINANC | Tabela Dinâmica  O objetivo deste campo é informar o tipo de financiamento correspondente a matricula: Se Gratuidade Regulamentar, Gratuidade Não Regulamentar ou Pago. A tabela referencial foi disponibilizada pelo Departamento Nacional. |
| CATEGORIA | Tabela Dinâmica  Neste campo deve ser informada a Clientela/Vinculo. A tabela de categorias para seleção, foi disponibilizada pelo Departamento Nacional. |
| NOMEEMPRESA | O nome da empresa vinculada a matricula do aluno deve ser informado neste campo. 'Razão Social da Empresa Vinculada' |
| TIPODOCUMENTO | Este campo foi criado com o objetivo de identificar o documento a ser informado é um CNPJ ou CEI. Esta informação será utilizada como filtro para validar se o extrator de dados irá buscar a informação do campo: CNPJEMPRESA ou CEIEMPRESA.  ***Atenção:*** *Esta informação não será enviada ao SCAE.* |
| CNPJEMPRESA | O CNPJ da empresa vinculada a matricula do aluno deve ser informado neste campo. Caso a empresa tenha CEI e não CNPJ, a informação deve ser preenchida no campo 'CEI da Empresa Vinculada'. |
| CEIEMPRESA | O CEI da empresa vinculada a matricula do aluno deve ser informado neste campo. Caso a empresa tenha CNPJ e não CEI a informação deve ser preenchida no campo 'CNPJ da Empresa Vinculada'. |
| CODMATRICULASCAE | Este campo foi criado para identificar as matriculas que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCAE. Para estas matriculas anteriormente enviados, o código da Matricula no SCAE deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCAE. Para as matriculas iniciadas no SGE o campo não deverá ser preenchido. |
| DTTERMINO | Este campo foi criado com o intuito de identificar, na matrícula de referência, a previsão de finalização do curso para as modalidades: EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3).  Será enviada como a Data Fim da Turma. |
| MATRICREFE | Este campo foi criado para identificar a matrícula de referência do aluno para os cursos da modalidade EJA Ensino Fundamental Anos Iniciais (3), EJA Ensino Fundamental Anos Finais (3) e EJA Ensino Médio (3). Essa informação indica a primeira matrícula do aluno no curso e a turma associada à essa matrícula será a referência para o SCAE. |
| CMOBEST | Este campo "Data da Mobilidade do Estudante" foi criado para registrar a data real da alteração da situação de matricula do aluno caso ela tenha ocorrido em data diferente da data que foi executada no SGE. Se a data da alteração da situação for a mesma da data da execução do SGE será utilizado a Data de Alteração de Log da Matricula no Período Letivo (SLOGPLETIVO.DTALTERACAO). (Detalhes das situações na pag. 18 - Nome do Campo: Data da movimentação) |
| **SALUNOCOMPL** | CODALUNOSCAE | Este campo foi criado para identificar os alunos que já haviam sido reportados pelo DR antes do primeiro reporte de produção utilizando o SGE para o SCAE. Para estes alunos anteriormente enviados, o código do Aluno no SCAE deve ser preenchido com o mesmo código reportado anteriormente através do sistema legado para o SCAE. Para os alunos reportados pela primeira vez via SGE o campo deve estar vazio. |
| NIT | Neste campo deve ser informado o número do NIT (PIS.PASEP) do aluno. |
| **ZSCAEMUNICIPIO** | | **Tabela de de-para: Município**  Os códigos dos municípios estão disponíveis na tabela de apoio disponibilizada pelo Departamento Nacional. |

# ORIGEM DOS DADOS

Abaixo segue o detalhamento dos campos / tabelas do SGE dos quais os dados serão extraídos.  Em caso de necessidade de alteração dos campos/tabelas de onde a informação é extraída do SGE por motivo de correção, o ajuste do extrator será feito pela TOTVS e a documentação atualizada. Para os casos onde a necessidade de ajuste for em decorrência de alteração na regra de negócio, a demanda será considerada como alteração de escopo.

Modalidades da EJA

Código: 3 = EJA  
Código: 7 = EJA Profissionalizante  
Código: 8 = Nova EJA

 Clique em cima de cada item para visualizas os campos e as tags:

1horizontal1UFhorizontal

**UF:****1 - Nome do Campo:** Unidade  
**Tabela:** GCOLIGADA.ESTADO  
**Tag:** <uf>

2Curso

**Curso:**2 - Nome do Campo: **Código do Curso**  
Campo Registro: SHABILITACAOCOMPL.CODCURSOSCAE. Se não tiver preenchido: SCURSO.CODCURSO + SGRADE.CODHABILITACAO + SGRADE.CODGRADE  
Tag: <codCurso> (limitado a 28 caracteres)

**2 -** Nome do Campo:  **Código do Curso (modalidade de código 3).**  
Campo Registro: SHABILITACAOCOMPL.CODCURSOSCAE. Se não tiver preenchido: SCURSO.CODCURSO + SOMA DA CARGA HORÁRIA DA ÚLTIMA MATRIZ DE CADA SÉRIE  
Tag: <codCurso> (limitado a 30 caracteres)

**3 -** Nome do Campo:  **Código do Serviço**Tabela: Campo complementar Código Serviço SCAE **- >** SHABILITACAOCOMPL.CODSERVICOSCAE  
*Tabela dinâmica de acordo com as tabelas de apoio do DN.*Tag: <codServico>

**4 -** Nome do Campo: **Código Tipo Portfólio**  
Tabela: Código Tipo Portfólio -> SHABILITACAOCOMPL.CODTIPOPORTIFOLIO  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: < codTipoPortfolio>

**4 -** Nome do Campo: **Código Tipo Portfólio (modalidade de código 3).**  
Tabela: Código Tipo Portfólio -> SHABILITACAOCOMPL.CODTIPOPORTIFOLIO extraído da matrícula de referência do aluno.  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: < codTipoPortfolio>

**5 -**Nome do Campo: **Código Portfólio**

Tabela:   
Quando campo TIPORTIFOLIO for igual a N busca do campo: SHABILITACAOCOMPL.CODPORTIFOLION  
Quando campo TIPORTIFOLIO for igual a R busca do campo: SHABILITACAOCOMPL.CODPORTIFOLIOR   
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: < codPortfolio>

**6 -** Nome do Campo: **Nome do curso**  
Tabela: Nome do Curso -> SCURSO.NOME  
Tag: <nomCurso> (limitado a 256 caracteres)

**7 -** Nome do Campo: **Descrição do curso**  
Tabela: Nome do Curso -> SCURSO.NOME  
Tag: <desCurso> (limitado a 256 caracteres)

**8 -** Nome do Campo: **Carga horária hora**  
Tabela: Carga Horária da Matriz Curricular -> SGRADE.CARGAHORARIA ( Em hora )  
Tag: <numCargaHorariaHora>

**8 -** Nome do Campo: **Carga horária hora (modalidade de código 3).**  
Tabela: Carga Horária da Matriz Curricular -> Soma da Carga Horária (SGRADE.CARGAHORARIA) em horas da última grade de cada série.  
Tag: <numCargaHorariaHora> (limitado a 4 dígitos/10 caracteres)

**9 -** Nome do Campo: **Carga horária minuto**  
Tabela: Carga Horária da Matriz Curricular -> SGRADE.CARGAHORARIA (Em minutos )  
Tag: <numCargaHorariaMinuto>

**9 -** Nome do Campo: **Carga horária minuto (modalidade de código 3).**  
Tabela: Carga Horária da Matriz Curricular -> Soma da Carga Horária SGRADE.CARGAHORARIA em minutos da última grade de cada série.  
Tag: <numCargaHorariaMinuto>

**10 -** Nome do Campo: **Descrição do centro de responsabilidade**  
Tabela: Enviar Fixo ‘CR’  
Tag: <desCentroResp> (limitado a 100 caracteres)

**11 -** Nome do Campo: **Indicador se o curso está ativo ou inativo (0 – inativo; 1 – ativo)**  
Tabela: Status da Matriz Curricular -> SGRADE.STATUS  
Tag: <indAtivo>

**11 -** Nome do Campo: **Indicador se o curso está ativo ou inativo (0 – inativo; 1 – ativo) (modalidade de código 3).**  
Tabela: Status da Matriz Curricular -> SGRADE.STATUS. Será enviado sempre ATIVO (1).  
Tag: <indAtivo

3Unidade

**Unidade:**

**12 -** Nome do Campo: **Código da Unidade (Filial)**  
Tabela: ‘Campo Livre 1’, se vazio busca o código da Filial -> DFILIAL.CAMPOLIVRE1, caso vazio traz GFILIAL.CODFILIAL  
“No Campo Livre 1 da Filial deve ser informado o código da Filial na base de Ativos do DN (OBA)”  
Tag: <codUnidade>

4Turma

**Turma:**

**13.** Nome do Campo: **Código da Turma no sistema DR**  
Enviar: Código do campo complementar, se vazio busca Filial + Turma + Período Letivo. STURMACOMPL.CODTURMASCAE. Se não preenchido envia: STURMA.CODFILIAL+ STURMA.CODTURMA + STURMA.CODPERLET  
Tag: <codTurma> (limitado a 30 caracteres)

**13.** Nome do Campo: **Código da Turma no sistema DR (modalidade de código 3).**  
Enviar: Código do campo complementar, se vazio busca Filial + Turma + Período Letivo. STURMACOMPL.CODTURMASCAE. Se não preenchido envia: STURMA.CODFILIAL+ STURMA.CODTURMA + STURMA.CODPERLET extraídos da primeira turma associada à matrícula de referência do aluno.  
Tag: <codTurma> (limitado a 30 caracteres)

**14.** Nome do Campo: **Código da modalidade**  
Tabela: STURMA.TIPOMEDIACAO  
Tag: <codModalidade>

**14.** Nome do Campo: **Código da modalidade (modalidade de código 3).**  
Tabela: STURMA.TIPOMEDIACAO extraídos da primeira turma associada à matrícula de referência do aluno.  
Tag: <codModalidade>

**15.** Nome do Campo: **Nome da Turma**  
Enviar: Nome da Turma, se vazio envia o código. STURMA.NOME  
Se não preenchido envia: STURMA.CODTURMA  
Tag: <nomTurma>

**15.** Nome do Campo: **Nome da Turma (modalidade de código 3).**  
Enviar: Nome da Turma, se vazio envia o código. STURMA.NOME  
Se não preenchido envia: STURMA.CODTURMA   
Informação extraída da primeira turma associada à matrícula de referência do aluno.  
Tag: <nomTurma>

**16.** Nome do Campo: **Data de Inicio da Turma**  
Tabela: STURMA.DTINICIAL  
Tag: <datInicio>

**16.** Nome do Campo: **Data de Início da Turma (modalidade de código 3).**  
Tabela: STURMA.DTINICIAL  
Informação extraída da primeira turma associada à matrícula de referência do aluno.  
Tag: <datInicio>

**17.** Nome do Campo: **Data de término da turma**  
Tabela: STURMA.DTFINAL  
Tag: <datTermino>

**17.** Nome do Campo: **Data de término da turma (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.DTTERMINO  
Informação extraída do campo complementar da matrícula no período letivo de referência do aluno  
Tag: <datTermino>

**18.** Nome do Campo: **Número de vagas**  
Tabela: STURMA.MAXALUNOS  
Tag: <numVagas>

**18.** Nome do Campo: **Número de vagas (modalidade de código 3).**  
Tabela: STURMA.MAXALUNOS  
Informação extraída da primeira turma associada à matrícula de referência do aluno.  
Tag: <numVagas>

**19.** Nome do Campo: **CNPJ da Instituição parceira**  
Tabela: STURMACOMPL.EMPRESAP   
Tag: <cnpjInstituicaoParceira>

**19.** Nome do Campo: **CNPJ da Instituição parceira (modalidade de código 3).**  
Tabela: STURMACOMPL.EMPRESAP  
Informação extraída da primeira turma associada à matrícula de referência do aluno.  
Tag: <cnpjInstituicaoParceira>

5Matrícula

**Matrícula:**

**20.** Nome do Campo: **Código da matrícula no sistema do DR**  
Tabela: Código do campo complementar, se vazio, ID da Turma + Registro Acadêmico. SMATRICPLCOMPL.CODMATRICULASCAE Se não preenchido envia: STURMA.IDFT + SALUNO.RA  
Tag: <codMatricula> (limitado a 30 caracteres)

**20.** Nome do Campo: **Código da matrícula no sistema do DR (modalidade de código 3).**  
Tabela: Código do campo complementar, se vazio, ID da Turma + Registro Acadêmico. SMATRICPLCOMPL.CODMATRICULASCAE. Se não preenchido envia: STURMA.IDFT + SALUNO.RA  
Informação extraída da matrícula de referência do aluno.  
Tag: <codMatricula> (limitado a 30 caracteres)

**21.** Nome do Campo: **Indicador EBEP (0 – não; 1 – sim)**  
Tabela: SMATRICPLCOMPL.EBEP  
Tag: <indEbep >

**21.** Nome do Campo: **Indicador EBEP (0 – não; 1 – sim) (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.EBEP  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <indEbep >

**22.** Nome do Campo: **Indicador Tempo Integral (0 – não; 1 – sim)**  
Tabela: SMATRICPLCOMPL.TEMPOINTEGRAL  
Tag: <indTempoIntegral>

**22.** Nome do Campo: **Indicador Tempo Integral (0 – não; 1 – sim) (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.TEMPOINTEGRAL  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <indTempoIntegral>

**23.** Nome do Campo: **Indicador ViraVida (0 – não; 1 – sim)**  
Tabela: SMATRICPLCOMPL.VIRAVIDA  
Tag: <IndViravida >

**23.** Nome do Campo: **Indicador ViraVida (0 – não; 1 – sim) (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.VIRAVIDA  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <IndViravida >

**24.** Nome do Campo: **Código do Financiamento**   
Tabela: SMATRICPLCOMPL.CODFINANC   
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: <codFinanciamento>

**24.** Nome do Campo: **Código do Financiamento (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.CODFINANC   
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <codFinanciamento>

**25.** Nome do Campo: **Código da Escolaridade**   
Tabela: Criar de-para com a escolaridade conforme tabela de apoio.  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: <codEscolaridade>

**25.** Nome do Campo: **Código da Escolaridade (modalidade de código 3).**  
Tabela: Criar de-para com a escolaridade conforme tabela de apoio.  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <codEscolaridade>

**26.** Nome do Campo: **Código da Situação**   
Tabela de De-para Situação Matrícula.  
Tag: <codSituacao>

**27.** Nome do Campo: **Código do vínculo**   
Tabela: SMATRICPLCOMPL.CATEGORIA  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Tag: <codVinculo>

**27.** Nome do Campo: **Código do vínculo (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.CATEGORIA  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <codVinculo>

**28.** Nome do Campo: **Data da efetivação da matrícula (yyyy-mm-dd)**  
Tabela: Se a data de Matricula for anterior ou igual a data de início da turma envia a Data início da Turma;

Para os alunos que tiveram a situação de matricula alterada de ‘Reconhecimento de Saberes’ para ‘Matriculado’ e a data de alteração for anterior ou igual a data de início da turma envia a Data início da Turma;  
Se a data de Matricula for posterior a data de início da turma envia a data informada no campo (SMATRICPL.DTMATRICULA);  
Para os alunos que tiveram a situação de matricula alterada de ‘Reconhecimento de Saberes’ para ‘Matriculado’ e a data de alteração for posterior a data de início da turma envia a data informada no campo (SLOGPLETIVO.DTALTERACAO);  
Se Matricula Isolada envia a data informada no campo Data de Alteração (SMATRICULA.DTALTERACAO), se não estiver preenchido envia o campo Data de Matricula (SMATRICULA.DTMATRICULA.

Tag: <datEfetivacaoMatricula>

**28.** Nome do Campo: **Data da efetivação da matrícula (yyyy-mm-dd) (modalidade de código 3).**  
Tabela: Se a data de Matricula for anterior ou igual a data de início da turma envia a Data início da Turma;

Para os alunos que tiveram a situação de matricula alterada de ‘Reconhecimento de Saberes’ para ‘Matriculado’ e a data de alteração for anterior ou igual a data de início da turma envia a Data início da Turma;  
Se a data de Matricula for posterior a data de início da turma envia a data informada no campo (SMATRICPL.DTMATRICULA);  
Para os alunos que tiveram a situação de matricula alterada de ‘Reconhecimento de Saberes’ para ‘Matriculado’ e a data de alteração for posterior a data de início da turma envia a data informada no campo (SLOGPLETIVO.DTALTERACAO);  
Informação extraída da matrícula de referência do aluno.

Tag: <datEfetivacaoMatricula>

**29.** Nome do Campo: **Data da efetivação reconhecimento (yyyy-mm-dd)**  
Tabela: Buscar a data de quando a situação foi alterado para Reconhecimento de Saberes (SLOGPLETIVO.DTALTERACAO)  
Tag: <datEfetivacaoReconhecimento>  
Informação extraída da matrícula de referência do aluno.

**30.** Nome do Campo: **Data da movimentação**  
Tabela: Se já tiver a situação de resultado como Aprovado, APL, AEP, Concluinte, Reprovado ou EPI envia a data final da turma (STURMA.DTFINAL).

Se a situação de matrícula for Matriculado, Inscrito ou Reconhecimento de Saberes envia a data da efetivação da matrícula (SLOGPLETIVO.DTALTERACAO). Se o campo SLOGPLETIVO.DTALTERACAO for menor que a data de início da turma envia a data de início da turma.  
Para as demais situações de matricula envia a data da alteração da matricula registrada no log de movimentação ou a informação preenchida no campo ‘Data da Mobilidade do Estudante’ caso o mesmo esteja preenchido. (SLOGPLETIVO.DTALTERACAO ou SMATRICPLCOMPL.CMOBEST)

Tag: <datMovimentacao>

**31.** Nome do Campo: **Indicador de exclusão da matrícula (0 – não exclui; 1 – exclui)**  
Tabela: Regra condicionada ao cancelamento da matricula descrita na Pág.1   
Tag: <indExclusao>

**31.** Nome do Campo: **Indicador de exclusão da matrícula (0 – não exclui; 1 – exclui) (modalidade de código 3).**  
Tabela: Regra condicionada ao cancelamento da matricula descrita na Pág.1 . e considerar apenas para matrícula de referência.  
Tag: <indExclusao>

**32.** Nome do Campo: **CNPJ da empresa ao qual o estudante é vinculado (quando Trabalhador/Dependente da Indústria e Comunidade por Demanda da Indústria)**  
Tabela:   
Quando campo TIPODOCUMENTO for igual a CEI busca do campo: SMATRICPLCOMPL.CEIEMPRESA,   
Quando campo TIPODOCUMENTO for igual a CNPJ busca do campo: SMATRICPLCOMPL.CNPJEMPRESA  
Tag: <numCnpjVinculo>

**32.** Nome do Campo: **CNPJ da empresa ao qual o estudante é vinculado, quando Trabalhador/Dependente da Indústria e Comunidade por Demanda da Indústria (modalidade de código 3).**  
Tabela:   
Quando campo TIPODOCUMENTO for igual a CEI busca do campo: SMATRICPLCOMPL.CEIEMPRESA,   
Quando campo TIPODOCUMENTO for igual a CNPJ busca do campo: SMATRICPLCOMPL.CNPJEMPRESA  
Informações extraídas dos campos complementares da matrícula de referência do aluno.  
Tag: <numCnpjVinculo>

**33.** Nome do Campo: **Razão Social da empresa vínculo**  
Tabela: SMATRICPLCOMPL.NOMEEMPRESA  
Tag: <nomeRazaoSocialIndustria>

**33.** Nome do Campo: **Razão Social da empresa vínculo (modalidade de código 3).**  
Tabela: SMATRICPLCOMPL.NOMEEMPRESA  
Informação extraída do campo complementar da matrícula de referência do aluno.  
Tag: <nomeRazaoSocialIndustria>

**34.** Nome do Campo: **Código do Ciclo**   
Tabela: Informação extraída da tabela dinâmica CODCICLO de acordo com as tabelas de apoio do DN que corresponde ao mês de referência da carga.  
Obs.: Esta Tabela será populada através de script até o ciclo 2020-12 para os demais ciclos deverão ser criados pelo próprio Regional diretamente na Tabela dinâmica CODCICLO.  
Tag: < codCiclo>

**35.** Nome do Campo: **Horas de Reconhecimento de Saberes**   
Tabela: Informação enviada com valor fixo de 35 horas. Somente quando o aluno alterar sua situação de matrícula no período letivo de Reconhecimento de Saberes para Matriculado, Concluinte, Desistente ou Falecido. Nos demais meses o envio será zerado.  
Tag: <horaReconhecimentoSaberes>

**36.** Nome do Campo: **Horas Destinadas**   
Tabela: O extrator verifica o campo STURMADISC.TIPO e de acordo com o tipo extrai as horas Presencial, Semi-Presencial e A Distância.  
Tag: < horaDestinada >

20%

**Presencial:**   
O extrator verifica se o campo STURMADISC.TIPO é igual a “P – Presencial” e envia as horas executadas do aluno de acordo com o plano de aula no mês informado no parâmetro que foi gerado o arquivo do SCAE. E o aluno não tiver saída.

 Caso o aluno tenha tido saída no mês informado no parâmetro, o cálculo será até um dia anterior a sua saída.

35%

**Semi-Presencial:**   
O extrator verifica se o campo STURMADISC.TIPO é igual a “S – Semipresencial” e para as horas presenciais envia as horas executadas do aluno de acordo com o plano de aula no mês informado no parâmetro que foi gerado o arquivo do SCAE.   
Para as horas a distância somente serão enviadas no último mês da turma disciplina (STURMADISC.DTFINAL). Nesse último mês será calculada a carga horária total da disciplina (SDISCGRADE.CH) e subtraído da carga horária presencial (soma do plano de aula). E o aluno não tiver saída.

 Caso o aluno tenha tido saída no mês informado no parâmetro, o cálculo será até um dia anterior a sua saída.

45%

**A distância:**  
O extrator verifica se o campo STURMADISC.TIPO é igual a “D – A distância” e enviará a carga horária rateada por mês. O cálculo será realizado através do total da CH da disciplina dividido pela quantidade de meses correspondentes ao período da Turma Disciplina (STURMADISC.DTINICIAL E STURMADISC.DTFINAL), esse envio será mensal. Fazendo o cálculo da SDISCGRADE.CH / quantidade de meses da turma disciplina.   
Se o aluno concluir a disciplina (SLOGMATRICULA.CODSTATUS=APROVADO) antes do prazo da turma/disciplina (STURMADISC.DTFINAL), a carga horaria integral da disciplina (SDISCGRADE.CH) será enviada.

 Para as Horas dos "Eventos" (Educação Continuada), no cadastro do Curso, o campo complementar (SCURSOCOMPL.TIPOACAO ) deverá estar preenchido com tipo “01 – Evento Educativo”. E também os alunos matriculados nestes “eventos” deverão estar com situação "Inscrito" e/ou resultado "Concluinte". (SMATRICPL.CODSTATUS = 66 e SMATRICPL.CODSTATUSRES = vazio OU 42)

**37.** Nome do Campo: **Indicador de Exclusão.** 

Tabela: Regra condicionada ao indicador de exclusão da matrícula (0 – não exclui; 1 – exclui)  
Tag: < horaDestinada >

6Estudante

**38.** Nome do Campo: **Código do estudante no sistema do DR**  
Tabela: Campo complementar CODALUNOSCAE; SALUNO.CODALUNOSCAE   
Se não tiver preenchido: SALUNO.RA   
Tag: <codEstudante>

**39.** Nome do Campo: **Nome completo do estudante**  
Tabela: PPESSOA.NOME  
Tag: <nomEstudante>

**40.** Nome do Campo: **Data de nascimento (yyyy-mm-dd)**  
Tabela: PPESSOA.DTNASCIMENTO  
Tag: <datNascimento>

**41**. Nome do Campo: **Sexo (M ou F)**  
Tabela: PPESSOA.SEXO  
Tag: <sexo >

**42.** Nome do Campo: **E-mail**  
Tabela: PPESSOA.EMAIL  
Tag: <desEmail>

**43.** Nome do Campo: **Número do RG**  
Tabela: PPESSOA.CARTIDENTIDADE  
Tag: <numRegistroGeral>

**44.** Nome do Campo: **Sigla do Órgão emissor**  
Tabela: PPESSOA.ORGEMISSORIDENT  
Tag: <sigOrgaoExpedidor>

**45.** Nome do Campo: **Nome do pai/responsável**  
Tabela: PPESSOA.NOME   
Tag: <nomPaiResp >

**46.** Nome do Campo: **Telefone com DDD (9999999999)**  
Tabela: PPESSOA.TELEFONE1  
Tag: <numTelefone >

**47.** Nome do Campo: **Celular com DDD (9999999999)**  
Tabela: PPESSOA.TELEFONE2  
Tag: <numCelular >

**48.** Nome do Campo: **CEP**  
Tabela: PPESSOA.CEP  
Tag: <numCep >

**49.** Nome do Campo: **Logradouro**  
Tabela: PPESSOA.RUA  
Tag: <endLogradouro >

**50.** Nome do Campo: **Complemento**  
Tabela: PPESSOA.COMPLEMENTO  
Tag: <endComplemento >

**51.** Nome do Campo: **Número**  
Tabela: PPESSOA.NUMERO  
Tag: <endNumero >

**52.** Nome do Campo: **Bairro**  
Tabela: PPESSOA.BAIRRO  
Tag: <nomBairro>

**53.** Nome do Campo: **Estado Civil**  
Tabela: De para  
Se Casado então 2   
Se Solteiro então 1  
Se Divorciado então 5  
Se Desquitado então 3  
Se Viúvo então 4  
Tag: <codEstadoCivil>

**54.** Nome do Campo: **Código do Municipio**  
Tabela: ZSCAEMUNICIPIO.CODIGOSCAE   
Obs: Criar tabela Z para fazer o de-para  
Tag: <codMunicipio>

**55.** Nome do Campo: **Nome da mãe**  
Tabela: PPESSOA.NOME  
Tag: <nomMae>

**56.** Nome do Campo: **CPF**  
Tabela: PPESSOA.CPF  
Tag: <numCpf>

**57.** Nome do Campo: **NIT**  
Tabela: SALUNOCOMPL.NIT  
Tag: <numNIT>

**58.** Nome do Campo: **Indicador Brasileiro**  
Tabela: Se nacionalidade igual Brasileira envia B senão E. PPESSOA.NACIONALIDADE  
Tag: <indBrasileiro>

**59.** Nome do Campo: **Responsável Legal**  
Tabela: Nome da mãe, se vazio então nome do Pai, se vazio então nome do responsável. PPESSOA.NOME da mãe, PPESSOA.NOME do Pai, FCFO.NOME  
Tag: <nomeResponsavelLegal>

7Disciplina

**60.** Nome do Campo: **Código da Disciplina**  
Tabela: SDISCGRADECOMPL.DISCEJA  
Tag: <codDisciplina>  
Tabela dinâmica de acordo com as tabelas de apoio do DN.  
- As disciplinas reportadas serão apenas as vinculadas a Cursos da EJA Profissionalizante e NOVA EJA.

**61.** Nome do Campo: **Data de Efetivação da Matricula na Disciplina**  
Tabela:  
Tag: <datEfetivacaoMatriculaDisciplina>  
A data enviada é correspondente a data em que a situação de matricula na disciplina (SMATRICULA.SSTATUS) foi alterada para Matriculado.   
Modalidade   
-As disciplinas reportadas serão apenas as vinculadas a Cursos da EJA Profissionalizante e NOVA EJA. Essa informação será extraída da matrícula de referência do aluno.

**62.** Nome do Campo: **Data de Movimentação da Disciplina**   
Tabela:  
Tag: <datMovimentacaoDisciplina>  
A data enviada é correspondente a data de qualquer alteração na disciplina (ou seja, quaisquer alterações nas situações da Disciplina).   
- As disciplinas reportadas serão apenas as vinculadas a Cursos da EJA Profissionalizante e NOVA EJA.

**63.** Nome do Campo: **Código da Mobilidade/Situação da disciplina**  
Tabela de De-para Situação Matrícula:  
Tag: <codSituacaoDisciplina>  
-As disciplinas reportadas serão apenas as vinculadas a Cursos da EJA Profissionalizante e NOVA EJA da matrícula de referência do aluno.  
-Será encaminhado como situação/saída: Aprovado (9), Dispensado (14) e Competência Certificada (72).   
-A situação Transferência de Turma (31) não será enviada como uma mobilidade assim como a situação Em Processo (71) de resultado final.

**64.** Nome do Campo: **Tipo Avaliação**  
Tabela: Para matriculas em disciplinas com situação: Competência Certificada  
- Tipo de Avaliação = 2  
Para matriculas em disciplinas com situação: Matriculado / Aprovado   
-Tipo de Avaliação = 1   
- As disciplinas reportadas serão apenas as vinculadas a Cursos da EJA Profissionalizante e NOVA EJA.  
Tag: <codTipoAvaliacao>

Menu que chama o relatório

Gerador de Saídas
