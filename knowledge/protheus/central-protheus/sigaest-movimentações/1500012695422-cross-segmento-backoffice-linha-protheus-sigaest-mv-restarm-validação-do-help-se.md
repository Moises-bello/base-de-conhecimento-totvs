---
article_id: 1500012695422
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5cb02cd2d681a44a99075e2144fe712660ca51a4346006f325b44757b1b2c434
fetched_at: '2026-06-28T22:38:57.200049+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_RESTARM - Validação
  do HELP SEMPERM ou RESTPRD
type: support-article
updated_at: '2025-10-13T18:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012695422-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-RESTARM-Valida%C3%A7%C3%A3o-do-HELP-SEMPERM-ou-RESTPRD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21693606928151) Tempo aproximado para leitura: **00:04:15 min****

**Dúvida**

Ao alterar o cadastro de uma Ordem de Produção (OP) ou outros movimentos de estoque é apresentado o **HELP: SEMPERM** ou também o **HELP RESTPRD**. Como corrigir estes HELP?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21693650804887)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Este problema é decorrente da configuração do parâmetro MV\_RESTARM, onde o mesmo tem por objetivo **indicar se utiliza o controle de permissão de uso de armazéns e em qual nível, sendo:**

**- 0 = Não utiliza;**

**- 1= Por usuário;**

**- 2 = Por produto;**

**- 3= Por usuário e produto**

**Como corrigir este HELP?**

A primeira possibilidade é deixar o Parâmetro **MV\_RESTARM = 0**. Desta forma ele não utiliza o controle de permissão de uso de armazéns.

Quando o parâmetro está com conteúdo 1, 2 ou 3 **e deseja mantê-lo assim**, deve-se fazer o cadastro das **permissões no Armazém**. Veja abaixo:

**- 1 -** Na tela de cadastro de Locais de estoque(AGRA045), selecione um armazém e clique em alterar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21693780772503)

**- 2 -** Nesta nova tela será apresentada duas abas sendo "Permissões por Armazéns E "Permissões por Produto";

**- 3 -** Selecione uma das duas opções;

**- 4 -** Preencha os dados de acordo com a opção selecionada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21693965781527)

**- 5 -** Clique em Confirmar.

Quando um usuário que ***não estiver cadastrado*** ***nesta permissão*** para o armazém tentar realizar uma movimentação, o sistema irá apresentar o **HELP "SEMPERM" ou "RESTPRD"** informado esta restrição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21693606951191)

**OBS:** Essa restrição não se aplica para usuario administrador

**Saiba mais:**

[SIGAEST - MATA230 - MV\_RESTTM - Como configurar permissões por TM a usuários específicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420276723735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA230-MV-RESTTM-Como-configurar-permiss%C3%B5es-por-TM-a-usu%C3%A1rios-espec%C3%ADficos)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
