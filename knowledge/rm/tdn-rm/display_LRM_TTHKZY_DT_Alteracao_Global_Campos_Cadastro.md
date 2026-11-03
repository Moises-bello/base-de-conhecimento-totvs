---
content_hash: ae3ceaa8548f032ef5559a08ff510529b60bd0758f41178e5bff4aa6ad957ee0
fetched_at: '2026-06-29T00:06:14.557310+00:00'
page_id: '210047794'
product: rm
source: tdn-rm
title: TTHKZY_DT_Alteracao_Global_Campos_Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHKZY_DT_Alteracao_Global_Campos_Cadastro
version: 3
---

# ALTERAÇÃO GLOBAL CAMPOS DO CADASTRO - CÓDIGO DO FORNECEDOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Global Campos do Cadastro - Código do Fornecedor* |
| **Situação/Requisito:** | Ao executar a Alteração Global Campos do Cadastro, para o campo CODFORNECEDOR utilizando  a formula CHAPA, sendo que o valor da formula é '7777777', alguns registros são alterados e outros não. Porém ao acessar o cadastro do funcionario que teve o registro alterado com sucesso, o campo Fornecedor Lançamento Financeiro é apresentado mensagem de advertencia. |
| **Solução/Implementação:** | Realizado validação se o código da formula for igual a "CHAPA", e o resuldado da formula for maior que zero, é consultado na tabela FCFO se existe o fornecedor informado, se existir realiza o processo senão apresenta mensagem de aviso informado que o fornecedor informado não existe. |
| **Chamados relacionados:** | TTHKZY |
| **Versões/Release:** | *12.1.8* |

divs
