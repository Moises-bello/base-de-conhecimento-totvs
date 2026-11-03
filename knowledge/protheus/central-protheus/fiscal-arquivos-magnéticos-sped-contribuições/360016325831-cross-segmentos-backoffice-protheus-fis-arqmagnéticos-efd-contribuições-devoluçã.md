---
article_id: 360016325831
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 1abe8b3e886fe939bb4ff2cfb3ec0437628174d4dd82f4fcf5b3c77d7f3e1218
fetched_at: '2026-06-28T22:42:05.163287+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Devolução de compra dentro e fora do período de emissão da Nota Fiscal de origem
  no Regime Não Cumulativo
type: support-article
updated_at: '2024-12-06T11:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016325831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Devolu%C3%A7%C3%A3o-de-compra-dentro-e-fora-do-per%C3%ADodo-de-emiss%C3%A3o-da-Nota-Fiscal-de-origem-no-Regime-N%C3%A3o-Cumulativo
---

**Dúvida**SITUAÇÃO 1 - Devolução de compra dentro do próprio mês de emissão da Nota Fiscal de origem.  
   
 **Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
   
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
 1. Os valores dos créditos correspondentes a serem anulados/estornados, devem ser informados preferencialmente mediante ajuste na base de cálculo da compra dos referidos bens nos registros **C100**/**C170** (informação individualizada). Ao gerar o arquivo TXT será apresentado o registro **C100** e **C170** da nota original com os campos 30 **VL\_PIS** = de valor de PIS e 36 **VL\_COFINS**= ZERADOS "Anulados/Estornado". Nos registro **C100** e **C170** referente a nota de devolução será apesentado no registro **C170** campos 30 **VL\_PIS** = com valor "Anulados/Estornado" e 36 **VL\_COFINS** = "Anulados/Estornado". Dessa forma realizando Estorno dos credito dentro do **Bloco C** e não será considerando valor de Crédito dentro do **Bloco M** - "APURAÇÃO" nos registros **M100** - PIS e **M500** - COFINS.  
Observação: O Guia Prático **EFD contribuições** solicita a utilização do CST 49 "Receita Não tributada".  
  
2. Crie uma **TES** com a configuração para CST 49 “Não Tributada” no Protheus para Devolução de Compra.  
Livro Fiscal ICMS ou ISS = Tributado, Isento ou Outros - > um dos livros deve estar diferente de Não para levar as informações do PIS e COFINS para as tabelas **SF3** e **SFT**.  
PIS/COFINS (**F4\_PISCOF**) = Não Considera  
Cred.PIS/COF (**F4\_PISCRED**) = Não Calcula  
Sit. Trib. COF (**F4\_CSTCOF**) = 49  
Sit. Trib. PIS (**F4\_CSTPIS**) = 49  
  
**Dúvida**SITUAÇÃO 2 - Devolução de compra posterior ao mês de emissão da Nota Fiscal de origem.  
  
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
1. Caso não seja possível proceder estes ajustes diretamente no **Bloco C** (como no caso da devolução ocorrer em período posterior ao da escrituração), a pessoa jurídica poderá realizar os ajustes diretamente no **Bloco M**, nos respectivos campos (campo 10 dos **Registros M100** e **M500**) e o detalhamento nos registros de ajustes de crédito (**M110** e **M510**). Neste último caso, deverá utilizar o campo “**NUM\_DOC**” e “**DESCR\_AJ**” para relacionar as notas fiscais de devolução, como ajuste de redução de crédito.  
Ao gerar o arquivo TXT, será gerado um **Registro C100** e **C170** da nota fiscal de devolução com valores de PIS e COFINS referentes aos débitos nos campos 30 **VL\_PIS** e 36 **VL\_COFINS** no **registro C170**, para realização de ajuste de redução de crédito no **Bloco M** "APURAÇÃO" **Registros M100**/**M110** e **M500**/**M510**.  
Observação: O Guia Prático **EFD contribuições** solicita a utilização do CST 49 "Receita Não tributada".  
  
2. Crie uma **TES** com a configuração para CST 49 “Não Tributada” no Protheus para devolução de compra.  
Livro Fiscal ICMS ou ISS = Tributado, Isento ou Outros - > um dos livros deve estar diferente de Não para levar as informações do PIS e COFINS para as tabelas **SF3** e **SFT**.  
PIS/COFINS (**F4\_PISCOF**) = Não Considera  
Cred.PIS/COF (**F4\_PISCRED**) = Não Calcula  
Sit. Trib. COF (**F4\_CSTCOF**) = 49  
Sit. Trib. PIS (**F4\_CSTPIS**) = 49
