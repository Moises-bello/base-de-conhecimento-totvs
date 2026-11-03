---
article_id: 9453877629079
category: Gestão
content_hash: a5e3de8e1393d02f40dbd16b7983dc07ac95ae9d1bcfc3cc7026aa4e60d61a0a
fetched_at: '2026-06-28T22:46:48.182544+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - Nome social nos relatórios RM Reports
type: support-article
updated_at: '2024-09-13T14:22:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9453877629079-RH-RM-FOP-Nome-social-nos-relat%C3%B3rios-RM-Reports
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23539630627735) Tempo aproximado para leitura: **00:02:25 min****Dúvida**Quais relatórios foram modificados para trazer o nome social do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2209  
  
**Solução**

Atendendo a Portaria 1.036/2015 ([https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo\_pdf)](https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo_pdf) "Follow link") será implementado nos relatórios do **RM Reports** de  Demonstrativo de Pagamento, Aviso e Recibo de Férias a opção de exibir o Nome Social ao invés do Nome do cadastro de funcionário.

Os relatóriosforam ajustados para obter o nome social caso tenha sido informado no cadastro do funcionário e marcado o parâmetro **Exibir Nome Social do Funcionário**, disponível em **RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais**. Com ele desmarcado continua sendo exibido o **nome** do cadastro de funcionário.

Exemplo:

Em **RM | RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Funcionários,** cadastre o **Nome Social** para o funcionário:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454852940951)

Acesse **RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais** e marque o parâmetro **Exibir nome social do funcionário**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454313654935)

Em **RM | RH | Folha de Pagamento| Gestão| TOTVS Compartilhamento,** importe os relatórios alterados:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454563286935)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454602807191)

Em **RM | RH | Folha de Pagamento | Gestão | RM Reports,** gere os relatórios:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9455569762711)

Os relatórios que sofreram alteração são:

1) Demonstrativo de Pagamento

**FOPREL00015 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport**

**FOPREL00016 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport**

**FOPREL00176 - Envelope Pgto Portal Padrão.TotvsReport**

**FOPREL00177 - Envelope Pgto Portal Personalizado ORACLE.TotvsReport**

**FOPREL00178 - Envelope Pgto Portal Personalizado SQL.TotvsReport**

**FOPREL00192 - Envelope pgto Model Extrato (frenteverso).TotvsReport**

**FOPREL25.0025 - 2.004.101 - Envelope de pagamento - Labo 05.0.TotvsReport**

2) Aviso de Férias

**FOPREL00200 - Aviso de Férias (Modelo 3).TotvsReport**

**FOPREL00193 - Aviso de Férias - Modelo 2.TotvsReport**

**FOPREL00180 - Aviso de Férias - ORACLE.TotvsReport**

**FOPREL00030 - Aviso de Férias.TotvsReport**

3) Recibo de Férias

**FOPREL00112 - Recibo de Férias.TotvsReport**

**FOPREL00190 - Recibo de Férias RM Portal.TotvsReport**

**FOPREL00194 - Recibo de Férias(Modelo 2).TotvsReport  
  
Todos disponíveis na ferramenta TOTVS COMPARTILHAMENTO:  
[RH - RM - FOP- Importação de relatórios e layouts através do Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)**
