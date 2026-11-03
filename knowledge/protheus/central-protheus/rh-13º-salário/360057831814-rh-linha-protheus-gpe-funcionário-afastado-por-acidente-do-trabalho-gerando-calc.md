---
article_id: 360057831814
category: RH - 13º salário
content_hash: 05a86fc7019d8559512319b806ca23e5a5893d68f9786b99a30e539487545c79
fetched_at: '2026-06-28T22:44:00.804014+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionário afastado por acidente do trabalho gerando
  calculo de 13º indevido
type: support-article
updated_at: '2025-08-13T11:13:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057831814-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-afastado-por-acidente-do-trabalho-gerando-calculo-de-13%C2%BA-indevido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19192901987351) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**O que analisar quando está gerando cálculo de 13º salário indevidamente para funcionário Afastado por Acidente de Trabalho?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Existem funcionários com afastamentos por acidente do trabalho e está sendo gerado valores de 13º tanto de primeira parcela quanto segunda parcela.  
Devemos analisar se o identificador de cálculo **1730 - Afastamento por acidente pago pela Previdência 13º** está criado como **Provento** erroneamente.

Para esse identificador de cálculo deve ser criada uma verba de base, que irá conter a remuneração dos dias do afastamento por acidente de trabalho pago pela previdência referente a 13º salário.  
Dessa maneira, se criado como um Provento irá gerar indevidamente valores para serem pagos de 13º.

Para **correção**, deve-se retirar o identificador de cálculo da verba criada como Provento e criar uma nova verba de **Base** **Provento** atribuindo o ID 1730.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34147301218711)

**Saiba Mais**[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=525824950)[RH - Linha Protheus - GPE - Como Conferir a Base de FGTS 13º Salário 1° e 2ª Parcela de funcionários Afastados por Acidente de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020659431-RH-Linha-Protheus-GPE-Como-Conferir-a-Base-de-FGTS-13%C2%BA-Sal%C3%A1rio-1-e-2%C2%AA-Parcela-de-funcion%C3%A1rios-Afastados-por-Acidente-de-Trabalho)
