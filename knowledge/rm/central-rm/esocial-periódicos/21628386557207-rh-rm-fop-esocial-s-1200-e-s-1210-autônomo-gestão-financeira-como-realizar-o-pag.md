---
article_id: 21628386557207
category: esocial - Periódicos
content_hash: b57aac10d48b84e91c7e601d5850985331ff0bd945b2600f9ace818aac281f28
fetched_at: '2026-06-28T22:47:09.482292+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - S-1200 e S-1210 Autônomo Gestão Financeira - Como
  realizar o pagamento de uma verba com incidência exclusiva em IRRF '
type: support-article
updated_at: '2024-06-19T18:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21628386557207-RH-RM-FOP-eSocial-S-1200-e-S-1210-Aut%C3%B4nomo-Gest%C3%A3o-Financeira-Como-realizar-o-pagamento-de-uma-verba-com-incid%C3%AAncia-exclusiva-em-IRRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21628386527255) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Como realizar o pagamento de uma verba com incidência exclusiva em IRRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2209.246, 12.1.2302.170, 12.1.2306.114 e Superiores.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse **RH | Folha de Pagamento | Configurações | Parametrizador |  eSocial | Configurações Gerais | Autônomos e Externos 2/2**, cadastre o **provento com incidência exclusiva em IRRF** no campo Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21629157398167)

2. **Lançamento financeiro** realizado para o autônomo com o tipo de documento **Gera IRRF**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21629157410455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21629157418519)

3. **XML** dos eventos periódicos S-1200 e S-1210.

* **S-1200**: O valor do lançamento financeiro informado no passo 2 é gerado no código do evento/verba informado no parametrizador "Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200)" passo 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21629157432471)

* **S-1210**: O valor do liquido do lançamento financeiro será levado na tag <vrLiq>:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21629141028375)

**Importante**Para geração dessa nova verba, serão contempladas todas as categorias, **EXCETO as categorias 711**-Contribuinte individual - Transportador autônomo de passageiros) **e 712** - Contribuinte individual - Transportador autônomo de carga).

**Saiba mais**[Eventos S-1200 e S-1210 - Autônomos do TOTVS Gestão Financeira - Como realizar o pagamento de uma verba com incidência exclusiva em IRRF?](https://tdn.totvs.com/pages/releaseview.action?pageId=776112878)
