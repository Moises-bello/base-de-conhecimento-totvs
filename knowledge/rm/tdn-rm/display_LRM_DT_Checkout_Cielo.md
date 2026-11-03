---
content_hash: 165b6a2ec4671b84aee78bf5aa425ad7b2ae9862f58c9c4f65ab099f508a7fc6
fetched_at: '2026-06-29T00:06:27.940344+00:00'
page_id: '233739272'
product: rm
source: tdn-rm
title: DT_Checkout_Cielo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Checkout_Cielo
version: 11
---

# CHECKOUT CIELO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Portal Educacional e Processo Seletivo* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Pagamento por Cartão de Crédito*.* | ***Pagamento por Cartão de Crédito**.* | |  |  | |
| **Requisito (ISSUE):** | PCREQ-8625 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *FINTEGRACAOCARTAO, FINTEGRACAOHISTORICO* |

## Descrição

Foi implementado o modelo Checkout da Cielo para pagamento com cartão de crédito/débito no portal Educacional e Processo Seletivo.

## Procedimento para Utilização

1.    Acessar a etapa 02.02.02.03 - Cartão de Crédito/Débito do parametrizador do TOTVS Gestão Financeira.

                Em Configurações Gerais 1/2 deve ser marcado a opção Checkout no campo Modelo E-commerce.

                Em Configurações Gerais 2/2 deve ser informado os seguintes campos:

                MerchantId: Identificação do cliente na Cielo

                URL Post: URL de post que será enviado para a Cielo para solicitar uma transação.

               Em Bandeira 1/3 deve ser informados os campos de Conta Caixa e Meio de Pagamento para a função crédito e débito para a bandeira Visa.

               Em Bandeira 2/3, deve ser informados os campos de Conta Caixa e Meio de Pagamento para a função crédito e débito para a bandeira Master

              .

                Em Bandeira 3/3, deve ser informados os campos de Conta Caixa e Meio de Pagamento para a função crédito para as outras bandeiras.

   

       

        2.    No BackOffice da Cielo acessar a aba Configurações | Configurações da Loja devem ser informados as URLs de Notificação e Mudança de Status

               URL de Notificação: []/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoNotificacao.aspx

     URL de Mudança de Status: []/Source/Fin-Financeiro/RM.Fin.Lan/CheckoutCielo/FinLanCartaoMudancaStatus.aspx

               A URL de Retorno não é obrigatória ser informada. Caso não seja informada ao finalizar o pagamento o usuário será redirecionado para uma pagina própria da Cielo.

       3.    No portal Educacional e Processo Seletivo ao acessar o boleto para pagamento, ao clicar em Avançar na tela de Confirmar Dados Cadastrais o usuário sera redirecionado para a página segura da Cielo para efetuar o pagamento.
