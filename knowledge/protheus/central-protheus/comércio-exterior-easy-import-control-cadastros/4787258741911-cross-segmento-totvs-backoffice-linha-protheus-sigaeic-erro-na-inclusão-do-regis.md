---
article_id: 4787258741911
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: eaa2576888ebf8cb4aadedfd5ff4cb200135bb328dd8473aff7b8fa48de0bfd0
fetched_at: '2026-06-28T22:39:52.191140+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro na inclusão
  do registro de operador estrangeiro para o catálogo
type: support-article
updated_at: '2022-03-17T18:17:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4787258741911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-na-inclus%C3%A3o-do-registro-de-operador-estrangeiro-para-o-cat%C3%A1logo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como faço para que a mensagem abaixo não seja exibida ao incluir um registro na rotina de Catalogo de Produtos (**EICCP400**)?

![ERRO-CATALOGO_DE_PRODUTOS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4786121870359/ERRO-CATALOGO_DE_PRODUTOS.PNG)

Mensagem: Erro na inclusão do registro de operador estrangeiro para o catalogo xxxxxxxxxxxxxxxx.  
Fornecedor: xxxxxx Loja: xx.  
Esse erro não interfere na gravação do catálogo de produtos (Veja mensagem abaixo)  
----------------------------------------------------------------------------------------------  
Id do formulario de erro: [EICOE400\_EKJ]  
Id do campo de origem: [VLDDATA\_OBRIGAT]  
Id do campo de erro: [EKJ\_SUBP]  
Id do erro [OBRIGAT]  
Mensagem do erro: [O campo Subdiv. País (EKJ\_SUBP) não foi preenchido]  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**Este ocorre porque neste momento o sistema também vai atualizar o cadastro de Operador Estrangeiro com os dados da rotina Forn/Fabricante (**MATA020**) então os sistema inclui o catálogo, mas não inclui o operador estrangeiro.  
Para que o erro não ocorra acesse a rotina rotina Forn/Fabricante (**MATA020**) e altere o fornecedor que foi relacionado no catalogo de produtos( o erro na tela mostrara qual é o fornecedor que esta com divergência no cadastro):  
1) Clique na aba Residente Exterior.  
2) Preencha os campos SubDivPais (**A2\_PAISSUB**)  e Cod.Postal (**A2\_POSEX**).   
3) Salve o cadastro para que alteração entre em vigor.  
  
Efetuado este procedimento é só alterar o registro da rotina catalogo de produtos e salvar novamente que o erro não ocorrerá.

![Fornecedor_-_Residente_Exterior.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4786198567063/Fornecedor_-_Residente_Exterior.PNG)

**Saiba mais**[Catalogo de Produtos](https://tdn.totvs.com/pages/releaseview.action?pageId=547226488)
