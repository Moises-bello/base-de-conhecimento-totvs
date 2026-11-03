---
article_id: 360051976953
category: ADVPL - Rotina Automática
content_hash: 307a6c3ea80f01a16582d9e07f6f7ee2bad8c42a18b7adc5d8cdfae70a77844f
fetched_at: '2026-06-28T22:40:23.921918+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Apontamentos Pendentes:Tabela
  T4K
type: support-article
updated_at: '2021-12-29T13:29:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051976953-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Apontamentos-Pendentes-Tabela-T4K
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**É possível desabilitar a inserção de dados/utilização da tabela T4K?

**Ambiente**Protheus – ADVPL – A partir da versão P12.

**Solução**A equipe de **SIGAPCP** criou uma nova regra no ExecAuto no processo de produção.  
Agora sempre que o seu ExecAuto retornar um erro, irá gerar a registros na tabela T4k tendo que reprocessar para limpar esse registro.  
Agora caso não queira usar essa tabela, ou seja, não usar essa inovação, basta colocar uma linha a mais no seu ExecAuto().  
**aaAdd(aVetor,{"PENDENTE","1",Nil})**

```
Exemplo do MATA250:   
dData:=dDataBase  
        aVetor := { {"D3_FILIAL"  ,XFILIAL("SD3") ,NIL},;  
                    {"D3_TM"      ,"010"          ,NIL},;  
                    {"D3_OP"      ,"10270901001"  ,NIL},;   
                    {"D3_COD"     ,"12900PA1"     ,NIL},;  
                    {"D3_QUANT"   ,1              ,NIL},;  
                    {"D3_LOCAL"   ,"01"           ,NIL},;  
                    {"D3_EMISSAO" ,dData          ,NIL},;     
                    {"ATUEMP"     , "T"           ,NIL}}     
                        
       aaAdd(aVetor,{"PENDENTE","1",Nil}) //<<------------ passar valor 1  
  
MSExecAuto({|x, y| mata250(x, y)},aVetor, nOpc )
```

**Saiba Mais  
[PCPA138 - Apontamentos Pendentes](https://tdn.totvs.com.br/display/public/PROT/PCPA138+-+Apontamentos+Pendentes)**
