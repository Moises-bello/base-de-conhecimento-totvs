---
content_hash: 1d8ce70b2a5349c5f174a298dce74ead95d9bcda39fa75b87d76843511deacc5
fetched_at: '2026-06-29T00:09:52.353669+00:00'
page_id: '439355674'
product: rm
source: tdn-rm
title: FOPROTINAS01-6842 - Criação de parâmetro para considerar chefe de seção como
  subordinado direto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439355674
version: 14
---

# Visualização de Subordinados - RM Portal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | RM Portal - Subordinados |
| **Situação/Requisito:** | A visualização de subordinados no portal traz os chefes da seção como subordinados diretos mesmo que eles não estejam alocados naquelas seções nas quais são chefes |
| **Solução/Implementação:** | Adicionar um parâmetro para informar se esse comportamento deve ser mantido ou se os chefes da seção serão retornados apenas se estiverem alocados nas mesmas. |
| **Conversores e Parâmetros:** | "Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção" |
| **Tickets relacionados:** | 4459800 |
|  | Para habilitar/desabilitar o parâmetro acesse:  RM | RH | Folha de Pagamento | Configurações | Parâmetros | Parametrizador | 06 - Folha de Pagamento | 06.05 - RM Portal | Seleção do Grupo de Acesso | Parâmetro | Etapa 6 - RM Portal: Supervisores | Opção “Considerar o Chefe da Seção como subordinado direto mesmo não estando alocado naquela seção”      **Definição de Subordinado Direto:** Subordinados diretos são os funcionários que na hierarquia da tela de “Cadastro de Chefe/Supervisor“ respondem diretamente à um determinado chefe. Ou seja, que pertencem à própria seção da qual o chefe é responsável ou se pertencem à seções filhas que não possuem chefes cadastrados e ativos.  **Exemplificação do parâmetro "Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção" marcado:**  O chefe **“Funcionário A”** visualiza o “**Funcionário B”** como subordinado direto, pois este é chefe da seção 01.01, apesar de estar alocado na seção 02.01 e essa seção é filha da 01 da qual o Funcionário A é chefe. O “**Funcionário A**” visualiza o “**Funcionário C**” como subordinado indireto, pois este é chefe e está alocado na seção 01.01.01.  Visualização de tela "Cadastro de Chefe/Supervisor":    Visualização do "Funcionário A" no RM Portal:      **Observação:** Para que este comportamento seja efetivo na tela de Subordinados e Gestão de Férias, o parâmetro "**Considerar o Chefe Alocado na seção como subordinado direto**" deve estar desmarcado.    **Exemplificação do parâmetro "Considerar o chefe da seção como subordinado direto mesmo não estando alocado naquela seção" desmarcado:**  O chefe **“Funcionário A”** NÃO visualiza o “**Funcionário B”** como subordinado direto, pois este está alocado na seção 02.01, apesar de ser chefe da 01.01. O “**Funcionário A**” visualiza o “**Funcionário****C**” como subordinado indireto, pois este está alocado na seção 01.01.01 e é subordinado do “**FUNCIONÁRIO B**”.  Visualização de tela "Cadastro de Chefe/Supervisor":      Visualização do "Funcionário A" no RM Portal: |
|  |  |
