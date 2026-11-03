---
article_id: 23632105217431
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 55a69e57cd4e2096f0d2b1b63722057f54b0c2b9beb8b62def00cd46b61fcb3d
fetched_at: '2026-06-28T22:42:05.012976+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os
  campos 02 IND_NAT_FRT e 05 NAT_BC_CRED dos Registros D101 e D105 do EFD Contribuições?
type: support-article
updated_at: '2024-05-22T17:50:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23632105217431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-campos-02-IND-NAT-FRT-e-05-NAT-BC-CRED-dos-Registros-D101-e-D105-do-EFD-Contribui%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23632105196567) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar os campos **02 - IND\_NAT\_FRT** e **05 - NAT\_BC\_CRED** dos Registros **D101** e **D105** do **EFD Contribuições**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução:**

Para gerar o campo **02 IND\_NAT\_FRT**, acesse o **Cadastro de TES (Tabela SF4)** e preencha o campo **Ind.Nat.Fret (F4\_INDNTFR)**, nele contém todas as opções conforme demonstradas no **Guia Prático do EFD Contribuições**. Ao escriturar o **Documento Fiscal**, o conteúdo será gravado no campo **FT\_INDNTFR** da Tabela **SFT.**

Para gerar o campo **05 NAT\_BC\_CRED**, acesse o **Cadastro de TES (Tabela SF4)** e preencha o campo **F4\_CODBCC,** ao escriturar o Documento Fiscal, o conteúdo será gravado no campo **FT\_CODBCC.**

Processe a **Apuração** do **EFD Contribuições** e Gere o **arquivo txt** do **EFD Contribuições.**

Importante:   
Caso tenha ocorrido a escrituração sem esses campos preenchidos, ajuste a **TES** para os próximos lançamentos e corrija na **Rotina de Acerto Fiscal.** Após, exclua a **Apuração,** reprocesse e gere um novo **Arquivo txt.**
