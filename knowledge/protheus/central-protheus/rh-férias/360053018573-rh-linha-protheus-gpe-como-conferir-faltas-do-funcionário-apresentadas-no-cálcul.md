---
article_id: 360053018573
category: RH - Férias
content_hash: 9d2c7f971bd151059b099d5e8ee6e0e08ac67e32bc08f1a02303a59cbc52ccbf
fetched_at: '2026-06-28T22:43:57.899315+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE -  Como conferir Faltas do Funcionário apresentadas
  no cálculo de Férias
type: support-article
updated_at: '2025-09-02T18:37:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053018573-RH-Linha-Protheus-GPE-Como-conferir-Faltas-do-Funcion%C3%A1rio-apresentadas-no-c%C3%A1lculo-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23718224045079)** Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**  
Como conferir a quantidade de **Faltas** no **Cálculo de Férias**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A busca de **Faltas** é feita diretamente no **acumulado** do Funcionário (SRD) e as Faltas devem estar **dentro do período aquisitivo das Férias que estão sendo calculadas.**As **verbas** que podem ser usadas para faltas são: **• 0054 -** Desconto de Faltas (tipo dias ou horas) **• 0055 -** Desconto de Atrasos (tipo horas) **• 0203 -** Desconto de falta mês anterior (tipo dias ou horas) **• 0242 -** Desconto de Faltas II (tipo dias ou horas) **• 0243 -** Atrasos II (tipo horas)  
  
Além destes, temos os Id's de cálculo para **abono de faltas e atrasos** que são:  
**• 0244** - Reembolso de Faltas (tipo dias)  
**• 0245** - Reembolso de Atrasos (tipo horas)  
  
Além disso, as verbas devem estar configuradas como **S** no campo **RV\_MEDFER - Méd. Fer,** no Cadastro de Verba (GPEA040), para que as Faltas sejam buscadas **dentro do período aquisitivo.**  
Existindo estas verbas nos **acumulados,** o sistema **proporcionaliza** no cálculo de Férias, deduzindo gradativamente os dias de direito quando existirem **faltas/atrasos superiores** **a** **cinco dias** conforme tabela abaixo:

**![](http://tdn.totvs.com/download/attachments/233740211/ferias.png?version=1&modificationDate=1457631855000&api=v2)**

**Conferência:** **1**. Abra o **cadastro de Verbas** em **Atualizações > Definições de Cálculo >Verbas** e verifique o **código da Verba** que possui os **id's** de cálculo mencionados acima (por exemplo: 0054):

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085574793)

**2.** Faça uma **consulta** do acumulado dos funcionários (tabela **SRD)** através do menu **Consultas > Cadastros > Genéricos:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085574313)

**3.** Clique em **Exportar XML** com a opção **MS Excel** e clique em C**onfirmar** para abrir o arquivo em tela:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084395874)

**4.** Faça um **filtro** na coluna **Código Verba** de acordo com os códigos verificados anteriormente no passo **1:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084395914)

**5.** Verifique os valores informados para a matrícula que está realizando a conferência e para qual **mês** os **lançamentos** se referem.  
  
**Observação:** Se as faltas forem lançadas em horas, o sistema faz uma conversão das horas em dias para serem consideradas no cálculo das Férias. Para isso, o sistema usa o campo **Horas Dia** do Cadastro do Funcionário, seguindo a seguinte fórmula: **TOTAL HORAS FALTAS DO PERÍODO / CAMPO HORAS DIA.**  
**Exemplo:** o funcionário tem um total de 51,33 horas de faltas no acumulado para o período aquisitivo, e no cadastro dele o campo Horas Dias esta preenchido com 7,3333. Para chegar ao total de faltas, será feito o seguinte cálculo: **51,33 / 7,3333 = 7,** portanto, serão considerados **7 dias de faltas.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10964010730647)**

**Importante:**O **abono** das faltas só será possível se for lançado no acumulado do funcionário **dentro do período aquisitivo** que está sendo calculado. Do contrário, as faltas serão demonstradas na rotina de **Férias (GPEM030)** e poderão ser alteradas **manualmente** pelo usuário **antes** de calcular as férias.  
Através da rotina de **Férias Coletivas/ Programadas, não** é possível ajustar o número de faltas.

**Saiba mais**[RH - Linha Protheus - GPE - Como não abater as faltas justificadas das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwif%2FabSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjQ0NDgzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1uJUMzJUEzby1hYmF0ZXItYXMtZmFsdGFzLWp1c3RpZmljYWRhcy1kYXMtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIik5MGY1ZmM1MC05ZTdiLTQ0OGYtYTJmNy04ODc4YjkwMDFhZDQGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlRSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBuw6NvIGFiYXRlciBhcyBmYWx0YXMganVzdGlmaWNhZGFzIGRhcyBmw6lyaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--fefacf1f8f77c5a4e04ed3670b5eb62e4f63eed4)   
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZUsrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjMxNDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWxhdCVDMyVCM3Jpby1kZS1tZW0lQzMlQjNyaWEtZGUtYyVDMyVBMWxjdWxvLWRhcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKWE2ZDFlNGZlLTkwYjAtNDE4Zi1hZTRlLWU5NTVkOTZmNTAwNAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGG1lbW9yaWEgZGUgY8OhbGN1bG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--e4ff2782a4a934d5dfd273d712d9ba1a3597d722)  
[RH - Linha Protheus - GPE - Dias de Faltas injustificadas não estão abatendo nas Férias da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhrFarSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjY0NzUzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRGlhcy1kZS1GYWx0YXMtaW5qdXN0aWZpY2FkYXMtbiVDMyVBM28tZXN0JUMzJUEzby1hYmF0ZW5kby1uYXMtRiVDMyVBOXJpYXMtZGEtUmVzY2lzJUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKWExYmI3MGU1LTM0NWMtNGE0OS04MDk0LWE4OGNhYWIwZmJkNQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkibFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBEaWFzIGRlIEZhbHRhcyBpbmp1c3RpZmljYWRhcyBuw6NvIGVzdMOjbyBhYmF0ZW5kbyBuYXMgRsOpcmlhcyBkYSBSZXNjaXPDo28GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--7324aad66232ea754319818ae22885e755909b98)  
[RH - Linha Protheus - GPE - Sistema está considerando as faltas para abatimento de avos mesmo alterando a quantidade na rotina de Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhteNLTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB4mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNjA3MTUzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU2lzdGVtYS1lc3QlQzMlQTEtY29uc2lkZXJhbmRvLWFzLWZhbHRhcy1wYXJhLWFiYXRpbWVudG8tZGUtYXZvcy1tZXNtby1hbHRlcmFuZG8tYS1xdWFudGlkYWRlLW5hLXJvdGluYS1kZS1Db250cm9sZS1kZS1EaWFzLWRlLURpcmVpdG8GOwhUOg5zZWFyY2hfaWRJIikwN2YzN2ZjNy1hMDdkLTRlODgtODkwNy04ZDE1ZDhkOWMwM2YGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGeUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFNpc3RlbWEgZXN0w6EgY29uc2lkZXJhbmRvIGFzIGZhbHRhcyBwYXJhIGFiYXRpbWVudG8gZGUgYXZvcyBtZXNtbyBhbHRlcmFuZG8gYSBxdWFudGlkYWRlIG5hIHJvdGluYSBkZSBDb250cm9sZSBkZSBEaWFzIGRlIERpcmVpdG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--9f3907099204f396ed341c713f868146abfcfca0)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
