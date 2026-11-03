---
article_id: 360057710594
category: MDT - Atendimento Médico
content_hash: 51bde4378b723b0fd582234f431ac797572ad7bfa1f08697e04fb40f6adbb8ae
fetched_at: '2026-06-28T22:44:21.394733+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - O que é Banco de Conhecimento e como utilizar para
  gravar arquivos no SIGAMDT
type: support-article
updated_at: '2025-03-12T18:37:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057710594-RH-Linha-Protheus-MDT-O-que-%C3%A9-Banco-de-Conhecimento-e-como-utilizar-para-gravar-arquivos-no-SIGAMDT
---

**Dúvida**O que é **Banco de Conhecimento** e como utilizar para gravar arquivos no modulo Medicina e Segurança do Trabalho (SIGAMDT)?  
  
**Ambiente**TOTVS RH  (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O **Banco de Conhecimento** do **Protheus** é um banco de informações genéricas, armazenadas em arquivos. Essas informações podem ser figuras, textos, planilhas ou qualquer tipo de arquivo que contenha informações relevantes ao Sistema.  
  
Ao incluir um arquivo no **Banco de Conhecimento**, o Sistema cria uma cópia de segurança deste arquivo. Dessa forma, se um arquivo incluído for apagado do seu diretório de origem, o Sistema não sofre alterações.  
  
Para armazenar os arquivos, o Sistema pode criar dois caminhos diferentes, a partir do diretório onde o **Protheus** está instalado. Quando no **SX2** a tabela **AC9**ou **ACB**ou **ACC**estiver compartilhada, ou seja, Sistema com uma única filial, um diretório *Shared*é criado e quando houver mais filiais, é criado um diretório para cada filial.  
  
Exemplo para uma filial:  
**\Protheus\_data\DIRDOC\CO99\SHARED**Exemplo para duas filiais:  
**\Protheus\_data\DIRDOC\CO99\BR01 (Filial 01)**  
**\Protheus\_data\DIRDOC\CO99\BR02 (Filial 02)**Em que:  
**Protheus12** É o diretório onde o **Protheus** está instalado.  
**DIRDOC** É o diretório criado pelo Sistema conforme definido no parâmetro **MV\_DIRDOC**.  
**CO99**  É o diretório que define a empresa para a qual o Sistema funciona onde: **CO - Companhia** e **99 - Código da empresa**.  
  
Glossário de Nomes:  
**MV\_SPLOCDR**- Indica se serão exibidos os drives locais, no banco Conhecimento**MV\_SPLPATH**- Diretório default do banco de conhecimento  
**MV\_DIRDOC**- Diretório destino onde serão armazenados os arquivos  
**AC9**- Relação de Objetos x Entidades  
**ACB** - Bancos de Conhecimentos  
**ACC** - Palavras-Chave  
  
Utilização o **Banco de Conhecimento** no modulo **Medicina e Segurança do Trabalho**  
É possível ver se a rotina que possui a opção de Banco de Conhecimento quando no botão **Outras Ações** existe a opção "**Conhecimento**".  
  
Abaixo vou demonstrar um exemplo de utilização do Banco de Conhecimento na rotina **Funcionários x Epi** (MDTA695) localizado no modulo SIGAMDT (35) o caminho: atualizações > EPI > Funcionários X Epi (MDTA695).  
  
**1.** Clique no botão Outras Ações > Conhecimento;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100155713)  
  
**2.** Clique na consulta (lupa) onde está a grid Objeto e na janela aberta clique em incluir;  
![banco_1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097887774)  
  
**3.** Clique em Outras Ações > **Selecionar Objeto** para incluir o arquivo, depois preencha os campos **descrição** e **palavra chave** disponíveis na tela, e por ultimo confirme.  
![banco_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100156393)  
  
**4.** Na tela anterior clique em abrir para visualizar o arquivo importado e depois salve.

![banco_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097887794)  
  
**Observação**  
A copia do arquivo é gravada na maquina conforme regras e definições de parâmetros explicadas no inicio desse artigo.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100157233)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MP - MDT - Como cadastrar um Equipamento de Proteção Individual (EPI)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048704353-MP-MDT-Como-cadastrar-um-Equipamento-de-Prote%C3%A7%C3%A3o-Individual-EPI-?source=search)
