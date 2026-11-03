---
article_id: 14653916150295
category: MDT - eSocial
content_hash: b21d76b5b2b312b7061a850ac615a5f7bf293d1719a7dec56d48bb0342303587
fetched_at: '2026-06-28T22:44:29.304278+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - Como saber se um campo do eSocial é obrigatório
  para os eventos SST
type: support-article
updated_at: '2025-08-04T12:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14653916150295-RH-Linha-Protheus-MDT-Como-saber-se-um-campo-do-eSocial-%C3%A9-obrigat%C3%B3rio-para-os-eventos-SST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como saber se um campo do eSocial é obrigatório para os eventos SST?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Na página Oficial do eSocial (<https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>) em que ele mostra as versões do *layout*, cada evento é apresentado de forma a visualizar cada um dos campos que o compõem.

Uma das colunas encontradas no layout é a de **Ocorrência (Ocor).**

Considere o seguinte: Quando a primeira posição for 1, aquele campo é obrigatório, mas quando for 0 (zero) o campo é não obrigatório.

Exemplo **1-1 (Obrigatório), 0-1 (Não Obrigatório)**.

Os indicativos desta coluna são compostos por um ou dois numerais separados entre si por um hífen.

Um único número indica somente a quantidade mínima de caracteres a serem preenchidos naquele campo, portanto, obrigatório.

Quando a coluna demonstrar dois números, separados por hífen, o numeral da esquerda indica a quantidade mínima de registros e o numeral da direita, a quantidade máxima.

Se a quantidade mínima é zero, o empregador/contribuinte somente deverá prestar informação se, de fato, ela existir, caso contrário nada deverá ser informado. Se o numeral da direita indicar um valor entre 1 e 99, o limite máximo de registros de informações será 99.

Seguem alguns exemplos:

• **0-1**: campo não obrigatório ou com no máximo um registro;  
• **1**: significa que deve conter no mínimo um (portanto é obrigatório) e no máximo um registro;  
• **1-99**: deve existir no mínimo um (portanto é obrigatório) e no máximo noventa e nove registros;  
• **0-999**: campo não obrigatório com o máximo de 999 registros.  
  
Verifique o exemplo:

Este é o evento **S-2210 - Comunicação de Acidente de Trabalho**.

O campo **localAcidente** está preenchido com "1" na coluna Ocorrência, logo é um campo obrigatório e deve ser preenchido com as opções válidas e apresentadas na coluna "**Condição**".

Já o campo **ideLocalAcid,**está preenchido 0-1, indicando que o campo é facultativo, mas se preenchido, deverá também utilizar uma das opções válidas e apresentadas na coluna "**Condição**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14654367714199)  
  
**Observação**: Caso tenha dúvidas no entendimento da obrigatoriedade de cada campo do *Layout*, é necessário que entre em contato com **Suporte do Governo** para orientações.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
