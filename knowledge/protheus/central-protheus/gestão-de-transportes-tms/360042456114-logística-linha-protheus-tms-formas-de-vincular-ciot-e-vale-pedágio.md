---
article_id: 360042456114
category: Gestão de Transportes (TMS)
content_hash: 9cace4b68aa04fbdf8c452a807caf1b9b45a3d33f672764ce4fb19ccea196a8c
fetched_at: '2026-06-28T22:45:29.206503+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Formas de vincular CIOT e Vale-Pedágio
type: support-article
updated_at: '2026-06-10T14:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042456114-Log%C3%ADstica-Linha-Protheus-TMS-Formas-de-vincular-CIOT-e-Vale-Ped%C3%A1gio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29739512440215)**Tempo aproximado para leitura:**00:04:30 min**  
  
**Dúvida**  
Como vincular o **CIOT** nos processos do **SIGATMS?**  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) – A partir da versão 11.80  
  
**Solução**  
No **SIGATMS** existem as seguintes formas de informar o **CIOT**:

* **Manual -**Cliente obtém o **CIOT** por meio de uma **IPEF** e informa manualmente no Complemento de viagem os dados da operação nos seguintes campos:
  + **DTR\_CIOT - CIOT -** Conhecimento de Identificação de Operação de Transporte. **Importante**: Este campo só é editável caso o campo **DTR\_CODOPE -Codigo da Operadora** esteja vazio.
  + **DTR\_FORCTO - For. CIOT** e **DTR\_LOJCTO - Loja CIOT** - Empresa responsável pela geração do **CIOT.**
* Para Vale Pedágio, necessário informar os seguintes campos:
  + **DTR\_IDVPO - Id Vale Pedagio ANTT.** Novo campo criado para gravação do Número da Compra do Vale Pedágio retornado pela **ANTT.** Caso não possua o campo **DTR\_IDVPO** em seu ambiente, preencha o número da compra do vale pedágio no campo **DTR\_PRCTRA - No. Proc. Tr -** Número do Processo de Transporte da Operadora de Frota. Na **Viagem Modelo 3 - TMSAF60**, o Número do Processo de Transporte da Operadora de Frota deve ser preenchido no campo **DM5\_PRCTRA - No. Proc. Tr**, disponível nas abas **Recursos/ Operadoras.**
  + **DTR\_FOROPE** - **Forn Op. Frt** e **DTR\_LOJOPE - Loja Op. Frt** - Empresa fornecedora do **Vale-Pedágio**. Este campo gatilha o **CNPJ**do fornecedor para o campo **DTR\_CNPJOP.**
  + **DTR\_FORPDG** **- Forn. Pedag.** e **DTR\_LOJPDG - Loja Pedag.** - Responsável pelo pagamento do **Vale-Pedágio.** Este campo gatilha o **CNPJ**do fornecedor para o campo **DTR\_CNPJPG**. Informar somente quando o responsável não for o emitente do **MDFe.**
  + **Pré-requisito:**Configurar operações para efetivação de viagem, frete mínimo e emissão do **MDFE***.*

* **ANTT -** O **TMS** possui integração para gerar **CIOT** diretamente com a **ANTT** para **frota própria**. É necessário estar com o Sistema atualizado e seguir as orientações da documentação em **Anexo**.
* No caso de frota de **terceiros e agregados**, deve-se gerar o **CIOT** com **IPEFs**, e o **TMS** possui integração com as seguintes **IPEFs**:
  + **Pamcard** -Por meio da integração com a operadora de frotas **Pamcard**, obtêm-se o número do **CIOT**e gerencia-se o pagamento de frete.  
    **Pré-requisito:** Configurar operações para efetivação de viagem, **MDFe**, Contrato de Carreteiro, frete mínimo e fechar contrato com a operadora **Pamcard.**
  + **REPOM -**Por meio da integração com a operadora de frotas **REPOM**, obtêm-se o número do **CIOT**e gerencia-se o pagamento de frete.  
    **Pré-requisito:** Configurar operações para efetivação de viagem, **MDFe**, Contrato de Carreteiro, frete mínimo e fechar contrato com a operadora **REPOM.**
  + **PagBem -** Por meio da integração com a operadora de frotas **PagBem**, obtêm-se o número do **CIOT**e gerencia-se o pagamento de frete.  
    **Pré-requisito:** Configurar operações para efetivação de viagem, **MDFe**, Contrato de Carreteiro, frete mínimo e fechar contrato com a operadora **PagBem.**

Estes campos citados acima, também são utilizados no preenchimento do **CIOT** e **Vale-Pedágio** no **MDFe**. As *tags* do **Vale-Pedágio** são preenchidas da seguinte forma:

* Para geração da *tag **<*****infCiot>**, é necessário que o campo **DTR\_CIOT** esteja preenchido:
  + **<CIOT> -** Número do **CIOT;**
  + **<CNPJ> - CNPJ** da empresa responsável pela geração do **CIOT;**
* Para geração da *tag* **<valePed>**, é necessário que os campos **DTR\_FOROPE** e **DTR\_LOJOPE** sejam preenchidos:
  + **<CNPJForn>** - **CNPJ** da empresa fornecedora do **Vale-Pedágio** informado nos campos **DTR\_FOROPE** e **DTR\_LOJOPE.** Lista de **FVPO**habilitadas pela **ANTT** disponível em [Fornecedores de VPO habilitadas;](https://www.gov.br/antt/pt-br/assuntos/cargas/vale-pedagio-obrigatorio/fornecedores-de-vpo-habilitadas)
  + **<CNPJPg>** - **CNPJ** do responsável pelo pagamento do **Vale-Pedágio** informada nos campos **DTR\_FORPDG** e **DTR\_LOJPDG;**
  + **<nCompra>** - Número de ordem do comprovante de compra do **Vale-Pedágio**. Esta *tag* é preenchida da seguinte forma:
    - Se o campo **DTR\_IDVPO** já foi criado no ambiente, este será o campo utilizado, independente da **FVPO** que está integrando. Quando este campo está criado na base, somente ele será considerado, e caso não esteja preenchido, a *tag* **<nCompra>** não será montada;
    - Caso ainda não tenha o campo **DTR\_IDVPO** criado no ambiente, a *tag* **<nCompra>** é montada conforme a seguinte regra:
      * Quando for preenchimento manual do vale pedágio **(DTR\_CODOPE VAZIO)** ou utilizar a integração com a **REPOM (DTR\_CODOPE = 01)**, utiliza o campo **DTR\_PRCTRA**;
      * Quando utilizar a integração com a **Pamcard (DTR\_CODOPE = 02)**, utiliza o campo **DTQ\_IDOPE**;
      * Quando utilizar a integração com a **PagBem (DTR\_CODOPE = 03)**, utiliza o campo **DTR\_IDPDG.**
      * Se nenhum desses campos estiver  preenchido, a *tag* **<nCompra>** não será montada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32618251347607)

* **<vValePed>** - Valor do **Vale-Pedágio**, utiliza o campo **DTR\_VALPDG**.
* **<tpValePed>** - Tipo do **Vale-Pedágio**, utiliza o campo **DTR\_TPSPDG**.
* **<categCombVeic>**- Categoria de Combinação Veicular, é preenchida conforme a quantidade de eixos do veículo.

**Glossário**  
**ANTT -** Agência Nacional de Transportes Terrestres  
**CIOT** ***-***Código Identificador da Operação de Transportes  
**CNPJ** ***-***Cadastro Nacional da Pessoa Jurídica  
**FVPO -** Fornecedoras de Vale Pedágio Obrigatório  
**IPEF*****-*** Instituição de Pagamento Eletrônico de Frete  
**MDFe*****-*** Manifesto de Documentos Fiscais Eletrônico  
**SIGATMS -**Gestão de Transportes  
  
**Anexo**

* Documentação de integração com **ANTT** para frota própria: [DT Integração com a ANTT para geração e declaração de CIOT.](https://tdn.totvs.com/pages/releaseview.action?pageId=1070535456)
* Documentação de integração com a **Pamcard**: [Logística - Linha Protheus - TMS - Informações sobre a integração Pamcard com o SIGATMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025729312-Log%C3%ADstica-Linha-Protheus-TMS-Informa%C3%A7%C3%B5es-sobre-a-integra%C3%A7%C3%A3o-Pamcard-com-o-SIGATMS)
* Documentação de integração com a **REPOM**: [Logística - Linha Protheus - INTEGRAÇÃO REPOM DOCUMENTAÇÃO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042532534)
* Documentação de  integração com a **PagBem**: [Integração TMS x PagBem (Integrações - SIGATMS)](https://tdn.totvs.com/x/SW06K)
* Documentação referente ao **Frete Mínimo**: [TIPO DE OPERAÇÃO DA VIAGEM - Frete Mínimo](https://tdn.totvs.com/pages/releaseview.action?pageId=425443149)
* Documentação referente à **NT 2020.001**: [7880412 DLOGTMS02-9632 DT NT 2020-001 MDF-e Integrado.](https://tdn.totvs.com/pages/releaseview.action?pageId=540891586)
* Documentação referente ao responsável pela geração do **CIOT**: [DT CNPJ do Fornecedor do Vale Pedágio inexistente na base da ANTT](https://tdn.totvs.com/pages/releaseview.action?pageId=683192530)
* Documentação sobre a criação do campo **DTR\_IDVPO**: [DT VPO Obrigatório ANTT- Operadoras de Frota](https://tdn.totvs.com/x/iX-RNw)
* Como obter o **CIOT**por meio de uma **IPEF:** [Instituições aptas à geração do CIOT.](https://www.gov.br/antt/pt-br/assuntos/cargas/pagamento-eletronico-de-fretes-pef-ciot/instituicoes-de-pagamento-eletronico-de-frete)
