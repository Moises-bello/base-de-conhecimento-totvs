---
article_id: 1500010730381
category: Evento S-2240
content_hash: 0a7577b7ff13a13cec27c20ca33a7e5ed57ef61a8c4f552adf97a92f7339673f
fetched_at: '2026-06-28T22:45:23.446816+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2240 - Ao executar alguma rotina que
  gera o evento S-2240 é apresentada a mensagem: "Descrição das Atividades Realizadas
  : Em branco"'
type: support-article
updated_at: '2024-11-27T21:30:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010730381-RH-Linha-Protheus-MDT-eSocial-S-2240-Ao-executar-alguma-rotina-que-gera-o-evento-S-2240-%C3%A9-apresentada-a-mensagem-Descri%C3%A7%C3%A3o-das-Atividades-Realizadas-Em-branco
---

**Ocorrência**Ao executar alguma rotina que gera o evento S-2240 é apresentada a mensagem: **"Descrição das Atividades Realizadas : Em branco".** Assunto relacionado ao conteúdo do Parâmetro MV\_NG2TDES **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**  
O Parâmetro **MV\_NG2TDES** está com o conteúdo de alguma rotina onde não foi cadastrada a descrição das atividades.   
  
A descrição das atividades são informações que podem ser cadastradas nas rotinas de Cargo, Função e Tarefas, estando relacionado aos campos **Descrição** (TN5\_DESCRI) ou **Nome Tarefa** (TN5\_NOMTAR), **Ds. Detalhada** (Q3\_MEMO1) ou **Desc. Sumaria** (Q3\_DESCSUM), **Requisitos** (RJ\_MEMOREQ) ou **Descrição** (RJ\_DESC). Para geração do evento **S-2240** o sistema verifica o conteúdo do parâmetro **MV\_NG2TDES** saber de qual rotina deve ser gerada a descrição.  
  
**Solução**Para ajuste siga as orientações abaixo:  
  
1. No módulo Configurador, acesse o menu **Ambiente > Cadastros > Parâmetros**e filtre o parâmetro **MV\_NG2TDES** (Indica qual descrição pegar e considerar na rotina de Condições Ambientais de Trabalho no TAF. 1= Tarefa; 2= Cargo; 3= Função; 4= Cargo + Tarefa). E escolha entre uma das opções disponíveis.  
  
2. O sistema vai gerar a descrição das atividades no S-2240 conforme a opção selecionada no parâmetro. Abaixo um exemplo de cada opção e de onde o sistema vai buscas a informação.  
  
 **1 - Tarefa:** O sistema vai buscar informações no Módulo 35 (SIGAMDT) no caminho: Atualizações > PPRA > **Tarefa Por Func.** (MDTA090) nos campos **Descrição** (TN5\_DESCRI) ou **Nome Tarefa** (TN5\_NOMTAR).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119717318423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119702373911)  
 **2 -** **Cargo:** O sistema vai buscar informações no Módulo 35 (SIGAMDT) no caminho: Atualizações > Cadastros Gerais > **Cargos** (GPEA370) nos campos **Ds. Detalhada** (Q3\_MEMO1) ou **Desc. Sumaria** (Q3\_DESCSUM).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119717325847)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119702378519)

**3 - Função:** O sistema vai buscar informações no Módulo 35 (SIGAMDT) no caminho: Atualizações > Cadastros Gerais > **Funções** (GPEA030) nos campos **Requisitos** (RJ\_MEMOREQ) ou **Descrição** (RJ\_DESC).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119717328535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28119702387095)  
 **4 - Cargo + Tarefa:** O sistema vai buscar informações dos cadastros do item 1 e 2 mencionados acima.  
  
Consulte exemplos de preenchimento dos campos citados acima no artigo[RH - Linha Protheus - MDT - eSocial - S-2240 - Como é buscada a informação de descrição das atividades realizadas (tag <dscAtivDes>) no evento S-2240](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407771559575)  
**Observações**

* Para acessar a documentação dos eventos SST (Medicina e Segurança do Trabalho) acesse o link: **[Eventos Não Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=390398468)**. Clique no evento desejado e verifique as abas Conceito, Premissas, Como Gerar.
* Para acessar o documento de De/Para de campos dos eventos SST (Medicina e Segurança do Trabalho) acesse o link: **[Correspondência Layouts eSocial x Protheus (SST)](https://tdn.totvs.com/pages/viewpage.action?pageId=344457675)**. Clique no evento desejado e veja os campos do Medicina e TAF utilizados em cada evento.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
