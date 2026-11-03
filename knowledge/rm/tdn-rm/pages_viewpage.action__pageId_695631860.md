---
content_hash: 766f3b95fbe9acbce871a012cff9f22bcfab4d96ea947fcb4b216b729d9c1843
fetched_at: '2026-06-29T00:11:21.429526+00:00'
page_id: '695631860'
product: rm
source: tdn-rm
title: DT - Nome Social - Mensagens de sugestão, aprovação e reprovação de férias
  RM Portal e MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=695631860
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Mensagens de sugestão, aprovação e reprovação de Férias RM Portal e MDI |
| País: | Brasil |
| Ticket: | S/N |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-2588](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2590) |

## **02. SITUAÇÃO/REQUISITO**

Atendendo a Portaria 1.036/2015 ([https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo\_pdf)](https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo_pdf) "Follow link") será implementado nas mensagens de sugestão, aprovação e reprovação disparadas pelos processos de férias (RM Portal e MDI) a opção de enviar o Nome Social ao invés do Nome do funcionário.

## **03. SOLUÇÃO**

Foi implementado nas mensagens disparadas pelos processos de férias (RM Portal e MDI)  a opção de enviar o Nome Social ao invés do Nome do funcionário. Para que o RM Portal e MDI envie o Nome Social nas mensagens de sugestão, aprovação e reprovação de férias, deverá ser marcado o parâmetro 'Exibir nome social do funcionário', disponível em RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais.

**Exemplo:**

**1) Em RM | RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Funcionários, cadastrar o Nome Social do funcionário:**

**2) Acessar RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais e marcar 'Exibir nome social do funcionário':**

**3) Acessar o RM Portal:**

**a) Cadastrar uma Sugestão de Férias:**

**E-mail enviado para o chefe (sugestão de férias):**

**E-mail enviado do chefe para o funcionário (Reprovação da sugestão de férias):**

**E-mail enviado do chefe para o funcionário (Aprovação da sugestão de férias):**

**4) Aprovação de férias pela MDI:**

**a) Férias 'D - Aguardando aprovação do DP':**

**Aprovação de Alterações Cadastrais:**

**E-mail enviado do chefe para o funcionário (Aprovação da sugestão de férias):**
