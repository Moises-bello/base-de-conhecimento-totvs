---
article_id: 23921962613399
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: 0e4b74e3044df25a535bd087a16f8ea56e510e734f74d2a180a6684ef5fb7497
fetched_at: '2026-06-28T22:37:47.977983+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA200 - Como faz
  para baixar via CNAB a receber um registro que tenha valores de "Outros Créditos"?
type: support-article
updated_at: '2026-03-25T19:42:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23921962613399-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA200-Como-faz-para-baixar-via-CNAB-a-receber-um-registro-que-tenha-valores-de-Outros-Cr%C3%A9ditos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23921962578071) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
FINA200 - Como faz para baixar via CNAB a receber um registro que tenha valores de "Outros Créditos"?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões.

**Cenário:**

Tenho um título a receber, em que o valor original do título é de R$ 5.500,00.

E o banco está retornando no arquivo de retorno do banco a receber, um valor de R$ 100,00 como "Outros Crédito"

Ao emitir o "FINR650 - Relatório de retorno CNAB", é possível visualizar todas essas informações.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/23921933791127)](https://centraldeatendimento.totvs.com/hc/article_attachments/23921933791127)

**Solução**  
Para o sistema entender o valor que está na coluna "**Outros Créditos**" e efetuar a baixa total do título, é necessário que a posição "**Valor Recebido**" não seja composta pelo valor da coluna "Outros Créditos".

No exemplo da imagem, em que a coluna "**Valor Recebido**" possui o conteúdo R$ 5.500,00, está correto, e o sistema irá baixar o título total.

Caso a coluna "**Valor Recebido**" tivesse o valor de R$ 5.600 (compondo o valor dos outros créditos), desta forma o sistema não iria conseguir baixar o título, apresentando erro.
