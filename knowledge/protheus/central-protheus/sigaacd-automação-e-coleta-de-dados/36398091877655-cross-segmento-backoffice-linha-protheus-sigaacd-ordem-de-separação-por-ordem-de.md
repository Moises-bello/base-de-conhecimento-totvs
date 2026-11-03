---
article_id: 36398091877655
category: SIGAACD - Automação e Coleta de Dados
content_hash: 0620876ada8a8f7ce30bc702b4bf9676a27cec955256c02b2eeb95ed965f22fc
fetched_at: '2026-06-28T22:39:12.916007+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ordem de Separação
  por Ordem de Produção para produtos sem empenho com o lote em branco.
type: support-article
updated_at: '2025-11-17T21:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36398091877655-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ordem-de-Separa%C3%A7%C3%A3o-por-Ordem-de-Produ%C3%A7%C3%A3o-para-produtos-sem-empenho-com-o-lote-em-branco
---

O artigo explica como gerar uma Ordem de Separação por Ordem de Produção sem empenho na SD4 e sem informar o lote, detalhando a criação dos campos CB8\_LOTORI e CB9\_LOTORI no Configurador do Protheus.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36398091863319) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar uma Ordem de Separação, por Ordem de Produção sem empenho na SD4, sem informar o lote na geração da Ordem de Separação.   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Tópicos importantes para geração da Ordem de Separação, por Ordem de Produção sem empenho e com o lote em branco na CB8 e na CB9.

**Criação de novo campo**

1) Acessar o ambiente do Configurador(SIGACFG) no Protheus.

2) Acessar: Base de Dados -> Dicionário -> Bases de Dados

3) Expandir as opções do menu: Empresa Grupo

4) Selecionar a opção: Dicionário de Dados

5) Pesquisar pela tabela Produtos Separados: CB8

6) Clicar no ícone de Editar: ![](https://tdn.totvs.com/download/thumbnails/889121180/image-2025-1-27_15-40-56.png?version=1&modificationDate=1738003256853&api=v2)

7) Expandir a opção de Produtos Separados e selecionar o item Campos

7) Clicar no ícone de Novo: ![](https://tdn.totvs.com/download/thumbnails/889121180/image-2025-1-27_15-44-40.png?version=1&modificationDate=1738003480633&api=v2)

8) Na tela Gerenciador de Base de Dados informar as seguintes informações:  
**Aba Campo:**  
- Campo: **CB8\_LOTORI**  
- Tipo: 1-Caracter  
- Tamanho: 10  
- Contexto: Real  
- Propriedade: Visualizar

**Aba Informações:**  
- Tit. Português: Lote Origem  
- Tit. Espanhol: Origen lote   
- Tit. Inglês: Lot Origin  
- Desc. Português: Lote Origem  
- Desc. Espanhol: Origen lote   
- Desc. Inglês: Lot Origin  
- Help: Lote de origem do produto separado.

**Aba Uso:**  
- Usado: Sim  
- Clicar em Salvar

9) Pesquisar pela tabela Produtos Separados: CB9

10) Clicar no ícone de Editar: ![](https://tdn.totvs.com/download/thumbnails/889121180/image-2025-1-27_15-40-56.png?version=1&modificationDate=1738003256853&api=v2)

11) Expandir a opção de Produtos Separados e selecionar o item Campos

12) Clicar no ícone de Novo: ![](https://tdn.totvs.com/download/thumbnails/889121180/image-2025-1-27_15-44-40.png?version=1&modificationDate=1738003480633&api=v2)

13) Na tela Gerenciador de Base de Dados informar as seguintes informações:  
Aba Campo:  
- Campo: **CB9\_LOTORI**  
- Tipo: 1-Caracter  
- Tamanho: 10  
- Contexto: Real  
- Propriedade: Visualizar

**Aba Informações:**  
- Tit. Português: Lote Origem  
- Tit. Espanhol: Origen lote   
- Tit. Inglês: Lot Origin  
- Desc. Português: Lote Origem  
- Desc. Espanhol: Origen lote   
- Desc. Inglês: Lot Origin  
- Help: Lote de origem do produto separado.

**Aba Uso:**  
- Usado: Sim- Clicar em Salvar

14) Clicar no ícone Sair: ![](https://tdn.totvs.com/download/thumbnails/889121180/image-2025-1-27_16-13-58.png?version=1&modificationDate=1738005238960&api=v2)

Esses campos será criado automaticamente no [Expedição Continua do BackOffice](https://suporte.totvs.com/portal/p/10098/download#detail/1039095).  Mas sempre certifique se os campos estão criados no ambiente CB9\_LOTORI e o CB8\_LOTORI.

Na rotina de Ordem de Produção(MATA650) deixar o parâmetro F12 dessa forma:   
Sugere Lote/End a Empenhar ? **Não**  
Mostra Tela Alt. de Empenhos ? **Sim**

Na rotina Ordem de Separação(ACDA100) deixar o F12 dessa forma: 

O pergunte "Confere Lote? = NÃO" 

**Sobre  o Fluxo do processo avaliar  o boletim na opção Exemplo de utilização "Ordem de Separação para uma Ordem de Produção para produtos sem empenho".**

[Ordem de Separação(ACDA100) para Ordem de Produção | Troca de Lote](https://tdn.totvs.com/pages/releaseview.action?pageId=889121180)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
