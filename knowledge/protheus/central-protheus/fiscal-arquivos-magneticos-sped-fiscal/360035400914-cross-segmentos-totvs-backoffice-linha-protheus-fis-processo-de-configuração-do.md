---
article_id: 360035400914
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f6c2705f2a52ba8db28aea4a21477afaab811fd94cdce11a7585a159b799d5ab
fetched_at: '2026-06-28T22:42:03.729852+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Processo de configuração
  do CIAP para gerar o SPED Fiscal
type: support-article
updated_at: '2025-03-26T13:03:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035400914-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Processo-de-configura%C3%A7%C3%A3o-do-CIAP-para-gerar-o-SPED-Fiscal
---

**Dúvida**Qual o Processo de configuração do CIAP para gerar o SPED Fiscal?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Inclusão de ativo na rotina Manutenção CIAP (MATA905), por meio da nota fiscal de compra do bem, ou manualmente na rotina.

Pela nota fiscal de compra do ativo:

1) Cadastro de TES:

Credita ICMS = Sim

Atu. Ativo = Sim – Caso haja integração com o módulo Ativo Fixo, o registro gerado na SF9 gera um registro também na SN1.

Desm. IT. ATF = Sim/Não – Parâmetro utilizado para desmembrar os itens constantes na nota fiscal de entrada. Por exemplo: Item 001 – Quantidade: 03 – Se campo for configurado como SIM, são criados 3 registros referentes a esta NF. Caso configure como NÃO, será lançado somente um ativo com valor total de ICMS.

Calcula ICMS = Sim

Livro Fiscal de ICMS = Outros

Material de Consumo = Sim

Livro Fiscal CIAP =Sim

2) Inclua a nota fiscal de entrada pelo módulo Compras rotina Documento de Entrada (MATA103).

3) Verifique no módulo Livros Fiscais/Atualizações/Cadastros/Manutenção CIAP, a geração de um registro de ativo, com as informações lançadas por meio da nota fiscal e valor de ICMS calculado no documento.

Para inclusão manual:

1) Acesse Livros Fiscais/Atualizações/Cadastros/Manutenção CIAP.

2) Inclua informações constantes na nota fiscal de compra, como código de fornecedor, número e série da nota fiscal, valor de ICMS calculado, quantidade de parcelas a serem apropriadas e saldo de parcelas.

Para bens já apropriados anteriormente em outros sistemas, deve ser realizado o seguinte procedimento:

Nota Fiscal com valor de ICMS = R$ 1.000,00

Quantidade de parcelas apropriadas anteriormente = 8

Informações a serem incluídas no sistema:

Qtd. de Parcelas: 40 (qtde que ainda não foi apropriada)

Sld. de Parcelas: 40

Valor do ICMS: R$ 833,33 (1.000,00/48=20,83\*40=833,33)

Os parâmetros abaixo são responsáveis pela geração de informações para o SPED FISCAL:

Os campos utilizados na geração dos registros G125, 0300 e 0305 do Sped Fiscal, não influenciam nas apropriações realizadas e nem nas inclusões dos bens que são feitos automaticamente por meio de documento de entrada.

Conforme consta no boletim técnico FIS - SPED FISCAL -  estes parâmetros foram criados para que o sistema gere os registros 0300 e 0305 de bens cadastrados diretamente no cadastro de manutenção CIAP (SF9), quando não existem as notas de entrada do bem no sistema.

MV\_F9ITEM = F9\_ITEMNFE

MV\_F9PROD = F9\_PROD

MV\_F9ESP = F9\_ESP

MV\_F9CC = F9\_CC

MV\_F9PL = F9\_PL

MV\_F9FRT = F9\_FRETE

MV\_F9ICMST = F9\_ICMSST

MV\_F9DIF = F9\_DIFALIQ

Dentre os campos relacionados, somente o F9\_ITEMNFE é um campo padrão existente na SF9, que ao incluir bem manual, bloqueia a inclusão caso não haja entrada da nota fiscal referente ao bem.

Para inclusão é necessário criar um novo campo para que gere a informação correta no Sped Fiscal.

Exemplo:

1) Inclua um novo campo na tabela SF9 por meio do Configurador:

Campo: F9\_ITEMNF2

Tipo: Caracter

Tamanho: 4

Decimal: 0

Formato: @!

Contexto: Real

Título: Item NF (Sped Fiscal)

Texto: Incluir item nf entrada

Modo de Edição: INCLUI

Nível: 1

2) Altere a informação no parâmetro MV\_F9ITEM, para que ao gerar o Sped Fiscal seja verificado o item da nota fiscal a partir do novo campo criado, e não pelo campo padrão constante na SF9, exemplo de conteúdo: F9\_ITEMNF2.

Caso não possua este parâmetro, configure:

Nome da Variável: MV\_F9ITEM

Tipo: Caractere

Conteúdo:

Descrição: Indica qual campo da tabela SF9 é considerado para indicar o item da nota de entrada. Por padrão este campo será criado com conteúdo F9\_ITEMNFE. Caso tenha necessidade, o usuário pode criar um campo na tabela SF9, por meio do Configurador, para informar o número do item de entrada e informar o novo campo neste parâmetro.

3) Incluir o bem na Manutenção CIAP informando o código do item no novo campo criado, deixando em branco o campo F9\_ITEMNFE.

O restante dos campos são sugestões para criação e preenchimento, quando não houver a nota fiscal de entrada incluída no sistema.

Sendo assim, ao lançar nota fiscal que alimente a Manutenção CIAP estes campos não serão preenchidos, devendo ser preenchidos manualmente ao incluir bem diretamente na Manutenção CIAP (SF9).

 Inclusão de ativo fixo na Manutenção CIAP, para realizar a apropriação de crédito de ICMS;  
Geração de informações para gerar Bloco G do Sped Fiscal.

**Documentos relacionados:**

Boletim técnico FIS - SPED FISCAL

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285>

Boletim técnico FIS - Ciap - Crédito ICMS sobre Ativo Permanente.

<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>

Observações:

Rotinas envolvidas:

MATA103, MATA080, MATA905, MATA906.
