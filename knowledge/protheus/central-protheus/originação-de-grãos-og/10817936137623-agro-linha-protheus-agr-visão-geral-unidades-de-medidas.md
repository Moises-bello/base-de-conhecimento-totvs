---
article_id: 10817936137623
category: Originação de Grãos (OG)
content_hash: ab8c984eb53bf9f33d16d9dbf2f628957a48c96b5ea8e81ff14ba70c10854211
fetched_at: '2026-06-28T22:45:45.930293+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Visão Geral Unidades de Medidas
type: support-article
updated_at: '2025-06-25T12:50:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10817936137623-Agro-Linha-Protheus-AGR-Vis%C3%A3o-Geral-Unidades-de-Medidas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21020434562711)*** Tempo aproximado para leitura: **00:01:25 min****Dúvida**  
Quais são as unidades de medidas utilizadas para registrar no Sistema?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Essa rotina permite registrar todas as unidades de medidas a serem utilizadas pelo Sistema.

Todo produto cadastrado no **Linha Protheus - AGR** deve, obrigatoriamente, ser associado a uma unidade de medida, caso contrário, o Cadastro de Produtos não será concluído.

A rotina Unidades de Medidas permite manter a descrição da unidade de medida em três idiomas distintos: Português, Inglês e Espanhol.

Além dessas descrições, é necessário informar um código único de identificação da **UM - Unidade de Medida**.

A **Linha Protheus - AGR** permite a utilização de duas unidades de medidas:

**1.** **Unidade de Medida Padrão:** utilizada em todos os movimentos, desde a compra até a venda.  
**2.****Unidade de Medida Secundária:** utilizada em transações nas quais as partes trabalham com unidades de medidas distintas, obtidas a partir do fator de conversão determinado.

**Exemplo:**

**1.** **Unidade de Medida do Fornecedor = (kg) 0,3 quilos**;  
**2.** **Unidade de Medida da Empresa** **= (gr) 300 gramas**;  
**3.** **Fator de Conversão = 1000**.

O Sistema controla o saldo nas duas unidades, mas o custo unitário reflete o valor na unidade padrão.

A unidade de medida secundária será selecionada nas rotinas de movimentação. Em alguns casos, o Sistema sugere uma unidade de medida, mas é possível alterá-la.

**IMPORTANTE!**

* A integração do módulo **SIGAPCP - Planejamento e Controle de Produção** e o **SIGADPR -** **Desenvolvedor de Produtos** ocorre com a habilitação do parâmetro **MV\_INTDPR=1.**
* Quando realizada uma operação de inclusão, alteração ou exclusão no **SIGAPCP**, as operações são replicadas no módulo **SIGADPR**.
