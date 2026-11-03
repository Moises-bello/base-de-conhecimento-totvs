---
article_id: 8423200910487
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: fec7cf73c4f20ec9b571a296bab8844c7f47cffa29fa7d3878cb44abb21d9983
fetched_at: '2026-06-28T22:39:48.814110+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Catálogo de Produtos
  para tratativa da DUIMP.
type: support-article
updated_at: '2024-06-19T18:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8423200910487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cat%C3%A1logo-de-Produtos-para-tratativa-da-DUIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17676472673431) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**  
Gostaria de saber mais sobre o Catálogo de Produtos que irá atender ao novo Processo de Importação, referente a nova exigência da Receita Federal para tratativa da DUIMP.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – a partir da versão 12.1.27

**Solução**No processo o **Catálogo de Produtos** será o módulo responsável por viabilizar a declaração dos produtos em momento anterior à operação de importação, desta forma a **DUIMP** irá conter os dados específicos da operação e fará referência a registros do Catálogo de Produtos com as definições dos produtos.   
Esta rotina permite a inclusão de Catálogo de Produtos para isso preencha os campos necessários.

**Passos:**

1. 1. Obs.:  Ao preencher o campo Produto de Referência perceba que foram "**gatilhados"** automaticamente os dados: Descrição do Produto, **NCM**, Descrição da **NCM**, **Unidade de Med.** Estat. e os Dados do produto na linha do grid Relação de Produtos.
2. Preencha o(s) Produto(s) no grid "**Relação de Produtos**".
   1. Ao pressionar **F3** ou clicar na lupa, os Produtos que serão mostrados/filtrados na tela serão os que tem **NCM** igual ao Produto referência(capa) e Produtos Importados(**SIGAEIC**).
   2. É possível remover o filtro, selecionar um produto de **NCM** diferente do Produto de Referência do cabeçalho e, será mostrada uma mensagem Perguntando se Deseja Prosseguir.
   3. Caso haja cadastro de registro na rotina **Produto x Fornecedor/Fabricante**, será perguntado se deseja carregar a lista de Fabricantes relacionados ao produto.
3. Preencha o(s) Fabricante(s) ou País(es) de Origem no grid "**Relação de Países de Origem e Fabricantes**".
   1. A informação de país de origem é obrigatória no registro, portanto caso não seja informado um fabricante, o sistema permitirá informar manualmente apenas o país de origem existente no cadastro.
   2. Ao pressionar **F3** ou clicar na lupa, os Fabricantes serão mostrados na tela para seleção.
   3. Ao digitar um Fabricante a loja será "**gatilhada"**, caso seja outra loja a desejada, digite manualmente.
   4. Ao digitar um fabricante, o sistema irá consistir contra o cadastro se existe o país de origem informado e preencherá automaticamente esta informação. Caso não exista o país de origem no cadastro, o sistema não permitirá utilizar este fabricante, sendo necessário ajustar o cadastro deste fabricante com o país de origem.
   5. Ao digitar um fabricante, caso exista este fabricante no cadastro de Operador Estrangeiro, serão exibidas as informações que estão no **Operador** **Estrangeiro**, caso não encontre, serão exibidas as informações do cadastro de **Fornecedor/Fabricante**, e ao Salvar o **Catálogo de Produtos** os registros dos fabricantes do catálogo que não existam no cadastro de **Operador Estrangeiro** serão automaticamente inseridos no cadastro de **Operador Estrangeiro**.
   6. não será permitido informar Fabricante cujo **Operador Estrangeiro** está com Cadastro definido como "**Bloqueado?**" - "**Sim**". Será informado na tela que não é possível selecionador Operador Estrangeiro com cadastro bloqueado.
4. Preencha o(s) Atributo(s) no grid "**Relação dos Atributos**".
   1. Permite informar os valores de acordo com o tipo de informação do atributo. **Exemplos**: Texto, Numérico, Booleano, etc.

**Exemplo do procedimento**

**Saiba mais**  
[Catálogo de Produtos](https://tdn.totvs.com/pages/viewpage.action?pageId=549491819)  
[Procedimento para Implantação DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=657762135)  
[EIC 001 - FAQ - Novo processo de Importação - Portal Único](https://tdn.totvs.com/pages/releaseview.action?pageId=788602791)
