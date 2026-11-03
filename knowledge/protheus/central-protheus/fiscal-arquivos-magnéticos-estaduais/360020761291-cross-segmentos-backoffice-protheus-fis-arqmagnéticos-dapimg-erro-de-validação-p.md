---
article_id: 360020761291
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 14ba9e114abb0a1c5998abf877c7db27db56bfa75ff3cfd5e3c21773a21295a2
fetched_at: '2026-06-28T22:42:10.674749+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DAPIMG - Erro
  de validação: "Para existir valores na coluna 2 a 11, deverá existir valor na coluna
  1(Linha ??)"  "Coluna 11 deve ser menor ou igual que coluna 1 (Linha ??)"'
type: support-article
updated_at: '2022-08-17T20:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020761291-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DAPIMG-Erro-de-valida%C3%A7%C3%A3o-Para-existir-valores-na-coluna-2-a-11-dever%C3%A1-existir-valor-na-coluna-1-Linha-Coluna-11-deve-ser-menor-ou-igual-que-coluna-1-Linha
---

**Ocorrência**Ao importar o arquivo da **DAPIMG**, consta os seguintes erros:  
Para existir valores na coluna 2 a 11, deverá existir valor na coluna 1(Linha ??)  
Coluna 11 deve ser menor ou igual que coluna 1 (Linha ??)

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre quando existem valores nas colunas de ICMS Tributado/ Outros/ Isento e não existe valor na coluna de Valor Contábil. O erro pode ocorrer também se o valor das colunas 2 a 11 estão maiores que a coluna 1.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique as notas fiscais com os **CFOPs** para a linha XX (vide link);  
2. Analise se os campos **FT\_VALCONT** e **F3\_VALCONT** estão preenchidos com valores.

Link: <http://tdn.totvs.com/display/PROT/DAP0010_Linha_016_da_DAPIMG>
