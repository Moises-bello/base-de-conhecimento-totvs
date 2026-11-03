---
article_id: 14693481696535
category: Encargos
content_hash: 17394e786ef2e7fe5b292c8babdee6de0e0800810a4b5e8d60be57198823d6e0
fetched_at: '2026-06-28T22:46:52.297565+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Geração do encargo TIPO M -Base: incidência de FGTS de 13o.
  salário'
type: support-article
updated_at: '2024-10-09T20:11:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14693481696535-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-M-Base-incid%C3%AAncia-de-FGTS-de-13o-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:23 min****Dúvida**Como gerar o encargo TIPO M -Base: incidência de FGTS de 13o. salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO M -Base: incidência de FGTS de 13o. salário, é necessário que exista base 13º salário em incidência da folha. O evento lançado no envelope será de CC 102 e caso houver adiantamento de 13º salário será no evento de CC 35:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14692679266199)

Para realizar o  cadastro do **Encargo** acesse**: Encargos | Cadastro | Encargos** deverá ser parametrizado conforme necessidade da organização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14692895470103)

**Importante:** Verificar o código ativo associado ao cadastro do encargo, pois no momento da geração do encargo será necessário selecionar o mesmo código ativo. Caso precise de apoio para criar o código ativo para vincular no encargo, utilize a documentação abaixo, após criar o código ativo, vincule o mesmo no cadastro do encargo.

[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14692940902295)**

Para geração do encargos acesse: **Encargo | Geração do encargo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14693055673495)**

Para o cálculo o sistema irá considerar base FGTS 13o \* % encargo / 100, o percentual do encargo é informado dentro do cadastro do encargo. Log de execução:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14693170511383)  
**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
