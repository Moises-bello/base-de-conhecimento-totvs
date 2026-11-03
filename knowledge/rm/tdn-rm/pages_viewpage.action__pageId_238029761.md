---
content_hash: 0f41cfdb5988f964274a749b97147606828d3d034de1258e8ef0d919f044d014
fetched_at: '2026-06-29T00:08:08.302730+00:00'
page_id: '238029761'
product: rm
source: tdn-rm
title: DT Arquivos Bancários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238029761
version: 15
---

# PAGAMENTO ELETRÔNICO CNAB 240 POSIÇÕES

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção & Projetos. | | |
| **Módulo:** | *Folha de Pagamento* | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Pagamento Eletrônico* | *Pagamento Eletrônico.* | | | |
| **Requisito (ISSUE):** | [RHFOP001-584](http://jiraproducao.totvs.com.br/browse/RHFOP001-584) | | |
| **País:** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Informações Iniciais

Relatório de Pagamento Eletrônico **CNAB 240 Posições** dos 7 principais bancos do Brasil, sendo eles:

**001 – Banco do Brasil**

**033 – Santander**

**104 – Caixa Econômica Federal**

**237 – Bradesco**

**341 – Itaú**

**389 – Mercantil do Brasil**

Disponível **Segmento A** e **Segmento B**

# Importar Layout

Para importar o layout do Relatório Bancário CNAB 240, entre em:

**RH | Folha de Pagamento | Gestão | Gerador de Saída**

Clique em Processos e depois **Importar Layout**, selecione **Adicionar Objetos** e localize os layouts desejados.

Os layouts Bancários se encontram em: ...\CorporeRM\ObjetosGerenciais\Layout

Os relatórios podem ser de **FOPPLAY0004** até **FOPPLAY0017**, dependendo do Banco desejado e do tipo da base (Oracle ou SQL)

# Gerar o Relatório

Após a importação, marque o Layout, clique em **Processos | Geração de Saídas**

Coloque as informações para complemento do Relatório, selecione o filtro e gere.

Para cada Banco, poderá ter parâmetros diferentes, como:

**Banco do Brasil, Santander e Mercantil:**

**Caixa Econômica Federal:**

**Atenção:**Para a Caixa Econômica Federal, no cadastro de bancos, deverá ser preenchido o campo **Código Febraban** (GBANCO.NUMEROOFICIAL) com o código 104.

**Bradesco:**

**Itaú:**

DAC = Dígito de Auto Conferência

Ao final será gerado o relatório como um arquivo .txt, no diretório escolhido, com as informações:

**- Header do Arquivo**

**- Header do Lote**

**- Segmento A**

**- Segmento B**

**- Trailer do Lote**

**- Trailer do Arquivo**

# Manutenção do Layout

Para manutenção do layout, acesse Integração | Gerador de Saída | Layouts

Dê um duplo clique no layout desejado
