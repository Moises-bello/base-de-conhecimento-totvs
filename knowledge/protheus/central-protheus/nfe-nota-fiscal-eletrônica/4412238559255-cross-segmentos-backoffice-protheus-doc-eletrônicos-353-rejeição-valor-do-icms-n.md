---
article_id: 4412238559255
category: NFe - Nota Fiscal Eletrônica
content_hash: 07c755df7014b3b57ed3ad339a03dfeaaaa387f3d98ce1b90f6719dd0a24946a
fetched_at: '2026-06-28T22:40:03.942741+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 353 Rejeição: Valor
  do ICMS no CST=51 não corresponde a diferença do ICMS operação e ICMS diferido'
type: support-article
updated_at: '2025-07-09T12:39:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412238559255-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-353-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-no-CST-51-n%C3%A3o-corresponde-a-diferen%C3%A7a-do-ICMS-opera%C3%A7%C3%A3o-e-ICMS-diferido
---

**Dúvida**Como solucionar a rejeição abaixo:

353 Rejeição: Valor do ICMS no CST=51 não corresponde a diferença do ICMS operação e ICMS diferido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - É necessário verificar se foi configurado corretamente no sistema a **nota de diferimento:**

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=654111155>. 

2 - Verifique no configurador se os parâmetros abaixo, **estão configurados dessa forma:**

**MV\_RNDICM = .T.**

Indica o padrão de arredondamento no cálculo do ICMS.  
**T** - Arredonda o valor.  
**F** - Não arredonda, apresenta o valor truncado.

**MV\_RNDSOBR = .T.**

Sempre que o **RNDSOBR** estiver como Falso, não teremos o tratamento das sobras e consequentemente os valores serão truncados por item.

Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* também como Verdadeiro, será efetuado o tratamento de arredondamento por item.

Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* como falso, será efetuado o tratamento de arredondamento no total do imposto (truncando por item e considerando a sobra).

**MV\_RNDPREC = 2**

Indica a precisão para o critério de arredondamento dos cálculos fiscais do Sistema, em que:  
**< 3**, o critério de precisão para arredondamento é 10 casas decimais, mantendo o número padrão do Sistema.

**>=3**, define um novo critério de precisão para o arredondamento.

Exemplo: Se o conteúdo do parâmetro for configurado com **3**, indica que um determinado número será truncado na terceira casa decimal de onde partirá o cálculo. Assim, se tivermos o valor de R$ 0,3549 para um determinado imposto, este número será truncado na terceira casa decimal em R$ 0,354 e, a partir deste ponto é efetuado o arredondamento.

3- Altere no  configurador os campo **F4\_PICMDIF e CD2\_PICMDIF conforme o exemplo abaixo:**  
​

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33347978788887)

4-  Caso seja diferimento parcial  é necessário que o campo no TES  Perc. ICM Dif **F4\_PICMDIF** = 33,3333 por exemplo.

5- Após isso, **exclua a nota e gere novamente.**

**Saiba mais:**

Quando for nota para UF do RJ para atender a resolução 13 a opção do diferimento que deve ser utilizada é a 7 conforme o link abaixo:

[MP - FIS - Configuração do calculo para o ICMS DIFERIDO Resolução SEFAZ 13/2019 RJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026830373)

* Para gerar diferimento com FECP conforme a **nota técnica 2020.005,** realizar as atualizações do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412238543511)**
