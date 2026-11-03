---
article_id: 360050562414
category: RH - EAI
content_hash: f0c4c3149ccd6efadc0b73d244da2e47bf27eb6f42451fd5fa53378d064c515d
fetched_at: '2026-06-28T22:43:47.314770+00:00'
product: protheus
section_id: 360001583772
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem informa Disponibilidade para Funcionário
  ao inserir um Afastamento
type: support-article
updated_at: '2025-07-29T19:21:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050562414-RH-Linha-Protheus-GPE-Mensagem-informa-Disponibilidade-para-Funcion%C3%A1rio-ao-inserir-um-Afastamento
---

**Ocorrência**  
Ao inserir **Afastamentos**, através da rotina **GPEA240**, em ambientes com integração ao sistema **PIMS**, é apresentada **mensagem** informando "**Problemas na integração: Existe Disponibilidade para o Funcionário com data posterior ao período de Afastamento**" e **impede** a gravação do afastamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esta mensagem ocorre devido à fontes desatualizados  
  
  
  
**Solução**1. Para solucionar essa ocorrência, necessário aplicação do pacote acumulado do módulo de RH mais recente correspondente à sua versão:  
Pacote acumulado RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848>  
  
2. Se a versão do Protheus for anterior à 12.1.27, necessário criar o parâmetro **MV\_AFASEAI** conforme documentação descritiva abaixo:  
<https://tdn.totvs.com/display/public/PROT/7858492+DRHGCH-16016+DT+Envio+de+Afastamentos+EAI>
