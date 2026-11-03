---
article_id: 1500003971702
category: License Sever Virtual
content_hash: 96e834c67da50d07736f5e968eec63b4a8935b3958feb5a3cd5ded1b2663cd5a
fetched_at: '2026-06-28T22:42:20.041252+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Conceito do consumo de licenças Totvs I
type: support-article
updated_at: '2024-08-06T18:32:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003971702-Framework-Linha-Protheus-Conceito-do-consumo-de-licen%C3%A7as-Totvs-I
---

**Dúvida**  
Como funciona o consumo de licenças TOTVS I no Protheus?  
  
**Ambiente**Protheus - LS Virtual - Todas as versões  
  
**Solução**A licença I é consumida em threads HTTP que são usadas para responder portais ou Web Services.   
Seu consumo segue a configuração contida na chave Instances (<http://tdn.totvs.com/display/tec/Instances>), existente dentro dos arquivos de configuração dos serviços Protheus.  
  
Exemplo de consumo:   
Considerando o exemplo contido no link do TDN:   
[localhost/ws]   
Enable=1  
Path=C:\Data\Web\ws  
Environment=Environment   
Instances=5,20,3,5   
DefaultPage=wsindex.apw

Logo de início seriam consumidas 5 licenças, e de acordo com a demanda seu consumo poderia atingir o máximo de 20 licenças.  
  
Por padrão, se uma thread HTTP ficar ociosa por mais de 60 minutos ela é encerrada e a licença I que estava sendo consumida é liberada, esse comportamento pode ser alterado através de chaves configuradas dentro do INI do ambiente Rest.

* [Mudança dos timeouts nas requisições REST 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=697263324)

A configuração da chave Instances deve ser dimensionada de acordo com a demanda de cada cliente. Se por ventura mais de um server utilizar essa configuração, o máximo de licenças consumidas é a soma de todas as configurações de Instances.   
  
A relação do consumo também se baseia no tempo em que a thread permanece ativa. Em um cenário onde possui uma aplicação que faz uma requisição a um serviço web, deve-se avaliar o tempo que está requisição fica ativa, isso, leva com que a licença permaneça em consumo até o fim do processamento.   
  
Assim, em um total de X licenças, apenas essa requisição fará o consumo de uma licença.   
  
Se uma thread HTTP ficar ociosa por mais de 60 minutos ela é encerrada, e a licença I que estava sendo consumida é liberada, mas respeitando o limite inicial e o limite mínimo de threads livres configurado.

**Composição dos valores da chave**

O valor dessa chave é composta das definições dos valores ***mínimo***,***máximo***,***mínimo livre*** e ***incremento***. Onde:

* mínimo: indica a quantidade inicial de threads que serão disponibilizadas.
* máximo: indica a quantidade máxima de threads que serão disponibilizadas.
* mínimo livre: indica a quantidade mínima de threads livres.
* incremento: indica a quantidade de novas threads que serão disponibilizadas quando o número de threads livres esteja abaixo do valor previamente definido.  
  O incremento respeita a quantidade máxima de threads configuradas. Deste modo, a quantidade de novas threads liberadas é igual ao menor valor entre o incremento e a diferença do máximo e threads em uso.
* OBS: Recomendamos a configuração do terceiro parâmetro, onde o serviço acatará sempre a quantidade de threads indicadas.  
  Caso não exista a configuração do terceiro parâmetro, ao iniciar o serviço, serão consumidas duas licenças.

Instances=1,1,1

**Consumo de Licença por demanda no REST do Protheus****:**

 

O consumo de licença sob demanda é uma abordagem no Protheus que permite que o serviço REST utilize licenças somente quando uma API está sendo usada, em vez de manter uma licença em uso para cada thread em execução no REST.  
  
Para ativar o consumo de licença sob demanda, é necessário configurar uma opção na seção de endereço (URI) no arquivo de configuração do AppServer. Essa opção é chamada de "Stateless" e deve ser definida como "1" para ativar o uso de licenças apenas quando necessário.  
  
Se essa opção não estiver presente ou se estiver definida como zero, o consumo de licença será mantido no início de cada tarefa. Como essa configuração é específica para cada endereço (URI), é possível ter diferentes modelos de licenciamento em uma mesma porta, cada um associado a uma URI diferente.  
  
A conexão do tipo **StateLess** realiza uma conexão não persistente com o License Server, renovando esta conexão a cada x minutos.

**Importante:****Não é possível a utilização da chave Stateless nas configurações via SOAP (WebService), pois a chave está preparada somente para uso do Rest.**

**Exemplo de utilização da chave Stateless:**

[URIHTML]  
URL=/rest/app  
PrepareIn=All  
Instances=2,2  
CORSEnable=1  
AllowOrigin=\*  
**Stateless=1**

**Teste das requisições\Relação de licenças:**  
É possível efetuar a análise das requisições das APIs customizadas por meio de ferramentas de mercado, (Ex. [**Apache** **JMeter**](https://jmeter.apache.org/), software de código aberto), simulando o comportamento funcional e medindo o desempenho a partir de testes de carga e de estresse em recursos estáticos ou dinâmicos.

**Importante:  
A TOTVS não disponibiliza suporte para ferramentas de mercado, conforme exemplo citado acima.**

**Saiba Mais**

[**Instances - TOTVSTEC**](https://tdn.totvs.com/display/tec/Instances)[**Consumo de Licença por demanda no REST do Protheus**](https://tdn.totvs.com/pages/releaseview.action?pageId=527852596)

[**Controle de Licenças dos Aplicativos - MINGLE**](https://tdn.totvs.com/pages/releaseview.action?pageId=544190925)[**Configuração do REST Protheus para uso com os aplicativos**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519719292) [**Mobile**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519719292)

**[Mudança dos timeouts nas requisições REST](https://tdn.totvs.com/pages/viewpage.action?pageId=697263324)** **[2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=697263324)**
