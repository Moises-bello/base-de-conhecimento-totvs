---
article_id: 26122660843927
category: Meu RH - Requisições
content_hash: 60b2ac5c2cc91e8303af3fe1082dedc260958f19e363b76a601036a66b3f7cbe
fetched_at: '2026-06-28T22:47:28.040210+00:00'
product: rm
section_id: 26902073559319
source: central-rm
title: RH - RM - Meu RH - Como habilitar e realizar requisições gerais
type: support-article
updated_at: '2025-02-03T11:39:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26122660843927-RH-RM-Meu-RH-Como-habilitar-e-realizar-requisi%C3%A7%C3%B5es-gerais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26122715409303) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**

Como habilitar e realizar requisições gerais no Meu RH?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2402, patch 134

**Solução**

1. Acessar o módulo de **Serviços Globais** e navegar até **Perfis**, selecione o sistema **Gestão de Pessoas** para habilitar a permissão ***12.01.02.01.01.10 Geral*** no perfil desejado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122715411991)

2. Acessar o módulo de **Gestão de Pessoas** e navegar até a aba **Configurações > Parametrizador**. Dentro do parametrizador, selecionar o item **07.00.16 - Portal Meu RH**e clicar em Avançar. Habilitar a permissão ***Considerar a nova requisição geral para o Meu RH***.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122715412759)

3. No módulo de **Gestão de Pessoas**, aba **Configurações**, será habilitada a opção ***Categorias de Tipo de Requisição***. Clique nesta opção e em seguida clique em Incluir para cadastrar uma nova categoria de tipo de requisição, que será utilizada para a requisição geral.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122715413911)

4. No módulo de **Gestão de Pessoas**, aba **Configurações**, clique em **Tipos de Requisição**. Na lista exibida, selecione a requisição geral que deseja utilizar no Portal Meu RH e edite-a. Preencha o campo **Cod. Categoria** com a categoria criada no passo anterior.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122660829335)

Ainda dentro da tela de edição da requisição geral que será utilizada dentro do Portal Meu RH, clique na aba **Permissões Meu RH**. Deve-se conceder permissão para o perfil do chefe/supervisor desejado nesta tela, localizando o perfil cujo Cód. Sistema é V e marcar a caixa de seleção **Vinculado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122660831127)

Agora, dentro do Meu RH, navegue até o painel **Gestor** e clique em **Requisições**. Será exibida a opção de Requisição Geral.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122660832151)

Clique na opção **Requisição Geral** e em seguida clique no botão **Nova requisição**. Será aberta uma janela para que seja selecionada a categoria da requisição. Neste campo, serão listadas todas as categorias de requisições criadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122660832919)

Após selecionar a categoria da requisição, o campo **Tipo de requisição** será habilitado. Nele, serão listadas todas as requisições que possuem a categoria selecionada na etapa anterior vinculadas a ela.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26122715421591)

**Atenção!**

Se sua empresa utiliza a parametrização de Hierarquia por posição e está configurada para não utilizar o fluxo do Agilis nas requisições, **neste momento esta funcionalidade não está disponível**.   
Estamos trabalhando para disponibilizá-la o mais breve possível.  
  
Para identificar se sua empresa está com esta parametrização, verifique a documentação [Ativação da Hierarquia Por Posição](https://tdn.totvs.com/pages/viewpage.action?pageId=653572529).

**Artigos relacionados:**

[Requisições Gerais](https://tdn.totvs.com/pages/viewpage.action?pageId=834829292)

[Tipos de Requisição - RHU](https://tdn.totvs.com/pages/viewpage.action?pageId=452719602)

[RH - RM - RHU - Parametrizações iniciais para utilizar requisição(s) no TOTVS Gestão de Pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034897674-RH-RM-RHU-Parametriza%C3%A7%C3%B5es-iniciais-para-utilizar-requisi%C3%A7%C3%A3o-s-no-TOTVS-Gest%C3%A3o-de-Pessoas)
