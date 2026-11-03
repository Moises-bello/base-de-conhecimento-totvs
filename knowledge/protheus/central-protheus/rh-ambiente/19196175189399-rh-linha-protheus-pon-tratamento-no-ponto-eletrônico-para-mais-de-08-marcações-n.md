---
article_id: 19196175189399
category: RH - Ambiente
content_hash: ab1476b45fb42e342cd1edb375b9efaf42c7b884923fa8be2f98480c33410488
fetched_at: '2026-06-28T22:44:55.986193+00:00'
product: protheus
section_id: 32302375681815
source: central-protheus
title: RH - Linha Protheus - PON - Tratamento no Ponto Eletrônico para mais de 08
  marcações no dia
type: support-article
updated_at: '2025-09-08T17:04:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19196175189399-RH-Linha-Protheus-PON-Tratamento-no-Ponto-Eletr%C3%B4nico-para-mais-de-08-marca%C3%A7%C3%B5es-no-dia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19196153192343) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O módulo de Ponto Eletrônico trata mais de 08 marcações no dia?  
  
**Ambiente**Microsiga Protheus – Ponto Eletrônico – Todas as versões  
  
**Solução**Por padrão o Ponto Eletrônico aceita até **quatro pares** de **entrada/saída** das marcações em uma mesma jornada, ou seja, 08 marcações diárias.  
  
Quando existe a necessidade de tratamento para mais marcações, é possível configurar o parâmetro **MV\_COLMARC** para aceitar até 12 marcações diárias, ou seja, 6 pares de entrada/saída em uma mesma jornada, no entanto, é **necessário customizar o sistema para considerar todas as marcações**, e ressaltamos que esta **é uma customização complexa**, que envolve a criação de campos, configuração de gatilhos de campos, implementação de um ponto de entrada e a customização dos relatórios que envolvem a listagem destas marcações.  
  
Para utilizar 5 ou 6 pares de marcações, será necessário utilizar o ponto de entrada **PNMTABC01** para alterar o calendário do Ponto gerado pelo sistema e **essa alteração reflete em todos os processos do Ponto**que utilizam o calendário como base para o processamento.  
  
Cabe ressaltar que mesmo em casos de customizações, o parâmetro **MV\_COLMARC**pode ser alterado para 5 ou 6, **sendo 6 o máximo aceito**.  
  
Para maiores detalhes sobre a criação de Campos, Gatilhos e o Ponto de Entrada PNMTABC01, **[acesse esta documentação.](https://tdn.totvs.com/pages/releaseview.action?pageId=718991442)**  
  
**Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MV\_COLMARC - Numero de Conjuntos de Entrada e Saída](https://tdn.totvs.com/pages/releaseview.action?pageId=718991442)
