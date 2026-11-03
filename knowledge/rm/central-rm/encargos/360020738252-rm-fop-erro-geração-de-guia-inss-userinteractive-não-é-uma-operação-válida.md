---
article_id: 360020738252
category: Encargos
content_hash: 580771f9534fec597b928dfd7fc0b6eab4e4eb0074504459e93b14f702ace99b
fetched_at: '2026-06-28T22:46:53.353220+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RM - FOP - Erro Geração de Guia INSS | UserInteractive não é uma operação válida
type: support-article
updated_at: '2025-03-14T13:25:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020738252-RM-FOP-Erro-Gera%C3%A7%C3%A3o-de-Guia-INSS-UserInteractive-n%C3%A3o-%C3%A9-uma-opera%C3%A7%C3%A3o-v%C3%A1lida
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30644007580439)**Tempo aproximado para leitura:**00:01:00 min*****Ocorrência**

No módulo **Folha de pagamento**, ao executar a Geração Guia de INSS que está localizado em Encargos | Guia de INSS | Guia de INSS é apresentada a seguinte mensagem de erro:  
  
" Mostrar um formulário ou uma caixa de diálogo restrita quando o aplicativo não está no modo UserInteractive não é uma operação válida. Especifique o estilo ServiceNotification ou DefaultDesktopOnly para exibir uma notificação de um aplicativo de serviços."  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o **Tipo de Guia** precisa estar de acordo com parametrização a ser utilizada no lançamento.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique qual o Tipo de Guia está sendo utilizada:

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017549332)

2. Ao utilizar parâmetro específicos, o campo **Parametrização a ser utilizada no lançamento** precisa estar de acordo com o tipo de guia selecionado no passo 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017433331)

3. Gere a Guia de INSS.
