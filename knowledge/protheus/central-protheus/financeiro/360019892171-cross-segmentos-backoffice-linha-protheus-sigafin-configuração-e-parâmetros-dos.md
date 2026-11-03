---
article_id: 360019892171
category: Financeiro
content_hash: 6da2f9b2c4236d786cb0cc61cc95b9e059d6ac5a092bb880a23f95ecbc71c6cd
fetched_at: '2026-06-28T22:38:01.275830+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Configuração e Parâmetros
  dos Impostos PIS/ COFINS/ CSLL
type: support-article
updated_at: '2023-03-30T01:09:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019892171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configura%C3%A7%C3%A3o-e-Par%C3%A2metros-dos-Impostos-PIS-COFINS-CSLL
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Quais parâmetros é preciso configurar para que seja calculado os impostos **PIS**/ **COFINS**/ **CSLL**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

**Configuração do imposto: PIS/ COFINS/ CSLL**

**NATUREZA**  
Calcula PIS (**ED\_CALCPIS**) = Campo que define se deve ser calculado PIS sobre um título dependendo da natureza   
  
Percentual de PIS (**ED\_PERCPIS**)= Percentual para cálculo de PIS em títulos com esta natureza  
  
Calcula COFINS (**ED\_CALCCOF**)= Campo que define se deve ser calculado COFINS sobre um título para natureza   
  
Percentual de COFINS (**ED\_PERCCOF**)= Percentual para cálculo de COFINS em títulos com esta natureza

**TES**  
Calcula PIS e COFINS (**F4\_PISCOF**) =   
Credito de PIS/COFINS, campo (**F4\_PISCRED**)=   
Informe se o imposto será creditado ou debitado

**PRODUTOS**  
Retém PIS (**B1\_PIS**)= Calcula PIS  
Retém COFINS (**B1\_COFINS**)= Calcula COFINS  
Retém CSLL (**B1\_CSLL**)= Calcula CSLL

**Alíquotas**

Perc.PIS(**B1\_PPIS**) =

Perc.COFINS(**B1\_PCOFINS**) =

Perc.CSLL(**B1\_PCSLL**) =

**CLIENTES**  
Recolhe COFINS (**A1\_RECCOFI**)= Campo para tratamento de efetivação de cálculo ou não de **COFINS** nos títulos deste cliente.  
  
Recolhe PIS (**A1\_RECPIS**)= Campo para tratamento de efetivação de cálculo ou não de **PIS** nos títulos deste cliente.  
  
Recolhe CSLL (**A1\_RECCSLL**)= Campo para tratamento de efetivação de cálculo ou não de **CSLL** nos títulos deste cliente.  
  
Modo de abatimento do imposto = cálculo do sistema

**FORNECEDORES**  
Recolhe COFINS (**A1\_RECCOFI**)= Informe se o Fornecedor é responsável pelo recolhimento da **COFINS**. Caso o fornecedor não seja responsável pelo recolhimento, o sistema fará a retenção do tributo.  
  
Recolhe PIS (**A2\_RECPIS**)= Informe se o Fornecedor é responsável pelo recolhimento do **PIS**. Caso o fornecedor não seja responsável pelo recolhimento, o sistema fará a retenção do tributo.  
  
Recolhe CSLL (**A2\_RECCSLL**)= Informe se o Fornecedor é responsável pelo recolhimento da **CSLL**. Caso o fornecedor não seja responsável pelo recolhimento, o sistema fará a retenção do tributo.

Importante: Os parâmetros abaixo indicam as alíquotas utilizada para **PIS**/**COFINS** via apuração.

**MV\_TXPIS** – Taxa de **PIS**  
**MV\_TXCOFIN** – Taxa de **COFINS**

Regra: Primeiro será buscada a alíquota do produto, caso não tenha buscará a informação do cadastro de Naturezas.

Parâmetros referente à retenção **PIS/COFINS/CSLL:**

**MV\_RF10925** = Data de referência inicial para que os novos procedimentos quanto a retenção de **PIS/COFINS/CSLL** seja m aplicados.  
  
**MV\_VL10925** = Valor Máximo de pagamentos no período para dispensa da retenção de **PIS/COFINS/CSLL**  
**MV\_RT10925** = Modo padrão de operação do sistema quanto a retenção de **PIS/COFINS/CSLL**. (1=Calculado p/sistema 2=Efetua Retenção sempre, 3=Não efetua retenção)  
  
**MV\_AC10925** = Controle de permissão para o usuário alterar modo de retenção na janela “cálculo de retenção” 1=Permite alteração, 2= Não permite alteração  
  
**MV\_AB10925** = Modo de retenção do **PIS,COFINS e CSLL** p/ C.Receber 1=Verif.retenção pelo valor da nota emitida 2=Verif.retenção p/soma notas emitidas no período  
  
**MV\_MT10925** = Verificar base de retenção pelo total ou apenas pelos títulos que retiveram impostos 1 = Todos 2 = Somente os que retiveram **PIS** etc  
  
**MV\_BX10925** = Define momento do tratamento da retenção dos impostos **PIS/COFINS/CSLL** 1 = Na Baixa ou 2 = Na Emissão  
  
**MV\_BS10925** = Indica se o cálculo da retenção será sobre a base do **PIS/COFINS/CSLL** ou pelo valor total da duplicata. 1=Valor da base; 2=Valor total  
  
**MV\_LJ10925** = Considerar para verificação de valores de retenção os valores de todas as lojas do cliente Opções: 1 = Loja atual ou 2 = Todas as lojas
