---
content_hash: c054f342537da161adf8d2c46013c796da7f4d1ff73fd05b21070dd7a87e3c1e
fetched_at: '2026-06-29T00:10:38.968257+00:00'
page_id: '545637912'
product: rm
source: tdn-rm
title: Filtro de WebServices
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtro+de+WebServices
version: 21
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Particularidades dos Produtos**

## **01. VISÃO GERAL**

    Em virtude da Lei Geral de Proteção de Dados, LGPD, estamos implementando uma série de funcionalidades em nossas aplicações.  
Uma delas, é uma camada de segurança específica para quem utiliza o acesso a dados do RM via Web Services. Este processo ganhou uma segurança específica para filtros de registros por usuário solicitante, restringindo assim acesso a dados pessoais/sensíveis.

## **02. EXEMPLO DE UTILIZAÇÃO**

    Foi criado o DataServer "TiPerfilData" para que seja utilizado como exemplo.

    A Tag de Segurança utilizada foi a Permissões de Segurança para o Wizard conforme print abaixo:

    Este exemplo é um DataServer de perfil onde o usuário só pode ver os perfis criados por ele mesmo. Caso o usuário possua a permissão que está informada no atributo serão listados todos os perfis. Está disponível o DataServer **TiPerfilData** no sistema para que o mesmo sirva de exemplo.

    Segue abaixo exemplo do projeto SoapUi para consumir o WS:



## **03. PARTICULARIDADES DOS PRODUTOS**

    Segue abaixo as documentações por produto, com as devidas particularidades.

TOTVS BackOffice

page10sidebarSecurityFilter\_BO

Totvs Gestão Financeira

[LGPD - Serviços Via WebService FIN](https://tdn.totvs.com/x/CMeVI)

Totvs Gestão Contábil

[LGPD - Serviços Via WebService CTB](https://tdn.totvs.com/x/hRXKI)

Totvs Gestão Patrimonial

[LGPD - Serviços Via WebService PAT](https://tdn.totvs.com/x/oRXKI)

[Encontrar mais resultados](https://tdn.totvs.com/dosearchsite.action?queryString=labelText:(SecurityFilter_BO)+AND+spacekey:(LRM)&type=page)

TOTVS Educacional

page10sidebarSecurityFilter\_EDU

[Encontrar mais resultados](https://tdn.totvs.com/dosearchsite.action?queryString=labelText:(SecurityFilter_EDU)+AND+spacekey:(LRM)&type=page)

TOTVS Obras & Projetos

page10truesidebarSecurityFilter\_CP

[Encontrar mais resultados](https://tdn.totvs.com/dosearchsite.action?queryString=labelText:(SecurityFilter_CP)+AND+spacekey:(LRM)&type=page)

TOTVS RH

page10sidebarSecurityFilter\_RH

[Encontrar mais resultados](https://tdn.totvs.com/dosearchsite.action?queryString=labelText:(SecurityFilter_RH)+AND+spacekey:(LRM)&type=page)

TOTVS Saúde

page10sidebarSecurityFilter\_Sau

[Encontrar mais resultados](https://tdn.totvs.com/dosearchsite.action?queryString=labelText:(SecurityFilter_Sau)+AND+spacekey:(LRM)&type=page)
