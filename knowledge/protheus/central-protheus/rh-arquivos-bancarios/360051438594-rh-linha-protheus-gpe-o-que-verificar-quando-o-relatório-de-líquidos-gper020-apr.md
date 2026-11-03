---
article_id: 360051438594
category: RH - Arquivos Bancarios
content_hash: b117bea950f884c56012d8033d62170d2ba05bf42e43b1df6eac918549aaeb96
fetched_at: '2026-06-28T22:43:38.223675+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE  - O que verificar quando o Relatório de líquidos
  GPER020 apresenta valores divergentes ou log em branco
type: support-article
updated_at: '2026-06-25T20:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051438594-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-Relat%C3%B3rio-de-l%C3%ADquidos-GPER020-apresenta-valores-divergentes-ou-log-em-branco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32323958004119) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**  
O que verificar quando o Relatório de líquidos GPER020 apresenta valores divergentes ou log em branco?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução:**  
1) Verifique se existe **valor líquido** na folha de pagamento;  
  
**Atenção:** Observe que a busca de líquido de pagamento será realizado nas verbas de base:  
  
**- Líquido de Folha:** verba com ID 0047  
**- Líquido de Férias:** verba com ID 0102  
**- Líquido de rescisão:** verba com ID 0126  
**- Líquido de 1ª parcela de 13º:** verba com ID0678  
**- Líquido de  2ª parcela de 13º:** verba com ID 0021  
**- Líquido Adiantamento:** verba com ID 0546  
**- Líquido VEX:** verba com ID 1411  
**- Líquido PLR:** verba com ID 0836  
  
2) Verifique se a data informada nos campos **Data de Pagamento De** / **Data de Pagamento Até**, estão de acordo com a data no cálculo da verba, seja informando a própria data ou se a data informada de/até contém a data do cálculo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080941734)

**Observação:** a conferência da data de pagamento pode ser realizado no cadastro de períodos, caso seja folha de pagamento, PLR ,VEX e adiantamento. Para férias e rescisão os valores podem ser observados no próprio cálculo. 

3) Caso os valores estejam duplicados, além da conferência referente a data informada, verifique também os seguintes detalhes: 

**-> Folha com período fechado:** como as verbas deverão ser transportadas para o movimento de histórico (SRD), verifique se existe incorretamente a mesma verba de líquido nas tabelas SRC e RGB.

**-> Folha com período aberto:** verifique se existe pagamento anterior com mesma data.

**Saiba Mais:**  
[RH - Arquivos Bancários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)
