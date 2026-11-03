---
article_id: 7225284646423
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: f73a379025bb7231e105e6d8c3bf30e8bb18e366626edd5e33cca423ced04883
fetched_at: '2026-06-28T22:38:28.454973+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – SIGAFAT - Como auditar rotinas
  do faturamento via relatório de log de acessos.
type: support-article
updated_at: '2022-07-05T13:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7225284646423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Como-auditar-rotinas-do-faturamento-via-relat%C3%B3rio-de-log-de-acessos
---

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7225196524311/mceclip0.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Como auditar via relatório de log de acessos?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12.

**Solução**

A rotina serve para visualizar as ações dos usuários com suas respectivas datas, assim podemos saber quando foi alterado algo dentro do sistema.

Etapas:

1. Em Alterar na rotina do módulo **CFGA510**, na aba "Restrições de Acesso", selecione na parte dos itens a Filial do sistema que o usuário escolhido terá acesso.
2. Na aba "Ambientes" certifique-se que o módulo 05 Faturamento está permitido para ele.
3. Na aba "Acessos" declare os acessos que serão permitidos ou não ao usuário.
4. No módulo configurador, Caminho: Usuário > Senhas > Política (**CFGA500**) na aba "Outros" na parte Regras de Auditoria, marcar todas as opções como sim e no campo "Auditar autenticação/acesso no Rest" deixe como "Sim, todas as requisições. Após isso, Salvar"
5. Agora, para ver o rastro, basta ir no SIGACFG (Módulo Configurador) no Caminho: Base de Dados > Auditoria > Log de Acesso (**APCFGR40**), configurar nos parâmetros o intervalo de data desejado para ser auditado, e no campo "Id Usuario ?" selecionar o usuário a ser analisado no relatório, no campo "Evento ?" marcar como "Todos".
6. Assim, será possível em um certo intervalo de tempo, de um certo usuário selecionado, será possível visualizar todos os eventos que fez ().

Alguns exemplos de Eventos:

Entrar no sistema (Login) / Sair do sistema (Logout) / Incluir / Alterar / Excluir.

![](https://atendimento.totvs.com/attachments/token/xfJl1ARERL7HhRR0OP6n8M8rF/?name=image001.png)
