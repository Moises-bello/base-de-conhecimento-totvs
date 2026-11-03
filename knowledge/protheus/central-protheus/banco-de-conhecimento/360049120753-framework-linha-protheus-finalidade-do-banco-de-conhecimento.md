---
article_id: 360049120753
category: Banco de Conhecimento
content_hash: 8b679b4313aac5d4d08c3d66cca4dba6409011a9ae86b4f52ef1ad70b90ae74e
fetched_at: '2026-06-28T22:42:16.360063+00:00'
product: protheus
section_id: 360008038474
source: central-protheus
title: Framework - Linha Protheus  - Finalidade do Banco de Conhecimento
type: support-article
updated_at: '2025-12-08T20:53:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049120753-Framework-Linha-Protheus-Finalidade-do-Banco-de-Conhecimento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23336790238359)***Tempo aproximado para leitura: **00:01:30 min**  
 **Dúvida**Qual a a finalidade do **Banco de Conhecimento**?  
   
 **Ambiente**Microsiga Protheus – Banco de Conhecimento – Versão 12  
  
**Solução**O **Banco de Conhecimento** do **Protheus** é um banco de informações genéricas, armazenadas em arquivos. Essas informações podem ser figuras, textos, planilhas ou qualquer tipo de arquivo que contenha informações relevantes ao Sistema.  
Ao incluir um arquivo no **Banco de Conhecimento**, o Sistema cria uma cópia de segurança deste arquivo. Dessa forma, se um arquivo incluído for apagado do seu diretório de origem, o Sistema não sofre alterações.  
Para armazenar os arquivos, o Sistema pode criar dois caminhos diferentes, a partir do diretório onde o **Protheus** está instalado. Quando no **SX2** a tabela **AC9** ou **ACB** ou **ACC** estiver compartilhada, ou seja, Sistema com uma única filial, um diretório *Shared*é criado e quando houver mais filiais, é criado um diretório para cada filial.  
Exemplo para uma filial:  
**\Protheus12\DIRDOC\CO99\SHARED**Exemplo para duas filiais:  
**\Protheus12\DIRDOC\CO99\BR01 (Filial 01)**  
**\Protheus12\DIRDOC\CO99\BR02 (Filial 02)**Em que:  
**Protheus12** – Diretório onde o **Protheus** está instalado.  
**DIRDOC** – Diretório criado pelo Sistema conforme definido no parâmetro **MV\_DIRDOC**.  
**CO99** – Diretório que define a empresa para a qual o Sistema funciona onde: **CO - Companhia** e **99 - Código da empresa**.  
  
**Glossário**  
**MV\_SPLOCDR** - Indica se serão exibidos os drives locais, no banco Conhecimento**MV\_SPLPATH** - Diretório default do banco de conhecimento  
**MV\_DIRDOC** - Diretório destino onde serão armazenados os arquivos  
**AC9** - Relação de Objetos x Entidades  
**ACB** - Bancos de Conhecimentos  
**ACC** - Palavras-Chave
