---
content_hash: ba662db3d171179bd2d3ced541be92d8c5aaaf035cddf60b29d245a38f0fc685
fetched_at: '2026-06-29T00:10:20.201021+00:00'
page_id: '489771317'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Excluir Registro da Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489771317
version: 26
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Excluir Registro da Tabela" tem por função, realizar a exclusão de um registro qualquer de uma determinada tabela.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos da atividade "Excluir Registro da Tabela":

**Atividade:**

* **Nome:**Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**RM.NET:**

* **Chave Primária:** Chave(s) primaria(s) da tabela utilizada.
* **Dados do Usuário:** Dados de usuário de parâmetro da execução da Atividade.
* **Nome da Tabela:**Nome da Tabela onde será executada a operação.
* **Submeter ao Banco:** Definir se o registro também será excluído do banco de dados.
* **Tabela de Origem:**Nome da tabela de origem utilizada (Data table a ser filtrado).

    Como exemplo, vamos utilizar a atividade para excluir um registro da tabela de Perfis (GPERFIL).

    Segue a abaixo o passo a passo para criação da fórmula:

    Após a criação da fórmula, adicione as seguintes atividades no Fluxo de Trabalho Sequencial:

* Ler Visão (Para mais informações sobre essa atividade [Clique Aqui](http://tdn.totvs.com/x/ogLvC))
* Excluir Registro da Tabela

    Nas propriedades da atividade "Ler Visão" adicione no campo "Filtro" o código do registro que deseja excluir (Ex de como deve ser aplicado: CODPERFIL = "Teste") e o nome do        "Data Server" utilizado (Ex: GlbPerfilData).

     Em seguida nas propriedades da atividade "Excluir Registro da Tabela" adicione no campo "Chave Primaria" as chaves primeiras da tabela utilizada (Ex de como deve ser                   aplicado: msReadViewActivity1.CODSISTEMA;rmsReadViewActivity1.CODPERFIL), Em seguida informe o nome da tabela (Ex: GPERFIL) e no campo "Tabela Origem"                     adicione novamente o nome da tabela, mas referenciando a mesma  pela atividade "Ler Visão" (Ex de como deve ser aplicado: Activity=rmsReadViewActivity1,                                     Path=Tables["GPerfil"].DataTable). 

Clique em "Salvar e Executar". Verifique que a formula foi executa e o registro excluído corretamente.
