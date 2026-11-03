---
article_id: 360059275933
category: Inspeção de Processos (SIGAQIP)
content_hash: 6103cc61bfb7da7e9cbb139a2c5369cdcaf661562c24ad83592ba592b156fb2c
fetched_at: '2026-06-28T22:42:25.790653+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QPXSKLNUMOP ao informar o código
  do produto
type: support-article
updated_at: '2025-04-11T14:41:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059275933-Manufatura-Linha-Protheus-SIGAQIP-Help-QPXSKLNUMOP-ao-informar-o-c%C3%B3digo-do-produto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31342707742487)***Tempo aproximado para leitura: **00:01:40 min**  
**Ocorrência**Ao informar um código de produto na rotina **MATA650 - Ordens de Produção**, o Sistema apresenta o *help* **QPXSKLNUMOP - Devido ao controle de Skip-Lote do ambiente Inspeção de Processos o número da Ordem de Produção foi alterado.**  
  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**Quando o produto possui integração com o módulo **SIGAQIP - Inspeção de Processos**, através do preenchimento do campo **B1\_TIPOCQ - Tipo de C.Q**. com o conteúdo **Q** e o parâmetro **MV\_QIPMAT - Indica se o módulo de Inspeção de Processos está integrado com materiais** possui o conteúdo **S**, a ordem de produção que está sendo incluída no momento sempre deve ter o número, preenchido no campo **C2\_NUM - Número da OP**, maior do que a **OP - Ordem de Produção** incluída anteriormente.  
Isso é necessário, pois o número da **OP** é uma informação chave para ordenar as **OPs** e aplicar corretamente o conceito de **skip-lote** a cada **OP**, identificando corretamente quais **OPs** devem ser certificadas.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Observar qual o maior número da **OP** existente na tabela **SC2 - Ordens de Produção;**  
2. Corrigir a numeração sugerida pelo Sistema através da rotina **APCFG110 - Controle de numeração**, alterando o próximo número da tabela **SC2** para o maior número existente atualmente nesta tabela somado de 1;  
3. Não alterar o número da **OP** sugerido ao incluir uma **OP** no **MATA650**.  
  
**Saiba mais**Para mais informações sobre o ajuste do número da **OP** veja a documentação do *link*: [Manufatura - Linha Protheus - SIGAPCP - Alterar o número da ordem de produção sugerida pelo Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044950994-MP-SIGAPCP-Como-corrigir-o-n%C3%BAmero-da-ordem-de-produ%C3%A7%C3%A3o-sugerida-pelo-Sistema?source=search)  
  
**Observação**Nas versões **12.1.2310** e **12.1.2410** o **help QPXSKLNUMOP foi descontinuado** em 10.04.2025 conforme documentação [Descontinuação help QPXSKLNUMOP](https://tdn.totvs.com/pages/releaseview.action?pageId=931602838). Caso seu fonte esteja desatualizado, verifique a aplicação do pacote [Manufatura - Linha Protheus - SIGAQIP - Pacote de Atualização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12320591674519-Manufatura-Linha-Protheus-SIGAQIP-Pacote-de-Atualiza%C3%A7%C3%A3o) ou solicite apoio ao Suporte Técnico.
