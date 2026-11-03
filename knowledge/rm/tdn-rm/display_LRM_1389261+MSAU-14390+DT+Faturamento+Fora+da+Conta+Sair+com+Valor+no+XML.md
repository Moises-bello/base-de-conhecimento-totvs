---
content_hash: fad652fb199c740c427751ef3512f94620fbdc35a2a3da1d1e4c309bc62f3ecf
fetched_at: '2026-06-29T00:08:43.791043+00:00'
page_id: '306843552'
product: rm
source: tdn-rm
title: 1389261 MSAU-14390 DT Faturamento Fora da Conta Sair com Valor no XML
type: documentation
url: https://tdn.totvs.com/display/LRM/1389261+MSAU-14390+DT+Faturamento+Fora+da+Conta+Sair+com+Valor+no+XML
version: 99
---

# Faturamento fora da conta sair com valor no xml

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios |  |  | | --- | | **Rotina(s) envolvida(s)** | | Elaboração de contas; Faturamento para Convênios. | |
| **Parâmetro(s):** | Valor Zerado |

## Descrição

Criado parâmetro para exibir valores de itens lançados fora da conta no XML e ajustes necessários na rotina de geração do mesmo.

## Procedimento para Utilização

       1.          Acesse o menu Cadastros / Faturamento / Condições Contratuais com Convênios e acesse o registro correspondente à condição contratual desejada.

* + Na **Versão da TISS** selecione a **3.03.01** ou superior.
  + Acesse a aba “**Eletrônico III - TISS**” e na seção "**Incluir Lançamentos Fora da Conta**", desmarque o checkbox “**Valor zerado**”.

       2.           Registre um **Atendimento Externo** ou **Interno**para Unidade de Atendimento e Convênio configurado no passo anterior.

       3.          Abra a Elaboração de Contas, na aba Honorários, realizar um lançamento e marcar o botão (no canto direito da tela) Honorários fora da conta e gravar.

       4.          Dê alta (se interno) e Encerrar a conta.

       5.          Acessar a nova MDI / menu Faturamento / Faturamento para Convênios.

* + Criar um novo com a Unid. Atendimento e Convênio usados no registro de atendimento e clicar em Executar.
  + Configurar conforme o atendimento e selecionar a conta/paciente em teste e concluir.

       6.            Confira os dados no XML e confirme.

divs
