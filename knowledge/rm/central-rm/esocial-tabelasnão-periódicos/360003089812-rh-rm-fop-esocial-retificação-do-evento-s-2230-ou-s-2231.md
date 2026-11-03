---
article_id: 360003089812
category: eSocial - Tabelas/Não Periódicos
content_hash: 237fd6989dbb27e342f860a54561b9f7898ef455612c665a879d56960311ef13
fetched_at: '2026-06-28T22:47:10.503439+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Retificação do evento S-2230 ou S-2231
type: support-article
updated_at: '2024-06-21T19:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003089812-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-S-2230-ou-S-2231
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24346831382167) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como retificar o evento S-2230/ S-2231 em razão da alteração das datas de afastamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Caso o afastamento do funcionário já tenha sido enviado para o governo e por algum motivo precisar ter sua data alterada/estendida, siga os passos abaixo:

**- Alterar data fim do afastamento**  
1. Acesse **Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico de Afastamentos**;  
2. Altere a data final do afastamento ou a quantidade de dias;  
3. O sistema irá gerar automaticamente na fila de eventos um gatilho do S-2230 com o tipo de operação **Retificação**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6378221347991)

4. Integre o evento com o TAF e transmita normalmente para o RET.  
  
**- Alterar data início de afastamento**  
1. Acesse **Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico de Afastamentos**;  
2. Selecione o afastamento desejado e acesse **Processos | Alterar Data Início do Afastamento**;  
3. Cadastre a nova data desejada e clique em executar;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8877134558871)

4. Após a execução da alteração da data do afastamento, o sistema irá verificar se existe evento o S-2230 ou S-2231 para este afastamento com com status **10-Aceito RET**. Caso tenha, será gerado um gatilho de retificação para o evento e o campo **Data Início Afastamento** será ajustado nos dois gatilhos (**Inclusão** e **Retificação**).  
  
**Importa****nte**Certifique-se de estar utilizando as versões mais recentes do RM, TAF (incluindo Dicionário de Dados) e TSS.   
  
**Saiba mais**  
Para mais informações acesse:  
      • [S-2230 e S-2231- Como retificar a data inicial de um afastamento temporário?](https://tdn.totvs.com/pages/viewpage.action?pageId=652842244)  
      • [S-2230 - Como retificar um afastamento temporário?](https://tdn.totvs.com/pages/viewpage.action?pageId=403735186)
