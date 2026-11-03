---
article_id: 33692777820439
category: SIGAACD - Automação e Coleta de Dados
content_hash: 1d51cb09ad163d8f85cc8895a25c8962be96248c4144d1c1996643ce082514d4
fetched_at: '2026-06-28T22:39:12.660799+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configuração para
  comunicação do meu coletor de dados com IP interno/externo?
type: support-article
updated_at: '2025-07-24T17:30:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33692777820439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-para-comunica%C3%A7%C3%A3o-do-meu-coletor-de-dados-com-IP-interno-externo
---

O artigo fornece orientações sobre como configurar a comunicação REST do Meu Coletor de Dados via IP interno no ambiente TOTVS Backoffice (Linha Protheus) para Estoque/Custos. Destaca a necessidade de configurar um IP estático dentro da rede local e assegurar que não haja conflitos com outros dispositivos. Além disso, enfatiza a importância de definir corretamente o gateway padrão e servidores DNS para garantir a comunicação eficiente. As políticas de segurança da informação devem ser consideradas, e as configurações devem ser realizadas pela equipe de infraestrutura da empresa. Caso necessário, suporte adicional pode ser solicitado através de um ticket. Links para documentação complementar são fornecidos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33692777807383) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar REST para comunicação do Meu Coletor de Dados, via IP interno/externo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**  
A utilização de um endereço IP interno para apontamento de serviços exige a realização de configurações específicas na infraestrutura de rede local da sua empresa. Esse tipo de ajuste deve ser conduzido pela equipe de infraestrutura responsável, visto que as políticas e práticas de rede podem variar conforme os critérios técnicos e de segurança adotados por cada organização.

### **1. Configuração de Endereço IP Estático**

Acessar as configurações de rede do ambiente onde o serviço será utilizado.  
Definir manualmente um endereço IP estático que esteja dentro da faixa de IPs da rede local  
(exemplo: `192.168.x.x`), abaixo "**EXEMPLO**" no Windows da configuração de IPs:  
![ipq.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33692732398743)

**Garantir que esse IP não entre em conflito** com outro equipamento da rede e esteja devidamente reservado, conforme as boas práticas da administração de redes.

### **2. Parâmetros de Comunicação**

Além do IP estático, é essencial configurar corretamente:

**Gateway padrão (default gateway):** responsável por rotear o tráfego fora da sub-rede local.  
**Servidor(es) DNS:** fundamentais para a resolução de nomes e a comunicação com serviços internos ou externos, conforme aplicável.

Essas definições asseguram que o dispositivo se comunique adequadamente com demais equipamentos da rede e, se necessário, com a internet.

### **3. Considerações sobre Segurança e Responsabilidade**

A configuração de IPs internos ou externos deve sempre levar em consideração as **políticas de segurança da informação** vigentes na empresa, incluindo:

* Segmentação de rede;
* Regras de firewall;
* Diretrizes de acesso e exposição de serviços.

**ATENÇÃO:** Dessa forma, **essas configurações devem ser avaliadas e implementadas exclusivamente pela equipe de infraestrutura da sua organização**, conforme suas práticas internas e alinhadas às exigências de segurança.

### **4. Encaminhamentos**

É extremamente importante que a equipe de infraestrutura da empresa avalie todos os pontos relacionados à comunicação de rede de forma criteriosa, garantindo a correta configuração dos parâmetros envolvidos, especialmente os relacionados ao uso de DNS e às permissões de tráfego definidas por regras de firewall.

Qualquer configuração incorreta ou ausência de regras adequadas pode resultar em falhas de conectividade, dificultando ou impossibilitando o funcionamento esperado da aplicação. **Em determinados cenários, pode ocorrer de o endereço IP interno funcionar corretamente, mas o IP externo apresentar falhas ou o inverso**, sendo essas situações geralmente relacionadas a restrições na camada de rede ou na resolução de nomes. Por isso, uma validação completa da infraestrutura é essencial para assegurar a estabilidade da comunicação, independentemente do tipo de IP utilizado.

Caso necessite de apoio complementar ou tenha dúvidas sobre os pontos abordados, solicitamos que seja aberto um ticket para o suporte, visando a sua necessidade, dessa forma podemos direcionar a solicitação para áreas internas com escopo específico fora do atendimento padrão, como o time de **HUB Plataformas** ou **TIS Comercial**, que poderão auxiliar conforme aplicabilidade.

**Documentação auxiliar do REST:**  
[Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/x/fEn6Hg)

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
