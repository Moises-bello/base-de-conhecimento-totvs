---
article_id: 360035159453
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: c65fb4a43a5131a305935c21ec23f21a704a2ed4fe2bc351ee3b72ecd70a0094
fetched_at: '2026-06-28T22:47:29.545814+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH -  Escolhendo e testando um certificado HTTPS/SSL válido para
  o Meu RH
type: support-article
updated_at: '2026-05-25T19:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453-RH-RM-Meu-RH-Escolhendo-e-testando-um-certificado-HTTPS-SSL-v%C3%A1lido-para-o-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20701313689879) Tempo aproximado para leitura: 00:09:23 min**

**Dúvida**  
Como testar se o meu certificado SSL será válido para o Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.18  
  
**Solução**  
Necessário vincular um Certificado SSL com um emissor terceiro e que seja válido conforme orientações dessa documentação.  
**Não pode ser** um **Certificado auto assinado** ou **criado pela própria empresa** devido a sucessões de validações de segurança feita pela **loja de aplicativos**.

**1. CERTIFICADO**

Certificado SSL é um certificado digital que autentica a identidade de um site e possibilita uma conexão criptografada. O termo "SSL" significa "Secure Sockets Layer" (camada de soquete seguro), um protocolo de segurança que cria um link criptografado entre um servidor Web e um navegador Web.

Empresas e organizações precisam adicionar certificados SSL aos seus sites para proteger as transações on-line e manter a privacidade e a segurança das informações dos clientes

Leia mais sobre o uso de certificados SSL, acesse: [**Uso de certificados SSL**](https://tdn.totvs.com/display/NPR/Certificado+SSL)

**2. VERIFIQUE O SEU CERTIFICADO**

No Meu RH, em ambas plataformas (Android e iOS) utilizamos um browser para renderizar o  aplicativo.

Isso implica na validação dos certificados assim como em qualquer site que você acessa normalmente por um browser comum. Para verificar se um determinado certificado é válido, recomendamos a validação através de portais como

<https://www.ssllabs.com/ssltest/>

<https://www.sslshopper.com/ssl-checker.html>

Por exemplo, o SSLLabs realiza a geração de um grade/score baseado em uma série de critérios como por exemplo inspeção do certificado e protocolos de criptografia, nos casos abaixo o certificado gratuito ficou grade B, pois nível de criptografia suportado é inferior ao disponível no mercado, nesse link podem ser identificado metodologia de validação: <https://github.com/ssllabs/research/wiki/SSL-Server-Rating-Guide>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424749560983)

**3. CERTIFICADOE SE O MEU CERTIFICADO ESTIVER INVÁLIDO?**

A tentativa de utilização de certificados inválidos geram erro no processo de handshake na validação das requisições e geração da chave de sessão entre o cliente requisitante e o servidor, consequentemente todas as suas informações não irão trafegar de modo seguro e criptografado pela rede. No exemplo da imagem abaixo, podemos observar que apesar de ser um certificado valido e configurado no server com sua chave privada, o mesmo não está autorizado a ser utilizado de acordo com o SAN, sendo rejeito pelo browsers no momento de negociação da chave de acesso para a sessão de comunicação. Ou seja, não podemos utilizar esse certificado para ser configurado em um IP externo ou mesmo em qualquer outro subdomínio, sendo assim realize essa verificação e validação para um correto funcionamento do ambiente seguro.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424768075415)

**5. CERTIFICADOS SSL MOBILE**

As plataformas de dispositivos móveis (IOS, Android) possuem limitações com relação aos certificados digitais. Por padrão, apenas os certificados homologados por elas são reconhecidos como confiáveis. Em geral, as maiores certificadoras são reconhecidas em ambos sistemas operacionais, porém  em caso de dúvidas, procure na sua unidade certificadora para assegurar que seu certificado é homologado para ambas plataformas. Para evitar a aquisição de certificados não homologados e outros problemas relacionados a segurança, é importante consultar a documentação técnica de cada plataforma sobre a lista de certificados reconhecidos como confiáveis:

**5.1. IOS**

A lista de certificados confiáveis para o iOS está disponível em: [Certificados confiáveis IOS](https://support.apple.com/pt-br/HT212140). (Esse link é constantemente atualizado. Até a data da escrita dessa documentação a versão é a 14).

Além disso, a Apple também instituiu a chamada Política de Transparência de Certificados da Apple, que define algumas diretivas de certificados que são válidos <https://support.apple.com/en-us/HT205280>.

Para verificar se o seu certificado se enquadra nessa política de transparência, utilize a ferramenta <https://sslmate.com/labs/ct_policy_analyzer/>.

**5.2. Android**

É necessário verificar no aparelho em: **Configurações > Segurança > Credenciais Confiáveis**

Na Aba **Sistema** existe a lista de certificados confiáveis para aquela versão do Android.

Atenção: Cada versão do Android pode ter uma lista de certificados confiáveis diferente.

**6. Problemas com o Certificado**

Alguns sinais são comuns e indicam que o certificado não é válido para utilização em mobile:

* Consegue se logar em apenas uma das plataformas pelo aplicativo (Android ou iOS)
* Carregamento com tempo excessivo na tela pós-login até resultar algum erro genérico na tela
* Ao acessar a URL do portal pelo browser do celular, exibe uma mensagem relacionada a algum problema de segurança:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21918278019095)

**IMPORTANTE :**

Para escolha do certificado o ideal é ter o apoio de um especialista no assunto para escolher a melhor opção.
