---
article_id: 14174203170455
category: RH - CNAB
content_hash: 42ad94c21484f615da9a40625d9409024d582657b33b3280612725bdb29ef914
fetched_at: '2026-06-28T22:43:39.291134+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o arquivo CNAB apresenta
  valores divergentes ou log em branco
type: support-article
updated_at: '2025-06-16T14:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14174203170455-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-arquivo-CNAB-apresenta-valores-divergentes-ou-log-em-branco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32844460743319)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O que verificar quando o arquivo CNAB apresenta valores divergentes ou log em branco?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução:**1) Verifique se existe **valor líquido** na folha de pagamento;  
  
**Atenção:** Observe que a busca de líquido de pagamento será realizado nas verbas de base:  
**- Líquido de Folha:** verba com ID 0047  
**- Líquido de Férias:** verba com ID 0102  
**- Líquido de rescisão:** verba com ID 0126  
**- Líquido de 1ª parcela de 13º:**verba com ID0678  
**- Líquido de  2ª parcela de 13º:** verba com ID 0021  
**- Líquido Adiantamento:**verba com ID 0546  
**- Líquido VEX:** verba com ID 1411  
**- Líquido PLR:** verba com ID 0836  
  
2) Verifique se a data informada nos campos **Data de Pagamento De** / **Data de Pagamento Até**, estão de acordo com a data no cálculo da verba, seja informando a própria data ou se a data informada de/até contém a data do cálculo:  
![GPEM080confere1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/14234317369367)

**Observação**: a conferência da data de pagamento pode ser realizado no cadastro de períodos, caso seja folha de pagamento, PLR ,VEX e adiantamento. Para férias e rescisão os valores podem ser observados no próprio cálculo. 

3) Caso os valores estejam duplicados , além da conferência referente a data informada, verifique também os seguintes detalhes:

**-> Folha com período fechado:**como as verbas deverão ser transportadas para o movimento de histórico (SRD), verifique se existe incorretamente a mesma verba de líquido nas tabelas SRC e RGB.

**-> Folha com período aberto:**verifique se existe pagamento anterior com mesma data.

4) Verifique se existe banco, agência e conta cadastrada no Cadastro de funcionários. Acesse Atualizações -> Atualizações -> Funcionários e verifique na Aba funcionais os campos:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14637130426647)

5) Importante verificar se a opção selecionada nas perguntas GERAR CONTA TIPO , corresponde ao cadastro do funcionário, pois se existem funcionários com conta corrente e conta poupança , deve ser selecionada a opção AMBAS:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19059165327255)

6) Caso seja gerado o LOG de Geração de Líquidos em Arquivo e o arquivo TXT não seja gerado, realize um teste com o arquivo CNAB anexo correspondente ao utilizado (CNAB modelo 1, CNAB modelo 2 ou SISPAG).  Sendo gerado com o modelo padrão disponibilizado (anexo), revalide seu arquivo de configuração:  
**![GPEM080confere2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/14234316258839)**

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
