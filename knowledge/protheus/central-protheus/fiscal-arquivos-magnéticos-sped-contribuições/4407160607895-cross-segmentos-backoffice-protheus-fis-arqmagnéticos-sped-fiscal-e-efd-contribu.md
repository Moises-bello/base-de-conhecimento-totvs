---
article_id: 4407160607895
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: f31f0a10994a6b3fcc88ae92fd6edaf87d62d25cfe1bc061f5404b4d370cb193
fetched_at: '2026-06-28T22:42:06.702390+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  e EFD Contribuições Código Município Campo 08 do Registro 0150 '
type: support-article
updated_at: '2022-08-31T12:58:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407160607895-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-e-EFD-Contribui%C3%A7%C3%B5es-C%C3%B3digo-Munic%C3%ADpio-Campo-08-do-Registro-0150
---

**Dúvida**

Como é gravado o código do município no campo 08 do registro 0150 do SPED FISCAL e EFD Contribuições?  
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80

**Solução**  
**"Ao validar o TXT do Sped Fiscal ou Contribuições o PVA acusa inconsistência no registro 0150 para participantes estrangeiros."**

O código IBGE gerado no campo 08 do 0150 contem 07 posições. No Protheus esta amarração é feita com a junção dos campos conforme abaixo:

UF e Município (02 dígitos da UF + 05 dígitos do Município).

Se ocorrer rejeição do PVA referenciando um participante estrangeiro avaliar as informações dos campos:

**Fornecedores**

**Aba Cadastrais:**Estado (A2\_EST) = EX (A2\_COD\_MUN) = 99999 (Caso não possua, basta cadastrar o município "estrangeiro").

**Aba Fiscais:**   
País Bacen (A2\_CODPAIS) = "Código do país".

**Clientes:**Aba Cadastrais. Estado (A1\_EST) = EX (A1\_COD\_MUN ) = 99999 (Caso não possua, basta cadastrar o município "estrangeiro").

**Aba Fiscais:**   
  
País Bacen (A1\_CODPAIS) = "Código do país".
