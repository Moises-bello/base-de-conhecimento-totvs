---
content_hash: 14b27cef68738f4af96251dee9248d045e4ecbda5dd989e85abd24f1177b7c18
fetched_at: '2026-06-29T00:10:22.068147+00:00'
page_id: '496388652'
product: rm
source: tdn-rm
title: Anexo | Histórico de Percentuais para INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496388652
version: 91
---

Este anexo foi disponibilizado no cadastro de seção para atender as situações onde é necessário a discriminação do Percentual de INSS. Dessa forma, ao gerar Folha Analítica ou Guia de INSS retroativa, o usuário poderá optar por ler os percentuais guardados neste histórico.

Como pré-requisito para habilitar o uso do histórico, o usuário deverá habilitar o parâmetro **"Habilita Histórico de INSS no Cadastro de Seção"** existente em: Parametrizador | Folha Normal | Encargos Sociais:

Após habilitar o parâmetro, o anexo ficará visível em Administração de Pessoal | Cadastros | Seções | Anexos.

O usuário deverá selecionar a **seção centralizadora** ou **a seção conforme a quebra de FPAS cadastrada em Parametrizador | eSocial | Lotação Tributária** que deseja cadastrar os históricos, abrir o anexo de "Histórico de Percentuais para INSS" e cadastrá-los conforme necessidade.

Para realizar o cadastro do histórico, o usuário deverá preencher o início e o fim da vigência e os percentuais nos campos: **%Empresa**, **%Autônomos**,**%Acid. Trabalho** e **%Terceiros**  referente à vigência.

Se o parâmetro "**Habilita Histórico de INSS no Cadastro de Seção"**estiver marcado, os históricos serão considerados na geração da Guia de INSS e Folha Analítica. Caso não haja histórico cadastrado no mês/ano definido no momento da geração dos processos, será considerado o percentual informado na tela.

**ATENÇÃO:**

1. Caso o parâmetro esteja marcado a prioridade será a leitura do histórico. Caso não haja valor no histórico, será considerado o percentual informado na tela da geração da Guia de INSS .
2. Somente será permitido cadastrar o histórico de percentuais para as Seções Centralizadoras.
3. Mais informações sobre a geração da Guia de INSS (comercialização ou folha de pagamento) com a leitura do Histórico de Percentuais para INSS :  ["Faturamento Bruto".](http://tdn.totvs.com.br/display/LRM/Faturamento+Bruto)

Ao marcar o parâmetro **'Discriminar Percentual de Terceiros'** em Parametrizador | Folha Normal | Encargos Sociais**,** será disponibilizada a aba **'Percentuais de Terceiros'** no menu Administração de Pessoal | Cadastros | Seções | Anexos | Histórico de Percentuais para INSS para que o usuário realize o cadastro dos percentuais de terceiros discriminados conforme Tabela de Códigos de Receita da DCTFWeb eSocial.

Parametrizador | Folha Normal | Encargos Sociais

Cadastros | Seções | Anexos | Histórico de Percentuais para INSS

**ATENÇÃO:**

Quando o parâmetro "**Discriminar Percentual de Terceiros"** esta marcado o sistema irá desabilitar o campo **'% Terceiros'** e apresentará neste campo a soma dos valores informados na aba **'Percentuais de Terceiros'.**

**Permissão - Perfis de Acesso**

No Cadastro de Perfis permitir acesso no item 01.01.51-Seções.

**Guia de INSS**

falseATENÇÃO!

A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.  
Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: <https://tdn.totvs.com/pages/viewpage.action?pageId=727915586>  
Para conferência dos valores da DCTFWeb, consulte a documentação: <https://tdn.totvs.com/pages/viewpage.action?pageId=717708785>

Ao gerar a Guia de INSS com o parâmetro habilitado, serão considerados os percentuais do histórico de INSS e desconsiderado o valor informado na tela para o campo Empresa e do cadastro de Seção para os campos Terceiros e Acidente de Trabalho.

**Folha Analítica**

Ao gerar Folha Analítica com o parâmetro global **"****Habilita Histórico de INSS do Anexo do Cadastro de Seção"**marcado, se houver histórico cadastrado na vigência correspondente ao mês/ano parametrizado no processo, ele será lido para calcular o **INSS Empresa**, **INSS SAT e INSS Terceiro** sendo que o valor informado na tela será desconsiderado.

* No exemplo abaixo, foi cadastrado 20,00 no **% Empresa**, 3,00 no **% Acid. Trabalho** e 5,8 no **% Terceiros** no histórico de percentuais para INSS com a vigência 3/2018 - 12/2018. O INSS Empresa, INSS SAT e INSS Terceiro, foram gerados multiplicando os percentuais informados no histórico.

*divs*
