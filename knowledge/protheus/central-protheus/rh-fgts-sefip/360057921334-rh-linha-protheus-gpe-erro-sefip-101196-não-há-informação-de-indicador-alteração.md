---
article_id: 360057921334
category: RH - FGTS / SEFIP
content_hash: 9217d7730f112715bcf7afdccd81d46414487f45e2bde6416329b45eb25fae0e
fetched_at: '2026-06-28T22:43:41.271291+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro SEFIP 101196 - Não há informação de indicador
  alteração CNAE Preponderante quando o recolhimento for exclusivo de FGTS ou para
  competência anterior a 12/2008 ou empresa que não centraliza (centralizadora ou
  centralizada)
type: support-article
updated_at: '2025-08-14T17:37:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057921334-RH-Linha-Protheus-GPE-Erro-SEFIP-101196-N%C3%A3o-h%C3%A1-informa%C3%A7%C3%A3o-de-indicador-altera%C3%A7%C3%A3o-CNAE-Preponderante-quando-o-recolhimento-for-exclusivo-de-FGTS-ou-para-compet%C3%AAncia-anterior-a-12-2008-ou-empresa-que-n%C3%A3o-centraliza-centralizadora-ou-centralizada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185429996439)** Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência**Ao importar o arquivo SEFIP.RE gerado no Protheus, o validador do programa SEFIP apresenta o seguinte erro: 101196 - Não há informação de indicador alteração CNAE Preponderante quando o recolhimento for exclusivo de FGTS ou para competência anterior a 12/2008 ou empresa que não centraliza (centralizadora ou centralizada)”

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse erro ocorre pois nos parâmetros para a geração do arquivo SEFIP.RE, o campo "**Indicador Alt. CNAE?"** esta com a indicação incorreta.  
  
**Solução**

Conforme layout da SEFIP, a empresa deve selecionar através dos parâmetros da SEFIP a opção correta. Veja abaixo;  
  
Opções para gerar o arquivo diferente de "A" ou "P", assim corrigindo o erro apresentado. 

![](https://totvssuporte.zendesk.com/attachments/token/iEMc3iYL5HTMqF6xmUKVZ2Wbu/?name=inline131600410.png)​  
  
  
"S" Altera o CNAE  
"N" Não Alt. CNAE  
"A" Alt. CANE Prep.  
"P" Não Alt. Prep.   
  
![](https://totvssuporte.zendesk.com/attachments/token/VoiSjhk1er2XBAyfpow5Vos8M/?name=inline-81528323.png)​  
  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/e3a1ba4VGVje0cD2Mtnv7UHfu/?name=inline1952751238.png)​

**Saiba mais:    
[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS)**
