---
article_id: 360046391933
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2760554b45a5d49d71b9a9b01f8f74d372882ec7c31c708a4f1071651cc760b9
fetched_at: '2026-06-28T22:39:56.351115+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Certificado
  Não Registrado
type: support-article
updated_at: '2023-10-13T11:35:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046391933-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Certificado-N%C3%A3o-Registrado
---

**Dúvida**Ao importar o certificado digital no wizard. config da rotina FISA022 ocorre "Certificado Não Registrado", como solucionar?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064593634)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**'Certificado Não Registrado' pode ocorrer **quando a senha está inválida ou quando o tamanho do arquivo pfx é inferior a 7 KB.**  
Para aumentar o tamanho do pfx, exporte novamente o certificado do seu navegador.  
No caso poderá clicar duas vezes no arquivo e selecionar para abrir com o navegador.  
Segue um exemplo:  
  
**Instalando o certificado**  
**1.** Selecione o local que você deseja instalar o certificado:  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000773919/image-0.png)  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000773899/image-1.png)

**2.** Insira a senha e marque as **3 opções de importação** abaixo.   
Apenas marcando essas opções será possível fazer a exportação do certificado com a chave privada.  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000777300/image-2.png)  
  
Finalize a instalação do certificado e siga o tutorial de exportação.  
  
**Exportando o certificado com chave privada**  
**1.** Abra o navegador Internet Explorer e clique no ícone **ferramentas**.  
**2.** Selecione **opções da internet.**  
  
**3.** Selecione a aba **conteúdo.**  
**4.** Clique em **certificados**.  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779800/image-4.png)

**5.** Escolha o certificado digital da sua empresa.  
**6.** Clique em **exportar**.  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779820/image-5.png)

**7.** Marque a opção **Sim, exportar a chave privada**.

![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779780/image-6.png)  
  
**8.** Marque as opções:

* **Incluir todos os certificados no caminho de certificação, se possível**,
* **Exportar todas as propriedades estendidas**
* **Habilitar privacidade de certificados**.

![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779840/image-7.png)

**9.** Crie uma **senha** para o certificado e anote.   
Essa senha será adicionada na plataforma, anote ela para que você possa inserir a mesma na hora do upload do seu certificado;  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779900/image-8.png)  
  
**10.** Escolha o local e salve o arquivo.  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779860/image-9.png)

**11.** Clique em **concluir**.  
  
![](https://suporte.contabilizei.com.br/hc/article_attachments/360000776119/image-10.png)

**12.** Finalize confirmando e clicando em **OK**.

![](https://suporte.contabilizei.com.br/hc/article_attachments/360000779880/image-11.png)
