---
article_id: 360043029374
category: RH – DIRF
content_hash: 0ee721451052543d4cfeea91105dad25a1dc5321a8a98a2e7777fc9f7456b867
fetched_at: '2026-06-28T22:44:06.923364+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como preencher os campos de informações complementares,
  para reembolso e coparticipação de assistência médica/odontológica para DIRF
type: support-article
updated_at: '2025-08-19T12:43:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043029374-RH-Linha-Protheus-GPE-Como-preencher-os-campos-de-informa%C3%A7%C3%B5es-complementares-para-reembolso-e-coparticipa%C3%A7%C3%A3o-de-assist%C3%AAncia-m%C3%A9dica-odontol%C3%B3gica-para-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21550840241303)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como preencher os campos de informações complementares, para reembolso e coparticipação de assistência médica/odontológica para DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**1.** Deve ser cadastrar a verba de reembolso e coparticipação com incidência R na aba DIRF, para isso, acesse pelo caminho **>Atualizações >Definições de Cálculos >Verbas,** localize a verba e ajuste na aba **Anuais:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096840814)  
  
**2.** Realize o lançamento dos reembolsos através do caminho **Atualizações > Benefícios > Plano de Saúde > Co-participação/reembolso** (**GPEA003):**

**Campos**:

Data Ocorrência: Informada automaticamente pelo sistema   
Origem: Titular ou dependente  
Tipo: Assis. Médica ou Assis. Odonto  
Cód. Fornecedor: o mesmo utilizado no cadastro do plano de saúde/odonto  
Sequencia: Código dependente. Apenas informar quando a origem for dependente  
Nome: Nome do titular ou dependente que está sendo lançado o reembolso  
Tipo lançamento: Co-participação ou reembolso  
Verba Calculada: Informar  a verba de reembolso ou de co-participação  
Descrição: Referente descrição da verba  
Valor funcionário: Valor da co-participação ou reembolso  
Valor empresa: Se houver o valor parte empresa  
Competência Pagamento: Competência que deve ser gerado o reembolso em folha

![](https://tdn.totvs.com/download/attachments/331864604/image2018-1-23_10-55-19.png?version=1&modificationDate=1516715858000&api=v2)

Após gerar a DIRF, o sistema apresentará o log demonstrando os funcionários que estão com informação de reembolso:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11322469091479)

3. Entre na rotina **Manutenção de Arquivo** pelo caminho **>Miscelânea >Dirf >Manutenção de Arquivo**, localize o funcionário e clique em **Alterar**;  
  
Clique em **>Outras Ações >Informações Complementares** e informe os campos **Prest. (CPF/CNPJ) e Nome Prest.S**, sendo o CPF ou CNPJ e nome do prestador de serviço para o reembolso.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11322541795735)

Confirme a alteração.

Gere o arquivo magnético pelo caminho **>Miscelânea >Dirf >Arquivo Magnético;**

No arquivo deve ser gerado conforme o layout, os códigos abaixo:

**Titular**: RTPSE – Reembolso do titular do plano de assistência à saúde – coletivo empresarial

**Dependente**: RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde – coletivo empresarial para o dependente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11322533886359)

No informe de rendimento a informação sairá com descrição da verba cadastrada para o reembolso.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11322568697623)

**Saiba Mais:  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)**
