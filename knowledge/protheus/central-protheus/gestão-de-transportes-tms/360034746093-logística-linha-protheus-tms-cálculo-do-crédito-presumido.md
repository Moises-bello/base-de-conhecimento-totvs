---
article_id: 360034746093
category: Gestão de Transportes (TMS)
content_hash: e8e1eec62d8e63efba43408e424a1eedbaae346f8579c12f75d2004dba1e9235
fetched_at: '2026-06-28T22:45:27.371035+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cálculo do crédito presumido
type: support-article
updated_at: '2024-09-03T20:19:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034746093-Log%C3%ADstica-Linha-Protheus-TMS-C%C3%A1lculo-do-cr%C3%A9dito-presumido
---

***![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26103281087767)***Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Qual a configuração para cálculo do **crédito presumido**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A configuração em questão serve para atender ao **Convênio ICMS 106/96**, onde fica concedido aos estabelecimentos prestadores de serviço de transporte um **crédito de 20%** do valor do **ICMS** devido na prestação, que será adotado, opcionalmente, pelo contribuinte, em substituição ao sistema de tributação previsto na legislação estadual.  
  
Segue as principais configurações para que o **CT-e** seja gerado utilizando o **crédito presumido**:

* Parâmetros via **Configurador** - **SIGACFG/ Ambiente/ Cadastros/ Parâmetros**:
  + **MV\_TMSGNRE -** Informe os estados inscritos para a geração do **GNRE**. Exemplo RJ/MG/SC/RS/PR/MT.
  + **MV\_UFCRD20 -** Estados que possuem a geração de **GNRE** com redução do **ICMS** em 20% conforme Convênio **ICMS** 106/96. Exemplo RJ/MG/SC/RS/PR/MT.
  + **MV\_TPSOLCF -** Informar os tipos dos clientes envolvidos no processo entre aspas, por exemplo **"S,F,R"**, sendo **S - Solidário**, **F - Consumidor Final** e **R - Revendedor**. O tipo do cliente é definido no campo **Tipo** - **A1\_TIPO** no cadastro de **Clientes**,localizado em **Atualizações/Cadastros/Clientes - MATA030**.
* Configuração da **TES** - em **SIGATMS/Atualizações/Cadastros/Tipos de Entradas e Saídas - MATA080**
  + Aba **Adm/fin/custo:**
    - **Crd. ICMS ST - F4\_CREDST = 2 - Retido ST**
  + Aba **Impostos:**
    - **Calcula ICMS - F4\_ICM = Sim**
    - **Cred. ICMS - F4\_CREDICM = Sim**
    - **Crd. Pres. - F4\_CRDPRES = 20**
    - **Crd. Transp. - F4\_CRDTRAN = 20.** Para que ocorra a dedução do presumido da **GNRE**.
    - **Cred Pr ST - F4\_CRPRST = 20.** Preencher este campo para casos onde existir o **ICMS** **ST**.
    - **Tp Cred Pres - F4\_TPCPRES = N**
  + Aba **Outros:**
    - **Agreg CrdPre - F4\_AGREGCP = 1 - Sim.** Se desejar que o valor do credito presumido seja agregado ao valor total do frete, então **F4\_AGREGCP = 1,** caso não**, F4\_AGREGCP = 2.**

**Importante**Aqui foram descritos os principais campos para o calculo do credito presumido, mas, podemos ter vários cenários e regras fiscais na prestação do serviço de transporte, desta forma, é imprescindível que o setor fiscal de sua empresa valide a configuração do **TES**. **Saiba mais**No cadastro do **TES**, temos varias opções de preenchimento do campo **Tp Cred Pres - F4\_TPCPRES** conforme descrito em [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configurar ICMS para Crédito Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048439114-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configurar-ICMS-para-Cr%C3%A9dito-Presumido).Para geração da **GNRE** - [Logística - Linha Protheus - TMS - Como gerar a GNRE e o Título a Pagar.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051794294-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-a-GNRE-e-o-T%C3%ADtulo-a-Pagar)Para uso do **ICMS ST** - [Logística - Linha Protheus - TMS - Configuração do ICMS ST.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402831031703-Log%C3%ADstica-Linha-Protheus-TMS-Configura%C3%A7%C3%A3o-do-ICMS-ST)Para calculo do credito presumido via configurador de tributos **-** [CFGTRIB - Crédito Presumido de ICMS.](https://tdn.totvs.com/pages/releaseview.action?pageId=747332379) **Glossário**  
**CT-e** - Conhecimento de Transporte Eletrônico**ICMS** - Imposto sobre Circulação de Mercadorias e Serviços**SIGATMS** - Gestão de Transportes**SIGACFG** - Configurador**ICMS ST** - Substituição Tributária **TES** - Tipos de Entrada e Saída  
**GNRE** - Guia Nacional de Recolhimento de Tributos Estaduais
