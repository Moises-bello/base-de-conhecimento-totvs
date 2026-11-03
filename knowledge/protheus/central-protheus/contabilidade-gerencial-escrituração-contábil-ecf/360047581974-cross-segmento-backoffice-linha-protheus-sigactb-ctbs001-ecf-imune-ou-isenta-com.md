---
article_id: 360047581974
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 6cff58e90224d0ea2515c05dd0589e9656aeaf285d767f9d863877ed33425d14
fetched_at: '2026-06-28T22:40:47.279784+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECF – IMUNE
  OU ISENTA COMO GERAR
type: support-article
updated_at: '2022-05-13T19:52:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-IMUNE-OU-ISENTA-COMO-GERAR
---

**Dúvida**Como gerar o arquivo da ECF para Imune ou Isenta

**Ambiente**  
Protheus – Contabilidade Gerencial – 12.1.17   
  
**Solução**

* Realizar a Apuração de Resultados [Trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search) ou [Anual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* Possuir [CADASTRO DE CALENDÁRIO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024569414-MP-SIGACTB-ECF-CADASTRO-DE-CALEND%C3%81RIO-CONTABIL?source=search)
* Para gerar com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search) necessário está devidamente cadastrado e apurado
* Veja com detalhe todos os  [Parâmetros para geração da Escrituração](http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF)

* Realize o preenchimento do parâmetro FORMA\_TRIB (Forma de Tributação:) 8 OU 9

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070931813/mceclip0.png)

* FORMA\_APUR (Período de Apuração do IRPJ e CSLL) = Em branco
* COD\_QUALIF\_PJ (Qualificação da Pessoa Jurídica:) = Preencher
* FORMA\_TRIB\_PER (Forma de Tributação no Período:)= EM BRANCO
* MES\_BAL\_RED (Forma de Apuração da Estimativa Mensal:)= EM BRANCO

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070932493/mceclip2.png)

* Preencher o campo  [TIP\_ESC\_PRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006982951-MP-SIGACTB-ECF-ERRO-PVA-TIP-ESC-PRE?source=search)
* Obs: veja com atenção o preenchimento deste parâmetro

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069804094/mceclip3.png)

* TIP\_ENT (Tipo de Pessoa Jur.Imune ou Isenta) =Preencher

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070934473/mceclip0.png)

* Apuração da IRPJ para Imunes e Isentas = Preencher
* Apuração da CSLL para Imunes e Isentas= Preencher

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069804934/mceclip1.png)

* Data Inicial ? = 01/01
* Data Final ? = 31/12
* Apuração do Exercício (L/P) = 31/12/14 (caso a apuração seja trimestral este campo não deve ser preenchido)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070935173/mceclip2.png)

* Preencher os parâmetros abaixo de forma correta

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070935893/mceclip3.png)

* Obtenha a  [Visões Gerenciais](http://tdn.totvs.com/pages/releaseview.action?pageId=189314312) U100 , U150 U180 e U182
* Importante **Não** [é permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)
* Ao gerar informando visão gerencial os sistema alimenta as tabelas CSD / CSE
* Ao gerar **NÃO** informando visão gerencial os sistema alimenta as tabelas CSC / CSK , com isso o sistema considera a amarração do plano de contas com o plano referencial para gerar o U100(balanço) e o U150 (dre)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070936013/mceclip4.png)

* O centro de custo não é obrigatório , porem caso informe  [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search) necessário está devidamente cadastrado e apurado
* Informe o plano de contas referencial para que o  [J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) seja gerado

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070937033/mceclip6.png)

* Caso exista necessidade informe as visões gerencial U180 e U182

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070936893/mceclip5.png)

* Caso gere Sem informar a visão gerencial de balanço e Dre verifique se a CSC e a CSK foram alimentadas com registro U
* Caso gere  informando a visão gerencial de balanço e Dre verifique se a CSD e CSE foram alimentadas com registro U

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069808554/mceclip7.png)

* Veja se todas as [Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search) CS foram alimentadas

Registro        Tabela  TASFST1

Reg 0010        CSZ     T127

Reg 0020        CSZ     T127

Reg 0030        Cadastro de Empresas - SIGAMAT

Reg 0035        CSR     T01AM

Reg 0930        CS8     T002

Reg J050        CS3     T010

Reg J051        CS4     T010AA

Reg J053        CST     T010AB

Reg J100        CS5     T0111

Reg K155        CSC     T087AA

Reg K156        CSK     T087AB

Reg K155        CSC     T087AC

Reg K156        CSK     T087AD

Reg T120    CSD / CSE          T093AA

Reg T150    CSD / CSE          T093AA

Reg T170    CSD / CSE          T093AA

Reg T181    CSD / CSE          T093AA

Reg U100    CSC / CSK,  T094AA quando não utilizado Visão Gerencial.

Reg U100    CSD / CSE,  T094AA quando utilizado Visão Gerencial.

Reg U150    CSC / CSK,  T094AB quando não utilizado Visão Gerencial.

Reg U150    CSD / CSE,  T094AB quando utilizado Visão Gerencial

Reg U180    CSD / CSE          T094AB

Reg U182    CSD / CSE          T094AC

Bloco X                CSD / CSE   T096 para os registros exportados pelo SIGACTB

Bloco Y                CSD / CSE   T096 para os registros exportados pelo SIGACTB

* Verifique se a tabela TAFST1 foi alimentada :
* registro da conta verifique T127,T087AA ...T094, T094AA , T094AC , T094AB , T094AB

\*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   |T094AA|1|2.01.01|0|1|1500.59|2|  [(Clique aqui para detalhe deste layout)](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

* Verifique o TAFSTATUS = 3

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069814354/mceclip8.png)

* Verifique se a tabela TAFST2 foi alimentada :
* no registro da conta verifique T127,T087AA ... T094, T094AA , T094AC , T094AB , T094AB

  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   |T094AA|1|2.01.01|0|1|1500.59|2|  [(Clique aqui para detalhe deste layout)](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

* Verifique o TAFSTATUS = 3

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070941493/mceclip9.png)

* Acesse a Rotina - **TAFA324** e verifique se foi preenchido

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070941753/mceclip10.png)

**Bloco U - Imunes ou Isentas [(Clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)**

**Registro U001 - Abertura do Bloco U**

**Registro U030 - Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas**

* Tabelas - CEY (Apuração IRPJ/CSLL Emp. Isenta) / CAH (Período de Apuração)
* Registro do Layout TOTVS - T094
* Rotina - **TAFA324** (Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

**Registro U100 - Balanço Patrimonial**

* Tabelas - C2R (Natureza Conta/Grupo Contab.) / CHA (Código de Conta Referencial) / CEZ (Balanço Patrimonial) / CAH (Período de Apuração)
* Registro do Layout TOTVS - T094AA
* Rotina - **TAFA324**(Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

**Registro U150 - Demonstração do Resultado**

* Tabelas - C2R (Natureza Conta/Grupo Contab.) / CHA (Código de Conta Referencial) / CHG (Demonstração do Resultado) / CAH (Período de Apuração)
* Registro do Layout TOTVS - T094AC
* Rotina - **TAFA324** (Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

**Registro U180 - Cálculo do IRPJ das Empresas Imunes e Isentas**

* Tabelas - CEY (Apuração IRPJ/CSLL Emp. Isenta) / CAH (Período de Apuração) / CH6 (Códigos de Lançamento ECF) / CFI (Registros Genéricos – Bloco U)
* Registro do Layout TOTVS - T094AB
* Rotina - **TAFA324**(Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

**Registro U182 - Cálculo da Contribuição Social sobre o Lucro Líquido (CSLL) das Empresas Imunes e Isentas**

* Tabelas - CEY (Apuração IRPJ/CSLL Emp. Isenta) / CAH (Período de Apuração) / CH6 (Códigos de Lançamento ECF) / CFI (Registros Genéricos – Bloco U)
* Registro do Layout TOTVS - T094AB
* Rotina - **TAFA324** (Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

**Registro U990 - Encerramento do Bloco U**

Para mais detalhes veja :

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>
