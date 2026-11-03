---
article_id: 360000600247
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 7a3c0d4526c0b31f65fddeb5371d057eb397708c97337f87cd250e7ac371aa0f
fetched_at: '2026-06-28T22:40:32.358758+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - MV_CTBFLAG - Marcação
  de Flags na Contabilização
type: support-article
updated_at: '2023-11-16T14:07:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000600247-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-MV-CTBFLAG-Marca%C3%A7%C3%A3o-de-Flags-na-Contabiliza%C3%A7%C3%A3o
---

**Dúvida**  
Qual a finalidade do parâmetro MV\_CTBFLAG?  
  
**Ambiente**  
Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**  
Indica se a marcação dos *flags* de contabilização (campos**Fx\_DTLANC** ou **Ex\_LA**) serão executadas nas rotinas **Contabilização Off-line** ou **Contabilização On-line**dentro do controle de transação do lançamento contábil no módulo **Contabilidade Gerencial.**Conteúdos possíveis:

T - Habilita marcação das *flags* de contabilização dentro do controle de transação;

F - Marcação das *flags* permanece através da rotina que chama a contabilização, fora do controle de transação.

**Importante**

Na contabilização On-line / Off-line, o sistema grava as linhas detalhes do arquivo de Contra-Prova (**CTK**) antes mesmo do sistema apresentar a tela de contabilização respectiva ao lançamento padrão.

Após clicar no botão "Confirmar" na tela de contabilização, o sistema irá gravar os lançamentos contábeis não deletados na tabela **CT2.**

Caso haja alguma linha de lançamento contábil (Débito, Crédito ou Partida Dobrada) referente ao registro a ser contabilizado DELETADA, o sistema não removerá a flag do registro, pois entende-se que o usuário não quis a contabilização do mesmo.

# [MV\_CTBFLAG Controle de transação na contabilização off-line](https://tdn.totvs.com/pages/viewpage.action?pageId=541984154)
