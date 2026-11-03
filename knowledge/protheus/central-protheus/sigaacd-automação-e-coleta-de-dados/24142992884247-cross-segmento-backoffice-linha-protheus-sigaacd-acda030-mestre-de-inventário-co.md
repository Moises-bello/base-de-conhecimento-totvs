---
article_id: 24142992884247
category: SIGAACD - Automação e Coleta de Dados
content_hash: c5b3f913691bdd37ce07ce8a44a10ad66779c72b175845aa65e5f61c48850da1
fetched_at: '2026-06-28T22:39:11.168679+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA030 - Mestre de
  Inventário - Como conferir através de Relatório as diferenças contadas no Inventário?
type: support-article
updated_at: '2025-03-12T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24142992884247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA030-Mestre-de-Invent%C3%A1rio-Como-conferir-atrav%C3%A9s-de-Relat%C3%B3rio-as-diferen%C3%A7as-contadas-no-Invent%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24142957334935) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**

Após gerar o Mestre de Inventário (ACDA030), em seguida efetuamos as contagens (ACDV035) pelo coletor, como podemos **conferir as diferenças** entre o **Saldo sistemico e o Saldo fisico** que foi contado através de Relatórios?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]

**Solução**

Para esse cenário é possível de duas opções, veja abaixo um passo a passo com exemplo:

***- 1ª opção-*** Na rotina Mestre de Inventário (ACDA030) no Browser contém o relatório que pode parametrizar o intervalo desejado para filtrar as Contagens.

![MESTRE INVENT relat.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24144278178199)

![MESTRE INVENT relat 2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24144274624535)

![MESTRE INVENT relat 3 param.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24144500145943)

![MESTRE INVENT relat 03.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24144500165783)

***- 2ª opção -*** Após gerar a tabelas SB7 que refere-se as contagens de inventário, também pode utilizar o relatório de Conferência de Inventário (MATR285), necessário revisar as parametrizações de impressão do relatório para que fiquem equivalentes ao intervalo das digitações. Veja o exemplo abaixo com as mesmas contagens do 1º exemplo.

![MATR285.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/24144783187223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24144744928407)

![MATR285 resultado.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/24144801816471)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[ACDR030 - Fonte de relatório para customizar a impressão do relatório do Mestre de Inventário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23566085069463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDR030-Fonte-de-relat%C3%B3rio-para-customizar-a-impress%C3%A3o-do-relat%C3%B3rio-do-Mestre-de-Invent%C3%A1rio)
