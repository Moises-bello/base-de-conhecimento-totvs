---
content_hash: 2953c3c622b33257d5f757917687b645fde96d106e712eed144c83bba9afbdd4
fetched_at: '2026-06-29T00:10:41.798693+00:00'
page_id: '546672615'
product: rm
source: tdn-rm
title: Máscara da Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546672615
version: 14
---

|  |  |
| --- | --- |
| Descrição | Máscara da Turma |
| Observações | Procedimento para configurar a Máscara da Turma, que possibilita a inserção padronizada e sequencial do Código da Turma no TOTVS Educacional (SGE). |

O TOTVS Educacional oferece a funcionalidade de criação de uma máscara para as turmas de cada curso, permitindo que a unidade operacional (filial) mantenha um padrão consistente no cadastro das turmas. A configuração da máscara é feita diretamente no cadastro do curso e pode ser aplicada de forma flexível, atendendo às necessidades específicas das instituições de ensino de acordo com suas regras de negócio. Isso é feito utilizando as "Tags" disponíveis para configuração, conforme os recursos disponíveis.

# **PARAMETRIZAÇÃO DA MÁSCARA DA TURMA - CADASTRO DO CURSO**

O processo de configuração da Máscara da Turma é realizado através do acesso ao Módulo TOTVS Educacional l Educacional

O acesso para configurar a Máscara da Turma está disponível em:  TOTVS Educacional l Aba: Currículo e Oferta l Curso.

Após selecionar o Curso desejado, clique em: Editar.

Ao acessar o cadastro de curso, na aba: Identificação, visualizamos o campo: Máscara da Turma.

Posicionando o cursor sobre o ícone de informação , temos acesso à estrutura de "Tags" disponíveis para configuração da padronização desejada, conforme:

Importante:

 *As letras utilizadas no quadro acima, se utilizadas fora dos colchetes serão apenas letras comuns, portanto se o usuário precisar utiliza-las como letras, basta não colocar os colchetes que indicam inicio e término de sessão.*

Tomamos como exemplo a padronização estabelecida pela unidade operacional para o curso: Ensino Fundamental - Anos Iniciais  ***[****cccc]-[h]-[T]-&&***aplicando-se **"-"** (ponto) para separação dos dados, a saber:

 Conforme padrão estabelecido, vincule a padronização estabelecida  ao campo: Máscara da Turma, e, após, clique em: Salvar.

## **CADASTRO DA TURMA**

Uma vez configurada a padronização da Máscara da Turma, ao realizar o cadastro de uma nova Turma, o campo: Código da Turma deverá permanecer com valor igual a "0" (zero).

Finalizado o cadastro, ao clicar em: Salvar, teremos a aplicação da codificação padronizada, seguindo a configuração da Máscara da Turma ***[****cccc]-[h]-[T]-&&***vinculada aoCadastro de Curso.

Assim, conforme o exemplo, temos: ***EF I-1-M-20***

Observações:

Ao realizar o cadastro de uma nova Turma podemos observar os seguintes comportamentos:

**Situação I:**

Se o campo: Código da Turma estiver com com valor diferente de "0" (zero), a Máscara da Turma não é aplicada, mantendo assim, o valor cadastrado;

**Situação II:**

Se o campo: Código da Turma estiver com com valor igual a "0" (zero), e não houver vínculo da Máscara da Turma no cadastro do Curso, ao salvar o cadastro da Turma, é apresentada a mensagem de alerta/notificação do RM, orientado a aplicação de um valor diferente de 0 (zero) no campo: Código da Turma, ou a aplicação de uma Máscara da Turma ao cadastro de Curso.

Importante:

O vínculo da Máscara da Turma ao cadastro de Curso se aplica por Coligada, ou seja, a sequência das Turmas serão contabilizadas por Coligada e não por Filial.
