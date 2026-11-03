---
article_id: 34944956182551
category: eConsignado (Crédito do Trabalhador)
content_hash: ace8a9d2e6892542ce421083d8bd77215e15fa326f2b23b68e35bc6e8e54c56e
fetched_at: '2026-06-28T22:43:07.332783+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na consulta do Histórico de Importações do eConsignado
  em Valores Futuros, Sistema emite alerta: Não existem importações no histórico que
  correspondam à verba selecionada'
type: support-article
updated_at: '2025-09-15T13:37:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34944956182551-RH-Linha-Protheus-GPE-Na-consulta-do-Hist%C3%B3rico-de-Importa%C3%A7%C3%B5es-do-eConsignado-em-Valores-Futuros-Sistema-emite-alerta-N%C3%A3o-existem-importa%C3%A7%C3%B5es-no-hist%C3%B3rico-que-correspondam-%C3%A0-verba-selecionada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34944950984599) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Na consulta do Histórico de Importações do eConsignado em Valores Futuros, Sistema emite alerta: Não existem importações no histórico que correspondam à verba selecionada.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34944950985367)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - a partir da versão 12.1.2210  
  
**Causa**  
A mensagem é apresentada quando não existe dados gravados na RUO - Histórico de Importações da verba selecionada com aquele número de contrato.  
  
**Solução**  
O Sistema valida o **código da verba selecionada** para consulta do histórico de importações e o **número de contrato do registro**. Caso exista dados na **RUO** com o **mesmo código de verba**, mas que seja referente a **outro número de contrato**, o Sistema vai emitir o alerta.

Caso exista registro da **verba selecionada** com o **mesmo número de contrato**, será apresentada tela com o histórico dela.  
  
**Exemplo**  
  
**Registros na SRK - Valores Futuros**  
**Verba**: E01  
**Contrato**: 0000000000001    
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34944956158359)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34944956159895)  
  
**Histórico de Importações**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34944950992279)  
  
**Saiba Mais**

[Manual do Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)

[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)

[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
