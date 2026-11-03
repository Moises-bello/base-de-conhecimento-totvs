---
content_hash: d668c94656ed9fc2eef014c4cf4d09b84d6b8a6639c366c150787cbb73bbae17
fetched_at: '2026-06-29T00:12:16.352382+00:00'
page_id: '985674478'
product: rm
source: tdn-rm
title: Gerenciamento de Códigos TUSS e TISS no RM Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=985674478
version: 2
---

Gerenciamento de Códigos TUSS e TISS no RM Saúde

# Visão Geral

O RM Saúde permite configurar como os códigos TUSS (8 dígitos) e TISS (10 dígitos) serão utilizados no processo de importação de tabelas (como Brasíndice) e na geração/envio de XML TISS. A lógica é baseada em parametrizações, garantindo aderência às exigências dos convênios e flexibilidade na gestão dos códigos de materiais e medicamentos.

# Regras de Funcionamento

## 1. Importação de Tabelas (Mat/Med)

* O sistema prioriza o código TUSS (8 dígitos).- Caso o item não possua TUSS, o sistema grava no cadastro o código TISS (10 dígitos) no campo correspondente.- Para que o TUSS seja priorizado, é necessário parametrizar corretamente a importação e a atualização de produtos.- A importação pode ser feita por meio de tabelas oficiais, como o Brasíndice.  
  Referência: RM - SAU - Atualização de código específico Brasíndice

  ## 2. Envio de Cobrança (XML TISS)
* A regra de prioridade entre TUSS e TISS é definida na configuração da Tabela de Mat/Med do convênio.- Se o parâmetro "Prioriza código de 10 dígitos" estiver desmarcado: - O sistema envia o TUSS (8 dígitos), se disponível. - Caso não exista TUSS, envia o TISS (10 dígitos).- Se o parâmetro estiver marcado: - O sistema envia sempre o TISS (10 dígitos), mesmo que exista TUSS.  
  Referências: RM - SAU - Utiliza 10 dígitos na ausência do código específico do MatMed; RM - SAU - Prioriza código de dez dígitos no XML

  # Onde Configurar

  ## 1. Tabela de Mat/Med (priorização no XML)

  Caminho: Cadastros > Faturamento > Tabela de Mat/Med usadasAba Identificação: parâmetro "Prioriza código de 10 dígitos".

  ## 2. Importação e Atualização de Produtos

  Caminho: Utilitários > Rotinas > Importação/Atualização (ex.: Brasíndice)Marcar a opção "Atualizar produto com código TUSS" conforme necessidade.

  ## 3. Produto

  Caminho: Cadastros > Estoques > Produto > Anexos > Informações TOTVS Saúde > Tabela de PreçoLocal onde o código específico é atualizado após a importação.

  # Exemplos de Cenário
* Cenário 1: Item possui TUSS → XML envia TUSS.- Cenário 2: Item sem TUSS, mas com TISS → XML envia TISS (10 dígitos).- Cenário 3: Parâmetro "Prioriza código de 10 dígitos" marcado → sempre envia TISS.- Cenário 4: Importação Brasíndice com opção "Atualizar produto com código TUSS" marcada → atualiza cadastro priorizando TUSS.

  # Links de Apoio

* **Utilização do código de 10 dígitos na ausência do TUSS:** <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056794934-RM-SAU-Utiliza-10-d%C3%ADgitos-na-aus%C3%AAncia-do-c%C3%B3digo-espec%C3%ADfico-do-MatMed>
* **Prioriza código de dez dígitos no XML:** <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026408173-RM-SAU-Prioriza-c%C3%B3digo-de-dez-d%C3%ADgitos-no-XML>
* **Atualização de código específico (ex: via Brasíndice):** <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037687613-RM-SAU-Atualiza%C3%A7%C3%A3o-de-c%C3%B3digo-especifico-Bras%C3%ADndic>
