---
content_hash: f96ff055a6c37d8f17b68978f02b91a3e8e78d029915f54eda11d0435b925842
fetched_at: '2026-06-29T00:06:14.692393+00:00'
page_id: '210048930'
product: rm
source: tdn-rm
title: 6. Configuração do TOTVSProfile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210048930
version: 7
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso.

Versão

 Disponível à partir da versão 12.1.8 da linha RM.

# Definição

O [TOTVSProfile](http://tdn.totvs.com.br/pages/viewpage.action?pageId=201724459) é um recurso que permite o gerenciamento de perfis de páginas no TOTVS HTML Framework.

# Criando a classe para manipulação do TOTVSProfile

O Framework RM criou um manipulador básico definido pela classe **RMSProfiler**. Ela define o método **DoGetProfileInfo**, no qual o desenvolvedor pode montar a lista de Profiles necessária.

Automaticamente ela também acrescenta nesta lista de Profiles o filtro (DataCode) **TableInfo** contendo os atributos dos campos (ColProps) de uma determinada tabela e as **TOTVSActions** padrões.

Para criar, siga os passos abaixo:

1. Crie uma classe server que herde de RMSProfiler
2. Sobrescreva o método DoGetTable e retorne a tabela que necessita já contendo as informações dos atributos (ColProps).

GlbColigadaProfilertruec#1

O JSON de retorno é o seguinte:

TOTVS Profiletruejs1true
