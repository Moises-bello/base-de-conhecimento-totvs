---
article_id: 360010316531
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c4617f024936d5cbf5410258637d2acd0d3e6c675a87c62b5beee77e6dea6bc3
fetched_at: '2026-06-28T22:42:02.571305+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registros G110, G125, G130 E G140
type: support-article
updated_at: '2025-03-19T17:52:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316531-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registros-G110-G125-G130-E-G140
---

**Dúvida**

Como gerar os registros G110, G125, G130 e G140?

**Ambiente**

Protheus - Livros Fiscais - A partir de 12.1.17

**Solução**

#### **REGISTROS G110, G125, G130 E G140**

Os registros do Bloco G podem ser gerado de duas formas: via notas de entrada ou manualmente.

**1- Geração do registro G110, G125, G130 e G140 via documento de entrada.**

1-TES

Cadastro de TES:

Credita ICMS = Sim

Atu. Ativo = Sim                               “Padrão não”

**Importante:**

Caso haja integração com o módulo Ativo Fixo, o registro gerado na SF9 irá gerar um registro também na SN1 e deverá ser realizado complemento de compra pelo modulo de ativo fixo.

Desm. IT. ATF = Sim/Não                “Padrão Não”

**Importante:**

Parâmetro utilizado para desmembrar os itens constantes na nota fiscal de entrada. Por exemplo: Item 001 – Quantidade: 03 – Se campo for configurado como SIM, serão criados 3 registros referentes a esta NF, caso configure como NÃO, será lançado somente um ativo com valor total de ICMS.

 CFOP = 1551

 Calcula ICMS = Sim

 Livro Fiscal de ICMS = Outros

 Material de Consumo = Sim

 Livro Fiscal CIAP =Sim

1.1  -Incluir a nota fiscal de entrada através do módulo de Compras rotina Documento de Entrada (MATA103).

1.2  - Verificar no módulo Livros Fiscais/Atualizações/Cadastros/Manutenção CIAP, a geração de um registro do estorno CIAP tabela SF9, com as informações lançadas por meio da nota fiscal e valor de ICMS calculado no documento.

1.3-  Após lançamento será gravado informação na tabela SF9 que será possível na rotina MATR995

2 - Após processo de lançamento de nota fiscal se o campo da TES Atu. Ativo = Sim deve ser realizado classificação de compra pelo modulo de ativo fixo.

Esse processo é de orientação da equipe de Controladoria contábil

3 - Realizar apropriação do bem na rotina MATA906 apropriação CIAP.

**Importante:**

Deve ser informado sempre o último dia do mês para geração da apropriação do credito CIAP para gravação das informações na tabela SFA.

4 – Poderá ser gerado relatório MATR995 com as apropriações do período gravados na tabela SFA.

  Ao gerar o Livro CIAP MATR995 serão demonstrados os valores totais do período, tendo como base de cálculo do crédito a soma de todos os ativos cadastrados, desconsiderando as baixas parciais e ativos baixados por finalização das parcelas/perda/venda.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-20%2017%3A16%3A42.png?version=1&modificationDate=1466449832000&api=v2)

 Tela complementa do relatório modelo C

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-20%2017%3A17%3A2.png?version=1&modificationDate=1466449850000&api=v2)

5 - Deverá ser realizado a geração do arquivo SPEDFISCAL onde será realizado a leitura da tabela SFA onde estão sendo gravado os créditos apropriados no período fiscal.

**2 - Geração dos registros G110, G125, G130 e G140 manualmente.**

1-      Deve ser criado os campos na tabela SF9.

**Importante:**

 Os campos não são criados via compatibilizador U\_UPDSIGAIFS pois os campos não são utilizados no processo de lançamento padrão via documento de entrada.

 O lançamento manual referente a continuação de apropriação de referente a créditos onde não existe nota fiscal incluídas no Protheus.

 Dessa forma sendo necessário a inclusão dos campos manuais na tabela SF9 para lançamento de créditos manuais via Protheus.

2 -Preencher os campos conforme informações das tabelas abaixo.

F9\_CC - Tabela CTT - Deve ser preenchido com a informação do campo C Custo  "CTT\_CUSTO"

F9\_PL - Tabela CT1 - Deve ser preenchido com a informação do campo Cod Conta "CT1\_CONTA"

F9\_PROD - Tabela SB1 - Deve ser preenchido com a informação do campo Codigo "B1\_COD"

Pode ser criado uma consulta padrão para pesquisa dos codigos das tabelas.

Ao efetuar criação dos campos na tabela SF9 é possivel configurar tabela para seleção padrão da tabela "criação da lupa - de pesquisa padrão".

Configuração / base de dados / tabela SF9 / editar/ aba opções  - campo Cons padrão - selecionar a tabela que será consultada para preenchimento do campo.

Exemplo para criação dos campos na manutenção CIAP.

Para inclusão do codigo do item é necessário criar um novo campo F9\_ITEMNF2 para que gere a informação correta no Sped Fiscal

Campo: F9\_ITEMNF2

Tipo: Caracter

Tamanho: 3

Decimal: 0

Formato: @!

Contexto: Real

Titulo: Num Item SPD

Texto: Incluir item nf entrada

Help: Incluir numero do item da nota fiscal de entrada para alimentar o campo 02\_NUM\_ITEM do registro G140 SPED FISCAL

Campo: F9\_CODPROD

Tipo: Caracter

Tamanho: 30

Decimal: 0

Formato: @!

Contexto: Real

Titulo: Cod Prod SPD

Texto: Informa codigo do produto

Help: Informa codigo do correspondente ao bem no documento fiscal, preenchimento do campo 03\_COD\_ITEM G140 SPED FISCAL

Campo: F9\_CC

Tipo: Caracter

Tamanho: 9

Decimal: 0

Formato: @!

Contexto: Real

Titulo: C. Custo

Texto: Informa centro de custo

Help: Informação do centro de custo para preenchimento do campo 02 COD\_CCUS registro 0305 SPED FISCAL

Campo: F9\_PL

Tipo: Caracter

Tamanho: 20

Decimal: 0

Formato: @!

Contexto: Real

Titulo: C. Contábil

Texto: Informa conta contábil

Help: Informa contata contábil da tabela CT1 plano de contas para preenchimento do campo 06 COD\_CTA registro 0300 SPEDFISCAL.

Amarração de campos aos parâmetros

MV\_F9ITEM = F9\_ITEMNF2

MV\_F9PROD = F9\_CODPROD

MV\_F9CC = F9\_CC

MV\_F9PL = F9\_PL

Para mais informações sobre o Sped Fiscal acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
