---
article_id: 360028914491
category: Rescisão
content_hash: 3c49c3b45abc5696748b8326cc413184cfebe600146dc97bcc4c582870bdac98
fetched_at: '2026-06-28T22:46:55.317984+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Saldo de Salário (Campo 50)'
type: support-article
updated_at: '2024-10-23T22:18:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028914491-RH-RM-FOP-TRCT-Saldo-de-Sal%C3%A1rio-Campo-50
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:02min 53sec  
  
Dúvida**Como realizar a parametrização do Saldo de Salário do TRCT no Campo 50?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Solução**Este campo deverá referenciar uma fórmula que retorne o valor do **Saldo de Salário Líquido** pago na rescisão. É necessário informar a fórmula para cálculo do Campo 50, pois não existem rubricas padrão pré-definidas pelo MTE para representar Faltas, DSR Perdido e Reflexo de DSR Perdido.   
  
Para criar a fórmula, siga os passos abaixo:  
  
**01.** Acesse **Administração de Pessoal** | **Fórmulas;**  
**02.** Clique em **Incluir** para adicionar uma nova fórmula ou edite uma fórmula pré cadastrada;  
**03.** Após criar a formula, salve o registro e selecione a formula criada no campo 50 saldo salario no momento da geração da TRCT.  
  
Abaixo uma **exemplo** de fórmula que pode ser utilizada:

```
(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0001') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0002'))   
(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0008') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0182') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0070'))
```

Detalhando a fórmula, temos:  
  
**MV,** função que retornará o valor de um evento. Os parâmetros desta função são: Mês Competência, Ano Competência e Código do Evento.  
**PARMQRY('MESCOMP')**, retornará o mês competência informado na geração do TRCT  
**PARMQRY('ANOCOMP')**, retornará o ano competência informado na geração do TRCT  
 **Importante**  
- A fórmula acima contempla o cálculo de Saldo de Salário da base exemplo. Desta forma, o usuário deverá verificar os códigos de eventos a considerar no cálculo do Líquido Salarial pago na rescisão e adequar à fórmula;  
- O suporte padrão não presta auxílio na criação ou manutenção de fórmulas. Para estes casos, verifique a possibilidade de contratar nossa equipe de consultoria tarifada.  
  
**Saiba mais**  
Para mais informações sobre as parametrizações do TRCT, [clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=42042615).
