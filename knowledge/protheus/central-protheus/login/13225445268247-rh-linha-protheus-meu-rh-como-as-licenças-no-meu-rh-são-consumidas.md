---
article_id: 13225445268247
category: LOGIN
content_hash: aefc88e484ff757c8fe0863ad70006459d81a95dd651957fe04fe83b997dc9e8
fetched_at: '2026-06-28T22:44:40.520120+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como as licenças no Meu RH são consumidas
type: support-article
updated_at: '2026-03-04T14:11:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13225445268247-RH-Linha-Protheus-Meu-RH-Como-as-licen%C3%A7as-no-Meu-RH-s%C3%A3o-consumidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21895194696599) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
RH - Linha Protheus - Meu RH - Como as licenças no Meu RH são consumidas  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Para utilização do App Meu RH é necessário adquirir licenças dos tipos **4000 -** **TOTVS FULL, 4177 - Portal RH** ***ON DEMAND ou*** **4001 - TOTVS I,** conforme consulta abaixo:  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38796137228311)**  
  
Caso ainda não possua esse tipo de licença, **entre em contato com o seu ESN (Executivo de Soluções de Negócio) para aquisição e maiores informações.**  
  
Abaixo, segue uma documentação que **exemplifica** o **uso** destas **licenças** e **como deve ser parametrizado** para o serviço do **Meu RH** possa utilizá-las corretamente:  
[**Consumo de Licenças e Configuração Apropriada**](https://tdn.totvs.com/pages/viewpage.action?pageId=654098131)  
  
Em relação a **quantidade de licenças**, seu **Gerente de Contas** pode ser acionado, pois deve ser avaliada a infraestrutura, picos de acessos, entre outros detalhes intrínsecos de cada ambiente. Este levantamento deve ser feito por um arquiteto de soluções, que deve direcionar essa demanda junto ao Gerente da conta para verificar a **quantidade de licenças necessárias para atender a Empresa.**  
  
No que cabe ao **consumo das licenças**, vale lembrar que a arquitetura do **Meu RH** usa o serviço ***API/REST***. Este serviço desde que configurado conforme informado acima, não requer nenhuma licença para ser disponibilizado, pois o consumo da licença ocorre **durante** o **período em que a** ***API*** está **processando a resposta** para a **requisição**.  
  
**Uma página do Meu RH utiliza em média de 3 a 4 requisições/threads** simultaneamente, sendo possível em tempo real, acompanhar o Monitor do LS, **01 única licença atenderá somente 01 requisição,**mas com a comunicação REST, e o uso de *token* para validar as API's, o processo de ***login*** realmente, utilizará **entre 3 a 4 requisições API's diferentes e "ao mesmo tempo"** para:  
- criação do *token;*  
- validação do *login*;  
- carregar a página inicial;  
- funcionalidades que o usuário tem acesso.  
  
Porém, os processos não precisarão ser executados todos ao mesmo tempo, entrará em uma espécie de fila de processamento, sendo que, enquanto houverem licenças disponíveis, as requisições consomem uma nova *thread* e por consequência uma nova licença, e executa o processamento.  
  
Exemplo, caso um cliente adquira 100 licenças TOTVS I e somente um funcionário acesse o Meu RH, como o processo do *login* são 4 operações distintas (execução de 4 *API's*), para agilizar o processo de *login*, **o sistema pode utilizar até 4 licenças, momentaneamente**, para fazer as 4 requisições de uma só vez.  
  
Importante ressaltar que, **neste momento do** ***login*** **somente,** mais licenças são consumidas, porém estas são liberadas logo após o consumo/*login*.  
  
Nesse momento, entrará no processo, o uso de *token* e das chaves *EnableKeepAlive* e *Stateless*.  
Ambas as chaves indicam que após a requisição *REST* responder com o resultado da API, a *thread* em questão é finalizada e, consequentemente, **liberada o uso do consumo de licença.**  
  
O *token* por sua vez, serve para **não seja necessário realizar uma validação de** ***login*** **a toda requisição e/ou que o usuário logado "prendesse" a licença.**   
Quando um novo botão é apertado em tela, uma nova requisição *API* é disparada ao *REST*, e o *token* é enviado no corpo da comunicação para validar se o *REST* pode responder àquela requisição ou não.  
  
Em um cenário onde o cliente adquira somente 1 licença TOTVS I, e habilite o ***EnableKeepAlive***e o ***Stateless***, o processo de *login* ainda vai consumir 4 *API's* da mesma forma, mas como somente possui uma licença disponível, o processo entrará em fila, e necessariamente precisará que **uma única** ***API*** **seja executada por vez**, e a cada retorno de uma, a próxima é executada, e assim sucessivamente, até que as 4 retornem e com isso o *login* é efetuado normalmente.  
  
Quando nenhuma requisição está em processamento, ou seja, o funcionário está logado, mas não está navegando, mesmo que ainda não tenha dado o *timeout*, nenhuma licença será consumida.  
  
Esta é a regra sobre o consumo das licenças para o Meu RH, tendo somente o adendo que a TOTVS I é a licença que consegue responder requisições *REST*, por isso que ela é utilizada e vendida para o Meu RH, pois o App funciona totalmente através de *API's/REST.*  
  
Devido à **estrutura do serviço REST**, que atende à requisições apenas, **o usuário logado no Meu RH não consome nenhuma requisição/thread**, enquanto não realiza nenhuma ação no aplicativo (clicar sobre algum item do Menu ou em tela). Além disso, dependendo de quantos usuários estiverem logados, será necessário mais licenças disponíveis.  
  
Por fim, em um cenário onde as licenças não estão sendo entregues, oriento consultar o artigo que demonstra como consultar as licenças via **Portal do Cliente**, para acessar o artigo [clique aqui.](https://totvscst.zendesk.com/hc/pt-br/articles/360000989247-CST-GSEN-Como-verificar-a-Quantidade-de-Licen%C3%A7as)  
  
Caso a empresa possua mais de uma instalação e as licenças não estejam devidamente distribuídas entre suas instalações, o artigo de **como distribuir licenças**, irá auxiliá-lo nessa demanda. Este artigo está disponível, [clicando aqui.](https://totvscst.zendesk.com/hc/pt-br/articles/360000829348-CST-GSEN-Como-Distribuir-Licen%C3%A7as)  
  
Após verificar a quantidade de licenças e confirmar se está correta, atualize manualmente o seu ***License Server Virtual (LSV)***, conforme indica a documentação no TDN a seguir:  
<https://tdn.totvs.com/display/public/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Atualizacao-Manual> 

**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
