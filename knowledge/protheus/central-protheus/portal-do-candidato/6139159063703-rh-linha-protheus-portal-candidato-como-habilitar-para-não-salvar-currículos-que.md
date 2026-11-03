---
article_id: 6139159063703
category: Portal do Candidato
content_hash: d0b045d99fb05722f0bc2402e90ba2d2ac5813b8a71281afe31b646a2ea76fdc
fetched_at: '2026-06-28T22:42:57.830559+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - Como habilitar para não salvar Currículos
  que não tiveram aceite ao Termo de Consentimento
type: support-article
updated_at: '2022-05-17T17:01:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6139159063703-RH-Linha-Protheus-PORTAL-CANDIDATO-Como-habilitar-para-n%C3%A3o-salvar-Curr%C3%ADculos-que-n%C3%A3o-tiveram-aceite-ao-Termo-de-Consentimento
---

**Dúvida**Como habilitar para **não salvar Currículos** que **não** tiveram aceite ao **Termo de Consentimento**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal do Candidato – Todas as versões  
  
**Solução  
Visão Geral** - Foi implementado parâmetro para definir se em casos de não aceite ao Termo de Consentimento à LGPD ou Termo de Aceite dos Responsáveis, para que o Currículo enviado não seja cadastrado no Protheus e seja desprezado seu envio.  
  
O parâmetro **MV\_BLQCV** permite seu preenchimento com os seguintes valores (considerando o Não Aceite à um dos termos):  
"1" - Não despreza o envio dos currículos e os salva com os campos de Aceite ao Termo de Consentimento com o valor "Não";  
"2" - Despreza o envio dos currículos e não os salva em nenhuma tabela.  
  
Para a existência deste parâmetro no ambiente, necessário atualização com o Pacote de Expedição Contínua do RH e seu respectivo Dicionário Diferencial:  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
**Saiba Mais**Documentação Técnica da Implementação: <https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=544704611>   
Como executar UPDDISTR: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152>   
[Artigos Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0)[Atualizações para adequação Lei Geral de Proteção de Dados (LGPD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054147634)  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
