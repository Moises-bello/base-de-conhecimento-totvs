---
article_id: 360056475154
category: RH - Folha de Pagamento
content_hash: dbf68bd53aba23503e6a2d3eb0227f42f9697c151c29f35ccfd66e632f74abd3
fetched_at: '2026-06-28T22:44:11.946040+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Adicionais que incorporam salário não aparecem
  nas alterações salariais do funcionário
type: support-article
updated_at: '2024-09-06T20:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056475154-RH-Linha-Protheus-GPE-Adicionais-que-incorporam-sal%C3%A1rio-n%C3%A3o-aparecem-nas-altera%C3%A7%C3%B5es-salariais-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15308170066327) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**  
Quando realizado alteração salarial de um funcionário que recebe adicional, como periculosidade e insalubridade, o Sistema não apresenta as informações no histórico de alteração salarial e na ficha de registros.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**Para que o adicional recebido pelo funcionário seja apresentado nas alterações salariais e no momento da impressão da Ficha de Registro, ou Ficha de Anotações da CTPS, é necessário que a configuração da verba de adicional esteja configurada para incorporar salário.

Os adicionais que não incorporarem ao salário do funcionário não serão gravados nas tabelas SR3 e SR7 (Histórico de Alterações Salariais), portanto o Sistema não emite nos relatórios.  
  
**Solução**Para que o Sistema apresente os adicionais na rotina de **Histórico de Salário** (**GPEA250**) e na impressão da **Ficha de Registro** (**GPEA260**), verifique as premissas abaixo:  
  
1. O Funcionário possui cadastro do adicional na aba **Adicionais** e vínculo com **Sindicato;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095886674)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095887034)

2. O **Sindicato** atrelado ao funcionário está configurado para cálculo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095887234)  
  
3. A verba correspondente ao adicional possui configuração para **incorporar salário** na aba **Incidências**;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098181353)

**Atenção**O Sistema utiliza como base **o valor do adicional calculado na Folha de Pagamento,** portanto os dados do ajuste do adicional **só será gravado na SR3 e SR7 após o Fechamento do Período que foi realizado reajuste salarial.**

**Somente a gravação da alteração do salário em si é gravado imediatamente.**

**Exemplo**Ajuste salarial por dissídio para funcionário que possui adicional de periculosidade.

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098182833)**

Sistema exibiu a alteração com a verba na rotina de **Histórico Salarial após fechamento** do período.

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
