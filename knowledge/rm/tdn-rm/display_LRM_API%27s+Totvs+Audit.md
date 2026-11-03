---
content_hash: 44a551fd2ce59344439a2111efc26b13e2f24b16f5bac2b5f9b9ac38b06d31c7
fetched_at: '2026-06-29T00:11:55.787140+00:00'
page_id: '864324708'
product: rm
source: tdn-rm
title: API's Totvs Audit
type: documentation
url: https://tdn.totvs.com/display/LRM/API%27s+Totvs+Audit
version: 1
---

Utilização com token CLOUDRM

As senhas das rotas de API que utilizam token CLOUDRM podem ser geradas através do software disponibilizado pela framework **RmApiKeyGenerator**. Para mais informações de como utilizar esse software acesse a documentação: . Este recurso esta disponível a partir da versão 12.1.2402.

Este documento tem como objetivo explicar como utilizar as API's do TOTVS Audit.

Observação

Em ambientes que possuem a definição de **SubDomainMask**, a base de dados será recuperada automaticamente a partir da URL, como é o caso do ambiente **Multi Tenancy**.

Mais detalhes sobre esse carregamento do alias podem ser encontrados em: <https://tdn.totvs.com/x/9XwcEQ>

Em ambientes que não possuem a definição de **SubDomainMask**, é necessário configurar a tag **DefaultDB** no arquivo de configuração do serviço.

## Routes:

## /api/totvs-audit/v1/totvs-audit-config/alias

### Get

Retorna o nome do alias que será utilizado pelo TOTVS Audit

### Autenticação

Basic Auth: Login e Password do Banco

### Resposta

bash1Response

### Paramêtros

Não possui parâmetros

## /api/totvs-audit/v1/totvs-audit-config

### Get

Retorna as Configurações do Totvs Audit

### Autenticação

Basic Auth: Login e Password do Banco ou usar /api/totvs-audit/v1/totvs-audit-config/token-auth para Configuração por token:

Type Api Key:

Key: CLOUDRM

### Resposta

bash1Response,
    "EnabledLogLGPD": 
}]]>

### Paramêtros

"Schema": Nome do Schema utilizado pelo TOTVS Audit

"Enabled": Status do TOTVS Audit

"EnabledLogLGPD": Status do TOTVS Audit para tabelas LGPD

### Post

Aplica configuração pendentes do TOTVS Audit.

Ao executar outras rotas do TOTVS Audit as configurações vão ficar marcadas como pendentes, a responsabilidade desta rota é aplicar estas configurações

### Autenticação

Basic Auth: Login e Password do Banco

ou

usar /api/totvs-audit/v1/totvs-audit-config/token-auth para Configuração por token:

Type Api Key:

Key: CLOUDRM

### Requisição

bash1Request,
  "EnabledLogLGPD": ,
  "NoUseRequirements": 
}]]>

### Paramêtros

"Enabled": Status do TOTVS Audit

"EnabledLogLGPD": Status do TOTVS Audit para tabelas LGPD

"NoUseRequirements":  Define se irá ignorar os pré requisitos de execução do totvs audit

Versão 12.1.2402

As rotas abaixo estão dísponiveis a partir da versão 12.1.2402.

## /api/totvs-audit/v1/totvs-audit-config/audit-tables

### Get

Retorna tabelas ativas no totvs audit

### Autenticação

Basic Auth: Login e Password do Banco

ou

usar /api/totvs-audit/v1/totvs-audit-config/audit-tables/token-auth para Configuração por token:

Type Api Key:

Key: CLOUDRM

### Resposta

bash1Response,
"update": ,
"insert": 
},
],
"lgpdAuditTables": [ #Lista de tabelas
{
"name": "TableName",
"delete": ,
"update": ,
"insert": 
},
]
}]]>

### Paramêtros

"auditTables": Tabelas que estão configuradas manualmente para serem auditadas

"lgpdAuditTables": Tabelas que estâo configuradas automaticamente pela LGPD para serem auditadas

"name":  Nome da Tabela

"delete": Status da auditoria de Deletes da tabela

"update": Status da auditoria de Updates da tabela

"insert": Status da auditoria de Insert da tabela

### Post

Configura as tabelas solicitadas para serem ativadas no Totvs Audit e recebe como parâmetros a lista de tabelas que deseja alterar as configurações de auditoria, Sendo obrigatório informar os parâmetros Update, Insert e Delete de cada tablela.

Caso deseje que uma tabela não seja auditada definir todos os parâmetros da mesma como false.

### Autenticação

Basic Auth: Login e Password do Banco

ou

usar /api/totvs-audit/v1/totvs-audit-config/audit-tables/token-auth para Configuração por token:

Type Api Key:

Key CLOUDRM

### Requisição

bash1Request,
"insert": ,
"update": 
}
]
}]]>

### Paramêtros

"auditTables": Tabelas que serão configuradas  para serem auditadas

"name":  Nome da Tabela

"delete": Status da auditoria de Deletes da tabela

"update": Status da auditoria de Updates da tabela

"insert": Status da auditoria de Insert da tabela
