---
article_id: 360020160271
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: dccaf72e60045e3ea3075535190ffe4770999b259a2065bb9a0ddc0bfa487cd9
fetched_at: '2026-06-28T22:38:28.540399+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de
  numeração via Tabela Genérica SX5
type: support-article
updated_at: '2023-08-15T14:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020160271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-via-Tabela-Gen%C3%A9rica-SX5
---

**Dúvida**

Como tratar Controle de numeração via Tabela Genérica SX5?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Essa opção é a mais antiga do Protheus. Ela se baseia unicamente na SX5 - Tabela de séries do Protheus para incrementar a numeração.

O controle de numeração via **SX5** realiza lock (trava de segurança) na Tabela SX5 de séries e no parâmetro **MV\_NUMITEN** para reservar a numeração. Caso possua grande volume de Faturamento, recomenda-se a utilização da opção 3 - **SD9** para evitar lock de registro por concorrência.

Premissas para correto funcionamento do controle de numeração:

* Ao utilizar a **SX5** para o controle de numeração, se houver necessidade de utilizar numeração exclusiva por Filial (cada Filial possui sua sequencia individual) então é necessário trabalhar também com séries exclusivas. Adeque o ambiente de acordo com o item "**Exclusividade de Séries**" ([**Exclusividade de Séries por Filial**](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579#FAT0049ControledeNumera%C3%A7%C3%A3odeDocumentodeSa%C3%ADdanoProtheus-ExclusividadedeS%C3%A9ries))

Ajuste para sugerir a numeração correta:

* Verifique o último/maior número de Nota gravada na **SF2** (nota "000009" por exemplo) a partir da qual deseja dar sequência. Atente-se à numeração de acordo com a Filial **F2\_FILIAL**
* Acesse o Configurador > Tabelas Genéricas
* Localize a **X5\_TABELA** = 01 e na **X5\_CHAVE** localize a **SERIE** utilizada para gerar a Nota (nesse exemplo, Serie 1): X5\_TABELA = 01 e X5\_CHAVE 1
* Nessa mesma linha, no campo X5\_DESCRI preencher com um número maior que a última nota gerada. Ex: X5\_DESCRI "000010"
* Assim o sistema irá recomeçar a numeração a partir da "000010".
