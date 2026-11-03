---
content_hash: 8ed6493ce831c84633acb64cfe4e944d03cc796aea0db9e8b74a7804684d4b4f
fetched_at: '2026-06-29T00:08:51.015130+00:00'
page_id: '336398420'
product: rm
source: tdn-rm
title: DT - Copiar Parâmetros Entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336398420
version: 2
---

# Copiar Parâmetros Entre Coligadas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Configurações |
| **Função:** | Copiar Parâmetros Entre Coligadas |
| **Situação/Requisito:** | Copiar Parâmetros Entre Coligadas |
| **Solução/Implementação:** | O processo de "Copiar Parâmetros Entre Coligadas" foi criado para facilitar o processo de parametrização de múltiplas coligadas. Após parametrizar a primeira coligada, é possível executar o processo para copiar as informações para as outras coligadas selecionadas. |

**Executar a cópia de parâmetros entre as coligadas:**

Acesse o novo item de menu criado no grupo de Configurações.

Na primeira tela, selecione as telas que possuem os parâmetros que deseja copiar. Na parte inferior selecione o comportamento caso o parâmetro já exista na coligada destino: Substituir os valores ou ignorar o parâmetro.

Na segunda tela é possível selecionar as coligadas para as quais deseja copiar os parâmetros da coligada atual. É possível selecionar mais de uma coligada. Não existem parâmetros específicos a serem configurados nessa tela.

Ao finalizar as seleções, basta mandar executar o processo. Ao final da execução será apresentado o log com as coligadas que foram atualizadas com sucesso, bem como possíveis mensagens de erro.

Atenção:

* Caso o sistema encontre erro copiando os parâmetros para alguma coligada, o processo continuará executando para as demais.
* Antes de executar a cópia de parâmetros, é necessário verificar que os eventos, relatórios etc que são referenciados nos parâmetros também existem na coligada de destino. O processo de cópia dos registros para a coligada destino é de responsabilidade do usuário e não será contemplado no processo de cópia de parâmetros.
