---
content_hash: 55c7f34042533bd47ad730fdc8d95dc87c74b920fd28e2c276585c03bdcabd43
fetched_at: '2026-06-29T00:09:50.801268+00:00'
page_id: '435113281'
product: rm
source: tdn-rm
title: API de Menus
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Menus
version: 28
---

# Sumário

---

10Sumário

# Objetivo

---

     Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

# 1 - Métodos

---

     A API de menu implementa somente o método GET, porém o mesmo aceita dois tipos de assinatura que são:

* {company}
* {company}/{parentId}

Onde company na linha RM representa a coligada e o parentId representa o ID do Menu que deseja exibir seus filhos.

# 1.1 - GET

---

     1.1.1 - Get (Retorna todos os módulos do RM que o usuário autenticado possui permissão na coligada informada no parâmetro company)

false1.1.1 GetfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus

falseExemplo de ResultadoVer resultado JSON...

{  
"hasNext": true,  
"menuItems": [  
{  
"id": "86624781592fa5e5dd649b57e1667df6",  
"name": "Gestão de Custos",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "6edb6b19adc2b967dcb6d225c5c089a8",  
"name": "Integração",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "2050d813014fc487ffead38ca1e49cdc",  
"name": "Inteligência de Negócios",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "b9982a14ccfb3d6c4b6a4e0406ea489a",  
"name": "Serviços Globais",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "7e128ef49d72932b49b6db15f2d24be3",  
"name": "Serviços Globais",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "8298bc939bc4a95a9c24f333cbdd6f35",  
"name": "Gestão do Relacionamento com o Cliente",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "f8811f490807addb6daa7c4de40ee4ac",  
"name": "Gestão do Relacionamento com o Cliente",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "394af69d94b0fe68f64ec7b61d211755",  
"name": "Manutenção",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "9b6531bd8da28ae8be6c2923d6c01114",  
"name": "Gestão de Conteúdos",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "6c4bd975a84afc3a7dc545ce1581fe5e",  
"name": "Gestão de Conteúdos",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "66c488e81895984a5de7be84067eb6a9",  
"name": "Gestão Contábil",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "0161f316970640a6bd3f8a53e6bd2561",  
"name": "Gestão Fiscal",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "1c8647a41151692197750531401956a6",  
"name": "Gestão Financeira",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "49512246df92fb8a5cddbc077df8b4b8",  
"name": "Gestão Financeira",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "ddc3337f62a6a45bcd0fd17d91996803",  
"name": "Gestão de Estoque, Compras e Faturamento",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "a25693005f36a69794a7acd9191c7ba1",  
"name": "Gestão de Estoque, Compras e Faturamento",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "d271f243a7d25db027ccf084ec91ced2",  
"name": "Avaliação e Pesquisa",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "7b5d93e8c314cd59ca8826b1c7ec2bc2",  
"name": "Gestão Bibliotecária",  
"type": "group",  
"custom": "Win"  
},  
{  
"id": "48513a97e0ff8ad23d541d07c471dbf0",  
"name": "Gestão Bibliotecária",  
"type": "group",  
"custom": "Web"  
},  
{  
"id": "8a554e97d5021b84e6d5d07b4568a348",  
"name": "Educacional",  
"type": "group",  
"custom": "Win"  
}  
]  
}

## 1.1.2 - Order(Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Campo:** name

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus?order=name

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Campo:** name

**Tipo de Ordenação:** Descendente

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus?order=-name

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Campo: custom**

**Valor:** win

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus?custom=win

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)

## 1.1.4 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Valor1:** 1

**Valor2:** 1

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus?page=1&pageSize=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**Campos:** id, name, custom

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus?fields=id,name,custom

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - GET {companyId}

---

1.2.1 - Get (Retorna o primeiro nível dos menus filhos que o usuário autenticado possui permissão na coligada informada no parâmetro company, referentes ao menu informado no parâmetro parentID)

false1.1.1 GetfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?companyId={CompanyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2.2 - Order(Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?order=[-]{campo}&{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Campo:** name

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?order=name&companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?order=[-]{campo}&/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Campo:** name

**Tipo de Ordenação:** Descendente

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?order=-name&companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2.3 - Filter (Resultado filtrado)

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?{campo}={valor}&/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Campo:** custom

**Valor:** success

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?custom=win&/companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2.4 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?page={valor1}&pageSize={valor2}/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Valor1:** 1

**Valor2:** 1

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?page=1&pageSize=1&companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2.5 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus/{parentID}?fields={campo}/{companyId}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Company: 1**

**ParentID:** b9982a14ccfb3d6c4b6a4e0406ea489a

**Campos:** id, name, custom

**Url Utilizada:** http://localhost:8051/api/framework/v1/menus/b9982a14ccfb3d6c4b6a4e0406ea489a?fields=id,name,custom&companyId=1

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2.6 - Desabilitar uso do OData e selecionar Tags

Parâmetros

**DisableODataFilter:** esse parâmetro tem a finalidade de desativar o recurso de OData da API, resultando em um desempenho mais rápido e eficiente na utilização da mesma.

**Exemplo:** ?**DisableODataFilter**=True

**TagsMenu:** esse parâmetro tem como objetivo permitir a especificação de quais tags serão incluídas na consulta, por meio da passagem de uma lista de identificadores. As tagsmenu passadas pelo parâmetro que irão determinar quais permissões de perfil que deve ser validadas. pela api, por padrão, todas as permissões de perfil são carregadas. Dessa forma, é possível obter apenas as informações desejadas e relevantes para a operação em questão fazendo com que a resposta da api seja mais rápida.

**Exemplo:** ?**TagsMenu**=800000010,800000015,826000037

falseFieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/menus?DisableODataFilter={disable}&TagsMenu={tags}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**DisableODataFilter:** True

**TagsMenu:** 999999903,999999902

**Url Utilizada:** <http://localhost:8051/api/framework/v1/menus?DisableODataFilter=True&tagsMenu=999999903,999999902>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true
