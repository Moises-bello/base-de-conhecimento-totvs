---
content_hash: 3cc8d839230781dbe3dee377d5b2a619455db8ebbea2a5525fb22797033485a4
fetched_at: '2026-06-29T00:05:57.084419+00:00'
page_id: '162168869'
product: rm
source: tdn-rm
title: COMO FAZER - Cancelamento de férias já lançadas (.Net)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=162168869
version: 1
---

Produto

**RMLabore**

Processo: **Cancelamento de férias já lançadas (.Net)**

Versão: 11.5X ou superior

Cancelamento de férias já lançadas no envelope do funcionário

Este roteiro irá auxiliar nos casos onde as férias já foram lançadas para o envelope do funcionário, fazendo com que a rotina de cancelamento do menu Movimento -> Férias -> Cancelamento não surta efeito.

Férias cadastrada para o funcionário

Clique para visualizar imagem

1. Acesse o cadastro do funcionário e altere a situação do mesmo de F – Férias para A – Ativo, no campo data de mudança, insira uma data posterior a data de início das férias do funcionário

   Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)
2. Vá até o histórico de situação do funcionário, deverão existir dois históricos: um para quando o funcionário entrou em férias e outro para quando ficou Ativo novamente (passo 1), apague ambos.

   Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)
3. Acesse o menu: Movimento -> Folha de pagamento -> Cancelamento de Movimento (Delphi) ou Folha Mensal -> Cancelamento (.Net) e faça o cancelamento do envelope do funcionário lembrando de marcar o parâmetro “Cancela movimento de férias”.

   Os demais parâmetros ficam a critério do cliente, avance até executar.

   Clique para visualizar imagem
4. Agora acesse o período aquisitivo do funcionário e na aba Período de Gozo, apague as férias do funcionário

   Clique para visualizar imagem
5. Agora, basta cadastrar novamente as férias do funcionário, fazendo as devidas correções e lançar novamente.

   Clique para visualizar imagem
