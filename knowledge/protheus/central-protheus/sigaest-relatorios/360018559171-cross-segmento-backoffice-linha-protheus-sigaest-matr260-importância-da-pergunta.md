---
article_id: 360018559171
category: SIGAEST - RELATORIOS
content_hash: 87596a4753d7e2adbc9c0583f125a54b15360d7ed724774401689a37a3b147f7
fetched_at: '2026-06-28T22:39:05.958090+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST  - MATR260 - Importância
  da pergunta "Saldo do produto a considerar?" para correta emissão do relatório
type: support-article
updated_at: '2026-03-30T12:02:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio
---

No relatório MATR260 a pergunta "Saldo do produto a considerar?" contém três valores:

Atual (saldo e valor da tabela SB2, desconsidera a data de referência),

Por fechamento (quantidade e valor dos campos B2\_QFIM e B2\_VFIM1, também desconsidera a data, pois considera a Data de Referência do Último processamento do Custo Médio) e

Movimento (considera a data, usa função Calcest para calcular saldo e valor com base em movimentações). A parametrização depende do parâmetro MV\_CUSFIL para filtrar por armazém, empresa ou filial.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39230984954135) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

O que quer dizer cada opção na pergunta “Saldo do produto a considerar? ”, do relatório “Relação da Posição de Estoque (MATR260)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Esta pergunta possui três respostas possíveis e trataremos cada uma individualmente para entendermos o seu conceito.

Antes de adentrarmos às perguntas, um ponto importante é o parâmetro **MV\_CUSFIL**. Dependendo de como este parâmetro estiver preenchido, os parâmetros do relatório precisam mudar para cada caso.

**MV\_CUSFIL = A**

Neste caso devemos preencher o parâmetro “Aglutina por? = Armazém" e informar o(s) armazém(ns) que se deseja filtrar conforme imagem abaixo.

![MATR260_PAR1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013894652)

**MV\_CUSFIL = E**

Quando o custo é apurado por empresa devemos preencher o parâmetro “Aglutina por? = Empresa” e ao invés de informar o armazém devemos colocar os carácteres “##” no local do armazém conforme imagem abaixo.

![MATR260_PAR2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013910431)

**MV\_CUSFIL = F**

Neste caso utilizamos o parâmetro “Aglutina por? = Filial” e os parâmetros “De armazém?” e “Até Armazém?” com os caracteres “\*\*”, veja a imagem abaixo.

![MATR260_PAR3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013910591)

**Entendendo a pergunta "Saldo do Produto a Considerar?"**

Abaixo veremos a parametrização padrão para o relatório e posteriormente iremos imprimir o relatório com o parâmetro “Saldo do produto a considerar? ”, das três formas possíveis para uma melhor compreensão.

![PARAM_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013910691)

![PARAM_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013895712)

![PARAM_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013895752)

## 

Atual

O parâmetro “Saldo do produto a considerar?  = Atual”, é a quantidade e valor que se encontra na tabela SB2 campos B2\_VATU1 e B2\_QATU ou seja, se a tabela SB2 estiver errada os valores estarão errados.

Agora vamos imprimir o relatório MATR260, veja na imagem abaixo que o saldo da tabela SB2 e o relatório MATR260 estão corretos.

**Observação**: Considerando o saldo "Atual", o relatório desconsidera a data informada no parâmetro “Data de referência? ”.

![MATR260_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013911771)

![MATR260_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013895852)

## 

## Por fechamento

Agora vamos emitir o relatório MATR260 por fechamento, neste caso o relatório irá imprimir a quantidade e valor, respectivamente, dos campos B2\_QFIM e B2\_VFIM1, conforme imagem abaixo.

**Observação**: Considerando o saldo por "Fechamento", o relatório desconsidera a data informada no parâmetro “Data de referência? ”.

![MATR260_FEC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013895912)

![MATR260_FEC2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013911891)

## Saldo por Movimento

Quando usamos o parâmetro “Saldo do produto a considerar?  = Movimento ”, devemos também preencher o parâmetro “Data de referência? ”, onde informamos a data que desejamos buscar conforme imagem abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000329961)

Neste caso o relatório utiliza a função "**Calcest**", função contida na rotina "**MATXFUNB**" e também a Stored Procedure 14 para realizar a busca e apresentar as informações, pegando inicialmente o saldo e valor da tabela SB9 e calculando as movimentações que ocorreram no período (SD1, SD2 e SD3) para calcular a quantidade e valor a serem mostrados no relatório.

A validação do SALDO DISPONIVEL pode tambem depender do uso sob o parametro MV\_TPSALDO

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO)

**Sobre o saldo empenhado:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - colunas EMPENHO PARA REQ/PV/RESERVA e VALOR EMPENHADO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15112669075223)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)

[Smart View - Posição de Estoque](https://tdn.totvs.com/x/g48WLQ%20)

[Smart View - Estoque (Consultas)](https://tdn.totvs.com/x/M8LrL)
