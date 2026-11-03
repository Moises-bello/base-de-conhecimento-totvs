---
article_id: 360037062034
category: RH - Contabilização
content_hash: 01b094089da49935043d0952872a180ecd446039584530ba60327cd083e466d3
fetched_at: '2026-06-28T22:43:45.913874+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração e geração PCO (processo 000085 - Fechamento
  Mensal da folha)
type: support-article
updated_at: '2025-07-31T19:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037062034-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-PCO-processo-000085-Fechamento-Mensal-da-folha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33856787305495)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como configurar e gerar o processo de PCO 000085 - Fechamento Mensal da Folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Para efetuar a configuração de **geração do PCO** do fechamento de folha mensal realize os seguintes procedimentos:   
  
1. Como premissa para integração com o módulo SIGAPCO, configure o parâmetro **MV\_PCOINTE = 1** , ativando a integração.

Acesse **Configurador -> Base de Dados -> Dicionário -> Base de Dados -> Parâmetros**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048501814)

2. Abaixo os cadastros básicos para iniciar a integração com o módulo (**Módulo 57 - Planejamento e Controle Orçamentário**): 

*![](https://tdn.totvs.com/download/attachments/243647601/image2016-7-13%2011%3A15%3A35.png?version=1&modificationDate=1468421946000&api=v2)*

 3. O primeiro cadastro referente a **Contas Orçamentárias**:

A conta orçamentária é o principal item da estrutura organizacional para elaboração das planilhas orçamentárias da empresa e é a base/guia para o detalhamento dos itens que se quer orçar.

O detalhamento e o conhecimento dos objetivos do planejamento e controle orçamentário da empresa são essenciais para cadastrar um plano de contas orçamentário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048502914)

Abaixo a confirmação de cadastro da conta exibida anteriormente:*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048503014)*

**DICA:** Uma opção muito útil é utilizar o plano de contas do módulo Contábil (SIGACTB) caso já possua as informações, conseguimos fazer a importação ativando o parâmetro **MV\_PCOSINC = 2**:  
<http://tdn.totvs.com/display/public/mp/MV_PCOSINC+-+Plano+de+Contas+Sincronizado++11315;jsessionid=C5AB3255FEDC43FDA80BC3106F587889>

*![](https://tdn.totvs.com/download/attachments/243647601/image2016-7-13%2011%3A17%3A20.png?version=1&modificationDate=1468421950000&api=v2)*

Em seguida na tela de cadastro de **Contas Orçamentárias** selecione a opção **Sincronizar**:*![](https://tdn.totvs.com/download/attachments/243647601/image2016-7-13%2011%3A19%3A7.png?version=1&modificationDate=1468421952000&api=v2)*

Ao finalizar a sincronização o plano de contas do contábil é importado para o SIGAPCO:![](https://tdn.totvs.com/download/attachments/243647601/image2016-7-13%2011%3A19%3A53.png?version=1&modificationDate=1468421951000&api=v2)

4) Em seguida iremos efetuar o cadastro de **Operações:**

Esta rotina responde pelo cadastramento e pela manutenção das operações que podem ser utilizadas na digitação e acompanhamento da planilha orçamentária.*![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048503394)*

Pode-se cadastrar diversas operações para auxiliar no acompanhamento de uma planilha orçamentária

5.Em seguida iremos cadastrar uma **Classe Orçamentária**:

A classe orçamentária permite organizar o orçamento segundo critérios que permitem compreender os tipos de valores que estão sendo apresentados. Propiciando informações para a administração, gerencia e a tomada de decisões:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049395473)

6. O próximo cadastro é o de **Tipos de Saldos**:

Podemos entender como saldo, toda e qualquer diferença de valores entre crédito e débito, em relação aos saldos iniciais de uma determinada conta orçamentária, em um determinado período.

A classificação dos tipos de saldos é de extrema importância, já que identifica os movimentos orçamentários contabilizados dentro do contexto definido pelo gestor do orçamento.

Este cadastro é utilizado para efetuar a criação e a manutenção dos tipos de saldos utilizados durante o acompanhamento do ciclo orçamentário:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048503894)

7) Após efetuar os cadastros básicos para integração, configure um ponto de lançamento:![](https://tdn.totvs.com/download/attachments/243647601/image2016-7-13%2011%3A38%3A16.png?version=1&modificationDate=1468421960000&api=v2)

8. O módulo nos proporciona diversos processos, onde cada módulo é responsável pelo seu ponto de lançamento. Iremos utilizar nos próximos passos o processo **000085 - Fechamento Mensal da folha - verba:**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048504254)

9) Ao abrir o processo temos as opções para configuração dos lançamentos:*![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049396493)*

**OBS:** Os índices na configuração dos lançamentos respeitarão os índices da **tabela SRD**: *![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016735922)*Sendo:  
**1: Centro de custos (conforme cadastro acima)**  
**B/11: Centro de custos + Item + Classe Valor**

Essa configuração pode ser utilizada  para validação da folha rateada por centro de custos, item contábil, classe valor ou ambas.

**ATENÇÃO:** As configurações mostradas nos *prints* servem apenas para ilustrar o processo. Realize a configuração de acordo com a regra de negócio da sua empresa. 

10) Em seguida no módulo Gestão de Pessoal, gere o cálculo da folha de pagamento pelo caminho **Miscelânea ->Cálculos ->Por Roteiros:**   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049582373)

11) Relatório do cálculo de folha referente à competência:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049584153)

12) Vamos configurar as verbas 112 - 318 - 417 - 708 - 713 - 748 - 749, como exemplo, para geração do fechamento com PCO ativo. Acesse **Atualizações -> Definições de cálculo -> Verbas** , aba**Contabilização**, campo **RV\_LANCPCO**, e inclua o item do PCO configurado:  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048692454)

13)  Acesse **Miscelânea -> Fechamentos -> Períodos** e execute o fechamento do período.![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049718433)

14) Durante o fechamento será apresentada a janela de Configuração *online* de lançamentos do PCO para confirmação:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048821794)

No módulo 57 - Planejamento e Controle Orçamentário, acesse **Atualizações -> Movimentos -> Lançamentos**e verifique os lançamentos das verbas de acordo com a configuração realizada:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049723633)

Veja que as verbas e valores estão de acordo com o relatório de folha (item 11):  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048824074)  
  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
