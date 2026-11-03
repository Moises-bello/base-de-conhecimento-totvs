---
article_id: 4412676924055
category: NFe - Nota Fiscal Eletrônica
content_hash: 2aa6ba11bd8bb990493e2870a26ae4a8f13e1e4389186aa4b8457b13c91253a0
fetched_at: '2026-06-28T22:40:05.156451+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 599 Rejeição :
  CFOP de Importação e não informado dados de II'
type: support-article
updated_at: '2025-07-18T18:48:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412676924055-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-599-Rejei%C3%A7%C3%A3o-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-de-II
---

**Dúvida**599 Rejeição: CFOP de Importação e não informado dados de II   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

**1.** Acessar o módulo Configurador (SIGACFG), em seguida em ***Ambiente /Cadastros / Parâmetros clicar em editar*** MV\_EIC0064 :  .T. ou .F. conforme necessidade da empresa.

Atenção: Com este parâmetro habilitado, significa que o valor informado no item da NF de importação não estará com o Valor de II. Com o parâmetro desabilitado, significa que o valor informado no item da NF de importação estará com o Valor de II. Cabe ao usuário informar ou não o Valor dos Produtos com o Valor de II, lembrando sempre considerando a definição do parâmetro citado.

***Procedimento para lançamento da nota de importação:***

**1.** Acesse a rotina ***MATA103*** e preencha o cabeçalho da nota; 

**2.** Some o valor Aduaneiro e o Imposto de Importação e informe o resultado nos campos: ***Valor do item (D1\_VUNIT) e Valor total (D1\_TOTAL);***

**3.** Insira o TES com a configuração específica para redução de ***base do ICMS % Red. do ICMS preencher o campo (F4\_BASEICM);***

**4.** Informe a alíquota do Imposto de Importação e o valor do Imposto de Importação **nos campos Aliq Import. (D1\_ALIQII) e  Vlr. I.I. (D1\_II);**

**5.** Informe as despesas acessórias, na aba **Descontos/Frete/Despesas;**

* **Para *mais informações:***

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=6076840)*

* **Saiba mais:**

CFOP de Importação **(inicia por 3)** e não informado o grupo de II Exceção: a regra não se aplica para os seguintes **CFOP: 3.201; 3.202; 3.211; 3.503; 3.553 (NT 2011/004)**

1. Preencher com um dos CFOPs no campo ***Cod. Fiscal F4\_CF 3.201; 3.202; 3.211; 3.503; 3.553.***

![F4_CF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412671143063)

2. Após isso, ***gere novamente a NF-e.***

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412663512599)
