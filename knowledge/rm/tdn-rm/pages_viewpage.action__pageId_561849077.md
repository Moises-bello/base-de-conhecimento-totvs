---
content_hash: 4a2bdf23a211ebb9d831656898ba58c3783d710ca939186574dba32ed6639ee2
fetched_at: '2026-06-29T00:10:48.409394+00:00'
page_id: '561849077'
product: rm
source: tdn-rm
title: DT- Alteração atestado x dias trabalhados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561849077
version: 3
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Ao realizar o lançamento da folha para funcionários, os valores são levados corretamente com suas devidas Referências. Ao realizar o Cadastro de um Afastamento e recalcular o envelope, o evento referente ao afastamento é lançado e o evento para pagamento (Código de cálculo 1 ou 2) é proporcionalizado na quantidade correta de dias afastado. Porém, ao realizar a exclusão do afastamento no histórico e recalcular o envelope, o evento de afastamento é removido como devido, mas não traz as informações corretas permanecendo o cálculo antigo constando o afastamento. |
| **Solução/Implementação:** | Criado o parâmetro " Recalcula dias trabalhados quando dias de direito for maior que o já existente no envelope" no Parametrizador e quando o parâmetro estiver marcado o cálculo retornará o valor de dias de direito no recálculo do movimento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-11494](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-11494) |
| **Documento de Referência:** | [Cálculo 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=561848185) |
| **Pacote:** | N/A |
