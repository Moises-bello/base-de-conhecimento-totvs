---
article_id: 360023355971
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 67d9ce31e85b51737abaff4edfe261b10a15c07f90bd774ae1d35ba0954f9ed7
fetched_at: '2026-06-28T22:39:22.065931+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Notas fiscais de
  serviços estão sendo geradas no MATR930 (livro de entrada/saida) com os valores
  zerados'
type: support-article
updated_at: '2021-07-27T19:32:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023355971--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Notas-fiscais-de-servi%C3%A7os-est%C3%A3o-sendo-geradas-no-MATR930-livro-de-entrada-saida-com-os-valores-zerados
---

**Dúvida**Notas fiscais de serviços estão sendo geradas no MATR930 com os valores zerados  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

As notas fiscais de Serviços serão impressas no Regime de Processamento de Dados (MATR930) somente nas seguintes situações:

Caso a pergunta nos parâmetros de Geração do Livro estiver preenchida: **Destaca Nf Servicos? = SIM**.

Serão apresentadas a notas de Serviço com seu número de nota, data, UF, porém não são apresentados Valor Contábil, nem a coluna base de cálculo, isentos e outros. Será apresentada na observação dos livros a expressão: ***NT. FISCAL DE SERVIÇO***. Esta opção geralmente deve ser selecionada para JUSTIFICAR a sequência de notas utilizadas pelo cliente entre suas saídas, e para identificar o que foi mercadoria e o que foi serviço. Os valores dos serviços não são apresentados para não influenciar nos totalizadores de um livro que possui apenas de valor de mercadorias.

A TES para nota de serviços deve ser configurada conforme abaixo:

Calcula ISS = Sim

L.Fiscal ISS = Tributado/Outros/Isento

Calcula ICMS = NÃO

L. Fiscal ICMS = NÃO

Calcula IPI = Não

L.Fiscal IPI = NÃO

Em alguns casos, identificamos que as notas de ISS estavam com configuração de ICMS, como por exemplo L.Fiscal ICMS = Outros/Isento. Isso faz com que o Sistema alimente mais uma linha na SF3 para o ICMS, e esta nova linha será apresentada no Livro de Entrada/Saida, bem como na Apuração do ICMS.

O sistema identifica que uma nota é de serviços quando o campo F3\_TIPO está como S.

Vale ressaltar que o MATR930 é um relatório de ICMS e não de ISS.   
  
Registro no Livro de ISS (Entrada/Saída)   
O livro de ISS para notas fiscais de entrada é o Modelo 56 - Livros Fiscais/Relatórios/Livros Oficiais/Reg. ISS Modelo 56.  
  
Para nota fiscais de saída será utilizado o Modelo 51 - Livros Fiscais/Relatórios/Livros Oficiais/Reg. ISS Modelo 51.
