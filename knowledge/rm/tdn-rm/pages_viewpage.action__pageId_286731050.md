---
content_hash: 95450170a051635ffbdb22b7440b7777e24aa796eef55559ed518ae7a6714176
fetched_at: '2026-06-29T00:08:41.490128+00:00'
page_id: '286731050'
product: rm
source: tdn-rm
title: RMCTB00004_Cópia de Contas Gerenciais entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286731050
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Cópia de Contas Gerenciais entre Coligadas |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Para agilizar e facilitar o cadastro, uma Conta Contábil ou Gerencial já cadastrada em uma coligada poderá ser copiada de uma coligada para outra utilizando o processo para copiar contas:        **Regras Gerais**   * As máscaras entre as coligadas origem e destino devem, obrigatoriamente, ser iguais para que a cópia seja efetuada; * Contas globais não poderão ser copiadas; * No processo de cópia, o sistema consistirá se na coligada destino já existe alguma conta (seja global ou não) com mesmo código da que está sendo copiada. Se já existir, a cópia não será efetuada; * Toda a hierarquia de contas sintéticas (todos os níveis anteriores, ou seja, os pais da conta que está sendo copiada) deve existir na coligada destino, caso contrário, a conta não será copiada; * Se para a cópia for selecionada, por exemplo, a conta sintética 1, será copiada apenas a conta sintética 1. Não será copiado todo o grupo 1 (as contas filhas do grupo 1 não serão copiadas); * Se a conta origem exigir rateio, a conta copiada também exigirá rateio, porém os rateios default da conta origem não serão copiados. A conta destino (cópia) ficará com rateio default vazio. (exclusivo para cópia de contas contábeis); * Os campos complementares não serão copiados;   **Parametrização Necessária**  1 - Selecione a conta a ser copiada e acesse o processo:      2 - Na tela seguinte o sistema abrirá a seleção da coligada destino: |
| **Observações:** |  |
