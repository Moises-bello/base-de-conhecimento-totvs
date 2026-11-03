---
content_hash: 3ecbcb1939f4ed4a67380ad07fa9ecbd61a7e233f393992655e433257a62b4e2
fetched_at: '2026-06-29T00:05:54.172476+00:00'
page_id: '1075951228'
product: rm
source: tdn-rm
title: Integração - OQDigital - Configurando
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075951228
version: 3
---

Abaixo está o trecho atualizado da documentação técnica, já incorporando a origem dos dados utilizados para criação automática do ambiente da incorporadora na OQ Digital.

Substitua a seção Provisionamento do Ambiente pela versão abaixo:

### Provisionamento do Ambiente

Pré-requisito

O cliente deve possuir slot OQ Digital ativo na licença.

Fluxo de Provisionamento

1. O cliente habilita a integração no RM/PI.
2. O RM/PI solicita a criação do ambiente da incorporadora na OQ Digital.
3. A OQ Digital cria automaticamente o ambiente da incorporadora.
4. O ambiente administrativo é disponibilizado.
5. As credenciais iniciais são enviadas para o e-mail da incorporadora.

Dados utilizados na criação do ambiente

Os dados enviados para a OQ Digital serão obtidos da Coligada 1 cadastrada na base RM.

Campos utilizados:

| Campo RM | Finalidade |
| --- | --- |
| EMAIL | E-mail principal da incorporadora |
| NOMEFANTASIA | Nome fantasia da incorporadora |
| NOME | Razão social da incorporadora |
| ESTADO | Estado da incorporadora |
| CIDADE | Cidade da incorporadora |
| TELEFONE | Telefone principal da incorporadora |
| CODCOLIGADA | Identificador da coligada no RM |
| CGC | CNPJ da incorporadora |

Essas informações serão utilizadas para provisionar automaticamente o ambiente e identificar a incorporadora na OQ Digital.

URL do ambiente

Padrão de acesso

[https://admin.qa.oqdigital.com/client/signin/{NOME\_INCORPORADORA}](https://admin.qa.oqdigital.com/client/signin/%7BNOME%5C_INCORPORADORA%7D)

Senha inicial da incorporadora

Senha padrão

TOTVSPI

Após o primeiro acesso recomenda-se que a senha seja alterada.

E adicione este trecho na documentação funcional, logo após a seção Habilitação da Integração:

### Dados Utilizados na Criação do Ambiente

Quando a integração for habilitada, o ambiente da incorporadora na OQ Digital será criado automaticamente utilizando as informações da Coligada 1 cadastrada no RM.

Serão utilizados dados corporativos como razão social, nome fantasia, CNPJ, cidade, estado, telefone e e-mail da incorporadora.

Esses dados servem para identificar e provisionar corretamente o ambiente da empresa na OQ Digital.

Processamento da Integração

Toda a integração entre o RM/PI e a OQ Digital será executada de forma assíncrona através do Host de Serviços da aplicação, garantindo que o processamento não impacte a operação dos usuários.

Os eventos de criação e atualização de corretores, leads, evolução de etapas, aquecimento de leads e evolução de vendas serão processados pelo Job:

```
ASYNC_TCGI - ImbOQDigitalProc
```

O processamento somente será realizado quando a integração com a OQ Digital estiver devidamente habilitada nos **Parâmetros Gerais do TCGI/PI**.

Para acompanhamento e auditoria da integração, o resultado de cada execução poderá ser consultado através do campo **"Resultado da Execução"** do Job, onde serão registradas informações sobre processamentos realizados, sucessos, alertas e eventuais erros encontrados durante a comunicação com a OQ Digital.
