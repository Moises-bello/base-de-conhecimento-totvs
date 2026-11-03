---
content_hash: 5e68d34e0a08f886e301e9c9422c3b0c733767d065705554f58b307f5a0d8a52
fetched_at: '2026-06-29T00:11:32.940817+00:00'
page_id: '751511548'
product: rm
source: tdn-rm
title: Pedido de Exames Simplificado
type: documentation
url: https://tdn.totvs.com/display/LRM/Pedido+de+Exames+Simplificado
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de Utilização**

itensVisão Geral

## **01. VISÃO GERAL**

O pedido de exames simplificado é um facilitador para inclusão de solicitação de exames de imagem e análises clínicas no Registro de Atendimento de pacientes EXTERNOS

1. A busca dos exames pode ser por código, descrição ou sinonímia
2. No mesmo pedido podem ser adicionados exames de imagem ou de laboratório individualmente ou por grupo de exames
3. Para lançamentos de exames de pacientes particular ou convenio os exames devem possuir item de débito cadastrado
4. Para lançamentos de exames de pacientes SUS o exame deve ter procedimentos SUS
5. Exames de laboratório devem conter um material cadastrado, caso haja mais de um tipo de material um deles deve estar marcado como default para lançamento
6. Ao finalizar o processo com sucesso os pedidos de exames são separados conforme a unidade de execução de cada no menu do pedido de exames do registro de atendimento um
7. Os exames serão exibidos nas telas de Laudos e/ou  Resultados Laboratorial de acordo com a configuração do exame
8. Para edição ou cancelamento do pedido do exame somente via menu pedido de exames
9. O processo de pedido de exames simplificado é somente para inclusão ou exclusão do item antes da execução do processo
10. Na elaboração de contas deverá ser exibido os itens na aba diagnose e terapia quando paciente for convênio ou particular, para SUS os itens não são exibidos na elaboração de conta somente no BPA ou APAC
11. Não esta contemplado nessa funcionalidade pedidos de exames para Execução Externa

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

 1. menu Registro de Atendimento , incluir um paciente Externo , preencher os campos obrigatórios e salvar 

  2. Após salvar o registro o menu pedido de exames ficara habilitado, clique no menu e será direcionado para a tela de pedido de exames

  3. Na tela do pedido de exames ir em Processos > Pedido de Exames Simplificado

  4. Incluir os exames ou grupos de exames e clicar em avançar

  5. Processo será concluído com sucesso ou caso haja alguma falha será exibido no final da execução
