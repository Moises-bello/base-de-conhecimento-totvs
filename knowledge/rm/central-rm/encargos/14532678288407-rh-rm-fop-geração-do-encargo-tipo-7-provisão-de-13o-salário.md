---
article_id: 14532678288407
category: Encargos
content_hash: 1b1f86a3398a00c2da6b028a3f80f20a27d399b7b1070a108eaad654c726eb30
fetched_at: '2026-06-28T22:46:52.324470+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo TIPO 7 - Provisão de 13o. salário
type: support-article
updated_at: '2024-10-11T19:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14532678288407-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-7-Provis%C3%A3o-de-13o-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como gerar o encargo TIPO 7 - Provisão de 13o. salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO 7 - Provisão de 13o. salário é necessário anteriormente gerar a provisão, o sistema irá considerar o valor da provisão de 13º salário do mês para o encargo: Para geração do histórico de provisões, siga a orientação da documentação abaixo.

[RH - RM - FOP - Parâmetros da geração do Histórico de provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413936936215-RH-RM-FOP-Par%C3%A2metros-da-gera%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-provis%C3%A3o#:~:text=O%20hist%C3%B3rico%20de%20provis%C3%B5es%20dever%C3%A1%20ser%20gerado%20mensalmente.&text=Quando%20o%20par%C3%A2metro%20Provis%C3%A3o%20F%C3%A9rias,antes%20da%20execu%C3%A7%C3%A3o%20da%20rotina).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14530849409815)

No cadastro do encargo possui a flag **provisão acumulada, e Abate adiantamento de 13º .**

Para cadastrar um encargo acesse: Encargos | Cadastros | Encargos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14533891461271)

Comportamento da geração do Encargo. Acesse: Encargo | Geração dos encargos

Com a flag marcada **provisão acumulada** no cadastro do encargo o comportamento do sistema é:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14534128721943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14534093007639)  
Log da geração do encargo com a Flag marcada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14531177256343)

Comportamento com a flag desmarcada irá levar o valor do mês:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14531182833047)

Com o parâmetro **abate adiantamento de 13º** no cadastro do encargo, irá considerar o CC09 lançados para chapa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14532340603159)  
  
Geração do encargo com a flag abate adiantamento de 13º marcada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14532364768535)  
**Importante:** Verificar o código ativo associado no cadastro do encargo pois no momento da geração será necessário selecionar o mesmo para gerar. Segue documentação para vinculação do código ativo no cadastro do encargo. [RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
