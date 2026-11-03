---
article_id: 16869771776151
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 59d3b80db9012e4b6cfbd640e67a170da3bf316b0a84e6a2dd749e9e06137c56
fetched_at: '2026-06-28T22:36:56.562437+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro ao transmitir
  a DUE
type: support-article
updated_at: '2023-08-18T19:06:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16869771776151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-ao-transmitir-a-DUE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16869779250199) Tempo aproximado para leitura: **03:00 min** **Dúvida**Ao tentar transmitir a DUE dentro do Embarque do SIGAEEC, a rotina retorna a mensagem "**Não foi possível encontrar o arquivo de retorno do pacote DUE. Tente novamente.**"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16868941569943)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Inicialmente pedimos por gentileza que valide o correto caminho do executável do JAVA utilizado na máquina local:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16869193765911)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16869227207447)**

Após tal ação, sempre utilizar o último arquivo integrador, disponibilizado dentro do **Pacote Acumulado do COMEX** contido na pasta "**config**". Importante ressaltar que tal arquivo deverá estar dentro da Pasta do *SmartClient* local.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16869425583767)  
  
Reforçamos que para a utilização da integração da DUE é necessário a instalação/atualização da versão do JAVA. Recomendamos a utilização da versão 11 do "***Amazon Correto***", distribuição gratuita do "OpenJDK", disponível em: **[Amazon Corretto 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html)  
  
Saiba mais: [DT DTRADE-8996 Nova versão do integrador DUE para o módulo Easy Export Control](https://tdn.totvs.com/pages/releaseview.action?pageId=754616979)  
                     [Pacote Acumulado COMEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)**
