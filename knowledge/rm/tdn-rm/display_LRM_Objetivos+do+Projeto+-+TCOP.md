---
content_hash: a5e6ffea7937149f1d7d4c37b02cb825d5dde50a0da1b47f38f06fb0b5ffa714
fetched_at: '2026-06-29T00:11:54.929093+00:00'
page_id: '859071180'
product: rm
source: tdn-rm
title: Objetivos do Projeto - TCOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Objetivos+do+Projeto+-+TCOP
version: 1
---

Nessa tela é possível cadastrar o objetivo do projeto

Os campos da tela de objetivos serão habilitados de acordo com tipo de grandeza definida no objetivo do projeto selecionado:

**Quando Eixo de Impacto for**  
Quantitativo  
  
Somente serão habilitados os campos:  
Limite Mínimo – Unidade definida no objetivo  
Limite Máximo - Unidade definida no objetivo  
  
Qualitativo  
  
Somente serão habilitados os campos:  
Lista de atributos qualitativos  
  
**Observações:**

* Quando o campo Valor Máximo for selecionado será atribuído ao campo Limite Máx. o maior valor permitido para o eixo de escala;
* Os fatores de escala terão sua definição de casas decimais própria, não seguindo a parametrização definida por projeto, uma vez que a escala é visível a todos os projetos e coligadas;
* Os campos seguirão a seguinte parametrização:
  + Limite Min. – 4 casas decimais;
  + Limite Máx. - 4 casas decimais;
  + Peso – 8 casas decimais

O intervalo definido nos atributos quantitativo de um fator de escala não poderá sobrepor o intervalo de um fator já cadastrado.  
  
**Exemplo:**  
Nulo: 0 - 5,  Baixo: 4 - 10 à Errado  
Nulo: 0 - 5,  Baixo: 5,0001 - 10 à Correto  
  
Quando um objetivo do projeto associado ao fator de escala for qualitativo, poderão ser associados vários atributos qualitativos a este objetivo. Porém um mesmo atributo qualitativo não poderá ser associado ao mesmo objetivo em fatores diferentes.   
**Exemplo:**  
**Errado**  
**Fator de escala                   Objetivo            Atributo qualitativo**  
Baixo                                    Qualidade            Irrelevante, Pouco relevante  
Médio                                    Qualidade            Irrelevante  
  
**Correto**  
**Fator de escala                   Objetivo            Atributo qualitativo**  
Baixo                                    Qualidade           Irrelevante, Pouco relevante  
Médio                                    Qualidade           Relevante   
  
**Quando Eixo de Probabilidade**

* Somente serão habilitados os campos os atributos quantitativos.
* Limite Mínimo – Unidade em %
* Limite Máximo - Unidade em %

**Observações:**

* Quando o campo Valor Máximo for selecionado será atribuído ao campo Limite Máx. o valor 100 %;
* Os fatores de escala terão sua definição de casas decimais própria, não seguindo a parametrização definida por projeto, uma vez que a escala é visível a todos os projetos e coligadas;
* Os campos seguirão a seguinte parametrização:
  + Limite Min. – 4 casas decimais.
  + Limite Máx. - 4 casas decimais.
  + Peso – 8 casas decimais

O intervalo definido nos atributos quantitativo de um fator de escala não poderá sobrepor o intervalo de um fator já cadastrado.  
  
Exemplo:

* Nulo: 0 - 5,  Baixo: 4 - 10 à Errado  
  Nulo: 0 - 5,  Baixo: 5,0001 - 10 à Correto

Informações Complementares | Anexo

**[Fator de Conversão para moeda do Projeto](https://tdn.totvs.com/pages/viewpage.action?pageId=859071079)**
