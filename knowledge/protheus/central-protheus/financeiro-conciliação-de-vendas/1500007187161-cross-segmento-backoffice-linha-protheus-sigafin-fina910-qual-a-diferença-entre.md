---
article_id: 1500007187161
category: Financeiro - Conciliação de Vendas
content_hash: cbbb14362faa9580b66b6940695208c8149db4bf9e1e1195a588fea1b53515a6
fetched_at: '2026-06-28T22:37:26.253303+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmento Backoffice Linha Protheus - SIGAFIN - FINA910 - Qual a diferença
  entre Sitef Antigo FINA910  e Sitef Novo FINA918
type: support-article
updated_at: '2026-02-04T13:36:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007187161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA910-Qual-a-diferen%C3%A7a-entre-Sitef-Antigo-FINA910-e-Sitef-Novo-FINA918
---

**Dúvida**  
Qual a diferença entre Sitef Antigo FINA910 e Sitef Novo FINA918?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA910 - A partir da versão12.0  
  
**Solução**  
A diferença são:

**FINA910 (Sitef Antigo)**:

 -  A partir da versão 12.1.25

 - Concilia somente cartões de crédito da administradora Software Express

 - Aceita somente arquivo com extensão .CSV

 - Ao processar o arquivo da **Software Express** pela **rotina FINA910,** é populada a **tabela FIF**, faz a conciliação e se confirmar, efetua a baixa na mesma rotina.

**FINA914, FINA916, FINA917, FINA918 (Sitef Novo):**

 - A partir da versão 12.1.27

 - Concilia os Cartões de Crédito da Administradora **Software Express**, **Cielo**, **Amex**, **Rede**

 - Aceita arquivo com extensão .CSV, TXT

 - Para importar o arquivo, deve-se utilizar a rotina **FINA914 -** Wizard de importação (Popula a **tabela fif**)

 - Se desejar e for para seu controle, poderá efetuar a conciliação de venda pela **rotina FINA916** - **Conciliação de Vendas** (conciliação prévia, apenas um controle a mais).

 - Pela rotina **FINA917,** pode consultar o log de importação caso tenha algum problema. (grava log nas tabelas)

 - Por último, a rotina **FINA918** - Conciliação do pagamento (efetua a baixa).

**Importante**  
A rotina FINA910 será descontinuada em 04/04/2022.

**Saiba mais**  
[Conciliador Pagamentos e Vendas](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)
