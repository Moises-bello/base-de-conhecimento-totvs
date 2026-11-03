---
content_hash: 8970c2937e5053ebd8406fa41b61e40502572c2d3a8b6f25cfc1ad1ec0257bfe
fetched_at: '2026-06-29T00:11:45.720604+00:00'
page_id: '821188997'
product: rm
source: tdn-rm
title: Alterações nas configuração do portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821188997
version: 9
---

A partir da versão **12.1.2402** algumas configurações passam a ser desnecessárias, simplificando assim o processo de configuração. Na documentação referente ao passo a passo das configurações estas alterações estão descritas em cada etapa. A seguir segue um resumo dessas alterações:

1. Em [Configuração dos Novos portais >> Pré-requisito >> URL Rewrite >> Configuração Rewrite](https://tdn.totvs.com/pages/releaseview.action?pageId=837434579), a segunda regra do rewrite que se aplica às api's onde é necessário passar o alias selecionado, não é mais necessária, ficando apenas a primeira regra.
2. Em [Configuração dos Novos portais >> Pré-requisito >> URL Rewrite >> Configuração do config](https://tdn.totvs.com/pages/releaseview.action?pageId=837434579), a chave **SubDomainMask** não é mais necessária. Ficando assim a obrigatoriedade da remoção da mesma, **com exceção de ambiente** **multitenancy,** onde essa chave é obrigatória.
3. A etapa de [Configuração dos host's](https://tdn.totvs.com/pages/releaseview.action?pageId=837434579) não é mais necessária.
4. Em [Configuração portal](https://tdn.totvs.com/pages/releaseview.action?pageId=837434579) no parâmetro apiServer é possível configurar este parâmetro com um endereço diferente do utilizado para acessar o portal.
5. Em [Configuração portal](https://tdn.totvs.com/pages/releaseview.action?pageId=837434579) as chaves **multitenant** e **subDomainMask** devem ser **removidas** do arquivo com exceção de ambiente que esteja configurado como multitenant.

Para mais informações sobre estas alterações consultar a página referente a cada configuração.

Caso apresente a seguinte mensagem ao tentar logar no portal, favor verificar o item 2.
