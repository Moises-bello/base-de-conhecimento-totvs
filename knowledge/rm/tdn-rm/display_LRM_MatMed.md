---
content_hash: b5880f8488d67a097bd2c81cc43d3a89a92316c69acb92ed5fcf789e26b417a5
fetched_at: '2026-06-29T00:11:05.360989+00:00'
page_id: '630372881'
product: rm
source: tdn-rm
title: MatMed
type: documentation
url: https://tdn.totvs.com/display/LRM/MatMed
version: 15
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
   1. **Caderno de Gabaritos**
   2. **Validações Específicas**
3. **Calculo do valor**
4. **Local de Uso**
   1. **Principais Campos e Parâmetros**
5. **Produto composto e itens associados**
6. **Vínculo com exame**
7. **Item de alto custo**
8. **Filtro por unidade de atendimento**
9. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A página de MatMed serve para visualizar os medicamentos e materiais lançados para o atendimento e também serem lançados manualmente pelo faturamento.

## **02. VALIDAÇÕES**

* **Atendimento**
  + Deverá estar com o status diferente de "Cancelado"

* **Parcial**
  + Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
  + Não poderá ter nota fiscal emitida e o convênio particular.
* **Centro de custo**
  + Obrigatório se o parâmetro "Centro de Custo obrigatório nos lançamentos?" estiver marcado em Parâmetros Gerais > Faturamento II
  + Paciente interno
    - Matmed
      * Obrigatório se o parâmetro "Centro de Custo sem possibilidade de alteração" estiver marcado
    - Outros lançamentos
      * Obrigatório se o parâmetro "Centro de Custo vinculado ao leito sem possibilidade de alteração" estiver marcado
  + Paciente Externo
    - Obrigatório se o parâmetro "Centro de Custo vinculado a Estação de Trabalho sem possibilidade de alteração" estiver marcado
* Item estornado não pode ser alterado
* O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial.
* O valor do MatMed incluído deverá ser maior que 0.
* Caso o parâmetro (aba Eletrônico III - Tiss | Limita quantidade máxima definida pela TISS) nas condições contratuais esteja marcado, e a quantidade informada for maior ou igual a 1000, o sistema não permitirá salvar o registro.
* Data:
  + A data do MatMed deve estar dentro do período da parcial
  + A data/hora de início não pode ser maior que a data/hora final

### **02.1 Caderno de Gabaritos**

Ao salvar um MatMed, o sistema verifica se existe um gabarito em aberto para a conta e se comporta de acordo com os parâmetros gerais:

* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Questionar inclusão no pacote". O sistema pede a confirmação do usuário para incluir a diária no pacote. Ou seja, o MatMed será cobrada além do pacote.
* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Incluir automaticamente no pacote". O sistema não pede confirmação e incluirá o MatMed automaticamente junto com o pacote.
* Caso não tenha um gabarito em aberto, o MatMed não será cobrado

### **02.2 Validações Específicas**

* Atendimento com alta administrativa: somente permite realizar o lançamento de MatMed se o parâmetro do perfil do usuário , no RMSaude.exe, estiver marcado "Permite lançamentos após Alta Administrativa"

* Permissão para Para produtos do tipo CONTROLADO, ANTIMICROBIANO e RESTRITO, somente será possível realizar o lançamento de MatMed se o parâmetro do perfil do usuário , no RMSaude.exe, estiver marcado para requisitá-los

Cadastro de Produto/Informações Totvs Saúde: campos antimicrobiano, restrito, controlado, kit Pré-Montado

* Kit Pré-Montado não poderá ser lançado pela Elaboração de Contas.

## **03. CÁLCULO DE VALOR**

Documentação para valorização de MatMed**:**

## **04. LOCAL DE USO**

Existe uma parametrização nos parâmetros gerais, classificando o local de uso para MatMed.

## **05. PRODUTO COMPOSTO E ITENS ASSOCIADOS**

O produto composto funciona como um kit de lançamentos, onde o produto que possui itens no anexo "Produtos Compostos", não é considerado na conta do paciente, ou seja, ele não deve ser somando as demais itens. O mesmo é estornado da conta.

Já os itens associados,, funciona tem um funcionamento parecido, onde o item principal também é considerado na conta do paciente.

kitProduto Composto

Cadastro do produto composto

Lançamento do Produto composto

O item composto é estornado da conta pelo sistema

Itens Associados

Cadastro dos itens associados.

Produto > Informações RM Saúde > Anexos > Produto Associado

Lançamento de um item que possui produtos associados

Lançamento do item associado ao AAS

## **06. VÍNCULO COM EXAME**

Ao realizar o lançamento de Matmed na conta, o usuário poderá vincular a um exame já lançado em conta.

O exame só aparecerá na pesquisa, caso possua número de guia vinculado.

 

## **07. ITEM DE ALTO CUSTO**

Para que o sistema identifique  um produto de alto custo, deve-se configurar nas Condições Contratuais, os parâmetros em destaque.

Qualquer item lançado na aba de Matmed na Elaboração de Contas, e que tiver o valor unitário maior ou igual ao parâmetro, será considerado de alto custo.

Ao identificar essa situação, um registro é incluído na tabela de alto custo e caso parametrizado o campo "**Incluir na Central de Autorizações**", também será inserido na central de autorizações. 

O item é considerado de alto custo somente se estiver na aba de Matmed. Se estiver configurado para ser grátis ou particular, o mesmo nada faz.

 

 

Mais informações sobre itens de alto custo na documentação:

## **08. FILTRO POR UNIDADE DE ATENDIMENTO**

Para a pesquisa de Matmed filtrar os produtos permitidos pela unidade de atendimento da parcial, é necessário marcar o parâmetro geral "Filtra Produtos pela Unidade de Atendimento da Parcial".

Com o parâmetro marcado, a pesquisa retornará somente os produtos configurados nas devidas unidades. O cadastro das unidades de atendimento permitidas por produto fica no anexo de produto do Saúde.

## **09.****TABELAS UTILIZADAS**

* SZATENDMATMED
* TPRDCOMPOSTO
* SZITEMESTOQASSOC

  ```

  ```
