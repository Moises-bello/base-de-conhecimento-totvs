---
content_hash: 800e96025cd98797270306f19ad50463d22527b61ed463b8164a736648171c6e
fetched_at: '2026-07-02T19:24:26.799226+00:00'
page_id: '654947393'
product: protheus
source: tdn-tec
title: 1 - A História
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654947393
version: 5
---

Inicialmente ele foi concebido para atender os testes unitários do desenvolvimento dos componentes da linguagem TLPP, portanto ele era somente uma iniciativa tímida para atender uma necessidade específica.

A decisão de criar algo novo deu-se pelo fato de que as funcionalidades do TLPP devem funcionar corretamente sem que haja dependências de nenhum outro produto.

Umas das premissas para essa iniciativa era utilizar em grande escala os recursos nativos da linguagem, não somente em testes específicos como também na construção do motor de testes, por isso é todo construído utilizando recursos novos do TLPP, tal como:

* [Namespaces](https://tdn.totvs.com/display/tec/Namespace)
* [Nomes longos](https://tdn.totvs.com/display/tec/Nomes+longos)
* [Reflection e Annotation](https://tdn.totvs.com/display/tec/Reflection+e+Annotation)
* [Tipagem de dados](https://tdn.totvs.com/pages/viewpage.action?pageId=579304379)
* [RegEx](https://tdn.totvs.com/display/tec/RegEx)
* [REST](https://tdn.totvs.com/display/tec/REST)

Com a concepção do tlppCore, RPO que é expedido juntamente com o AppServer da TOTVS, contendo recursos novos da linguagem e produtos nativos à tecnologia TOTVS, houve a necessidade de ampliar a abrangência do Motor de Testes.

Logo vimos que o Motor precisava mais do que atender testes unitários, necessitava também de Testes Integrados, Testes Sistêmicos, Testes Funcionais e Testes de Versões.

Além disso nosso cenário de ambiente de testes cresceu consideravelmente, tal como testar ambiente de desenvolvimento, ambiente Master e o ambiente final chamado Stable, isso tudo para Windows, Linux utilizando AppServer Lobo-Guará e Harpia.

Resumidamente o motor deixou de ser um Motor de Testes Unitários para um MOTOR DE TESTES.

Abaixo podemos ver uma breve "timeline" das principais funcionalidades e evolução da ferramenta:

Após tantos recursos implementados e qualidade alcançada, nos sentimos motivados em compartilhar com todos esta ferramenta e acreditamos que pode ser útil para nossos clientes e parceiros assim como é para nós!  
  
Portanto batizamos a ferramenta como PROBAT, palavra com origem do Latim na qual remete à qualidade, que é o que desejamos que você alcance em seu projeto de software.

Seja bem vindo!
