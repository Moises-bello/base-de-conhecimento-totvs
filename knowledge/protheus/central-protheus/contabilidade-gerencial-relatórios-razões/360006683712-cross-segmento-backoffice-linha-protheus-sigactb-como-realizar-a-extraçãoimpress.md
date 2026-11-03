---
article_id: 360006683712
category: Contabilidade Gerencial - Relatórios Razões
content_hash: 5cfd59737c29eb128b0b8ba8dff182599c5360c06316f1effd164afbd8b3ea43
fetched_at: '2026-06-28T22:40:41.118898+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como realizar a extração/impressão
  do Razão Contábil no PROTHEUS (CTBR400)?
type: support-article
updated_at: '2022-08-05T12:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006683712-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-a-extra%C3%A7%C3%A3o-impress%C3%A3o-do-Raz%C3%A3o-Cont%C3%A1bil-no-PROTHEUS-CTBR400
---

**Dúvida**Como realizar a extração/impressão do Razão Contábil no PROTHEUS (CTBR400)?

**Ambiente**Protheus – Contabilidade – A partir da versão 11.80  
  
   
**Solução**

O Razão também é um livro de escrituração, e dos livros utilizados pela Contabilidade, é o mais importante sob o ponto de vista contábil, pois através dele se controla separadamente o movimento de cada conta.

O controle individualizado das contas é importante para conhecer os seus saldos e elaborar as demonstrações contábeis, como Balancetes, Balanços entre outras.

Para emitir o relatório Razão Contábil no ambiente Contabilidade Gerencial no Microsiga Protheus, realize os seguintes passos:

Em Razão Contábil, clique em Parâmetros.

O sistema apresenta a tela para configuração dos parâmetros referentes ao relatório.

Observe o parâmetro Tipo de Relatório, que permite três formas de impressão:

* **Analítico:** imprime todos os lançamentos contábeis, exibindo todas as colunas do relatório.
* **Resumido:** imprime todos os lançamentos contábeis, mas exclui as colunas das entidades de custo (Centro de custo, item contábil e Classe de Valor).
* **Sintético:** imprime a totalização da movimentação contábil diária de uma conta contábil, em uma única linha exibindo as colunas Data, Valor de Débito, Valor de Crédito e Saldo Atual.

Importante: Os parâmetros abaixo, se informados incorretamente, o relatório não irá realizar a extração correta dos dados:

**Imprime C.C. extra?**Informe se deseja imprimir ou não os Centros de Custo

**Do Centro de Custo?**Informe o Centro de Custo inicial a partir do qual se deseja imprimir o relatório. Caso queira imprimir todos os Centros de Custos, deixe esse campo em branco.

**Até Centro de Custo?**Informe o Centro de Custo final até o qual se deseja imprimir o relatório. Caso queira imprimir todos os Centros de Custos, preencha este campo com "ZZZZZZZZZ".

**Imprime Item Contab?**Informe se deseja imprimir os Itens Contábeis.

**Do Item Contábil?**Informe o Item Contábil inicial a partir do qual se deseja imprimir o relatório. Caso queira imprimir todos os Itens Contábeis, deixe esse campo em branco.

**Ate Item Contábil?**Informe o Item Contábil final até o qual se deseja imprimir o relatório. Caso queira imprimir todos os Itens Contábeis, preencha este campo com "ZZZZZZZZZ".

**Imprime Classe de Vlr ?**Informe se deseja ou não imprimir as Classes de Valor.

**Da Classe de Valor?**Informe a Classe de Valor inicial a partir da qual se deseja imprimir o relatório. Caso queira imprimir todas as Classes de Valor, deixe esse campo em branco.

**Até Classe de Valor?**Informe a Classe de Valor final até a qual se deseja imprimir o relatório. Caso queira imprimir todas as Classes de Valor, preencha esse campo com 'ZZZZZZZZZ'.

**Cod. Conf. Livros ?**  
Determine qual a Configuração de Livro será utilizada neste relatório. Se não desejar nenhuma configuração específica deixe este campo em branco. Neste relatório a Visão Gerencial não poderá ser utilizada. Somente as máscaras das entidades serão herdadas.

Após isto, preencha os demais parâmetros conforme a necessidade de sua extração e clique em OK.

Clique no botão de imprimir.

**Atenção**A personalização dos relatórios exigidos por lei, afeta a legalidade do documento. Por esta razão, por padrão do Sistema, a personalização destes documentos está bloqueada no Contabilidade Gerencial. Observe a configuração do parâmetro [MV\_CTBPOFF](http://tdn.totvs.com/pages/viewpage.action?pageId=233764389).

É possível também imprimir o cabeçalho padrão com o campo de data e número correlativo por linha de lançamento, caso o campo Imprimir Cabeçalho? esteja como Sim.
