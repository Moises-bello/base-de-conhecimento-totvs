---
content_hash: 066a2365e4f0d18757c1c2f244d102b8df2c6fcee96bcdb9cf38d38626bbcc51
fetched_at: '2026-06-29T00:10:27.051706+00:00'
page_id: '516208592'
product: rm
source: tdn-rm
title: Utilizando a atividade "Salvar Registro"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516208592
version: 5
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Salvar Registro" tem por função salvar um registro que esta sendo adicionado a uma visão.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Salvar Registro":

**Atividade:**

* **Nome:** Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:**Define se a atividade estará em uso ou não.

**Diversos:**

* **Atividade Ler Registro:** rmsReadRecordActivity1 (para saber da onde esta vindo as informações que serão salvas)

**RM.NET**

* **Conjunto de Dados:** Retorno do arquivo enviado em transformado em bytes
* **Dados do Usuário:** Dados do usuário(OwnerData) de parâmetro da execução da atividade
* **Nome do DataServer:** Nome do servidor que executará a ação da atividade
* **Registros Alterados:** Número de registros que foram alterados na execução da atividade

Como exemplo, vamos montar um fluxo para ler uma visão, adicionar um registro na visão e salvar esse registro adicionado.

* Foi adicionado uma atividade de "Ler Registro" para chamar o Data Server da Tabela Utilizada (GlbPerfilData)
* Em seguida foi utilizada a atividade "Adicionar Registro na Tabela" para adicionar os dados do registro que vai ser criado e referenciar em qual tabela está sendo criado
* Para finalizar a fórmula foi adicionado a atividade "Salvar Registro" para salvar o registro que está sendo criado, passando como informação o data server utilizado e referenciando a atividade de "Ler Registro"

Segurança na Atividade

A partir das versões **12.2302.104**,  **12.1.2209.176**, **12.1.2205.230** para que a atividade valide as permissões do Usuário que está executando a Formula visual e aplique a mesma segurança do **Data Server** é necessário habilitar a propriedade 'Aplicar segurança nas atividades do fluxo de trabalho'.
