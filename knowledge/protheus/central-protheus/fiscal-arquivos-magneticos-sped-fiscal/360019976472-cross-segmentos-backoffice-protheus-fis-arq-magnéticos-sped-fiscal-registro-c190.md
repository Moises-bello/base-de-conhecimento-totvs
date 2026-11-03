---
article_id: 360019976472
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: fe27b56ebf0e332dfe8f98b3d571b4420716d9d40f9a9ad8a656e9518226b550
fetched_at: '2026-06-28T22:42:02.419251+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C190, Campo 10 (VL_RED_BC)
type: support-article
updated_at: '2025-07-23T13:34:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019976472-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C190-Campo-10-VL-RED-BC
---

**Dúvida**Qual é a configuração para preencher o **Campo 10 (VL\_RED\_BC)** do Registro **C190** corretamente?  
  
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
**Solução**1 - Preencha o parâmetro MV\_NRPRBIC conforme abaixo:

![MV.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950412/MV.JPG)

**Importante**

Este parâmetro indica se na geração do registro **C190**, **campo 10 – VL\_RED\_BC** o valor da parcela referente à redução da base de cálculo do ICMS é recalculado na geração do arquivo. Se informado .**F.** *(False/*Falso) o valor é recalculado considerando percentual de redução da tabela **Processamento do SPED Fiscal (CD2)** ou do **Cadastro de TES** (SF4), forma que é feita antes da criação deste parâmetro, se informado .T.*(True/*Verdadeiro), então não se faz o recálculo e considera para geração do **campo 10**do registro **C190** o valor do campo **Vlr Isen ICM (FT\_ISENICM)** ou **Vlr Out ICMS (FT\_OUTRICM)**.

 2 - Configure a TES conforme abaixo:

- Calcula ICMS = SIM

- % Redução do ICMS = (? )

- Livro Fiscal ICMS = Outros ou Isento

- Situação Tributaria ICMS = 20 ou 70

![TES.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015994131/TES.JPG)

3 - Gere a Nota Fiscal de entrada:

![NF.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950752/NF.JPG)

4 - Verifique se o sistema alimentou a tabela CD2:

![CD2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950472/CD2.JPG)

5 - Verifique se o sistema alimentou corretamente as tabelas SFT e SF3:

![SFT.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015994391/SFT.JPG)

![SF3.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950792/SF3.JPG)

6 - Gere o arquivo SPED FISCAL:

![TXT.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950872/TXT.JPG)
