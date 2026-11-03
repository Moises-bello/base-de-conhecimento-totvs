---
article_id: 10594304396055
category: Folha Mensal
content_hash: dd804de3b38f4457e5c9d87d162bc9e3e973d138f9ab0e6e7a97615e61d51375
fetched_at: '2026-06-28T22:46:58.298225+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Valores FGTS iguais a GFIP emitida pela SEFIP'
type: support-article
updated_at: '2024-09-16T19:17:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10594304396055-RH-RM-FOP-Folha-Anal%C3%ADtica-Valores-FGTS-iguais-a-GFIP-emitida-pela-SEFIP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:17 min  
  
Dúvida**  
Como faço pra gerar a Folha Analítica de forma que os valores de FGTS possam conferir com os valores da GFIP emitida pelo SEFIP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que os valores de FGTS da folha analítica possam conferir com os valores da GFIP emitida pelo SEFIP, o usuário poderá criar as fórmulas abaixo e inserir nos campos de bases de eventos campo 'Fórmula 1' e 'Fórmula 2' da folha analítica. As fórmulas abaixo zeram a base FGTS dos funcionários demitidos no mês, tipo 2 e tipo T e que tiveram o recolhimento através da GRFC.  
  
1. Cadastre as seguinte formulas:  
  
Criar a fórmula :**Base FGTS (GFIP)**SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )  
OU  
( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E  
( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E  
( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )  
ENTAO 0  
SENAO BASEFGTS  
FIMSE  
  
Criar a fórmula :**Base FGTS 13º (GFIP)**SE( (SFUNC = 'D') E ( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) )  
OU  
( (SFUNC = 'A') E( (TABFUNC('RESCISAOCALCULADA' , 'V') = 1) ) E  
( (TABFUNC('TIPODEMISSAO' , 'S') = '2') ou (TABFUNC('TIPODEMISSAO' , 'S') = 'T') ) E  
( (TABFUNC(' FGTSMESANTRECOLGRFP' , 'V') = 1) ) )  
ENTAO 0  
SENAO BSFGTS13  
FIMSE  
  
2. Acesso o processo de geração da folha analítica:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10594063490967)  
  
3. Avançar até "**Dados dos Funcionários**", informe as formulas conforme imagem abaixo:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10594101746071)  
  
4. No arquivo gerado, veja que irá retornar os valores correspondentes:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10594207298967)  
  
**Saiba Mais**  
[Como faço pra gerar a Folha Analítica de forma que os valores de FGTS possam conferir com os valores da GFIP emitida pelo SEFIP?](https://tdn.totvs.com.br/pages/viewpage.action?pageId=146965934)
