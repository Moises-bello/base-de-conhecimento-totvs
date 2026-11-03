---
content_hash: 3db6f17fed13be4cfbca951ef7de12496f489066d9c891d24ca9943615cbde7f
fetched_at: '2026-06-29T00:06:09.660998+00:00'
page_id: '203756031'
product: rm
source: tdn-rm
title: Novo Conceito - Como alterar a quantidade de registros por transação na conexão
  do tipo Banco de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203756031
version: 5
---

# Pré-requisitos

---

2
complete
Linha RM atualizada a partir da versão 11.82

# Objetivos

---

     Este documento tem como objetivo demonstrar como configurar a Conexão de Destino do tipo banco de dados para processar registros de 1 em 1. Auxiliando na identificação de possíveis erros como estouros de campos, etc.

# Procedimentos

---

      Para alterar o número de registros que serão processados por transação deve-se:

1. Editar a conexão de destino. Este exemplo é do tipo Banco de Dados:

2. Na propriedades *"**Registros por transação"* altere seu valor para 1:

3. Deve ser marcado o checkbox referente a opção*"Continuar a execução em caso de erros"*

     Dessa forma ao processar o conceito será exibido um log detalhado informando qual registro apresentou inconsistência, conforme print de exemplo abaixo:

OBSERVAÇÕES:

Clicando no ícone Bloco de Notas é exibido um arquivo de texto com o log completo referente à execução do conceito.

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82 e superiores |
| **Processo** | Conceito |
| **Subprocesso** | Conexão de banco de dados |

|  |  |
| --- | --- |
| **Status do documento** | Produção |
| **Data** | 29/09/2015 |
| **Versão** | 1.0 |
| **Versão anterior** | 1.0 |
| **Autores** | Raphael Bracarense Romano |
