---
article_id: 37322060976151
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 95f9d8361db23895ecead06e64e598b866d41cefa993ecad4bcbe0bbb0e696d5
fetched_at: '2026-06-28T22:39:08.008952+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como configurar
  permissões e restrições de armazéns por Usuário ou Produto?
type: support-article
updated_at: '2025-12-29T17:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37322060976151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-AGRA045-Como-configurar-permiss%C3%B5es-e-restri%C3%A7%C3%B5es-de-armaz%C3%A9ns-por-Usu%C3%A1rio-ou-Produto
---

O parâmetro MV\_RESTARM no TOTVS Protheus permite configurar permissões de uso de armazéns por usuário, produto ou ambos. Valores possíveis são 0 (sem controle), 1 (por usuário), 2 (por produto) e 3 (usuário e produto). Para ativar, cadastre permissões no armazém via AGRA045. Usuários não autorizados recebem aviso de restrição, exceto administradores.

 Tempo aproximado para leitura: **00:03:12 min**  
   
**Dúvida**

Como configurar permissões e restrições de uso de armazéns por usuário ou produtos específicos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para atingir este objetivo é possível por meio da configuração do parâmetro MV\_RESTARM, onde o mesmo tem por objetivo **indicar se utiliza o controle de permissão de uso de armazéns e em qual nível, sendo:**

**- 0 = Não utiliza;**

**- 1= Por usuário;**

**- 2 = Por produto;**

**- 3= Por usuário e produto**

**Opções para configurações de permissões ou restrições**

A primeira possibilidade é deixar o Parâmetro **MV\_RESTARM = 0**. Desta forma ele não utiliza o controle de permissão de uso de armazéns.

Quando o parâmetro está com conteúdo 1, 2 ou 3 **e deseja mantê-lo assim**, deve-se fazer o cadastro das **permissões no Armazém**. Veja abaixo:

**- 1 -** Na tela de cadastro de Locais de estoque(AGRA045), selecione um armazém e clique em alterar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37322024269719)

**- 2 -** Nesta nova tela será apresentada duas abas sendo "Permissões por Armazéns E "Permissões por Produto";

**- 3 -** Selecione uma das duas opções;

**- 4 -** Preencha os dados de acordo com a opção selecionada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37322060967831)

**- 5 -** Clique em Confirmar.

Quando um usuário que ***não estiver cadastrado*** ***nesta permissão*** para o armazém tentar realizar uma movimentação, o sistema irá apresentar o **HELP "SEMPERM" ou "RESTPRD"** informado esta restrição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37322060968983)

**OBS:** Essa restrição não se aplica para usuário administrador

**Saiba mais:**

[*SIGAEST - MATA230 - MV\_RESTTM - Como configurar permissões por TM a usuários específicos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420276723735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA230-MV-RESTTM-Como-configurar-permiss%C3%B5es-por-TM-a-usu%C3%A1rios-espec%C3%ADficos)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
