---
article_id: 360028924191
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 31e4a85fececb8220fc6a11a69196ae2229e9fc638902b89aac6d27dbff2ac4d
fetched_at: '2026-06-28T22:42:42.073355+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Componentes que não são impressos no
  relatório MATR225
type: support-article
updated_at: '2024-03-11T18:09:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028924191-Manufatura-Linha-Protheus-SIGAPCP-Componentes-que-n%C3%A3o-s%C3%A3o-impressos-no-relat%C3%B3rio-MATR225
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21921639359383)*** Tempo aproximado para leitura: **00:01:33 min****Dúvida**Por que há componentes que não são impressos no relatório **MATR225** **- Relatório Estruturas Simples**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Todas as versões  
  
**Solução**Os componentes não são impressos no relatório quando:

* O componente está bloqueado no **MATA010 - Cadastro de Produto**, ou seja, o campo **B1\_MSBLQL - Blq. de Tela** está igual a **Sim**;
* O componente está fora da revisão no **PCPA200 - Estrutura**;
* O componente em questão possui quantidade inferior a 0,50 no **PCPA200** e no **MATA010** o item possui o campo **B1\_TIPODEC - Tipo Dec. OP** preenchido com **A - Arredonda** ou **T - Trunca as casas**;
* São realizados cálculos e validações da mesma forma que se fosse aberta uma **OP - Ordem de Produção** da quantidade base do item pai, o componente não é impresso pois o resultado desse cálculo é zero;
* Quando há itens opcionais e há item opcional *default* definido para o item pai, os demais opcionais não selecionados como *default* não são listados no relatório;
* O componente está fora da validade no cadastro de estrutura no **PCPA200**, ou seja, a pasta está vermelha conforme pode ser verificada na tela abaixo.  
  ![Imagem001.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/21981800831383)
