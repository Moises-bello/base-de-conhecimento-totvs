---
article_id: 4418359660055
category: Integrações Outros BackOffice
content_hash: 6bbb7981df2574e387923860a3a816bb9374449c61897ba680d80655a4d68687
fetched_at: '2026-06-28T22:46:42.188166+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM Labore x BackOffice Protheus, o valor do rateio
  não confere com o valor do título
type: support-article
updated_at: '2025-02-03T19:42:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418359660055-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-o-valor-do-rateio-n%C3%A3o-confere-com-o-valor-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29721203910679) Tempo aproximado para leitura: **00:03:22 min****Ocorrência**Ao realizar a integração do Lançamento Financeiro proveniente do **RM** ao **BackOffice Protheus**, retorna o erro: O valor do rateio não confere com o valor do título.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O é erro retornado pois quando gerado o Lançamento Financeiro pelo **RM** para ser enviado ao **Protheus**, o valor do rateio desse título está diferente do valor original.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes procedimentos:

Para ter certeza que todos funcionários estão com valores de rateio devidamente preenchidos, acesse**Administração de Pessoal | Alterações Cadastrais | Alteração Rateio Fixo:**![](https://totvssuporte.zendesk.com/attachments/token/uSJrNEg36wrgTpqADhF7Ah6Gb/?name=inline2086936093.png)  
  
Nessa rotina, é possível aplicar o rateio fixo de um ou mais **Centro de Custo** para os funcionários automaticamente apenas utilizando a seleção de funcionários.  
![](https://totvssuporte.zendesk.com/attachments/token/tr7RKQV1EBj1dFGU1UsygPTkU/?name=inline-1633508575.png)  
  
Feito a aplicação​ do percentual de rateio para todos funcionários selecionados, deve-se recalcular o envelope para os valores serem rateados para cada Centro de Custo informado no passo anterior, para executar de forma geral poderá acessar **Folha Mensal | Lançamentos | Executa Recálculo**![](https://totvssuporte.zendesk.com/attachments/token/Uy6DNK64luuL3EFd08e6fzYbU/?name=inline-1805332937.png)  
  
Essa rotina também conta com a **Seleção de Funcionários**, você pode utilizar a mesma seleção feita na rotina anterior (onde preencheu o rateio).  
![](https://totvssuporte.zendesk.com/attachments/token/rynthnDCUx8nJrqgsiSW7K1pC/?name=inline-2091526595.png)  
  
Com os valores devidamente preenchidos e rateados, gere novamente os lançamentos financeiros​​ marcando a flag **Gerar lanctos rateados por centro de custo.**![](https://totvssuporte.zendesk.com/attachments/token/9CZt7iJhwFQbeiv0pyZT1dW47/?name=inline-385547377.png)

**Importante**Caso ainda persistir, poderá ser necessário gerar novamente o lançamento marcando a flag **Calcular rateio conforme Gestão Financeira** em **Configurações | Parametrizador | Integrações | Outros BackOffice**![](https://totvssuporte.zendesk.com/attachments/token/yEAVADvtYkKgiM6SJbA3gyqfU/?name=inline-846370265.png)

Caso o valor esteja correto e o erro persistir, o erro pode estar relacionado ao tamanho das casas decimais do campo CTJ\_PERCEN no Protheus. Para realizar esta alteração, siga os passos desta documentação:

[Cross Segmento - Totvs BackOffice Protheus - SIGAFIN - FINA050 - Help: FA050RATEI - O valor do rateio não confere com o valor do título](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413023003671-Cross-Segmento-Totvs-BackOffice-Protheus-SIGAFIN-FINA050-Help-FA050RATEI-O-valor-do-rateio-n%C3%A3o-confere-com-o-valor-do-t%C3%ADtulo)
