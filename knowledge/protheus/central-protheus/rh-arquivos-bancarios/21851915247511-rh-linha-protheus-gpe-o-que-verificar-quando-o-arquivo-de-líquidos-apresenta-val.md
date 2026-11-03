---
article_id: 21851915247511
category: RH - Arquivos Bancarios
content_hash: 95954a1e1ad49ab3ca8a67eab09a0e0581a86c8cbe6d7508ad779f5288db9279
fetched_at: '2026-06-28T22:43:38.338635+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o arquivo de líquidos apresenta
  valores divergentes, duplicados ou log em branco
type: support-article
updated_at: '2025-09-19T22:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21851915247511-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-arquivo-de-l%C3%ADquidos-apresenta-valores-divergentes-duplicados-ou-log-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21851915243287) Tempo aproximado para leitura: **00:01:00 min  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.

**Dúvida**  
O que verificar quando o arquivo de líquidos apresenta valores divergentes, duplicados ou log em branco?

**Solução:**  
**1)** Verifique se existe a verba de valor líquido no cálculo (folha de pagamento/ Adiantamento/férias/rescisão/PLR/13º)  
  
**Atenção:** Observe que a busca de líquido de pagamento será realizado nas verbas de base:

- Líquido de Folha: verba com ID 0047  
- Líquido de Férias: verba com ID 0102  
- Líquido de rescisão: verba com ID 0126  
- Líquido de 1ª parcela de 13º: verba com ID0678  
- Líquido de 2ª parcela de 13º: verba com ID 0021  
- Líquido Adiantamento: verba com ID 0546  
- Líquido VEX: verba com ID 1411  
- Líquido PLR: verba com ID 0836

**2)** Verifique se a data informada nos campos **Data de Pagamento De / Data de Pagamento Até,** estão de acordo com a data no cálculo da verba, seja informando a própria data ou se a data informada de/até contém a data do cálculo:

**Observação:** a conferência da data de pagamento pode ser realizado no cadastro de períodos, caso seja folha de pagamento, PLR ,VEX e adiantamento. Para férias e rescisão os valores podem ser observados no próprio cálculo.

**3)** Caso os valores estejam duplicados , além da conferência referente a data informada, verifique também os seguintes detalhes:

**-> Folha com período fechado:** como as verbas deverão ser transportadas para o movimento de histórico (SRD), verifique se existe incorretamente a mesma verba de líquido nas tabelas SRC e RGB ou se ocorreu pagamento em período anterior com a mesma data na própria tabela SRD.

**-> Folha com período aberto:** verifique se existe pagamento anterior com mesma data.

**4)** Ao configurar a opção quanto a Conta corrente (COM, SEM ou AMBOS), verificar se existe banco, agência e conta cadastrada no Cadastro de funcionários. Acesse Atualizações -> Atualizações -> Funcionários e verifique na Aba funcionais o preenchimento das informações.

**Saiba Mais:**  
[Página Centralizadora dos Arquivos Bancários - GPE](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)
