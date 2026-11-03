---
article_id: 29607113728791
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 956a2a0d3a88f19c96065e6c7dece41a3784ad92ebccf3190c5db295dc5c22d1
fetched_at: '2026-06-28T22:39:08.182407+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Criação de gatilho
  com função de usuário
type: support-article
updated_at: '2025-03-12T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29607113728791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Cria%C3%A7%C3%A3o-de-gatilho-com-fun%C3%A7%C3%A3o-de-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29607154779415) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como criar um gatilho utilizando como retorno uma função de usuário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução**Quando o espaço do campo regra no cadastro de gatilhos não é suficiente para a fórmula que se deseja inserir, ou quando a regra é muito complexa, a sugestão é de inserção de uma função de usuário no gatilho.

Neste exemplo criamos uma função simples que retorna um texto:

![Custom Gatilho 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29607113692183)

Após compilar essa customização, vamos inserir a chamada dessa função de usuário no cadastro do gatilho:

![Custom Gatilho 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29607113697047)

Neste exemplo, ao preencher o campo de **"Código do Produto" (B1\_COD)**, a função "**U\_GAT01**" deve ser executada e o resultado dela será levado para o campo de **"Descrição do Produto" (B1\_DESC).**

Caso necessite de informações sobre os campos na tela de inclusão de gatilhos, consulte:

[Gatilhos (CFGX037 - SIGACFG)](https://tdn.totvs.com/x/uiWbEg)

Após o preenchimento do campo **"Código do Produto" (B1\_COD)** no **"Cadastro de Produtos" (MATA010)** a função **"U\_GAT01"** é executada, e seu retorno é preenchido no campo **"Descrição do Produto" (B1\_DESC):**

![Custom Gatilho 03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29607113699479)

Saiba mais:

* [Criação de gatilho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021876611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-gatilho)
* [Como criar um gatilho em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051029514-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-gatilho-em-MVC)
* [Retirar o gatilho (SX7) de uma rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439811-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retirar-o-gatilho-SX7-de-uma-rotina-MVC)
* [Gatilho entre tabelas em rotina mvc](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018867011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gatilho-entre-tabelas-em-rotina-mvc)
* [Como utilizar gatilhos para preenchimento dos campos em rotinas MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018580812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-gatilhos-para-preenchimento-dos-campos-em-rotinas-MVC)
* [Retornar o campo que esta sendo alterado em rotina MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019002512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-o-campo-que-esta-sendo-alterado-em-rotina-MVC)
* [Gatilho do cabeçalho para o item na rotina MATA415](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025839851-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Gatilho-do-cabe%C3%A7alho-para-o-item-na-rotina-MATA415)
* [Execução de Gatilho sem a necessidade de enter no campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019797791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-de-Gatilho-sem-a-necessidade-de-enter-no-campo)
* [Instrução não cabe no campo do gatilho ou formulas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020884771-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Instru%C3%A7%C3%A3o-n%C3%A3o-cabe-no-campo-do-gatilho-ou-formulas)
* [Criando gatilho com User Function para validar a execução em rotina especifica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021541971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criando-gatilho-com-User-Function-para-validar-a-execu%C3%A7%C3%A3o-em-rotina-especifica)
