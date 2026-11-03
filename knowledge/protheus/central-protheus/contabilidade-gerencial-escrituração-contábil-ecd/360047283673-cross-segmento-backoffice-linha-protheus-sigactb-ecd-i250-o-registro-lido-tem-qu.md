---
article_id: 360047283673
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2dec30c6067ef1e420f00a8e22bceaff7fe7c5686c92d5aa769fb0f3a4481aec
fetched_at: '2026-06-28T22:40:44.365895+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD I250 O REGISTRO LIDO
  TEM QUANTIDADE DE CAMPOS DIFERENTE DO ESPECIFICADO NO LAYOUT
type: support-article
updated_at: '2026-05-15T13:43:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047283673-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I250-O-REGISTRO-LIDO-TEM-QUANTIDADE-DE-CAMPOS-DIFERENTE-DO-ESPECIFICADO-NO-LAYOUT
---

O erro ocorre porque o registro gerado contém 10 campos, enquanto o PVA espera 9, devido à presença de caracteres especiais ou espaços em branco no histórico do lançamento contábil. Para corrigir, deve-se acessar o lançamento e remover esses caracteres especiais.

**Dúvida**

**O registro lido tem quantidade de campos diferente do especificado no layout**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068060893)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068061833)  
  
**Ambiente**

Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

O PVA espera que seja gerado 9 Campos   
  
![](https://totvssuporte.zendesk.com/attachments/token/kkK3DCoPmcsA7U2EYxlYUH8DK/?name=inline1271433209.png)

Esta sendo gerado 10 campos   
  
Campo 01 – Tipo de Registro: I250   
Campo 02 – Código da Conta Analítica Debitada/Creditada: 111020001  
Campo 03 – Código do Centro de Custos: não há.   
Campo 04 – Valor da Partida: 521744,38 (corresponde a 521744,38)   
Campo 05 – Indicador da Natureza da Partida: C (Credito)   
Campo 06 – Número, Código ou Caminho de Localização dos Documentos Arquivados: 0120180522008850001000001133097C0110101  
Campo 07 – Código do Histórico Padronizado: não há.   
Campo 08 – Histórico Completo da Partida ou Histórico Complementar: TRANSF BANCARIA ORIGEM -22/05/2018-Refer ente a OP: 3846794  
Campo 09 – Código de Identificação do Participante (Registro 0150): ***|***Doc: 347238600  
Campo 10 - não há.

![](https://totvssuporte.zendesk.com/attachments/token/IEujzE3igpIPfGqnrrQS6OlzU/?name=inline892751938.png)​  
  
Situação esta sendo apresentada pois existe um "***| "*** e o Espaço em branco em no histórico do lançamento  
  
Erro apresentado no validador esta sendo ocasionado devido algum conteúdo no histórico do lançamento contábil "algum carácter especial" ,"/","%", "Espaço em branco" ,"-" , ":".

Para corrigir o erro acesse a o lançamento contábil e excluir o carácter especial , para mais detalhes [CARÁCTER ESPECIAL NO HISTÓRICO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047562333-MP-SIGACTB-ECD-ECF-CAR%C3%81CTER-ESPECIAL-NO-HIST%C3%93RICO-?source=search)

Saiba mais:

[ECD0039\_USO\_DE\_HISTORICOS\_PADRONIZADOS\_NA\_ECD\_REGISTRO\_I075](https://tdn.totvs.com/pages/releaseview.action?pageId=619765270)
