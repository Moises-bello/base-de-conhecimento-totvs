---
content_hash: 7eeaa50f882947da2a6b27c29b745898b5e37f7c027fdc50f73eb9e44eded5dd
fetched_at: '2026-06-29T00:09:34.729902+00:00'
page_id: '425459238'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Produto (Item)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459238
version: 3
---

**TOTVS Obras e Projetos x BackOffice Protheus  - Cadastro Produto (Item)**

---

A inclusão, alteração e exclusão do cadastro de produtos são realizadas no Protheus. No TOP deverá ser permitido apenas a consulta dos registros, ou seja, as permissões de Incluir, Alterar e Excluir devem ser negadas. Os dados são sincronizados automaticamente.  
    
 **Alteração:** Ao realizar uma alteração no campo unidade de medida no registro do produto, também serão alterados os insumos relacionados aquele produto.   
 **Exclusão:** Ao realizar uma exclusão no Protheus, o registro correspondente no TOP será desativado. A exclusão no Protheus será concluída apenas se a exclusão no TOP for bem sucedida.   
    
 Para incluir, alterar ou excluir um produto no Protheus acesse: Protheus | SigaEst | Atualizações | Cadastros | Produto   
 Para visualizar os produtos no TOP acesse: RM | BackOffice | Compras, Estoque e Faturamento | Cadastros | Produtos   
     
 **Dados Sincronizados**  
    
 Os dados sincronizados do Protheus para o TOP referente ao cadastro Produto são:

* Código da coligada
* Código do produto
* Código reduzido
* Número do fabricante
* Nome fantasia
* Código da unidade de controle
* Código da unidade de venda
* Código da unidade de compra
* Custo médio
* Custo unitário
* Preço 1
* Preço 2
* Tipo
* Status (com valor inativo)

***Observações:***

* Embora no RM exista conceito de máscara para o código do produto, não haverá máscara para integração com o Protheus.
* Os valores totais podem possuir no máximo duas casas decimais.
* O sincronismo dos campos de preço e custo ocorrerá da forma como demonstrado na imagem abaixo.
* Os processos referente a "importação de produtos para insumo" e "importação de preço de produto" podem ser utilizados. Para isso é necessário ativar a integração Obras e Projetos x Gestão de Estoques, Compras e Faturamento (RM Solum x RM Nucleus). Esta configuração deve ser realizada na versão em Delphi. Acesse: RM.Solum.exe | Opções | Parâmetros | Integração
* Ao incluir um produto, este fica relacionado a filial da empresa. Quando apenas uma empresa está cadastrada este relacionamento não interfere na sincronização dos dados.

Entretanto, quando duas ou mais empresas estão cadastradas é necessário configurar em cada empresa o compartilhamento do produto, e relacioná-lo com a empresa, permitindo a sincronização dos produtos para o TOP.   
 Este procedimento é realizado no Protheus através da alteração da tabela de produto (SB1) de exclusiva para compartilhada.   
    
 Para realizar a configuração acesse: Protheus / Módulo SigaCFG / Base de Dados / Dicionário / Base de Dados  
    
 Selecione, dentro da empresa o Dicionário de Dados. Selecione e edite o **Prefixo SB1**, referente a Descrição Genérica do Produto. No campo **Ac. Filial** altere o valor de Exclusivo para Compartilhado, e confirme a alteração. Este procedimento deve ser realizado para todas as empresas. Não é necessário realizar para cada filial.
