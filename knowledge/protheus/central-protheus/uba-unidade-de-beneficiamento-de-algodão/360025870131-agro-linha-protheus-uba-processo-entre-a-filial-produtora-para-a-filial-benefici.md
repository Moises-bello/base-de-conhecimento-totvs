---
article_id: 360025870131
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: c3d4c87f0a234cecb45c615d8bcc4bcb3bcc0cc309967bd74dca98bc40baa0ab
fetched_at: '2026-06-28T22:45:35.655890+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Processo entre a Filial produtora para a Filial
  beneficiadora
type: support-article
updated_at: '2025-06-20T19:32:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025870131-Agro-Linha-Protheus-UBA-Processo-entre-a-Filial-produtora-para-a-Filial-beneficiadora
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21969353647639)* Tempo aproximado para leitura: **00:01:10 min****Dúvida**Como são feitos os processos de **Beneficiamento**,**Classificação e Comercialização** quando no grupo de empresas existe uma filial **Fazenda Produtora de Algodão** que envia o fardão à outra filial do grupo **Algodoeira** para a realização do beneficiamento?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**Filial Produtora:**

**1.** Registra o fardão por meio da rotina **Cadastro de Fardão - AGRA601** e efetua a entrada no estoque por meio de uma Ordem de Produção com peso estimado, geralmente menor;

**2.** Faz a **Nota Fiscal de Saída transferência da filial A para a B**, efetuando a saída no estoque;

**3.** Verifica na função de **Complemento de Fardão** o que há de notas para complementar, que já chegou no destino, que tem peso real e que falta complementar.  
  
Filial Beneficiadora:

**1.** Registra a entrada da **Nota Fiscal de Transferência**, que gera a entrada no **estoque** com o peso da **Nota Fiscal**;

**2.** Faz o romaneio de entrada pelo **UBA**, vincula a**Nota de Transferência**, permitindo a **pesagem real** e mostra a **diferença de quantidade**, para ser complementado com nota fiscal pela função **Complemento de Fardão** na filial de origem;

**3.** Quando recebe **notas de complemento**, vincula no **romaneio de entrada** as notas de complemento;

**4.** As **classificações** do algodão ocorrem no **Beneficiamento**, cada fardinho recebe uma **identificação e classificação**;

**5.** A **comercialização** ocorre nesta **filial**, ou seja é a partir dela que ocorre o **faturamento das vendas**.
