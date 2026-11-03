---
article_id: 17965322901015
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 4815608bef144d69d096411159b44455937c0cdc2c1c923683cac6f3a3920e03
fetched_at: '2026-06-28T22:40:44.643382+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS480 - Funcionamento
  Validador ECD/ECF
type: support-article
updated_at: '2023-10-02T16:36:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17965322901015-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS480-Funcionamento-Validador-ECD-ECF
---

Abaixo possuímos alguns vídeos explicativos sobre a utilização da rotina e mais abaixo as informações técnicas:

**How To | MP-SIGACTB - Validador ECF:**

**How To | MP-SIGACTB - Validador ECD:**

## **01. VISÃO GERAL**

Tela para validação do ambiente e base de dados para auxiliar na entrega das escriturações contábeis.

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-9-58.png?version=2&modificationDate=1651762235457&api=v2)

Atenção

Dependendo da quantidade de inconsistências encontradas será mostrado o aviso abaixo indicando que para completa visualização das informações é necessário exportar os dados clicando no botão 'Baixar Dados'.

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-32-44.png?version=1&modificationDate=1644341784447&api=v2)

## 

## **02. VALIDAÇÕES GERAIS**

Nos três primeiros Dash são mostradas algumas informações básicas do ambiente, conforme abaixo:

### **01. DADOS DO SERVIDOR DE APLICAÇÃO**

Exibe os dados do binário, lib, dbaccess, release do rpo, etc.

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-20-24.png?version=1&modificationDate=1644341785330&api=v2)

### **02. DATA DOS PRINCIPAIS FONTES**

Exibe a data dos principais fontes envolvidos na entrega do ECD / ECF.

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-22-41.png?version=1&modificationDate=1644341785267&api=v2)

### **03. PROCEDURES E PONTOS DE ENTRADA**

Valida se existem os pontos de entrada ECDCHVCAB, CTBTXCACHE e ECDCHVMOV e se as procedures dinâmicas estão ativas, parâmetro [MV\_CTBSPRC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=549503023).

![](https://tdn.totvs.com/download/attachments/665275974/image2022-2-8_9-23-48.png?version=1&modificationDate=1644341785137&api=v2)

## **03. VALIDAÇÕES DO ECD**

Nesta tela serão mostradas diversas validações de cadastro e base de dados referente a Escrituração Contábil Digital, conforme abaixo:

![](https://tdn.totvs.com/download/attachments/665275974/ecd.gif?version=1&modificationDate=1644341783407&api=v2)

**Cadastros**

**1 - Compartilhamento de Tabelas:**

Valida o compartilhamento das principais tabelas envolvidas nas rotinas da Escrituração Contábil Digital (ECD).

**2 - Layout do ECD:**

Valida se foram encontrados os layouts do ECD na pasta system. Veja mais detalhes [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=536725577)

**3 - Validação de Parâmetros:**

Verifica os parâmetros: [MV\_CTBSDOC](https://tdn.totvs.com/pages/releaseview.action?pageId=362459051) e [MV\_GRIVSOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL).

**Base de Dados**

**1 - Contas Contábeis sem conta referencial:**

As contas contábeis listadas nesta validação não possuem conta referencial.

**2- Plano de contas possuem os campos CT1\_NATCTA ou CT1NTSPED em branco:**

Os planos de contas listadas nesta validação possuem os campos CT1\_NATCTA ou CT1\_NTSPED em branco. Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-MP-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF)

**3 -  Contas Contábeis (CT1) possuem conta, classe ou natureza diferente da tabela CVD:**

As contas contábeis (CT1) listadas nesta validação possuem conta, classe ou natureza diferentes da CVD.

**4 - Compartilhamento de tabelas (CT1, CVD e CVN):**

Valida o compartilhamento das tabelas CT1, CVD e CVN. É necessário a utilização do mesmo compartilhamento para estas tabelas.

**5 - Compartilhamento de tabelas CTG e CQD:**

Valida o compartilhamento das tabelas CTG, CQD. Caso o compartilhamento entre estas tabelas seja diferente a performance na escrituração pode ser comprometida.

**6- Compartilhamento diferente da CT2:**

Valida se existem tabelas de movimentos / saldos com o compartilhamento diferente da CT2.  
Caso seja encontrada alguma divergência de compartilhamento entre a tabela CT2 e as tabelas de movimentos e saldos, será exibido no item o compartilhamento da tabela CT2 e das tabelas divergentes para que o usuário possa comparar.

**7- Campo M0\_NOMECOM:**

Valida se o tamanho do campo SM0\_NOMECOM é igual em todas as empresas.

Além da visualização dos dados em tela é possível baixar uma planilha com todas as informações para consulta clicando no botão '**Baixar Dados**'.

![](https://tdn.totvs.com/download/attachments/665275974/baixar_dados_ecd.gif?version=1&modificationDate=1644341783097&api=v2)

Para complementar a análise é possível baixar um relatório listando os **lançamentos de transferência de saldos** clicando no botão abaixo:

![](https://tdn.totvs.com/download/thumbnails/665275974/image2022-2-8_14-17-17.png?version=1&modificationDate=1644341782937&api=v2)

## **04. VALIDAÇÕES DO ECF**

Nesta tela serão mostradas diversas validações de cadastro e base de dados referente a Escrituração Contábil Fiscal, conforme abaixo:

![](https://tdn.totvs.com/download/attachments/665275974/ecf.gif?version=1&modificationDate=1644341780027&api=v2)

**Cadastros**

**1 - Compartilhamento de Tabelas:**

Valida o compartilhamento das principais tabelas envolvidas nas rotinas da Escrituração Contábil Fiscal (ECF).

**2 - Layout TAF:**

Valida a versão e data dos layouts do TAF, bem como a validação das Auto-Contidas do ambiente.

**3 - Validação de Parâmetros:**

Verifica os parâmetros: MV\_CTBSDOC e MV\_GRIVSOR.

**Base de Dados**

**1 - Os planos de contas possuem a natureza da conta do plano referencial (CVN\_NATCTA) diferente da natureza da conta do plano associada (CT1\_NTSPED):**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/display/public/PROT/ECF0008_Mensagem_CH5_IDCTAR)

**2- Os ID\_Conta\_Referencial (CEZ\_IDCODC) não existem na estrutura da visão gerencial utilizada (Tabela CHA):**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=241698525)

**3 -  Os ID\_Conta\_Referencial (CAQ\_IDCODC) abaixo não existem na estrutura da visão gerencial utilizada (Tabela CHA):**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=241698456)

**4 - As contas superiores (C1O\_CTASUP) não existem no plano de contas utilizado (Tabela CT1):**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=241698479)

**5 - As naturezas (C1O\_CODNAT) não existem no plano de contas contábil (Tabela C2R) ou as tabelas auto contidas estão desatualizadas:**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=241698504)

**6 - Os ID Período Apuração (CAP\_IDPERA) abaixo não existem na base de dados (Tabela CAH) ou as tabelas auto contidas estão desatualizadas:**

Para maiores informações sobre qual erro essa inconsistência pode gerar clique [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=241698430)

**7- As Entidades Gerenciais abaixo não existem na base de dados do TAF (Tabela CHA):**

Valida se a entidade gerencial CTS\_CONTAG existe na base do TAF (Tabela CHA, campo CHA\_CODIGO).

**8 - Os Planos Gerenciais abaixo não existem na base de dados do TAF (Tabela CHA):**

Valida se a entidade gerencial CVN\_CTAREF existe na base do TAF (Tabela CHA, campo CHA\_CODIGO).

**9 - As Entidades Gerenciais abaixo não existem na base de dados do TAF (Tabela CHA):**

Valida se a entidade gerencial CVF\_CONTAG existe na base do TAF (Tabela CHA, campo CHA\_CODIGO).

Além da visualização dos dados em tela é possível baixar uma planilha com todas as informações para consulta clicando no botão '**Baixar Dados**'.

![](https://tdn.totvs.com/download/attachments/665275974/baixar_dados_ecf.gif?version=1&modificationDate=1644341782663&api=v2)

Para complementar a análise também é possível baixar um relatório listando os **lançamentos extemporâneos** clicando no botão abaixo:

![](https://tdn.totvs.com/download/thumbnails/665275974/image2022-2-8_14-23-33.png?version=1&modificationDate=1644341782443&api=v2)

**Saiba mais:**  
[Validador ECD/ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=665275974)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS480 - Validador ECD/ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6112312502295-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS480-Validador-ECD-ECF?source=search)
