---
article_id: 360051180213
category: RH - Definições de Cálculo
content_hash: 71d93f9f02de0d18b33db015f869ea4dee73bf59f848a767a16ad7fac264a519
fetched_at: '2026-06-28T22:43:22.310559+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar exceções para Filiais em Manutenção
  de Tabelas
type: support-article
updated_at: '2025-10-03T17:32:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051180213-RH-Linha-Protheus-GPE-Como-cadastrar-exce%C3%A7%C3%B5es-para-Filiais-em-Manuten%C3%A7%C3%A3o-de-Tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27052675969303) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como cadastrar exceções para Filiais em Manutenção de tabelas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Quando as tabelas **RCC** e **RCB** são compartilhadas **(CCC)**, a gravação dos dados não inclui código de filial, já que as informações incluídas nela valem para todas as entidades cadastradas no ambiente. Contudo, podem existir casos que a filial não se enquadra na configuração das demais.

Para incluir exceção para uma ou mais filiais, faça o seguinte processo:  
  
**1.** Acessar a rotina de Manutenção de Tabelas - GPEA320 em **Atualizações> Definições de Cálculo> Manutenção de Tabelas**;

2 - Selecione a tabela que deseja incluir uma exceção e clique em **Alterar** no Menu **Outras Ações** (utilizaremos como exemplo a tabela S043 - Tipos de Rescisão);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27052675981335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27052671207575)  
  
  
**3.** Posicione o cursor na última linha da tabela e pressione **seta para baixo**no seu teclado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27052671209751)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27052675989527)  
  
  
**4.** Inclua o código da Filial desejada e informe as demais informações da tabela;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078345513)

**5.** Clique em **Salvar**para gravar as alterações.  
  
Desta forma o Sistema priorizará a informação com campo filial preenchido.  
Caso não existe exceção cadastrada, será utilizada a regra padrão configurada.

**Saiba mais:**

[RH - Definições de Cálculos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011913513-RH-Defini%C3%A7%C3%B5es-de-C%C3%A1lculo)
