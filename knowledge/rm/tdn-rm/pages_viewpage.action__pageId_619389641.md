---
content_hash: 01822868623cef9045891e22c60083fe5e72c6b9d1ccfe0d494425a2578263a7
fetched_at: '2026-06-29T00:11:03.161853+00:00'
page_id: '619389641'
product: rm
source: tdn-rm
title: Movimentos Gerados por Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619389641
version: 14
---

Para visualização dos movimentos gerados pelo processo de geração de movimento por competência temos agora a tela de visão "Movimentos Gerados por Competência" que possibilita ao usuário visualizar todos movimentos gerados por competência para os contratos conforme o filtro desejado. Vale ressaltar que essa tela visão só ficará disponível somente quando o sistema estiver configurado para utilização do recurso de geração de movimento por competência. E mostrará somente contrato com movimentos gerados. Caso o contrato não tenha movimento gerado, o mesmo não será exibido na visão.

ATENÇÃO

A tela de visão Movimentos Gerados por Competência estará disponível a partir das versões:

* 12.1.32: A partir do patch 12.1.32.103
* 12.1.31: A partir do patch 12.1.31.159
* 12.1.27: A partir do patch 12.1.27.363

A partir da *versão **12.1.2406,*** o serviço de geração do movimento por competência poderá utilizar recurso de fracionamento no processo.

Seguem as documentações com um melhor detalhamento técnico sobre a disponibilização do recurso, caso queiram utilizá-los via webservice:

- [Serviço Rest](https://tdn.totvs.com/x/IAXVMQ)

- [Webservice](https://tdn.totvs.com/x/4kbVMQ)

Observação

Na criação de filtro para os campos “Mês / Ano” e “Data de Competência Final” utilizar um período de data onde se encontrará a data desejada.

Exemplo:

* Retornar os dados onde o campo “Mês / Ano” é 05/2021.  Criar um filtro onde:

**>= (mês/ano da consulta) AND < (mês/ano subsequente)**.

A permissão para acessar a nova tela de visão será realizada pela configuração de permissão de acesso pelo perfil do usuário.

A tela de visão "Movimentos gerados por competência" ficará disponível no menu Financeiro / Contábil → Geração → NF-e.

A tela também ficará disponível na tela de visão de contrato pelo anexo "Movimentos Gerados por Competência".

Na realização de duplo clique nos dados retornados pelo filtro desejado, o sistema irá abrir a tela do movimento correspondente à linha selecionada para usuário. Isso possibilitará a visualização das demais informações do movimento gerado por competência.

Integração com Protheus

O sistema **não**exibirá as colunas de **Status, Ícone do Status, Segundo Número, Data de Entrega do Movimento, Data de Saída do Movimento e Data de Cancelamento do Movimento**, caso esteja parametrizado com as seguintes configurações:

* O parâmetro "Fiscal" **marcado** em Educacional | Integração | Protheus | Módulos integrados
* O parâmetro "Utiliza movimento por competência " **marcado** em Educacional | Integração | Fiscal
* Integração com o Protheus EAI 2.0 **ativa** em TOTVS linha RM, EAI 2.0
