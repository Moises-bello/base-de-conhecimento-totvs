---
article_id: 360016344771
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 9c3b9864fac2559e4b1f16e8a0f1874f1cf74420523af6d04ff41e6b1ccf006f
fetched_at: '2026-06-28T22:42:05.168550+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Devolução de Venda Dentro e Fora do Período de Emissão da Nota Fiscal de Origem
  - Regime Cumulativo
type: support-article
updated_at: '2024-12-06T16:43:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016344771-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Devolu%C3%A7%C3%A3o-de-Venda-Dentro-e-Fora-do-Per%C3%ADodo-de-Emiss%C3%A3o-da-Nota-Fiscal-de-Origem-Regime-Cumulativo
---

**Dúvida**SITUAÇÃO 1 - Devolução de venda dentro do próprio mês de emissão da Nota Fiscal de origem.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
 1. Neste caso, a venda é gerada com a base de cálculo zerada, não gera contribuição, pois a mercadoria foi devolvida no mesmo período de emissão do documento. Sendo assim, a Devolução de Venda não é apresentada no arquivo magnético **EFD Contribuições** e ovalor será abatido do documento original (Receita).  
Nos casos de devolução com base no Decreto-Lei nº 1.598/1977 (nova redação Lei 12.973/2014), as receitas devem ser tratadas no campo 02 - **VL\_REC\_COMP** do registro **F550** - Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência e os valores de devolução são tratados como exclusão da base de cálculo nos campos 04 - **VL\_DESC\_PIS** e 09 - **VL\_DESC\_COFINS**.  
Dessa forma, o estorno das receitas dentro do **bloco F**, não será considerado o valor da Receita dentro do **bloco M** - "APURAÇÃO", nos registros **M200** - PIS e **M600** - COFINS.  
Observação: O Guia Prático **EFD contribuições**, solicita a utilização da CST 98 "Outras Operações de Entrada".  
  
2. Crie um TES com a configuração para o CST 98 “Outras Operações de Entrada” para Devolução de Venda.  
Livro Fiscal ICMS ou ISS = Tributado, Isento ou Outros - > um dos livros deve estar diferente de "Não" para levar as informações do PIS COFINS para as tabelas **SF3** e **SFT**.  
PIS/COFINS (**F4\_PISCOF**) = Não Considera;  
Cred.PIS/COF (**F4\_PISCRED**) = Não Calcula;  
Sit. Trib. COF (**F4\_CSTCOF**) = 98;  
Sit. Trib. PIS (**F4\_CSTPIS**) = 98.  
  
SITUAÇÃO 2 - Devolução de Venda posterior ao mês de emissão da Nota Fiscal de origem.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Neste caso, é feito um ajuste de diminuição da contribuição nos Registros **M220** e **M620**, diminuindo o valor da contribuição a pagar no período fiscal, com os campos de observação e número de documentos preenchidos, referindo à devolução de venda, pois a mercadoria foi devolvida em período posterior ao de emissão do documento.  
Caso não seja possível proceder estes ajustes diretamente no bloco F (neste caso, da devolução ocorrer em período posterior ao da escrituração), a pessoa jurídica poderá realizar os ajustes no **bloco M**, nos respectivos campos (campo 10 dos registros **M210** e **M610**) e o detalhamento nos registros de ajustes de Contribuições/Receita (**M220** e **M620**). Neste último caso, deverá utilizar o campo “**NUM\_DOC**” e “**DESCR\_AJ**” para relacionar as notas fiscais de devolução, como ajuste de redução de crédito.  
Independente de formulário próprio igual a SIM/NÃO, o sistema irá gerar um registro de ajuste no **M220**/**M620**, uma vez que não existe o termo crédito no regime cumulativo.  
Observação: O Guia Prático da EFD Contribuições, solicita a utilização do CST 98 "Outras Operações de Entrada".  
  
2. Crie um TES com a configuração para CST 98 “Outras Operações de Entrada” Para Devolução de Venda.  
Livro Fiscal ICMS ou ISS = Tributado, Isento ou Outros - > um dos livros deve estar diferente de Não para levar as informações do PIS COFINS para as tabelas **SF3** e **SFT**.  
PIS/COFINS (**F4\_PISCOF**) = Não Considera;  
Cred.PIS/COF (**F4\_PISCRED**) = Não Calcula;  
Sit. Trib. COF (**F4\_CSTCOF**) = 98;  
Sit. Trib. PIS (**F4\_CSTPIS**) = 98.
