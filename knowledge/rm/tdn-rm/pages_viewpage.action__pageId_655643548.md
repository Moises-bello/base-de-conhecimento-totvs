---
content_hash: db8329c6f512e279275fe3e46a3011e193ee99c6f33ea0cf53e2a3224b52bc88
fetched_at: '2026-06-29T00:11:12.612117+00:00'
page_id: '655643548'
product: rm
source: tdn-rm
title: Importação de Hierarquia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655643548
version: 5
---

**Disponível a partir da versão 12.1.34**

Através deste processo será possível importar uma ou mais hierarquias através de uma consulta SQL. Para realizar a importação alguns fatores são presumidos.  
São eles:

* Os níveis de hierarquia retomadas pela sentença SQL já devem estar cadastrados.
* A sentença SQL deve retornar as hierarquias ordenadas pela estrutura. Exemplo: Hierarquia pai -> Hierarquia filha
* A sentença SQL deve estar cadastrada em TOTVS Gestão de Pessoas

**Detalhamento de Campos**

**Fonte de Dados - Sentença SQL**

Para importação será necessário realizar a seleção da sentença SQL que contenha as devidas informações.

**Importante !**A consulta SQL deverá conter os seguintes campos:

**-** CODCOLIGADA(INT)

Representa o Código da Coligada. Valor inteiro. Envio obrigatório.

**-**IDHIERARQUIA(INT)

Representa o ID da Hierarquia. Valor inteiro. Envio obrigatório.

**-** DESCRICAOHIERARQUIA(VARCHAR)

Representa a descrição/título da hierarquia. Valor do tipo alfanumérico. Envio obrigatório.

**-** IDNIVELHIERARQUIA(INT)

Representa o código do nível da hierarquia. Valor do tipo inteiro. Envio obrigatório

**-** IDHIERARQUIASUPERIOR(INT)

Representa o código da hierarquia superior. Enviar valor do tipo inteiro. Envio opcional.

**-** STATUS(INT)

Representa o status da hierarquia. Enviar valor 0 (Inativo) ou 1 (Ativo). Envio obrigatório.

**-**CODCALENDARIO(VARCHAR)

Representa o código do Calendário da Hierarquia. Valor do tipo alfanumérico. Envio Opcional.

**-**IDHIERARQUIAEXTERNO(VARCHAR)

Representa o código da Hierarquia Externa. Valor do tipo alfanumérico. Envio Opcional.

**Exemplo:**

**O que fazer com os registros já existentes ?**

Ao marcar a opção **Substituir,**caso já exista uma hierarquia na base de dados com o mesmo ID informado na consulta SQL, essa hierarquia terá seu dados substituídos.

Ao marcar a opção **Não Substituir,**caso já exista uma hierarquia na base de dados com o mesmo ID informado na consulta SQL, essa hierarquia não será importada.

**Hierarquias encontradas**

Após selecionar a consulta SQL e clicar em Consultar será listado na caixa as informações da hierarquia informada na Consulta SQL.

**Links Importantes e Complementares:**
