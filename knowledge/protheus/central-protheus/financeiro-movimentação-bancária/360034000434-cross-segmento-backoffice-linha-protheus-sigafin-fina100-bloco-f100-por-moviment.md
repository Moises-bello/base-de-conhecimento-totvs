---
article_id: 360034000434
category: Financeiro - Movimentação Bancária
content_hash: 49ea4cdde35ba5288a8503b42e735dc70988a1a054c21e7b692d59d330871f73
fetched_at: '2026-06-28T22:38:19.398195+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100 - Bloco F100
  por Movimentos Bancários e Aplicação e Empréstimo
type: support-article
updated_at: '2026-01-21T13:23:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034000434-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Bloco-F100-por-Movimentos-Banc%C3%A1rios-e-Aplica%C3%A7%C3%A3o-e-Empr%C3%A9stimo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20476729712023)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como gerar o bloco F100 pela rotina de Movimentação Bancária e Aplicação e Empréstimo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Solução**  
1. Configurar o parâmetro **MV\_APLFIN** = .T.  
2. Informar o código da **natureza** para o **Movimentos Bancário** e/ou da **Aplicação e Empréstimo**no parâmetro **MV\_APLNAT**, campo **ED\_CODIGO** da tabela **SED.**  
3. Nessa natureza, devem constar as alíquotas para tratamento das aplicações financeiras de **PIS** e **COFINS** na aba **FISCAL.**  
4. Acesse o módulo **Financeiro - Atualizações - Cadastro - Naturezas.**

Exemplo:  
Aba **Dados da Natureza**  
Campo **Cond Naturez (ED\_COND)** conteúdo = Receita   
Campo **Tipo Naturez (ED\_TIPO)** conteúdo = 2 - Analítico  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044752393)  
  
Aba **Imposto**  
Campo **Tp Reg (ED\_TPREG)** conteúdo = 1 - Não cumulativo.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043888554)  
  
Aba **Fiscal**  
Campo **Apur. Pis (ED\_APURPIS)** conteúdo= D - Débito.    
Campo **Apur. Cofins (ED\_APURCOF)** conteúdo= D - Débito  
Campo **CST Cofins (ED\_CSTCOF)** conteúdo = conforme a necessidade.  
Campo **CST Pis (ED\_CSTPIS)** conteúdo =conforme a necessidade.  
Campo **% Ap. PIs (ED\_PCAPPIS)** conteúdo = 1,65  
Campo **% Ap. Cofins (ED\_PCAPCOF)** conteúdo = 7,60  
Campo **Ind Cmulat (ED\_INDCMLT)** conteúdo = 2 - Não cumulativo.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044752473)  
  
5. Configurar o parâmetro **MV\_APLAPRO** = .F.  
6. Incluir uma**Movimentação Bancária** ou **Aplicação e Empréstimo** com a **natureza** informada no parâmetro **MV\_APLNAT.**  
7. Gerar apuração via rotina **FISA001** nova apuração **PIS**, **COFINS** no módulo de **Livros Fiscais**.  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo Comp.  
8 - Gerar arquivo TXT no módulo **FISA008**  
**Parâmetros de geração do arquivo**  
**Regime PIS/COFINS** = 1- N.Cumulativo  
**Indicador do regime cumulativo** = 1-Consolidado

**Importante**  
Ao realizar uma aplicação em dólar utilizando a rotina (**FINA100)**, para que o valor seja convertido, o registro inserido pela rotina de movimento bancário (**FINA100**) deve estar nas moedas **M2, M3, M4** ou **M2** e o **banco** deve ser na mesma moeda desejada do movimento.

**Saiba mais**  
[Parâmetros MV\_APLFIN, MV\_APLNAT e MV\_APLAPRO](http://tdn.totvs.com/pages/releaseview.action?pageId=6070545)
