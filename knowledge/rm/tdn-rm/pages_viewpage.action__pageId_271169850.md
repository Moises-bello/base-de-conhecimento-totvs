---
content_hash: 80711046be9dcbd0485ebe643126c7c9a265975fc145ca48713192e8870e4637
fetched_at: '2026-06-29T00:08:26.261307+00:00'
page_id: '271169850'
product: rm
source: tdn-rm
title: Segurança Estendida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271169850
version: 12
---

## **CONTEÚDO**

Aviso de Descontinuidade

A partir das seguintes versões essa funcionalidade foi removida!

12.1.2410 - Patch 100

12.1.2406 - Patch 156

12.1.2402 - Patch 228

12.1.2310 - Patch 257

## **01. VISÃO GERAL**

  A segurança estendida por Filial e/ou Centro de Custo tem como objetivo tratar as restrições de registros no sistema com funções de permissões pré-definidas dentro do cadastro de Perfis.

       Todos os cadastros e processos de todas as Gestões estarão utilizando a tratativa definida através do perfil do usuário, em cada produto.

       A Segurança Estendida é baseada na aplicação de critérios de acesso às Filiais e Centros de Custo definidos por perfil. Esses critérios irão permitir ou bloquear os usuários associados ao Perfil para ter acesso aos itens definidos nos critérios.

       Uma vez realizada a configuração de Segurança por Filial e/ou Centro de Custo do perfil do usuário em determinado produto, o mesmo só terá acesso às Filiais e aos Centros de Custos definidos.

       Se o usuário não possuir nenhum Perfil associado a ele que tenha permissão de Filial o usuário irá ser inibido de ver qualquer registro.

       A Segurança Estendida será aplicada pelo contexto de cada Coligada. Portando, o filtro deve ser informado no perfil do usuário, em cada Contexto de Sistema e Coligadas que forem necessários aplicar a segurança.

       As permissões definidas para a Segurança são restritivas e cumulativas.  
       Se o usuário tiver associado a mais de um Perfil, estas permissões se somam.

**ATENÇÃO:**A segurança estendida não está disponível para base de dados Oracle.

## **02. EXEMPLO DE UTILIZAÇÃO**

* **CONFIGURANDO A SEGURANÇA ESTENDIDA:**

Para definir e habilitar a segurança estendida deve-se criar duas tags no arquivo config do produto / módulo, a tag “XST” e a tag “XSTCC”.

       Para ativar a exibição da segurança estendida na tela de Parâmetros Globais e a interface de configuração dos critérios supracitados, as tags devem ter seu valor preenchido com “true”, conforme figura abaixo (Linhas 13 e 14):

xmlRM.exe.configtrue

















]]>

Para ativar/desativar a segurança por Filial e/ou Centro de Custo no produto / módulo, deve-se utilizar os parâmetros “Ativar Segurança por Filial” e “Ativar Segurança por Centro de Custo” na aba Segurança, menu Opções/Parâmetros Globais:

       Para ativar a segurança estendida, use os campos abaixo:  
    
**Usa segurança estendida por filial**    
        Habilite este parâmetro caso queira habilitar a segurança estendida por filial.  
    
**Usa segurança estendida por centro de custo**  
        Habilite este parâmetro caso queira habilitar a segurança estendida por centro de custo.

* **CACHE DE SEGURANÇA ESTENDIDA NO HOST**  
      
         Ao ativar a Segurança Estendida, estará por padrão ativado o Cache dessa funcionalidade, o mesmo torna a utilização do sistema mais fluída e performática, o sistema trabalha com Cache de 15 minutos, portanto qualquer alteração da Segurança Estendida será efetivada dentro desse espaço de tempo, sendo possível reiniciar o Servidor de Aplicação (Host) para forçar a limpeza do Cache. Também há a possibilidade de desativar o Cache da Segurança Estendida, tendo por efeito, aplicação imediata das alterações, porém penaliza a velocidade do sistema por completo.

       É possível configurar duas tags no arquivo RM.host.Service.exe.config para controlar a utilização do Cache da Segurança Estendida:  
    
**<add key="UseSecurityExtCache" value="true" />**  
        Esta Tag controla a ativação/desativação do uso de Cache para a Segurança Estendida.   
    
**<add key="SecurityExtCacheMaxSize" value="100" />**  
        Esta tag controla o número máximo de consultas em cache.

       Quando é aberto um cadastro que tenha registros de filial e centro de custo é aplicada a segurança. Exemplo abaixo no cadastro de consulta SQL:

       SELECT por fora do sistema:

## **03. ERRO NA APLICAÇÃO DA SEGURANÇA ESTENDIDA**

Quando um DataServer não possuir a coluna CODFILIAL ou CODCCUSTO, o filtro de segurança poderá não ser aplicado.   
Um erro será apresentado impedindo a continuidade do processo e uma mensagem de alerta será exibida informando sobre a necessidade de adicionar o campo.

Isto ocorrerá apenas quando a tabela em questão possuir a coluna, mas não estiver listada no Select da query.

Exemplo:

DataServer utiliza a tabela PFUNC, esta tabela possui a coluna CODFILIAL, mas não foi informada no Select da query.  
Isto significa que é uma tabela onde a segurança estendida deve ser aplicada obrigatoriamente.  
Entretanto o DataServer precisa ser corrigido, caso contrário a segurança seria violada!

false

**Versão:** 11.82.44 ou Superiores
