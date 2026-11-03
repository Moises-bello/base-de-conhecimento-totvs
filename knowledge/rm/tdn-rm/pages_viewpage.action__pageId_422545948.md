---
content_hash: 0e8a98ab0671b9e11a75695f35d858e63615d57e7c096f23f6675f7b343b64b3
fetched_at: '2026-06-29T00:09:22.018966+00:00'
page_id: '422545948'
product: rm
source: tdn-rm
title: Apuração FUNRURAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545948
version: 28
---

#f5f5f5#363636noneFUNRURAL

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

O Fundo de Assistência ao Trabalhador Rural (FUNRURAL) é um imposto de contribuição previdenciária que incide sobre a receita bruta obtida com a comercialização da produção rural. Ele funciona de forma semelhante ao INSS, só que é destinado aos trabalhadores rurais. Este tributo poderá ser recolhido por Pessoas Físicas ou Pessoas Jurídicas conforme orientações legais [**LEI COMPLEMENTAR Nº 11, DE 25 DE MAIO DE 1971**](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/lcp%2011-1971?OpenDocument).

## **02. Origem dos ValoresOrigemValores**

No TOTVS Gestão Fiscal, o FUNRURAL será apurado considerando todos os Lançamento Fiscais cujo tributo FUNRURAL esteja preenchido na pasta "Outros Tributos" do item do lançamento fiscal.

Imagem

## **03. ApuraçãoApuracao**

A apuração do FUNRURAL ocorre através do Período de Apuração, ao encerrar o Período, todas as movimentações com o tributo FUNRURAL ficarão indisponíveis para o período encerrado, porém o valor do tributo será calculado somente ao executar o processo de Geração de Guias.

Ao gerar as Guias GPS automaticamente o sistema irá verificar o parâmetro "Gerar GPS por Nota Fiscal". Caso ele esteja habilitado, o sistema gera as guias por Lançamento separadamente. Ao desmarcar o parâmetro, o sistema agrupa as guias (Os campos CodColCFo, CodCFo, IdCEI, CodRetencao, DocIni, DataLF, CodTDO, SerieDOC, TiopLF, CodFilial e CodColigada são obrigatórios no agrupamento. Se o valor do campo é nulo, indica que não participa do agrupamento e assim não é preenchido na criação do objeto para geração da guia).

O Sistema também verifica o parâmetro "Gerar GPS Centralizada", caso ele esteja habilitado, o sistema irá verificar todos os lançamentos de todas as Filiais e irá gerar as Guias GPS para todas as Filiais centralizadas na Matriz. Se esse parâmetro não estiver habilitado o sistema irá verificar os lançamentos da Filial Corrente e gerar a Guia GPS.

Quando houver Código de Receita informado para o SENAR no Cadastro do INSS/PJ, o SENAR terá o seu valor gerado em uma guia separada dos demais valores, caso contrário os valores referentes ao FUNRURAL, GILRAT e SENAR serão somados e gerados em uma única guia.

Imagem

## **04. RelatórioRelatorio**

Para ajudar a conferir os valores gerados considerados na Apuração do FUNRURAL foi disponibilizado o

Imagem

## **05. Vídeo de DemonstraçãoHowTo**

**648432**

## **05. Outras informaçõesOutrasInformacoes**

**Código Pagamento:**

* O campo "Código de Pagamento" do FUNRURAL  será gerado com o "Código da Retenção" informado no Cadastro do INSS/PJ.  
  Quando o "Código da Retenção"  não for informado, a guia será gerada com ressalvas. O Log informará em qual  Lançamento o Código do Pagamento não foi preenchido.  
  Nesse caso será usada a informação do campo "Código de Receita" do cadastro do tributo quando houver.
* O campo "Código de Pagamento" do SENAR  será gerado com o "Código da Receita - SENAR" informado no Cadastro do INSS/PJ

#f5f5f5#feac0eDocumentos Relacionados10%90%10%90%10%90%10%90%10%90%
