---
article_id: 115008354807
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 17fd983cab15b0c3a6dd71d2ecbcf657e1185e30622906f7fec1c462cef076e2
fetched_at: '2026-06-28T22:40:47.482774+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGACTB - ECF - Mensagem
  CH5_IDCTAR
type: support-article
updated_at: '2022-06-03T22:49:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008354807-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGACTB-ECF-Mensagem-CH5-IDCTAR
---

**Ocorrência**

Ao entrar no ambiente de contabilidade gerencial/central de escrituração é exibido a mensagem: CH5\_IDCTAR

**Ambiente**  
Protheus – Contabilidade Gerencial – 12.1.17   
  
**Causa**A ocorrência se deve pelo fato da Natureza da conta do plano referencial ser diferente da natureza da conta do plano associada (ct1\_ntsped)  
  
**Solução**

Após associar a uma conta referencial com a mesma natureza, não apresentou a mensagem, assim como os registros do bloco L foram gerados no TAF que antes não haviam sido gerados.

Erro 1 - Linha: 2 - Coluna: 3 e 4

O valor '041.02.06.01.31' informado no campo ID Conta Referencial (CH5\_IDCTAR) não existe na base de dados.

|T010|19800101|04|1|5|411101|DESPESAS COM IMOBILIZADOS|||4111|19800101|

|T010AA||04|1.02.06.01.31|201

Veja :<http://tdn.totvs.com/display/public/PROT/ECF0008_Mensagem_CH5_IDCTAR>

Para maiores informações, acessar o link: <http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>

Veja Também : [MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)
