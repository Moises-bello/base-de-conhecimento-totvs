---
article_id: 360026231891
category: Gestão de Transportes (TMS)
content_hash: 91b47f1d2ce783c3b9d5d54dd6e0adce306803241d17e512943f9abe1809d1ae
fetched_at: '2026-06-28T22:45:29.168102+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Fatura por Documento
type: support-article
updated_at: '2025-07-24T12:46:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026231891-Log%C3%ADstica-Linha-Protheus-TMS-Fatura-por-Documento
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19881349110295)*Tempo aproximado para leitura: **00:01:10 min****Dúvida**Como utilizar a rotina **Fatura** **por Documento**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Utilização da **Fatura por Documento**  
  
No Menu acessar: **Atualizações** / **Financeiro** / **Fatura por Docto - TMSA850**Esta rotina permite aglutinar vários documentos de transporte em uma única fatura - título a receber, com diversas parcelas para o mesmo cliente, com isso é possível selecionar apenas os documentos da loja informada ou documentos independentes de loja. Os títulos a receber são gerados para o cliente informado na seleção dos documentos.  
  
A fatura do cliente aparece na tela, apresentando o valor máximo da fatura, caso haja configuração definida no **Perfil do Cliente**, os documentos relacionados e a quantidade de documentos que estão relacionados.  
  
O Documento incluso manualmente, deve pertencer a mesma filial de débito e o mesmo cliente informado na tela inicial da fatura deve estar com *status* **Em Aberto**, ou seja, ainda não baixado e faturado.  
  
**Atualizações / Comercial / Perfil do Cliente - TMSA480**Permite relacionar os dados comerciais e financeiros com a possibilidade de agrupar clientes para o pagamento de frete, especificando dados sobre a geração da fatura, cálculo do documento.  
  
Com as configurações do **Perfil do Cliente**, é possível definir:

* **Fatura Manual**
* **Tipo de Faturamento**
* **Parâmetro: MV\_TMSMFAT**=**2** - Faturamento a partir da tabela **DT6**.
* **Tipos de Documento** - atalho **F5**, disponível em **Ações Relacionadas**: Tipos de documentos que permitem gerar a Fatura. Caso esteja selecionado, gera a fatura separadamente para cada tipo de documento.

**Parâmetros Utilizados:**

* **MV\_TMSMFAT**: Modo de Faturamento do **TMS - Gestão de Transporte**. Opções disponíveis: **1**-Faturamento a partir da tabela **SE1**/ **2**-Faturamento a partir da tabela **DT6**.
* **MV\_FATPREF**: Prefixo do título da fatura de transporte.
* **MV\_NATFAT**: Código da Natureza do título de transporte.
* **MV\_TIPFAT**: Tipo do título da fatura de transporte.
* **MV\_TMSTIPT**: Tipo do título a ser gerado no Contas a Receber.
* **MV\_NUMFAT**: Número sequencial de Faturas.

**Importante**  
No **TOTVS Logística TMS Protheus**, nunca se deve utilizar a **Condição de Pagamento** do **Tipo = 9 ou B**, pois ao utilizar qualquer um destes tipos, o Sistema não irá gerar a fatura na tabela **SE1**.  
  
**Saiba mais**  
Mais informações poderão ser acessadas no *link:*[Logística - Linha Protheus - TMS - Como configurar o parâmetro MV\_TMSTIPT?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9986662499863-Log%C3%ADstica-Linha-Protheus-TMS-Como-configurar-o-par%C3%A2metro-MV-TMSTIPT)
