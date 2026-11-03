---
article_id: 31670844301591
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: e3121f0907e02abd7dbe1dcdb19bc1b2ff929f282c9563c93d095872aaae69ac
fetched_at: '2026-06-28T22:42:07.978411+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - GISS ABRASAF - Extrator fiscal
  - GISS ABRASAF
type: support-article
updated_at: '2026-04-24T14:15:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31670844301591-Cross-Segmentos-Backoffice-Protheus-TAF-GISS-ABRASAF-Extrator-fiscal-GISS-ABRASAF
---

**Dúvida**  
 Como integrar os dados da GISS Abrasaf no TAF via extrator fiscal, Abaixo passo a passo para utilização da rotina Extrator fiscal(***EXTFISXTAF*****)**, na integração dos dados da GISS ABRASAF, nesse formato de integração será necessário preenchimento de 3 campos manualmente no **TAF.**

IMPORTANTE: A rotina oficial de integração da GISS abrasaf é o TSI conforme indicado no boletim técnico da rotina, liberado pelo time de produto.

<https://tdn.totvs.com/pages/releaseview.action?pageId=878920036>

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31670930054807)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal- Todas as versões.  
  
**Solução**

**Livros Fiscais -> Miscelânea -> Arq. Magnéticos -> Extrator Fiscal (EXTFISXTAF)**.

**OBS**: O extrator fiscal gera os dados diretamente na TAFST2 para clientes que utilizam o TAF como módulo. A TAFST1 não é utilizada.

  Atenção aos parâmetros a serem preenchidos na *Wizard* do **Extrator Fiscal**.

Pasta: **Geração**

**Data de?** = Obrigatório conter o período de extração preenchido.

**Data até?** = Obrigatório conter o período de extração preenchido.

**Tipo de Saída?** = Banco a Banco.

**Deseja integrar?**  1- Somente cadastros:  **(Serão extraídos todos os cadastros presentes no Layout TAF, sendo necessário selecionar os cadastros específicos para a GISS ABRASAF)** Utilize esta opção para carga inicial no **TAF**, sendo necessário executa-la uma única vez.   2**-**Somente Movimentos:  **(Serão extraídos todos os movimentos presentes no Layout TAF, sem opção de selecionar um movimento específico)**  
  3**-**Ambos: **(Serão apresentados todos os cadastros e movimentos presentes no Layout TAF, sendo possível selecionar os cadastros e movimentos a serem gerados)** Lembramos que ao selecionar os cadastros presentes nesta opção, serão considerados apenas os cadastros realizados dentro do período de extração dos dados.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31670930056215)

**Filtra Apenas Reinf?**  Para extrair as informações para a **GISS ABRASAF**, preencher = 2- NÃO.

Pasta:**Movimento**

Tipo de Movimento? = 1-Ambos

Nota Fiscal de? = BRANCO

Nota Fiscal até? = ZZZZZZ

Serie de? = BRANCO

Serie até? = ZZZ

Pasta: **Apuração / SPED**

  Centralizar apurações e totalizadores em uma única filial? = 1-Não

**Observação:**

  Abaixo relação dos Layout essenciais para geração da **GISS ABRASAF**:

**Deseja integrar**:  1 - Somente Cadastros

**Filtra Reinf**: 2 - Não,

Selecione os *Layouts* de Cadastros**, T003, T005, T006, T007, T009, T010 e T011.**

  Após a **Extração Fiscal** ser concluída para os *Layouts* de cadastro acima, execute a rotina de processamento, conforme passo **5-Processamento** e **6-Gerenciador de Integração.**

  Após concluir o ajuste das inconsistências (se houverem) apresentadas no gerenciador de integração, conforme passo 6, realize a extração fiscal dos movimentos **T013, T154, T157** com as perguntas:   
  
**Deseja integrar**: 3 - Ambos

**Filtra Reinf**: 2 - Não

**Observação:**Para as entregas dos meses seguintes da **GISS ABRASAF**, basta realizar a extração com a pergunta **Deseja integrar**: Ambos e marcar tanto os *Layouts* de **cadastro** quanto os de **movimento**, pois serão considerados somente os cadastros realizados dentro do período. Desta forma, garantiremos que não faltem dados inclusos recentemente para entrega da obrigação fiscal no **TAF** e não ocorrerá erros na falta de algum cadastro novo.

*Layouts*: **T003, T005, T006, T007, T009, T010, T011, T013, T154, T157.**

  Após a**Extração Fiscal** ser concluída para os *Layouts* acima, execute a rotina de processamento, conforme passo **5-Processamento** e **6-Gerenciador de Integração**

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como consultar o gerenciador de integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-consultar-o-gerenciador-de-integra%C3%A7%C3%A3o)

  Após integração dos dados no TAF, acesse os documentos fiscais que foram integrados na rotina **documento de entrada(TAFA062E**) e preencha os campos abaixo manualmente.

Documento de entrada - ***TAFA062E*** - C20\_DTCPIS

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31670844288407)

Documento de entrada - ***TAFA062E*** - C30\_DESCRI

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31670930061463)

Natureza de operação - ***TAFA059*** - C1N\_CODEXI

![Captura de tela 2025-04-25 151133.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31670930062999)
