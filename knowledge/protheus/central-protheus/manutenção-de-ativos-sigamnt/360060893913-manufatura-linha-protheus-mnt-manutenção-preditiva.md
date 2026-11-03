---
article_id: 360060893913
category: Manutenção de Ativos (SIGAMNT)
content_hash: f303b67008b26b2615e986cf444f0beab1a699b9a83abe2107995cdb1a4d6f1f
fetched_at: '2026-06-28T22:42:34.231338+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Manutenção Preditiva
type: support-article
updated_at: '2021-07-05T20:31:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060893913-Manufatura-Linha-Protheus-MNT-Manuten%C3%A7%C3%A3o-Preditiva
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:05:30 min**  
**Dúvida**Como utilizar o conceito de **Manutenção preditiva** no **Protheus**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Na manutenção, o conceito de **Manutenção preditiva** já existe há algum tempo. Sendo uma das modalidades da manutenção, se tornou uma importante ferramenta para o aumento da produtividade.  
  
A **Manutenção preditiva**, dentro da área de manutenção, é um método que tem por finalidade indicar quais são as reais condições de funcionamento dos equipamentos, baseando-se em dados sobre seu desgaste e/ou processo de degradação. Esse tipo de manutenção tem por objetivo monitorar regularmente as condições mecânicas, eletrônicas, pneumáticas, hidráulicas e elétricas dos equipamentos e instalações através de dados coletados por meio da monitoração ou de inspeções. De uma forma mais simples, pode-se afirmar que essa modalidade de manutenção possui a capacidade de predizer o tempo de vida útil dos componentes dos ativos e as condições para que esse tempo de vida útil seja melhor aproveitado.  
  
Dessa forma, a **Manutenção preditiva** possui os objetivos de determinar de forma antecipada a necessidade de serviços de manutenção em peça/componente de um determinado ativo, eliminar o serviço de desmontagens desnecessárias para inspeção, aumentar o tempo de disponibilidade dos ativos, reduzir as manutenções corretivas, as paradas emergenciais, aumentar a vida útil dos ativos e seus componentes, bem como aumentar o grau de confiabilidade no desempenho dos ativos.  
  
**Como aplicar esses conceitos no Protheus SIGAMNT?**É necessário ter cadastrado um **Serviço Preventivo** no programa de **Cadastro de Serviço - MNTA040**, localizado em: **Atualizações / Controle de Oficina / Manutenção / Serviços - Incluir um s****erviço**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000629441/mceclip0.png)

Com o serviço criado, é necessário criar uma **Etapa** que indique qual é o limite de uso do ativo ao qual se quer aplicar o conceito, para tanto é necessário acessar o programa de **Etapas Genéricas - MNTA015,** localizado em **Manutenção de Ativos / Atualizações / Controle de Oficina / Manutenção / Etapas Genéricas**.   
Clique em incluir e informe no cabeçalho os dados para a **Manutenção preditiva**. Criar um **Código** e a **Descrição da etapa** e definir quais os parâmetros que irão gerar uma **Manutenção preditiva**. Por exemplo, um equipamento, que deve ter um nível mínimo de óleo para operar em boas condições, conforme vai baixando o nível de óleo o equipamento opera em menor qualidade, bem como se deteriora mais rapidamente, levando ele a um conserto, ou seja, manutenção corretiva, ativo parado por mais tempo para troca de peças etc. Pode-se criar uma etapa, indicando que se o nível de óleo tiver abaixo de 50ml, então deverá realizar a troca.  
Na aba **Dados das Opções** informar os campos conforme *help*. O campo **Fórmula** pode ser preenchido de forma manual, ou com auxílio da consulta padrão. A **Fórmula** para indicar uma **Manutenção preditiva** é criada pelas informações dos campos. As opções são: **Sem Ação**, **Gera OS** e **Gera SS**. O que definirá se será corretiva ou preventiva é a característica do **Tipo de manutenção** utilizado no serviço.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101715393/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000630801/mceclip2.png)

Caso seja selecionada uma opção que gere **O.S. - Ordem de serviço** preventiva, é necessário ter cadastrado um tipo de manutenção para o bem para isso é necessário acessar o programa de cadastro de **Tipos de Manutenção - MNTA110**, localizado em: **Atualizações / Controle de Oficina / Manutenção / Tipos Manutenção - Incluir um tipo de Manutenção**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000615522/mceclip3.png)

A **Manutenção preditiva** pode ser gerada através de uma **Manutenção corretiva** ou **preventiva**.  
  
1. Manutenção corretiva:  
Incluir uma **O.S. corretiva - MNTA420**. Para isso acesse: **Atualizações / Controle de Oficina / Ordem de Serviço / Corretiva - Incluir uma OS**, informando o **Bem** e o **Serviço** corretivo. Marcar a **O.S.** como liberada. Clicar na opção **Etapas** e informar a **Etapa genérica**, que foi cadastrada anteriormente.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101716873/mceclip4.png)

2. Manutenção preventiva:  
Para gerar uma **O.S Preditiva** via uma **Manutenção preventiva**, é necessário ter uma **Manutenção - MNTA120** cadastrada, para tanto deve-se acessar: **Atualizações / Controle de Oficina / Manutenção / Manutenção - Incluir uma manutenção para o bem/serviço**.  
Cadastrar a **Manutenção preventiva** para o **Bem**. Na aba **Etapa** deve ser incluído a **Etapa** **preditiva**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000631421/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000615842/mceclip6.png)

Incluir uma **O.S preventiva**, acessando o cadastro de **O.S Manual - MNTA410** em **Atualizações / Controle de Oficina / Ordem de Serviço / Manual - Selecionar a manutenção preventiva e incluir uma OS**, marcar a mesma como **Liberada**, e verificar que na opção **Etapas** está informada a **Etapa preditiva**.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101717213/mceclip7.png)

Após a inclusão da **O.S**. seja corretiva ou preventiva deverá ser efetuado o retorno da mesma, para esse processo pode ser utilizado o programa **Retorno Mod. 2 - MNTA435**. Para isso é necessário acessar: **Atualizações / Controle de Oficina / Retorno O.S. / Retorno Mod. 2**: 

* Procure a **O.S.** criada.
* Selecione a aba **Etapas.**
* Marque a **Opção** desejada, e informe o **Valor**.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099504754/mceclip8.png)

Fazer a finalização da **O.S**, caso a **Etapa** informe a possibilidade de um problema para o ativo, irá gerar uma nova **O.S**.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000617382/mceclip9.png)

A nova **O.S** é gerada com a situação **Pendente**, para liberar a mesma é possível acessar o programa de **Liberação de O.S - MNTA490** em **Atualizações / Controle de Oficina / Plano Manutenção / Liberação de O.S. / Selecionar a O.S e salvar**.
