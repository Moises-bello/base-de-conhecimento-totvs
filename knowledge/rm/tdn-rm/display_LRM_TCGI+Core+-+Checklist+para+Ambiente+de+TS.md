---
content_hash: b76428de113bd433e410ae1ca2ff0bfe81e1b69b8df7340796322b6a32252926
fetched_at: '2026-06-29T00:11:56.705068+00:00'
page_id: '868249565'
product: rm
source: tdn-rm
title: TCGI Core - Checklist para Ambiente de TS
type: documentation
url: https://tdn.totvs.com/display/LRM/TCGI+Core+-+Checklist+para+Ambiente+de+TS
version: 4
---

**USO INTERNO**

O objetivo deste documento é criar um checklist para validar o ambiente de teste sistêmico disponibilizado pela engenharia, garantindo que o ambiente está funcional para os testes, tanto do TCGI quanto dos portais e app.

 

Máquina virtual para testes dos Instaladores disponibilizados pela Engenharia: **BH-DEV-TSTCP.sp01.local**

 

**Pré requisitos de Ambiente:**

* Ambiente RM e Portais 12.1.2410 disponível para instalação;
* Atualizar base para ambiente 12.1.2410;
* ISS instalado;
* PHP e demais pré requisitos para o PI instalados, conforme documentação [Portal de Imóveis - Instalação e configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=697715936);
* Configurar Smart Reports

Importante!

Para maior fidedignidade dos testes, os mesmos deve ser realizados com o Smart Client fora da VPN da TOTVS, simulando assim o cenário real dos Clientes.

**Pré requisitos de Testes:**

* TCGI Vendas:

+ Cadastro de Venda;
+ Cadastro de Comissão;
+ Cadastro de Atendimento;
+ Execução de Cobrança;
+ Reajuste;
+ Baixas
+ Despesa
+ Etc.

* Portal Imóveis - PI (PO UI):

+ Acesso;
+ Sincronismo;
+ Cadastro Pessoas;
+ Cadastro Propostas;
+ Comissão;
+ Efetivação Contrato;
+ Cadastro Conjugue;
+ Cadastro Fiador;
+ Funil de Vendas;
+ Roleta de Vendas;

* Portal do Cliente - PDC:

+ Acesso;
+ Visualização do Plano de Financiamento;
+ Geração de Boleto e PIX;
+ Renegociação;
+ Cadastro de Atendimento;
+ Visualização de Atendimento;
+ Menus de Gestão;
+ Etc.

* Meu Imóvel

+ Acesso;
+ Visualização de Atendimentos;
+ Cadastro de Atendimento;
+ Visualização Situação Financeira;
+ Renegociação;
+ Geração de Boleto e PIX;
+ Etc.
+ Smart Reports
+ Acesso;
+ Importação de Relatórios;
+ Geração de Relatórios;
+ Exclusão de Relatórios;
+ Etc.
