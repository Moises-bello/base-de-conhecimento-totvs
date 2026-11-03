---
article_id: 360028969891
category: Atualização
content_hash: d4be0f151798aa55ed0d8bded7ff4faa0f6753b7aac7dbed04d87f32cb748164
fetched_at: '2026-06-28T22:42:21.328512+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - FRAME - Atualização de Help
type: support-article
updated_at: '2023-10-24T18:10:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028969891-Framework-Linha-Protheus-FRAME-Atualiza%C3%A7%C3%A3o-de-Help
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15771557385111)*** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como posso atualizar os *Helps* do meu ambiente?  
  
**Ambiente**Framework - Framework (Linha Protheus) - AppServer - Todas as versões.  
  
**Solução**Segue abaixo procedimento para atualizar ou recriar os *Helps* de Campos do **Protheus**:  
  
Primeiramente faça o *download* do arquivo.  
  
1. Portal do Cliente: <http://suporte.totvs.com>;  
2. Menu **Downloads** e **Atualizações**;  
3. Linha **Protheus**;  
4. **Microsiga Protheus** Versão 12.1.XX, onde XX é a Release do seu P12;  
5. Todos;  
6. Categoria: *Help* de campo/pergunta;  
7. Baixe os arquivos: *HELPS* DE CAMPOS/PERGUNTAS COMPLETO - BRASIL.  
  
Se não estiverem aparecendo as versões, em **Filtros de pacotes** selecione **Todos pacotes disponíveis** e selecione a categoria novamente.  
  
Após baixar o pacote, descompacte os arquivos **.txt** para dentro da pasta **Systemload** do **Protheus**.  
  
Para atualizar, pare o serviço do **Protheus**, acesse a pasta **System** e:  
- Para o *help* de campos em português, apague o arquivo **sigahlp.hlp**.  
- Para o *help* de campos em inglês, apague o arquivo **sigahle.hle**.  
- Para o help de campos em espanhol, apague o arquivo **sigahls.hls**.  
  
Reinicie o serviço do **Protheus**. Ao acessar o Sistema, o *help* será recriado a partir do **.txt** descompactado. Uma imagem de alerta será exibida durante a atualização dos arquivos:

![Help_Campos.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029786352)

**Importante**  
Se a sua base já estiver com **Dicionário de Dados** no **Banco de Dado**s, deverá atualizar diretamente pelo Menu do **Configurador**, após baixar os arquivos e salvar na pasta **Systemload**:  
  
1. Acesse o **Configurador**  
2. Menu **Ambiente** > **Help** > **Atualização do Help**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15771541142679)**
