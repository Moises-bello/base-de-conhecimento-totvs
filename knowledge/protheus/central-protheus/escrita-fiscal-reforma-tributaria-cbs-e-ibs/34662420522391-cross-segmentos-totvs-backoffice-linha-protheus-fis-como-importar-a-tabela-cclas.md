---
article_id: 34662420522391
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: c5091af7af66645f1aa7d7304573f02871255bfd11ba39f8018cecbe13a5fd68
fetched_at: '2026-06-28T22:39:15.807688+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela
  cClassTrib-IBS/CBS no Configurador de Tributos?
type: support-article
updated_at: '2025-11-20T22:01:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34662420492311) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2410  
  
**Solução**

O primeiro processo a ser realizado é atualizar o ambiente, pois sem essa etapa não conseguirá importar a tabela cClassTrib-IBS/CBS.

Após isso, deve aplicar o UPDDISTR.

Abaixo link da Expedição Continua:

[Expedição Continua](https://tdn.totvs.com/pages/releaseview.action?pageId=525823851)

---

Posteriormente, deve baixar a tabela do IBS/CBS.

A rotina processará somente arquivo do tipo ".CSV", portanto, a tabela original, que possui formato ".xlsx" (Planilha do Microsoft Excel), deverá ser transformada para o formato ".CSV". Como sugestão para esse procedimento, abra a tabela através do Microsoft Excel, opção "Salvar Como", selecione o Tipo "CSV (separado por vírgulas)" e salve o documento.

Como forma de validar o arquivo, será exigida a presença dos campos abaixo exatamente com esses nomes. Caso algum desses campos não exista no arquivo, será exibido um alerta na tela e a importação não será realizada.

CST-IBS/CBS  
Descrição CST-IBS/CBS  
cClassTrib  
Descrição cClassTrib

Para baixar a tabela, deverá acessar o portal da nfe.fazenda.gov.br, abaixo o link:

<https://www.nfe.fazenda.gov.br/portal/principal.aspx>

obs: a tabela terá atualizações, portanto sempre acompanhe os comunicados na nfe.fazenda.

Clique no Menu Documentos -> Diversos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34864769272087)

Identifique a última versão vigente da tabela e faça o download.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34864736968343)

Salve a planilha com o Tipo "CSV (separado por vírgulas)".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34864769276183)

---

E por último deve acessar a rotina Configurador de Tributos (FISA170) e realizar a importação da seguinte maneira.

Clique na pasta Regras Fiscais -> Cadastros -> Tabela cClassTrib -IBS/CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34662396326935)

#### 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34662396327959)

#### 

Após a importação da tabela, poderá criar as Regras de Escrituração conforme sua operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34662396331671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34662420502039)

#### 

Abaixo documentação sobre a adequação no Configurador de tributos.

#### [CFGTRIB - Adequação do Configurador de Tributos aos Códigos de Classificação Tributária do IBS, CBS e IS](https://tdn.totvs.com/pages/viewpage.action?pageId=962623217)
