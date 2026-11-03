---
article_id: 360018993471
category: RH - CNAB
content_hash: 4280b4d421f922cd514843a7789b7c97c80d090fb2a6e9622f860e9f35c50860
fetched_at: '2026-06-28T22:43:39.246192+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Função para gerar sequência numérica referente
  ao lote do CNAB da Folha de Pagamento
type: support-article
updated_at: '2025-06-16T18:44:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018993471-RH-Linha-Protheus-GPE-Fun%C3%A7%C3%A3o-para-gerar-sequ%C3%AAncia-num%C3%A9rica-referente-ao-lote-do-CNAB-da-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32851842485143)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**No módulo de Gestão de Pessoal, **qual função padrão** pode ser usada para gerar uma**sequência numérica referente ao lote do arquivo CNAB da Folha de Pagamento**?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para geração da sequência numérica referente ao lote do CNAB de Folha de Pagamento, poderá ser utilizada a função padrão **CNABSequencia()**, que é chamada na rotina **GPEM080** no momento da geração do arquivo.   
  
Para que a função funcione corretamente, é necessário cadastrar os dados da instituição bancária na tabela **S052** (SIGAGPE -> Atualizações -> Manutenção de Tabelas) com o número inicial para a sequência e também é necessário que faça a leitura da tabela na rotina de geração de líquido , de modo que o SEQUENCIAL DO ARQUIVO seja atualizado após o processamento.   
  
Acesse Atualizações -> Definições de Cálculo -> Manutenção de Tabelas -> Código S052   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12461683981079)

Ao efetuar a configuração das perguntas , faça a leitura da tabela S052 de acordo com o banco pagador :

![S052.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/17215002322455)

Processo realizado para alteração da tabela S052 e arquivo CNAB gerado com o código sequencial.   
![GIFTAB052.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17215414120727)

Anexo um arquivo configurado com a função para apoio na configuração.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045165513-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM080)

[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
