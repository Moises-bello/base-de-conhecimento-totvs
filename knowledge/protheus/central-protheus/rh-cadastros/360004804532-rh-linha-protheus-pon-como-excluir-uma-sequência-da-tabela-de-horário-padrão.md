---
article_id: 360004804532
category: RH - Cadastros
content_hash: 4e824df3f19693c8c43a4ae8ffb029359fd9ccccf517b7f1b017bc82fed98e08
fetched_at: '2026-06-28T22:44:52.867200+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como excluir uma sequência da Tabela de Horário
  Padrão
type: support-article
updated_at: '2025-12-29T12:14:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004804532-RH-Linha-Protheus-PON-Como-excluir-uma-sequ%C3%AAncia-da-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31781348853527) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como excluir uma sequência da Tabela de Horário Padrão?    
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Acessar o módulo **16 - SIGAPON - Ponto Eletrônico**, em **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**. Deverá selecionar a tabela que deseja excluir uma sequência em **Outras Ações > Excluir**, conforme exemplo abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250662807)  
  
  
2- Selecionar a sequência que deseja excluir e clicar em **confirmar**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250664855)  
  
  
3- Após será gerado a mensagem abaixo, onde deve confirma a exclusão da sequência, clicar em **Sim**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250667031)  
  
  
4- Será validado a mensagem se deseja gera log, clicar em **Sim**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607226125719)  
  
  
5- Posteriormente, será exibido a mensagem se deseja excluir todas as sequências da tabela, clicar em **Não**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607226127895)

6- Quando a sequência da tabela de horário padrão não possuir histórico de uso, o sistema fechará sem geração de log e efetuará a exclusão. E após finalizar o processo de exclusão e visualizar a tabela, poderá verificar que sequência 02 foi excluída:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250672279)

**IMPORTANTE:** Em caso da sequência da tabela de horário padrão que já foi utilizada, ao tentar excluir o sistema apresentará o log conforme abaixo:  
  
- Na opção de gravar o log, selecionar as opções desejadas e clicar em ok:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250673303)  
  
  
Com isso será gerado o log alertando que a sequencia não pode ser excluída, pois o sistema não permite excluir uma sequência que já foram utilizadas em algum momento. Ou seja, por questão de integridade de dados e para manter o histórico utilizado desta sequência da tabela por conta de processos de cálculos anteriores, o sistema não permitirá a exclusão e apresentará o log abaixo como exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607250675479)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)
