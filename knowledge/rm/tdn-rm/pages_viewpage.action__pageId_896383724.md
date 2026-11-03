---
content_hash: c697e8b288e833e6fdc5dc266376c08aa3c7cdc51e97e8256fed38f2a34b4241
fetched_at: '2026-06-29T00:12:01.610252+00:00'
page_id: '896383724'
product: rm
source: tdn-rm
title: 2 – Entendendo o que são testes funcionais automatizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896383724
version: 7
---

Os testes funcionais automatizados são uma forma de validar as funcionalidades do sistema usando ferramentas ou scripts de automação, em vez de execução manual. Esses testes reproduzem ações de um usuário ou interações com sistemas externos, verificando os resultados automaticamente.

## Características dos testes funcionais automatizados:

* Testam funcionalidades de um sistema
* Teste de Regressão (Garante que o que funcionava continua funcionando)
* Teste feito alimentando a entrada e validando as saídas
* Execução automática sem intervenção humana
* Simula a interação com o software como um usuário final
* Os testes seguem um script (Caso de Teste)
* Os testes são repetíveis

## Benefícios dos Testes Funcionais Automatizados

* **Eficiência e rapidez**: Execução de testes é muito mais rápida em comparação com a manual.
* **Cobertura maior**: Permite testar mais cenários em menos tempo.
* **Consistência**: Elimina o risco de erros humanos durante a execução dos testes.
* **Reutilização**: Scripts podem ser reutilizados em diferentes ciclos de desenvolvimento.
* **Integração contínua**: Facilita a validação em pipelines de DevOps.
* **Redução de custo**: Reduz o custo com pessoal para realização de testes manuais
* **Evolução gradual**: Você consegue aumentar seus cenários de testes gradualmente

Testes funcionais automatizados são criados uma única vez e podem ser executados repetidamente, economizando tempo e esforço em testes repetitivos.

## Estrutura de testes automatizados

Ao criar e executar um teste funcional automatizado, é importante seguir uma estrutura bem definida para garantir a confiabilidade e repetibilidade dos testes.

Os testes funcionais automatizados seguem a seguinte estrutura:

1. **Preparação do Ambiente**: Essa etapa envolve configurar o ambiente necessário para executar o teste. Isso inclui garantir que o sistema esteja em um estado inicial previsível e pronto para o teste, eliminando interferências externas que possam causar inconsistências.
2. **Testar a regra de negócio**: Nesta etapa, a funcionalidade ou regra de negócio que está sendo testada é executada. Esse é o núcleo do teste funcional automatizado, onde o sistema é testado em relação ao comportamento esperado.
3. **Validação do Teste**: Depois de executar a funcionalidade, esta etapa verifica se o comportamento do sistema está conforme o esperado. Isso pode incluir validar respostas, mudanças no estado do sistema, dados na base ou a saída gerada pelo teste.
4. **Restaurar o ambiente**: Para garantir que o ambiente fique limpo e preparado para testes futuros, é necessário restaurá-lo ao estado inicial após o término do teste. Isso é especialmente importante para evitar que um teste impacte outros

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896383405) | [Próximo](https://tdn.totvs.com/pages/viewpage.action?pageId=896383780) [→](https://tdn.totvs.com/pages/viewpage.action?pageId=896383780)
