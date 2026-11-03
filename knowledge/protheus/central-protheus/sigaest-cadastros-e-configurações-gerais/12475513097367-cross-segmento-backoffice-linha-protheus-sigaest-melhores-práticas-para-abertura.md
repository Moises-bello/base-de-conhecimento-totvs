---
article_id: 12475513097367
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5ab2453ce1b327c1710f8fd773210274e884aea3231f4e074a2d41112c04f41c
fetched_at: '2026-06-28T22:39:09.650378+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Melhores práticas
  para abertura de tickets para um pronto atendimento de ocorrências já mapeadas
type: support-article
updated_at: '2023-03-22T12:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12475513097367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Melhores-pr%C3%A1ticas-para-abertura-de-tickets-para-um-pronto-atendimento-de-ocorr%C3%AAncias-j%C3%A1-mapeadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais são as melhores práticas para abertura de tickets?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões  
  
**Solução**

Para facilitar o entendimento de sua solicitação destacamos algum pontos importantes no momento da abertura do seu ticket.

**Dicas para abertura dos tickets**

**- 1 -** **Título dos tickets -** Na abertura de um ticket sempre incluir o nome da rotina no título:

**Exemplo:** "MATA038 Acompanha Custos"

**- 2 - Descrição do ticket -** Na parte de descrição de sua solicitação insira novamente o código da rotina e detalhe o problema ou dúvida.

**- 3 - Helps das rotinas -**  Para os Helps apresentados em algum processo ou rotina específica. Nesse cenário o mais adequado é **digitar o nome do Help** tanto na descrição do ticket, como no título. É importantíssimo essa informação para agilidade na identificação da ocorrência.

**Exemplo:** ***"Help: MA240NEGAT"*** quando tenta requisitar saldo dos produtos em algum processo ou rotina. Print de exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12477202776215)

**- 4 -** **Error.log -** Quando o problema for relacionado a error.log o mais adequado para o atendimento ser eficiente é: **Incluir um *trecho*** do error.log na descrição do ticket, **(Obs.:** Não precisa ser o error.log completo**).** Também é necessário enviar anexo em um **Bloco de Notas** o error.log completo.

**Exemplo:**

**Título de abertura do ticket:** "Alias does not exist SCGN000012 on REPORTPRINT(MATR241.PRW) 21/07/2022 17:53:57 line : 534"

**Descrição do ticket:**

THREAD ERROR ([189999] TOTVS, DESKTOP-TOTVS) 16/02/2023 11:16:20  
Alias does not exist SCGN000012 on REPORTPRINT(MATR241.PRW) 21/07/2022 17:53:57 line : 534

[TOTVS build: 7.00.210324P-20221216]  
Called from {|OREPORT| REPORTPRINT(OREPORT,AALIAS)}(MATR241.PRW) 21/07/2022 17:53:57 line : 104  
Called from {|| IIF(SELF:INIT(),(LACTION := EVAL(SELF:BACTION,SELF),SELF:FINISH()),LOK:= .F. ),LEND := .T. ,ODLG:END()}(REPORT01.PRW) 13/12/2022 14:23:45 line : 2205  
Called from ::MSDIALOG:ACTIVATE  
Called from TREPORT:PRINT(REPORT01.PRW) 13/12/2022 14:23:45 line : 2218  
Called from TREPORT:PRINTDIALOG(REPORT01.PRW) 13/12/2022 14:23:45 line : 3469  
Called from MATR241(MATR241.PRW) 21/07/2022 17:53:57 line : 44  
Called from \_\_EXECUTE(APLIB090.PRW) 13/12/2022 14:23:45 line : 721  
Called from MDIEXECUTE(APLIB260.PRW) 13/12/2022 14:23:45 line : 924

**Obs.:** Também incluir em um BLOCO DE NOTAS o error.log completo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12478294957847)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
