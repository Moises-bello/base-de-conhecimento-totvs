---
article_id: 360020139292
category: Call Center - Telecobrança
content_hash: 9a7f52346cdd766c928e020c436b4ef5afd5ea73664cdb27b4aafbb525768ade
fetched_at: '2026-06-28T22:41:28.619587+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGATMK - Schedule Seleção de Títulos
  (TMKA180) '
type: support-article
updated_at: '2024-04-25T12:47:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020139292-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Schedule-Sele%C3%A7%C3%A3o-de-T%C3%ADtulos-TMKA180
---

**Dúvida**

Como configurar Schedule para geração automática da seleção de títulos?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

**Procedimentos para Utilização do Schedule**:

1. No módulo **Configurador (SIGACFG)** acesse as opções: "Ambientes" e "Schedule"

2. Na pasta "**Schedule**", selecione as opções "Agent" e "Cadastro", selecione a opção "Incluir", conforme imagem abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12610702398615)  
(Selecione a opção no browser "(abrir imagem em uma nova guia para uma melhor visualização)".

3. Realize o preenchimento das informações. Ou acesse a opção no canto superior direito  "Adicionar agents padrões", para o preenchimento automático dos campos, conforme imagem:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12610433834647)

4. Selecione a opção de "Agendamento" e a opção "Cadastro":  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12610861629975)

5. Informe **"Usuário"** (XX1\_USERID).  
  
6. Informe no campo "**Rotina"** (XX1\_ROTINA)  a chamada **TMKA185** e os **parâmetros**.

Quanto aos parâmetros **(PARAM1, PARAM2, PARAM3, PARAM4, PARAM5),** devem ser preenchidos conforme abaixo:

* **PARAM1** = Este parâmetro deve ser substituído pela empresa que se está executando. Exemplo:  01;
* **PARAM2** = Este parâmetro deve ser substituído por uma filial válida da empresa selecionada no **PARAM1**;
* **PARAM3** = Parâmetro que correspondente à pergunta **Filial De** do programa TMKA180.
* **PARAM4** = Parâmetro que correspondente à pergunta **Filial Até** do programa TMKA180.
* **PARAM5** = Parâmetro correspondente à pergunta **Gerar Log** do programa TMKA180. Informe **1** para Não, e **2**para Sim.

**Exemplo de utilização:** Para a Empresa 99 ,Filial 01, com Filtro de branco á zz e Geração de log ativada, o campo "Rotina" (XX1\_ROTINA) deve ser preenchido da seguinte forma:

**TMKA185("99","01","  ", "zz","2").**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12720270169111)**7. Realize o preenchimento dos demais campos "Data" (XX1\_DATA), "Hora" (XX1\_HORA), "Ambiente" (XX1\_ENV),"Empresa/Filial" (XX1\_EMPFIL), "Modulo" (XX1\_MODULO) e marque o campo "Habilitada" .

Segue abaixo um modelo para utilizar como referencia no cadastro do agendamento:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12613807889943)

8. Configure os agendamentos de acordo com sua necessidade, selecionando a opção "Recorrência", conforme imagem abaixo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12613387789207)  
  
10. Confirme a operação.

**Observações relevantes para configuração:**

* A Frequência, Data, Hora de início, intervalo entre uma execução e outra, **Data** e **Hora final** e o número de tentativas, em caso de inconsistências
* É imprescindível que a empresa seja aquela em que o programa será executado, e o segundo parâmetro corresponda a uma filial que exista e seja válida na empresa selecionada.
* No campo **Ambiente** deve ser informado o ambiente que o processo será executado. Recomenda-se um repositório exclusivo para execução de agendamentos por Schedule.
* É recomendada a criação de um usuário específico para a execução do Job.

**Saiba mais:**

* **[TMK0049 Schedule Seleção de Titulos TMKA180](http://tdn.totvs.com/pages/viewpage.action?pageId=286746024)**
* **[MP - FRAME - AppServer dedicado para o Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029081192-MP-FRAME-AppServer-dedicado-para-o-Schedule)**
* **[MP - FRAME - Schedule: agendando a execução de rotinas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028340252-MP-FRAME-Schedule-agendando-a-execu%C3%A7%C3%A3o-de-rotinas)**
