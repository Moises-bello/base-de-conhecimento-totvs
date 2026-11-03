---
article_id: 360016304872
category: BI - Business Intelligence - Crystal-Reports
content_hash: 5b0760ca2df963973422bc92e795e82010c6e568bb8316248490b9156a307d7d
fetched_at: '2026-06-28T22:40:29.055666+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - CRYS - Chamando a tela de
  parâmetros duas vezes na integração do Crystal com Protheus
type: support-article
updated_at: '2022-07-27T18:30:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016304872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-CRYS-Chamando-a-tela-de-par%C3%A2metros-duas-vezes-na-integra%C3%A7%C3%A3o-do-Crystal-com-Protheus
---

**Dúvida**Como retirar a reabertura da tela de Parâmetros na Integração do *Crystal* com Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – *Crystal*– A partir da versão 11.80  
  
**Solução**Para que a tela de parâmetros não abra duas vezes, ou seja, a abertura dos parâmetros do **Protheus** e posteriormente a do **Crystal**, deverá validar os seguintes itens:  
1. Validar se o nome do Pergunta (SX1) está com o mesmo nome do relatório aberto;  
2. Verificar se existe o arquivo **crwini** dentro na mesma pasta do **crysini** ( outro arquivo de configuração do *Crystal*);  
2.1  Exemplo do Arquivo:

```
[sxs]  
Sx1=1   
Sx2=2
```

**Importante**A localidade dos arquivos de configuração variam de acordo com o tipo de geração, sendo local na pasta **SmartClient** e via servidor na pasta **Appserver.****Saiba mais**Documentação completa da Integração Crystal x Protheus  
[Help Crystal](https://cms.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/crystal.htm)
