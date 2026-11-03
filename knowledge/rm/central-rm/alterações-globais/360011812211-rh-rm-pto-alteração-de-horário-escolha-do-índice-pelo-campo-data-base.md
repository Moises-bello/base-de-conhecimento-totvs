---
article_id: 360011812211
category: Alterações Globais
content_hash: 05d55e4eaa036fb2cc5cc4eba7fc49ce7548624e59f7b683c54904c118e257ac
fetched_at: '2026-06-28T22:46:27.084163+00:00'
product: rm
section_id: 6045417448343
source: central-rm
title: RH - RM - PTO - Alteração de Horário - escolha do índice pelo campo data base
type: support-article
updated_at: '2025-09-12T14:03:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011812211-RH-RM-PTO-Altera%C3%A7%C3%A3o-de-Hor%C3%A1rio-escolha-do-%C3%ADndice-pelo-campo-data-base
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409113750039) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como saber qual índice que deve ser selecionado ao alterar um horário?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as Versões

**Solução**

Para saber qual **índice/letra** deve ser selecionado no campo **Índice do horário/Data base** ao realizar a troca de horário. Devemos avaliar no cadastro do horário, o índice cadastrado como descanso até índice do dia da data-base. E este será o índice a ser associado ao funcionário.

Observação: A contagem do índice deve ocorrer sempre de cima para baixo.

Vamos avaliar a estrutura do horário abaixo:

Na criação do horário foi definido que a data base inicia em uma **segunda-feira**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22317730450327)

Na estrutura da jornada identificamos que o índice que corresponde ao descanso é o 7.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22321137340439)  
  
Exemplo 1:

Período do ponto 01/01/2023 a 31/01/2023

1) Considerando o horário acima, suponhamos que o descanso do funcionário, deva ser em uma sexta-feira e a troca do horário é para o dia 01/01/2023, o índice que deverá a ser informado no campo **Índice do horário/Data base** é o índice 3 para que no horário o descanso caia sempre na sexta-feira e assim a data-base vai ser na segunda-feira.    
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22317730474519)

2) Considerando o horário acima, suponhamos que o descanso seja em uma quarta-feira e a troca do horário é para o dia 01/01/2023, índice que deverá ser associado é o índice 5 para que no horário o descanso caia sempre na quarta-feira.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22317736059031)

Exemplo 2:

1) Período do ponto 01/01/2023 a 31/01/2023 e Data base do horário: 04/01/2023 (quarta-feira)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22317730508695)  
  
2) Na estrutura da jornada identificamos que o índice que corresponde ao descanso é o 7.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22321301766295)

3) O funcionário descansa toda sexta-feira ao avaliarmos a jornada do horário descobrimos que o índice que corresponde ao descanso é o número 7 e a troca do horário é para o dia 01/01/2023. Ao fazer a contagem do índice de cima para baixo, contando a partir do índice 7 descanso, identificamos o índice que representa a da data base do horário, é o 5. Dessa forma para este funcionário descansar na sexta-feira, temos que associar letra ao índice 5 que é uma quarta-feira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22317730515735)

4) Considerando o horário acima, suponhamos que o descanso seja em um domingo o índice que deverá ser associado é o índice 3 para que no horário o descanso caia sempre no domingo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22320791732759)

**Saiba mais**

Para realizar alteração de horário global acesse o link: [Alteração global de escala de horário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000289207-RM-PTO-Como-realizar-altera%C3%A7%C3%A3o-global-de-escala-de-hor%C3%A1rio)
