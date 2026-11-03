---
content_hash: 32ecb59c18e70e01aa5aae8c35b58dea525bfc786f1c0fd532c163942ef27930
fetched_at: '2026-06-29T00:08:40.963378+00:00'
page_id: '286519333'
product: rm
source: tdn-rm
title: RMCTB00006_Atualização da Data de  Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286519333
version: 11
---

# Assunto

|  |  |
| --- | --- |
| Produto: | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | **Atualização da Data de Inclusão** |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Este processo permitirá ao usuário atualizar a Data de Inclusão de várias contas contábeis ao mesmo tempo, basta marcar a conta desejada, acionar o processo e informar a data de inclusão. A data informada será incluída simultaneamente em todos os registros marcados.  Ao incluir uma conta contábil é obrigatório informar a Data de Inclusão. A data do dia será sugerida como data de inclusão, podendo neste momento antes de salvar a inclusão do registro, ser modificada.  A data de inclusão é essencial para a geração do Sped Contábil, já que as contas sem data de inclusão não são listadas nesta rotina.  **DESENVOLVIMENTO/PROCEDIMENTO**  1 - Acesse: Cadastros / Contábil / Selecione a conta a ser alterada e clique em Processos / Atualização da Data de Inclusão:  2 - Este processo permitirá ao usuário inserir/atualizar a data de inclusão de várias contas contábeis ao mesmo tempo: |
| **Observações:** | * Não será possível gerar o SPED Contábil caso haja no cadastro de contas contábeis algum registro em que a ‘Data de Inclusão’ esteja em branco. * As contas contábeis que tiverem datas de inclusão maiores que a data final da escrituração gerada para o SPED Contábil não serão enviadas para o registro I050 do arquivo digital, porém, se para estas mesmas contas existirem movimentações no período da escrituração, estas contas serão enviadas normalmente para o registro I050 com suas respectivas datas de inclusão assim como suas movimentações e, neste caso, como as datas de inclusão destas contas são maiores que a data final da escrituração, serão apresentadas Advertências ao validar o arquivo digital no PVA (Programa Validador do SPED Contábil). |
