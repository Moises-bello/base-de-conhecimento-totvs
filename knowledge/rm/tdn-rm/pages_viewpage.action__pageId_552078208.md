---
content_hash: b2a785ba276d78841a504fa74bf9cb4c5d21df636d26bb32a3da32f8188f3261
fetched_at: '2026-06-29T00:10:44.010222+00:00'
page_id: '552078208'
product: rm
source: tdn-rm
title: Dicas Automação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552078208
version: 12
---

# **1) Introdução**

---

Este documento tem por finalidade listar problemas nas execuções de script do Testflow e suas soluções, além de listar alguns recursos já disponíveis no auxilio da manutenção dos projetos.

# **2) Problemas e soluções**

---

## Problema

Script funciona, porém a atividade SQL apresenta erros.

## Solução

Este problema acontece pois, mesmo quando o script webservice finaliza com (200 OK), independente da mensagem de erro do processo, o TestFlow considera que o script foi executado com sucesso, dando uma falsa impressão ao teste.

#fffPara solucionar este problema:

1. Consulte todas as atividades de script ws presentes no projeto, verificando se terminaram do modo desejado, através do link de "olhinho" presente no log
2. Verificar que o log do processo WS, mesmo com status code 200, na verdade terminou com um erro

## Problema

Script winforms apresentando erros como o log abaixo:

## Solução

Após a atualização da devExpress, os scripts Winforms passaram a exibir esse problema nas ações de Refresh.  A solução é remover todas as ações de refresh da atividade Winforms.

#fffPara solucionar esse problema:

1. Ir no log da atividade e clicar com o botão direito na atividade winforms e selecionar editar atividade.
2. Remover a atividade de refresh presente na atividade.

## Problema

Não consigo simular o problema acontecendo pois o Testflow ao final do script deleta a base com o cenário pronto.

## Solução

Há uma série de métodos para conferir o script executando, o meu método preferido é simplesmente alterar o projeto, alterando a última ação para um código c# que não faz nada. Desta forma, podemos acessar a base onde o script executou para verificar / debugar o cenário do projeto.

#fff

Editando o projeto

1. Na visão de projetos, clicar em editar projeto.
2. Alterar a última atividade pela atividade C# Faz Nada
3. Rodar novamente o projeto e colher a base e o servidor consultando o log.

   Neste caso a base TF\_LWXVPX0Z em BD-AUTOMACAO\SQL2014 estará pronta para ser acessada.

   Importante: Após a análise, alterar novamente a atividade C# Faz nada para a atividade original que foi substituida.

## Problema

Preciso executar um script winforms porém o RM não enxerga o RM.exe como programa executável.

## Solução

Para iniciar uma atividade winforms, precisamos usar uma TAG no RM que é a /automationtest. Sem ela, o TestFlow não conseguirá renderizar as telas corretamente.

#fff

Para executar / criar / analisar uma automação winforms seguir os passos:

1. Certificar-se que o seu atalho do RM.exe esteja com a flag /automationtest preenchida. Iniciar o RM por este atalho.

   Inicie e logue no RM através deste atalho.

   Importante: Para que a automação funcione o Agent deve ser iniciado primeiro antes do RM.host.exe e do RM.exe.   
   Caso inicie o RM antes do Agent o Testflow não irá enxergar o PID do RM, e o script não poderá ser iniciado.
2. Editar a atividade Winforms no log do projeto.
3. Dentro da atividade winforms, selecione o servidor cujo agent esteja iniciado e o RM.exe iniciado e logado.
4. Clicar em iniciar para começar uma nova gravação ou executar para executar um script já existente

# **3) Outras documentações disponíveis**

---

* [Automação via Webservices](https://tdn.totvs.com/pages/viewpage.action?pageId=349184324)
