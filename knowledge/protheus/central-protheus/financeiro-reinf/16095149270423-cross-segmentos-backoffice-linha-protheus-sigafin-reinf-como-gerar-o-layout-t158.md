---
article_id: 16095149270423
category: Financeiro - Reinf
content_hash: 6cc8cd38d78a1cc730c5b99b0d884663e0e18cc6114bce68d83504d51899125d
fetched_at: '2026-06-28T22:37:51.804652+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como gerar
  o layout T158 REINF
type: support-article
updated_at: '2024-05-23T20:00:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16095149270423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-gerar-o-layout-T158-REINF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16095108181911) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o layout T158 REINF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**Para solucionar essa ocorrência, validar os seguintes passos:

1. Primeiro valide se foi informado na NF a natureza de rendimento no modulo de **Compras,** posicione no item, clique em**Outras Ações**, selecione a opção **"Nat. Rendimento".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16862322416791)**  
Se é um titulo avulso direto pelo modulo Financeiro, na inclusão do titulo clique em: "**Outras Ações** > **Complemento do titulo**"

![](https://tdn.totvs.com/download/attachments/736180686/image2023-1-27_17-40-44.png?version=1&modificationDate=1674852044527&api=v2)

Na aba **Complemento Titulo > REINF**, no campo "**Natur. Rend**." (**FKF\_NATREN**):

![](https://tdn.totvs.com/download/attachments/736180686/image2023-1-27_11-40-56.png?version=1&modificationDate=1674844441370&api=v2)

2. Após a validação acima, realize a baixa do titulo principal com um motivo de baixa que **movimenta banco,** exemplo o Motivo de Baixa "**Debito CC**";  
  
**Obs.** O layout **T158** é gerado após a baixa do título principal (exemplo: título do tipo **NF, DP, BOL**, etc.). O Extrator Fiscal irá considerar como fato gerador do **PIS**, **COFINS** e **CSLL** o pagamento do título principal através do campo **FK2\_DATA**.

3. No extrator Fiscal processar o período realizado a baixa do título principal.   
  
4. Valide se o ambiente está com o fonte FINA989 na data igual ou superior **06/09/2023** e o **FINXREINF 17/08/2023** caso não esteja realizar aplicação do patch e realizar um novo processamento no extrator Fiscal.  
  
12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1119309> ;   
12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1119311> ;   
12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1119310> ;

Obs. Valida se os campos do título principal **FKF\_REINF** e o **FK2\_REINF** ambos com o conteúdo = 2, para assim realizar um novo processamento do **extrator fiscal**. 

**ATENÇÃO AO PASSO 5 (COMPARTILHAMENTO DAS TABELAS)**

**AVALIAR TODAS AS TABELAS SERÁ FUNDAMENTAL PARA EFICÁCIA DO PROCESSO**

5. Valide os compartilhamentos das tabelas (TODAS PRECISAM ESTAR COM MESMO MODO DE COMPARTILHAMENTO)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19667209283735)

Avaliar também as tabelas

* Tabela FK0 : Definir com o mesmo status da SE5
* Tabela FKF e FKG Definir com o mesmo status da SE2
* Tabela FKE : Definir com o mesmo status da FKX
* Tabela FKJ : Definir com o mesmo status da SA2
* Tabela FKD : Definir com o mesmo status da SE2
* Tabela FKY : Definir com o mesmo status da SE5
* Tabela FKC : Status de abertura conforme a necessidade
* FI7 e FI8 : Definir com o mesmo status da SE1 e SE2
* FK1 a FK9 e FKA : Definir com o mesmo status da SE5

**Saiba mais:**  
[FAQ - 0016 - Quais os fatos geradores serão considerados no extrator financeiro?](https://tdn.totvs.com/pages/releaseview.action?pageId=737543501)  
[Compartilhamento de tabelas do módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)
