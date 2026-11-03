---
content_hash: 9e0d90fff82d9f1b32fab00198aa4c46719ea390f73adbe4a9f72680b4d328af
fetched_at: '2026-06-29T00:09:14.822141+00:00'
page_id: '421385269'
product: rm
source: tdn-rm
title: Exportação de Motivos de Improdutividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385269
version: 3
---

---

O coletor móvel necessita de um cadastro de motivos de improdutividade para a realização de apontamentos das horas improdutivas de equipamentos, porém esses motivos de improdutividade devem ser os mesmos que estão cadastrados no TOP e no Manutenção de Ativos.  
 Para que isso seja possível, o TOP recebe os motivos de improdutividade provenientes do Manutenção de Ativos, enquanto o TOP Mobile recebe os motivos de improdutividade exportados pelo TOP (os motivos de produtividade não são importados, pois os apontamentos produtivos não necessitam que seja informado o motivo).

**Importante:**

* Em caso de erros durante a exportação, os dados do erro serão gravados na tabela de logs do TOP e poderá ser enviado um e-mail para o usuário/grupo parametrizado informando o erro ocorrido.

**Passos para Exportar para o Coletor Móvel os Motivos de Improdutividade:**

1. Fazer sincronismo no TOP Mobile;
2. O coletor móvel verifica a necessidade de atualizar os dados;
3. O coletor móvel envia ao TOP solicitação para atualizar os motivos de improdutividade;
4. O TOP valida se o usuário do coletor móvel possui permissões para obter os motivos de improdutividade;
5. O TOP envia para o coletor móvel os dados atualizados;
6. O coletor móvel atualiza os motivos de improdutividade salvos.
