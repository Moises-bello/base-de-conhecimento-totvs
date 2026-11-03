---
article_id: 12101369434647
category: Gestão Ambiental (SIGASGA)
content_hash: 9ab8bf09c081c607d06d0c5ea4164b73171e6297799c0de54414e8292ea40293
fetched_at: '2026-06-28T22:42:38.431593+00:00'
product: protheus
section_id: 360012117893
source: central-protheus
title: Manufatura - Linha Protheus - SGA - Atualização do Gestão Ambiental
type: support-article
updated_at: '2023-02-01T19:03:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12101369434647-Manufatura-Linha-Protheus-SGA-Atualiza%C3%A7%C3%A3o-do-Gest%C3%A3o-Ambiental
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)Tempo aproximado para leitura: **00:01:53 min** **Dúvida**Como manter o **Gestão Ambiental** atualizado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Gestão Ambiental (SIGASGA) – Versão 12

**Solução**

Com o objetivo de manter o módulo **Gestão Ambiental - SIGASGA** sempre atualizado sem a necessidade de substituir o repositório de dados, no portal do cliente é disponibilizado semanalmente um pacote com os arquivos *dots*, *htms*, *http*, *contents* e *ptm*do **SIGASGA**.

* Para baixar o pacote, basta acessar a documentação [Pacotes de Atualização - Gestão Ambiental](https://tdn.totvs.com/pages/releaseview.action?pageId=525026837) e identificar a versão e o idioma de acordo com seu ambiente.
* Ao identificar o pacote correto para atualização do módulo, **clicar** sobre o mesmo e realizar o *download* selecionando a opção **Fazer o download do arquivo**;
* Após baixar e descompactar o mesmo, é possível verificar que, além do**.ptm**e do arquivo de**contents**, o qual cita todos os fontes do *patch*, também há três arquivos que são:

1) **Dots.zip**:Contém os arquivos a serem atualizados na pasta *sample*que está parametrizada em **MV\_DIRACA****- Path onde serão gravados os arquivos DOT na estação de trabalho**.  
Exemplo:**\\TOTVS\Protheus\protheus\_data\samples\documents\ng\**;  
2) **http.zip**:Contém os arquivos a serem atualizados da pasta **http**;  
3) **htms.zip**: Contém os arquivos a serem atualizados na pasta *workflow*que está parametrizada em **MV\_WFDIR - Diretório de trabalho do Workflow.****Importante**É imprescindível realizar *backup* do repositório de dados no *SourcePath* antes de prosseguir com a atualização.
