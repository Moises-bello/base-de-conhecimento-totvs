---
article_id: 360012650891
category: Materiais - Compras (SIGACOM)
content_hash: d915b5cc49339fec6c025930ec3e60ffb38426f42f873445e25d6b55a09b5c5b
fetched_at: '2026-06-28T22:41:07.361297+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Como lançar  RPA -
  Recibo de Pagamento de Autônomos através da entrada de Notas Fiscais de Prestação
  de Serviços na MATA103 ?
type: support-article
updated_at: '2022-07-18T20:02:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012650891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-lan%C3%A7ar-RPA-Recibo-de-Pagamento-de-Aut%C3%B4nomos-atrav%C3%A9s-da-entrada-de-Notas-Fiscais-de-Presta%C3%A7%C3%A3o-de-Servi%C3%A7os-na-MATA103
---

**Dúvida**Como lançar RPA - Recibo de Pagamento de Autônomos através da entrada de Notas Fiscais de Prestação de Serviços na MATA103 ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para agilizar o processamento da folha de pagamento dos funcionários autônomos, na rotina  "Documento de Entrada" **(MATA103),** foi disponibilizada melhoria que permite, através do registro da NFPS (Nota Fiscal de Prestação de Serviços), a atualização automática dos dados para a emissão do RPA – Recibo de Pagamento de Autônomos, no ambiente Gestão de Pessoal.

Ao efetuar a gravação da NFPS, o sistema atualizará a tabela de dados "**SRK – Lançamentos Futuros"**, que contém os valores a serem pagos/descontados no futuro, isto é, valores que deverão ser descontados ou adicionados no movimento do mês de acordo com a data do vencimento.  
  
No processamento do cálculo da folha de pagamento para o funcionário autônomo relacionado ao fornecedor da NFPS, serão atualizados os dados do autônomo e lançada a verba de pagamento referente, conforme o valor informado no documento de entrada. Para atualização da verba de pagamento, será utilizado o identificador de cálculo “**0218**” para o recibo de pagamento de autônomos.

**Obs**: Além do identificador de cálculo "0218", é  necessário a existência dos demais   "Identificadores de cálculos" e suas respectivas verbas,  tabela **SRV** os quais são obrigatórios para execução do cálculo  da folha de Pagamento.

Para atender a esta implementação, no Cadastro de Fornecedores, foi criado o campo "Funcionário"(A2\_NUMRA), que deve ser utilizado para relacionar o fornecedor autônomo com o código cadastrado para o funcionário autônomo da folha de pagamento.

**Observação:**  
*Quando um fornecedor é vinculado a um funcionário, mesmo que o TES (Tipo de Entrada e Saída)**do documento de entrada esteja configurado para atualizar o financeiro com um movimento no**contas a pagar, o sistema irá substituir este processo por um movimento na folha de pagamento,**atualizando a tabela de dados "SRK – Lançamentos Futuros".  
Após a inclusão da nota fiscal de prestação de serviços, a tabela de valores futuros da folha de**pagamento será alimentada com as informações da duplicata contidas na pasta “Duplicatas” da**rotina “Documento de Entrada”, com exceção dos impostos que serão recalculados pela folha de**pagamento.*

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
