---
article_id: 360028792131
category: RH - CNAB
content_hash: 6f64367b2cb7bf39b2924c8f95c95b4ed867fc7b9ad9e607bdf37fbe64cfdda3
fetched_at: '2026-06-28T22:43:39.196778+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivo líquido CNAB do roteiro VEX
type: support-article
updated_at: '2025-09-18T19:29:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028792131-RH-Linha-Protheus-GPE-Como-gerar-arquivo-l%C3%ADquido-CNAB-do-roteiro-VEX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32879339231127)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como gerar arquivo líquido CNAB do roteiro VEX?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

1) Para geração do arquivo CNAB será necessário cadastrar uma verba utilizando o identificador de cálculo disponibilizado 1411-Liquido Valores Extras.  
  
Essa verba deve ser cadastrada como uma verba do tipo base provento, configurando o campo Tipo do Cód. (RV\_TIPOCOD) com 3-Base (Provento).  
  
O valor dessa verba será gerado após a execução do roteiro de Cálculo Valores Extras (VEX) e será utilizada pelas rotinas de geração do CNAB/SISPAG e Relação de líquidos.

**Esse identificador de cálculo é obrigatório para geração do CNAB.**Mais informações acesse sobre o cálculo VEX acesse: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018301831-MP-GPE-Roteiro-de-C%C3%A1lculo-VEX-Valores-Extras?source=search>

2) Cadastrar o roteiro VEX no cadastro de períodos (Atualizações -> Definições de cálculo -> Períodos):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029331832)

3) Exemplo dos valores lançados e calculados na tabela RGB (Atualizações -> Definições de Cálculo -> Por funcionário), apresentando a verba com ID de cálculo 1411 (799 - Líquido de Val Extras):

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029331811)**

4) Relatório de folha do roteiro VEX com as informações do cálculo realizado (Relatórios -> Periódicos -> Folha de Pagamento: ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029332151)

5) No grupo de perguntas da rotina (Miscelânea-> Líquido ->Geração de Arquivo Líquido), configurar o campo roteiro = VEX e no campo Data de pagamento de/até, observar a data de pagamento utilizada no cadastro de períodos para o roteiro VEX:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029343072)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029345251)

06) O relatório do Log de geração do arquivo líquido será apresentado com os valores correspondentes aos lançados no roteiro VEX:  ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029346571)

**Saiba Mais**[Artigos CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
