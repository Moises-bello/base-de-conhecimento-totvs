---
article_id: 360011410291
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: e339ca9acded72954f8b09feb3c4f45e31bdc46506da043d28f186a50bec747a
fetched_at: '2026-06-28T22:41:48.308105+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF  - Rotina Importação de
  Classificação
type: support-article
updated_at: '2021-10-07T16:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Rotina-Importa%C3%A7%C3%A3o-de-Classifica%C3%A7%C3%A3o
---

**Dúvida**Como utilizar a rotina de Importação de Classificação?

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80.  
  
**Solução**Para atualizar as fichas de imobilizado já existentes em um ambiente com as informações contábeis/gerenciais dos tipos 10 – Depreciação Contábil / Gerencial foi disponibilizado um facilitador de importação CSV da classificação contábil/gerencial de ativos.

A funcionalidade de importação de classificação contábil segue as regras de importação de arquivos texto com formato CSV (Comma-separated values) com uma estrutura específica. O arquivo .CSV deve conter no mínimo as informações obrigatórias pertinentes à classificação de um item de uma ficha de ativo. Os campos definidos como obrigatórios devem existir na estrutura do arquivo .CSV independentemente de possuírem informações.

Importante:

Os campos de valores em outras moedas não são obrigatórios, porém se o parâmetro MV\_ATFMOED estiver definido com um conteúdo diferente de 1, os campos referentes à moeda configurada serão exibidos pela validação do processo de importação.

**Pré-requisitos**

• O parâmetro MV\_ALTLCTO deve estar configurado com N.  
• O parâmetro MV\_PRELAN deve estar configurado com S.

**Procedimentos**

Para importar a classificação contábil:

1. Em Ativos, selecione o Ativo que deseja importar.  
2. Clique em Ações Relacionadas.  
3. Selecione a opção Import. Classificação.  
4. Informe o diretório onde se encontra o arquivo de extensão .CSV.  
5. Atenção aos parâmetros:  
• Nome do arquivo para importação: Caminho e nome do arquivo com a classificação contábil.  
• Exclui classificação anterior: Caso o bem já possua classificação, selecione Sim. A rotina excluirá a classificação anterior e incluirá a descrita no arquivo.  
6. Confira os dados e confirme.

Importante:

A rotina somente realiza a exclusão, caso não exista nenhuma movimentação após a classificação do bem.

Mais informações da importação

[Importação de classificação](https://tdn.totvs.com/pages/releaseview.action?pageId=533747879)
