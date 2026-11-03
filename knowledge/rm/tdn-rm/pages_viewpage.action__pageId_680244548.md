---
content_hash: 009716999f662e1b157169445caa4f5952c48dcf8e113ba4ea1c04ae68e88144
fetched_at: '2026-06-29T00:11:17.446874+00:00'
page_id: '680244548'
product: rm
source: tdn-rm
title: Empreendimento - Vacância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680244548
version: 31
---

O rateio de Vacância tem como finalidade ratear o valor dos Imóveis vagos para os lojistas ou empreendedores.  
Abaixo seguem os tipos de rateio de vacância:

3

### **Rateio linear entre empreendedores / sócios**

---

Esta modalidade de rateio, ocorre quando os imóveis pertencentes a um empreendimento estejam vagos, então o sistema irá repassar os valores de vacância destes imóveis diretamente para os empreendedores / sócios cadastrados no empreendimento, conforme o percentual definido nos dados de repasse no cadastro do empreendimento.

Esta documentação se aplica ao Condomínio Integral.

Para entender como realizar o Rateio entre Lojistas e Percentual de ocupação no Condomínio Individual ou Por Competência, **[consulte a documentação aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=980988616)**

Importante lembrar que cada sócio pode ter uma participação diferente no empreendimento, sendo assim o valor de vacância será sempre sobre este percentual de participação.

Para cadastrar um sócio / empreendedor, [consulte a documentação aqui (clique aqui)](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

O exemplo abaixo reflete este cálculo:

Temos um fechamento de condomínio onde apenas 3 dos 20 imóveis estão ocupados.

Desta forma, todos os valores dos 17 imóveis restantes serão repassados aos sócios.

Este repasse é realizado apenas após a **geração dos lançamentos de Condomínio**. Este processo deve ser executado em [*Processos / Gerar lançamentos*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105232).

Após a geração dos lançamentos teremos uma informação adicional em *Anexos / Histórico de cálculos,* que retratará na forma de um log este rateio:

Clicando nesta linha do rateio, teremos o log detalhado.

Neste caso, o sócio A com 60% de participação e o sócio B com 40%:

### **Rateio entre Lojistas**

---

Ao acessar o Cadastro de Empreendimentos clique no menu Vacância e em seguida no campo Modelo de cálculo de rateio para vacância selecione a opção **“Rateio entre Lojistas”**

Ao selecionar esta opção, caso o imóvel esteja vago, deve-se realizar a soma de todos os condomínios que possuem imóvel vago e ratear linearmente entre os Lojistas.

ATENÇÃOOs exemplos abaixo utilizam a funcionalidade do Condomínio Integral para exemplificar os tipos de rateio existentes.  
Para o condomínio individual, o procedimento é diferente. Para realizar o Rateio entre Lojistas ou por Percentual de Ocupação utilize o processo **Calcular Rateio de Vacância**. [Maiores informações, consulte a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=980988616)

**Realizando o rateio de vacância**

---

**Para que o sistema realize o rateio, será necessário realizar os seguintes processos:**

* Calcule o Fechamento;

* Selecione as opções respectivas necessárias para realização do cálculo;

* Ao acessar Histórico de cálculos, observe na guia “**Apurações”** os valores gerados respectivamente para cada um dos imóveis. Em destaque os imóveis que possuem, contratos de locação associados;

* Após o sistema finalizar o cálculo, é possível editar este registro gerado e visualizar a memória de cálculo realizada pelo sistema; Veja esta descrição utilizada no exemplo:

* Em processos, Gere os lançamentos Financeiros. Este processo irá incluir os lançamentos Financeiros rateados para cada lojista;
* Ao realizar a edição de um registro de apuração na tela de Fechamento do condomínio, é possível acessar o lançamento financeiro gerado para este Lojista.

### **Rateio por percentual de ocupação**

---

Ao acessar o Cadastro de Empreendimentos clique no menu Vacância e em seguida no campo Modelo de cálculo de rateio para vacância selecione a opção **“Rateio por percentual de ocupação”**

No campo percentual de ocupação, o usuário deverá informar o percentual de ocupação máximo exigido para cobrança entre os Sócios.  
Exemplo: se informar no campo o valor de 20% de ocupação, e o empreendimento possui um percentual alugado que seja maior do que este percentual, será gerada a cobrança para o Lojista.

Caso contrário, ou seja, se o percentual de ocupação em determinada competência, for menor ou igual ao estipulado neste parâmetro, toda a cobrança será gerada para os Sócios do Empreendimento.  
Neste exemplo que iremos abordar utilizaremos para este empreendimento o valor de percentual de 20% de ocupação, e veremos que ao realizar o processo de geração de lançamentos os valores serão rateados entre os lojistas;

Observe que os 4 imóveis selecionados possuem associados em seus cadastros o contrato de Locação já incluídos no sistema, ou seja, tratam-se de imóveis já locados, cada qual com o seu respectivo contrato de locação associado. Já os outros 7 imóveis estão vagos, sem contrato de locação associados. Ou seja, neste cenário possuo 36% de ocupação. Logo o sistema irá gerar toda a vacância para os lojistas.

* Acesse o menu Fechamento do condomínio, incluindo um registro de fechamento para este empreendimento:

* Calcule o Fechamento:

* Será apresentada no campo Memória de cálculo, o modelo de cálculo do rateio de vacância é Rateio entre lojistas por percentual de ocupação:

### **Tipo de Imóvel não considerado no rateio**

---

Ao se tratar de rateio de vacância exista a possibilidade de alguns imóveis não serem incluídos no rateio.

Para isso no cadastro de empreendimento no menu vacância existe o cadastro de **"Tipo de Imóvel não considerado no cálculo"** onde podemos inserir os tipos de imóveis que não serão considerados no rateio.  
Após isso, deve se ir ao cadastro de imóveis e para todo imóvel que não esteja alugado e que não deve ser considerado no rateio inserir no campo **"Tipo de Imóvel"**o mesmo tipo cadastrado na tela do empreendimento.

Importante: No [condomínio individual](https://tdn.totvs.com/pages/viewpage.action?pageId=857578505), quando um imóvel possui um tipo não considerado na vacância, seu status, (Campo Status) na lista de apuração irá ser "**Vacância Ignorada**".

**Saiba mais**

---

[TOTVS Construção Gestão de Imóveis - Condomínio - Fechamento do Condomínio](https://tdn.totvs.com/pages/viewpage.action?pageId=435105112)
