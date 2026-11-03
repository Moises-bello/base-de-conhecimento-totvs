---
content_hash: 9694fad805821bef07e48e1f95a9f80e81f2f9cd19158216a4abd4a4e0a9172d
fetched_at: '2026-06-29T00:10:42.668933+00:00'
page_id: '547240322'
product: rm
source: tdn-rm
title: Itinerário Formativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547240322
version: 92
---

## **Conteúdo**

Importante

As funcionalidades relacionadas ao Novo Ensino Médio estão disponíveis a partir da versão 12.1.27.

## **01. Visão Geral**

Os itinerários formativos são o conjunto de disciplinas, projetos, oficinas, núcleos de estudo, entre outras situações de trabalho, que os estudantes poderão escolher no ensino médio. Os itinerários formativos podem se aprofundar nos conhecimentos de uma área do conhecimento (Matemáticas e suas Tecnologias, Linguagens e suas Tecnologias, Ciências da Natureza e suas Tecnologias e Ciências Humanas e Sociais Aplicadas) e da formação técnica e profissional (FTP) ou mesmo nos conhecimentos de duas ou mais áreas e da FTP. As redes de ensino terão autonomia para definir quais os itinerários formativos irão ofertar, considerando um processo que envolva a participação de toda a comunidade escolar. Através do menu **'Itinerário Formativo'** será possível cadastrar o conjunto articulado de unidades curriculares ofertadas pelas escolas e redes de ensino.  
**Exemplo:**  Matemática e suas Tecnologias

## **02. Permissão no Perfil do Usuário**

Para que o menu Itinerário Formativo seja visualizado deve ser dado a permissão em seu perfil de acordo com a imagem abaixo:

  **Acessar MDI I Menu | Serviços Globais| Perfil | Educacional | Acesso ao Menus | Educacional | Currículo e oferta | Estrutura curricular | Mais... | Itinerário Formativo**

## **03. Cadastro de Itinerário Formativo**

Para efetuar o cadastro de itinerário formativo acesse: Currículo e Oferta | Estrutura curricular | Mais... > **Itinerário Formativo**

O cadastro do itinerário formativo é composto pelos seguintes campos:

* Nome - indica o nome do itinerário formativo
* Descrição - descrição do itinerário formativo
* Carga Horária - carga horária mínima do itinerário formativo
* Ativo - indica se o itinerário formativo está disponível para ser associada a matriz curricular
* Controle da matrícula por Carga Horária - definição dos valores mínimos e máximo de carga horário do itinerário formativo a serem matriculadas
* Controle da matrícula por Número de Disciplinas - define o número mínimo e máximo de disciplinas do itinerário formativo a serem matriculadas.

Os itinerários formativos são compartilhado entre filiais de mesma coligada e nível de ensino, ou seja, o usuário da coligada **1**, filial 1 e nível de ensino **1**, irá ver todos os itinerário da coligada **1**, filial 2 e nível de ensino **1**, totalmente desvinculado da filial.

A partir da versão 12.1.32.302 Foi incluindo o campo Itinerário formativo Integrado, este campo e referente ao Censo.

A partir das versões **12.1.2302.100** e **12.1.2306** foi incluído um vinculo referente ao [itinerário formativo do histórico](https://tdn.totvs.com/pages/viewpage.action?pageId=740687296).

## **04. Cadastro de disciplina no Itinerário Formativo**

Após realizar o cadastro do Itinerário Formativo deve-se realizar o cadastro das disciplinas do itinerário formativo e realizar o vínculo entre o itinerário e suas disciplinas através do Anexo "Disciplinas do Itinerário Formativo".

Com a disciplina do itinerário formativo cadastrada e vinculada ao itinerário formativo, é possível associar a ela uma área do conhecimento, habilidades que o aluno deve alcançar para ser aprovado na disciplina e complementos da disciplina através do anexo existente no cadastro.

Importante

Uma disciplina só ficará disponível para ser vinculada ao Itinerário Formativo se a flag **"Itinerário Formativo"**  for selecionada no cadastro da disciplina (Currículo e Oferta | Estrutura Curricular | Disciplinas)

O check-box "Indica se imprime no boletim e exibe no portal do aluno", existente no cadastro de disciplinas tem duas funções:

* Indicar que a disciplina do itinerário formativo deverá ser impressa no boletim do aluno.
* Indicar que a disciplina do itinerário formativo deverá ser exibida no portal do aluno (esse comportamento é verdadeiro apenas se o parâmetro "Educacional | RM Portal | Gerais | Portal - Geral 4/15 | Exibir as disciplinas para o aluno de acordo com o campo 'Imprime no Boletim' do cadastro de disciplinas da matriz curricular" estiver marcado. Caso o parâmetro esteja desmarcado, a disciplina sempre será exibida no portal do aluno).

Os anexos relacionados a visualização de log de movimentações feitas no complemento das disciplinas serão visíveis apenas se o parâmetro **Educacional | Secretária | Geral 4/6 | Gravar log de alterações dos complementos das disciplinas** estiver marcado.

É possível definir um conjunto de  para o cadastro das disciplinas do itinerário formativo, para isso, deve-se realizar o cadastro desses campos em **Configurações |  Campos complementares | Disciplinas do itinerário formativo**. Para que os campos complementares criados sejam exibidos no cadastro da disciplina do itinerário é necessário acessar o cadastro de  e fazer o vínculo do mesmo na aba de campos complementares disponíveis.

### 04.01 Exclusão de disciplina de itinerário formativo

A partir das versões **12.1.2209.241, 12.1.2302.163, 12.1.2306.107 e 12.1.2310** disciplinas do itinerário formativo, somente poderão ser excluídas caso não haja oferta (), se houve oferta uma mensagem de validação irá ecoar na tela e não será possível excluir.

### 04.02 Cadastro de disciplina no Itinerário Formativo na área ofertado do processo seletivo

Para que as matérias disciplinas cadastradas como itinerário formativo apareça no processo seletivo será necessário Currículo e oferta | Estrutura curricular | Cursos

Anexos > Séries

Anexos > Matriz Curricular

Edite ou adicione uma matriz curricular > Itinerário Formativo ou matriz curricular

Adicione uma disciplina de itinerário formativo para matriz curricular utilizada na área ofertada.

## **05. Complemento de disciplinas do itinerário formativo**

É possível incluir [complementos de disciplinas](https://tdn.totvs.com/x/XPxbGQ) através do anexo da disciplina do itinerário formativo

Os complementos podem ser incluídos manualmente ou automaticamente. Para incluirmos complementos de maneira automática, deve-se possuir um grupo de complementos com tipos de complementos cadastrados e informar o mesmo no cadastro das disciplinas do itinerário formativo. Após a inclusão do grupo, os complementos serão criados conforme os tipos presentes no cadastro do grupo.

### **05.01****Copiar complemento de disciplina do itinerário formativo entre períodos letivos**

O processo "Copiar complemento de disciplina do itinerário formativo entre períodos letivos" foi criado com o intuito de facilitar a criação do mesmo complemento de disciplina do itinerário em um período letivo diferente. Para executar o processo basta informar o "Período letivo de origem" e o "Período letivo destino".

O parâmetro "**Sobrepor complemento de disciplina no período letivo de destino**" define se todos complementos existentes na disciplina do período letivo de destino serão sobrepostos pelos complementos da mesma disciplina do período letivo de origem, ou seja, os complementos no período letivo de destino serão excluídos para posteriormente serem inseridos os complementos do período letivo de origem. Caso o parâmetro não seja marcado, o processo irá copiar para o período letivo de destino apenas os complementos da disciplina do período letivo de origem que forem diferentes dos já existentes.

O processo Copiar complemento de disciplina do itinerário formativo entre períodos letivos só estará disponível se o parâmetro "**Educacional | Secretaria | Geral 4/6 | Manter histórico de complemento de disciplina por período letivo**" estiver marcado.

### **06** **Visão de matricula no Itinerário Formativo**

Importante

A visão de matrícula no itinerário formativo está disponível a partir da versão 12.1.33.290 e posteriores.

A matricula no Itinerário Formativo só aparece no ensino básico.

**6.1 Matricula e avaliação | Matricula | Matriculas | Matricula no Itinerário Formativo| Anexo| Matriculas em diciplinas.**

Informações Complementares

---

**[Novo Ensino Médio](https://tdn.totvs.com/x/C3R9IQ)**

* [Área do conhecimento](https://tdn.totvs.com/x/njaeI)
* [Competências e habilidades](https://tdn.totvs.com/x/8RVxIQ)
* [Itinerário Formativo da Matriz Curricular](https://tdn.totvs.com/x/ThVxIQ)
* [Estrutura Curricular](https://tdn.totvs.com/x/zf1bGQ)
* [Turma/Disciplina do Itinerário Formativo](https://tdn.totvs.com/x/jBVxIQ)
* [Parametrização por Curso](https://tdn.totvs.com/x/x-xbGQ)
* [Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)
* [Matricular Aluno](https://tdn.totvs.com/x/4vtbGQ)
* [Registro de avaliação por habilidades](https://tdn.totvs.com/x/Ygp9IQ)
