---
content_hash: 01f294b9687aad53daabcd8fc48bc3d56af8226d71a9cd28499efd7757eb7025
fetched_at: '2026-06-29T00:11:12.617616+00:00'
page_id: '655644434'
product: rm
source: tdn-rm
title: Importação de Posição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655644434
version: 5
---

**Disponível a partir da versão 12.1.34**

Através deste processo será possível importar uma ou mais posições através de uma consulta SQL. Para realizar a importação alguns fatores são presumidos.  
São eles:

* Se informado a hierarquia que será associada a posição, a mesma já deverá estar previamente cadastrada;
* Se informado a chapa do funcionário que ocupará a posição, o mesmo já deverá estar previamente cadastrado;
* A sentença SQL deve estar cadastrada em TOTVS Gestão de Pessoas

**Detalhamento de Campos**

**Fonte de Dados - Sentença SQL**

Para importação será necessário realizar a seleção da sentença SQL que contenha as devidas informações.

**Importante !**A consulta SQL deverá conter os seguintes campos:

**-** CODCOLIGADA(INT);

Representa o Código da Coligada. Valor do tipo inteiro. Envio obrigatório.

**-** IDPOSICAO(INT);

Representa o ID da Posição. Valor do tipo inteiro. Envio obrigatório.

**-** IDHIERARQUIA(INT);

Representa o código da hierarquia que é necessário existir no sistema. Valor do tipo inteiro. Envio obrigatório.

**-**CHAPAFUNCIONARIO(VARCHAR);

Representa a chapa do funcionário que será associado à posição. Valor do tipo alfanumérico. Envio obrigatório.

**-** STATUS;

Representa o status da Posição. Enviar valor 0 (Inativo) ou 1 (Ativo). Envio obrigatório.

**-**HIERARQUIADELOTACAO(INT);

Representa se a Hierarquia informado é de lotação ou não do funcionário. Enviar valor 0 (Caso não seja de lotação) ou 1 (Caso seja hierarquia de lotação). Envio obrigatório.

**O que fazer com os registros já existentes ?**

Ao marcar a opção **Substituir,**caso já exista uma posição na base de dados com o mesmo ID informado na consulta SQL, essa posição terá seus dados substituídos.

Ao marcar a opção **Não Substituir,**caso já exista uma posição na base de dados com o mesmo ID informado na consulta SQL, essa posição não será importada.

**Posições encontradas**

Após selecionar a consulta SQL e clicar em Consultar será listado na caixa as informações da posição informada na Consulta SQL.

**Flag Deletar Hierarquias existentes**

Com a opção marcada, serão removidas todas as hierarquias vinculadas as posições listadas no resultado da sentença SQL.

Ou seja ao marcar a opção Substituir e Deletar Hierarquias Existentes, antes da realizar a importação da posição, será feita a exclusão de todas as hierarquias vinculadas as posições informadas na consulta SQL.

**Links Importantes e Complementares:**
