---
content_hash: 0b68e811f9c8fc4e115d1714e32c76e6a324bfd732fe05524cd45219da11a0c8
fetched_at: '2026-06-28T21:35:24.463420+00:00'
page_id: '270087659'
product: fluig
source: tdn-fluig
title: Segurança da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270087659
version: 49
---

4true.\*ndicenone

Dica!

[Acesse aqui](https://tdn.totvs.com/x/yUZrJ) e veja nossas recomendações sobre as **Boas práticas de segurança para o seu ambiente** no TOTVS Fluig Plataforma.

# Objetivo

---

Esse guia tem o objetivo de declarar os controles de segurança realizados dentro do TOTVS Fluig Plataforma e sua execução em ambiente internos (on-premise) ou *cloud*.

## Segurança nos padrões internacionais

---

O TOTVS Fluig passa por testes de segurança seguindo as principais metodologias internacionais. Ele faz parte do programa de Bug Bounty da TOTVS, que tem como principal objetivo identificar e corrigir potenciais vulnerabilidades em seu ambiente tecnológico de produtos, aderindo e seguindo as melhores práticas recomendadas pelo OWASP (Open Web Application Security Project), uma comunidade mundial dedicada a melhorar a segurança de software. Ao alinhar nossos processos com as diretrizes do OWASP, buscamos garantir a identificação e correção eficazes de potenciais vulnerabilidades em nossa plataforma, contribuindo para um ambiente digital mais seguro e resiliente.

Possuímos certificados e atestados de reconhecimento que demonstram nosso compromisso em seguir as práticas do mercado para processos de desenvolvimento seguro. Esses documentos evidenciam que nossas metodologias e procedimentos estão alinhados com os mais altos padrões de segurança, validados por auditorias internas e externas.

Os certificados e atestados, como os exemplificados abaixo, podem ser solicitados a qualquer momento por meio dos nossos canais de atendimento:

* ;

* *Letter of attestation* - *Bounty program*.

# Criptografia

---

|  |  |
| --- | --- |
| Tráfego de dados | Toda a comunicação da plataforma TOTVS Fluig e os clientes é feito por HTTPS/TLS, o protocolo mais utilizado e confiável no mercado. [Saiba mais sobre configuração HTTPS](http://tdn.totvs.com/x/k_UTEQ)  É de responsabilidade do cliente fornecer um certificado válido para utilização do servidor Fluig, exemplo: fluig.empresa.com.br.  Caso o cliente não tenha um certificado, sugerimos a utilização do seguinte endereço:  Também é recomendável a configuração de uma  para a plataforma. |
| Senhas | Os dados sensíveis de usuário são gravados de forma que não podem ser descobertos o conteúdo original. É utilizado o algoritmo PBKDF2WithHmacSHA1, para gravação das senhas dos usuários no TOTVS Identity. |
| Autenticação | O processo de Single Sign On (SSO) é feito através do protocolo SAML, com um certificado gerado internamente, onde não é feita a troca de informações de senha. |

# Disponibilidade e continuidade

---

|  |  |
| --- | --- |
| Serviços TOTVS Identity  na Nuvem | Disponibilidade mínima do ambiente do Identity é de 99,5% por mês sobre o **ambiente de produção**. Todo o acompanhamento e notificações sobre mudanças de estado do serviço são disponibilizadas em: [http://status.fluigidentity.com](http://status.fluigidentity.com/). O ambiente de homologação (customerfi) não tem SLA de disponibilidade e página de status. |
| Serviço Analytics  na Nuvem | Disponibilidade mínima do ambiente do Fluig Analytics é de 99,5% por mês sobre o **ambiente de produção**. |
| Serviço CLOUD | As políticas de disponibilidade e continuidade dependem de proposta comercial, onde nossos planos iniciam com disponibilidade de 97,5% por mês.  Confirme na proposta os valores específicos de uso e de disponibilidade. |
| Alta disponibilidade  On premises | É de responsabilidade do cliente on-premises criar um ambiente que atenda a necessidade de disponibilidade e desempenho que o negócio necessitará.  Possuímos recomendações sobre como um cliente deve configurar seu ambiente para garantir uma maior disponibilidade.  .  Caso o cliente necessite de um apoio na administração de seu ambiente, possuímos pacotes de serviços para melhor atendê-lo. |

# Ambiente físico

---

Dependendo do uso e contrato, o cliente pode estar no datacenter NIMBVS da TOTVS ou no datacenter Amazon. Cada um possui características diferentes.

|  |  |
| --- | --- |
| Ambiente NIMBVS | **Certificações**   * ISAE 3402 Tipo II * ISO 9001:2008 * Datacenter TIER III * Gestão de vulnerabilidades executada por consultoria especializada * Monitoramento e bloqueio contra ataques DDOS 24x7 * SIEM * Firewall Next Generation * Política de backup conforme proposta comercial * Política de entrega de dados em caso de interrupção irrecuperável no datacenter TOTVS conforme proposta comercial * Garantia de integridade dos dados conforme contrato   **Localidade**  Data centers estão localizados em São Paulo, Brasil |
| Ambiente Amazon | Para serviços Fluig Viewer e para clientes alocados na nuvem Amazon, as seguintes certificações estão incluídas:   * ISO 27001 * SOC 1 e SOC 2/SSAE 16/ISAE 3402 (antes SAS 70 Type II) * PCI Level 1 * FISMA Moderate * Sarbanes-Oxley (SOX)   [Mais detalhes sobre as certificações em ambiente Amazon](https://aws.amazon.com/pt/compliance/)  **Localidade**  Data centers alocados são da Zona São Paulo, Brasil |

# Ambiente de serviços complementares

---

Para o funcionamento da plataforma, no conceito de [fog computing](https://pt.wikipedia.org/wiki/Fog_computing), alguns serviços rodam em serviços na nuvem. Para transparência para nossos clientes, segue serviços e localidades.

|  |  |
| --- | --- |
| Ambiente Identity (Produção) | **Localidade**  Data centers estão localizados na Zona São Paulo, Brasil, em serviços da Amazon AWS |
| Ambiente Analytics | Para mais informações sobre a arquitetura e segurança referente aos serviços do Analytics, consulte o [guia de segurança](https://www.gooddata.com/sites/default/files/GoodData_Security_Overview.pdf).  **Localidade**  Data centers alocados nos Estados Unidos, em serviços da Rackspace |
| Ambiente Fluig Viewer | **Localidade**  Data centers estão localizados na Zona São Paulo, Brasil, em serviços da Amazon AWS |

# Integração com sistemas externos

---

A plataforma pode ser integrada com diversos sistemas em diferentes cenários. Como segurança recomendamos verificar todas essas integrações.

|  |  |
| --- | --- |
| Sistemas legados | Com a plataforma TOTVS Fluig uma das características que é muito utilizada nos projetos criados é a integração com sistemas que a empresa já tem, seja para consulta seja para efetivação.  **Tipos de integração suportados:**   * SOAP (HTTP e HTTPS) * REST (HTTP e HTTPS) * JDBC (criptografia depende do fornecedor do Banco de Dados)   **Autenticações suportadas em REST:**   * Basic * OAuth 1 * OAuth 2 * Custom (escrito em JavaScript) * Nenhuma |
| Serviços para desenvolvimento | A plataforma disponibiliza diversos serviços que possibilitam o desenvolvimento de personalizações e integrações. Por isso recomendamos revisar a segurança de acesso às APIs, Datasets e Webservices. Acesse o  para mais informações. |
| Componentes obrigatórios | **On-Premise - License Server**  Para verificar o contrato do cliente, será necessário instalar o License Server. Ele se conecta a nuvem para verificar o contrato do cliente ao qual ele tem acesso. .  **On-Premise - Banco de Dados**  Conforme , a plataforma requer a utilização de um banco de dados. Para obter mais detalhes sobre características de segurança desse componente verifique a documentação do seu fornecedor. |
| Componentes opcionais | **Microsoft Active Directory**  Para autenticação de usuários é possível utilizar o Microsoft Active Directory. Tanto a plataforma como o Identity possuem conexões, sendo que para o [Identity](https://tdn.totvs.com/display/fluig/TOTVS+IDENTITY) possuímos o  que é utilizado para aumentar a segurança nessa comunicação.  **SSO Identity - Single Sign On**  Por meio do [Identity](https://tdn.totvs.com/display/fluig/TOTVS+IDENTITY) é possível criar ambientes de acesso a diversos sistemas usando protocolos abertos de SSO, como  [SAML](https://tdn.totvs.com/display/fluig/Identity+%7C+Single+Sign+On+via+SAML) e [OIDC](https://tdn.totvs.com/pages/viewpage.action?pageId=842293735) (OpenID), incluindo integração com Microsoft Entra ID.  **MFA - Autenticação Multifator**  Permite um nível extra de segurança na autenticação, exigindo além do usuário e senha, de um número de 6 dígitos gerado usando o protocolo TOTP, gerando um segundo fator de autenticação (2FA) Serviço exclusivo por meio do [Identity](https://tdn.totvs.com/display/fluig/TOTVS+IDENTITY).  **SMTP - Envio de e-mail**  Para realizar o envio de e-mail de notificações, utilizamos o protocolo SMTP tanto com SSL como TLS. .  **Notificações PUSH**  Para notificar os usuários de aplicativos móvel é utilizado tanto a infra-estrutura do Google® como da Apple®, em que pequenas mensagens sem dados críticos de negócio são repassadas usando o parceiro de tecnologia UrbanAirship que centraliza todas as mensagens enviadas para clientes TOTVS Fluig. |

# Ambiente mobile

---

A plataforma pode ser acessada via dispositivos móveis com o Fluig Mobile, disponível para [Android](https://play.google.com/store/apps/details?id=br.com.fluig) e [iPhone/iPad](https://itunes.apple.com/br/app/fluig/id682057015).

|  |  |
| --- | --- |
| Trafego de dados | A comunicação entre o Fluig Mobile e o servidor do Fluig é feita através de conexão de rede, onde todo o tráfego de informações ocorre via HTTP.  Para acesso via rede de dados celular (3G/4G) é necessário que o endereço do Fluig esteja publicado na internet. Para uma maior segurança, é possível habilitar HTTPS, [respeitando os certificados válidos para dispositivos móveis](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Certificadodigitalmobile).  Caso não esteja publicado na internet, é necessário que o dispositivo móvel onde o Fluig Mobile está instalado esteja conectado à uma rede onde seja possível acessar o servidor do Fluig.  Ex.: Wi-Fi interna da empresa, conexão VPN, etc. |
| Autenticação | É realizada utilizando [oAuth](https://oauth.net/), um protocolo seguro de autorização que não armazena o usuário e senha no momento do login, apenas a chave de autenticação (*token*). |

# Segurança da rede e aplicação

---

|  |  |
| --- | --- |
| Recomendação seguida | Para boa parte das ações de segurança, são levadas em consideração as recomendações da OWASP |
| Teste de vulnerabilidades | Empresas terceiras realizam *Pentests* de forma regular e de forma independente.  Descobertas de vulnerabilidades são avaliadas conforme impacto e probabilidade da falha, nisso são criadas tarefas de correção para o time responsável.  Para garantir o processo, clientes são orientados a abrir um ticket relatando a situação mapeada no Pentest, juntamente com o impacto.  Cada ticket aberto será avaliado pelo time de segurança TOTVS, caso a vulnerabilidade seja confirmada, o ticket entrará em processo de manutenção padrão.  Cada situação deve ter um ticket e deve ser evitado criar um ticket com todas as situações.  É importante que os testes sejam realizados em um ambiente atualizado com a versão mais recente do Fluig, disponível para download no Portal de Clientes. |
| Incidentes de segurança | No evento de um vazamento de informações ou de uma descoberta de uma vulnerabilidade, nossos profissionais técnicos são alocados.  Para garantir o processo, clientes são orientados a abrir um *ticket* relatando a situação. |
