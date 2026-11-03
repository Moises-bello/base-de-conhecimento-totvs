---
article_id: 1500000564121
category: Financeiro
content_hash: a06458a4b26293a247a8ca320963a94a7402d400313bb7a427b26bf0e2f9adcd
fetched_at: '2026-06-28T22:38:01.244514+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como ativar ou desativar
  customizações no Protheus
type: support-article
updated_at: '2022-06-20T22:57:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000564121-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-ativar-ou-desativar-customiza%C3%A7%C3%B5es-no-Protheus
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como ativar e desativar customizações no Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

Muitos clientes utilizam Pontos de Entrada para a execução de rotinas, ou seja, uma otimização para atendimento de necessidade específica. Estas customizações podem ser ativadas e desativadas através do **appserver.ini**Existe neste arquivo uma chave chamada IXBLOG que deverá ser adicionada nas configurações do ambiente (***environment***), esta chave receberá o seguinte conteúdo:  
  
**IXBLOG=LOGRUN**  
Executa e armazena informações dos Pontos de Entrada encontrados durante a execução do sistema. Ao informar a chave, o sistema grava um *LOG* dentro do diretório IXBLOG (C:\TOTVS 118\Protheus\_Data\ixblog), com o arquivo ‘nome do usuário’+\_+’sequencial.log para que seja possível efetuar a análise.  
  
**IXBLOG=NORUN**  
Armazena as informações no *LOG*, porém NÃO executa o Ponto de Entrada.

**TABELA XX7 - Status=2**

Para teste completo em ambiente livre de customizações, alterar o campo "Status=2" , desta forma não serão carregadas as customizações.

**Para maiores informações;**

<https://tdn.totvs.com/pages/viewpage.action?pageId=43549250>
