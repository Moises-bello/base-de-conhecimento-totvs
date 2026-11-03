---
content_hash: 8495339659426b583b6767d770aaad2a3f88782ab6c192fd9ff32e136216208c
fetched_at: '2026-06-29T00:10:42.233372+00:00'
page_id: '546699616'
product: rm
source: tdn-rm
title: Máscara da Turma - SENAI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546699616
version: 27
---

**Processo para configuração da Máscara da Turma, que permite o cadastro padronizado e sequencial de Código de Turma no TOTVS Educacional (SGE).**

O TOTVS Educacional permite que a instituição crie uma máscara para as turmas de cada curso, possibilitando que a Unidade operacional (Filial) mantenha um padrão de cadastro das suas Turmas.

A configuração da máscara é realizada diretamente no cadastro de curso e a sua aplicação é bastante flexível, atendendo a necessidade das Instituições de Ensino de acordo com a sua regra de negócio, utilizando da aplicação das "Tags" disponíveis para configuração, conforme recursos a saber:

# **PARAMETRIZAÇÃO DA MÁSCARA DA TURMA - CADASTRO DO CURSO**

O processo de configuração da Máscara da Turma é realizado através do acesso ao Módulo **TOTVS Educacional l Educacional**

O acesso para configurar a Máscara da Turma está disponível em: **TOTVS Educacional l <aba> Currículo e Oferta l Curso**.

Após selecionar o Curso desejado, clique em: Editar.

Ao acessar o cadastro de curso, na aba: Identificação, visualizamos o campo: Máscara da Turma. Posicionando o cursor sobre o ícone de informação, temos acesso à estrutura de "Tags" disponíveis para configuração da padronização desejada, conforme:

Importante:

 *As letras utilizadas no quadro acima, se utilizadas fora dos colchetes serão apenas letras comuns, portanto se o usuário precisar utiliza-las como letras, basta não colocar os colchetes que indicam inicio e término de sessão.*

Tomamos como exemplo a padronização estabelecida pela Unidade Operacional: **[CCC].TDSI.[T].&&&&.###,** aplicando-se **"."** (ponto) para separação dos dados, a saber:

* **CCC:** HAB (Três primeiras letras do nome do curso);
* **TDSI:** Modelo padrão fixo aplicado para a descrição do curso;
* **T:** Turno;
* **&&&&:** Período Letivo;
* **###:** Padrão sequencial de número de turmas cadastradas.

 Conforme padrão estabelecido, vincule a padronização estabelecida  ao campo: Máscara da Turma, e, após, clique em: Salvar

## **CADASTRO DA TURMA**

Uma vez configurada a padronização da Máscara da Turma, ao realizar o cadastro de uma nova Turma, o campo: Código da Turma deverá permanecer com valor igual a "0" (zero).

Finalizado o cadastro, ao clicar em: Salvar, teremos a aplicação da codificação padronizada, seguindo a configuração da Máscara da Turma ( **[CCC].TDSI.[T].&&&&.###** )vinculada aoCadastro de Curso.

Assim, conforme o exemplo, temos: **HAB.TDSI.V.2023.001.**

Observações:

**Ao realizar o cadastro de uma nova turma podemos observar os seguintes comportamentos:**

**Situação I**

Se o campo: Código da Turma estiver com com valor diferente de "0" (zero), a Máscara da Turma não é aplicada, mantendo assim, o valor cadastrado;

**Situação II**

Se o campo: Código da Turma estiver com com valor igual a "0" (zero), e não houver vínculo da Máscara da Turma no cadastro do Curso, ao salvar o cadastro da Turma, é apresentada a mensagem de alerta/notificação do RM, orientado a aplicação de um valor diferente de 0 (zero) no campo: Código da Turma, ou a aplicação de uma Máscara da Turma ao cadastro de Curso.

Importante:

O vínculo da Máscara da Turma ao cadastro de Curso se aplica por Coligada, ou seja, a sequência das Turmas serão contabilizadas por Coligada e não por Filial.
