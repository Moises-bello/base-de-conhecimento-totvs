---
article_id: 10811119314199
category: Financeiro
content_hash: 991a5770ba164e772dfd6d3b42f9fd0090ab182460ca4ca196abe2e283683613
fetched_at: '2026-06-28T22:38:01.068024+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como Exportar e Aumentar
  o tamanho do arquivo .PFX ( Certificado Digital  - modelo A1 )
type: support-article
updated_at: '2023-08-14T20:46:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10811119314199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-Exportar-e-Aumentar-o-tamanho-do-arquivo-PFX-Certificado-Digital-modelo-A1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:09:00 min  
  
Dúvida**Como Exportar e Aumentar o tamanho do arquivo .PFX (Certificado Digital - modelo A1)?  
  
**Ambiente**

Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA710 - Todas as versões

**Solução**

Quando ocorre erro no Configurador **CFGX060 - Wizard de Conversão de Certificado**, com uma mensagem de entidades certificadoras ausentes, inválidas ou erro de tamanho do arquivo .PFX

Isso ocorre pelo motivo do tamanho do certificado digital estar com aproximadamente 3KB, diferente do tamanho inicial de 7KB permitido pelo Protheus, conforme exemplo abaixo:

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10783416657687)  
  
Você deve exportar novamente o certificado no seu navegador. Segue um exemplo:  
  
**Requisitos**

* ​​É recomendado pelas certificadoras emissoras do Certificado o uso do Internet Explorer na exportação do arquivo .PFX . Para passo a passo detalhado em outros navegadores ou sistemas operacionais, consulte a certificadora emissora do arquivo antes de qualquer ação.
* Possuir certificado digital e-CNPJ modelo A1 válido instalado com permissão para exportação de chave privada. Confira o processo abaixo referente a exportação da chave privada.

Para o processo de exportação é necessário que o arquivo .PFX esteja instalado no computador. (Caso tenha alguma duvida sobre a instalação ou a emissão do Certificado é recomendado que entre em contato com a Certificadora Emissora do arquivo)

**Instale****o Certificado A1**  
Selecione o local que você deseja instalar o certificado:  
  
.  
Insira a senha e marque as **3 opções de importação** abaixo. Apenas marcando essas opções será possível fazer a exportação do certificado com a chave privada.

![AZ4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10783578809111)  
  
Finalize a instalação do certificado e siga o tutorial de exportação, nos exemplos abaixo:  
  
**Exportando o certificado com chave privada.**  
1. Abra o navegador Internet Explorer e clique no ícone **F****erramentas (****engrenagem****)** e Selecione **Opções da internet.**

![za1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10782770274583)

2. Selecione a aba **C****onteúdo - > Certificados.**

![az2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10782869588247)

3. Escolha o certificado digital da sua empresa e clique em **Exportar.**

![exp1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10783942387863)  
  
4. Marca a opção **Sim, exportar a chave privada**.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10487832503319)

5. Marque as opções:

* **Incluir todos os certificados no caminho de certificação, se possível**,
* **Exportar todas as propriedades estendidas**
* **Habilitar privacidade de certificados**.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10783125116439)

6. Crie uma nova **senha** para o certificado e **anote**. Essa senha será adicionada na plataforma do Protheus,  será utilizado essa nova senha para o upload do seu certificado no sistema  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10487858623895)

7. Escolha o diretório e salve o arquivo.  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10783226759959)

8. Clique em **C****oncluir** para finalizar o processo de exportação do Certificado .PFX  
![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10783268396055)

**Importação do Certificado para o Protheus:**

Após realizar a exportação do arquivo .PFX com o tamanho permitido pelo Protheus, localize o diretório que foi salvo a cópia do arquivo e acesse o **Modulo Configurador> Cadastro> Wizard de Conversão de Certificado.**

Siga as orientações abaixo:

O arquivo .PFX deve estar dentro da pasta system do ambiente Protheus, ao validar o caminho deve inserir a senha de criação da copia para continuar. Clicar no botão "**Avançar**"

![unnamed__2_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10629975413655)

Nesse momento o Assistente Conversor irá converter o arquivo .PFX em arquivo extensão .PEM

Clique no botão "**Avançar**" para continuar

![unnamed__3_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10630012184343)

Ao finalizar o Assistente conversor irá **Concluir** o processo de conversão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10810877438231)

**IMPORTANTE:**

Os Caminhos acima no processo de conversão devem conter letras **"M****inúsculas"**, conforme exemplo demonstrado.

**Saiba Mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como testar o Certificado Digital Modelo A1, antes de Importar ao Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10755484313751)
