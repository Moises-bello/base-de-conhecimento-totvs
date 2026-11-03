---
article_id: 360025225292
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 9ca5b28d0f2116331674c33e77c42849b0de12ed58823293382b8cc8c281396f
fetched_at: '2026-06-28T22:39:22.211245+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Divergência entre
  a Apuração de ICMS e o Regime de Processamento de Dados
type: support-article
updated_at: '2021-07-15T17:42:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025225292-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Diverg%C3%AAncia-entre-a-Apura%C3%A7%C3%A3o-de-ICMS-e-o-Regime-de-Processamento-de-Dados
---

**Dúvida**

**Divergência entre a Apuração de ICMS e o Regime de Processamento de Dados**

**Ambiente**Protheus - Livros Fiscais  - A partir da versão 11.80  
  
   
**Solução**

Divergência entre a Apuração de ICMS e o Regime de Processamento de Dados

Foi desenvolvido o parâmetro **MV\_CODRSEF,** que controla os códigos de retorno da SEFAZ, os quais são gravados após a transmissão das notas fiscais no campo **F3\_CODRSEF.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024403971/mceclip0.png)

A rotina MATR930 não tem controle dos códigos de retorno como a Apuração de ICMS. Caso a nota gere Livros Fiscais (L.Fisc.ICMS = Sim/L.Fisc.IPI=Sim), será demonstrada no Relatório Regime de Processamento de Dados (MATR930) por conter informações nos livros (SFT/SF3). Porém, para que esta nota também seja considerada na Apuração de ICMS (MATA953), deve ser verificado o conteúdo do campo**F3\_CODRSEF** e validar se o código em questão existe no parâmetro **MV\_CODRSEF.**

* A equipe fiscal da empresa é responsável por verificar se o código de retorno é válido ou não para ser considerado na Apuração de ICMS. Ao incluir um código de retorno correspondente à uma Rejeição, as notas que tiverem com o campo**F3\_CODRSEF**preenchido com este código, também serão consideradas na Apuração de ICMS.
* Após a transmissão da nota é necessário que ela seja visualizada no “Monitor” do Faturamento. Esta rotina é responsável por gravar o código de retorno da SEFAZ no campo Existem casos em que algumas notas não são consideradas pelo fato de inicialmente terem sido Rejeitadas. Após isto, é possível efetuar a devida correção e fazer a transmissão autorizada, sem visualizar novamente o "Monitor". A nota é transmitida, porém, o campo **F3\_CODRSEF** continua com o código da Rejeição por não ter sido verificada após a transmissão.

**Procedimento para análise:**

**1º Abra a APSDU, selecione a tabela SF3 e filtre os CFOPs em que constam os valores divergentes;**

**2º Verifique no campo F3\_CODRSEF das tabelas filtradas se possuem os códigos de retorno do SEFAZ. Ex: 102, 103;**

**3º Os códigos que estiverem no campo F3\_CODRSEF devem ser iguais aos do parâmetro MV\_CODRSEF. Caso não esteja com a mesma informação, preencha o parâmetro MV\_CODRSEF com os mesmos códigos do campo F3\_CODRSEF.**

**OBS:** O conteúdo do parâmetro MV\_CODRSEF deve estar entre aspas simples, conforme imagem abaixo:

Conteúdo padrão: '','100'

![Screenshot_11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070566954/Screenshot_11.png)

Boletim Técnico: <http://tdn.totvs.com/pages/releaseview.action?pageId=185739255>
