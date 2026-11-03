---
article_id: 360059771573
category: MDT - Laudos
content_hash: 35e3d4d405a047aee8ac3ddcc7f67db042c9e008495de6a9f4869747e8aec705
fetched_at: '2026-06-28T22:44:26.356096+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Lista Funcionário
type: support-article
updated_at: '2025-03-03T12:29:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059771573-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Lista-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19672285116055)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Lista Funcionário** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo (**TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.**Atalho**: Lista Funcionário

**Tabelas:**  
SRA - Funcionários  
SRJ - Funções  
  
**Campos:**  
RA\_MAT - Matricula   
RA\_NOME - Nome   
RJ\_FUNCAO - Função  
  
**Vínculos:**  
Em A**tualizações > Cadastros Gerais > Funcionários**. Incluir um funcionário.   
  
Em **Atualizações > Laudos > Laudos.** Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**.  Na aba de Conteúdo Laudo, adicionar o atalho "**LISTA FUNCIONARIOS**"  
  
Exemplo de cadastro: Como incluir um atalho **Lista Funcionário** em um Laudo do tipo PCMSO.  
  
![UEmuHgNa37.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098480174)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
