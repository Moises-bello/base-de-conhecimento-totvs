---
article_id: 23000054827799
category: RH - Provisão
content_hash: b61c0ae289698fda92fd42834464ca0499b1e252637f4d22bc236cf6482cd633
fetched_at: '2026-06-28T22:43:56.742353+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisão de Férias e 13º Salário para Professor
  Aulista
type: support-article
updated_at: '2025-06-17T19:37:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23000054827799-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-para-Professor-Aulista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23000054795031) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como Conferir os Cálculos de Provisão de Férias e 13º Salário para Professor Aulista - Categoria J?  
  
**Ambiente**TOTVS RH – TOTVS RH (Linha Protheus) – Gestão de Pessoal – À Partir do Release 12.  
  
**Solução**Para os Professores Aulistas (Categoria J), a Folha de Pagamento é calculada considerando as aulas variáveis inseridas no Lançamento das Tarefas, portanto não há Salário no cadastro do Funcionário.  
Nos cálculos de Provisão, como não há um Salário Base, a média das aulas serão calculadas como Adicionais de Férias e Adicionais de 13º Salário.

Para mais informações sobre o Cadastro e Cálculo do Professor Aulista [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051143753-RH-Linha-Protheus-GPE-Como-cadastrar-professor-categoria-J).

Para conferir as provisões para o Professor Aulista, realize os seguintes passos:  
  
1. Acesse: Miscelânea / Provisões / Provisões Férias e 13º (GPEA070), Selecione o Professor Aulista, Clique em Visualizar e em Seguida em Médias:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23000054796695)  
  
2. Será emitido um relatório de médias com os valores das Médias das Aulas de Férias e de 13º Salário.

- A primeira página do relatório apresentará todos os fontes, parâmetos e mnemônicos utilizados no cálculo das médias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23004958685079)

- Nas próximas páginas serão apresentados os relatórios com as Médias das Aulas de Férias e 13º Salário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23004958693527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23004958701847)

 A Média de Pagamento é calculada de acordo com a Configuração de Médias aplicada na base, que é composta principalmente pelo Mnemônico P\_MEDDIREN (ou parâmetro MV\_MEDDIRE).

Considerando o exemplo acima, o Mnmeônico P\_MEDDIREN está configirado com N, portanto a regra do cálculo das médias é:

Total Médias / Meses considerados para Média = Média.  
Média / 12 x Avos de Direito = **Média de Pagamento**

**Média de Férias à Vencer** :   
1650,00 / 5 = 330,00  
330 / 12 \* 5 = 137,50  
  
**Média de 13º Salário** :   
1650,00 / 2 = 825,00  
825,00 / 12 \* 2 = 137,50

Para consultar as configurações de Médias [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=224112471)

3. Acesse: Relatórios / Provisões / Provisões de Férias (GPER070) ou Provisões de 13º (GPER090), e preencha as perguntas para emissão do relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23006761465623)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23006798670231)

Veja que como não há Salário no cadastro do Funcionário, a coluna "Valor" não apresentará nenhum cálculo, e as Médias das Horas do Professor serão calculadas na coluna "Adicionais".

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
