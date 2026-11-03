---
article_id: 360058862353
category: Financeiro - Contas a Pagar
content_hash: 04632f9acc3e0aee9b528f47e9b93dc6ec3a82add02d475afdf96318f848f15e
fetched_at: '2026-06-28T22:38:08.432111+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus   - SIGAFIN - Pontos de entrada
  FINA080
type: support-article
updated_at: '2026-05-13T18:19:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058862353-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-FINA080
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20897122026903) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Quais os pontos de entrada da rotina **FINA080** ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**  
Segue abaixo a relação dos pontos de entrada da rotina **FINA080**:

**F080BENEF** -  **Manipular o campo Beneficiário.**   
<http://tdn.totvs.com/display/PROT/TUPQD3_DT_PE_F080BENEF_para_manipular_o_campo_Beneficiario>  
  
**F080BROW - Pré-avaliação de dados a exibir.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070927>  
  
**F080BXLOTE** - **Manipular a variável cLoteFin.**   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071475>  
  
**F080BXLT** - **Baixa por lote.**  
<http://tdn.totvs.com/display/public/mp/F080BXLT+-+Baixa+por+lote+--+11656>  
  
**F080BXVEND** - **Manipula variáveis.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071466>  
  
**F080BXVL** -  **Mecanismos de Auto-Validação.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071364>  
  
**F080CM** - **Cálculo de correção monetária.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=763258452>  
  
**F080DCNB - Desabilita campos: multa, juros, descontos.**  
<http://tdn.totvs.com/display/PROT/F080DCNB+--+11658>  
  
**F080EST - Grava complemento de cancelamento.**  
<http://tdn.totvs.com/display/public/mp/F080EST+-+Grava+complemento+de+cancelamento+--+11659>  
  
**F080EST2 - Gravações complementares na baixa a pagar.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070933>  
  
**F080FIL - Antes da IndRegua na baixa por lote CP.**  
<http://tdn.totvs.com/display/public/mp/F080FIL+-+Antes+da+IndRegua+na+baixa+por+lote+CP+--+11661>  
  
**F080FILEMI - Campo data validado na baixa a data a ser validada**  
<http://tdn.totvs.com/display/PROT/F080FILEMI+-+Campo+data+validado+na+baixa>  
  
**F080LOJA - Retorna array com códigos de fornecedor**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070936>  
  
**F080MTBX - Permite verificar o conteúdo digitado para o motivo da baixa.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071618>  
  
**F080NATINS - Altera a natureza dos títulos de INSS.**  
<http://tdn.totvs.com/pages/viewpage.action?pageId=184781683>  
  
**F080PCAN - Completo de informações após cancelamento da baixa.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071643>  
  
**F080PCBX - Bloqueio de baixa parcial.**  
<http://tdn.totvs.com/display/public/mp/F080PCBX+-+Bloqueio+de+baixa+parcial+--+11664>  
  
**F080VCHEQ - Valida o campo número do cheque.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071635>  
  
**F080VEND - Alterar dados do título de vendor.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071614>  
  
**F080VLAD - Valida parâmetro MV\_VLTITAD para rotina automática.**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071560>  
  
**SE5FI080 - O ponto de entrada SE5FI080 será executado para gravar dados complementares da tabela SE5.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=309405536>

**F080TXIR - Informar taxa em baixas manuais rotina automática.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=546681841>  
  
**CanPaImp - Ponto de Entrada pode permitir que sejam canceladas baixas de PAs que contêm impostos.**  
<https://tdn.totvs.com.br/display/PROT/DT_CanPaImp_Permite_cancelar_baixas_PA_impostos>

**CriaImp - Permite ou não gerar impostos na baixa da NF.**  
<https://tdn.totvs.com.br/display/PROT/DT_CriaImp_Permite_ou_nao_gerar_impostos_na_baixa_da_NF>

**DelTx - Deleta TX do PA.**  
<https://tdn.totvs.com.br/display/PROT/DT_DelTx_Deleta_TX_da_Pa_FINA080>  
  
**F80GRVFK - Gravação de dados complementares na baixa.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=268817868>  
  
**PaComp - Altera valores dos campos pret. do PA.**  
<https://tdn.totvs.com.br/display/PROT/DT_PaComp_Altera_valor_dos_campos_pret_do_PA>  
  
**F080ACRE - Permite alterar o valor do acréscimo/decréscimo.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=552571454>  
  
**F080EXEA - Tratamentos específicos na exclusão do borderô.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=539690432>

**F080KCO - Ponto de entrada para validar o banco em baixas manuais.**  
<https://tdn.totvs.com.br/display/PROT/F080KCO+-+Ponto+de+entrada+para+validar+o+banco+em+baixas+manuais>  
  
**F80L9816 - Ponto de entrada para determinar a taxa a ser utilizada na formação da base de cálculo do IRRF.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=680243383>

**FA080IMP - Trata valores de impostos.**  
<https://tdn.totvs.com.br/display/PROT/FA080IMP-+Trata+valores+de+impostos>  
  
**FA080PCC - Verifica valores do PIS,** [COFINS,](https://tdn.totvs.com.br/display/PROT/FA080POS_DT_Altera_variaveis_de_memoria) **CSLL IRRF.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=507002093>

**FA080POS - Altera variáveis de memória.**  
<https://tdn.totvs.com.br/display/PROT/FA080POS_DT_Altera_variaveis_de_memoria>  
  
**FA080VEST - Validação de estorno.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=273977943>  
  
**FIN080PCC - Incremento de query no cálculo de PCC.**  
<https://tdn.totvs.com.br/pages/viewpage.action?pageId=63277108>

**FA080DT - Validação da data da baixa no contas a pagar**

<https://tdn.totvs.com/display/public/mp/FA080DT+-+Valida+data++--+11890>

**Saiba mais Pontos de entradas e a Rotina FINA080 do Financeiro.**

[Baixas a pagar manual - FINA080](https://tdn.totvs.com.br/display/PROT/Baixas+a+pagar+manual+-+FINA080)  
[Baixa manual contas a pagar - FINA080](https://tdn.totvs.com/display/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)  
[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)
