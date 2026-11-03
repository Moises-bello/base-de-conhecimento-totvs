---
article_id: 360034303213
category: Escrita Fiscal - Impostos - ICMS
content_hash: a3a9e308dbf0cd05efb871a48713714a7c66bac237bf47280b15c0feaf3f32e4
fetched_at: '2026-06-28T22:39:26.013722+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Transferência de Ativo
  Imobilizado entre filiais
type: support-article
updated_at: '2023-07-24T14:00:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034303213-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Transfer%C3%AAncia-de-Ativo-Imobilizado-entre-filiais
---

**Dúvida**Transferência de Ativo Imobilizado entre filiais  
  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

1) No módulo Configurador, informe o parâmetro MV\_FILTRAN = Campo da tabela SF9 que contém a filial para qual o ativo é transferido.

Sugestão para o conteúdo: F9\_FILTRAN.

2) Acesse Livros Fiscais/ Cadastros/ Manutenção CIAP e altere o item, informando no campo F. Transf. CIAP o código da filial para qual o ativo será transferido.

3) Após emissão da Nota Fiscal de Saída, baixe o ativo na filial 01 informando os dados da Nota Fiscal de Saída e no campo Tipo Evento informe 3 = Transferência.

4) Após efetuar a baixa, o item deve ser incluído manualmente na filial 02 seguindo os procedimentos:  
a) Informe nos campos F9\_QTDPARC e F9\_SLDPARC:

Qtd. de Parcelas: 40 (quantidade que ainda não foi apropriada)

Sld. de Parcelas: 40  
Valor do ICMS: R$ 833,33 (1.000,00/48=20,83\*40=833,33)  
b) Inclua um novo campo na tabela SF9 por meio do Configurador.

Exemplo:

Campo: F9\_ITEMNF2

Tipo: Caracter

Tamanho: 4

Decimal: 0

Formato: @!

Contexto: Real

Título: Item NF (Sped Fiscal)

Texto: Incluir item nf entrada

Modo de Edição: Inclui

Nível: 1

c) Altere a informação no parâmetro MV\_F9ITEM, para que na geração do Sped Fiscal, o item da Nota Fiscal seja verificado a partir do novo campo criado, e não pelo campo padrão constante na SF9.

Exemplo de conteúdo: F9\_ITEMNF2.

Caso não possua este parâmetro, efetue a configuração:

Nome da Variável: MV\_F9ITEM

Tipo: Caractere

Conteúdo:

Descrição: Indique qual campo da tabela SF9 é considerado para indicar o item da nota de entrada. Por padrão este campo será criado com conteúdo F9\_ITEMNFE. Caso tenha necessidade, é possível criar um campo na tabela SF9 por meio do módulo Configurador, a fim de informar o número do item de entrada e o novo campo neste parâmetro.

d) Inclua o bem na Manutenção CIAP, informe o código do item no novo campo criado, e deixe em branco o campo F9\_ITEMNFE.

Desta forma, o bem será incluído para apropriação do valor de crédito CIAP e irá gerar as informações necessárias para o Sped Fiscal.

Importante: Estes procedimentos devem ser utilizados quando não há integração com o módulo Ativo Fixo.

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>
