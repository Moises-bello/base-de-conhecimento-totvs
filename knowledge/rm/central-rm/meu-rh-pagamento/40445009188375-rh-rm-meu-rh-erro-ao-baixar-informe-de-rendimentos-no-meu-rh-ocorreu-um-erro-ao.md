---
article_id: 40445009188375
category: Meu RH - Pagamento
content_hash: b4ae6db2d04a70c70e1b4bdb78274c005a046c05754f81d523f85e4fa4140c92
fetched_at: '2026-06-28T22:47:33.799539+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: 'RH - RM - Meu RH - Erro ao baixar Informe de Rendimentos no Meu RH: Ocorreu
  um erro ao efetuar a leitura do registro Object reference'
type: support-article
updated_at: '2026-05-18T21:08:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40445009188375-RH-RM-Meu-RH-Erro-ao-baixar-Informe-de-Rendimentos-no-Meu-RH-Ocorreu-um-erro-ao-efetuar-a-leitura-do-registro-Object-reference
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40445009163543) Tempo aproximado para leitura: **00:01:48 min**  
  
**Ocorrência**  
Ao realizar o download do informe de rendimentos no Meu RH, é apresentado a mensagem de erro: **Ocorreu um erro ao efetuar a leitura do registro Object reference not set to an instance of an object.".**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40445009164439)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir do release 12.1.2209.169.  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do informe de rendimentos no Grupo de Quiosque do colaborador está sem o relatório vinculado para geração.  
  
**Solução**  
Para vincular o relatório do Informe de Rendimentos no Meu RH, realize os seguintes passos:

1. Acesse **Folha de Pagamento** > **Configurações** > **RM Portal** >  **Parametrizador** > Edite o **Grupo de Acesso** vinculado ao funcionário > **Informe de Rendimentos**. Marque a Flag **Relatórios do RM Reports** e selecione o relatório padrão "**FOPREL0008.01".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40445009166103)

2- Caso o relatório não seja listado para seleção, acesse a ferramenta **TOTVS Compartilhamento** para realizar o download do novo modelo **"FOPREL0008.01 - Informe de Rendimentos - NOVO MODELO".**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40445009167767)**

3- Finalizando a parametrização, será possível realizar o download do informe de rendimentos no Portal.

**![image2022-9-29_15-49-14.png](https://tdn.totvs.com/download/attachments/714234519/image2022-9-29_15-49-14.png?version=1&modificationDate=1664477355053&api=v2)**
