---
article_id: 360026398471
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b772db9871a6b8f35f26cbcfab02e16767b75e862d4d14fbdb1cdd7d28ed07b0
fetched_at: '2026-06-28T22:38:29.776242+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Como incluir campos ou colunas
  no Browse das rotinas de Faturamento
type: support-article
updated_at: '2026-02-13T21:14:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026398471-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Como-incluir-campos-ou-colunas-no-Browse-das-rotinas-de-Faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38393384492823)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**  
Como realizar a inclusão de novos campos ou colunas na visualização (Browse) das rotinas de Faturamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

As rotinas do módulo SIGAFAT são montadas sobre um layout pré-definido, exibindo colunas com os principais dados de uma tabela específica (Exemplo: A rotina **MATA450A** utiliza a tabela **SC9 - Pedidos Liberados**).

Para adicionar informações visualizadas no Browse, siga os critérios abaixo:

**1 - Campo pertencente à tabela padrão da rotina:**

* Se o campo que você deseja inserir já existe na tabela principal da rotina (ex: SC9), basta configurar o campo no **Dicionário de Dados (SX3)** para que ele seja exibido no Browse (propriedade `Visualizar` ou através da opção `Configurar` no próprio Browse da rotina): [Browse - Incluir campo](https://tdn.totvs.com/x/P1IxE)

**2 - Campo de outra tabela ou informação calculada:**

* **Campo de Usuário:** Crie um campo virtual ou real na tabela padrão (ex: SC9) para gravar/exibir o conteúdo desejado, e então configurar o campo para ser exibido no Browse com a orientação acima;
* **Ponto de Entrada:** Utilize o Ponto de Entrada[**Ponto de Entrada - M520BROW**](https://tdn.totvs.com/x/8YRn) ou equivalentes para manipular as colunas do Browse via código ADVPL. *Havendo dificuldades com a criação da função customizada, acione Suporte ADVPL do Protheus.*
* "[Configuração da tabela](http://tdn.totvs.com/pages/viewpage.action?pageId=273307679)" Em rotinas que permitem, acesse **Outras Ações > Configuração da Tabela > Colunas > Incluir Coluna**

**Observação**: Incluindo campos em rotinas MVC

As novas rotinas do sistema no qual são desenvolvidas em MVC muitas vezes não podem sofrer alterações em sua ordenação de Dicionário, por esse motivo para a inclusão de campos no browser se faz necessário a utilização de um Ponto de Entrada para esta edição.

Segue relação completa de P.E.s para análise: [Pontos de Entrada - Faturamento - Protheus 12](https://tdn.totvs.com/x/owQhH)
