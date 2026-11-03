---
content_hash: b7fc498ba00a3d44661a7512ef78378886dc0d775655ba1bf4558f09e0163c8d
fetched_at: '2026-07-02T19:24:27.896841+00:00'
page_id: '687762740'
product: protheus
source: tdn-tec
title: Validação de Cobertura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687762740
version: 2
---

Além de se obter as linhas de códigos cobertas pelos testes e seus respectivos percentuais de cobertura, podemos validar se atingimos um percentual mínimo de cobertura, caso contrário, será gerado erro e o resultado dos testes invalidado.

Para ligar a validação, basta na INI modificar as seguintes chaves:

```
[PROBAT]  
CODECOVERAGE=1  
CODECOVERAGE_PERCENT=80
```

> O valor da chave [CODECOVERAGE\_PERCENT] deve ser numérico e entre 0 e 100 O valor 0 [zero] significa que a validação está desativada. Valores acima de zero indicam o percentual mínimo que será aceito para todos os fontes.

No exemplo acima, definimos que o percentual mínimo de cobertura a ser atingido é de 80%.

Importante saber que esse percentual será usado para validar todos os fontes de seu projeto, porém existem recursos para que possam tanto modificar o percentual por fonte ou indicar ao **PROBAT** quais módulos (folders) serão validados pelo % informado.

#### Modificando % por fonte

Podem existir casos em que o percentual aplicados para todos os fontes não faça sentido a um ou outro fonte em específico.

Para isso o **PROBAT** tem um recurso específico para que possa ser alterado esse percentual por fonte, e iremos novamente recorrer ao arquivo-fonte de configuração com comando específico, sendo:

```
COVERAGE PERCENTAGE {%} NAMESPACE {"nome_namespace"} SOURCE {nome_fonte} TYPE {extensao_fonte}  
​  
COVERAGE PERCENTAGE {%} SOURCE {nome_fonte} TYPE {extensao_fonte}
```

> O valor passado para o namespace deve estar obrigatoriamente entre aspas.

Exemplo

```
#include 'tlpp-probat.th'  
​  
// Aplica o Percentual em:  
//    60%  
// para o fonte:  
//    calculos.tlpp  
// Que utiliza o namespace:  
//    prj.lib  
​  
  COVERAGE PERCENTAGE 50 NAMESPACE "prj.lib" SOURCE calculos TYPE tlpp  
​  
// Aplica o Percentual em:  
//    20%  
// para o fonte:  
//    formulas.prw  
  COVERAGE PERCENTAGE 20 SOURCE formulas TYPE prw
```

Ao final basta compilar o fonte em seu RPO!

#### Filtro de módulos

É possível indicar ao **PROBAT** quais módulos (folder e sub-folders) devem ser validados pelo percentual indicado, caso não seja informado esse filtro a validação será aplicada a todos os fontes.

Bom, pode parecer um recurso inútil à primeira vista mas imagine um projeto grande de desenvolvimento onde já existam módulos maduros e que podem ir para a produção ou serem publicados, e ao contrário, módulos ainda em desenvolvimento e que ainda não estejam alinhados com a qualidade exigida e portanto não faz sentido quebrar toda uma expedição por módulos ainda em processo de amadurecimento.

Para informar quais módulos devem ser validados, é simples, basta seguir a configuração no INI abaixo:

```
[PROBAT]  
CODECOVERAGE=1  
CODECOVERAGE_FILTER_SRC=pasta_1,pasta_2,pasta_3
```

> Os nomes das pastas (módulos) devem ser separadas por vírgula.

No exemplo acima, a validação de cobertura de código somente será aplicada aos fontes que pertençam hierarquicamente aos diretórios [pasta\_1], [,pasta\_2] e [pasta\_3].
