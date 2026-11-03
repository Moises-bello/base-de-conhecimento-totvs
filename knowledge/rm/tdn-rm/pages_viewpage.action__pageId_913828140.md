---
content_hash: ca0caa3a0c9b11d2521d1d1414db6eefddf414a72750184d5e8abb0ac78e7de9
fetched_at: '2026-06-29T00:12:06.146518+00:00'
page_id: '913828140'
product: rm
source: tdn-rm
title: Classificação Fiscal de Bens e Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=913828140
version: 52
---

# Conteúdo

Conteúdonone

# 1. Visão Geral

O **Cadastro de Classificação Fiscal de Bens e Serviços** tem como objetivo padronizar e facilitar a classificação de mercadorias e serviços por meio da **Nomenclatura Comum do Mercosul (NCM)** e da **Nomenclatura Brasileira de Serviços (NBS)**. Esse cadastro é essencial para garantir que a tributação ocorra corretamente, evitando erros no cálculo de impostos e assegurando a conformidade com a legislação fiscal vigente.

Este documento detalha as orientações para o correto preenchimento do cadastro, garantindo que as informações sejam aplicadas corretamente nos processos que compões as nossas soluções fiscais.

# 2. Configuração Inicial

## 2.1 Atualização Base de Dados

Para atualizar a Base de Dados, seguem informações na documentação [Atualizar a Base de Dados do RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000994448-Framework-Framework-RM-BD-Como-converter-atualizar-a-Base-de-Dados-RM).

## 2.2 Permissão de Acesso

Para acessar o menu eCadastro de Classificação Fiscal de Bens e Serviços, é necessário configurar a permissão de acesso ao menu.

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão Fiscal;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*01] Cadastros | [01.02] Globais | [01.02.02] Mais...***, selecione **[01.02.02.14] Cadastro de Classificação Fiscal de Bens e Serviços**e, logo após, clique em **Permitir Acesso**.

Segurança - Acesso - Perfis

# 3. Classificação Fiscal de Bens e Serviços

O Cadastro pode ser acessado através do Módulo Gestão Fiscal | Cadastros | Na divisão de "Globais" opção Mais | Classificação Fiscal de Bens e Serviços. 

Acesso ao Menu

# 4. Campos do Cadastro

Esse cadastro será **Global,** garantindo que ele seja compartilhado entre todas as coligadas, sem registros individuais por empresa.

Campos

|  |  |  |
| --- | --- | --- |
| **Campos** | **Obrigatório** | **Descrições dos Campos** |
| Identificador | Sim | Código único gerado automaticamente para cada cadastro. |
| Tipo | Sim | Utilizado para definir se o cadastro é referente a um Produto ou Serviço |
| Ativo | Não | Indicativo do Status do registro, marcado é ativo e desmarcado é inativo |
| Descrição | Não | Informar a descrição para o NCM ou NBS |
| Referência | Não | Informe a referência de A a Z do produto, cada letra se relaciona ao número informado no campo posterior, para o produto com IPI. Esta letra poderá ser impressa na nota fiscal |
| Número NCM | Não | Nomenclatura Comum do Mercosul é um código de 8 dígitos usado para classificar mercadorias de forma padronizada no Brasil e em outros países do Mercosul. |
| Código Ex | Não | É usado quando um produto específico dentro de um NCM possui tratamento fiscal diferente dos demais produtos da mesma classificação. Aparece geralmente em tabelas da **TIPI.** |
| Número NBS | Não | Código NBS (Nomenclatura Brasileira de Serviços) é semelhante ao **NCM**, mas voltado exclusivamente para serviços. |

# 5. Anexos

* Produtos

  No Anexo de Produtos, teremos um registro de Classificação de Bens e Serviços associado em um ou muitos produtos, portanto nesse anexo podemos ver em quais produtos esse registro esta presente.

  Aba IdentificaçãoAba Produtos

  Preenchimento do campo NCM/NBS no cadastro do Produto.

  **Observação**:

  Caso esteja trabalhando com o Produto Global e o campo NCM/NBS não esteja sendo exibido no formulário conforme imagem acima.

  Faça a seguinte parametrização acessando pelo módulo Gestão de Estoque, Compras e Faturamento, no menu Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | 04.01 - Parâmetro Gerais | 04.01.04 - Tabelas | 04.01.04.07 - Produtos | Definições de Produtos 3/3 | Marque a opção "Dados Fiscais".

**Quer contribuir com a evolução da nossa documentação? [Clique aqui e dê um feedback sobre esta página!](https://forms.gle/RZXc3eYwhuq9TNtD6)**
