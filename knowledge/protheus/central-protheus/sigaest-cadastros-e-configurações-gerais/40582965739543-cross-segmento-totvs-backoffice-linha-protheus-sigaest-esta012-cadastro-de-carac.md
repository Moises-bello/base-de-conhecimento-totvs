---
article_id: 40582965739543
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 264a27d3834dbd245a8c079fefd6d372ccb5f5859b4c41476586925c2f5334c6
fetched_at: '2026-06-28T22:39:09.790322+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - ESTA012 - Cadastro
  de Características de Produtos
type: support-article
updated_at: '2026-05-19T16:51:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40582965739543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-ESTA012-Cadastro-de-Caracter%C3%ADsticas-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40583008138391) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar o cadastro e a parametrização de Características de Produtos (rotina ESTA012) para padronizar e flexibilizar a gestão do catálogo no módulo Estoque?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12.1.2410  
  
**Solução**  
O cadastro de Características de Produto centraliza as classificações do catálogo, garantindo consistência por meio de regras e atributos padronizados (como cor, tamanho e voltagem). Essa estrutura otimiza a busca avançada de itens e previne erros de digitação ao eliminar textos livres na descrição técnica.

O controle é gerenciado através de duas tabelas nativas do sistema:

* **Tabela D4V**: Armazena o cabeçalho e as configurações gerais da característica de produto.
* **Tabela D4W**: Armazena os valores que compõem a lista de opções, quando o tipo selecionado exigir.

**Regras e Validações do Sistema:**

* Não é permitida a duplicidade de nomes para características;
* O sistema bloqueia variações de plural e singular para o mesmo termo (exemplo: Cor e Cores);
* Características configuradas como Lista de Opções exigem obrigatoriamente o cadastro de ao menos um valor;
* Características configuradas como Consulta Padrão exigem a indicação da consulta (tabela SXB) correspondente;

**Passos**

1. Acesse o módulo Estoque (SIGAEST);
2. Siga o caminho Atualizações -> Cadastros -> Produtos -> Características de Produto e clique na opção Incluir. (Caso não possua a opção no Menu, realize a[**inclusão via Configurador**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035446693-Framework-Linha-Protheus-Como-incluir-e-utilizar-menus-customizados-com-o-dicion%C3%A1rio-no-banco-de-dados));
3. No campo D4V\_NOME, informe o nome descritivo da característica de forma clara e objetiva;
4. No campo D4V\_TIPO, selecione o tipo de dado esperado para o atributo:
   * **Lista de opções**: Permite criar uma lista restrita de valores pré-definidos;
   * **Consulta Padrão**: Vincula o campo a uma consulta padrão do sistema (SXB). Exempo: Fornecedores (SA2);
   * **Livre**: Campo de texto aberto para digitação direta;
   * **Número**: Campo restrito a valores numéricos.
5. Defina o Tipo de Seleção (D4V\_TPSEL):
   * **Única**: Permite apenas um valor por produto;
   * **Múltipla**: Permite vincular mais de um valor ao mesmo produto (exemplo: compatibilidade com múltiplos modelos). Esta opção só é habilitada se o tipo for Lista de opções ou Consulta Padrão;
6. No campo D4V\_SECAO, selecione o agrupador visual para organizar as telas de cadastro. As seções padrão são: Comerciais, Logísticos, Fiscais/Financeiros, E-commerce, Aplicações e Técnicos.
7. Caso o tipo escolhido seja Lista de opções, acesse a grade inferior correspondente à tabela D4W e insira os itens permitidos preenchendo o campo D4W\_VALOR.

Confira os dados preenchidos e clique em Confirmar para salvar o registro.

**Saiba Mais**

[*Cadastro de características de produtos (ESTA012 - SIGAEST)*](https://tdn.totvs.com/x/HuxqP)

[*Categorização e caracterização de produtos*](https://tdn.totvs.com/x/N1LePQ)
