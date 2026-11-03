---
article_id: 7726351592855
category: RH - Férias
content_hash: bdffd2a1fb2ad0e9071324615ac6b2d959f820fbab310faa5513d64579be74cc
fetched_at: '2026-06-28T22:43:59.307868+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias
type: support-article
updated_at: '2025-09-22T13:22:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22080796720791) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar o **demonstrativo de médias** para conferencia dos valores de **Médias de Férias?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**

O demonstrativo de médias pode ser gerado diretamente no **Cálculo das Férias (DEM\_MED)** ou na rotina de **Demonstrativo de Médias (GPER080)** para gerar o relatório em lote.  
Indicamos gerar o relatório **diretamente no cálculo**, pois as parametrizações serão geradas automaticamente e sem o risco de informar algum parâmetro incorreto. 

**• Demonstrativo de Médias (DEM\_MED)  
>** Acesse **Miscelânea/ Cálculo/ Férias**, selecione o funcionário e clique em **Outras Ações/ Visualizar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22081095925399)

**>** Na tela de cálculo, clique em **Outras Ações/ Visualizar Médias:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22081108872983)

**• Demonstrativo de Médias via rotina (GPER080)**> Acesse **Relatórios/ Lançamento/** **Demonstrativo de Médias**, clique em **Parâmetros** para preencher o grupo de perguntas.  
  
**- Data Base:** Informe a data de inicio das férias do funcionário  
**- Filial De/Até:** Informe ou selecione o código da Filial Inicial/Final;  
**- Centro de Custo De/Até:** Informe ou selecione o código do Centro de Custo Inicial/Final;  
**- Matricula De/Até:** Informe ou selecione o código de Matrícula Inicial/Final;  
**- Nome De/Até:** Informe ou selecione o Nome do Funcionário Inicial/Final;  
**- Médias De:** Informe sobre qual Rotina deseja imprimir o Relatório de Médias (Férias, 13º Salário, Aviso Prévio, Licença Maternidade ou Todos);  
**- Situações a Imp:** Selecione as Situações dos funcionários que serão exibidos;  
**- Categorias a Imp:** Selecione as Categorias dos funcionários que serão exibidos;  
**- Considera Mês Atual:** Informe se considera para Média o Mês Atual, o Acumulado ou não considera o Mês Atual, somente o Acumulado;  
**- Imprime Média Pgto:** Informe se deseja imprimir a linha "Medias de Pagamento".  
- **Apenas Histórico de Cálculo:** Selecione se serão impressos apenas funcionários que tiveram cálculos (férias e/ou 13º) salvos na tabelas de histórico de médias ou se serão impressos todos os funcionários que possuem médias. Se selecionado "Sim", será impresso exatamente o mesmo relatório que foi gerado no cálculo e se selecionado "Não", será impresso todos os funcionários que possuem médias de acordo com a parametrização do relatório.  
  
**Exemplo:  
![GPER080.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7726451488919)**

**OBS:** existem parametrizações especificas para gerar os valores de médias, portanto, sugerimos que verifique as documentações relacionadas.  
Para auxiliar na conferência dos valores gerados e como está a parametrização do ambiente, gere a [Memória de Cálculo.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058080854-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Mem%C3%B3ria-de-C%C3%A1lculo-no-13%C2%BA)

**Saiba Mais:**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgKFbLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ8aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwNzI2MTU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtbSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIik1M2JjNDQ4Mi0xZTU0LTQ3MTYtYWJhNy01Y2QxYjg0ZDY1NjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjw6FsY3VsbyBkZSBtw6lkaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--cbb28a0877b3f7ce647878c32dbd2838b92ccf23)  
[RH - Linha Protheus - GPE - Histórico de Médias (GPER080)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiCzlzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MTkxNDc1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSGlzdCVDMyVCM3JpY28tZGUtTSVDMyVBOWRpYXMtR1BFUjA4MAY7CFQ6DnNlYXJjaF9pZEkiKWFhOGI4YjI2LTI1MDQtNGIwNC1iMzkwLWEyNmE5MWYyZjllZQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHWRlbW9uc3RyYXRpdm8gZGUgbcOpZGlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--706aaeefec6fb717798bf9e4a7a981280c0abeec)  
[RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual Demonstrativo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024606114-RH-Linha-Protheus-GPE-Coluna-Valor-Original-e-Valor-Atual-Demonstrativo-de-M%C3%A9dias)  
[RH - Linha Protheus - GPE - Como demonstrar o salário Incorporado no Relatório de Médias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgRyX4%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDg4NTk5MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGVtb25zdHJhci1vLXNhbCVDMyVBMXJpby1JbmNvcnBvcmFkby1uby1SZWxhdCVDMyVCM3Jpby1kZS1NJUMzJUE5ZGlhcy1kZS1GJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKWFhOGI4YjI2LTI1MDQtNGIwNC1iMzkwLWEyNmE5MWYyZjllZQY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHWRlbW9uc3RyYXRpdm8gZGUgbcOpZGlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--10a2929f271ec974849818a8b47a15e3572f07b0)
