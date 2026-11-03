---
content_hash: 3e15edc7a3e3aa9184b46b4e1c74ea7bbd22464b756f33023f2701eefc42ca3f
fetched_at: '2026-06-29T00:08:40.087702+00:00'
page_id: '286206653'
product: rm
source: tdn-rm
title: RMCTB00006_Atualização da Data de Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286206653
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO CONTÁBIL |
| **Versões:** | 12.1.16 |
| **Ocorrência:** | Atualização da Data de Inclusão dos Centros de Custos |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**   Ao incluir uma conta contábil, conta gerencial ou um centro de custo é obrigatório informar a Data de Inclusão. A data do dia será sugerida como data de inclusão, podendo neste momento antes de salvar a inclusão dos registros, ser modificada. A data de inclusão é um dado obrigatório na geração do SPED Contábil.  **Como Fazer:**  Para as contas contábeis, contas gerenciais e centros de custos já incluídos na base e cuja data de inclusão ainda esteja em branco, o preenchimento da data poderá ser feito editando-se os registros dos respectivos cadastros e preenchendo o campo Data de Inclusão com a data desejada ou através da execução do Processo Atualização da Data de Inclusão. Acesse o cadastro dos Centros de custos / selecione os Centros de custos desejados / Processos / Atualização da data de Inclusão:        Este processo permitirá ao usuário atualizar a Data de Inclusão de várias contas contábeis, contas gerenciais ou centros de custos ao mesmo tempo. Os procedimentos para a execução deste processo serão os mesmos para os três cadastros: Basta marcarem os registros desejados, acionar o processo e informar a data de inclusão. A data informada será incluída simultaneamente em todos os registros marcados. |
| **Observações:** | * Não será possível gerar o SPED Contábil caso haja no cadastro de contas contábeis ou contas gerenciais/centros de custos, algum registro em que a ‘Data de Inclusão’ esteja em branco.  * As contas contábeis, contas gerenciais ou centros de custos que tiverem datas de inclusão maiores que a data final da escrituração gerada para o SPED Contábil não serão enviadas para o registro I050 (Contas Contábeis) e I100 (Centros de Custos) do arquivo digital no exercício corrente, porém,  se para estas mesmas contas existirem movimentações no período da escrituração, estas contas serão enviadas normalmente para os registros I050 e I100 com suas respectivas datas de inclusão assim como suas movimentações e, neste caso, como as datas de inclusão destas contas são maiores que a data final da escrituração, serão apresentadas Advertências ao validar o arquivo digital no PVA (Programa Validador do SPED Contábil). |
