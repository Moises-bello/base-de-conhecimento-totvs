---
article_id: 360019899972
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: f282f8af4fa3d9e14dcdbad34675f565149eee001352787a687784382a902de4
fetched_at: '2026-06-28T22:41:48.409174+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Chave duplicada na SN2
  ao incluir descrição estendida do bem
type: support-article
updated_at: '2023-11-30T17:08:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019899972-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Chave-duplicada-na-SN2-ao-incluir-descri%C3%A7%C3%A3o-estendida-do-bem
---

**Dúvida**

Erro log apresentado ao incluir descrição estendida no bem

THREAD ERROR ([5288], magali.morais, SPON010114086) 22/11/2018 13:57:34

DB error (Insert): -37 File: SN2040 - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Não é possível inserir uma linha de chave duplicada no objeto 'dbo.SN2040' com índice exclusivo 'SN2040\_UNQ'. O valor de chave duplicada é (00 , 0001, 01 , 10, \*\*, 0). ( From tISAMFile::Write )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015838472)

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução:**Pelo Configurador altere o tamanho do campo "N2\_SEQUENC" do tamanho 2 para o tamanho 3.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015838512)
