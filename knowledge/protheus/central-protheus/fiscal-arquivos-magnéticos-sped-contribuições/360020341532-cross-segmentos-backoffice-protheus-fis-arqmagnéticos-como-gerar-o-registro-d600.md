---
article_id: 360020341532
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4c0325cc1d734b0f8f7d4410636853dbf14bd588966c2f904cad49fe8c9d3b9e
fetched_at: '2026-06-28T22:42:04.982887+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro D600 do EFD Contribuições
type: support-article
updated_at: '2022-09-15T21:22:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020341532-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-D600-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro D600 do arquivo magnético EFD Contribuições?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1.Verifique a espécie do documento:

Este registro é gerado a partir da tabela dos **Livros Fiscais (SFT)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal de Serviço de Comunicação, modelo 21 (NTSC);
* Nota Fiscal de Serviço de Telecomunicação, modelo 22 (NTST);

2. Vincule a espécie no parâmetro **MV\_ESPECIE**

3. Inclua um pedido de venda, onde a venda deve gerar débito de PIS/COFINS e alimentar os **Livro Fiscal(Tabelas SFT e SF3).**

**TES**   
L.Fisc.ICMS (**F4\_LFICM**)  = Tributado/Outros/Isento, <> de Não para alimentar o Livro Fiscal.  
PIS/COFINS (**F4\_PISCOF**) = Ambos   
Cred. PIS/COF (**F4\_PISCRED**) = Debita (Saída)

**Aba Outros**   
Tp Regime (**F4\_TPREG)** = Não Cumulativo ou AMBOS (Cumul/N Cumul);  
Sit. Trib PIS (**F4\_CSTPIS**) = 01 Saída;   
Sit. Trib COFINS (**F4\_CSTCOF**) = 01 Saída.

4. Após a emissão da NTSC ou NTST acesse o caminho:

Módulo 09 (Livros Fiscais)>Movimentos>Nota Fiscal Manual de Saída>Outras Ações>Complementos;  
Preencher a opção de complementos **Comunicação e Telecomunicação (Tabela SFX).**

5. Processe a rotina Apuração EFD Contribuições(**FISA001**) e em seguida realize a geração do arquivo magnético EFD Contribuições(**FISA008**).
