---
article_id: 35515574708759
category: Financeiro - Contabilização
content_hash: 251172188f56d4938bb378335fca2afaebe5d35b7728f4fcf54745971b6c4a4f
fetched_at: '2026-06-28T22:38:05.203503+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Bloqueio do usuário
  na contabilização
type: support-article
updated_at: '2025-10-09T12:50:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35515574708759-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Bloqueio-do-usu%C3%A1rio-na-contabiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35515574690327) Tempo aproximado para leitura: **00:06 min**  
  
**Dúvida**  
Para a contabilização, existe algum parâmetro que impeça o acesso simultâneo à rotina, de forma que, enquanto um usuário estiver utilizando-a, outro não possa acessá-la?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Atualmente, não existe um parâmetro que impeça o acesso simultâneo de usuários à rotina. O bloqueio de contabilização (lock) atua apenas como uma mensagem informativa, com o objetivo de alertar os usuários de que há mais de um acesso ocorrendo no mesmo momento.

Contudo, há um parâmetro disponível que permite desabilitar essa mensagem, caso não se deseje exibi-la em tela. Ressalta-se, porém, que este parâmetro não impede o acesso simultâneo de usuários à rotina.

Este parâmetro define a habilitação do controle de serialização, responsável por gerenciar os processos Off-Line e On-Line no módulo de Contabilidade Gerencial. Sua função é utilizar um semáforo para controlar o acesso simultâneo a processos críticos, assegurando a integridade e a consistência dos dados.

* **1 (padrão):** Habilita o controle de Semáforo/Serialização, garantindo a execução ordenada dos processos.
* **2:** Mantém o controle de Semáforo/Serialização habilitado.
* **3:** Ativa o modo de teste, exibindo alertas durante a ativação ou desativação do semáforo, útil para validações e ajustes.

A configuração adequada deste parâmetro é fundamental para prevenir conflitos entre processos simultâneos e assegurar a confiabilidade das operações contábeis.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35515574691735)

**Saiba mais**

[Semáforo - Tabela F74 - Controle de Processamento Simultâneo no Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=600817818)

[Financeiro (SIGAFIN)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545422-Financeiro-SIGAFIN)
