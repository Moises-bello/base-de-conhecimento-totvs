---
article_id: 1500001648942
category: LEGAIS - BLOCO H/MATR460
content_hash: d8eab6e542e40caa6270a3703b4358bbc86d9e7c58d0090a677109cea43853a5
fetched_at: '2026-06-28T22:42:15.202951+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tabela H_ + grupo
  + filial não foi criada com a execução do relatório MATR460
type: support-article
updated_at: '2021-06-14T14:42:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001648942-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tabela-H-grupo-filial-n%C3%A3o-foi-criada-com-a-execu%C3%A7%C3%A3o-do-relat%C3%B3rio-MATR460
---

**Dúvida**

Ao gerar o relatório MATR460 (Inventário Modelo 7 - P7) não está gerando a tabela H\_. O que fazer?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

A não geração da tabela H ao gerar o relatório MATR460 pode estar atrelada à parametrização.

O primeiro passo é validar, na tela dos parâmetros do MATR460, as perguntas:

"Gerar Aqr. Exportação?" = Deve estar com conteúdo **Sim**;

"Arquivo Exp. Sped Fiscal" =  Deve estar com a data do último inventário que será levado ao Bloco H (ex: 20201231 - data em formato americano).

Caso esteja com a parametrização conforme instruído acima e mesmo assim não estiver gerando a tabela H, por gentileza aplique o pacote acumulado do Estoque.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

**Observação**: Sempre atualizar primeiramente em ambiente de homologação.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H)
