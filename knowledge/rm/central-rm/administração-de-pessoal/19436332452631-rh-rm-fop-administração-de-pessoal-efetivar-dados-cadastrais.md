---
article_id: 19436332452631
category: Administração de Pessoal
content_hash: 9657d2e27a89777a738424322aeb880ae0f103d197d262bab92f77e3c479bec6
fetched_at: '2026-06-28T22:47:01.194614+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Administração de Pessoal: Efetivar Dados Cadastrais'
type: support-article
updated_at: '2025-03-05T17:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19436332452631-RH-RM-FOP-Administra%C3%A7%C3%A3o-de-Pessoal-Efetivar-Dados-Cadastrais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19436268000023) Tempo aproximado para leitura: **00:02:11 min****Dúvida**Como realizar a efetivação dos dados cadastrais?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2310.120
* e Superiores.

**Solução**É possível realizar a efetivação dos Dados Cadastrais por dois caminhos: No momento da Liberação de competência ou pelo processo disponibilizado no sistema que deverá ser utilizado quando o usuário não realizar a efetivação da alteração no momento da liberação de competência.

Para isso, é necessário seguir os seguintes passos: 

1. Acesse **Administração de Pessoal | Alterações Cadastrais | Efetivar Dados Cadastrais**:

![](https://tdn.totvs.com/download/thumbnails/687158765/image-2023-11-9_16-24-5.png?version=1&modificationDate=1699557845397&api=v2&effects=border-simple,shadow-kn) 

2. Dessa forma, será apresentada uma tela onde é possível selecionar os funcionários e escolher a quebra de seção desejada. Realize a parametrização e execute o processo:

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-9_16-25-23.png?version=1&modificationDate=1699557923543&api=v2&effects=border-simple,shadow-kn)

Após a execução deste processo o sistema irá:

* Atualizar os dados cadastrais (PFUNC) que foram alterados através de uma requisição;
* Criar o registro nos anexos dos históricos (Salarial, Seção, Função) que foram alterados na requisição;
* Atualizar o rateio fixo no cadastro do funcionário;
* Limpar os dados do anexo "Histórico Dados Cadastrais Futuro".

**IMPORTANTE:**

* A efetivação somente poderá ser realizada quando a data de alteração for dentro da competência atual.
* O sistema não irá inserir registro nos anexos dos históricos com data anterior à próxima competência.

**OBSERVAÇÃO:** Caso o usuário opte por efetivar os dados cadastrais na Liberação da competência, é necessário seguir as instruções da documentação disponibilizada:

[RH - RM - FOP - Folha Mensal: Efetivar Dados Cadastrais na Liberação de Competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19436267832855-RH-RM-FOP-Folha-Mensal-Efetivar-Dados-Cadastrais-na-Libera%C3%A7%C3%A3o-de-Compet%C3%AAncia-?source=search)

**Saiba Mais:**

[RH - RM - FOP - Parametrização e Cadastro do Histórico Dados Cadastrais Futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19403698359575-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-e-Cadastro-do-Hist%C3%B3rico-Dados-Cadastrais-Futuro?source=search)

[Histórico Dados Cadastrais Futuro](https://tdn.totvs.com/pages/releaseview.action?pageId=687158765#1-6)
