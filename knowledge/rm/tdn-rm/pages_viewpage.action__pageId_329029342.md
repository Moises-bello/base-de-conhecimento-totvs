---
content_hash: 8e6382256e0c75d1cc4ff8368c8af19a3945a5f346408b38e7d8d2c3e85fbd89
fetched_at: '2026-06-29T00:08:48.917392+00:00'
page_id: '329029342'
product: rm
source: tdn-rm
title: 06- Geração e aplicação do modelo preditivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329029342
version: 20
---

O modelo preditivo é gerado a partir da execução de algoritmos de inteligência artificial, que analisam os dados dos alunos no passado, para aprender os padrões de comportamento desses alunos. Após esse aprendizado, o modelo é utilizado para tentar prever o comportamento dos alunos matriculados na instituição de ensino.

Na Figura 1 podemos observar este processo, descrito detalhadamente logo abaixo.

Figura 1 - Etapas para geração da lista e perfis de prováveis evasores

### 1) Geração da Base de treinamento e de Teste

Inicialmente, é definido o período que deseja-se identificar os prováveis evasores, que vamos chamar de período de interesse. Sabendo-se o período de interesse, as bases de treinamento e de teste são geradas a partir dos dados de matrícula que antecedem esse período.

Supondo que deseja-se classificar os alunos do ano de 2019 (Figura 2), as bases de dados serão construídas da seguinte forma :

* a base de treinamento será composta por dados de matrículas concluídas e canceladas em períodos letivos finalizados até o final do ano de 2017.
* a base de teste será composta por dados de matrículas concluídas ou canceladas em períodos letivos pertencentes ao ano de 2018.

Figura 2 - Representação gráfica das bases de treinamento e de teste

### 2) Geração do Modelo Preditivo

A partir da base de treinamento criada, são utilizadas para identificação dos padrões de comportamento dos alunos e geração do modelo preditivo as seguintes informações:

* Informações Acadêmicas dos alunos:

a) Notas

b) Ausências

c) Carga de Disciplinas

* Informações Financeiras:

a) Pagamentos de Parcelas

* Quais alunos abandonaram a instituição de ensino.

**Observação**: Um estudante é considerado evasor quando seu último período letivo cursado não corresponde ao último período do seu curso. Considerando um curso de Direito com 10 períodos, por exemplo, um aluno que tem como último registro de matrícula o 9º período no 1º semestre de 2018 seria considerado como evasor neste semestre.

Após o treinamento, o modelo preditivo será capaz de fornecer as seguintes informações:

* Classificação, quanto à evasão: onde o modelo preditivo atribui a um estudante uma probabilidade de evasão e determina se ele é um provável evasor;
* Classificação, quanto ao perfil evasor: onde o modelo preditivo agrupa os estudantes com perfis semelhantes, considerando suas características acadêmicas e financeiras.

### 3) Validação do Modelo Preditivo

Uma vez gerado, o modelo preditivo é aplicado na base de teste e os resultados alcançados são comparados com dados reais do passado. Assim, é possível avaliar se o modelo alcançou uma boa precisão.

A precisão é calculada da seguinte forma:

Onde:

a = matrículas em períodos letivos da base de teste que foram canceladas e identificadas corretamente pelo modelo.

b = todas matrículas em períodos letivos da base de teste que foram canceladas.

### 4) Aplicação do Modelo Preditivo

Caso a precisão alcançada no treinamento seja boa, o modelo preditivo é aplicado nas matrículas do período de interesse, que no nosso exemplo é o ano de 2019.

Com estas informações os gestores da Instituição de Ensino poderão realizar ações para reter estes alunos.
