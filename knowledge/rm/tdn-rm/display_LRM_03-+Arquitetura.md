---
content_hash: 68e4a3b0094b9a4110710b87a36ad517744451953fcd0f0bd5930e6ffbef3846
fetched_at: '2026-06-29T00:08:48.913324+00:00'
page_id: '329029340'
product: rm
source: tdn-rm
title: 03- Arquitetura
type: documentation
url: https://tdn.totvs.com/display/LRM/03-+Arquitetura
version: 42
---

Na Figura 1 está representado a arquitetura da solução Retenção de Alunos.

Figura 1 - Arquitetura da solução Retenção de Alunos

A seguir, cada um destes componentes é detalhado:

### Fonte de dados

É a fonte de informações que serão utilizados pelo Retenção de Alunos. Atualmente, a principal fonte de dados utilizada é o sistema de gestão educacional da instituição de ensino. Entretanto, é possível configurar outras fontes de informação como redes sociais, sistema de catraca, planilhas, entre outros.

### Carol Conector (2C)

É a ferramenta responsável por enviar as informações das fontes de dados para a CAROL.

### CAROL

É uma plataforma de dados que oferece diversas possibilidades. No aplicativo Retenção de Alunos, são utilizados os seguintes recursos:

* **MDM**

Gerenciamento de dados mestre, ou master data management (MDM), pode ser entendido como um banco de dados que contém tabelas, conhecidas como Staging Tables e Data Models, cujos dados são organizados em colunas e são alimentados por diversas fontes de dados.

Staging Tables são as tabelas que inicialmente recebem os dados das fontes de dados da aplicação. Já o Data Model é o resultado final da combinação de um conjunto de registros provenientes de uma ou mais Staging Table.

1. Cada conector envia para a plataforma CAROL um conjunto de dados;
2. Este dados são armazenados em Staging Tables.
3. Os registros das Staging Tables são transformados, respeitando-se algumas regras pré-definidas, e o resultado será utilizado para preencher os Data Models.

* **Inteligência artificial:**

É o componente responsável pelos recursos de inteligência artificial da plataforma que pode ser divididos em duas categorias:

a) Algoritmos preditivos: baseiam-se na aplicação de técnicas de aprendizado de máquina em alunos que já passaram pela instituição e cujas condições de conclusão ou abandono de cursos são conhecidas para, desta forma, obter modelos que antecipem o comportamento destes alunos num futuro próximo. 

b) Algoritmos NLP: baseiam-se na aplicação de técnicas de processamento de linguagem natural e permite a interação do usuário com a solução por meio de comandos de voz.

* **Carol App**

Um carol APP, é um aplicativo hospedado na CAROL que utiliza alguns de seus recursos. No contexto da solução Retenção de Alunos, é o sistema de BI que possibilita a visualização de algumas informações sobre a evasão escolar na instituição e as principais características dos estudantes como rendimento, frequência, financeiro, etc.
