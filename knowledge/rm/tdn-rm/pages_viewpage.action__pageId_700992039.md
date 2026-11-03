---
content_hash: f2c0b1ae03f84c0c3001033b7781b893f0fd64f51ee32ee7fe159bfdeb68f99c
fetched_at: '2026-06-29T00:11:22.245910+00:00'
page_id: '700992039'
product: rm
source: tdn-rm
title: Importação/Exportação do Grupo de Produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=700992039
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

O processo de exportação do gerador de saída do Grupo de Produtos, possuir como finalidade gerar o arquivo txt com os dados da tabela TGRUPOPRODUTO.

Após a geração é possível importa o arquivo no conceito do Grupo de Produtos. para realizar o processo desta documentação é necessário ter o layout do

**layout do grupo de produto.**

## **02. EXEMPLO DE UTILIZAÇÃO**

**LAYOUT DE IMPORTAÇÃO**

Importe o layout do grupo de produtos, no módulo Integração/Gerador de saída:

**Entre em layouts:**

**Em processo, click no importar layout:**

**Adicione objeto com o arquivo de layout do grupo de produtos, em sequencia execute a tarefa.**

**GERAR ARQUIVO DE SAÍDA DO GRUPO DE PRODUTO**

No Gerador de saída, selecione o layout do grupo de produto em sequência click em geração de saídas.

**Selecione o diretório onde o arquivo vai ser salvo e avance.**

**Escolha o filtro para determina quais dados da tabela Grupo de Produto vai ser exportados:**

**Layout está configurado para exporta arquivo separados por ponto e virgular, caso possuir algum Grupo de Produtos com descrição contendo ponto e virgula, altere o separador de saída de ponto e virgula para algum caractere especial que não contenha na coluna de  descrição da tabela TGRUPOPRODUTOS, alteração deve ocorre no layout e no conceito. Observação.**

**Importa Conceito.**

Para realizar a importação de , é necessário antes, importar o layout de importação através da ferramenta Conceito, que compõe o TOTVS Integração.

Neste caso deve-se primeiro importar o layout de importação disponibilizado na pasta de objetos gerenciais.

* + Para acessar o Conceito, primeiro acesse o módulo **Integrações**, e navegue para a aba **Integração \ Conceito (ETL)**.
  + Na visão da tela do Conceito, selecione a opção **Processos \ Importar conceito.** Selecione o arquivo de conceito disponível na pasta de objetos gerenciais e informe o nome para a importação.
  + Após a importação selecione o conceito na visão e execute o processo **Processar novo conceito** selecionando o arquivo desejado.
  + Após a conclusão do processo os grupos de produtos informados no arquivo de importação estarão atualizados no sistema.

O Layout do conceito pode ser customizado para se adequar a realidade de cada empresa. Para conhecer e obter informações sobre o Conceito acesse .

Recurso disponível a partir da versão 12.1.2209 do TOTVS Linha RM.IMPORTANTE!
