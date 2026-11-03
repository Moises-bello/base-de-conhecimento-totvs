---
article_id: 16598748695703
category: SIGAACD - Automação e Coleta de Dados
content_hash: adf29a7ecb4e74997b1fe4072c514d32c8de95453ad0ee7dfd5ab586d022c168
fetched_at: '2026-06-28T22:39:11.173644+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA030 - Mestre de
  Inventário - Legenda / Status da rotina
type: support-article
updated_at: '2023-08-08T11:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16598748695703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA030-Mestre-de-Invent%C3%A1rio-Legenda-Status-da-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16598705457175) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais campos atualizam a legenda da rotina ***MESTRE DE INVENTÁRIO (ACDA030)***?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16598952984087)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Na rotina ***MESTRE DE INVENTÁRIO (ACDA030)*** as legendas são compostas da seguinte forma, através do campo ***CBA\_STATUS***:  
  
aCores := {      
**{ "CBA->CBA\_STATUS == '0'", "BR\_VERDE"},;**  
**{ "CBA->CBA\_STATUS == '1'", "BR\_AMARELO"},;**  
**{ "CBA->CBA\_STATUS == '2'", "BR\_CINZA"},;**  
**{ "CBA->CBA\_STATUS == '3'", "BR\_LARANJA"},;**  
**{ "CBA->CBA\_STATUS == '4'", "BR\_AZUL"},;**  
**{ "CBA->CBA\_STATUS == '7'", "BR\_BRANCO"},;**  
**{ "CBA->CBA\_STATUS == '5'", "BR\_VERMELHO"},;**  
**{ "CBA->CBA\_STATUS == '6'", "BR\_PRETO"} }**  
  
aCorDesc := {      
**{"BR\_VERDE",    STR0011},; //"Nao Iniciado"**  
**{"BR\_AMARELO",    STR0012},; //"Em Andamento"**  
**{"BR\_CINZA",    STR0044},; //"Em Pausa"**  
**{"BR\_LARANJA",    STR0045},; //"Contado"**  
**{"BR\_AZUL",  STR0013},; //"Finalizado"**  
**{"BR\_BRANCO",    STR0113},; //Parcialmente Processado**  
**{"BR\_VERMELHO",    STR0014},; //"Processado"**  
**{"BR\_PRETO",  STR0112} } //"Endereco Sem Saldo"**

V**eja também no link abaixo as instruções da rotina ACDA030.**

**<https://tdn.totvs.com/pages/viewpage.action?pageId=450148951>**

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
