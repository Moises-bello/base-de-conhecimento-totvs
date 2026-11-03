---
content_hash: ccfbeabddfa92a1cd225bc9e0d2f6c5d4ace1b07a8c68bbd1e2073bdcac5b806
fetched_at: '2026-06-29T00:09:45.895424+00:00'
page_id: '435099861'
product: rm
source: tdn-rm
title: API de Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435099861
version: 27
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [Veja Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Método

---

false

* A API de Parâmetros retorna todos os parâmetros do sistema presente na classe de parâmetros e nas tabelas: GPARAMETROSSISTEMA, GPARAMS, GMAILPARAMS, GDEPPAR, GCCUPAR e GGOOGLESERVICE.
* É necessário utilizar o filtro "group.name" para informar qual servidor de parâmetros a API irá utilizar para apresentar os parâmetros.
* A propriedade systemParameterId é composta pela companyId|parameterCode, onde companyId é a Coligada e parameterCode é o nome do parâmetro. Nos parâmetros da GPARAMETROSSISTEMA e GPARAMS, não é possível informar a companyId, pois são parâmetros globais, que independem de coligada.

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os parâmetros do sistema)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url's Utilizada:**

* [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)
* [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=gparams](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)
* [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=gmailparams](http://localhost:8051/api/glb/v1/system-parameters?group.name=gmailparams)
* [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=gdeppar](http://localhost:8051/api/glb/v1/system-parameters?group.name=gdeppar)
* [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=gccupar](http://localhost:8051/api/glb/v1/system-parameters?group.name=gccupar)
* [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparams)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=ggoogleservice](http://localhost:8051/api/glb/v1/system-parameters?group.name=ggoogleservice)
falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON) - GPARAMETROSSISTEMAtrueA9CPrB4DxF97G/PSV7ng6A==082KMtFVWr/nPPqdVMULxA=="
}
],
"group": {
"name": "gparametrossistema",
"displayName": "Parâmetros do Sistema (RMSSystemParameter)",
"customData": ""
}
},
{
"scope": "Global",
"systemParameterId": "Tamanho Chave Simetrica",
"code": "Tamanho Chave Simetrica",
"type": "String",
"description": [
{
"language": "pt-BR",
"descriptionText": "Armazena o tamanho da chave de criptografia simétrica utilizada (Valores possíveis: 128 / 192 / 256)."
}
],
"value": [
{
"language": "pt-BR",
"parameterValue": "128"
}
],
"group": {
"name": "gparametrossistema",
"displayName": "Parâmetros do Sistema (RMSSystemParameter)",
"customData": ""
}
},
{
"scope": "Global",
"systemParameterId": "Nivel Log Comunicacao",
"code": "Nivel Log Comunicacao",
"type": "Int32",
"description": [
{
"language": "pt-BR",
"descriptionText": "Determina a quantidade de informações de logs que será armazenada a cada comunicação. Quanto mais alto o nível, mais informações (Valores possíveis: 0 / 1 / 2 / 3)."
}
],
"value": [
{
"language": "pt-BR",
"parameterValue": 0
}
],
"group": {
"name": "gparametrossistema",
"displayName": "Parâmetros do Sistema (RMSSystemParameter)",
"customData": ""
}
}
]
}]]>js1Resultado (JSON) - GPARAMStruejs1Resultado (JSON) - GMAILPARAMStruejs1Resultado (JSON) - GDEPPARtruejs1Resultado (JSON) - GCCUPARtruejs1Resultado (JSON) - GGOOGLESERVICEtrue

## 1.1.2 - Order(Resultado ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&order={{campo}}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** code

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** [http://localhost:8051/api/](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&order=code)[framework](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema)[/v1/systemParameters?group.name=gparametrossistema&order=code](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&order=code)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** code

**Tipo de Ordenação:** Descendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema&order=-code](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&order=code)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&{{campo}}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** code

**Valor:** Servidor

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema&code=Servidor](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&code=Servidor)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 2

**Valor2:** 2

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema&page=1&pageSize=2](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&page=1&pageSize=2)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueA9CPrB4DxF97G/PSV7ng6A==082KMtFVWr/nPPqdVMULxA=="
}
],
"group": {
"name": "gparametrossistema",
"displayName": "Parâmetros do Sistema (RMSSystemParameter)",
"customData": ""
}
},
{
"scope": "Global",
"systemParameterId": "Tamanho Chave Simetrica",
"code": "Tamanho Chave Simetrica",
"type": "String",
"description": [
{
"language": "pt-BR",
"descriptionText": "Armazena o tamanho da chave de criptografia simétrica utilizada (Valores possíveis: 128 / 192 / 256)."
}
],
"value": [
{
"language": "pt-BR",
"parameterValue": "128"
}
],
"group": {
"name": "gparametrossistema",
"displayName": "Parâmetros do Sistema (RMSSystemParameter)",
"customData": ""
}
}
]
}]]>

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campos:** code

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema&fields=code](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&fields=code)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)trueA9CPrB4DxF97G/PSV7ng6A==082KMtFVWr/nPPqdVMULxA=="
}
]
},
{
"code": "Tamanho Chave Simetrica",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": "128"
}
]
},
{
"code": "Nivel Log Comunicacao",
"type": "Int32",
"value": [
{
"language": "pt-BR",
"parameterValue": 0
}
]
},
{
"code": "Tamanho Minimo Compressao",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": "800"
}
]
},
{
"code": "Servidor",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Porta",
"type": "Int32",
"value": [
{
"language": "pt-BR",
"parameterValue": 0
}
]
},
{
"code": "Domínio",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Usuário",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Senha",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Url do Help Wiki",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Usuário do Help Wiki",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Senha do usuário Help Wiki",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Domínio do usuário Help Wiki",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
},
{
"code": "Concatena filtro de perfil com AND",
"type": "Boolean",
"value": [
{
"language": "pt-BR",
"parameterValue": false
}
]
},
{
"code": "Sistema de mensagens habilitado",
"type": "Boolean",
"value": [
{
"language": "pt-BR",
"parameterValue": false
}
]
},
{
"code": "Intervalo em minutos de pulling ao banco (host)",
"type": "Int32",
"value": [
{
"language": "pt-BR",
"parameterValue": 10
}
]
},
{
"code": "Intervalo em minutos de pulling ao host (client)",
"type": "Int32",
"value": [
{
"language": "pt-BR",
"parameterValue": 10
}
]
},
{
"code": "Endereço Alternativo do Licence Server",
"type": "String",
"value": [
{
"language": "pt-BR",
"parameterValue": ""
}
]
}
]
}]]>

## 1.1.6 - Fields &Order (Retornar os campos específicos em ordem)

---

Parâmetros

**Expand:** Parâmetro responsável pela especialização e ordenação de campos em um resultado.

**Exemplo:** ?fields=id&order=-id - Nesse exemplo, serão retornados o campo "id" de perfis e em ordem descendente.

false1.1.6 GetOnefalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters?group.name={{tabela}}&fields={campo}&Order={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor Campo Fields:** code

**Valor Campo Order:** code

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters?group.name=gparametrossistema&fields=code&order=-code](http://localhost:8051/api/glb/v1/system-parameters?group.name=gparametrossistema&fields=code&order=-code)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Atualiza o valor de um parâmetro)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters](http://localhost:8099/api/rm/glb/v1/systemParameters)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT

---

## 1.3.1 - Put (Atualiza o valor do parâmetro)

---

false1.3.1 PostfalseConfiguração

**Máscara de Url:** http://{{dominio}}:{{port}}/api/framework/v1/systemParameters/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 1|MASCARACC

**Url Utilizada:** [http://localhost:8051/api/framework/v1/systemParameters/1|MASCARACC](http://localhost:8099/api/rm/glb/v1/users/testeapiusuario)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)true
