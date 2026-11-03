---
article_id: 31673236417943
category: Financeiro - Contabilização
content_hash: 0a9965b92304fbd532ac36f87fd32cb18ff6242a930027fdc8611814d553ed3d
fetched_at: '2026-06-28T22:38:05.189637+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Como automatizar
  o processo de contabilização off-line
type: support-article
updated_at: '2025-04-25T20:02:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31673236417943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Como-automatizar-o-processo-de-contabiliza%C3%A7%C3%A3o-off-line
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236382743) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como posso realizar a contabilização off-line automática?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - Todas as versões  
  
**Solução**

Antes de configurar o Schedule pelo Configurador, é necessário incluir uma fórmula no cadastro do Protheus para definir a data de contabilização.

**No ambiente do Financeiro, acesse:**

**Atualizações > Cadastros > Fórmulas.**

Será necessário incluir uma condição com Data Inicial e Data Final.

No exemplo abaixo, foi informado um código, uma descrição e a fórmula:  
**`DDATABASE - 30`**

Essa fórmula define uma data com base em 30 dias antes da data atual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236383639)

**Essa fórmula indica que queremos sempre considerar 30 dias antes da data base do sistema.**

**Exemplo:**  
Se a data base para contabilização estiver definida como o dia 30 de cada mês, ao aplicar a fórmula `DDATABASE - 30`, o sistema irá considerar o dia 1º do mesmo mês como Data Inicial.

Já para a **Data Final**, deve-se informar diretamente o valor **`DDATABASE`**, mantendo a data base do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192780055)

Após concluir esse processo, podemos prosseguir com a configuração do Schedule.

No Configurador, acesse o menu:  
**Cadastros > Schedule > Schedule.**

Dentro do Schedule vamos em agendamentos ![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192780951) e incluir no novo agendamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192781335)

Exibirá a tela de inclusão de agendamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236387223)

Vamos parametrizar o período em que a rotina será executada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192782103)

Neste exemplo, configuraremos a execução para ocorrer mensalmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192782615)

Vamos definir o dia e o horário em que o Schedule será executado. No exemplo, configuraremos para ocorrer sempre no dia 30, às 08:00, de forma recorrente — ou seja, a rotina será executada todo dia 30 de cada mês, sempre nesse horário

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236389527)

Após essa etapa, avançamos para a configuração onde devem ser informados a Empresa, a Filial e o Módulo. O usuário será, por padrão, o que estiver logado no momento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236391447)

No canto superior direito, há a opção 'Editar Parâmetro'.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192784023)**

Será exibida a tela de parâmetros para configuração, onde você poderá preenchê-los da mesma forma que faria em uma contabilização manual.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192784663)**

Para os campos **'Da Data' e 'Até a Data'**, utilizaremos a fórmula criada anteriormente. Basta acessar a aba 'Fórmula' e informar os respectivos códigos.

**Importante**

É possível criar e aplicar outras fórmulas nos demais campos, conforme necessário

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673192785431)

Após essa configuração, basta avançar e salvar o agendamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236393879)

O agendamento será realizado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31673236394647)

**Saiba mais**

[Contabilização Offline - CTBAFIN - Financeiro - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=497932563)
