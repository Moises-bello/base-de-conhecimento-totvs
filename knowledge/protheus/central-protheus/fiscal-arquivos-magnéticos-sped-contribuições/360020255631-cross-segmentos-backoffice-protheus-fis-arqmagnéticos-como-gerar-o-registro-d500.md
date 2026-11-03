---
article_id: 360020255631
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4d9fbc4f6f7db8043d5009d536f79fcac218d7c73f38dd9ecd1a841943d0e945
fetched_at: '2026-06-28T22:42:04.979458+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro D500 do EFD Contribuições
type: support-article
updated_at: '2022-09-15T21:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020255631-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-D500-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro D500 do arquivo magnético EFD Contribuições?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1.Verifique a espécie do documento:

Este registro é gerado a partir da tabela dos **Livros Fiscais (SFT)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal de Serviço de Comunicação, modelo 21 (NTSC);
* Nota Fiscal de Serviço de Telecomunicação, modelo 22 (NTST);

2. Inclua a nota fiscal no sistema. A NF de entrada deve ser geradora de Crédito PIS/COFINS e alimentar os **Livro Fiscal(Tabelas SFT e SF3).**

**TES**   
L.Fisc.ICMS (**F4\_LFICM**)  = Tributado/Outros/Isento, <> de Não para alimentar o Livro Fiscal.  
PIS/COFINS (**F4\_PISCOF**) = Ambos   
Cred. PIS/COF (**F4\_PISCRED**) = Credita (Entrada)

**Aba Outros**   
Tp Regime (**F4\_TPREG)** = Não Cumulativo ou AMBOS (Cumul/N Cumul);  
Sit. Trib PIS (**F4\_CSTPIS**) = Entrada (50 a 66) Lembrando que as CST de crédito estão no intervalo de 50 a 66.  
Sit. Trib COFINS (**F4\_CSTCOF**) = Entrada (50 a 66) Lembrando que as CST de crédito estão no intervalo de 50 a 66.  
  
3. Processe a rotina Apuração EFD Contribuições(**FISA001**) e em seguida realize a geração do arquivo magnético EFD Contribuições(**FISA008**).
