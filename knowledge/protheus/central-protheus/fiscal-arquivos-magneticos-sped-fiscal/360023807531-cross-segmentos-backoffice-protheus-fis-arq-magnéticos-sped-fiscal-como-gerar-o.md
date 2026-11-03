---
article_id: 360023807531
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: fa95d9384ce4b09bd34cefba98afce1ca6f7a42b650b551a43f49ad5edd6219d
fetched_at: '2026-06-28T22:42:01.216206+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro D500 - Prestação de serviços
type: support-article
updated_at: '2025-02-11T21:06:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023807531-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-D500-Presta%C3%A7%C3%A3o-de-servi%C3%A7os
---

**Dúvida**Como gerar o registro D500 referente a prestação de serviços do arquivo magnético SPED FISCAL?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1.Verifique a espécie do documento:

Este registro é gerado a partir da tabela dos **Livros Fiscais (SFT)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal de Serviço de Comunicação, modelo 21 (NTSC);
* Nota Fiscal de Serviço de Telecomunicação, modelo 22 (NTST);

2. Vincule a espécie no parâmetro **MV\_ESPECIE**

3. Inclua um pedido de venda, onde a venda deve gerar débito de ICMS e alimentar os **Livro Fiscal(Tabelas SFT e SF3).**

**TES**CalculaICMS (**F4\_ICM**) = Sim  
L.Fisc.ICMS (**F4\_LFICM**)  = Tributado/Outros/Isento, <> de Não para alimentar o Livro Fiscal.  
Sit.Trib.ICM (**F4\_SITTRIB) =**00

**Aba Outros**   
Tp Regime (**F4\_TPREG)** = Não Cumulativo, Cumulativo ou AMBOS (Cumul/N Cumul);  
Sit. Trib PIS (**F4\_CSTPIS**) = 01 a 09 Saída;   
Sit. Trib COFINS (**F4\_CSTCOF**) = 01 a 09 Saída.

4. Após a emissão da NTSC ou NTST acesse o caminho:

Módulo 09 (Livros Fiscais)>Movimentos>Nota Fiscal Manual de Saída>Outras Ações>Complementos;  
Preencher a opção de complementos **Comunicação e Telecomunicação (Tabela SFX).**

5. Processe a rotina para gerar o arquivo SPED FISCAL.
