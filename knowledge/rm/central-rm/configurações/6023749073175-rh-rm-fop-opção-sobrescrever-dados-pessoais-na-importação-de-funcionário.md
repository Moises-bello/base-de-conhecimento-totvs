---
article_id: 6023749073175
category: Configurações
content_hash: 635ee2fb17e5666a2ab42018a8ac9711f9e7f63208c1a82607b09c779c40975e
fetched_at: '2026-06-28T22:46:49.517942+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Opção sobrescrever Dados Pessoais na importação de Funcionário
type: support-article
updated_at: '2025-08-07T13:51:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6023749073175-RH-RM-FOP-Op%C3%A7%C3%A3o-sobrescrever-Dados-Pessoais-na-importa%C3%A7%C3%A3o-de-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34013237286167) Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como realizar importação do funcionário verificando se a **pessoa** já existe na base, e caso exista, sobrescreva os Dados Pessoais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o módulo  **Folha de Pagamento | Configurações | Importações |  Importações de Dados da Folha de Pagamento**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34013263761303)  
  
2. Ao acessar a rotina marque a opção a seguir:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34013237292567)  
  
**Exemplo:**Funcionário já está cadastrado em nossa base com a chapa: 00078. Importação do funcionário alterando o campo **Nome**, referente a dados pessoais, e o campo **Função**, referente a dados contratuais, somente com o parâmetro**Sobrescrever Dados Pessoais** marcado.  
O sistema irá realizar a importação com sucesso, porém irá sobrescrever somente os **dados pessoais**, ou seja, o campo **Nome**, será alterado em todas as coligadas. O campo **Função** não sofrerá alteração:  
  
  
  
**Importante**

* A verificação da existência da **Pessoa** é analisada pelos campos: CPF e Data de Nascimento  ou Nome e Data de Nascimento em todas as coligadas;
* O parâmetro apresentado poderá ser utilizado conforme necessidade na importação;
* Caso realize a importação de um novo funcionário e o mesmo já possua a pessoa cadastrada e não marque o parâmetro **Sobrescrever Dados Pessoais**, a importação ocorrerá com sucesso, porém não haverá atualização de dados cadastrais.
