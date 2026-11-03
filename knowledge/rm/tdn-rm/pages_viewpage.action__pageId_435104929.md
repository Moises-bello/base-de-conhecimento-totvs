---
content_hash: efe218f3b85631968a5f98b809386637e5b5990e64571429e23a5d66f48a6d04
fetched_at: '2026-06-29T00:09:47.114035+00:00'
page_id: '435104929'
product: rm
source: tdn-rm
title: Gerar Movimento RPS - Recibo Provisório de Serviços - How To - Habilitar a
  utilização de RPS em um Empreendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104929
version: 3
---

Para  gerar a RPS (Recibo Provisório de Serviços) em uma Venda imobiliária é necessário que as informações necessárias sejam habilitadas na aba de Integrações com a Gestão de Estoque, Compras e Faturamento , no cadastro do Empreendimento.

**Pré-Condições:**

**1 -** Ter incluído um [Tipo de Movimento do grupo 2.1](http://tdn.totvs.com.br/display/LRM/Parametrizando+o+tipo+de+movimento+utilizado+para+gerar+RPS "Parametrizando o tipo de movimento utilizado para gerar RPS"), que será utilizado para gerar movimentos ao executar o processo [Gerar Movimento de  RPS] do Contrato de Venda;  
**2 -** Ter permissão para Editar Empreendimentos;  
**3 -** Ter incluído um Serviço, ativo e de último nível;   
**4 -** Ter incluído uma fórmula para Valor  de Dedução c/Material.

**Habilitando a utilização de RPS:**

**1 -** Acesse: TOTVS Projetos/ Incorporação/ Cadastros/ Empreendimento;  
**2 -**Selecione o Empreendimento desejado e clique no ícone [Editar Empreendimento];  
**3 -** Acesse a aba Integração e a sua sub-Aba Gestão de Estoque, Compras e Faturamento;  
**4 -** Marque o checkBox [Emite NFS-E Carioca]. Os campos serão habilitados para preencimento;  
**5 -** Informe :

* **Tipo de Movimento:** Informe um Tipo de movimento que atenda a Pré-Condição 1.
* **Produto/ Serviço:** Informe um Tipo de movimento que atenda a Pré-Condição 3.
* **Fórmula Vr Dedução c/Material:** Informe uma fórmula para calcular o valor de dedução com material que será carregado no campo de Dedução com  Material do  movimento de RPS (TMOVFISCAL.VLRDEDUCAOMATERIAL).

Esta formula será executada no contexto de sub unidade da parcela baixada.

**6-** Salve o cadastro do Empreendimento.
