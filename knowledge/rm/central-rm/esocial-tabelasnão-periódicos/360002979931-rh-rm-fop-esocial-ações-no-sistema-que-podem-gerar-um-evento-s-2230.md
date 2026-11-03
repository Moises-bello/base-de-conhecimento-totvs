---
article_id: 360002979931
category: eSocial - Tabelas/Não Periódicos
content_hash: 3cdda330b48087b93bbb5828ba7502f521d581005953f9c6e714f88f7715e633
fetched_at: '2026-06-28T22:47:10.225946+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Ações no sistema que podem gerar um evento S-2230
type: support-article
updated_at: '2026-05-27T21:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360002979931-RH-RM-FOP-eSocial-A%C3%A7%C3%B5es-no-sistema-que-podem-gerar-um-evento-S-2230
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23564048398103) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Quais ações no sistema podem gerar um evento S-2230 (evento de afastamento temporário)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Todas as vezes que um processo do sistema cria um registro no histórico de afastamento ou período aquisitivo de férias, automaticamente é gerado um gatilho do evento S-2230, por exemplo:   
  1. Inclusão de um atestado (afastamento) pelo **TOTVS Gestão de Pessoas**;  
  2. Alteração da situação do funcionário através da edição do funcionário no **TOTVS Folha de Pagamento**;  
  3. Inclusão de registro diretamente no histórico de afastamento do cadastro do funcionário;  
  4. Inclusão/aprovação de férias cadastradas pelo **Portal RH**;  
  5. Cadastro de férias individual ou coletivas/globais;  
  6. Cadastro de férias realizado através do período aquisitivo do cadastro do funcionário;  
  7. Importação do histórico de férias ou período de gozo.

Ao executar as ações acima, o sistema gera de forma automática gatilhos do evento S-2230 na fila de eventos. Deve-se realizar a geração dos *XMLs*, integrá-los ao TAF (caso não utilize o Middleware) e transmiti-los ao governo.  
  
**Saiba mais**  
Para mais informações sobre a geração de gatilhos do S-2230, acesse:  
     - [S-2230 Afastamento Temporário](http://tdn.totvs.com/pages/releaseview.action?pageId=364908488)
