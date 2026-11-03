---
content_hash: 1cfa64b212190d598e73b8215983dd12bff3daadb938a8be8d92d2c2c4bccac1
fetched_at: '2026-06-29T00:11:42.940080+00:00'
page_id: '799270888'
product: rm
source: tdn-rm
title: Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799270888
version: 7
---

O **Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas** tem como finalidade facilitar a migração de dados entre essas entidades.

Importante

Disponível a partir das versões: 12.1.2306.182 e superiores

**Informações importantes/Regras básicas:**

* Apenas processos de um tipo específico, a ser selecionado no assistente, serão considerados. No entanto, você pode consistir mais de um tipo, mas nesse caso, o processamento precisará ser realizado separadamente.
* Os processos devem ter uma numeração de 15 ou 20 caracteres alfanuméricos. Caracteres especiais não são considerados.

A vinculação dos dados de Processos Jurídicos com os Processos Trabalhistas só ocorrerá para os registros considerados "Aptos para Sincronia". Isso implica que os reclamantes devem ser pessoas ou funcionários, conforme os cenários a seguir:

* É necessário que haja pelo menos um Reclamante no processo definido como Pessoa ou Funcionário.  (**Outros tipos de reclamantes não são considerados**).
* Um reclamante do tipo pessoa deve também possuir um registro de funcionário, independentemente de sua situação atual no sistema.

  + Funcionário é identificado pelo preenchimento da Chapa.
  + Uma pessoa só será considerada se possuir um vínculo de funcionário.
    - Registros de Pessoas que possuem mais de um vínculo de funcionário no sistema (ou seja, mais de uma chapa) não terão seu vínculo realizado automaticamente pelo assistente. O usuário precisará editar o registro na próxima etapa deste assistente, clicando duas vezes sobre o registro, e vincular a chapa adequada. Após esse procedimento, o registro será considerado "Apto Sincronia".
    - Registros que não possuem chapa e apresentam o status de "Inapto Sincronia" serão desconsiderados na execução do processo.

Na etapa de "Registros para Vinculação", as seguintes informações devem ser preenchidas e contempladas:

* *Vincular o Tipo de Processo:* Este item funciona como um filtro, onde apenas os processos do tipo selecionado serão exibidos para seleção no campo "Número do Processo."
* *Selecionar o Número do Processo* (Opcional): Se este item não for preenchido, todos os processos do tipo informado na vinculação serão listados.
* *Carregar os Processos*: Carrega as informações vinculadas do processo com a pessoa/funcionário.
* Realizar as devidas adequações nos registros dos Reclamantes: É necessário fazer ajustes, se necessário, nas chapas para registros do tipo pessoa.
* Selecionar a opção "Confirma operação conforme os critérios anteriormente informados?" para avançar o assistente.

Veja também

[Comparativo de Campos: Processos Jurídicos x Assistente de Vinculação de Processo Jurídico a Processo Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=799272048)

[Comparativo de Campos: Processos Jurídicos x Processos Trabalhistas](https://tdn.totvs.com/pages/viewpage.action?pageId=799272153)
