---
article_id: 360038998854
category: PCO - Contingências
content_hash: d64e2da52321d78bdb5d8b4ab5120466ed5f703eca557fa9104e32e8292fd3e7
fetched_at: '2026-06-28T22:37:12.140854+00:00'
product: protheus
section_id: 1500001539761
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização
  do modulo Planejamento de Custos Orçamentários
type: support-article
updated_at: '2025-09-30T20:44:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios
---

**Dúvida**  
CheckList para utilização do modulo Planejamento de Custos Orçamentários?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Planejamento Orçamentário – A partir da versão 12.

**Solução**  
1) Definir Plano de Contas Orçamentário (Tabela AK5 – Rotina PCOA010)

Para dar início a utilização do SIGAPCO,  é necessário definir o plano de contas orçamentário utilizado para elaboração das planilhas orçamentárias. Normalmente as empresas utilizam o próprio plano de contas contábil (Tabela CT1) ou a tabela de centros de custos (Tabela CTT) como base para este cadastro.

**Saiba mais**  
<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa010_contas_orcamentarias.htm>

2) Definir Operações Orçamentárias (Tabela AKF – Rotina PCO080)

Neste cadastro podem ser definidas as operações, utilizadas para como subdivisão da classe nos itens orçamentários.

**saiba mais**

|  |  |
| --- | --- |
| **Classe** | **Operação** |
| Compra de Produtos | Compra de Produtos Nacionais |
| Compra de Produtos Importados |

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa080_opera%E7%F5es.htm>

3) Definir Classes Orçamentárias (Tabela AK6 – Rotina PCOA020)

As características das classes devem ser definidas antes da elaboração das planilhas, pois a classe é um item orçamentário obrigatório na planilha.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa020_classes.htm>

* Cadastrar **Tipos de Saldos (Tabela AL2 - Rotina PCOA195)**

O cadastro de tipos de saldos é utilizado no processo de atualização e reprocessamentos dos cubos gerenciais.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa195_tipos_de_saldos.htm>

4) Cadastrar **Entidades Contábeis/Máscaras de Entidade Contábil (Tabelas CTT , CTH CTD – Rotinas CTBA130, CTBA040, CTBA030)**

Quando a empresa utiliza o sistema Protheus de maneira integrada estes cadastros normalmente já estão sendo utilizados ambiente "[Contabilidade Gerencial - SIGACTB](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigactb.htm)", caso não haja integração devem ser definidos neste momento as entidades contábeis e suas máscaras.

**Saiba mais**

**Centro de Custo**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba180_centro_de_custos.htm>

**Item Contábil**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba180_item_contabil.htm>

**Classe Valor**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba180_classe_de_valor.htm>

**Mascara Entidade Contábil**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctb130est_mascaras_contabeis.htm>

5) Cadastro **de Contingencias**

**Grupo de Aprovadores (Tabelas ALI, ALJ, ALK, ALL, ALM, AKD – Rotina PCOA520)**

Permite cadastrar grupos de aprovadores para contingência que serão os responsáveis pela aprovação dos saldos de contingências por tipo de bloqueio.

Parâmetros:

**MV\_PCOSDCT, MV\_PCOWFCT, MV\_PCOVENC, MV\_PCO520L  
  
Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa520_grupo_aprovadores.htm>

**Limite de Aprovação (Tabelas T18, T19, T20, T21, T22, T23, T24, T25 – Rotina PCOA510)**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa510_limite_aprovacao.htm>

Parâmetros:

**MV\_PCOSDCT, MV\_PCOWFCT, MV\_PCOVENC**

6) Elaborar **Planilha Orçamentária (Rotina PCOA100)**

Após o preenchimento dos cadastros a planilha orçamentária pode ser criada definindo suas contas orçamentárias, informando a periodicidade e seus valores, além da classe/operação e entidades contábeis.

Parâmetros:

**MV\_PCODEC, MV\_LPLAPCO**

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa100_orcamentos.htm>

7) Revisões da **Planilha Orçamentária (Tabelas AKE, AKG, AK1, AK2 e AK3 – Rotina PCOA120)**

A planilha orçamentária pode ser modificada, normalmente condicionada a mudanças de situação, reajustes/cortes determinados por ordens superiores. As revisões preservam a versão atual da planilha criando uma cópia, na qual os usuários efetuam os ajustes necessários para atendimento das solicitações.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa120_revisoes.htm>

8) Simulações da **Planilha Orçamentária (Tabelas AKR, AK1, AK2, AK3. AKG, AKE - Rotina PCOA200)**

A planilha orçamentária pode ser copiada para uma ambiente de simulação, no qual os itens orçamentários podem sofrer modificações para experimento de uma nova situação ou para simular o impacto ocorrido em função de determinados reajustes/cortes nos valores informados.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa200_simulacoes.htm>

**9) Movimentação – Lançamentos (Tabelas AKD - Rotina PCOA050)**

Normalmente os lançamentos são gerados pelos processos de contabilização orçamentária e suas origens são definidas no cadastro de lançamentos por processo, que utilizamos para cadastrar as funções do sistema (integração com ERP) e detalhar as operações tais como: inclusão, alteração e exclusão para que automaticamente atualizem a tabela de movimento. Contudo, os  movimentos podem também ser incluídos manualmente.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa050_lancamentos.htm>

10) **Movimentos – Contingencias (Tabelas ALI, ALJ, ALK, ALL, ALM, AKD – Rotina PCOA500)**

Quando houver algum bloqueio de verbas em rotinas do Sistema, será exibida uma tela de advertência, no entanto, tratando-se de uma contingência o sistema exibe os botões na tela, permitindo:

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa500_contingencias.htm>

11) **Cubos gerencias (Tabelas AKJ, AKW, AL1 e ALA - Rotina PCOA193)**

Cubo gerencial é uma ferramenta disponibilizada pelo sistema para facilitar o processo de acompanhamento de lançamentos orçamentários. Um cubo determina a forma de acumulação dos valores lançados nas movimentações orçamentárias e serve para acompanhamento e comparação.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa193_cubos_gerenciais.htm>

**12) Bloqueios (Tabelas AK8, AKA, AKB, AKH, AKI – Rotina PCA035)**

Os bloqueios são gerados pelos processos de contabilização orçamentária e suas origens são definidas no cadastro de pontos de bloqueio, que utilizamos para cadastrar as funções do sistema (integração com ERP) e detalhar as operações, tais como: inclusão, alteração e exclusão para que automaticamente atualizem os movimentos de bloqueio além do relacionamento com o cadastro dos tipos de bloqueio.

Parâmetros:

**MV\_PCOINTE, MV\_LOCPCO, MV\_LOCEPCO, MV\_LOCOPCO**

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa035_bloqueios_por_processo.htm>

13) **Acompanhamento e Controle**

O acompanhamento e controle do orçamento pode ser realizado mediante consultas aos cubos gerenciais em tela e relatórios comparativos entre orçado e realizado e também consulta de visão gerencial (orçado).

14) **Consultas:**

Possibilita efetuar consultas e/ou visões gerenciais orçamentárias, gerando consolidações de planilhas, demonstrativos de resultados, etc, de acordo com as definições e parâmetros estabelecidos.

**Visão Gerencial por Cubo | Saldo na Data (Rotina PCOC350)**

Mostra um demonstrativo dos saldos para os períodos informados, que permitem visualizar o cubo selecionado numa visão gerencial, de acordo com a configuração definida.

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoc350_visao_gerencial_por_cubo_saldos_na_data.htm>

Parâmetros:

**MV\_PCOCNIV, MV\_PCOTPGR**

**Visão Gerencial por Cubo | Saldo por periodo (Rotina PCOC360)**

Mostra um demonstrativo dos saldos para os períodos informados, que permitem visualizar o cubo selecionado numa visão gerencial, de acordo com a configuração definida.

Parâmetros:

**MV\_PCOCNIV, MV\_PCOTPGR**

**Saiba mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoc360_visao_gerencial_por_cubo_saldos_por_periodo.htm>

15) **Reprocessamento (Tabelas AKS e AKT – Rotina PCOA300)**

Tem como objetivo recalcular e analisar os saldos de um determinado período, efetuando acompanhamento dia-a-dia, atualizando os dados até a data base do sistema. Este recurso é utilizado no caso de haver necessidade de recalcular os resultados por ocasião da realização de entrada de movimentos retroativos no sistema.

**Saiba Mais**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/pcoa300_reprocessamento_cubos_gerenciais.htm>

16) **Relatórios**

Os diversos relatórios do sistema possibilitam um acompanhamento amplo da posição orçamentária da organização bem como de todos os seus projetos em andamento.

Consulte também as FAQs sobre o módulo PCO em nossa página no TDN.  
<http://tdn.totvs.com/pages/releaseview.action?pageId=224460550>  
  
Consulte o acervo do banco de conhecimento sobre o modulo em nosso portal de documentação.  
<http://tdn.totvs.com/display/PROT/Banco+de+Conhecimento+--+34959>
