---
article_id: 27443210050199
category: TAF - eSocial - Atualização
content_hash: 7573b182c9df033137779eefe510e9d6fcef1cdd3e1247cc9712ca462240f015
fetched_at: '2026-06-28T22:45:13.265636+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - ATUALIZAÇÃO - Erro no migrador "Valor inválido
  para o parâmetro name."
type: support-article
updated_at: '2026-06-23T20:42:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27443210050199-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Erro-no-migrador-Valor-inv%C3%A1lido-para-o-par%C3%A2metro-name
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27443530523799) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Erro no migrador do TAF : "Valor inválido para o parâmetro name."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443558317719)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões  
  
**Solução**

O erro é apresentado quando existe algum serviço da estrutura do TAF instalado no **serviço do Windows** fora da **pasta raiz de instalação do TAF**, por exemplo, o serviço do appserver ou do DBAccess.

Vamos apresentar um exemplo:

1. Caminho incorreto do DBAccess, ocasiona o erro abaixo no migrador do TAF:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443530537239)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443558329495)

1.1 Como corrigir:

O serviço deve ser instalado no caminho correto, ou seja, na estrutura de instalação do TAF.

A) Primeiro, deve remover o serviço do DBAccess do Windows, pode ser utilizado o comando:

**SC DELETE + (nome do serviço)** via **DOS** para remove-lo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443558332695)

B) Após remoção, abra a pasta **DBAccess** localizada dentro da pasta **TAF:**

**Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443558335767)**

C) Encontre o arquivo dbaccess.exe, clique com o botão direito do mouse, e escolha a opção criar atalho, para ser criado um atalho do Dbaccess.exe.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443530559255)**

D) Após criar o atalho, clique com o botão direito do mouse vá em **propriedades** do atalho, no box destino, após o .exe,  de um espaço, e digite -install,

Exemplo:

C:\TOTVS\_ORA19\TAF\TafDbAccess64\dbaccess64.exe **–install**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27443530561559)**

E) Execute o atalho **como administrador,** para que o serviço seja criado novamente.

**\*\*Importante!**

Após o serviço ser criado,  compare o arquivos **dbaccess.ini** com o existente no **antigo** **dbaccess (o que estava no caminho errado),** eles precisam ser iguais!

Ou seja, o arquivo **dbaccess.ini** desse novo dbaccess deve ser igual ao arquivo **dbaccess.ini** do antigo, que estava fora na pasta do TAF.

F) Abra o arquivo **dbaccess.ini** para edição e adicione o seguinte comando, salve a alteração:

```
[SERVICE]  
NAME=Taf-DbAccess64  
DISPLAYNAME=Taf-DbAccess64
```

G) O novo serviço criado, ficará com a configuração abaixo:

Atente-se para deixar o **Tipo de inicialização** como: **Automático**

**![image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVSa%2B6XuazKRsBAeFIIuVXDgp%2F4%2F2OE8kp6hMnkCdYlV7inOE%2BDLQ5t5UEh9I9pxQUn8TVzVgInDoTa23Ha2MgECJUMAlZaSUC7D44AjgGHgi1ZGX%2FDIYffWnRlceb84%2BYrGLvm%2FzkSmVMNkjEHOxiH96UFjOQvz8cpKAphy5De1hpqvV1nD4DP%2F5QXavsaoz1fjhTouXV6bdanDP7Z%2F7xUZdSAOG1TkZ2GFzEuK6Op2AQfM2eT9BdRymMm0MxqvMwM%2FiFUuTRdFFDfFERWCL20NI1QwHuuk4u9lsGZROSOA%2FVc1OPOsGy%2FSu2mnV9XeFkrXlNzm4ey1ifhUbUmKj8wi3GUI0SBwkulBNiIYQ6T32slo371wKRUfrZ6Yf9z06%2B3enptAYybk%2Bim4bsFCb2HM70PV22ZErtwkhqnT%2BFPHmvlNy3G0tQz0znfeykXLVVeMAhn9KZkM41a9UEHqOGaMHBlUYDGe35Yc%2FGcsi5ILp%2F4OxB5mr5scTrc7E9G%2Frgh02z2jDXSZuU1JpEOaWCZ2Ld4VO%2B3XpRywTxTaxzyRReFkCHaAcT5rYya&sz=w512)**

**Saiba Mais**Para saber mais consulte os links abaixo:   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
