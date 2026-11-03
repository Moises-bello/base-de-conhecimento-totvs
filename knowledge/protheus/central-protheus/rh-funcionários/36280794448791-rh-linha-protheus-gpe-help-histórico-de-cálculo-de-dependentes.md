---
article_id: 36280794448791
category: RH - Funcionários
content_hash: 509fdf496ade850d83828f8f35880604f218119d03f8ff45ed1af4ffa916aebc
fetched_at: '2026-06-28T22:43:28.509966+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: 'RH - Linha Protheus - GPE - Help: Histórico de cálculo de dependentes'
type: support-article
updated_at: '2025-11-12T22:01:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36280794448791-RH-Linha-Protheus-GPE-Help-Hist%C3%B3rico-de-c%C3%A1lculo-de-dependentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36280804528151) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao realizar manutenção ou exclusão no cadastro de dependente é apresentado a mensagem:  
**Help: Histórico de cálculo de dependentes**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - 12.1.2310  
  
**Causa**  
Após a execução do cálculo de Folha Pagamento (Férias, Rescisão ou 13º Salário) e gravação na tabela RU6 – Histórico de Dependentes **não é possível realizar nenhum tipo de manutenção no cadastro de Dependentes.**  
  
**Solução**  
A mensagem será apresentada nos seguintes cenários:

**1.** Caso o usuário altere o conteúdo do campo Tipo Dep. IRRF (RB\_TIPIR) para 4-Não é dependente e existir cálculo, a alteração não será permitida sendo exibida a seguinte mensagem ao usuário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36280794440983)

**2.** Caso o usuário tente excluir o dependente com o conteúdo do campo Tipo Dep. IRRF (RB\_TIPIR) **diferente de 4-Não é dependente** e existir dados na tabela de Histórico, a exclusão **não será permitida**sendo exibida a seguinte mensagem ao usuário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36280804534039)

Apenas será possível prosseguir com a manutenção se o cálculo for cancelado. Para consultar qual cálculo está relacionado ao dependente acesse **Outras Ações > Histórico** no Cadastro de Dependentes  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36281022250391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36281083152407)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como cancelar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050830934-RH-Linha-Protheus-GPE-Como-cancelar-c%C3%A1lculo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como efetuar cancelamento de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052940993-RH-Linha-Protheus-GPE-Como-efetuar-cancelamento-de-c%C3%A1lculo)
