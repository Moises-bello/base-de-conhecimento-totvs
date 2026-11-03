---
article_id: 4411677253783
category: RH - Definições de Cálculo
content_hash: a931f3b23063cb8a830f68a3f5e8e99842e0349cf94a415a6b84f07aefd14a28
fetched_at: '2026-06-28T22:43:22.338289+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus
type: support-article
updated_at: '2025-09-30T16:57:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26453976137751)** Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como cadastrar verbas no Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**O cadastro de Verbas é um dos **cadastros mais importantes** para que sejam feitos os cálculos de folha de pagamento, rescisões e férias no sistema. Sem ele, não será permitido **nenhum cálculo no sistema,** impossibilitando a utilização do módulo Gestão de Pessoal do Protheus.   
  
Nele são armazenados os códigos para **pagamentos, descontos e bases de cálculo** que serão gerados pelo sistema ou lançados manualmente. As verbas são utilizadas para demonstrar os pagamentos e descontos mensalmente nos diversos relatórios do sistema, bem como para atender às obrigações trabalhistas.  
  
Desta forma basicamente, as verbas estão divididas em:  
  
**Proventos** – São verbas positivas, ou seja, verbas que serão pagas ao funcionário.  
**Descontos** – São verbas negativas, ou seja, verbas que serão descontadas do funcionário.  
**Bases** – São verbas compostas pela diferença entre as verbas de proventos e descontos, e tem como objetivo principal servir de referência para o cálculo de outras verbas, como por exemplo: INSS, FGTS, Imposto de Renda, etc.  
  
As verbas serão calculadas automaticamente pelo sistema, que as identificará através do **campo “Id. Cálculo**”, que cadastra o identificador de cálculo correspondente ao cadastro, sendo eles, efetivamente, que definem o que é a verba, ou seja, se é um pagamento, um desconto etc.  
  
**Algumas verbas não possuem Id de Cálculo**  
  
As verbas com identificadores, **serão geradas pelo sistema** através dos diversos cálculos disponíveis no ambiente Gestão de Pessoal (Adiantamento, Folha de Pagamento, Férias, Rescisão, 13º salário, etc.) e armazenadas em suas respectivas tabelas, sendo posteriormente, após o fechamento mensal, transportadas para a tabela de movimento anual (SRD).  
  
**Alguns identificadores são obrigatórios** uma vez que o ambiente Gestão de Pessoal está preparado para atender a legislação (CLT). Com isso, ao cadastrar uma verba para cada identificador, a rotina de cálculo estará pronta para gerar os cálculos disponíveis no sistema, como: folha de pagamento, adiantamento, férias, rescisão e 13º salário, etc.  
  
No entanto, de acordo com a necessidade, poderão ser criadas verbas não vinculadas a um identificador, como por exemplo **verbas de horas extras**. As verbas de horas extras são específicas para cada empresa, pois os percentuais podem variar de acordo com as regras da convenção coletiva do sindicato da categoria a que pertencem os funcionários.  
  
Para cadastrar uma verba, acesse o módulo Gestão de Pessoas e, no menu **Atualizações/ Definições de Cálculo**, acesse a rotina de Verbas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411684090135)

Principais Campos:

**Aba Cadastrais**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10893513937815)

**Codigo** (RV\_COD): O usuário que determina, pois é o que será apresentado na folha quando calculado, e também na impressão de relatórios.  
**Descricao** (RV\_DESC): Crie uma descrição para a verba  
**Tipo do Cod** (RV\_TIPOCOD): Definir se a verba é um Provento, um Desconto ou uma Base Provento ou Desconto.  
**Id.p/Calculo** (RV\_CODFOL): Identificador para cálculo automático ou direcionamento em relatórios. Exemplo: Salário Mensalista tem o id 0031, então neste campo de Id tem que ser  
preenchido 0031.  
**Tipo Verba** (RV\_TIPO): Informar se a verba é de tipo horas, valor ou dias

**Aba Incidências**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10894083191831)**

**INSS** (RV\_INSS): Indica se a verba entrará para Base de Cálculo do INSS.  
**IR** (RV\_IR): Indica se a verba entrará para Base de Cálculo do IRRF  
**FGTS** (RV\_FGTS): Indica se a verba entrará para Base de Cálculo do FGTS  
**Ref.a Ferias** (RV\_REFFER): Indica se a verba que está sendo criada, é para ser paga quando calculadas as Férias. Exemplo: 1/3 de Férias, tem que ficar com SIM neste campo

**Aba Médias  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32866864595479)**

**Média 13°** (RV\_MED13): Indica se a verba é para ser paga como média, quando calculado o 13º Salário.  
**Média Férias** (RV\_MEDFER): Indica se a verba é para ser paga como média, quando calculado Férias  
**Med.Av.Prev** (RV\_MEDAVI): Indica se a verba é para ser paga como média, quando calculado Rescisão com Aviso Prévio.

**Aba Dissidio Retroativo**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10894180187543)

**Dissid.Ret**. (RV\_COMPL\_): Informa se a verba deverá ou não ser considerada no calculo do Dissídio Retroativo  
**Verba p.Diss**. (RV\_CODCOM\_): Informar o código da verba correspondente a ser utilizada no Dissídio Retroativo

**Aba eSocial**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10894621097239)

Na pasta **eSocial d**evem ser preenchidos os campos referentes ao eSocial, além dos códigos de incidência e, quando for o caso, das determinações judiciais para suspensão da incidência do encargo.

**Natureza** (RV\_NATUREZ): Informar a natureza da rubrica conforme layout do eSocial (Tabela S047)  
**Cd. Inc. IRRF** (RV\_INCIRF): Informar a incidência de IR conforme layout do eSocial (Tabela S138)  
**Cd. Inc. FGTS** (RV\_INCFGTS): Informar a incidência de FGTS utilizada no eSocial  
**Cd. Inc. CP** (RV\_INCCP): Informar a incidência para Previdência Social utilizada no eSocial

**Obs:** As configurações das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil

**Saiba Mais**[Manual Cadastro de Verbas](https://tdn.totvs.com/display/PROT/Manual+Cadastro+de+Verbas)   
[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
