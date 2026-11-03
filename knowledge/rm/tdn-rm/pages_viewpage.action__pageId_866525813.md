---
content_hash: 0e9f59f071b9e31385ea98ca514112828c5f4e75fb230a6c6983edc59d0131a0
fetched_at: '2026-06-29T00:11:56.458301+00:00'
page_id: '866525813'
product: rm
source: tdn-rm
title: Api's de modelos de negócio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866525813
version: 6
---

# **Resumo**

Este manual tem como objetivo orientar a criação e utilização de uma API para listar dados de uma entidade específica, baseada em um modelo previamente definido.

# **Sobre**

1. **Serviço Utilizado:** Para transformar o modelo em uma entidade utilizável, deve-se utilizar o serviço BusinessModelCodeToBusinessModelSchema. Esse serviço converte o modelo de dados especificado no endpoint em um formato apropriado para manipulação e retorno de dados.

**Endpoint de Exemplo:** O acesso à API para listagem de dados de um modelo específico é feito por meio de uma requisição GET. Abaixo, um exemplo do formato de endpoint que deve ser utilizado:  
GET <http://localhost:8051/api/framework/v1/smartx/datamodel/data/GlbUsuarioModel>

1. Nesse exemplo, a API retornará os dados da entidade relacionada ao modelo GlbUsuarioModel.

# **Obrigatoriedade**

Para garantir o correto funcionamento e alinhamento com os padrões estabelecidos, os seguintes critérios foram definidos:

1. **Retorno de Dados:** A API **deve** retornar apenas os dados da entidade principal (entidade pai) associada ao modelo fornecido. Os dados das entidades filhas ou relacionadas não devem ser incluídos nesse retorno inicial.
2. **Conformidade com o Guia de API TOTVS:** A API **deve** seguir o guia de boas práticas da TOTVS para a formatação e estruturação do retorno dos dados. Isso inclui padrões de nomenclatura, formatação de resposta, e headers adequados. [Guia de implementação de API V2.0](https://tdn.totvs.com/pages/releaseview.action?pageId=484701395#Guiadeimplementa%C3%A7%C3%A3odeAPIV2.0-Ordena%C3%A7%C3%A3o)
3. **Sem Ordenação de Dados:** Neste momento, a API **não deve** implementar a ordenação dos dados retornados. A ordem dos registros será baseada na inserção ou em outro critério padrão, mas sem suporte a parâmetros de ordenação na requisição.
4. **Sem Recurso de** ***Fields*****:** O recurso que permite a seleção de campos específicos para exibição (conhecido como *fields*) **não deve** ser implementado agora. Assim, todos os campos definidos no modelo serão retornados integralmente, sem a possibilidade de omitir campos.
5. **Sem Filtros de Dados:** A API **não deve** implementar filtros de dados, sejam eles simples ou complexos. Neste momento, o retorno será de todos os registros sem a possibilidade de aplicar condições de filtragem.
