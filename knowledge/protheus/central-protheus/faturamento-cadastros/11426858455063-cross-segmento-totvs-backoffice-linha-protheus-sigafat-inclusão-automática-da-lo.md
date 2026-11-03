---
article_id: 11426858455063
category: Faturamento - Cadastros
content_hash: 3f2d896b9018a9e307674d3e47839b337f9041bfe65989b0bc81ed97d8775157
fetched_at: '2026-06-28T22:38:36.591373+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão automática
  da Loja no cadastro do Cliente
type: support-article
updated_at: '2023-01-04T11:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11426858455063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-autom%C3%A1tica-da-Loja-no-cadastro-do-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Preenchimento automático do campo A1\_LOJA ao incluir um novo cliente na rotina CRMA980  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Tanto o código sequencial do cadastro do cliente quanto a loja não possuem preenchimento automático no padrão do Protheus  
  
Para que a numeração sequencial do código seja automática na inclusão do cadastro, basta colocar no SX3 (inicializador padrão) GetSx8Num("SA1","A1\_COD").   
  
Abaixo link das documentações detalhadas

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Numeração automática incorreta nas Tabelas do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000582027-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Numera%C3%A7%C3%A3o-autom%C3%A1tica-incorreta-nas-Tabelas-do-Protheus?source=search)  
  
https://tdn.totvs.com/x/P4YKDg  
  
Para o campo de loja, neste caso, será necessário usar o Ponto de Entrada **CriaSXE - Controle de Numeração** ou deixar um valor fixo no inicializador padrão do campo  
  
Link documentação do Ponto de Entrada  
  
<https://tdn.totvs.com/x/y-1n>  
  
Abaixo exemplo de inicializador padrão  
  
![](https://totvssuporte.zendesk.com/attachments/token/JTXur5FpYIDso4toWq2Cab08C/?name=image.png)
