---
article_id: 14554136739863
category: Encargos
content_hash: 6179f618e4b4f455152eb7c21f717858a671a5823c01b55a2b550708a15995aa
fetched_at: '2026-06-28T22:46:52.320329+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo TIPO 8 - Provisão de FGTS de 13o. salário
type: support-article
updated_at: '2024-10-09T20:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14554136739863-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-8-Provis%C3%A3o-de-FGTS-de-13o-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar o encargo TIPO 8 - Provisão de FGTS de 13o. salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO 8 - Provisão de FGTS de 13o. salário é necessário anteriormente gerar o histórico de provisão. Caso tenha dúvidas na geração do histórico de provisões, siga as orientações da documentação abaixo.

[RH - RM - FOP - Parâmetros da geração do Histórico de provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413936936215-RH-RM-FOP-Par%C3%A2metros-da-gera%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-provis%C3%A3o)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14553561311895)

Será necessário cadastrar o encargo do tipo 8 em **Encargos | Cadastros | Encargos** conforme a necessidade da organização informando valor no campo porcentagem, pois para a geração do encargo a fórmula interna do sistema irá considerar Valor provisão 13º referente ao mês atual \* % encargo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14553602659735)

**Importante** : Verificar o código ativo associado ao cadastro do encargo pois no momento da geração do encargo será necessário selecionar o mesmo código ativo. Caso precise criar códigos ativos, segue manual para apoio.   
[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)

Para Geração dos encargos acesse: **Encargos | Geração dos encargos:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14553703111447)

Utilizando o cadastro do encargo com a flag **Provisão acumulada** esse é o comportamento do sistema:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14553760412439)  
  
Utilizando o cadastro do encargo com a flag desmarcada **Provisão acumulada** esse é o comportamento do sistema:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14553896464407)  
**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
