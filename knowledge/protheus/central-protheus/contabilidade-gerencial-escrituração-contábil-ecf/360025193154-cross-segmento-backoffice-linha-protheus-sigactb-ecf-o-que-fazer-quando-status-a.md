---
article_id: 360025193154
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: c767234ae2378883bfcc822b87ecd0be7c5dfbaa49b73dafbb39427f0ddd4e8a
fetched_at: '2026-06-28T22:40:47.747938+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - O que fazer quando
  STATUS a Tabela TAFST1 permanece 1 e não integra os dados para a TAFST2
type: support-article
updated_at: '2023-07-03T12:01:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025193154-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-O-que-fazer-quando-STATUS-a-Tabela-TAFST1-permanece-1-e-n%C3%A3o-integra-os-dados-para-a-TAFST2
---

**Dúvida**

* O que fazer quando STATUS a Tabela TAFST1 permanece 1 e não integra os dados para a TAFST2?  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039694933)
* O que fazer quando a Tabela TAFST2 não são Alimentado ou Recriadas

**Ambiente**Microsiga Protheus – Contabilidade  – A partir da versão 11.80.  
  
**Solução**

**1º Passo** : Verifique os parâmetros do TAF e o cadastro de complemento de empresa:

* [Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-?source=search)

**2º Passo** : Realize o procedimento a baixo primeiramente **em ambiente de testes**, para validação:

* Aplique a [Atualização TAF Completo.](https://tdn.totvs.com/pages/viewpage.action?pageId=374311673)
* Crie o parâmetro (tipo numérico)  de acordo com a documentação
* Alterado rotinas de processamento para utilizar a Clausula de Limitação de Registros somente quando o parâmetro MV\_TAFQPRC estiver configurado com um número maior que 0, consequentemente para inibição da Cláusula deve-se preencher o parâmetro com 0.
* Deve ser configurado 0 ou 9999999 , se estiver configurado com 1 o sistema só irá integrar um registro na TAFST1 , se estive com 0 o sistema irá inibir a clausula de limitação

**3º Passo** - Realize uma nova integração do Rotina de "Escrituração Contábil(CTBS001)" para o TAF.

**Saiba Mais**

[ECF - Pré Requisitos para gerar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-)
