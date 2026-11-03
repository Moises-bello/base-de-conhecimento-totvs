---
article_id: 4404777944215
category: SIGAEST - LEGAIS
content_hash: 26d1ee60fda0ef082cbd3fcf173f404452f968b80710be87e710f9e828d9d18f
fetched_at: '2026-06-28T22:38:51.861880+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPED FISCAL - Registro
  K280 gerando indevidamente
type: support-article
updated_at: '2025-03-12T12:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404777944215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPED-FISCAL-Registro-K280-gerando-indevidamente
---

**Dúvida**Ao emitir o SPED Fiscal com Bloco K com escopo reduzido (K200/K280), está gerando registros K280 indevidos. Como corrigir este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Normalmente registros K280 são gerados quando há apontamento de correção com relação a um periodo de apuração imediatamente anterior.

**Por exemplo:**

* MATA261 - Transferência de produtos
  + Ocorre através da opção estorno
* MATA242 - Desmontagem
  + Ocorre através da opção estorno
* MATA103 - Documento de Entrada
  + Apontamento de produção em terceiros
    - Ocorre através da opção excluir
  + Apontamento de produção conjunta em terceiros
    - Ocorre através da opção excluir

**Vamos a um exemplo prático onde o K280 é gerado indevidamente**

Em um cenário onde temos:

PA5: Qtde 100

PA6: Qtde 0

No mês de maio, faremos uma Transferência (MATA261) do PA5 para o PA6 de quantidade 25:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404777745943)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404777751319)

Emissão do SPED de Maio (rotina SPEDFISCAL):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404770694807)

Neste exemplo, usaremos o Escopo Reduzido do Bloco K (K200/K280:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404777786007)

Resultado:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404777790615)

No mês de Junho, o produto não passou por **nenhum** estorno de movimento feito em Maio.

Emissão do SPED de Junho:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404770749591)

Neste caso, gerou, **indevidamente**, registro K280, já que não houve estornos de movimentos de Maio:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404777827095)

**Como corrigir este problema?**

Normalmente este problema ocorre quando há fontes responsáveis pela montagem dos registros do SPED Fiscal no bloco K em desacordo. Para isso, basta aplicar o pacote Acumulado de Livros Fiscais e Estoque, onde possuem os fontes responsáveis pela correta geração do bloco K:

**Atualização**: [Atualizacao Backoffice Protheus](https://tdn.totvs.com/x/2hgdHw)

|  |
| --- |
| *Em conformidade com o compromisso de evolução do produto, a Engenharia Protheus uniu a expedição contínua dos módulos que compõem o **Backoffice Protheus** num único pacote acumulado, **suspendendo expedições isoladas para cada módulo**.*  *Essa estratégia garante mais simplicidade no processo de atualização, e mais confiabilidade garantindo compatibilidade entre os fontes que se relacionam.* |

**OBS:** Sempre aplicar pacotes de atualização primeiramente em ambiente de homologação com backup prévio.

Recomendamos fortemente que sempre mantenha o seu ambiente atualizado com os artefatos e acumulados mais atuais do Protheus e Módulos:

**[Central de Atualizações - LIB - Acumulados - Binários](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
