---
article_id: 360019267711
category: PCO - Reprocessamentos
content_hash: dd381ca8bf79b8d91c747e3a16e41b7bfaf1daa881c58eb8b715cb127115fe02
fetched_at: '2026-06-28T22:37:07.023936+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO Como reprocessar lançamento.
type: support-article
updated_at: '2025-05-07T18:05:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019267711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Como-reprocessar-lan%C3%A7amento
---

**Dúvida**Como reprocessar lançamento de algum processo no módulo PCO?  
Mostraremos um exemplo com o processo 000082, porém o princípio é o mesmo para qualquer processo.

**Ambiente**Protheus - PCO - a partir P12.1.17  
  
**Solução**Acessar a Rotina PCOA310, PCO ->Miscelânea -> Reprocessamentos-> Lançamentos.  
Posicionar sobre o processo e clicar em Reprocessar.

![1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360015072651/1.jpg)

 A coluna, Perm. Reproc.? Deve estar igual a sim.

Os Campos, **Período de?/ Período Ate**? (selecionado em vermelho na imagem a baixo) São referentes a tabela AKD para informar o período que deseja excluir os registros no modulo PCO, caso marque a flag "apagar lançamentos do período?

O quadro filtro refere-se a tabela Origem, em nosso exemplo a CT2 (selecionado em azul na imagem a baixo).  
Clique em Editar e defina o filtro do que irá reprocessar (selecionado em azul na imagem a baixo).

![2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360015074051/2.jpg)

Um exemplo de Filtro pode ser:  
Data Lcto Maior ou igual a 01/10/2018 e Data Lcto Menor ou igual a 10/10/2018

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073661614/mceclip0.png)

Se optar por selecionar a Flag, Apagar Lançamentos do Período?  
Após clicar em Ok, exibirá uma outra tela para confirmar o desejo de exclusão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038547174/mceclip0.png)

Se informa Não, o reprocessamento não excluirá lançamentos.

Se informar Sim, exibirá uma tela para inserir o filtro com mais detalhes do que será excluído na tabela AKD.  
Clique em Editar e insira as informações do Filtro.

, ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038547334/mceclip1.png)

Se não informar o Filtro a Operação será Cancelada.
