---
content_hash: 96adbb3da78a9227f76b14599bf03e95bd1a914451427d4da28c870113d1cece
fetched_at: '2026-06-29T00:10:18.467569+00:00'
page_id: '4811967'
product: rm
source: tdn-rm
title: RMFIN000014_RPA - pagamento de tributos incidentes
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIN000014_RPA+-+pagamento+de+tributos+incidentes
version: 5
---

BLOCK

RPA - pagamento de tributos incidentes

FAQ: **RPA - pagamento de tributos incidentes**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Solução

|  |  |
| --- | --- |
| **Introdução**  O RPA Recibo de Pagamento de Autônomo a Pessoa Física possui características e tributação específica, porém variável de acordo com o valor e o tipo do serviço prestado. Nesta operação incidem o IRRF e INSS.   Para determinadas categorias poderá incidir também o ISS.  O IRRF será calculado de acordo com a tabela Progressiva do Imposto de Renda e o INSS de acordo com a tabela da Previdência Social.  [image](http://lh5.ggpht.com/_G7KXZLoZDsY/TN2M2j6VYAI/AAAAAAAADn0/4rP9j1shy7E/s1600-h/image%5B10%5D.png) |  |
|  |  |
| **Desenvolvimento/Procedimento.**    **TOTVS Gestão Fiscal**    **1º – Cadastro de Tributo**  Cadastrar os tributos IRRF, INSS e ISS com as respectivas alíquotas.  **2º Cadastro de Período de Apuração**  Cadastrar os Períodos de Apuração relacionados.        **TOTVS Gestão Financeira:**    **1º. Cadastro de Tipo de Documento:**    Cadastrar quatro de Documentos:  Exemplo:  01. Descrição: “Gerador de INSS e IRRF” – informar classificação = Gera INSS e IRRF.  02. INSS do Empregador – sem classificação  03. INSS do Empregado – sem classificação  04. IRRF a Recolher PF – sem classificação  **2º. Cadastro do Cliente Fornecedor:** - Cadastrar o Fornecedor - Previdência Social/ Receita (para pagamento de Tributos relacionados)  - Cadastrar o Fornecedor – SECRETARIA DE RECEITA FEDERAL (para pagamento das DARF´s)    - Cadastrar o fornecedor - Prestador de Serviço do RPA.   Informar todos os dados necessários zelando para que não falte nenhuma informação essencial ao processo, principalmente:  · Pasta “Identificação”. Campo “Categoria” deverá ser Pessoa Física e “Numero de Dependentes” informados se houver. O numero de dependentes é utilizado no cálculo de dedução para fins de IRRF.  [clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TN2M4Qu-3HI/AAAAAAAADn8/YFkvPuVwoKk/s1600-h/clip_image004%5B4%5D.jpg)  · Pasta “Dados Fiscais”, informar o código da receita, essencial para o processo.  [clip_image006](http://lh6.ggpht.com/_G7KXZLoZDsY/TN2M6lruWdI/AAAAAAAADoE/CnFmhmwJXCc/s1600-h/clip_image006%5B4%5D.jpg)  **3º. Acessar o Assistente de Implantação de Processos, etapa 02.01.01.03.01 – IRRF-PF e definir os parâmetros, conforme o modelo abaixo.**    **[clip_image008](http://lh4.ggpht.com/_G7KXZLoZDsY/TN2M8ylje4I/AAAAAAAADoM/ZgkaCa4zMlE/s1600-h/clip_image008%5B4%5D.jpg)**      **[clip_image010](http://lh6.ggpht.com/_G7KXZLoZDsY/TN2M-17Bu7I/AAAAAAAADoU/PlGasKqoMyM/s1600-h/clip_image010%5B4%5D.jpg)**    Indicar os campos conforme os dados cadastrados nos itens 1 e 2 citados acima(Gestão Financeira).  **4º. Acessar o Assistente de Implantação de Processos, etapa 02.01.01.03.03 – INSS-PF e definir os parâmetros, conforme o modelo abaixo.**    *[clip_image012](http://lh4.ggpht.com/_G7KXZLoZDsY/TN2NAeAJNtI/AAAAAAAADoc/uTSwi4Ky1vQ/s1600-h/clip_image012%5B4%5D.jpg)*  Indicar conforme os dados cadastrados nos itens 1 e 2 citados acima(Gestão Financeira).          **TOTVS Gestão de Estoque, Compras e Faturamento:**    **1º. Parametrizar o Tipo de Movimento**  Acessar o Assistente de Implantação de Processos e parametrizar um Tipo de Movimento que contenha essencialmente os seguintes requisitos:  · Etapa 53 - Parâmetros de Faturamento, campo “Tipo de Documento Duplicata Default” = tipo de documento com classificação Gera INSS e IRRF.  · Etapa 61 – Escrituração Fiscal, informe o “Tipo documento Escrituração”.  · Etapa 63 – Tributação Item: Indicar os Tributos IRRF ,INSS e ISS (para as categorias de serviços cujo o tributo incide).  **2º. Incluir o movimento.**  Verifique se gerou corretamente a tributação do item do movimento.  Nesse momento serão gerados no sistema de Gestão Financeira três lançamentos, sendo:  · Um Lançamento Financeiro no valor do serviço (RPA)  · Um lançamento Financeiro equivalente ao INSS empregado  · Um lançamento Financeiro equivalente ao IRRF. |  |
| **TOTVS Gestão Fiscal**    **3º** **Cadastro de Período de Apuração**    **. IRRF**  A guia DARF referente ao tributo IRRF deve ser gerada no sistema de Gestão Fiscal, para que o mesmo seja considerado na geração das obrigações acessórias como DCTF e DIRF.  Após o encerramento do Período de Apuração do Tributo, clique no ícone “Inserir DARF automaticamente” na pasta Guias. O sistema irá gerar guia(s) DARF para os lançamentos de IRRF gerados pelo sistema de Gestão Financeira.  [imagem](http://lh3.ggpht.com/_G7KXZLoZDsY/TN2NBp2nnjI/AAAAAAAADok/1nf68h1NuCM/s1600-h/imagem%5B2%5D.png)  **4º. ISS**  Para os serviços prestados através de RPA’s que incidirem ISS, o Movimento criado no sistema de Gestão de Materiais precisa ser escriturado para o sistema de Gestão Fiscal, para que seja considerado na apuração do ISS, também, na geração das obrigações acessórias municipais.  Para a apuração do ISS, é imprescindível que o tributo esteja informado na pasta Outros Tributos do Lançamento Fiscal juntamente com o Tipo de Recolhimento. Deve ser informado, também, o município onde o serviço é prestado (pasta Outros Dados / Prestação de Serviço).  [imagem1](http://lh4.ggpht.com/_G7KXZLoZDsY/TN2NDYYt8TI/AAAAAAAADos/Vb_ftAhip0o/s1600-h/imagem1%5B1%5D.png)  [imagem3](http://lh3.ggpht.com/_G7KXZLoZDsY/TN2NEqyfYKI/AAAAAAAADo0/v12Rhi-CsJc/s1600-h/imagem3%5B1%5D.png)  Após o encerramento do Período de Apuração do Tributo, clique no ícone “Inserir Guias ISSQN automaticamente” na pasta Guias. O sistema irá gerar guia(s) de ISS com os valores devido pela empresa nas operações próprias e, também, para os valores retidos de terceiros.  [imagem4](http://lh6.ggpht.com/_G7KXZLoZDsY/TN2NGQ5PAII/AAAAAAAADo8/D394GoP_4jY/s1600-h/imagem4%5B2%5D.png) |  |
| **Informações Adicionais**  A GPS é gerada pelo TOTVS Gestão Folha de Pagamento. Portanto é necessário avaliar o processo para que não gere lançamentos em duplicidade.  Para garantir maior flexibilidade, o Gestão Financeira disponibiliza recurso para que o processo do INSS não gere lançamentos Financeiros(parâmetos do INSS print acima).  Lembre-se:  O valor do INSS interfere no cálculo do IRRF. |
