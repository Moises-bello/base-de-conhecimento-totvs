---
article_id: 360038654813
category: Financeiro - Contas a Receber
content_hash: edca1a7173ec3435d472b336021ba3db0d85f62998578813ba47df5a46e8a359
fetched_at: '2026-06-28T22:38:13.784392+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FISA001 - Como gerar
  registro F500 e F525
type: support-article
updated_at: '2025-10-03T20:48:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038654813-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FISA001-Como-gerar-registro-F500-e-F525
---

**Dúvida**  
Como gerar registro F500 e F525?  
  
**Ambiente**Microsiga Protheus – Financeiro - FINA070 - A partir da versão 11.8  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. No módulo Financeiro, preenchendo os campos conforme segue no cadastro de natureza:

* **Código;**
* **Descrição;**
* **Tipo Natureza (ED\_TIPO):** (2 – Analítico);
* **Condição Natureza (ED\_COND):** (R – Receita);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204075927)

* **Tp Reg (ED\_TPREG) =** Cumulativo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204078231)

* **Apur. Pis** (**ED\_APURPIS**)= DEBITO;
* **Apur. Cofins** (**ED\_APURCOF**)=DEBITO;
* **% Ap. PIs** (**ED\_PCAPPIS**) = 0,65;
* **% Ap. Cofins** (**ED\_PCAPCOF**) = 3,00;
* **CST Pis** (**ED\_CSTPIS**) = 01;
* **CST Cofins** (**ED\_CSTCOF**) = 01;
* **Ind Cmulat** (**ED\_INDCMLT**) = cumulativo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204082327)

2. Havendo incidência de juros e multa, o parâmetro **MV\_NATRNT** deverá ser configurado com uma natureza distinta daquela utilizada no título.

3. No módulo financeiro, rotina contas a**Receber:**  
Incluir um registro com a natureza que cadastrou as informações dos impostos de apuração.   
  
4. Realizar a baixa do título na rotina de baixa **manual.**5. Na rotina **Gerar Apuração** **(FISA001)**, selecione a opção **Apuração EFD Contribuições**, em seguida, clique em **Processar Apuração da EFD Contribuições** e preencha os parâmetros solicitados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172892439)

Preencha os parâmetros conforme indicado abaixo:

* **Data Inicial** (informar o mês);
* **Data Final;**
* **Livros: deverá conter um asterisco:** (\*);
* **Selecionar Filial;**
* **Tributos: (1 - PIS/ Cofins);**
* **Regime PIS/COFINS:** (3 - Cumulat. Caixa);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172895895)

* **Indicador Regime Cumulativo**: (1 - Consolidado);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204087575)

* Ao confirmar a operação, o processamento será realizado conforme demonstrado na imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172900631)

* Após a conclusão, será exibida a mensagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172903319)

* Será possível validar as informações referentes aos tributos gerados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172906263)

6. Para gerar o arquivo da EFD deve clicar em "**Geração do arquivo da EFD Contribuições"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204094487)

Preencha os parâmetros conforme indicado abaixo:

* **Data Inicial** (informar o mês);
* **Data Final;**
* **Livros**: deverá conter um asterisco (\*);
* **Selecionar Filial;**
* **Diretório:** Caminho que será salvo o arquivo;
* **Arquivo:** (nome do arquivo) ;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204096791)**

* **Regime PIS/Cofins:** (2 - Cumulativo);
* **Tipo de Escrituração:** (0-Original);
* **Indicador Situação Especial**: 0;
* **Indicador Natureza PJ:** 00;
* **Atividade Preponderante:** 9;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397172912279)

* **Indicador Regime Cumulativo:** (1 - Caixa) ;
* **Indicador NFe/Cupom:** (1 - Consolidado);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35397204100247)
