---
article_id: 9625796554391
category: RH - Relatórios
content_hash: 324ada8f42fe73f13443ce6e4a06156d28e8090c10add8f20704d666429a9eff
fetched_at: '2026-06-28T22:44:43.576273+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Gráfico de Horas Realizadas PONM020
type: support-article
updated_at: '2025-09-05T19:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9625796554391-RH-Linha-Protheus-PON-Gr%C3%A1fico-de-Horas-Realizadas-PONM020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32102084082199) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Utilização do **Gráfico de Horas Realizadas** - PONM020.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução****1. Visão Geral:**O **Gráfico de Horas Realizadas (Miscelanea>Gráficos>Horas Realizads),** tem como objetivo **exibir** diversos tipos de gráficos **totalizando as horas dos funcionários** e **dividindo em porcentagens** o **tipo de hora realizada.  
Exemplo:** o **total de horas** de um funcionário no mês foi de **100h**, sendo que **80h** foram **Horas Normais Trabalhadas**, **10h** foram referentes a **Hora Extras** e **10h** **Noturnas**, portanto, na divisão teremos **80% das horas como Horas Normais**, **10%** de **Horas Extras** e **10%** de **Horas Noturnas**.   
  
No **total, o Gráfico de Horas Realizadas** exibe **7 tipos de eventos do ponto**, que são:  
**-> Horas Normais**  
**-> Horas Noturnas**  
**-> Horas Extras**  
**-> DSR**  
**-> Faltas**  
**-> Atrasos**  
**-> Saída Antecipada****Observação:** O gráfico **só exibirá as informações do período aberto**, ou seja, **apenas o eventos presentes na tabela SPC serão exibidos**.  
  
**2. Configuração:**Para que o **gráfico consiga exibir os dados**, será necessário realizar algumas **configurações** nos **Eventos** do Ponto, **Tipos de Horas Extras** e na **Regra de Apontamento** para que **sejam gerados** os **apontamentos no período.  
  
2.1** Em **Atualizações>Cadastro do Ponto>Regra de Apontamento:** os campos **Pg.Hrs.Norm.** e **Pg.DSR** devem estar **= SIM:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649431575703)  
  
**2.2** Em **Atualizações>Cadastro do Ponto>Eventos:** para a **configuração dos eventos** é preciso que eles sejam **identificados** através do **Identificador do Ponto (ID Ponto),** conforme exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649450794519)  
**Eventos Autorizados e Não Autorizados:  
- Horas Normais (001A);  
- DSR (002A);****- Adicional Noturno (003N)** e **(004A);**  
**- Falta 1/2 Período (007N)** e **(008A);**  
**- Falta (009N)** e **(010A);**  
**- Atraso (011N)** e **(012A);**  
**- Saída Antecipada (013N)** e **(014A);**  
**- Saída Expediente (019N)** e **(020A);  
  
2.3** Em **Atualizações>Cadastro do Ponto>Tipos de Horas Extras:** abaixo, temos um **e****xemplo** de **configuração do tipo de hora extra normal**, mas será **necessário** realizar a **mesma configuração** para os **demais tipos: DSR, Compensada, Feriado e os pares Noturnos**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649466024471)  
  
**Eventos Utilizados:  
- Hora Extra Autorizada:**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649484824471)  
  
**- Hora Extra Não Autorizada:**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649488914455)  
  
**3- Exemplos de utilização:**Neste exemplo, foi utilizado a [**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) **(Atualizações>Cadastro do Ponto>Tabela de Horário Padrão)** onde o funcionário realiza marcações **noturnas** em todas as sextas-feiras.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32102099986711)  
  
**3.1 Em** **Atualizações>Lançamentos>Apontamentos**::![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649657365271)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649685928727)

**Apontamentos:****001 -** HE 50% AUT: 2 Horas  
**101 -** Horas Normais: 36 Horas  
**100 -** Horas Noturnas Normais: 4:34 Horas  
**011 -** Hora Extra Compensada: 1 Hora  
**055 -** Hora Extra DSR: 1 Hora  
**102 -** DSR: 7:20 Horas  
**104 -** Falta Meio Período: 5  
**112 -** Falta: 8 Horas  
**433 -** Atrasos: 30 Minutos  
**478 -** Saída Antecipada: 30 Minutos  
  
**Total de Horas**O **total** será **composto pelos apontamentos** mencionados anteriormente, ou seja, **serão somados** tanto os **proventos (Horas Normais, Horas Noturnas, Hora Extra e etc.)** como os **descontos** (Atraso, Falta Saída Antecipada e etc.). **Somando todos os eventos** teremos no total **65:54 Horas.**Para acessar o **Gráfico de Horas Realizadas,** acessar: **Miscelânea -> Gráficos -> Horas Realizadas**.  
Nos **parâmetros**, temos as seguintes perguntas:

**-> Calcular Por:** Ordenação da **tabela de funcionários**, nesta pergunta teremos **3 opções: Filial, Centro de Custo e Matricula.** Ao selecionar **qualquer uma das opções,** a **diferença** será na **ordenação dos funcionários**, caso seja selecionada a **opção Filial**, então o processamento será feito **primeiro com a filial A, depois filial B e assim sucessivamente**. Se for a **opção Centro de Custo,** a **ordenação será Filial + Centro de Custo**, e por fim se for a **opção Matricula**, a **ordenação será Filial + Matrícula**. **Qualquer uma das opções não altera o resultado do gráfico.****-> Filial De e Até:**, Filtro das **filias** que serão **consideradas** para a **montagem do gráfico**.  
**-> Centro de Custo De e Até:** Filtro dos **Centros de Custos** que serão **considerados** para a **montagem do gráfico.****-> Matricula De e Até:** Filtro das **matrículas** que serão **consideradas** para a **montagem do gráfico**.  
**-> Data De e Data Até: Período** que será **utilizado** para **buscar os eventos** gerados para a **montagem do gráfico.**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649730098583)  
  
Na **montagem do gráfico** abaixo, teremos o **total** de **cada evento** e sua **respectiva porcentagem**. No caso das **Horas Normais**, por exemplo, temos um **total de 36 Horas Normais,** e o total de **horas realizadas** pelo funcionário é de **65:54 horas**, portanto, **36 Horas Normais equivalem a 55,27%** das **horas realizadas**. O sistema fará o **calculo** separadamente para **cada evento** e posteriormente exibe as porcentagens dos eventos:  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649692506135)  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649761435543)  
  
No **Menu**superior, é possível **selecionar** diversos **tipos de gráficos** clicando em cada um deles.  
O **resultado será o mesmo**, apenas o **tipo do gráfico será alterado**:  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649753620247)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9649755174039)  
  
**Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
