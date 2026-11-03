---
article_id: 21461416880023
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 52c6e8204cf40862049ef04cc02fae8be528f7154bea96d5e9f1dc40239f071e
fetched_at: '2026-06-28T22:39:09.475506+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - É possível
  adicionar campo customizado no Facilitador de Produtos?
type: support-article
updated_at: '2024-02-19T17:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21461416880023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-%C3%89-poss%C3%ADvel-adicionar-campo-customizado-no-Facilitador-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21461402445335) Tempo aproximado para leitura: 00:01:00 min **Dúvida**É possível adicionar campo customizado no Facilitador de Produtos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Sim, é possível que o Facilitador tenha outros campos padrões e também customizados.

**Passo 1** - Criar ou identificar o campo customizado que deseja inserir no Facilitador. De maneira didática, criamos o campo B1\_XPTO no Dicionário de Dados (SIGACFG):

![](https://totvssuporte.zendesk.com/attachments/token/xJISSneQqL50lGp1fAoKc3AhR/?name=image.png)

**Passo 2** - Inserir o campo no parâmetro MV\_A010FAC. É importante colocar a barra ( / ) ao final da sequencia de campos que deseja incluir no facilitador. No exemplo abaixo, o campo criado no Passo 1 foi cadastrado:

![](https://totvssuporte.zendesk.com/attachments/token/c9v8QHYnxB9lO96AEHHBqEQ7Q/?name=image.png)

OBS: Detalhes do parâmetro MV\_A010FAC: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como configurar o parâmetro MV\_A010FAC para adicionar campos corretamente e seu limite?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17564654562583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-configurar-o-par%C3%A2metro-MV-A010FAC-para-adicionar-campos-corretamente-e-seu-limite)

**Passo 3** - Abrir o Facilitador (MATA010 -> Outras Ações -> Facilitador) e na primeira tela do Wizard, buscar seu campo customizado:

![](https://totvssuporte.zendesk.com/attachments/token/WKl0d7aiVpXsZMerBqxrqfO0w/?name=image.png)

Com isso, basta seguir para os proximos passos do Wizard para efetuar a alteração desejada com base em seus critérios.

Saiba mais:

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
