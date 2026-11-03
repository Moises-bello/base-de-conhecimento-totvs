---
article_id: 360057868013
category: RH - Definições de Cálculo
content_hash: 10285ea27b7dc03e8eae6d419643d567dcc65cc8be751019f70bd3aa5ae27265
fetched_at: '2026-06-28T22:43:22.419261+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o bloqueio de lançamentos em determinado
  período
type: support-article
updated_at: '2025-08-20T19:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057868013-RH-Linha-Protheus-GPE-Como-realizar-o-bloqueio-de-lan%C3%A7amentos-em-determinado-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31647905575063) Tempo aproximado para leitura: 00:02:00 min**  
**Dúvida**Como realizar o bloqueio de lançamentos em determinado período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o sistema realize o **bloqueio** corretamente, primeiramente o **Sistema Operacional** deve estar com a **data dentro do período de bloqueio**, por exemplo: bloqueio parametrizado para 20/08 à 31/08, neste caso, a data do Sistema Operacional deve estar dentro do mês 08.   
  
O parâmetro **MV\_BLOQSEM** foi criado para bloquear a manutenção de horas/valores nas seguintes  
rotinas:  
**> Lançamento Mensal:** Atualizações/Lançamentos/Mensal (GPEA090)  
**> Lançamento por Verba:** Atualizações/Lançamentos/Por Verba (GPEA100)  
**> Lançamentos Futuros:** Atualizações/Lançamentos/Futuros (GPEA110)  
**> Lançamento de Tarefas:** Atualizações/Lançamentos/Tarefas (GPEA190)  
**> Lançamento de Valores Extras:** Atualizações/Lançamentos/Valores Extras (GPEA230)  
**> Cálculo de Folha:** Miscelânea/Cálculos/Folha (GPEM020)  
**> Cálculo de Férias:** Miscelânea/Cálculos/Férias (GPEM030)  
**> Cálculo de Rescisão:** Miscelânea/Cálculos/Rescisão (GPEM040)  
**> Cálculo de Férias Coletivas/Programadas:** Miscelânea/Cálculos/Fer. Colet. Progr.  
(GPEM060)  
**> Cancelamento de Cálculos:** Miscelânea/Cálculos/Cancel. de Cálculo (GPEM160)  
> **Geração de Verbas:** Miscelânea/Cálculos/Geração de Verbas (GPEM170)  
**> Valores 2ª parcela do 13º salário:** Miscelânea/13º salário/Valores 2ª parcela  
(GPEM260)  
**> Cálculo de Rescisão Coletiva:** Miscelânea/Cálculos/Rescisão Coletiva (GPEM630)  
  
O **MV\_BLOQSEM** pode ser configurado com as seguintes opções:  
**>S (Sim)** - determina a verificação da semana digitada, para então validar a entrada de dados  
**>N (Não)** - determina o bloqueio do acesso às rotinas, não permitindo qualquer tipo de  
manutenção de horas/valores, com exceção da visualização, sendo este o conteúdo padrão do  
parâmetro.  
  
Também foi criado o parâmetro **MV\_BLOQPON** para bloquear a manutenção de horas/valores,  
das verbas originadas do Ponto Eletrônico, nas seguintes rotinas:  
**> Lançamento Mensal:** Atualizações/Lançamentos/Mensal (GPEA090)  
**> Lançamento por Verba:** Atualizações/Lançamentos/Por Verba (GPEA100)  
**> Cancelamento de Cálculos:** Miscelânea/Cálculos/Cancel. de Cálculo (GPEM160)  
**> Geração de Verbas:** Miscelânea/Cálculos/Geração de Verbas (GPEM170)  
**> Cálculo de Rescisão:** Miscelânea/Cálculos/Rescisão (GPEM040)  
  
O **MV\_BLOQPON** pode ser configurado com as seguintes opções “**12345**”, sendo que :  
**> “1” -** determina o bloqueio de manutenção na rotina de Lançamento Mensal (GPEA090)  
**> “2” -** determina o bloqueio de manutenção na rotina de Lançamento por Verba (GPEA100)  
**> “3” -** determina o bloqueio de manutenção na rotina de Cancelamento de Cálculo (GPEM160)  
**> “4” -** determina o bloqueio de manutenção na rotina de Geração de Verbas (GPEM170)  
**> “5” -** determina o bloqueio de manutenção na rotina de Cálculo de Rescisão (GPEM040)  
O conteúdo deste parâmetro deve ser informado em números sequenciais ou não, sem espaços ou  
sinais gráficos, e podem indicar somente algumas das rotinas para bloqueio, por exemplo: “125” ou “35” ou “421” ou “31542”.  
  
Para efetivar o **bloqueio do período**, acesse **Atualizações > Definições de Cálculo >** **Períodos,** selecione o período que deseja bloquear e clique em **Outras Ações** **> Bloqueio:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097345453)  
  
  
O sistema apresentará para bloqueio os roteiros criados para o período selecionado, então se for necessário bloquear lançamentos para o roteiro de Rescisão por exemplo, devemos **criar o roteiro** RES no **cadastro de períodos:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095045594)  
  
  
Após criar os roteiros e entrar no menu **Bloq.Periodos**, os campos devem ser preenchidos corretamente para que seja possível realizar o bloqueio:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095045554)  
  
  
Após a parametrização, será gerada a mensagem abaixo nas rotinas:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095048954)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar bloqueio de período na rotina GPEA400 - Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053486853-RH-Linha-Protheus-GPE-Como-configurar-bloqueio-de-per%C3%ADodo-na-rotina-GPEA400-Cadastro-de-Per%C3%ADodos)
