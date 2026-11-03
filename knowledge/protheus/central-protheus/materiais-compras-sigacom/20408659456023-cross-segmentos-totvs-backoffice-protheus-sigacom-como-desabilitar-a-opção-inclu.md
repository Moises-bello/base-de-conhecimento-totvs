---
article_id: 20408659456023
category: Materiais - Compras (SIGACOM)
content_hash: d41d9376db93ccae940582d0182780cbcded12dfc08da223eb7e6798e8af2179
fetched_at: '2026-06-28T22:41:15.731569+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como desabilitar a
  opção "Incluir" da consulta padrão?
type: support-article
updated_at: '2024-01-08T16:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20408659456023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-a-op%C3%A7%C3%A3o-Incluir-da-consulta-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649628695) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao clicar na "lupa" da consulta padrão de algum campo, o sistema abre a tela abaixo. Como faze para desabilitar o botão "Incluir" para que não apareça mais e não seja mais possível incluir um novo cadastro?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649631767)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Protheus Compras - Todas as versões  
  
**Solução**Para realizar a desabilitação desse campo, será necessário seguir o passo a passo descrito abaixo:

1º passo: Verifique o nome do campo que deseja ajustar a consulta padrão. Para isso, clique no campo desejado até ficar azul e clique em F1 do teclado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649633303)

2º passo: Acesse o SIGACFG para verificar qual tabela é responsável por essa consulta padrão. Acessar o módulo configurador -> Base de dados -> Dicionário -> Base de dados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659421463)

Depois disso, selecione Empresa teste -> Dicionário de dados -> Pesquise o nome da tabela (no caso SC7)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649635863)

Clique no nome da tabela -> Campos -> Localize o campo em questão -> Visualizar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649637527)

Vá na aba "Opções" -> verifique o nome da tabela na linha Consulta padrão. No caso é a tabela SB1 do cadastro de produto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649639575)

3º passo: Agora, acessar o CFG para alterar a configuração dessa consulta padrão. Acesse o módulo configurador -> Base de dados -> Dicionário -> Base de dados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659421463)

Depois clique em Empresa teste -> Consultas padrão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659426583)

Pesquise a consulta padrão desejada -> Clique em "Editar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659427863)

Clique em "Avançar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649648663)

O sistema avançará para a tela abaixo. Desabilite a opção "Habilitar Inclusão", ou seja, deixe sem o certinho no quadrado, conforme print abaixo e clique em "Avançar":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649650071)

Clique em "Avançar" novamente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659433367)

Clique em "Avançar" novamente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408649654423)

E depois em "Finalizar".

Depois disso, log novamente no sistema e clique na consulta padrão do campo em questão e note que o botão "Incluir" não irá mais aparecer.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20408659439639)

**Saiba Mais:**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
