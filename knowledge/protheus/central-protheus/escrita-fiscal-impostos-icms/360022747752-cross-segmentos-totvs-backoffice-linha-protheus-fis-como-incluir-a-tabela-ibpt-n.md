---
article_id: 360022747752
category: Escrita Fiscal - Impostos - ICMS
content_hash: 4ffbc53c131b4f2b81096dd969c198923550c80cebc48cd33edb5bc5733191ea
fetched_at: '2026-06-28T22:39:24.109071+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como incluir a tabela
  IBPT no Protheus?
type: support-article
updated_at: '2025-11-04T22:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022747752-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-incluir-a-tabela-IBPT-no-Protheus
---

**Dúvida**Como incluir a tabela IBPT no Protheus?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse [https://deolhonoimposto.ibpt.org.br](https://deolhonoimposto.ibpt.org.br/) para baixar o arquivo com as alíquotas referentes aos códigos NCM/NBS cadastrados nos produtos. Este arquivo será atualizado duas vezes por ano, conforme manual de integração, também disponível no site mencionado.

2. Inclua o arquivo baixado no mesmo diretório do PROTHEUS para no momento aplicar o procedimento o sistema encontre o arquivo.

3. Verifique se a nomenclatura do arquivo refere-se a **TabelaIBPTax+UF+Versão**da tabela. Ex: **TabelaIBPTaxAM14.2.a.csv.** Caso o nome não esteja com esta nomenclatura, o arquivo não será importado

4. No módulo **Fiscal (SIGAFIS)**, acesse **Atualizações / Cadastros / Cadastro da tabela IBPT (FISA092)** clicar em Outras Ações / Importar.

Com isso, será executado a carga das alíquotas através da importação do arquivo (.CSV).
