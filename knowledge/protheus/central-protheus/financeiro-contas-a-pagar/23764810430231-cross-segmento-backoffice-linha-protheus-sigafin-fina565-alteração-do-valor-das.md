---
article_id: 23764810430231
category: Financeiro - Contas a Pagar
content_hash: b9223bf63da9a4e458272edeee7ac641e2caae9648552bd91bbc83dc70e21cc1
fetched_at: '2026-06-28T22:38:08.326065+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA565 - Alteração
  do valor das parcelas da liquidação bloqueado
type: support-article
updated_at: '2024-05-27T17:27:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23764810430231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA565-Altera%C3%A7%C3%A3o-do-valor-das-parcelas-da-liquida%C3%A7%C3%A3o-bloqueado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800811159) Tempo aproximado para leitura: **05:00 min** **Dúvida**Como alterar o valor das parcelas da liquidação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução  
1.** No **Configurador (SIGACFG)** acesso o caminho **Base de Dados > Dicionário > Bases de Dados**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800812183)  
  
**2.** Abra o **diretório a esquerda**, selecione o **Dicionário de Dados** e clique na **lupa** para pesquisar a tabela **SE2**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764810407575)  
  
**3.** Ao localizar a tabela clique em **editar** abra novamente o **diretório a esquerda** e clique em **Campos:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800813079)  
 **4.** Clique na **lupa da esquerda** e pesquise o campo **E2\_VLCRUZ**, selecione o campo e clique em **editar**:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800814359)  
  
5.** Altere os campos **Propriedade** > **X3\_VISUAL = Alterar** (na aba campo) e **Modo Edição** > **X3\_WHEN = .T.** (na aba opções) conforme as imagens abaixo e clique em **salvar**: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764810410007)     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764810411799)  
  
**6.** Após **salvar**, clique em **sair** e em **salvar,** logo em seguida será apresentado um **Wizard**.Clique um **avançar** e **finalizar:** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800817047)![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800820631)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764810415895)  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800821783)  
  
**7.** Faça **logoff e login** no Protheus para os dados serem atualizados e ao tentar liquidar será possível alterar o valor das parcelas, dando **dois cliques** no valor:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764800822551)  
  
**Importante**Faça esse processo em ambiente de homologação antes de realizar em produção.
