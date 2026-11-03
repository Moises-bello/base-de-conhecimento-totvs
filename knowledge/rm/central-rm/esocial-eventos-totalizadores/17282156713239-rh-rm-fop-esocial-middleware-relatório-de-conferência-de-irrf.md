---
article_id: 17282156713239
category: eSocial - Eventos Totalizadores
content_hash: 42b0170949c02d82e4611166b81050509cfe3a545fc617197d41d091f99fa024
fetched_at: '2026-06-28T22:47:07.006244+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência de IRRF'
type: support-article
updated_at: '2024-09-23T12:19:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17282156713239-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-de-IRRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17282091304343) Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como configurar e gerar o Relatório de Conferência de IRRF para identificação de divergências entre Folha de Pagamento e Governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos pacotes 12.1.2302.200, 12.1.2306.142 e superiores.   
  
**Solução**O Relatório de Conferência de IRRF tem como objetivo principal auxiliar na identificação de eventuais divergências entre os valores de IRRF presentes no envelope de pagamento e os valores reportados pelo RET.   
Os dados apresentados são o resultado de uma análise comparativa entre os valores de IRRF enviados do RH ao governo por meio dos eventos S-1200, S-2299 e S-2399, e os valores que o Governo retorna por meio do evento S-5002.

Abaixo segue documentação com orientações de como configurar e gerar o relatório:

      • [Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=782303914)

**Importante**

1. Para que o relatório seja gerado corretamente, é necessário que os eventos de remuneração tenham sido encaminhado pelo Middleware e conste o evento de retorno S-5002 no RM;
2. Após atualização do pacote, faz-se necessário rodar o **RM.Atualizador**e **Reiniciar o Host.**

**Saiba mais**Para mais informações, acesse:

* [How To | Relatório de Conferência de IRRF](https://www.youtube.com/watch?v=4j2ZIAIS56I)
* [Configurando DefaultDB](https://tdn.totvs.com/display/public/LRM/Configurando+DefaultDB);
* [Configuração do API e APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633);
* [Painel de Conferência do Imposto de Renda no TAF;](https://tdn.totvs.com/pages/releaseview.action?pageId=786557296)
* [RM Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687?source=search);
* [Framework - Linha RM - Frame - Reiniciar Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827?source=search)
