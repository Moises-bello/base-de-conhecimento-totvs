---
article_id: 360060683734
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 7cd6aca58a81f9e63ffa7cb6763173feac00e411b00bf98b239efa5201231ad7
fetched_at: '2026-06-28T22:39:09.780592+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Comportamento
  do campo B1_CODBAR e cálculo do dígito verificador
type: support-article
updated_at: '2026-04-06T13:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060683734-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Comportamento-do-campo-B1-CODBAR-e-c%C3%A1lculo-do-d%C3%ADgito-verificador
---

No Protheus, o campo B1\_CODBAR armazena códigos de barras com 15 caracteres, preenchendo automaticamente o dígito verificador na última posição via gatilho. O parâmetro MV\_EANCALC controla esse cálculo: se .T., o sistema calcula o dígito; se .F., permite entrada manual sem cálculo automático. Para alterar, ajuste MV\_EANCALC no Configurador e reinicie a rotina de Cadastro de Produtos.

**Dúvida**

Na rotina Cadastro de Produtos, o campo B1\_CODBAR preenche no banco de dados 15 caracteres mas meu código de barras possui menos dígitos do que isso. Por quê isso acontece? Tem como aproveitar o último dígito? eu posso remover o digito verificar automatic?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque - Todas as versões

**Solução**

O campo B1\_CODBAR do Cadastro de Produtos (tabela SB1) é projetado para armazenar o código de barras do produto.

Por padrão, o sistema utiliza um gatilho para calcular e preencher automaticamente o dígito verificador na última posição do campo, baseando-se no código informado.

Devido a essa regra de validação e ao tamanho padrão do campo no dicionário de dados (SX3), o preenchimento pode ocupar as posições reservadas para o cálculo estrutural do código de barras.

Para controlar se o sistema deve ou não realizar o cálculo automático do dígito verificador, utiliza-se o parâmetro **MV\_EANCALC**.

* Se o parâmetro estiver configurado como **.T.** (True/Verdadeiro): O sistema calcula o dígito verificador e o preenche automaticamente no campo.
* Se o parâmetro estiver configurado como **.F.** (False/Falso): O sistema não realiza o cálculo, permitindo que o usuário informe o código de barras livremente, sem a interferência do gatilho de validação do dígito.

**Passos**

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Vá em **Ambiente > Dicionário > Base de Dados**.
3. Clique em **Parâmetros** e busque pelo parâmetro **MV\_EANCALC**.
4. Altere o valor para **.F.** caso deseje desativar o cálculo automático e utilizar o campo de forma manual.
5. Confirme a alteração e reinicie a rotina de Cadastro de Produtos para que a nova configuração seja aplicada.

| **Nome** | MV\_EANCALC |
| --- | --- |
| Tipo | L |
| **Cont. Por** | .T. |
| Descrição | Define se o dígito verifcador do código de barras será calculado. .T. = Sim; .F. = Não |
|

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
