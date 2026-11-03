---
content_hash: fa01653e7a299d21bfec5a2a83c5e93193e040a9f97928ca35a1f548101f97da
fetched_at: '2026-06-29T00:05:59.515330+00:00'
page_id: '191465785'
product: rm
source: tdn-rm
title: Censo da Educação Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191465785
version: 119
---

Fique Atento ao Cronograma!!!

O cronograma pode ser acessado no portal do INEP: [http://portal.inep.gov.br/censo-da-educacao-superior](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-da-educacao-superior/orientacoes)

# Introdução

O Censo da Educação Superior reúne informações sobre os cursos de graduação presencial, a distância e sequenciais, tais como vagas ofertadas, matrículas, ingressantes e concluintes. A coleta inclui dados relativos a corpo docente e organização acadêmica. 

Fonte:  Portal Brasil, com informações do Inep

# **Requisitos mínimos**

* 12.1.2502.307
* 12.1.2506.329
* 12.1.2510.218
* 12.1.2602.174
* Base atualizada com todos os scripts rodados.
* Importar o novo Layout - (Gestão |Utilitários |Totvs Compartilhamento)
  + EDULAY0001 - Censup - Censo da Educação Superior - Aluno, Docente, Mediador

# Desenvolvimento/Procedimento

O TOTVS Educacional disponibiliza funções que permitem a criação dos arquivos com dados da Escola, Professores e Alunos.

Estas funções se dividem em:

* + Preparação dos Cadastros
  + Assistente de preparação dos dados
  + Relatórios de exportação de dados

 O usuário deverá estar autenticado no Contexto Ensino Superior, e parametrizar os dados para a geração do arquivo Censo.

## 1. **Cadastros**

Para realizar a parametrização do Censo, Acesse: Configurações| Parâmetros| Secretaria | Geral 7/7

O cadastro dos dados da instituição agora pode ser realizado de duas formas:

* Filial
* Nível de Ensino

### 1.1  **Relação de cadastros do Censo**

Acesse: Atividades acadêmicas | Acadêmico | Censo | Relação de Cadastros do Censo

Na tela de relação de cadastros do Censo devem ser cadastradas as relações dos cadastros do sistema com as tabelas auxiliares do Censo.

Deficiências, é a relação de cadastro entre as sub deficiências do sistema e as deficiências do Censo.

### 1.2  **Cadastro da Instituição do MEC**

#### **1.2.1**  **Cadastro da Instituição pela Filial**

**Acesse:** 

Módulo Gestão Fiscal | Cadastros | Filial | Anexo > Dados Educacionais | Anexo > Instituição do MEC 

ou 

Atividades acadêmicas | Acadêmico| Censo | Instituição do MEC

Aviso

A partir da versão 12.1.2506, o cadastro da Instituição do MEC deixa de ser por filial ou por nível de ensino e passa a ser um cadastro global, permitindo que sejam associados os contextos educacionais à respectiva Instituição do MEC.

Alguns ajustes serão necessários no(s) cadastro(s) de Instituição do MEC já existente(s).

Para mais detalhes, verifique a documentação em <https://tdn.totvs.com/x/IBKHNw>.

Estes dados agora podem ser informados no anexo Instituição do MEC no cadastro da Filial em gestão de fiscal.

A tela exibe os dados solicitados no questionário “Dados da Escola”. Preencha as seis abas de acordo com as instruções solicitadas pelo MEC.

É possível associar uma [Mantenedora](https://tdn.totvs.com/display/LRM/Mantenedora) á instituição do MEC.

#### **1.2.2** **Cadastro da Instituição pelo Nível de Ensino**

Aviso

A partir da versão 12.1.2506 esta opção de menu não estará mais disponível.

**Acesse:** Configurações | Níveis de ensino | Anexo > Instituição do MEC

Estes dados agora podem ser informados no anexo Instituição do MEC no cadastro de Nível de Ensino.

A tela exibe os dados solicitados no questionário “Dados da Escola”. Preencha as abas de acordo com as instruções solicitadas pelo MEC.

**Obs.** Como o cadastro da [Instituição do MEC](https://tdn.totvs.com/x/IBKHNw)  agora é global, para que as consultas possam ser visualizadas, é necessário que a opção **“Visível a todas as coligadas”** esteja marcada.

### **1.3****Curso do MEC**

Verifique o registro de todas as habilitações dos cursos que são objeto do censo: os de graduação e os sequenciais de formação específica.

**De acordo com o que foi informado no passo 1.1, acesse:**

**Nível de Ensino:** Configurações | Níveis de ensino | Anexo > Instituição do MEC | Anexo > Curso do MEC

**Filial:** Módulo Gestão Fiscal | Cadastros | Filial | Anexo > Dados Educacionais | Anexo > Instituição do MEC | Anexo > Curso do MEC

Na tela de edição do Curso do MEC certifique-se de que o “Cód. INEP do Curso” esta preenchido corretamente.

Nesta tela pode-se informar as características da habilitação solicitadas pelo MEC e, se for o caso, a lista de tipos de laboratórios à disposição dos alunos. No momento estas informações ainda não são exportadas pelo “TOTVS Educacional”.

A partir da versão **12.1.2406** os campos "Nome da Habilitação" e "Ênfase" foram removidos do cadastro.

#### **1.3.1****Informando o Curso do MEC**

**Acesse:** Currículo e Oferta | Estrutura curricular | Matrizes Curriculares | Anexo > Matriz Aplicada

Neste momento deve-se informar o campo "Id. Curso" no cadastro da matriz aplicada conforme criado na Filial/Nível de Ensino.

Caso o campo não seja informado, os cursos que possuem a matriz aplicada não serão buscados pelo processo do Censo.

### **1.4** **Cadastro do Aluno**

**Acesse:** Currículo e Oferta | Aluno | Anexos > Dados do Censo Escolar e SISTEC

Esta tela apresenta os dados solicitados pelo MEC no questionário “Dados do Aluno” também sendo necessário informar outras necessidades especiais para o aluno. Deve ser usada para a correção do código INEP atribuído ao aluno.

Note que no primeiro momento do Censo, este campo é enviado em branco sendo preenchido automaticamente pelo processo de importação do arquivo gerado pelo MEC.

No cadastro de aluno deve-se atentar para o registro da instituição de ingresso do aluno.

Acesse no cadastro de Aluno a aba “Diversos”, e confirme o tipo da instituição (pública ou particular) no cadastro de Instituições de Ensino.

**Observação:**  O campo Justificativa do Aluno está incluso no anexo dados para o Censo e SISTEC na matrícula do período letivo.

#### **1.4.1 Informando Necessidades Especiais.**

**Acesse:** Atividades Acadêmicas | Acadêmico | Censo | Relação de cadastro do  censo

Neste momento devemos cadastrar as deficiências do censo e suas subdeficiências.

**Acesse:** Currículo e Oferta | Aluno | Aba Identificação | Aba Pessoas com necessidade educacionais especiais

Devemos informar nesse momento a Deficiência do aluno e depois através do cadastro de Detalhes, informamos as subdeficiência conforme registrado nas relações de cadastro.

#### **1.4.2 Situação de Matrícula do Aluno**

**Acesse:** Currículo e Oferta | Acadêmico | Situação de Matrícula

Os dados de situação de matrícula devem estar configurados corretamente conforme o status do aluno no curso. **É de extrema importância que os dados estejam corretos, pois o arquivo gerado pelo sistema identifica a situação dentro do curso/habilitação do aluno identificando qual o status do mesmo na instituição.** Segue os parâmetros utilizados e as opções disponíveis do status do aluno conforme solicitado pelo MEC:

Falecido (7)

* O aluno receberá esta situação se a pessoa do aluno possuir o parâmetro falecido marcado.

Desvinculado do curso (4)

* O aluno receberá esta situação caso não se enquadre na classificação acima e se a situação de matrícula do aluno no período letivo possuir uma das opções "Indica jubilamento" ou "Indica desvinculação do curso" marcada.

Formado (6)

* O aluno receberá esta situação caso não se enquadre nas classificações acima e se a situação de matrícula do aluno no curso possuir a opção "Indica conclusão do curso" marcada. Para esta situação, é necessário que a data de conclusão do curso, informada na aba Diploma do cadastro de Curso/Habilitação do Aluno, esteja preenchida e seja anterior à data de referência.

Matrícula trancada (3)

* O aluno receberá esta situação caso não se enquadre nas classificações acima e se a situação de matrícula do aluno no período letivo possuir a opção "Indica trancamento" marcada.

Transferido para outro curso da mesma IES (5)

* O aluno receberá esta situação caso não se enquadre nas classificações acima, se a situação do curso/habilitação e a situação de matrícula no período letivo do aluno possuírem a opção "Indica transferência" marcada, e se o curso de origem e de destino não possuírem o mesmo código do e-MEC.

Cursando (2)

* O aluno receberá esta situação caso não se enquadre nas classificações acima e esteja matriculado no período letivo.

#### **1.4.3 Curso/Habilitação do Aluno**

**Acesse:** Currículo e Oferta  | Aluno e Professor | Aluno | Anexos > Cursos/Habilitações

A forma de ingresso e a data de ingresso do aluno são dados obrigatórios para o Censo. Devem ser informados na aba “Ingresso“ do anexo “Cursos / Habilitações” do Cadastro de Alunos. Como estes dados são de preenchimento opcional, nesta versão, o sistema esta informando como data de ingresso a MENOR data de matrícula do aluno no curso. Caso o tipo de ingresso não esteja registrado, o sistema considera que o ingresso foi através de vestibular.

Caso o aluno receba algum tipo de apoio social ou exerça alguma atividade complementar (monitoria, pesquisa, estágio não obrigatório), abra o anexo “Dados do Curso do Aluno para o Censo Escolar” para registrar esta informação.

Caso tenha ingressado por politica de ação afirmativa ou por programa diferenciado de destinação de vagas, os dados são informados abaixo.

**Observação:**Alunos PARFOR devem possuir como forma de ingresso Programa Especiais. Caso o curso do aluno não for licenciatura, a informação de PARFOR será desconsiderada.

### **1.5 Cadastro do Professor**

**Acesse:** Currículo e Oferta | Professores | Anexos > Dados para o Censo Escolar e SISTEC

O cadastro dos professores deve ser complementado com as informações solicitadas pelo Censo. O “Código INEP” não deve ser informado.

Ainda na tela de ‘Dados para o CENSO’ no cadastro do professor, atente-se para informar se ele é um ‘Professor Visitante’.

Caso necessário, informe também qual a Área de atuação do mesmo.

A aba de Formação do professor é também solicitado o preenchimento dos dados, sendo a Escolaridade obrigatória e a Pós Graduação condicional.

Caso o professor tenha alguma deficiência, as mesmas devem ser informadas na aba identificação

### Aba **Atuação / Vínculo do Docente**

A aba **Atuação / Vínculo do docente** é destinada ao registro das informações acadêmicas e contratuais do professor no contexto do Censo Escolar e SISTEC. Nela são informadas as áreas de atuação, carga horária, tipo de vínculo empregatício, participação em bolsas e situações específicas relacionadas à admissão, desligamento e função de conteudista.

Esta aba está organizada nos seguintes blocos:

---

#### 1. Área de Atuação

Permite indicar em quais frentes o docente exerce atividades na instituição. É possível selecionar uma ou mais opções:

* **Ensino**
* **Pesquisa**
* **Extensão**
* **Gestão, planejamento e avaliação**

Essas informações são utilizadas para caracterização da atuação acadêmica do docente no ano de referência do Censo.

---

#### 2. Bolsa

Campo destinado à indicação de participação em programas institucionais de bolsa:

* **Bolsa de pesquisa**
* **Bolsa de extensão**

Pode ser marcado conforme aplicável à atuação do docente.

---

#### 3. Carga Horária Semanal

Campo numérico para informar a **carga horária semanal do docente**, considerando as atividades exercidas na instituição no período de referência.

---

#### 4. Vínculo Contratual

Neste bloco são registradas as informações relativas ao tipo de vínculo do docente com a instituição:

* **Tipo de vínculo empregatício** (seleção obrigatória conforme regras de validação do Censo);
* **Tipo de consórcio, acordo ou programa de cooperação**, quando aplicável aos casos de docente sem vínculo contratual direto com a IES.

Esses campos determinam a natureza jurídica da relação entre o docente e a instituição.

---

#### 5. Função de Conteudista

Destinado aos casos em que o docente exerce a função de conteudista.

Inclui:

* Indicação se a função de conteudista é exercida em contrato específico (distinto do contrato de regência e/ou gestão);
* Tipo de vínculo exclusivo para conteudista;
* Tipo de consórcio ou programa de cooperação exclusivo para conteudista, quando aplicável.

As informações deste bloco devem respeitar as regras de validação relacionadas ao vínculo e à atuação do docente.

Apenas os Professores que possuem vínculo com a Instituição de Ensino Superior por, no mínimo, 60 dias dentro do período letivo do ano de referência do Censo são enviados para o Censo.

Ou seja, para que o professor não seja enviado para o Censo, todas as turmas e disciplinas que ele leciona no período letivo considerado pela data de corte (período do Censo) devem ter o período inferior a 60 dias.

No campo **Tipo Professor** foi adicionada a opção:

* **Mediador Pedagógico**

Essa inclusão atende às exigências do layout vigente do Censo, que passou a prever a identificação específica do professor que atua na mediação pedagógica.

A seleção dessa opção impacta diretamente a geração das informações declaradas, sendo utilizada na composição do arquivo de exportação do Censo. Portanto, deve estar coerente com o cadastro do docente na aba **Atuação / Vínculo do Docente**, especialmente quanto à área de atuação, vínculo e carga horária.

Após a conclusão de todas as configurações necessárias para a geração do arquivo do Censo, o sistema utilizará um layout específico para docentes classificados como **Mediador Pedagógico**, em conformidade com a legislação e o manual técnico vigente do Censo.

A aba **Dados do Censo** é destinada ao detalhamento da atuação do docente em cada turma, conforme exigências do Censo Escolar/SISTEC.

Caminho:  
**Turma Disciplina → Turmas do Professor → Aba Dados do Censo**

O preenchimento desta aba é obrigatório para os docentes vinculados à turma que serão considerados na geração das informações do Censo.

---

#### Finalidade

Registrar:

* O tipo de atuação do docente na turma (Regente, Conteudista ou Coordenador);
* A carga horária semanal atribuída àquela turma;
* As atividades pedagógicas exercidas no contexto da mediação e acompanhamento dos estudantes.

Essas informações compõem os dados declaratórios enviados aos órgãos reguladores.

#### Observação Importante

O correto preenchimento desta aba é requisito prévio para que a aba **Atuação / Vínculo do Docente** funcione adequadamente e permita a geração consistente das informações do Censo.

Para **Docente Regente** ou **Docente Conteudista**, a área de atuação correspondente é **Ensino** (Caminho: *Dados Censo Escolar e Sistec > Atuação > Vínculo do Docente*).

Para **Docente Coordenador**, a área de atuação correspondente é **Gestão, Planejamento e Avaliação** (Caminho: *Dados Censo Escolar e Sistec > Atuação > Vínculo do Docente*).

Ao realizar o processo de Preparação de dados do Censo da Educação Superior, os Professores que foram retirados do CENSO, terão sua situação alterada no sistema para "Desvinculado".

**Acesse:** Currículo e Oferta | Professores | Editar | guia: identificação | sub guia: informações adicionais | grau de instrução

O cadastro de grau de instrução é levado para o layout do arquivo do professor, registro 41 campo 22.

As informações cadastradas ficarão da seguinte forma:

| Cadastro no TOTVS Educacional: | Valores esperados no INEP: |
| --- | --- |
| 1 - Analfabeto | 1 - Sem formação de nível superior |
| 2 - Até o 5º ano incompleto do ensino fundamental | 1 - Sem formação de nível superior |
| 3 - 5º ano completo do ensino fundamental | 1 - Sem formação de nível superior |
| 4 - Do 6 ao 9 ano do ensino fundamental | 1 - Sem formação de nível superior |
| 5 - Ensino fundamental completo | 1 - Sem formação de nível superior |
| 6 - Ensino médio incompleto | 1 - Sem formação de nível superior |
| 7 - Ensino médio completo | 1 - Sem formação de nível superior |
| 8 - Educação superior incompleto | 1 - Sem formação de nível superior |
| 9 - Educação superior completo | 3 - Nível superior sem pós |
| A - Pós graduação incompleto | 3 - Nível superior sem pós |
| B - Pós graduação completo | 4 - Especialização |
| C - Mestrado incompleto | 3 - Nível superior sem pós |
| D - Mestrado completo | 5 - Mestrado |
| E - Doutorado incompleto | 3 - Nível superior sem pós |
| F - Doutorado completo | 6 - Doutorado |
| G - Pós doutorado incompleto | 6 - Doutorado |
| H - Pós Doutorado completo | 6 - Doutorado |

Atenção

**Para os campos:  
  
\* C - Mestrado incompleto;  
\* E - Doutorado incompleto.**

**O equivalente é 3 - Nível superior sem pós, pois a pessoa pode cursar o mestrado sem ter finalizado a pós graduação e pode também cursar o doutorado, sem ter finalizado o mestrado e a pós graduação.**

**Lembrando que essas são possibilidades e não a regra.**

### **1.6 Cadastro do Período Letivo**

**Acesse:** Currículo e Oferta | Períodos Letivos

Deve-se atentar as datas de início e fim dos períodos letivos referentes ao ano base do censo, pois as mesmas são consideradas para inserção dos alunos no arquivo do censo.

Exemplo

Um aluno matriculado em 2024/1 será levado para o arquivo do censo, caso a data de início do período letivo 2024/1, seja do ano de 2023 (por exemplo 01/11/2023), visto que a matrícula dos alunos ocorre antes do real início do ano.

**Observação:** Caso as datas estejam em branco ou incorretas, os arquivos não serão gerados corretamente.

### **1.7 Matriz Aplicada ( Curso do MEC e Campus/Polo)**

#### **1.7.1 Informando o Curso do MEC**

**Acesse:** Currículo e Oferta | Estrutura curricular | Matrizes curriculares | Anexos > Matriz aplicada

No cadastro da Matriz Aplicada, deve-se informar o Curso do MEC relativo à mesma. O mesmo será buscado automaticamente pelo processo do censo.

### **1.7.2 Informando o Campus/Polo**

**Acesse:** Currículo e Oferta | Estrutura curricular | Matrizes curriculares | Anexos > Matriz aplicada | Anexos > Campus da matriz aplicada

No anexo de Campus da matriz aplicada se informa o Campus/Polo utilizado por aquela matriz aplicada. O mesmo será buscado pelo processo do censo caso o curso esteja configurado como "A distância".

### **1.8 Turmas**

**Acesse:** Currículo e Oferta | Oferta | Turmas | Anexos > Dados do Curso para o CENSO Escolar e SISTEC

Nos dados do Censo das Turmas, informar se atende a pessoas portadoras de deficiência - PCD.

### **1.9****Tipos de Bolsas**

Verifique se as características dos tipos de bolsa, conforme exigidas pelo MEC foram registradas no sistema.

**Acesse:** Cadastros | Financeiros | Bolsas

Verifique os dados do anexo “Dados da Bolsa para o Censo Escolar” de cada registro e assinale a origem dos recursos que financiam a bolsa.

Conforme Manual de Preenchimento do Censo, **apenas bolsas de 50% ou mais de desconto na mensalidade devem ser informadas em financiamento estudantil**.

Portanto, serão consideradas para o Censo apenas as bolsas que estão cadastradas para os alunos com percentual igual ou superior a 50.

### **1.10****Cadastros de LICENCIATURA**

Antes de iniciarmos o processo de Preparação do Censo, é necessário realizar o cadastro da LICENCIATURA.

#### **1.10.1****Informando o campo LICENCIATURA**

**De acordo com o que foi cadastrado no passo 1, acesse:**

**Nível de Ensino:** Configurações | Níveis de ensino |  Anexo > Instituição do MEC | Anexo > Curso do MEC

**Filial:** Módulo Gestão Fiscal | Cadastros | Filial | Anexo > Dados Educacionais | Anexo > Instituição do MEC | Anexo > Curso do MEC

Deve-se marcar o parâmetro "Curso de licenciatura" caso o Curso do MEC seja de licenciatura.

---

## **2.** **Preparação do Cadastro para o CENSO Escolar Ensino Superior**

Uma vez verificado os cadastros, pode-se realizar o processo de extração de dados e conversão de códigos utilizando-se do “Assistente de preparação de dados”.

Este Assistente vai preparar a base de dados para a gravação de um arquivo texto com os dados da Escola, Alunos e Professores solicitados na etapa inicial.

**Acesse:** Atividades Acadêmicas | Acadêmico | Censo | Preparação de dados do Censo da Educação Superior

Se os dados específicos referentes à Escola não tiverem sido registrados no Cadastro de Filiais, o Assistente não irá prosseguir.

Caso esta informação tenha sido registrada corretamente, será solicitado o preenchimento da data de referência.

### **2.1** **Preparação do Arquivo**

Informe a “Data de Referência” do Censo.

Se houver qualquer período letivo com datas de “início” ou “fim” em branco, o Assistente exibirá uma mensagem de alerta.

Uma vez informada a data, o Assistente exibe todas as habilitações que estão com o código do INEP não preenchido

Verifique se nesta lista consta alguma que deva ser informada no Censo. Caso exista, o código do INEP pode ser informado na mesma tela.

### **2.2** **Carga Horária**

Caso fique faltando informação de carga horária para alguma grade curricular ou disciplina que será utilizada no Censo, isso será exibido no passo de Carga Horária da tela de preparação dos dados para o censo superior.

Não é permitido avançar no assistente sem informar todas as cargas horárias que estão faltando.

Para facilitar o ajuste das informações, foi criado um botão na frente de cada registro da tela [...], que irá direcionar para o lugar correto onde deve ser colocado a carga horária.

Essas informações são necessárias para compor os seguintes campos que serão gerados no arquivo do Censo:

* Carga horária total do curso por aluno: Somatório do total da carga horária dos componentes curriculares que fazem parte da matriz do curso. Cada aluno poderá possuir uma carga horária total a depender do currículo que ele deva integralizar.
* Carga horária integralizada pelo aluno: Somatório da carga horária dos componentes curriculares que o aluno tenha aproveitado e que fazem parte da matriz do curso e cujo as atividades curriculares associadas estejam vinculadas a um período letivo dentro da data de referência no Censo.

Caso o parâmetro "Utilizar carga horária de disciplinas de origem na integralização de carga horária" estiver marcado (em Configurações | Parâmetros | Secretaria | Geral 2/7), o cálculo da integralização para disciplina concluída por equivalência de disciplinas irá utilizar a carga horária da disciplina efetivamente cursada e não a carga horária da disciplina da matriz que foi concluída por equivalência. Para disciplina concluída por aproveitamento de estudos, a carga horária integralizada será a carga horária da disciplina de origem do aproveitamento de estudo, caso ela tenha sido cadastrada. 

Caso a carga horária integralizada de algum aluno que possui o vínculo "Formado" ultrapasse em mais de 100 horas a carga horária total do curso, o INEP poderá notificar a instituição para verificar se as informações estão corretas.

### **2.3** **Atuação do Professor**

No passo em questão apenas serão exibidos professores que não possuem vínculo com nenhum curso no período do censo. Os mesmos serão identificados pelo cadastro de Atuação na Instituição dentro dos dados do MEC do Professor.

Selecione os professores que deverão ser enviados para o censo e avance o processo.

### **2.4 Cadastro do País de Origem**

Nesta página o Assistente exibe os diversos códigos de nacionalidade referentes aos alunos e professores recenseados.

Para cada “Código Próprio” da lista deve ser informado o “Código INEP” correspondente. Clique no botão com os três pontos [...] para abrir a tela de pesquisa.

Para avançar para a próxima tela todos os códigos devem ser informados.

O país de origem Aluno e/ou Professor é inferido primariamente a partir do estado informado em seu cadastro de pessoa:

**Exemplo 1:**

**Exemplo 2:**

No primeiro exemplo o país de origem é o Brasil e no segundo os Estados Unidos da América. A nacionalidade informada no Censo inicialmente é inferida a partir do cadastro de pessoa:

No caso de haver naturalização do aluno/professor em seu cadastro de pessoa (aba Doc. Estrangeiros), a nacionalidade a ser considerada no Censo é a brasileira:

### **2.5 Forma de ingresso**

Agora na página o Assistente exibe as diversas formas de ingresso nos cursos dos alunos recenseados conforme informado na tela “Cursos” do cadastro de alunos.

Para cada forma de ingresso informe suas características conforme determinado pelo MEC.

Marcações simultâneas

Somente os campos “ Vestibular”, ” Enem” e “Seleção Simplificada” podem ser informados marcados simultaneamente.

### **2.6 Finalização**

Neste ponto o Assistente já tem todas as informações necessárias para preparar os dados necessários à geração do arquivo. Clique em “Executar”.

## 3. **Geração do Arquivo Censo**

**Acesse:** Gestão | Ferramentas de Análise | Gerador de Saída

### **3.1 Importando o Arquivo** **de Layout**

Para realizar a importação do arquivo do censo, deve-se acessar o processo "Importar Layout".

Para realizar o processo de exportação, será necessário adicionar os layouts do Censo e executar o processo. Para isso acesse na lateral direita do RM o menu "**Central de Recursos**", clique em "**Não Encontrou? Pesquise na TOTVS!**"

Pesquise pelo termo "**Censup**", marque os dois registros que serão exibidos e clique em Download.

Na sequência, escolha a opção "Importar", para que os layouts sejam diretamente importador para sua base de dados.

Atente-se que ao adicionar **cada um dos layouts** através TOTVS Compartilhamento (Gestão | Utilitários | TOTVS Compartilhamento), os mesmos **devem possuir uma categoria** (Serviços Globais| Serviços| Utilitários),na aba de parâmetros da tela de importação de layout, conforme o print abaixo:

### **3.2 Seleção de Arquivo**

Selecione o arquivo que será gerado e utilize o processo "Geração de saída".

**Deve-se atentar para as consultas utilizadas no gerador.**

**O sistema utiliza consultas internas para a geração dos arquivos do Censo. Porém, se for necessário alterar essas consultas para buscar informações de forma personalizada, isso poderá ser feito no seguinte caminho: Atividades acadêmicas | Acadêmico | Censo | Instituição do MEC**

**Caso as consultas estiverem em branco, serão utilizadas consultas internas do sistema.**

**É possível fazer a exportação das consultas do sistema** **utilizando o botão "Exportar Consultas Internas" e após fazer a alteração, parametrizar para o sistema buscar a personalizada.**

### **3.3 Seleção de Layout**

Nesta tela, será necessária a seleção de um layout para o gerador e definido um "**Diretório de Destino**", onde o arquivo de exportação será armazenado.

### **3.4 Parâmetros da Geração**

Em seguida, devemos informar a coligada, instituição, data início e data fim que visamos gerar.

No caminho informado durante o processo é gerado uma pasta Saidas, contendo o arquivo gerado.

Arquivos gerados - Alunos

Arquivos gerados- Docentes

Arquivos gerados- Mediador

# Importação de dados do Censo

Antes de fazer a importação, deve ser feita exportação do arquivo contendo os dados do Censo através do portal do INEP. Esse arquivo que deve ser utilizado na importação. Para isso, basta selecionar o arquivo e executar o processo de Importação de dados do Censo Escolar.

### Campos que serão atualizados na importação do Censo Superior

Código INEP do aluno na tela de Dados do Censo Escolar do aluno

### **Documentação do Censo**

Esta documentação do Censo poderá ser acessada rapidamente a qualquer momento através do próprio menu do Censo no sistema.

Acesse: Atividades acadêmicas | Acadêmico | Censo | Documentação - Censo da Educação Superior

# Documentações de Apoio

Acesse o link abaixo para visualizar onde cada campo do layout do INEP está localizado no Educacional:
