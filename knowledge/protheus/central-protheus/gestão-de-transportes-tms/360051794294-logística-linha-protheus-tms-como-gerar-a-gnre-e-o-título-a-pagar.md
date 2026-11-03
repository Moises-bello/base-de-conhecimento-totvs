---
article_id: 360051794294
category: Gestão de Transportes (TMS)
content_hash: 0cb8abddd570c6ed11070ff554d4ed87aed77114bfd4f0538ef7c036374fc01b
fetched_at: '2026-06-28T22:45:27.441421+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como gerar a GNRE e o Título a Pagar
type: support-article
updated_at: '2026-04-27T13:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051794294-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-a-GNRE-e-o-T%C3%ADtulo-a-Pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24671656047895)** Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar a **GNRE** e o **Título a Pagar de ICMS** a partir do **TOTVS Logística TMS**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para gerar a **GNRE** e o **Título a Pagar de ICMS** é necessário acessar a rotina **Cálculo de Frete - TMSA200**, acionar a **tecla F12** e habilitar os seguintes perguntes:

* Quando for **ICMS Próprio**, a guia será gerada quando a **UF** de origem da prestação de serviço de transporte for diferente do conteúdo do parâmetro **MV\_ESTADO** da filial corrente, ou, se a **UF** informada no **MV\_ESTADO** estiver contida no parâmetro **MV\_TMSGNRE**, e com os perguntes **Gera Título ICMS Próprio** e **Gera Guia ICMS Próprio:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083727513)**

* Quando for **ICMS ST**, configure os perguntes **Gera Título Por Produto** e **Gera Guia por Produto:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24788417995543)**

* Quando for **DIFAL**, configure o pergunte **Gera Guia ICM Comp UF Dest:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29249365011479)

* Quando for **FECP**, configure o pergunte **Gera Guia FECP da UF Dest:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29249319536279)

* Preencher os parâmetros:
  + **MV\_RECEST -** Utilizado para informar o código e loja do cadastro de Fornecedor referente a secretaria do Estado de onde esta localizada a transportadora para pagamento do **ICMS.** Exemplo 000002;01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29454397149591)

* **MV\_RECST + UF** de origem - Utilizado para informar o código e loja referente ao cadastro de Fornecedor de cada Estado de onde começou a prestação de serviço de transporte para geração dos **Títulos a Pagar do ICMS Próprio** ou de **ICMS ST - Substituição Tributária.** Exemplo 000001;01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29454438258455)

* **MV\_ICMS** **-** Define a natureza a ser utilizada na geração automática do título com o valor do **ICMS** apurado no período pela rotina Apuração - **MATA953.**
* **MV\_TMSGNRE** **-** Informe os Estados inscritos para a geração do **GNRE**. Exemplo RJ/MG/SC/RS/PR/MT.
* **MV\_UFCRD20 -** Estados que possuem a geração de **GNRE** com redução do **ICMS** em 20% conforme Convênio **ICMS** 106/96. Exemplo **RJ/MG/SC/RS/PR/MT**.   
  Para que o credito presumido seja deduzido do valor do **GNRE**, no cadastro do **TES** deve estar informado o percentual do credito no campo **Crd. Transp. - F4\_CRDTRAN.**
* **MV\_GNRENF** - Para que não seja exibida a tela **GNRE** quando a opção **Guia de Recolhimento = Sim**, então, basta habilitar este parâmetro. A guia não será exibida em tela, mas será gerada juntamente com o titulo a pagar.

Com essa configuração, ao realizar o calculo do frete, será aberta a tela de geração da guia da **GNRE**, ao confirmar teremos a geração da **GNRE** e o **Título a Pagar** com o **ICMS** utilizado na operação, mas, caso o usuário cancele a tela de geração da guia **GNRE**, o **Título a Pagar** será gerado e registro referente a guia na tabela **SF6** não será gerado.  
Caso deseje bloquear a ação do usuário de cancelar a emissão da guia da **GNRE** durante o calculo do frete, sugerimos a utilização do ponto de entrada do Fiscal **APURF6CAN.** Esse ponto de entrada inibe em tela a ação do usuário de cancelar a geração da guia.  
  
**Importante**  
Por regra do motor Fiscal, o Sistema verifica se a **GNRE** está sendo gerada para um imposto configurado a partir do **Configurador de Tributos,** ou seja, se estiver utilizando o **Configurador de tributos** para ocalculo do **ICMS,** a configuração para a geração da **GNRE** deve ser realizada via **Configurador de tributos.** Caso a **GNRE** não esteja configurada no **Configurador de Tributos**, **a geração da GNRE será abortada**.  
  
Ao configurar a **GNRE** via **Configurador de tributos,** então, para que o **título a pagar** do imposto seja gerado, devemos cadastrar as **Regras Financeiras,** caso contrário, teremos apenas a geração da **GNRE** e não teremos o **título a pagar**.  
  
Ao gerar a **GNRE** na tabela **SF6 - Guias de Recolhimento**, nela teremos o código e loja do cliente tomador de serviço. Na tabela **SE2 - Contas a Pagar**, teremos o fornecedor conforme conteúdo dos parâmetros citados acima.  
  
**Saiba mais**  
Ponto de entrada [APURF6CAN - Defini se permite cancelar as inclusões das guias de recolhimento.](https://tdn.totvs.com/pages/releaseview.action?pageId=655882500)  
Documentação do **Configurador de Tributos** para configurar a **GNRE** - [CFGTRIB - Configurador de Tributos.](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos)  
Documentação do **Configurador de Tributos** para cadastrar as **Regras Financeiras** - [Configurador de Tributos - Regras Financeiras.](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)  
Para realizar a transmissão da **GNRE**, basta seguir as orientações disponíveis em [Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como configurar o sistema para transmissão das guias de recolhimento pela rotina GNRE WS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040642734-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-configurar-o-sistema-para-transmiss%C3%A3o-das-guias-de-recolhimento-pela-rotina-GNRE-WS?source=search)  
Documentação sobre o parâmetro **MV\_UFCRD20** - [Crédito presumido nos serviços de transportes](https://tdn.totvs.com/pages/releaseview.action?pageId=717695704).  
Para alterações de número, data de vencimento e natureza da guia de **GNRE**, temos o ponto de entrada [TITICMST](https://tdn.totvs.com/pages/releaseview.action?pageId=655862729)**.**  
  
**Glossário**  
**DIFAL** - Diferencial de alíquotas  
**FECP** - Fundo de Combate à pobreza  
**GNRE** - Guia Nacional de Recolhimento de Tributos Estaduais  
**ICMS** - Imposto sobre Circulação de Mercadorias e Serviços  
**ICMS ST** - Substituição Tributaria  
**TES** - Tipos de Entrada e Saída  
**UF** - Unidade Federativa
