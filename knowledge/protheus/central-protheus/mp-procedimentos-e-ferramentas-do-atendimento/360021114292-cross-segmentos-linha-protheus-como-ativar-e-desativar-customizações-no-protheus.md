---
article_id: 360021114292
category: MP - Procedimentos e Ferramentas do Atendimento
content_hash: 20f22d08cf58f7b9d64616da5a06a3d9290f1d4611aac4b3db34157cb855731a
fetched_at: '2026-06-28T22:36:36.780346+00:00'
product: protheus
section_id: 360011719313
source: central-protheus
title: ' Cross Segmentos - Linha Protheus - Como ativar e desativar customizações
  no Protheus'
type: support-article
updated_at: '2026-05-15T20:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus
---

**Ocorrência**Como ativar e desativar customizações no Protheus?  
  
**Ambiente** Cross Segmentos - Linha Protheus - A partir da versão 12  
  
**Solução**Muitos clientes utilizam Pontos de Entrada / funções customizadas para a execução de rotinas, ou seja, uma otimização para atendimento de necessidade específica. Estas customizações podem ser desativadas provisoriamente para testes pontuais no sistema padrão. Segue abaixo métodos para desabilitar as chamadas customizadas:

**1 - Através da chave IXBLOG no arquivo APPSERVER.ini**

Deverá ser adicionado no arquivo **appserver.ini -** nas configurações do ambiente (***environment***) uma chave chamada IXBLOG atribuindo-lhe o seguinte conteúdo:

**IXBLOG=NORUN**  
Deste modo, ao realizar o processo no sistema, NÃO serão executados os Pontos de Entrada, permitindo validar o comportamento no Padrão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402048902551)

OBS: Uma outra alternativa é: **IXBLOG=LOGRUN**Porém, deste modo, ao realizar o processo no sistema, os Pontos de Entrada serão normalmente executados, mas, o sistema irá gravar um *LOG* dentro do diretório IXBLOG *(C:\TOTVS 118\Protheus\_Data\ixblog)*, com um arquivo *‘nome do usuário’+\_+’sequencial.log´* com informações dos Pontos de Entrada encontrados durante a execução do sistema,  para que seja possível efetuar a análise.

**2 - Através do Configurador CFG - Catálogo de Personalizações**

Você pode desativar suas customizações através do caminho: "*Ambiente - Cadastro - Catalogo de Personalizações"*Posicione na Customização - Alterar - Muda para 2 - Desabilitado nos detalhes da tela de alteração, de modo que, na tabela XX7 o campo X7\_STATUS seja preenchido = 2

[Veja detalhes de como realizar aqui!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-MP-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-)

**3 - Desabilitar customizações chamadas no dicionário de dados**

Se o ponto de entrada estiver **compilado no dicionário** ele ainda pode ser chamado no Log e executado no sistema. Deste modo é necessário buscar seus campos (SX3) e gatilhos (SX7) que possuam chamada customizada. Busque os respectivos campos X3\_PROPRI e X7\_PROPRI registrados = U ou mesmo, demais campos da SX3 / SX7 que contenham a chamada U\_

Em ambiente e base de homologação retire / delete as chamadas customizadas
