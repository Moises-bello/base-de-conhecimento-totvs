---
content_hash: 70e398d1c502e6a696a62ad97a5f85e37ef97184c36b8b557cae481829fd60fa
fetched_at: '2026-06-29T00:11:42.854098+00:00'
page_id: '799267042'
product: rm
source: tdn-rm
title: DES - Belo Horizonte - Registro D - Dedução De Materiais, Serviços Ou Repasses
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799267042
version: 4
---

Para gerar esse Registro é preciso que a Filial esteja com o parâmetro "Emite Livros de Construção Civil" habilitado e que o campo "Código Projeto" esteja preenchido no Lançamento Fiscal. Será gerado um Registro do tipo "D" para cada Nota Fiscal de Dedução vinculada ao Lançamento Fiscal de saída.

|  |  |  |
| --- | --- | --- |
| Posição | Campo | Origem dos Dados |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "D". |
| 02 | Número da NFS-e importada com dedução | Se o Lançamento Fiscal de saída vinculado à dedução dor uma NFS-e estes campos serão preenchidos com número e valor da NFS-e. |
| 03 | Valor da NFS-e importada com dedução | Mesma validação do campo 2. |
| 04 | Tipo da dedução | Se as Notas de Dedução forem de Materiais (Tipo de Dedução "1"), então recebe "1 - para Materiais".  Se as Notas de Dedução forem de Sub Empreitada (Tipo de Dedução "2"), então recebe "2 – Serviços".  Não aderência para os Tipos: • "3" para Alimentação e Bebidas/Frigobar, • "4" para Reembolso de despesas, • "5" para Outras Deduções e • "6" para Repasse consorciado. |
| 05 | Descrição do tipo de dedução | Se as Notas de Dedução forem de Materiais (Tipo de Dedução "1"), então recebe "Dedução de Materiais".  Se as Notas de Dedução forem de Sub Empreitada (Tipo de Dedução "2"), então recebe "Dedução de SubEmpreitada".  Não aderência para os Tipos: • "3" para Alimentação e Bebidas/Frigobar, • "4" para Reembolso de despesas, • "5" para Outras Deduções e • "6" para Repasse consorciado. |
| 06 | Data de emissão do documento utilizado na dedução. | Esses campos serão preenchidos com as informações dos Lançamentos Fiscais associados como Notas Fiscais de Dedução. |
| 07 | Número do documento utilizado na dedução. | Esses campos serão preenchidos com as informações dos Lançamentos Fiscais associados como Notas Fiscais de Dedução. |
| 08 | Valor bruto do documento utilizado na dedução/repasse | Esses campos serão preenchidos com as informações dos Lançamentos Fiscais associados como Notas Fiscais de Dedução. |
| 09 | Valor do material, serviço ou repasse utilizado na operação | Valor da dedução informado para a Nota Fiscal de Dedução. |
| 10 | Alíquota | Alíquota informada para o tributo ISS no Item ou no Lançamento Fiscal de entrada utilizado como Dedução de Sub Empreitada. |
| 11 | Tipo de Recolhimento do ISSQN | Se o Tipo de Recolhimento informado para o tributo ISS no Item ou no Lançamento Fiscal de entrada utilizado como Dedução de Sub Empreitada ISS for "Retido na Fonte" ou "Retido na Fonte Deduzido" então preencher com "1". Caso contrário, preencher com "2". |
| 12 | Inscrição Municipal do emissor do documento de dedução/repasse | Estes campos serão preenchidos com os dados do Cliente/Fornecedor do lançamento de dedução associado ao Lançamento Fiscal de saída. |
| 13 | CNPJ do emissor do documento de dedução/repasse | Mesma validação do campo acima. |
| 14 | CPF do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 15 | Razão Social do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 16 | Logradouro do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 17 | Número do endereço do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 18 | Complemento do endereço do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 19 | Nome do bairro do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 20 | Cidade do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 21 | País do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 22 | CEP do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 23 | Telefone do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
| 24 | E-mail do emissor do documento de dedução/repasse | Mesma validação do campo 12. |
