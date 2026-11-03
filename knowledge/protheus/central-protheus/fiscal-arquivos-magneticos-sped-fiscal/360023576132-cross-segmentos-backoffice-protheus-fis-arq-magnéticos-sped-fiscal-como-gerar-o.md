---
article_id: 360023576132
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 89ff7e61b39a7b1b61b31293743471f951507fd546a0e1faf7a62b6164c36e39
fetched_at: '2026-06-28T22:42:01.212851+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro D500
type: support-article
updated_at: '2025-02-11T21:05:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023576132-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-D500
---

**Dúvida**Como gerar o registro D500 referente a aquisição de serviços do arquivo magnético SPED FISCAL?

**Produto**

Protheus - Livros Fiscais - A partir de 12.1.17

**Solução**

1.Verifique a espécie do documento:

Este registro é gerado a partir da tabela dos **Livros Fiscais (SFT)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal de Serviço de Comunicação, modelo 21 (NTSC);
* Nota Fiscal de Serviço de Telecomunicação, modelo 22 (NTST);

2. Inclua a nota fiscal no sistema. A NF de entrada deve alimentar os **Livro Fiscal(Tabelas SFT e SF3).**

**TES**   
CalculaICMS (**F4\_ICM**) = Sim ou Não  
L.Fisc.ICMS (**F4\_LFICM**)  = Tributado/Outros/Isento, <> de Não para alimentar o Livro Fiscal.  
Sit.Trib.ICM (**F4\_SITTRIB) =**00, 40 ou 41

**Aba Outros**   
Tp Regime (**F4\_TPREG)** = Não Cumulativo ou AMBOS (Cumul/N Cumul);  
Sit. Trib PIS (**F4\_CSTPIS**) = Entrada (50 a 73)   
Sit. Trib COFINS (**F4\_CSTCOF**) = Entrada (50 a 73)

3. Após a entrada da NTSC ou NTST acesse o caminho:

Módulo 09 (Livros Fiscais)>Movimentos>Nota Fiscal Manual de Saída>Outras Ações>Complementos;  
Preencher a opção de complementos **Comunicação e Telecomunicação (Tabela SFX).**

4. Processe a rotina para gerar o arquivo SPED FISCAL
