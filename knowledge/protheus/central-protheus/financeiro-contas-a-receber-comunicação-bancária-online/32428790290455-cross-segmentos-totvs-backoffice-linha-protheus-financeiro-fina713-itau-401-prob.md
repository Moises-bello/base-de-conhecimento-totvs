---
article_id: 32428790290455
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: ed25e709be04da4201db625fac9035982021dcc16ed113a88a87cd83240f6154
fetched_at: '2026-06-28T22:37:49.268366+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713
  - ITAU - 401 - Problema ao assinar a mensagem com o certificado.
type: support-article
updated_at: '2025-06-12T12:44:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32428790290455-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-FINA713-ITAU-401-Problema-ao-assinar-a-mensagem-com-o-certificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32428762509719) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo **Financeiro**, ao realizar a configuração de contas **ITAU 341 para emissão de cobrancas online via API - FINA713**, ocorre a mensagem de erro: **401 - Erro comunicação / Problema ao assinar a mensagem com o certificado. Verifique se o ceriticado utilizado é válido.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32428762510487)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210

**POSSIVEIS CAUSAS DO ERRO**

**1 - Chaves de comunicação com o banco, estão invalidas ou expiraram**

As chaves **client\_id** e **client\_secret**, no banco do Itau, possuem geralmente um **periodo de 07 dias** de renovação do **TOKEN**, a sugestão é avaliar junto ao **Gerente da Conta** no banco se as chaves geradas são validas para a emissão de cobrancas **(API V2)** -> **{{ cash\_management/v2/boletos }}**  
  
**2 - Certificados utilizados podem estar vencidos**Para avaliar se um certificado encontra-se vencido, deve clicar duas vezes sobre o certificado e avaliar a validade do mesmo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32428762520087)

**3 -** **Certificados não estão na versão 2 cash\_management/v2/boletos**

Novas configurações de contas serão realizadas apenas para a **nova versão 2 (V2),** com certificado.  
Consulte a documentação do itau: **[https://devportal.itau.com.br/](https://devportal.itau.com.br/nossas-apis/itau-ep9-gtw-cash-management-ext-v2)  
  
4 - Certificados gerados com senha de acesso**

O protheus não utiliza senhas de certicados e sim um token de acesso, **avalie o passo a passo abaixo com a orientação para utilização de certificado sem senha**

Durante o processo de criação do certificado digital com o **Itaú**, serão gerados dois arquivos: um com extensão **.crt** e outro com extensão **.key.** Esses arquivos são utilizados na configuração e integração com o Novo Gestor Financeiro.

**Importante**:  
O sistema não suporta certificados cujo arquivo .key esteja protegido por senha. Caso o arquivo tenha sido gerado com senha, será necessário removê-la antes da utilização.

**Como remover a senha do arquivo .key:**  
Você pode utilizar o comando abaixo com o **OpenSSL** para gerar uma nova chave sem senha:

|  |
| --- |
| ***openssl rsa -in sua\_chave.key -out chave\_sem\_senha.key*** |

**Passo a passo:**

1. Ao executar o comando, será solicitada a senha da chave original **(sua\_chave.key).**
2. Digite a senha e pressione **Enter**.
3. Um novo arquivo chamado **chave\_sem\_senha.key** será gerado, agora sem proteção por senha.

Esse novo arquivo poderá ser utilizado normalmente no processo de configuração do sistema.  
  
**5 - Arquivos de certificados não estão na pasta correta dentro da Protheus\_data**  
  
**-- Caso o ambiente seja local**  
Acesse a pasta referencia no **Appserver.ini ( RootPath )**, geralmente denomeada como **"Protheus\_data",** crie a pasta **cert**, acesse a pasta e crie a pasta **ngf,**cole os arquivos de certificados nessa pasta.  
  
**Referencia,**  
**Obs**: Todos arquivos de certificados que serão usados para **API FINA713 / FINA717** devem estar nessa pasta.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32428790262935)

**Posteriormente, deve verificar se o arquivo está na Validação de Credenciais com o mesmo nome via Novo Gestor Financeiro FINA710  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32428790264599)  
-- Caso o ambiente seja CLOUD**Acesse o **FTP do ambiente** que está configurando e efetue o mesmo passo acima  
-- Deve avaliar se a pasta criada possui as devidas permissões de acesso, atraves do botão direito propriedades ou no momento da criação da pasta

Exemplo: Pasta **cert**, o mesmo processo deve segui para a pasta **ngf**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32428762522903)  
  
**Saiba mais:**  
**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-foi-poss%C3%ADvel-gerar-os-arquivos-corretamente-Erro-ao-extrair-o-Certificado-de-Autoriza%C3%A7%C3%A3o-no-CFGX060-Wizard-de-Convers%C3%A3o-de-Certificado)**  
**[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)**  
**[Itaú - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=675571899)**
