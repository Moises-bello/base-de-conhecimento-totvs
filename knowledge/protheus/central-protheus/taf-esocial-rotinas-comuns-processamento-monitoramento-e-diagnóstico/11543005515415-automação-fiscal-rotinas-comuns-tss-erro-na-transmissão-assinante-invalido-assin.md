---
article_id: 11543005515415
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 6e16a5337e1d674af12037cce2b952dafc57fe09a1ad150e80769456d46275be
fetched_at: '2026-06-28T22:45:20.857186+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: Automação Fiscal - Rotinas Comuns - TSS - Erro na transmissão,  Assinante invalido.
  Assinante nao possui perfil de procuracao eletronica para enviar este tipo de evento
  ou assinante nao consta como representante legal da empresa.
type: support-article
updated_at: '2026-06-26T12:05:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11543005515415-Automa%C3%A7%C3%A3o-Fiscal-Rotinas-Comuns-TSS-Erro-na-transmiss%C3%A3o-Assinante-invalido-Assinante-nao-possui-perfil-de-procuracao-eletronica-para-enviar-este-tipo-de-evento-ou-assinante-nao-consta-como-representante-legal-da-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23703837300759) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao tentar transmitir os eventos para o eSocial é retornada a mensagem abaixo:

*"Codigo da ocorrência: Descrição: Assinante invalido. Assinante nao possui perfil de procuracao eletronica para enviar este tipo de evento ou assinante nao consta como representante legal da empresa."*  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Rotinas Comuns -Monitor - TSS - Todas as versões  
  
**Solução**1. Certifique-se, com o contador da empresa ou área apropriada, se o certificado configurado no TAF, utilizado pelo TSS, **está autorizado** á transmitir evento para o **eSocial**.

2. Caso tenha dúvidas em como confirmar, acesse o site do eCac - [eCAC - Centro Virtual de Atendimento (fazenda.gov.br)](https://cav.receita.fazenda.gov.br/autenticacao/login) e faça o login com o Certificado

Clique em - Senhas e Procurações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25921296372759)

Consulta por Outorgante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25921319180823)

Veja se o outorgante possui a liberação para a utilização de envio do evento que está tentando enviar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25921319184279)

3. Verifique se o **CNPJ do certificado** é o mesmo da **Matriz**, empresa que transmite os eventos do eSocial.

4. Se o certificado possuir um **CNPJ diferente** da empresa **Matriz**, é necessário que este certificado esteja **autorizado** á realizar transmissão para o CNPJ da Matriz. Chamamos de **Outorga**. Neste caso, é necessário, durante a configuração do certificado do TSS, pela **Wizard de Configuração do TSS**, que o campo ***CNPJ/CPF Transmissor (Dif. do Empregador)***seja preenchido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11542820124823)

5. Se o certificado possuir um **CNPJ igual** ao da empresa **Matriz**, não preencha (deixe sem conteúdo) o campo ***CNPJ/CPF Transmissor (Dif. do Empregador).***

6. Configure novamente o certificado do TSS, pela **Wizard de Configuração do TSS,** corrigindo as informações, caso necessário.

**Documentação:**

[RH - Linha Protheus - TAF - eSocial - Configuração - TSS - CERTIFICADO DIGITAL A3 - Como realizar a preparação do Certificado Digital e configurá-lo no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034171074)
