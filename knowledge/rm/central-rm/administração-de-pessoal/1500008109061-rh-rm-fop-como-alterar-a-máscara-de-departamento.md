---
article_id: 1500008109061
category: Administração de Pessoal
content_hash: 663762d2722967ef0461e0859319ed1359084f44ab26e0d320b176066bf0c8ff
fetched_at: '2026-06-28T22:47:02.167630+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP -  Como Alterar a Máscara de Departamento
type: support-article
updated_at: '2025-03-12T10:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008109061-RH-RM-FOP-Como-Alterar-a-M%C3%A1scara-de-Departamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00min**

**Dúvida**Como faço a alteração da máscara do cadastro de departamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Antes de mais nada, é importante informar que não é possível alterar máscaras do Departamentos via produto uma vez que as mesmas já foram definidas. Diante disso, a **saída de contorno** será a alteração via banco de dados. Para isso, é necessário o apoio de seu setor especializado em banco de dados ou até mesmo por meio de nossa Consultoria, se desejar.

Recomendamos que seja realizado o processo inicialmente e uma **base de homologação**, para posteriormente ser replicada na **b****ase de produção** após validação realizada na base de teste.

A alteração na máscara influenciará todos os demais departamentos já cadastrados na base. Será necessário ajustar todos os departamentos para que fiquem de acordo com a máscara informada.  
  
**Tabela**: GDEPPAR  
**Campo:** MASCARADEP  
 **Importante**Lembre-se de que qualquer ação realizada em seu banco sem conhecimento técnico adequado e profundo conhecimento do produto, poderá implicar em resultados danosos para a integridade de sua base de dados.

Caso não tenha segurança para executar determinadas ações, entre em contato com o serviço de Consultoria da Totvs!  
  
**Saiba mais**  
Para criar um banco de homologação: [RM - Frame - Como criar ambiente para homologação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014226872-RM-Frame-Como-criar-ambiente-para-homologa%C3%A7%C3%A3o)
