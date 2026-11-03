---
article_id: 360059466773
category: Portal de Gestão de Capital Humano
content_hash: 051a96ab80968fe3800204dfbb594b487be7bd89e430973dad77fe1dce3bb56f
fetched_at: '2026-06-28T22:43:00.076636+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Local de gravação dos dados do banco de
  conhecimento
type: support-article
updated_at: '2021-04-07T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059466773-RH-Linha-Protheus-PORTAL-GCH-Local-de-grava%C3%A7%C3%A3o-dos-dados-do-banco-de-conhecimento
---

**Dúvida**Onde é gravado os dados do banco de conhecimento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Capital Humanos – A partir da versão 12..1.17  
  
**Solução**O **Banco de Conhecimento** do **Protheus** é um banco de informações genéricas, armazenadas em arquivos. Essas informações podem ser figuras, textos, planilhas ou qualquer tipo de arquivo que contenha informações relevantes ao Sistema.  
  
Ao incluir um arquivo no **Banco de Conhecimento**, o Sistema cria uma cópia de segurança deste arquivo. Dessa forma, se um arquivo incluído for apagado do seu diretório de origem, o Sistema não sofre alterações.  
  
Para armazenar os arquivos, o Sistema pode criar dois caminhos diferentes, a partir do diretório onde o **Protheus** está instalado. Quando no **SX2** a tabela **AC9**ou **ACB**ou **ACC**estiver compartilhada, ou seja, Sistema com uma única filial, um diretório *Shared*é criado e quando houver mais filiais, é criado um diretório para cada filial.  
  
Exemplo para uma filial:  
**\Protheus12\DIRDOC\CO99\SHARED**Exemplo para duas filiais:  
**\Protheus12\DIRDOC\CO99\BR01 (Filial 01)**  
**\Protheus12\DIRDOC\CO99\BR02 (Filial 02)**Em que:  
**Protheus12** – Diretório onde o **Protheus** está instalado.  
**DIRDOC** – Diretório criado pelo Sistema conforme definido no parâmetro **MV\_DIRDOC**.  
**CO99** – Diretório que define a empresa para a qual o Sistema funciona onde: **CO - Companhia** e **99 - Código da empresa**.  
  
**Glossário**  
**MV\_SPLOCDR**- Indica se serão exibidos os drives locais, no banco Conhecimento**MV\_SPLPATH**- Diretório default do banco de conhecimento  
**MV\_DIRDOC**- Diretório destino onde serão armazenados os arquivos  
**AC9**- Relação de Objetos x Entidades  
**ACB** - Bancos de Conhecimentos  
**ACC** - Palavras-Chave
