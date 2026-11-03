---
article_id: 28136617191575
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 247593d81be4df82a5bcf479cf82791de5651f4d33b1ef05e1d29b76caca9d1e
fetched_at: '2026-06-28T22:38:28.770851+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Acrescentar campo como índice
  em consultas no faturamento
type: support-article
updated_at: '2024-11-28T20:08:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28136617191575-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Acrescentar-campo-como-%C3%ADndice-em-consultas-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610890135) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como acrescentar campo como índice em consultas no faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

1 - Saiba em qual consulta padrão deseja acrescentar o campo como índice de pesquisa, para isso, vá até o campo com a consulta (lupa), de Enter nele e aperte F1 (para ver o nome técnico dele)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610892183)

* OBS: A tabela do campo são as duas primeiras letras do campo, exemplo: "**ADB**\_CAMPO (Tabela **ADB**)" e "**A1**\_COD (Tabela S**A1**)"

No exemplo: "C5\_CLIENTE"

2 - Vá no configurador no caminho "SIGACFG > Base de dados > Dicionário > Base dados" na parte do menu esquerdo "Dicionário" e depois pesquise pela tabela na qual o campo que possui a consulta padrão que deseja alterar está e altere.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617147159)

No exemplo: "SC5"

3 - Procure pelo campo na qual deseja acrescentar em sua consulta padrão um campo como índice, selecione, edite e veja na aba "Opções" no campo "Cons. Padrão" qual é a consulta padrão a ser alterada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617150359)

No exemplo: "SA1 - Clientes"

4 - Vá no configurador no caminho "SIGACFG > Base de dados > Dicionário > Base dados" na parte do menu esquerdo "Consultas Padrão" e depois pesquise pela consulta padrão na qual deseja acrescentar o índice:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617150999)

5 - Selecione-a, edite e avance até essa tela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617151767)

6 - Edite no canto inferior esquerdo "no + amarelo" e escolha qual índice deseja acrescentar na busca e de duplo clique:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610897047)

No exemplo: "A1\_FILIAL + A1\_NREDUZ", quinto índice da tabela SIX sobre a tabela SA1.

7 - Após isso o campo ficará a esquerda, porém vazio de colunas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617153559)

8 - Edite no canto inferior direito "no + amarelo" (posicionado no novo índice), agora com a tela que abre, clique no ícone (![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610901271)) do campo "Expressão" e dê duplo clique em cada campo que deseja que componha o índice de busca que buscará o cliente. OBS: Um campo por inclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610904087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610904855)

OBS: Esse processo pode ser repetido, para serem acrescentados vários campos para compor o índice que buscará o cliente.

No exemplo: "A1\_FILIAL + A1\_COD + A1\_LOJA"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617162263)

9 - Após isso, avançar para finalizar, salvando:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136617164055)

**Antes:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610907543)

**Depois (resultado):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28136610908439)

Interpretando: Agora podemos buscar por filial (A1\_FILIAL), o nome reduzido (A1\_NREDUZ) do cliente, visualizando na consulta seus valores: Filial, código do cliente e loja do cliente (A1\_FILIAL, A1\_COD, A1\_LOJA)

**OBSERVAÇÃO:** Dúvida geral no processo de estruturação acima, contate a Equipe Protheus Framework.
