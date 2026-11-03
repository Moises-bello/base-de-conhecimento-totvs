---
article_id: 360043563633
category: Escrita Fiscal - Error.log
content_hash: cd2ae72d8b1f302639d71186409758a1c3412834079b557fb3d66e7d15944f26
fetched_at: '2026-06-28T22:39:32.794729+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Botões da TES MATA080
  desabilitados (PE MA080MNU)
type: support-article
updated_at: '2021-07-08T13:51:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043563633-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Bot%C3%B5es-da-TES-MATA080-desabilitados-PE-MA080MNU
---

**Ocorrência** Botões de cadastro de TES (MATA080) desaparecem após atualização do fonte

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12

**Solução:**

Com a atualização do fonte MATA080 (TES) será necessário reconfigurar a customização que usa o ponto de entrada MA080MNU.

Sugiro que consulte sua equipe de customização para ajustes, é possível localizar o Ponto de Entrada especifico via Log do sistema.

Se precisar de auxilio com customizações poderá abrir uma nova solicitação com nosso time de *ADVPL*.

Muitos clientes utilizam Pontos de Entrada para a execução de rotinas, ou seja, uma otimização para atendimento de necessidade específica.

Estas customizações podem ser ativadas e desativadas através do **appserver.ini**

Existe neste arquivo uma chave chamada IXBLOG que deverá ser adicionada nas configurações do ambiente (environment), esta chave receberá o seguinte conteúdo:

**XBLOG=LOGRUN**

Executa e armazena informações dos Pontos de Entrada encontrados durante a execução do sistema. Ao informar a chave, o sistema grava um LOG dentro do diretório IXBLOG (C:\TOTVS 118\Protheus\_Data\ixblog), com o arquivo ‘nome do usuário’+\_+’sequencial.log para que seja possível efetuar a análise.

**IXBLOG=NORUN**

Armazena as informações no LOG, porém NÃO executa o Ponto de Entrada.

**TABELA XX7 - Status=2**

Para teste completo em ambiente livre de customizações, alterar o campo "Status=2" , desta forma não serão carregadas as customizações.

**Para maiores informações;**

**<https://tdn.totvs.com/pages/releaseview.action?pageId=6784261>**
