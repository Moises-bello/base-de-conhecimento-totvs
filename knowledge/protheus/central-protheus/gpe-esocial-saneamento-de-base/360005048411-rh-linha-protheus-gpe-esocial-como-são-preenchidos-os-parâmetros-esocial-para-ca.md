---
article_id: 360005048411
category: GPE - eSocial - Saneamento de Base
content_hash: bc7862ad659e7b8cfa31dabb25a0833075b6dabc6f85f8ba8b1ccb42e70fd561
fetched_at: '2026-06-28T22:45:01.628881+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como são preenchidos os parâmetros eSocial
  para cada grupo de empresas conforme cronograma do governo
type: support-article
updated_at: '2023-11-30T20:17:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048411-RH-Linha-Protheus-GPE-eSocial-Como-s%C3%A3o-preenchidos-os-par%C3%A2metros-eSocial-para-cada-grupo-de-empresas-conforme-cronograma-do-governo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19461844999319)**Tempo aproximado para leitura: 00:**02:00 min  
  
Dúvida**Como são preenchidos os parâmetros eSocial para cada grupo de empresas conforme cronograma do governo  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**As informações de data dos parâmetros são definidas conforme o cronograma do governo, é de responsabilidade do empregador verificar qual grupo de empresa faz parte para que realize o preenchimento correto das informações.  
Link Cronograma: [Cronograma Governo](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)

**Parâmetros Protheus**

* **1º GRUPO** -  Empresas com faturamento superior a **R$78 milhões**.  
  MV\_RHTAF = .T.  
  MV\_FASESOC = 2  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = 20180101 (Inicio Tabelas Inicias)  
  MV\_TAFININ = 20180301 (Inicio Não Periódicos)  
  MV\_DTCGINI = 01/03/2018 (Inicio Não Periódicos)

* **2º GRUPO** -  Empresas com faturamento inferior a **R$78 milhões**, exceto as optantes pelo **SIMPLES**.  
  MV\_RHTAF = .T.  
  MV\_FASESOC = 2  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = 20180701 (Inicio Tabelas Inicias)  
  MV\_TAFININ = 20181010 (Inicio Não Periódicos)  
  MV\_DTCGINI = 10/10/2018 (Inicio Não Periódicos)

* **3º GRUPO**  - **ME e EPP** optantes pelo **SIMPLES, MEI**, empregadores pessoas físicas  
  (exceto doméstico), produtor rural PF e entidades sem fins lucrativos  
  MV\_RHTAF = .T.  
  MV\_FASESOC = 2  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = 20190101 (Inicio Tabelas Inicias)  
  MV\_TAFININ = 20190410 (Inicio Não Periódicos)  
  MV\_DTCGINI = 10/04/2019 (Inicio Não Periódicos)
* Para o **4º GRUPO** órgãos públicos e organizações internacionais:  
  MV\_RHTAF = .T.  
  MV\_FASESOC = 2  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = 20210701 (Inicio Tabelas Inicias)  
  MV\_TAFININ = 20211122 (Inicio Não Periódicos)  
  MV\_DTCGINI = 22/11/2021 (Inicio Não Periódicos)

**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[Cronograma oficial eSocial](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
