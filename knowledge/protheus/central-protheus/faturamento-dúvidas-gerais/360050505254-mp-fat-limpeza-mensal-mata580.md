---
article_id: 360050505254
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 9464986041a9dfacc982005abb6fc9663e8b4cd1b4fb57a69945c38e29a31907
fetched_at: '2026-06-28T22:38:31.090127+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Limpeza Mensal - MATA580
type: support-article
updated_at: '2021-04-28T15:53:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050505254-MP-FAT-Limpeza-Mensal-MATA580
---

**Dúvida**

Explicativo do processamento da limpeza dos dados.  
   
 **Ambiente**

Microsiga Protheus – A partir da versão 12.  
  
**Solução**

A rotina efetua limpeza de registros(deleta) já atendidos das tabelas Pedido de Venda(SC5 e SC6) e Pedido Liberado(SC9) e Documentos de Saída(SD2 e SF2), e posteriormente gera um arquivo com dados deletados.  
  
Serão consideradas as seguintes informações para a limpeza:

* Pedidos de Venda (SC5 e SC6): pedido encerrados, ou seja, todos com itens atendidos ou com resíduos eliminados, dentro do período indicado.
* Pedidos Liberados (SC9): registros que consta como liberado e tem documento de saída;
* Documentos de Saída(SD2 e SF2): registros do tem número de nota fiscal.

**IMPORTANTE**: Não recomendado utilizar a rotina por que ao processar os dados são deletados de pedidos e documento de saída, e se posteriormente as informações não será mais visualizada em browser ou relatórios.

1. Acessar Ambiente Faturamento, Miscelânea, Ajustes, Limpeza Mensal(**MATA580**);

2. Parâmetros:

* Elimina Documento de Saída: Informe se terá limpeza da SD2 e SF2;
* Elimina liberações de PV: Informe se terá limpeza da SD9
* Elimina Pedidos de Venda: Informe se terá limpeza da SC5 e SC6;
* Roda Exclusivo: Informe se o processamento deve ser executado em modo exclusivo;
* Data Limite: data final a ser considerada para a seleção dos registros nas tabelas de dados;
* Diretório: Informe o diretório \system\ onde serão gravados os registros deletados da base de dados principal.

3. Ao terminar o processamento será gerado os arquivos na system na extensão .CSV com este padrão de nome:  
Primeira posição o Alias;  
Segunda posição o Código da Empresa;  
Terceira posição o Dia do processamento (data base);  
Quarta posição o Mês do processamento (data base).  
  
**Saiba mais: [Limpeza Mensal](https://tdn.totvs.com/x/FhoPIQ)**
