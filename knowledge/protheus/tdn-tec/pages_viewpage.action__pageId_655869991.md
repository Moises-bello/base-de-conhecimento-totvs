---
content_hash: 0f47ce9fc21b87506220cfa09f3588503a1d01f4f7d38efcc882f420dce7fef8
fetched_at: '2026-07-02T19:24:27.048437+00:00'
page_id: '655869991'
product: protheus
source: tdn-tec
title: c - Impondo a cobertura de código
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655869991
version: 2
---

Nós já vimos o recurso de cobertura de código em [Recursos Avançados] na sessão de Construindo testes.

Aprendemos que para ativar existem chaves de configuração no INI do appserver.

Porém há uma forma de ativar e desativar a Cobertura de Código independentemente da chave o INI em tempo de execução dos testes.

E como podemos fazer isso?

## Ligando Coverage

Podemos ligar por algumas formas:

c#

```

```

## Desligando Coverage

Podemos desligar por algumas formas:

c#

#### Importante:

Vale ressaltar que os modos apresentados acima terão prioridade sobre a configuração do INI, ou seja, se no INI estiver ligado o coverage, porém usaram 'coverage:off' no parâmetro da RUN, o Coverage será desligado em tempo de execução e a chave INI será ignorada.
