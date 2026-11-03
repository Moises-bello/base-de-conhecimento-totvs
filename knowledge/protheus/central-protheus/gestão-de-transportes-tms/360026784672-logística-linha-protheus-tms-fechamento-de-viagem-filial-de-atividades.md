---
article_id: 360026784672
category: Gestão de Transportes (TMS)
content_hash: b8a4013582c0c519d4269bf62bc244b980473cdd69f65c2a0d3c7b27c3ae5809
fetched_at: '2026-06-28T22:45:29.188372+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Fechamento de viagem -  Filial de atividades
type: support-article
updated_at: '2025-10-20T14:02:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026784672-Log%C3%ADstica-Linha-Protheus-TMS-Fechamento-de-viagem-Filial-de-atividades
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35750331508887)***Tempo aproximado para leitura: **00:02:20 min****Ocorrência**No fechamento da viagem, como resolver o problema da mensagem: **Não foi encontrada atividade de saída ou chegada para esta filial**.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Esta mensagem é apresentada devido à incorreta parametrização do Sistema.  
  
**Solução** **- MV\_ATIVSAI:**Atividade de saída de viagem. Por padrão, o parâmetro vem configurado com o valor **049**.

![MV_ATIVSAI.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026788971)

**- MV\_ATIVCHG:**Atividade de chegada de viagem. Por padrão, o parâmetro vem configurado com o valor **050**.

![MV_ATIVCHG.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026788951)

**- MV\_CDRORI:** Define o código de região de origem da **Filial**.

![MV_CDRORI.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026788991)

Na rotina **Tarefas x Atividades - DLGA080**, a tarefa possui a filial a qual ela estará associada.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026533231)

Na rotina de **Serviços x Tarefas - DLGA070**, o **serviço operacional** deve conter a tarefa configurada anteriormente.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026542872)

No cadastro de **Rotas - OMSA100**,vincular o serviço operacional à rota.

**![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026533271)**

Neste exemplo, na rotina de **Viagem de Entrega Mod2- TMSA144D**, utilizar a rota que possui o serviço operacional:

**![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026542952)**

Ao fechar a viagem, são geradas as operações conforme parametrizado.

![9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026542972)

**Possíveis situações**Mesmo seguindo o processo acima, existem situações que podem impedir o correto funcionamento da rotina.  
  
**- Região da rota não cadastrada na estrutura de região:**Caso o **Grupo de Região - TMSA115** informado na **Rota - OMSA100** não esteja devidamente cadastrado na **Estrutura de Região - TMSA120**, o erro ainda será exibido. Verifique a estrutura de região, efetue ajuste caso necessário e tente novamente o processo. **- Região do parâmetro MV\_CDRORI não cadastrada na estrutura de região:**Caso o **Grupo de Região - TMSA115** informado no parâmetro **MV\_CDRORI** não esteja devidamente cadastrado na **Estrutura de Região - TMSA120**, o erro ainda será exibido. Verifique a estrutura de região, efetue ajuste caso necessário e tente novamente o processo. **- Parâmetro MV\_CDRORI vazio:**Caso o conteúdo do parâmetro **MV\_CDRORI** esteja vazio, o erro ainda será exibido. Preencha o parâmetro com a região de origem da filial da viagem.  
  
**- Customizações no processo de geração das operações:**  
Caso possua customizações em seu ambiente no processo de fechamento da viagem ou de operações da viagem, o fluxo do Sistema pode estar sendo alterado de uma forma não esperada. Por exemplo, se utiliza o ponto de entrada **TM310FFL**, dependendo da regra definida na customização, o Sistema pode não gerar alguma operação na viagem.  
  
**Saiba mais**Mais informações sobre **Serviços Vs Tarefas** e **Tarefas Vs Atividades** acesse os *links*:  
[Serviços Vs Tarefas (WMSA070 - SIGAWMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=569502196)  
[Tarefas Vs Atividades (WMSA080)](https://tdn.totvs.com/pages/viewpage.action?pageId=569505365)
