---
article_id: 1500010075722
category: REQUISIÇÕES
content_hash: 183c753ea089d9f50587ea96e874037efcba4f023504f854f2451778ebc77fae
fetched_at: '2026-06-28T22:44:37.638809+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - MEU RH - Imagem do atestado incluído pelo MEU RH não
  é mostrada no Protheus
type: support-article
updated_at: '2025-09-16T17:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010075722-RH-Linha-Protheus-MEU-RH-Imagem-do-atestado-inclu%C3%ADdo-pelo-MEU-RH-n%C3%A3o-%C3%A9-mostrada-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24768484701719)Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Porque ao incluir uma imagem de atestado através do MEU RH a mesma não é apresentada no Protheus na rotina de "Efetivar Solicitação" (TCFA040)?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015658242)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
 **Solução**As imagens que são atribuídas aos funcionários e participantes, ou as movimentações de atestado médico realizadas por meio do Meu RH, ficam armazenadas no Repositório de Imagens do Protheus.  
  
Quando o sistema está configurado para utilizar o Repositório de Imagens no banco de dados, o correto é que as imagens também sejam armazenadas na tabela PROTHEUS\_REPOSIT e não no arquivo SIGAADV.BMD.  
Para que as imagens sejam tratadas direto no Banco de Dados, na tabela *PROTHEUS\_REPOSIT*, basta criar a chave **RepositInDataBase=1** abaixo dentro da Sessão de Ambiente do arquivo appserver.ini do Servidor de Aplicação que o usuário acessa.  
  
A configuração do Repositório de Imagens deve ser efetuada seguindo a orientação do documento disponibilizado no link:  **<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=271164947>**  
  
Acesse o [**Boletim Técnico**](https://tdn.totvs.com/pages/releaseview.action?pageId=612552445) para mais informações sobre as imagens exibidas no MEU RH  
  
Segue abaixo artigos relacionados:  
**[MP - MEU RH - Como incluir um atestado no MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050895593)**  
**[CLIQUE AQUI e consulte os formatos de arquivo ('.JPG' e etc) suportados pelo Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=492709559)**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
