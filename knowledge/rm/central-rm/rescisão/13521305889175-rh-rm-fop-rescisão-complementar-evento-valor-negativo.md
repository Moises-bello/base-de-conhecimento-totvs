---
article_id: 13521305889175
category: Rescisão
content_hash: 29f77ab577ebeadf64bbd0db6685df3bc591d1ef3e8df1a7b14a40e0a803a286
fetched_at: '2026-06-28T22:46:54.264432+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão complementar: Evento valor negativo'
type: support-article
updated_at: '2024-09-16T18:51:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13521305889175-RH-RM-FOP-Rescis%C3%A3o-complementar-Evento-valor-negativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:04 min****Ocorrência**  
Ao calcular a rescisão complementar do funcionário o evento de cc96 fica negativo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13520807695767)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O que ocorre no processo da rescisão complementar, relacionado ao [96 - Dif. Salário Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718608) estar negativo, não é exatamente um erro.   
Detalhando um pouco mais, como o valor de desconto do Aviso Prévio Indenizado ([140 - Desconto de Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718339)) é maior que o valor de pagamento do Saldo de salário e os dois eventos são direcionados para o evento de diferença [96 - Dif. Salário Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718608), o valor deste evento fica negativo.  
  
Neste caso, existem duas possibilidades para que o valor não fique negativo:  
  
**1 opção:**  
  
Pode criar um novo evento de desconto e sem código de cálculo e inseri-lo no campo 'Evento de Diferença de Salário' do seu evento com [140 - Desconto de Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718339).  
  
Evento de diferença:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13521032251159)  
  
Evento Principal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13521094013463)  
  
Desta forma, a diferença do evento de desconto de Aviso Prévio será lançada neste novo evento, ou seja será desmembrado, não interferindo no valor do evento com [96 - Dif. Salário Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718608).  
  
**2 opção:**Pode acessar **Configurações | Parametrizador | Folha Normal | Cálculo 1/2** e marcar o parâmetro 'Zerar evento de diferença quando o valor fica negativo'.   
Desta forma, o valor do evento com [96 - Dif. Salário Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718608) será zerado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13521149600535)  
  
**Saiba Mais**  
[RH - RM - FOP - Rescisão complementar referente alteração salarial retroativa á competência atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412581826327-RH-RM-FOP-Rescis%C3%A3o-complementar-referente-altera%C3%A7%C3%A3o-salarial-retroativa-%C3%A1-compet%C3%AAncia-atual)
