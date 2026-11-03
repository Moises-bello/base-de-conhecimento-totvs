---
content_hash: f8f34f8d8b5db61f32c5e44ef08297b5eb73c8cec372fd76cd3dc603a0719960
fetched_at: '2026-06-29T00:12:01.607284+00:00'
page_id: '896383405'
product: rm
source: tdn-rm
title: 1 – Conhecendo a pirâmide de Teste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896383405
version: 10
---

A Pirâmide de Testes é um conceito essencial que organiza os diferentes tipos de testes em camadas, de modo a maximizar a eficiência e minimizar o custo. Ela é composta por:

* **Testes Unitários**: A base da pirâmide. São testes rápidos e mais baratos, que validam pequenas unidades de código.
* **Testes de Integração**: Valida a interação entre diferentes unidades ou módulos.
* **Testes End-to-End**: No topo da pirâmide, validam o sistema como um todo, simulando o comportamento do usuário. São testes mais lentos e mais caros.

Entender a pirâmide ajuda a focar no equilíbrio certo de testes, priorizando aqueles que são mais baratos e rápidos de executar.  
Quanto mais alto seu teste estiver na pirâmide, mais caro e lento ele será.

No nosso caso, utilizando o **TOTVS Automação de Testes** , temos atividades específicas para o teste de **Integração** (**WebService e API´s**) e para o teste **End-to-End** (**Script Winforms, Selenium**).

Vamos sempre optar por criar testes de **Integrações** por serem mais baratos e rápidos. Utilizaremos testes **End-to-End** somente em casos específicos onde não for possível utilizar testes de integrações ou for realmente necessário testar a tela do sistema.

[←](https://tdn.totvs.com/pages/viewpage.action?pageId=896383724) [Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=895612217) | [Próximo →](https://tdn.totvs.com/pages/viewpage.action?pageId=896383724)
