---
article_id: 360040697714
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6c4cb5d1ffa9078185d7dcab656414c71f5e52b49be1e8c594ba13ca1e73b563
fetched_at: '2026-06-28T22:42:32.787394+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atualização do Manutenção de Ativos e Gestão
  de Frotas
type: support-article
updated_at: '2025-06-16T11:47:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040697714-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-do-Manuten%C3%A7%C3%A3o-de-Ativos-e-Gest%C3%A3o-de-Frotas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura:**00:01:30 min****Dúvida**Como manter o **Manutenção de Ativos** e **Gestão de Frotas**atualizado?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Com o objetivo de manter o módulo **Manutenção de Ativos - SIGAMNT** sempre atualizado sem a necessidade de substituir o repositório de dados, no portal do cliente é disponibilizado semanalmente um pacote com os arquivos *dots*,*htms*,*http*,*contents* e *ptm*do **SIGAMNT**.

* Para baixar o pacote, basta acessar a documentação [Pacotes de Atualização - Manutenção de Ativos](https://tdn.totvs.com/x/MSsdHw) e identificar a versão e o idioma de acordo com seu ambiente.
* Ao identificar o pacote correto para atualização do módulo, **clicar** sobre o mesmo e realizar o *download* selecionando a opção **Fazer o download do arquivo**;
* Após baixar e descompactar o mesmo, é possível verificar que, além do**.ptm**e do arquivo de**contents**, o qual cita todos os fontes do *patch*, também há três arquivos que são:

1) **Dots.zip**:Contém os arquivos a serem atualizados na pasta *sample*que está parametrizada em**MV\_DIRACA** **- Path onde serão gravados os arquivos DOT na estação de trabalho**.   
Exemplo: **\\TOTVS\Protheus\protheus\_data\samples\documents\ng\**;  
2) **http.zip**:Contém os arquivos a serem atualizados da pasta **http**;  
3) **htms.zip**: Contém os arquivos a serem atualizados na pasta *workflow*que está parametrizada em**MV\_WFDIR - Diretório de trabalho do Workflow.****Importante**É imprescindível realizar *backup* do repositório de dados no *SourcePath* antes de prosseguir com a atualização.
