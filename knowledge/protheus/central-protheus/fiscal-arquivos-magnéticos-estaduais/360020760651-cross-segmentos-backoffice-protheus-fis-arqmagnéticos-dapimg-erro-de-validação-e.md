---
article_id: 360020760651
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: bef81788d486431b3bac2d7e68177ec6a43a91f9d033e4cf98e67e6d08bc381f
fetched_at: '2026-06-28T22:42:10.671938+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DAPIMG - Erro
  de validação "Existindo valor na coluna 1, a soma dos valores das colunas 2 a 10
  ou 2 a 11 deverá ser maior que 0,00 (Linha ??)"
type: support-article
updated_at: '2022-08-17T20:11:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020760651-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DAPIMG-Erro-de-valida%C3%A7%C3%A3o-Existindo-valor-na-coluna-1-a-soma-dos-valores-das-colunas-2-a-10-ou-2-a-11-dever%C3%A1-ser-maior-que-0-00-Linha
---

**Ocorrência**Ao importar o arquivo da **DAPIMG** no validador, consta o seguinte erro:  
Entradas: Existindo valor na coluna 1, a soma dos valores das colunas 2 a 11 deverá ser  
maior que 0,00 (Linha ??)  
Saídas: Existindo valor na coluna 1, a soma dos valores das colunas 2 a 10 deverá ser  
maior que 0,00 (Linha ??)  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois as composições das colunas são feitas através das escriturações das notas fiscais, onde o sistema verifica os campos do **TES**, neste caso a configuração do sistema está incorreta.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique o Cadastro da TES, se os campos estão condizentes **(F4\_LFICM) L.Fisc.ICMS** x **Sit.Trib.ICM (F4\_SITTRIB)**   
Exemplo:  
**L.Fisc.ICMS** = Tributado  
**Sit.Trib.ICM** = 00 Tributado

2. Verifique o Cadastro da **TES** das Notas Fiscais do período, com os **CFOPs** para a(s) linha(s) XX, segue link com os **CFOPs** que cada linha compõe a geração do arquivo: <http://tdn.totvs.com/display/PROT/DAP0010_Linha_016_da_DAPIMG> ;  
  
3. Filtre nas tabelas **SFT** e **SF3** as notas fiscais do período geradas com as **CFOPs** que compõem as linhas onde ocorrem o problema, e verifique se os campos **FT/F3\_VALCONT, FT/F3\_BASEICM, FT/F3\_VALICM, FT/F3\_OUTRICM,  FT/F3\_ISENICM FT\_CLASFIS**,  estão condizentes.  
Independente da escrituração, nenhum desses campos devem estar vazios, ou seja, se por exemplo alguma nota fiscal foi escriturada no livro tributado, os campos **FT/F3\_VALCONT, FT/F3\_BASEICM, FT/F3\_VALICM** deverão obrigatoriamente estar preenchidos, assim como **FT/F3\_VALCONT e FT/F3\_OUTRICM** no livro Outros e **FT/F3\_VALCONT** e **FT/F3\_ISENICM** no livro Isento.
