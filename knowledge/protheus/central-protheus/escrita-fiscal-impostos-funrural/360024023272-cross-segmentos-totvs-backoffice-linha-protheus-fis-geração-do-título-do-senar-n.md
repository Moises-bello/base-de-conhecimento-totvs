---
article_id: 360024023272
category: Escrita Fiscal - Impostos - Funrural
content_hash: d9082248f4ea4f72d87417652306779b4558621e708f131448bc041408ffaf38
fetched_at: '2026-06-28T22:39:28.159734+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Geração do Título
  do SENAR no Financeiro.
type: support-article
updated_at: '2022-11-01T18:03:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024023272-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-do-T%C3%ADtulo-do-SENAR-no-Financeiro
---

**Dúvida**

Como gerar o título do SENAR no financeiro?

**Ambiente**

Protheus – Livros Fiscais - A partir da versão 11.80

**Solução**

Para que a correta geração do título do SENAR seja gerado no financeiro após a escrituração da nota é necessário seguir o procedimento abaixo:

Em Livros Fiscais (SIGAFIS) acesse Miscelânea/Apurações/Apuração de ICMS (MATA953) e configure as perguntas Gera titulo e Gera Guia de Recolhimento? como Sim.

Efetue a apuração do ICMS do período, para verificar o valor a ser recolhido ao SENAR. As demais perguntas devem ser configuradas de acordo com as necessidades do contribuinte.

Verifique que o valor apurado do SENAR é apresentado em Informações Complementares. Confirme.

Ao confirmar a apuração, a guia de recolhimento é gerada automaticamente, com o tipo SENAR, o título a pagar com a natureza e o prefixo de acordo com a configuração dos parâmetros MV\_PFSENAR e MV\_APSENAR.

Será gerado um título e guia recolhimento SENAR quando ocorrer conforme TES e venda de um Produtor Rural (M0\_PRODRUR).

Abaixo documentação completa referente o Funrural "SENAR/GILTAR/INSS" :

<https://tdn.totvs.com/pages/releaseview.action?pageId=336407064>
