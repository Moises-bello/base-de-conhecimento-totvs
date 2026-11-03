---
content_hash: d1f06cfb1e3e58eb0080140fdbfc5464ad57516a1f4417d7c318ca760ea5b24c
fetched_at: '2026-06-29T00:09:28.472808+00:00'
page_id: '423938681'
product: rm
source: tdn-rm
title: Gerar Plano de Contas Paralelo a partir do Plano de Contas Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938681
version: 4
---

O processo tem como objetivo gerar o plano de contas paralelo a partir de um plano de contas contábil que possua máscara. Além de gerar o novo plano paralelo ainda existe a possibilidade de mapear automaticamente as contas contábeis que foram utilizadas como modelo na geração das contas paralelas.

A tela possui os seguintes campos:

1. Coligada do Plano de Contas Contábil: Esta opção lista todas as coligadas disponíveis para ser utilizada no processo de geração do novo plano paralelo.
2. Código do Plano Paralelo: Código do novo plano de contas paralelo. O código deve ser diferente de um já cadastrado para coligada que está executando o processo.
3. Descrição do Plano Paralelo: Descrição do plano de contas paralelo. O campo pode conter no máximo 40 caracteres.
4. Grupo de Contas: Grupos de contas que serão utilizados para serem a base das novas contas paralelas que serão criadas.
5. Instituição Responsável / Finalidade: Esta opção lista todos os tipos de plano paralelo que podem ser utilizados pelo processo.
6. Associar as contas da coligada selecionada ao Mapeamento do Plano Paralelo: Define se as contas paralelas serão associadas automaticamente as contas do plano de contas contábil da coligada informada.
7. Grupo Empresarial: Caso a Finalidade do Plano Paralelo a ser gerado seja "Consolidação de Saldos" será necessário informar o Grupo Empresarial utilizado para a consolidação.

**Exemplo:** Se o código da conta paralela for 1.01.001 ela será associada a conta contábil 1.01.001.

Vale ressaltar que esta opção será habilitada somente se a coligada selecionada for igual a coligada corrente.

O campo "Associar as contas da coligada selecionada ao Mapeamento do Plano Paralelo" não é obrigatório para execução do processo.

Os Grupos Empresariais disponíveis para seleção serão os grupos em que a Coligada corrente é a Holding ou Investidora de alguma outra Coligada do Grupo.

Os dados da conta paralela serão idênticos aos da conta contábil que deu origem a ela, porém se o campo "Natureza da conta para emissão do SPED" for "Não informada" a natureza para emissão do SPED, da conta paralela, irá buscar essa informação da conta contábil de nível superior.

**Exemplo:** Se o campo "Natureza da conta para emissão do SPED", da conta contábil 1.01.001, for "Não informada" então a conta paralela gerada a partir dela receberá a natureza da conta 1.01.
