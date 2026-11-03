---
article_id: 4410625269655
category: eSocial
content_hash: f604df12e577760525f1cb6788b75449a7e88be5fd9dce125a45a1ffe986f745
fetched_at: '2026-06-28T22:47:39.149985+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2240: O campo ''dscAgNoc'' do registro ''agNoc'' é obrigatório
  e não está preenchido'
type: support-article
updated_at: '2026-04-01T12:46:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410625269655-RH-RM-SMT-S-2240-O-campo-dscAgNoc-do-registro-agNoc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035832622615) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O que fazer quando aparece a mensagem **"*****O campo 'dscAgNoc' do registro 'agNoc' é obrigatório e não está preenchido*****"**ao gerar o XML do evento S-2240?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM- Segurança e Saúde Ocupacional - A partir da versão **12.1.28** e **superiores.**  
  
**Solução**  
Esse erro ocorre quando há utilização de **Agentes Nocivos específicos** no cadastro, porém **a descrição do agente não foi preenchida**.

A descrição (**dscAgNoc**) é obrigatória para os seguintes códigos de agentes:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39442661299223)  
  
1. **Como validar se o erro ocorre no seu cenário**

Verifique:

* Se o risco está vinculado a algum dos códigos acima
* Se o cadastro do agente nocivo possui o campo **Descrição** em branco

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39442661300887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39442742005271)  
  
  
**2. Como corrigir**

Acesse a guia **PPRA/PGR** | **Tipos de Agentes** e edite o **Tipo de Agente Nocivo** vinculado ao risco, e preencha o campo '**Descrição'**. Após salvar estas alterações, gere o XML do S-2240 novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39442742005527)  
  
**Saiba Mais**

Para maiores informações, acesse:

- [Tipos de Agentes](https://tdn.totvs.com/display/LRM/Tipos+de+Agentes)

- [RH - RM - SMT - Gerar o evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007674022)
