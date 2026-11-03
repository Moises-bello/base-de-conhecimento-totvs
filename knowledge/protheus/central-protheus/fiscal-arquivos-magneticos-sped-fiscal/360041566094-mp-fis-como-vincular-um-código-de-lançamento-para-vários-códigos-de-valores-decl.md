---
article_id: 360041566094
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 89dd64a887e88c2df1fefcb9c5695ab648484fbe842d474e1f4a32d5e0466656
fetched_at: '2026-06-28T22:42:03.878176+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP- FIS- Como vincular um Código de Lançamento para vários Códigos de Valores
  Declaratórios  para escriturar corretamente o registro C197 EFD ICMS/IPI.
type: support-article
updated_at: '2021-04-28T14:25:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041566094-MP-FIS-Como-vincular-um-C%C3%B3digo-de-Lan%C3%A7amento-para-v%C3%A1rios-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-para-escriturar-corretamente-o-registro-C197-EFD-ICMS-IPI
---

**Dúvida**

Como vincular um Código de Lançamento para vários Códigos de Valores Declaratórios para escriturar corretamente o registro C197 EFD ICMS/IPI?  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

Após reformulação da rotina FISA140 foi incluso o campo F3K\_CODLAN para gerar os lançamentos da apuração na tabela CDA.

Ao preencher o campo F3K\_CODLAN serão escriturados na tabela Lançamentos do Documento Fiscal (CDA) e podem ser visualizados na Aba Lançamentos da Apuração de ICMS e também é feito a amarração do código da tabela 5.2 correspondente ao código de lançamento da tabela 5.3.

Ao utilizar essa configuração não será necessário fazer a amarração TES X Lançamentos Da Apuração na Rotina Tipos de Entrada e Saída (MATA080).

Assim possibilita o vínculo de um Código de Lançamento (F3K\_CODLAN) para vários Códigos de Valores Declaratórios (F3K\_CODAJU).

O funcionamento da rotina através das configurações deste documento só funcionará quando o parâmetro MV\_MTCLF3K estiver com 1 (Enquadramento por grupos: cliente, produto e fornecedor).

Informações adicionais:

[FIS0005\_SPED\_FISCAL](https://tdn.totvs.com/x/MYGUD)

[FIS0006\_Códigos\_de\_Lançamento\_e\_Reflexos\_da\_Apuração](https://tdn.totvs.com/x/uI6UD)

[FIS0085\_Produto x Código de Valores Declaratórios\_F3K](https://tdn.totvs.com/x/rXcMEQ)

[FIS0087\_Informações Adicionais da Apuração de ICMS (E115 e 1925)](https://tdn.totvs.com/x/RJ8TEQ)

[FIS0005\_INCENTIVOS E BENEFÍCIOS FISCAIS](https://tdn.totvs.com/x/nTn7Gw)

[Melhoria na amarração para o código de valor declaratório do ICMS da tabela 5.2 e novo tratamento do vínculo da tabela 5.3 para mais de um código 5.2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=520651465)
