---
article_id: 360060272254
category: SIGAEST - LEGAIS
content_hash: 2e90d74899be11f2e9e23cab6ea9f5de302552aa110e1f3f9f1482ddebdfe09f
fetched_at: '2026-06-28T22:38:51.937259+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - Geração do SPED Fiscal com Bloco K em Looping
type: support-article
updated_at: '2026-06-11T15:14:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060272254-MP-SIGAEST-Gera%C3%A7%C3%A3o-do-SPED-Fiscal-com-Bloco-K-em-Looping
---

**Dúvida**

Ao gerar o Sped Fiscal (rotina SPEDFISCAL) com a pergunta "Gera Bloco K = Sim", o Protheus fica processando e não conclui a geração do arquivo. O que fazer para resolver?

**Ambiente**

Microsiga Protheus - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Para solucionar este problema, siga os passos a seguir:

**1. Certifique-se de que o seu ambiente está atualizado:**

Abaixo os pacotes Acumulados de Estoque e Livros Fiscais.

***Pacotes acumulados Estoque/Custos:***

**12.1.27**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571)* **|** **12.1.25**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640)* **|** **12.1.23**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)*

***Pacotes acumulados Livros Fiscais:***

**12.1.27**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585)***| 12.1.25**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589)* **| 12.1.23**- *[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)*

**2. Se persistir, analisar via DBTrace ou tabela CV8**

Para melhor diagnóstico do ponto chave em que o processamento está "travando" ou ficando em looping, a melhor forma é analisando via LogProfiler. Então, para habilitá-lo (e tentar identificar qual função ou ponto a rotina está travando), [**clique aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021553991-MP-SIGAFIN-Como-habilitar-e-gerar-o-LogProfiler-para-avalia%C3%A7%C3%A3o-de-desempenho-?source=search%20e%20https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024300052-MP-SIGACOM-Como-gerar-o-Log-DbTrace-para-monitorar-baixa-performance-para-rotinas-ADVPL?source=search)

**3. Em caso de dificuldades de identificação da causa raiz do problema, acione o nosso Suporte Técnico**

Caso mesmo com o ambiente atualizado e gerando o LogProfiler não identificar o ponto raiz do problema, acione o nosso time de Suporte Técnico para o devido auxílio e identificação o problema.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
