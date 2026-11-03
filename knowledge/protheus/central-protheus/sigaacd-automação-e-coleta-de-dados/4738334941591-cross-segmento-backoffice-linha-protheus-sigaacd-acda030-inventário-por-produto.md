---
article_id: 4738334941591
category: SIGAACD - Automação e Coleta de Dados
content_hash: b7ef7c37e9cf70e48a953dad96778cb9db4d33b65f1c154876987c32c5a9af1c
fetched_at: '2026-06-28T22:39:11.164634+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA030 - Inventário
  por produto guiado
type: support-article
updated_at: '2025-12-09T21:05:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4738334941591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA030-Invent%C3%A1rio-por-produto-guiado
---

O Inventário por produto guiado via Coletor de Dados no TOTVS Protheus simplifica a contagem, apresentando intuitivamente o produto para o operador informar a quantidade. O processo envolve configurar parâmetros no sistema, cadastrar operadores, locais, produtos, saldo inicial e mestre de inventário, e realizar a contagem pelo aplicativo Meu Coletor de Dados, com monitoramento e ajustes no sistema.

**Dúvida**  
Como funciona o Inventário por produto guiado via Coletor de Dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados- Todas as versões.

**Solução**

O objetivo desta rotina é tornar o inventário uma operação simples de ser executada e eficaz no resultado. Todo o processo é executado de maneira intuitiva informando sempre ao operador, os passos que devem ser seguidos.

O inventário por produto guiado trata-se de um recurso do Meu coletor de dados onde tange o tratamento de indicar o produto que deve ser inventariado sendo necessário somente informar a quantidade localizada pelo operador.

**Inventário por endereço com recontagem**

Configurar os parâmetros do sistema

1. Acessar o modulo Configurador
2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
3. Pesquise pelo parâmetro MV\_CBINVMD
4. Edite o parâmetro MV\_CBINVMD   
   ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-24-3.png?version=1&modificationDate=1553079973277&api=v2)

**Configurar os parâmetros do sistema**

a) Acessar o modulo Configurador

b) Acessar o Menu > Ambiente > Cadastros > Parâmetros

c) Pesquise pelo parâmetro MV\_VLDTINV

d) Edite o parâmetro MV\_VLDTINV  
![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-29-41.png?version=1&modificationDate=1553079973467&api=v2)

**Configurar os parâmetros do sistema**

a) Acessar o modulo Configurador

b) Acessar o Menu > Ambiente > Cadastros > Parâmetros

c) Pesquise pelo parâmetro MV\_LOCALIZ

d) Edite o parâmetro MV\_LOCALIZ  
![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-35-23.png?version=1&modificationDate=1553079973640&api=v2)

**Configurar Operador.**

a) Acessar o modulo Estoque/Custos

b) Acessar o Menu > Atualizações > ACD> Operadores

c) Clique Incluir

d) Informe os campos obrigatórios

![](https://tdn.totvs.com/download/attachments/465371630/image2019-2-19_8-16-59.png?version=1&modificationDate=1553079968747&api=v2)

**Exemplo prático do processo utilizando o Protheus**

As informações aqui apresentadas visa no simples intuito de explicar didaticamente como gerar as informações para utilização do Meu coletor de dados.

Inventário por produto guiado

* Cadastrar local de estoque
  + Acessar o modulo Estoque/Custos
  + Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
  + Clique Incluir
  + Informe os campos obrigatórios  
      
    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-39-19.png?version=1&modificationDate=1553079973737&api=v2)
  + Clique Confirmar
* Cadastrar produto
  + Acessar o modulo Estoque/Custos
  + Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
  + Clique Incluir
  + Informe os campos obrigatórios e campo de código de barras.  
    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-40-41.png?version=1&modificationDate=1553079973827&api=v2)  
    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-11_14-57-20.png?version=1&modificationDate=1553079974917&api=v2)
  + Cliente confirmar
* Cadastrar saldo inicial
  + Acessar o modulo Estoque/Custos
  + Acessar o Menu > Atualizações > Saldos > Inicial
  + Clique Incluir
  + Informe os campos obrigatórios do produto  
    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-1_14-43-31.png?version=1&modificationDate=1553079973987&api=v2)
  + Clique Salvar
* Cadastrar Mestre de Inventario
  + Acessar o modulo Estoque/Custos
  + Acessar o Menu > Atualizações > ACD > Inventário
  + Clique Incluir
  + Informe os campos obrigatórios e tipo de inventário por produto

    Configuração de inventario guiado

    Verifique na imagem abaixo que o campo Inv. Guiado está ativo.

    Esse recurso é exclusivo do Meu Coletor de dados.

    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-20_11-22-9.png?version=1&modificationDate=1553091803920&api=v2)

    Inventário

    A contagem do inventario será realizada pelo Meu Coletor de dados.
* Acessar Meu coletor de dados.
  + Acessar informando login do operador.
  + Selecionar inventario.  
    ![](https://tdn.totvs.com/download/attachments/465371630/logininventario2.gif?version=1&modificationDate=1553079977823&api=v2)
  + Realizar a contagem do item.

    Podendo selecionar um ou mais inventários para contagem online ou offline.
  + Será apresentado o produto
  + informe a quantidade e finalize.  
    ![](https://tdn.totvs.com/download/attachments/465371630/inventarioguiado.gif?version=1&modificationDate=1553079979887&api=v2)
* Visualizar o mestre de inventário.
  + Acessar o modulo Estoque/Custos
  + Acessar o Menu > Atualizações > ACD > Inventário
  + Posicionar no inventário 000000047 > Outras Ações > Monitor
  + Verificar as contagens, se necessário gerar acerto.  
    ![](https://tdn.totvs.com/download/attachments/465371630/image2019-3-18_15-59-31.png?version=1&modificationDate=1553079980973&api=v2)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
