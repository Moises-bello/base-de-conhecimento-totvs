---
article_id: 4404095499543
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2196f292fe8d967b44eac676b11d22c393141a709771c9371b1a1d1506b080c0
fetched_at: '2026-06-28T22:38:43.843307+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Acerto do Parâmetro
  MV_DOCSEQ no Faturamento
type: support-article
updated_at: '2021-07-12T13:56:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404095499543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Acerto-do-Par%C3%A2metro-MV-DOCSEQ-no-Faturamento
---

**Dúvida**Ao realizar um faturamento sistema aponta uma inconsistência e solicita ajuste do **Parâmetro MV\_DOCSEQ**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

O parâmetro **MV\_DOCSEQ** é responsável por **controlar a numeração** de registros de Movimentação das Tabelas **SD1** (**Itens NF de Entrada**), **SD2** (**Itens NF de Saída**) e **SD3** (**Movimentações Internas**).

Quando há inconsistência na configuração do Parâmetro, o sistema informa através da mensagem de Help "Problema no conteúdo do parâmetro **MV\_DOCSEQ"**

Dessa forma é necessário informar a maior numeração das tabelas no parâmetro.

Para realizar o **levantamento da maior numeração gravada** deve-se seguir o procedimento: **[Como corrigir a mensagem AJUSTAR PARAMETRO MV\_DOCSEQ](https://tdn.totvs.com/display/PROT/Como+corrigir+a+mensagem+AJUSTAR+PARAMETRO+MV_DOCSEQ)**

• Abrir as tabelas **SD1, SD2 e SD3**.

• Em cada uma destas tabelas, verificar qual é o maior valor gravado para os campos **D1\_NUMSEQ**, **D2\_NUMSEQ** e **D3\_NUMSEQ**.

• Após identificar o maior valor, informa-lo no parâmetro **MV\_DOCSEQ**.

• Após realizar uma nova movimentação (interna, NF entrada ou NF saída) e verificar se será apresentada alguma mensagem de validação. Caso continue sendo apresentada, significa que o valor informado no parâmetro não foi o maior valor entre os registros da tabela. Dessa forma deve-se realizar o procedimento novamente.

**Obs.:** Caso possua **mais de uma Filial**, verifique se as Tabelas estão em modo Exclusivo. Sendo assim, confirme se as **SX2 (Mapeamento de Tabelas)** e **SX6 (Parâmetros)** são exclusivas.

**Mais informações:** **[Numeração Sequencial de Movimentação MV\_DOCSEQ](https://tdn.totvs.com/pages/viewpage.action?pageId=6085087)**

**[MP - SIGAEST - Problema no conteúdo do parâmetro MV\_DOCSEQ ao fazer movimentações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011729672-MP-SIGAEST-Problema-no-conte%C3%BAdo-do-par%C3%A2metro-MV-DOCSEQ-ao-fazer-movimenta%C3%A7%C3%B5es)**

**Em caso de problemas relacionados ao parâmetro, contate a Equipe de Estoque para auxiliar no processo.**
