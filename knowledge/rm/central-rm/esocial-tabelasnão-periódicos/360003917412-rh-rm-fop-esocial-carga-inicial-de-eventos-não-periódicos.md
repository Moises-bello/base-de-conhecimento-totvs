---
article_id: 360003917412
category: eSocial - Tabelas/Não Periódicos
content_hash: ca0801189d79255087e7d9ee3fa513f619855f7ef0a631f62fb94494995c986d
fetched_at: '2026-06-28T22:47:10.278914+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Carga Inicial de eventos não periódicos
type: support-article
updated_at: '2024-06-28T15:17:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003917412-RH-RM-FOP-eSocial-Carga-Inicial-de-eventos-n%C3%A3o-peri%C3%B3dicos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24453155808407) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como gerar **Carga Inicial** para funcionários admitidos antes da obrigatoriedade do eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as Versões  
 **Solução**Para gerar corretamente a carga inicial dos eventos não periódicos, siga os passos abaixo:  
1. Valide se no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 1/7**, as **Datas de Obrigatoriedade/Adesão ao eSocial** estão corretamente preenchidas, principalmente dos Não Periódicos;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24504473409559)

2. Selecione o menu **eSocial | Gerar Gatilhos Eventos Iniciais** e selecione **2ª Fase** na área **Faseamento eSocial**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041729614)

3. Avance a tela selecionando a coligada desejado e executando o processo;  
4. Os eventos S-2200 e S-2300 dos funcionários admitidos antes da obrigatoriedade serão apresentados na fila de eventos com **Tipo da Operação** como **Carga Inicial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013672331)

**Importante**Para os funcionários admitidos depois da data de obrigatoriedade, assim que o cadastro do novo funcionário for salvo, o sistema incluirá **automaticamente** o gatilho na fila de eventos com o tipo de operação **Inclusão**, ou seja, o gatilho será gerado ao concluir o cadastro da admissão.
