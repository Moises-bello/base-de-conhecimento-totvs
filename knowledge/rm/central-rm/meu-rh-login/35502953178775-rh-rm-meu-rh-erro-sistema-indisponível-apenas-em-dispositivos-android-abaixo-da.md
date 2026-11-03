---
article_id: 35502953178775
category: Meu RH - Login
content_hash: 6ed15abac0f0d8ca14cf797e72109164df884d19b018b543ecbcffc2ea6108f9
fetched_at: '2026-06-28T22:47:27.233890+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro Sistema indisponível apenas em dispositivos Android
  abaixo da versão 14
type: support-article
updated_at: '2026-06-23T18:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35502953178775-RH-RM-Meu-RH-Erro-Sistema-indispon%C3%ADvel-apenas-em-dispositivos-Android-abaixo-da-vers%C3%A3o-14
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35502953130007) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar acessar o APP Meu RH apenas em dispositivos Android abaixo da versão 14 é apresentada a mensagem: **Sistema indisponível no momento**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35502972813463)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Quando o problema ocorre apenas em dispositivos Android inferiores à versão 14, a causa está no servidor onde o **Meu RH** foi instalado. Nesse caso, o servidor está enviando a cadeia de certificados em ordem incorreta. Essas versões mais antigas do Android não conseguem corrigir automaticamente uma cadeia de certificados malformada enviada pelo servidor, o que resulta na falha de conexão.  
  
**Solução**  
É necessário acessar o servidor onde o Meu RH e o IIS estão instalados e verificar a configuração do Certificado.  
  
Para garantir **compatibilidade total com as versões do Android**, é necessário:  
  
1- Corrigir a configuração do servidor para que envie apenas:  
  
1.1. O certificado do domínio.  
  
1.2. O(s) certificado(s) intermediário(s).  
  
2- Remover o certificado raiz (**root CA**) da cadeia enviada.  
  
3- Garantir que os certificados estejam na ordem correta.

**Caso o incidente persista, recomenda-se:**

* Revisar a configuração do certificado SSL/TLS no servidor **(IIS, proxy reverso ou balanceador)**, assegurando que toda a cadeia de certificação esteja devidamente configurada, conforme as orientações da autoridade certificadora.
* Confirmar junto à CA emissora se há certificados intermediários que devem ser incluídos no pacote de instalação.
* Realizar a configuração de cifras seguras para comunicação TLS.

**Documentação completa e orientações mais detalhadas:**  
[Incompatibilidade de Certificado SSL em Androids abaixo da versão 14](https://tdn.totvs.com/pages/viewpage.action?pageId=961003106)  
  
**Observação:**  
O ajuste da configuração de certificados é um procedimento técnico e relacionado à infraestrutura, portanto **excede o escopo do Suporte Padrão**.

Caso necessite de apoio especializado de infra, recomendamos o acionamento do serviço de **TIS da Totvs**, que possui a expertise necessária para esse tipo de intervenção.  
**Contato da TIS:**  
📧 [*tis.atendimento@totvs.com.br*](mailto:tis.atendimento@totvs.com.br)  
*A TIS é composta por uma equipe de consultoria especializada em infraestrutura.*  
  
**Importante:** Caso o erro de Sistema Indisponível esteja ocorrendo para "todos", deverá conferir a documentação abaixo:  
[RH - RM - Meu RH - Erro ao logar no APP Meu RH, Sistema indisponível no momento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Sistema-indispon%C3%ADvel-no-momento)
