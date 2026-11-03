---
article_id: 20672026455319
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: f55d33087f1b328e85f4dea0ebd9fe881f9560f442b741e3a5bfdbba581494d8
fetched_at: '2026-06-28T22:47:29.478404+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como configurar certificado SSL no portal Meu RH
type: support-article
updated_at: '2025-09-11T18:26:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20672026455319-RH-RM-Meu-RH-Como-configurar-certificado-SSL-no-portal-Meu-RH
---

**Dúvida**Como configurar certificado SSL no portal Meu RH?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões

**Importante**Não prestamos suporte à este tipo de configuração por envolver configurações relacionadas à infra da organização, o documento serve apenas como guia. Para tanto, é necessário o auxílio de um Web Master.

**Solução**Para configurar o SSL no FrameHTML siga os passos abaixo:

1. Acesse o **servidor** onde o **Portal RM** está instalado;
2. Abra o **IIS**;
3. Em sites selecione o **DefaultWebSite**;
4. Em **Associações** adicione uma ligação com Tipo **HTTPS**;
5. Selecione o **Certificado** a ser utilizado;  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/20700838506391)  
     
   Para testes internos utilizamos a Porta **http** para 80 e a **https** para 443;  
     
   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699460258071)**
6. **Salve** as configurações;
7. Clique em **OK**;
8. Reinicie o **IIS**:  
   1. Selecione o diretório do **IIS**;
   2. Clique em **Reiniciar**;  
        
      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/20672020588567)

**Realizando o teste de validação:**

1. Para testes, no **IIS** selecione o diretório **FrameHTML/Web/App/RH/PortalMeuRH**;
2. Clique em **Procurar \*:"Porta"(Https)**;  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699535645207)
3. Será apresentada a tela de login do Portal Meu RH:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699514233239)  
     
   Portal Meu RH após o acesso:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699460264983)  
   Nos Prints acima o Site é apontado como **Não Seguro**, isso acontece pois utilizamos um certificado Auto Assinado, criado no IIS.

**Importante**

* Após realizadas as configurações acima, gere o QR Code novamente para acesso ao APP via Smartphone, como por exemplo, o APP Meu RH. Para mais detalhes, acesse o link abaixo:  
  [RM - FOP - Meu RH: O que é e como gerar o QR Code de acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024702953-RM-FOP-Meu-RH-O-que-%C3%A9-e-como-gerar-o-QR-Code-de-acesso-?source=search)

Pode retornar o erro **Ops! Algo deu errado!** devido a configuração do Meu RH no IIS com o uso do Protocolo HTTPS e certificado SSL que é auto-assinado. Atualmente, devido a sucessões de validações feita pela loja de aplicativos onde é realizado o download do MEU RH, o certificado auto-assinado não é válido e confiável. Para a correção e funcionamento total do APP utilizando o protocolo HTTPS/SSL, será necessário que adquira um certificado válido e aplique-o, **faça a validação de seu certificado em:** [RH - RM - Meu RH - Testando se o certificado HTTPS/SSL é válido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453)
