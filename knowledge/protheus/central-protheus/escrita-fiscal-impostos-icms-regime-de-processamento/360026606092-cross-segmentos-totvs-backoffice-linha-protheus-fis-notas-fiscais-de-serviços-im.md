---
article_id: 360026606092
category: Escrita Fiscal - Impostos - ICMS - Regime de Processamento
content_hash: 36ee22440c438f341f6451b6cc825f38e752968eb259624024a642ae8ade22b1
fetched_at: '2026-06-28T22:39:22.857022+00:00'
product: protheus
section_id: 1500001549862
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Notas Fiscais de Serviços
  impressas no Regime de Processamento de Dados (MATR930)
type: support-article
updated_at: '2021-07-15T18:10:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026606092-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Notas-Fiscais-de-Servi%C3%A7os-impressas-no-Regime-de-Processamento-de-Dados-MATR930
---

**Dúvida**Notas de serviço destacadas no livro fiscal de mercadoria (MATR930)

**Ambiente**Protheus – Fiscal – A partir da versão 12.1.17  
  
**Solução**

As notas fiscais de Serviços serão impressas no Regime de Processamento de Dados (MATR930) somente nas seguintes situações:

Caso a pergunta nos parâmetros de Geração do Livro estiver preenchida: Destaca Nf Servicos? = SIM.

Serão apresentadas a notas de Serviço com seu número de nota, data, UF, porém não são apresentados Valor Contábil, nem a coluna base de cálculo, isentos e outros. Será apresentada na observação dos livros a expressão: NT. FISCAL DE SERVIÇO. Esta opção geralmente deve ser selecionada para JUSTIFICAR a sequência de notas utilizadas pelo cliente entre suas saídas, e para identificar o que foi mercadoria e o que foi serviço. Os valores dos serviços não são apresentados para não influenciar nos totalizadores de um livro que possui apenas de valor de mercadorias.

A TES para nota de serviços deve ser configurada conforme abaixo:

Calcula ISS = Sim

L.Fiscal ISS = Tributado/Outros/Isento

Calcula ICMS = NÃO

L. Fiscal ICMS = NÃO

Calcula IPI = Não

L.Fiscal IPI = NÃO

 Em alguns casos, identificamos que as notas de ISS estavam com configuração de ICMS, como por exemplo L.Fiscal ICMS = Outros/Isento. Isso faz com que o Sistema alimente mais uma linha na SF3 para o ICMS, e esta nova linha será apresentada no Livro de Entrada/Saida, bem como na Apuração do ICMS.
