---
article_id: 360022695891
category: Escrita Fiscal - Impostos - ISS
content_hash: e7d4ce0f7bf553a923dca2a769b6f8302e4166a36b20427781ade8af00d02e40
fetched_at: '2026-06-28T22:39:35.236087+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nota fiscal de serviço
  não gerar no livro de ICMS
type: support-article
updated_at: '2021-06-15T13:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022695891-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-de-servi%C3%A7o-n%C3%A3o-gerar-no-livro-de-ICMS
---

**Dúvida**Como Fazer para nota fiscal de Serviço Entrada ou Saída não gerar Livro Fiscal de ICMS?  
  
**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

O que determina se uma nota será apresentada nos livros de ICMS ou de ISS, é o conteúdo do campo na SF3, F3\_tipo.   
Quando esse campo em branco, o sistema interpreta como produto, portanto, nota de ICMS e deverá ser apresentada no Reg. Processamento de Dados, quando esse conteúdo S, o sistema entende tratar-se de uma operação de serviço, portando, passível de ISS.

Para que o sistema preencha o campo F3\_tipo com S, o campo da TES, Calcula ISS, obrigatoriamente deverá ser configurado =Sim, independente de ter o calculo do imposto ou não na operação, esse, será determinado pelo campo Livros Fiscais de ISS, o qual determinará se haverá crédito ou não do imposto.

TES  
Calcula ICMS = Não  
L. Fisc ICMS = Não  
Calcula ISS = Sim  
L. Fiscal ISS = Diferente de não

Campo F3\_TIPO = S
