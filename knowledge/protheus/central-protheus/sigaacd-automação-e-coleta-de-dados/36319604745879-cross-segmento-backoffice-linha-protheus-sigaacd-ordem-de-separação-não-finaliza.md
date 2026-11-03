---
article_id: 36319604745879
category: SIGAACD - Automação e Coleta de Dados
content_hash: 8c11201f2b2aa619fcd30dbc3fcfd1b1a5f79470900dc5b3f4e7e6d998fc24c8
fetched_at: '2026-06-28T22:39:11.030732+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ordem de Separação
  não finaliza no Aplicativo Meu Coletor de Dados.
type: support-article
updated_at: '2026-01-15T18:32:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36319604745879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ordem-de-Separa%C3%A7%C3%A3o-n%C3%A3o-finaliza-no-Aplicativo-Meu-Coletor-de-Dados
---

O aplicativo Meu Coletor de Dados não finaliza a Ordem de Separação se o campo CB7\_TIPEXP estiver preenchido com valores como "00\*02", pois não valida esses parâmetros, deixando a ordem aberta na rotina ACDA100. Apenas valores no formato "00\*" são reconhecidos, finalizando corretamente a ordem e exibindo legenda verde. Essa limitação é nativa do aplicativo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36319597419031) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao fazer uma Ordem de Separação, no aplicativo Meu Coletor de Dado,s a ordem de separação não finaliza, como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
O aplicativo Meu Coletor de Dados, não realiza a validação do campo **CB7\_TIPEXP** quando está preenchido conforme o exemplo **(00\*02),** ficando com a ordem com a legenda amarela como não finalizada na rotina de Ordem de Separação**(ACDA100).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36319604727959)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36319597421207)

Dessa forma o aplicativo finaliza a separação corretamente, mas na rotina de Ordem de Separação continuar como em aberto, conforme demostra na legenda acima. É nativo do aplicativo não ler os parâmetros do **F12** da rotina Ordem de Separação, quando está com preenchimento.

### **Se os parametros estiverem como SIM, significa que esta preenchido os campos na CB7\_TIPEXP, altere para NAO.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37705950951575)

O aplicativo só realiza leitura quando o campo **CB7\_TIPEXP (00\*).** Ficando com a legenda verde na rotina de  Ordem de Separação, dessa maneira fica como finalizado a Ordem de separação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36319597421719)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Significado do campo CB7\_TIPEXP na Ordem de Separação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34879226447511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Significado-do-campo-CB7-TIPEXP-na-Ordem-de-Separa%C3%A7%C3%A3o)
