---
article_id: 360028474032
category: RH - CNAB
content_hash: 43ee15e0e2c83b7f5021aa2a4b4fac90c217cdba05069027232215a324ff7eea
fetched_at: '2026-06-28T22:43:39.162724+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar a inclusão de Segmento B no layout
  do arquivo CNAB
type: support-article
updated_at: '2025-09-18T19:29:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028474032-RH-Linha-Protheus-GPE-Como-configurar-a-inclus%C3%A3o-de-Segmento-B-no-layout-do-arquivo-CNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32879443667607)** Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como configurar a inclusão de Segmento B no layout do arquivo CNAB?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Esta documentação deverá ser utilizada como apoio para configuração do **Segmento "B"** dentro do l**ayout do Cnab**, incluindo as variáveis/funções que poderão ser utilizadas.

01) Informações para gerar os dados **Tipo de Inscrição do Favorecido** e **N°** **de Inscrição do Favorecido**, conforme layout da FEBRABAN:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029311292)

2) Para o **Segmento B**, a posição **De**: 18, **Até**: 18, com informação de apenas um único dígito, representa o **Tipo de Inscrição do Favorecido**, conforme nos mostra a tabela abaixo:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029311432)  
Esse dígito determina o tipo de inscrição para reconhecimento do favorecido. Ex: '**1**', será utilizado o **CPF**.

3) Para o **Segmento B**, na posição **De**: 19, **Até**: 32, com 14 dígitos, informamos o **N° de Inscrição do Favorecido**.

 **OBS**: Para este campo, alguns modelos não conseguiam gerar o **N° de Inscrição do Favorecido**, pois estavam consultando diretamente o campo **SRA→RA\_CIC**, que é o número de CPF do funcionário.

**Utilizar apenas a variável** "**CCPF**", da seguinte maneira: STRZERO(VAL(CCPF),14) .

**Importante:** O Segmento B, esta implementado apenas para o o **Modelo 2** e **Sispag**. Não há implementação do Segmento B, para o **Modelo 1**.

**Informações complementares:**

* Variáveis que podem ser utilizadas:

**cNome**: Ex: cNome.

**cBanco**: Ex: cBanco.

**cConta**: Ex: "0000"+SUBS(CCONTA,1,9), SUBS(cConta,1,8).

**cCPF:** Ex: STRZERO(VAL(CCPF),14), PADL(CCPF,14,'0').

* Funções que podem ser utilizadas:

**CNABSequencia():**Função para gerar sequência numérica referente ao lote do CNAB da Folha de Pagamento. Ex: CNABSEQUENCIA()  
  
**Saiba Mais**[Artigos CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
