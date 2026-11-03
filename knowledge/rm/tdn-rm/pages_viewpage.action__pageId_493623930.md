---
content_hash: 64394730d2be6ef8b96830491847eb85928daf4d3aa1332f0c20f9fbcbba3af1
fetched_at: '2026-06-29T00:10:21.750855+00:00'
page_id: '493623930'
product: rm
source: tdn-rm
title: Anexo "Histórico de Percentuais para INSS" do cadastro de seção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493623930
version: 20
---

Foi criado o anexo "Histórico de Percentuais para INSS" no cadastro de seção para auxiliar os estabelecimentos que optam pelo recolhimento por filial, permitindo a alteração dos percentuais.

### Pré-requisitos:

Para habilitar o histórico, o usuário deverá ativar o parâmetro "Habilita Histórico de INSS no Cadastro de Seção".

### Utilização do Histórico:

1. **Selecionar Seção Centralizadora**: O usuário deve selecionar a seção centralizadora onde deseja salvar os históricos.
2. **Abrir o Anexo de Percentuais para INSS**: No anexo, inserir os valores dos percentuais de empresa, SAT e terceiros, juntamente com a vigência.

### Considerações:

* **Habilitação do Parâmetro**: Se o parâmetro "Habilita Histórico de INSS no Cadastro de Seção" estiver habilitado, os históricos serão considerados na geração da Guia de INSS e da Folha Analítica.
* **Ausência de Histórico**: Caso não haja histórico cadastrado para o mês/ano definido no momento da geração dos processos, será considerado o percentual informado na tela principal.

**Atenção :**

1. Caso o parâmetro esteja marcado a prioridade será a leitura do histórico. Caso não haja valor no histórico , será considerado o percentual  informado na Tela da geração da Guia de INSS.
2. Somente  será permitido cadastrar o histórico de percentuais para as s**eções Centralizadoras** ou **seções conforme a quebra de FPAS cadastrada em Parametrizador | eSocial | Lotação Tributária**.
3. Mais informações sobre a geração da Guia de INSS (comercialização ou folha de pagamento) com a leitura do Histórico de Percentuais para INSS :  ["Faturamento Bruto".](http://tdn.totvs.com.br/display/LRM/Faturamento+Bruto)

### Atenção:

* **Prioridade de Leitura**: Caso o parâmetro esteja marcado, a prioridade será a leitura do histórico. Se não houver valor no histórico, será considerado o percentual informado na tela da geração da Guia de INSS.
* **Cadastro do Histórico**: O histórico de percentuais só poderá ser cadastrado para as **seções centralizadoras** ou para **seções conforme a quebra de FPAS** cadastrada em **Parametrizador | eSocial | Lotação Tributária**.

### Parametrização:

* No Parametrizador confirme o parâmetro "Habilita Histórico de INSS no cadastro de seção", conforme demonstrado abaixo:

* No Cadastro de Perfis permitir acesso no item **01.01.51 - Seções**.

* Será visualizado no cadastro de Seções o anexo "Histórico de Percentuais para INSS".

**Exemplo:**

* + Foi informado na seção centralizadora o  percentual  12,02.

**Folha Analítica**

Ao gerar Folha Analítica com o parâmetro global **"****Habilita Histórico de INSS no Cadastro de Seção"**marcado, se houver histórico cadastrado na vigência correspondente ao Mês/Ano parametrizado no processo, ele será lido para calcular o INSS Empresa e o valor informado na tela será desconsiderado.

* No exemplo abaixo, foi cadastrado 10% no histórico de percentuais para a vigência 3/2018 - 12/2018. O INSS Empresa foi gerado utilizando o percentual do histórico.

[Retornar página anterior](http://tdn.totvs.com.br/pages/viewpage.action?pageId=490324995)
