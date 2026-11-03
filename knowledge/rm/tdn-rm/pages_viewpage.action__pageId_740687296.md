---
content_hash: d645d35d4cb377756f67871ea60070deb718e731725b6ed25c2804a6868f4d16
fetched_at: '2026-06-29T00:11:31.548785+00:00'
page_id: '740687296'
product: rm
source: tdn-rm
title: Histórico Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=740687296
version: 12
---

Permite realizar toda a configuração do histórico.

# Cursos do Histórico

***Currículo e Oferta | Histórico | Cursos do Histórico.***

Cadastre os “Cursos do Histórico” e, em seguida, as “Séries do histórico” que farão parte do Histórico da Instituição de Ensino.

Exemplo:

* Ensino Fundamental e Ensino Médio

O Ensino Médio apresenta as seguintes Séries do histórico (1º Série, 2º Série e 3º Série).  
*Acesse:  Currículo e Oferta / Histórico /Cursos do Histórico. Em Anexos “Séries do histórico”.*

# *Partes do Histórico*

***Currículo e Oferta | Histórico | Partes do histórico.***

Em seguida cadastre as “Partes do Histórico” e as “Disciplinas do histórico” para que seja possível realizar o cadastro do “layout de importação” presente nos “grupos de séries”.

Tais partes já são pré-determinadas pelo ministério da educação como:

* Base Nacional Comum
* Parte diversificada

***Currículo e Oferta | Histórico | Disciplinas do histórico.***

Realize o cadastro das disciplinas do histórico. Essas disciplinas são identificadas no histórico importado do aluno e serão associadas às disciplinas da grade do aluno posteriormente.

Mas, o que seriam as Disciplinas do Histórico e porque não usar as mesmas disciplinas da grade do aluno?  
Exemplo: Temos as seguintes disciplinas da grade do aluno:

* Português
* Redação

No entanto no Histórico do Aluno apresentará apenas a disciplina **Língua Portuguesa,** assim unificamos mais de uma disciplina ou mesmo disciplinas com nomenclaturas diferentes em uma única Identificação.

**Importante!!!**

**Nessa tela também poderão ser incluídas disciplinas de Itinerário Formativo**

# Disciplinas do Histórico

Todos os registros de histórico devem possuir disciplinas. Se houver algum registro de histórico para o aluno sem disciplina, o relatório "EDUREL0001 - Histórico Escolar - Ensino Fundamental" não apresentará corretamente as notas de cada série.

***Currículo e Oferta | Histórico | Grupos de Séries | Séries.***

Nessa etapa definiremos os “Grupos de Série”, nos quais serão determinados o “Layout de importação” de disciplinas para o histórico com suas respectivas posições.

Vincule o “Curso” e suas “Séries” respectivas.

# Ordem da Série

Todas as séries devem possuir valor para o campo "Ordem". Essa informação é muito importante para a organização das notas no relatório "EDUREL0001 - Histórico Escolar - Ensino Fundamental". Sem essa informação as notas podem ficar fora de ordem.

Importante

**Apenas a ordem das séries pode ser configurada, e a posição irá variar de acordo com as séries existentes. Por exemplo, se não existir cadastrado a "1a Série" com a ordem 1, mas existir a "2a Série" com a ordem 2, o relatório irá apresentar a "2a Série" na primeira posição.**

# Layout de importação

***Currículo e Oferta | Histórico | Grupos de Séries | Layout de importação.***

Determine qual a parte do histórico e posição de cada disciplina do histórico.

***Currículo e Oferta | Disciplinas.***

Vincule as “Disciplinas do histórico” no cadastro de disciplinas (grade, etc.).

***Currículo e Oferta | Curso | Séries***

Vincule o “Curso” e o “Período do histórico” no cadastro do curso.

Assim com todos os cadastros necessários é possível fazer a “Geração do histórico”

# Itinerário Formativo do Histórico

Disponível apenas a partir das versões **12.1.2302.100** e **12.1.2306**.

Para que o menu Itinerário Formativo seja visualizado deve ser dado a permissão em seu perfil de acordo com a imagem abaixo:

  **Acessar MDI I Menu | Serviços Globais| Perfil | Educacional | Acesso ao Menus | Educacional | Currículo e oferta | Acadêmico | Histórico | Itinerário Formativo do histórico**

Para realizar o cadastro do Itinerário formativo do histórico, acesse: 

 **Currículo e oferta | Acadêmico | Histórico | Itinerário Formativo do histórico** 

Caso o parâmetro **Utilizar Histórico por Nível de Ensino** ( parâmetros | secretaria | geral 3/7 |) estiver marcado, ao criar um novo itinerário formativo de histórico ele será exclusivo para o nível de ensino atual, caso entre em outro nível de ensino este itinerário formativo do histórico criado não será visível.

# Área de conhecimento do Histórico

Disponível apenas a partir das versões **12.1.2302.111** e **12.1.2306**.

Para que o menu Área de conhecimento do histórico seja visualizado deve ser dado a permissão em seu perfil de acordo com a imagem abaixo:

  **Acessar MDI I Menu | Serviços Globais| Perfil | Educacional | Acesso ao Menus | Educacional | Currículo e oferta | Acadêmico | Histórico | Área do conhecimento do histórico**

Para realizar o cadastro do Área do conhecimento do histórico, acesse: 

 **Currículo e oferta | Acadêmico | Histórico | Área de conhecimento**
