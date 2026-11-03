---
article_id: 9994847150743
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 1fcf9da1f3a8cb23342839d92c85aef4cfd373530eae99e3478dc2011c329ee3
fetched_at: '2026-06-28T22:42:05.292156+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Qual é a ordem de aproveitamento de créditos na Apuração do Pis e Cofins?
type: support-article
updated_at: '2024-05-09T17:07:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9994847150743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Qual-%C3%A9-a-ordem-de-aproveitamento-de-cr%C3%A9ditos-na-Apura%C3%A7%C3%A3o-do-Pis-e-Cofins
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23372484442263) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual é a ordem de aproveitamento de créditos na Apuração do EFD Contribuições?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**No **Protheus** existe uma **ordem para o aproveitamento de créditos na Apuração EFD Contribuições**.  
  
Enquanto houver débitos no mês, o abatimento do crédito ocorrerá na ordem abaixo, se os créditos do período anterior e período atual for suficiente para o Valor do débito do mês, os valores que créditos excedentes deverão ser compensados via **PERD/COMP**.  
  
**1º Valor do Crédito descontado - Período Anterior**  
**2º Valor do Crédito descontado - Período Atual**  
**3º Valor Retido na Fonte descontado - Período Anterior**  
**4º Valor Retido na Fonte descontado - Período Atual**  
**5º Outras Deduções no período**  
  
Segue o *link* da **Orientação já publicada por esta Consultoria:**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=107381307>

Importante:

Caso seja necessário definir prioridade dos códigos de créditos **(tabela 4.3.6)** a serem consumidos primeiro, deverá utilizar o parâmetro **MV\_OCODCSC.**

Exemplo de preenchimento do parâmetro **MV\_OCODCSC: 101, 201, 301**.

Neste exemplo a ordem de processar os créditos será pelos códigos **101, 201 e 301**. A ordem descrita será aplicada primeiro sobre o saldo de crédito anterior para depois ser aplicada no saldo de crédito atual.

Segue boletins com mais informações sobre os **créditos na Apuração do EFD Contribuições**:

*Link:*  
[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Tratamento do Controle de Crédito de PIS e COFINS na Apuração e geração dos Registros 1100 e 1500 no Arquivo do EFD Contribuições](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028344732-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Tratamento-do-Controle-de-Cr%C3%A9dito-de-PIS-e-COFINS-na-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-dos-Registros-1100-e-1500-no-Arquivo-do-EFD-Contribui%C3%A7%C3%B5es?source=search)

*Link:*  
[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os registros 1100 e 1500 do EFD Contribuições pelas Rotinas Controle de Saldo de Crédito, Rotinas FISA044 e FISA045](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8736173147671-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-registros-1100-e-1500-do-EFD-Contribui%C3%A7%C3%B5es-pelas-Rotinas-Controle-de-Saldo-de-Cr%C3%A9dito-Rotinas-FISA044-e-FISA045?source=search)
