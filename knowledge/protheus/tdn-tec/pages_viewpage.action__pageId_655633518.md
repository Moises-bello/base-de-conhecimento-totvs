---
content_hash: f298ce986a355fd14184f5d52d047f8d6079830f937a0c48605fd2520f6c86d4
fetched_at: '2026-07-02T19:24:27.024649+00:00'
page_id: '655633518'
product: protheus
source: tdn-tec
title: e-6 - Cobertura de Código
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655633518
version: 12
---

Escrevemos nossos testes esperando avaliar a qualidade das nossas aplicações, descobrindo se as funcionalidades estão corretas ou não. Porém, como saber se tais testes estão percorrendo todas as linhas codificadas de nossos projetos?

Os testes passam por todos os caminhos (felizes, infelizes, alternativos ou inesperados) ? Todos os fluxos possíveis estão sendo testados?

Como saberemos se nosso código possui trechos sem utilidade e/ou que são inalcançáveis?

Não há como saber apenas olhando para os resultados dos testes, por isso será necessário utilizar os conceitos de Cobertura de Código para responder esses questionamentos.

A Cobertura de Código nos propicia a utilização de métricas claras para obtenção do percentual de cobertura, como também é possível analisar visualmente seu código-fonte e observar de forma simples quais linhas foram executadas e quais linhas deixaram de ser testadas.

O **PROBAT** possui recursos suficientes para geração dos resultados de cobertura de código necessários para aprimorar a qualidade dos testes.

##### Ativando a Cobertura

Para acessá-los, é preciso primeiro ativar o recurso através da configuração do **PROBAT**, portanto basta na INI modificar as seguintes chaves:

```
[PROBAT]  
CODECOVERAGE=1
```

> O valor da chave [CODECOVERAGE] deve ser numérico, sendo (0=desligado) e (1=ligado)

Essa chave irá informar ao **PROBAT** que agora ele deverá ativar e registrar a cobertura de código de cada Teste executado.

Vale lembrar que a captação da informação de cobertura de código em tempo de execução é responsabilidade do appserver e ao **PROBAT** cabe avisar o appserver para captar esses valores e após isso, quantificar os valores, registrar os dados, validar os testes e gerar as exportações conforme configurações da Cobertura.

> Nota: a chave acima somente liga a Captação e registro dos resultados nas tabelas do SQLite

##### Recursos

Ao ativar, podemos ter acesso aos seguintes recursos:

* [Consolidação de Resultados](https://tdn.totvs.com/pages/viewpage.action?pageId=687762732)

  + Persistência em SQLite
  + Valores sintéticos e analíticos
* [Exportação](https://tdn.totvs.com/pages/viewpage.action?pageId=687762736)

  + XML
  + JSON
* [Validação](https://tdn.totvs.com/pages/viewpage.action?pageId=687762740)

  + Percentual mínimo de cobertura
  + Filtro por módulo
  + Modificando % por fonte
* [Extensão VsCode](https://tdn.totvs.com/pages/viewpage.action?pageId=687762745)

  + Visualização Cobertura por fonte
