---
article_id: 6218136002071
category: RH - Provisão
content_hash: aeb37aa5ed12e6ce0009df1d30fdfded8212b5b15438dcbf5c36619c1ddb5275
fetched_at: '2026-06-28T22:43:56.911898+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração e geração PCO (processo 000091 - Provisão
  de Férias/13.Salario)
type: support-article
updated_at: '2024-08-13T10:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6218136002071-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-PCO-processo-000091-Provis%C3%A3o-de-F%C3%A9rias-13-Salario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25579681205399) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como configurar e gerar o processo de PCO 000091 - Provisão de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Para efetuar a configuração de **geração do PCO** das Provisões de Férias e 13º Salário realize os seguintes procedimentos: 

1.Como premissa para integração com o módulo SIGAPCO, configure o parâmetro **MV\_PCOINTE = 1** , ativando a integração.  
Acesse: Configurador (SIGACFG) / Ambiente / Cadastros / **Parâmetros**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6216491976087)**

2. Acesse o Módulo Planejamento e Controle Orçamentário (Módulo 57) / Atualizações / Cadastros / **Contas Orçamentárias**.

A conta orçamentária é o principal item da estrutura organizacional para elaboração das planilhas orçamentárias da empresa e é a base/guia para o detalhamento dos itens que se quer orçar.

O detalhamento e o conhecimento dos objetivos do planejamento e controle orçamentário da empresa são essenciais para cadastrar um plano de contas orçamentário.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6216680474519)

3. Acesse: Atualizações / Cadastros / **Operações**.  
Esta rotina responde pelo cadastramento e pela manutenção das operações que podem ser utilizadas na digitação e acompanhamento da planilha orçamentária.*![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6216745682071)*

4. Acesse: Atualizações / Cadastros / **Classes**.  
A classe orçamentária permite organizar o orçamento segundo critérios que permitem compreender os tipos de valores que estão sendo apresentados. Propiciando informações para a administração, gerencia e a tomada de decisões.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6216780183703)

5. Acesse: Atualizações / Cadastros / **Tipos de Saldos**.

Podemos entender como saldo, toda e qualquer diferença de valores entre crédito e débito, em relação aos saldos iniciais de uma determinada conta orçamentária, em um determinado período.

A classificação dos tipos de saldos é de extrema importância, já que identifica os movimentos orçamentários contabilizados dentro do contexto definido pelo gestor do orçamento.

Este cadastro é utilizado para efetuar a criação e a manutenção dos tipos de saldos utilizados durante o acompanhamento do ciclo orçamentário:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6217178619031)

6. Acesse: Atualizações / Lançamentos / **Pontos de Lançamento /** Localize o processo **000091** através do Filtro e clique em Lançamentos  
O módulo nos proporciona diversos processos, onde cada módulo é responsável pelo seu ponto de lançamento. Iremos utilizar nos próximos passos o processo **000091 - Provisão de Férias/13.Salario**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6217620656919)**

****ATENÇÃO:**** As configurações mostradas nos *prints* servem apenas para ilustrar o processo. Realize a configuração de acordo com a regra de negócio da sua empresa.

7.  Em seguida acesse o Módulo Gestão de Pessoal (módulo 07), e Processe o Cálculo da Folha de Pagamento dos funcionários.  
  
8. Acesse: Miscelânea / Provisões / **Provisão de Férias/13º Salário** / Outras Ações / Cálculo e preencha os parâmetros para Cálculo das Provisões.  
  
9. Totais do Relatório de Provisão de Férias e 13º Salário:  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6218240124055)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6218307102231)

10. No módulo 57 - Planejamento e Controle Orçamentário, acesse Atualizações / Planilhas / **Lançamentos (PCOA050)** e verifique os lançamentos das provisões:  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6217980678167)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
