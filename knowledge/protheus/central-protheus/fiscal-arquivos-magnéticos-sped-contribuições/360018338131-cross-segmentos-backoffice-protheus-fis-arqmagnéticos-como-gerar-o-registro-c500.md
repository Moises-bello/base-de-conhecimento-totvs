---
article_id: 360018338131
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 8a66de04168e27ed0d24273903ea2a171ef293bfbb0e42a0f945a753c42f0df0
fetched_at: '2026-06-28T22:42:04.976055+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro C500 do EFD Contribuições
type: support-article
updated_at: '2022-09-15T21:18:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018338131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-C500-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro C500 do arquivo magnético EFD Contribuições?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1.Verifique a espécie do documento:

Este registro é gerado a partir da tabela dos **Livros Fiscais (SFT)**, e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal de energia elétrica, modelo 06 (NFCEE);
* Nota Fiscal de fornecimento D’Água canalizada, modelos 29 (NFFA);
* Nota Fiscal de consumo fornecimento de gás, modelos 28 (NFCFG).
* NF-e, modelo 55 (SPED).

**Importante:**

Para que os documentos fiscais de aquisição de energia elétrica com modelo 55 (SPED) sejam considerados no registro C500, o documento deve conter um dos CFOPs listados abaixo:

1251, 2251, 3251: Compra de energia elétrica para distribuição ou comercialização;

1252, 2252: Compra de energia elétrica por estabelecimento industrial;

1253, 2253: Compra de energia elétrica por estabelecimento comercial;

1254, 2254: Compra de energia elétrica por estabelecimento prestador de serviço de transporte;

1255, 2255: Compra de energia elétrica por estabelecimento prestador de serviço de comunicação;

1256, 2256: Compra de energia elétrica por estabelecimento de produtor rural;

1257, 2257: Compra de energia elétrica para consumo por demanda contratada.  
  
2. NF de entrada deve ser geradora de Crédito PIS/COFINS e alimentar os **Livro Fiscal(Tabelas SFT e SF3).**

**TES**   
Livro Fiscal de ISS = Tributado/Outros/Isento, <> de Não para alimentar o Livro Fiscal.  
PIS/COFINS (**F4\_PISCOF**) = Ambos   
Cred. PIS/COF (**F4\_PISCRED**) = Credita (Entrada)

**Aba Outros**   
Tp Regime (**F4\_TPREG)** = Não Cumulativo ou AMBOS (Cumul/N Cumul);  
Sit. Trib PIS (**F4\_CSTPIS**) = Entrada (50 a 66) Lembrando que as CST de credito estão no intervalo 50 a 66.  
Sit. Trib COFINS (**F4\_CSTCOF**) = Entrada (50 a 66) Lembrando que as CST de credito estão no intervalo 50 a 66.  
  
3. Processe a rotina Apuração EFD Contribuições(**FISA001**) e em seguida realize a geração do arquivo magnético EFD Contribuições(**FISA008**).
