---
article_id: 360004980892
category: GPE - eSocial - Saneamento de Base
content_hash: 030ca45b71c1b133954d0ac933373990cd11c50c3930a854d7cf6c8cd0b365af
fetched_at: '2026-06-28T22:45:01.526312+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Parâmetros 2ª Fase esocial (Não Periódicos)
type: support-article
updated_at: '2024-09-19T14:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980892-RH-Linha-Protheus-GPE-eSocial-Par%C3%A2metros-2%C2%AA-Fase-esocial-N%C3%A3o-Peri%C3%B3dicos
---

**Dúvida**Quais são os Parâmetros 2ª Fase esocial (Não Periódicos)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**As informações de data dos parâmetros são definidas conforme o cronograma atual do governo, é de responsabilidade do empregador verificar se existe alteração no cronograma e ajustar os parâmetros.  
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
  MV\_TAFINIE = 20180701 (Inicio Tabelas Inicias)  
  MV\_TAFININ = 20181010 (Inicio Não Periódicos)  
  MV\_DTCGINI = 10/10/2018 (Inicio Não Periódicos)

* **3º GRUPO**  - **ME e EPP** optantes pelo **SIMPLES, MEI**, empregadores pessoas físicas (exceto domésticos), entidades sem fins lucrativos.  
    
  **Eventos de tabela** e **não periódicos** - já implantados  
  MV\_RHTAF = .T.  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = (Preencher com Inicio Tabelas Inicias)  Ex: **20190101**MV\_TAFININ = (Preencher Inicio Não Periódicos) Ex: **20190410**MV\_DTCGINI = (Preencher com Inicio Não Periódicos) Ex: **10/04/2019****Eventos Periódicos (folha de pagamento) - S-1200 a S-1299**MV\_FASESOC = 2 (Preencher o parâmetro com **2** quando chegar a data de inicio de eventos periódicos de acordo com o cronograma do governo, caso ao contrario deixar com **1**)  
  [Clique aqui para acessar o Cronograma Governo](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)

* Para o **4º GRUPO,  5º GRUPO e 6º GRUPO.**  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = (Preencher com Inicio Tabelas Inicias de acordo com o cronograma do governo)  Ex: **20190101**  
  MV\_TAFININ = (Preencher com Inicio Não Periódicos de acordo com o cronograma do governo) Ex: **20190410**  
  MV\_DTCGINI = (Preencher com Inicio Não Periódicos de acordo com o cronograma do governo) Ex: **10/04/2019**  
  MV\_RHTAF = .T. (Preencher o parâmetro com .T. quando entrar não fase de entrega de eventos de acordo com o cronograma do governo)  
  MV\_FASESOC = (Preencher com **0** na fase de eventos de tabelas, **1** fase de eventos não periódicos, **2** fase de eventos periódicos de acordo com o cronograma do governo)  
  [Clique aqui para acessar o Cronograma Governo](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)
* Transmissão para Ambiente de **Pré Produção** do Governo (teste)  
  MV\_RHTAF = .T.  
  MV\_FASESOC = 2  
  MV\_EFDMSG = .T.  
  MV\_TAFINIE = 20170101 (Inicio Tabelas Inicias)   
  MV\_TAFININ = 20170301 (Inicio Não Periódicos)  
  MV\_DTCGINI = 01/03/2017 (Inicio Não Periódicos)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
