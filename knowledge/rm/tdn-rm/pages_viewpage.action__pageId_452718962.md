---
content_hash: bcc31e95afdb21bf5f531e924e35f96b9ed05654eff52ebeb35a32e561b10837
fetched_at: '2026-06-29T00:10:02.569631+00:00'
page_id: '452718962'
product: rm
source: tdn-rm
title: Inclusão de Cliente/Fornecedor - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718962
version: 5
---

O processo tem por objetivo incluir Cliente/Fornecedor através do cadastro de um funcionário, copiando também os dados bancários do funcionário. Esse Cliente/Fornecedor será utilizado para geração dos lançamentos de estorno, e outros pagamentos para os funcionários.

Existem 3 possibilidades para execução do processo, de acordo com os dados do funcionário:  
   
1.   Funcionário que não possui Cliente/Fornecedor associado, e não existe cadastro de Cliente/Fornecedor com o seu CPF.  
No processo deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre as contas bancárias alternativa e principal. Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO). Será inserido um registro de Dados Bancários (FDADOSPGTO).  
   
2.    Funcionário que não possui Cliente/Fornecedor associado, mas existem um ou mais registros de Cliente/Fornecedor com o seu CPF.  
Serão exibidos os registros de Cliente/Fornecedor encontrados, o usuário poderá escolher um deles para associar ao funcionário, ou optar por criar um novo.   
   
Caso seja utilizado um Cliente/Fornecedor já existente, a próxima etapa exibirá o Cliente/Fornecedor, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.  
Será inserido registro de Dados Bancários apenas (FDADOSPAGTO). O Cliente/Fornecedor será associado ao usuário, mas não sofrerá alterações.  
   
Caso seja selecionada a opção 'Criar um novo Cliente/Fornecedor', deverá ser informado um código para o cliente/fornecedor e escolhida uma conta bancária entre as contas bancárias alternativa e principal.   
0Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO). Será inserido um registro de Dados Bancários (FDADOSPGTO).  
   
3.   Funcionário que possui Cliente/Fornecedor associado.  
Será exibido o Cliente/Fornecedor que está associado, não precisando informar o código. A conta bancária a ser cadastrada nos dados bancários do CliFlor poderá ser escolhida entre as contas Principal e Alternativa do funcionário.  
Será inserido e associado ao usuário um registro de Cliente/Fornecedor (FCFO). Será inserido um registro de Dados Bancários (FDADOSPGTO).  
   
**Observação**

Quando incluindo um novo Cliente/Fornecedor, através do cadastro ou através do processo 'Inclusão de Cliente/Fornecedor', será solicitado um código para o mesmo. Esse código obedece a uma máscara que pode ser definida nos Parâmetros Gerais do Totvs Gestão Financeira (Contas a Pagar | Manutenção de Lançamentos | Lançamento). Caso a máscara definida seja numérica, é possível marcar o parâmetro 'Usar código sequencial', caso marcado, o código será gerado automaticamente, não precisando informa-lo ao executar o processo.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Inclusão de cliente/Fornecedor -  Dependente](https://tdn.totvs.com.br/pages/viewpage.action?pageId=563426898)
