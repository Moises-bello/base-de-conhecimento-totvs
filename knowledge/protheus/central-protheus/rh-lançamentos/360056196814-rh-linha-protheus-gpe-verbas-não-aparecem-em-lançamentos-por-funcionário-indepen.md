---
article_id: 360056196814
category: RH - Lançamentos
content_hash: a46bd8a8787df611e0385f3edf769a821b601f8829c54011f87f56c332e89b3e
fetched_at: '2026-06-28T22:43:31.428913+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas não aparecem em Lançamentos Por Funcionário,
  independente da origem
type: support-article
updated_at: '2024-09-13T16:40:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056196814-RH-Linha-Protheus-GPE-Verbas-n%C3%A3o-aparecem-em-Lan%C3%A7amentos-Por-Funcion%C3%A1rio-independente-da-origem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354085065879) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Verbas não aparecem em Lançamentos Por Funcionário, independente da origem.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Este problema normalmente acontece quando existem **divergências** entre o **compartilhamento** e o **conteúdo** gravado na **SRV** **- Cadastro de Verbas.**

Será necessário verificar o compartilhamento da Tabela SRV pelo Configurador (**SIGACFG**) com senha de **administrador,** se está **Compartilhada** (C) ou **Exclusiva** (E) e verificar se dentro da Tabela SRV o **campo filial** está em branco ou preenchido.  
  
Acesse pelo SIGACFG no menu **Base de Dados > Dicionário > Base de Dados**. Selecione a opção **Dicionário de Dados** e busque na lupa pela **SRV.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26354101766167)  
  
Clique em **Visualizar** e confirme o compartilhamento da mesma.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26354101768343)  
  
Se o compartilhamento estiver **C,** o campo filial deve estar em **branco,** se estiver com compartilhamento **E**, o campo filial deve estar **preenchido.**  
  
No exemplo acima, em modo compartilhado, a SRV deve estar com todos os campos **Filial** em Branco.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26354085072663)  
  
Só pode existir um tipo de informação na SRV, não pode ter as duas situações.

**Saber mais**

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555452-MP-GPE-Como-cancelar-valores-lan%C3%A7ados-na-rotina-de-Valores-Futuros?source=search)

[RH - Linha Protheus - GPE - Impressão de relatório de Valores Futuros GPER570](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052070034-MP-GPE-Impress%C3%A3o-de-relat%C3%B3rio-de-Valore-Futuros-GPER570?source=search)

[RH - Linha Protheus - GPE - Relatório Valores Futuros em planilha (GPER570)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053605673-MP-GPE-Relat%C3%B3rio-Valores-Futuros-em-planilha-GPER570-?source=search)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
