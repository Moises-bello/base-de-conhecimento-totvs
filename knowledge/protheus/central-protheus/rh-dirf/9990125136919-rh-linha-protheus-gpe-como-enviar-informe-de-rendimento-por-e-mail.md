---
article_id: 9990125136919
category: RH – DIRF
content_hash: c1ca5de324fb3572a953da78f059d1b5a7005edab0faa086b55be913a72d7419
fetched_at: '2026-06-28T22:44:06.860328+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como Enviar Informe de Rendimento por E-mail
type: support-article
updated_at: '2025-06-16T20:11:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9990125136919-RH-Linha-Protheus-GPE-Como-Enviar-Informe-de-Rendimento-por-E-mail
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32853962719767)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como enviar o Informe de Rendimentos no formato HTML para o e-mail do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Solução**Foi disponibilizado uma nova opção no parâmetro "Tipo de formulário" para que seja feito o envio via e-mail no formato HTML em lote.  
  
Para que o Informe de Rendimento seja enviado por e-mail para os Funcionários, na rotina **Funcionários**, na aba **Cadastrais**, o campo **E-mail Principal** tem que ter um e-mail cadastrado;  
  
Após isso, entre na rotina **Informe de rendimento** pelo caminho **>Miscelânea >Dirf >Informe de rendimento**;  
Preencher o parâmetro **“Tipo de Formulário” = E-mail** e os demais parâmetros de acordo com a sua necessidade de envio:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22006013734039)  
  
Clique em “Ok”, o sistema irá processar os informes de rendimentos e enviar para o e-mail cadastrado na rotina Funcionários, no campo E-mail Principal (RA\_EMAIL).  
  
O informe rendimento será enviado anexo ao e-mail, com a descrição **Informe de Rendimentos Referente ao ano de 2023** (ou ano calendário em questão), conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22005990551063)

Para visualizar o informe, baixe o arquivo e abra o mesmo, o informe será aberto no navegador:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22005990563351)

**IMPORTANTE:** O ambiente precisa estar atualizado com o último [RH ACUMULADO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854) e rodar o UPDDISTR.

**Observações**1. No envio do Informe de Rendimentos por e-mail, para que o logo seja impresso, é necessário salvar o logo na mesma pasta que o informe de rendimentos, para que seja exibido corretamente ([Saiba mais](https://tdn.totvs.com/display/public/PROT/16389506+DRHCALCPRT-7805+DT+Informe+de+Rendimentos+por+e-mail+sem+o+logo+da+Receita+Federal)).  
2. Melhoria disponibilizada apenas para envio do informe de rendimento por e-mail para Funcionários que estejam cadastrados na rotina Funcionários no GPE.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Configuração de envio de informações por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1aAPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA1NjA1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kZS1lbnZpby1kZS1pbmZvcm1hJUMzJUE3JUMzJUI1ZXMtcG9yLWUtbWFpbAY7CFQ6DnNlYXJjaF9pZEkiKWQ4Mjg5NjMxLTUyYWMtNDcxOS1hZDRhLTZiMmM0NTc0ZDI4MQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiKlJIIC0gTGluaGEgUHJvdGhldXMgLSBlbnZpbyBwb3IgZW1haWwGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--043fe9530b6000539a0e65553766193fa6162521)  
[RH - Linha Protheus - GPE - Como incluir a logo da Receita Federal no Informe de Rendimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002273481-RH-Linha-Protheus-GPE-Como-incluir-a-logo-da-Receita-Federal-no-Informe-de-Rendimentos?source=search)
