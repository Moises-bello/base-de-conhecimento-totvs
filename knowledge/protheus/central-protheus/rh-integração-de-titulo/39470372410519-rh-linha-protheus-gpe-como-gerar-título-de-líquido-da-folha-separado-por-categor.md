---
article_id: 39470372410519
category: RH - Integração de Titulo
content_hash: e35127b22622482294119a01b55d8c94bde8432ca162b2be3893c1d036c7e04c
fetched_at: '2026-06-28T22:43:36.525376+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como Gerar Título de Líquido da Folha Separado
  por Categoria do Funcionário
type: support-article
updated_at: '2026-04-03T12:59:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39470372410519-RH-Linha-Protheus-GPE-Como-Gerar-T%C3%ADtulo-de-L%C3%ADquido-da-Folha-Separado-por-Categoria-do-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39470372387863) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como Gerar Título de líquido da Folha de Pagamento, Separado por Categoria do Funcionário?   
  
**Ambiente**  
TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as Versões  
  
**Solução**

Como a verba de Líquido da Folha (ID de Cálculo 0047) é única, independentemente da categoria (funcionários com contrato determinado ou indeterminado, pró-labore, autônomos ou estagiários), a geração de títulos segregados por categoria exige a criação de uma Definição de Título específica para cada uma.   
Para isso, deve-se utilizar o filtro SRA, permitindo a distinção das categorias em cada definição.  
  
Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse: Miscelanea / Títulos / Definição (GPEM640), Clique em **Incluir** e selecione a opção **Definido por Usuário** e em seguida clique em **Definir Título**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39470343919255)

2. Inclua a Verba de Líquido em **Verbas Selecionadas para Geração** e em seguida clique na opção **Filtro para o Cadastro de Funcionário SRA**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39470372389143)   
3. Pra cada Definição de Título, crie a Expressão de Filtro por Categoria do Funcionário, no exemplo abaixo, foi inserida a caegoria "A", para Atônomos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39470343921431)

As categorias disponíveis são:

A - Autônomo  
C - Comissionado  
D - Diarista  
E - Estagiário Mensalista  
G - Estagiario Horista  
H - Horista  
I - Professor Mensalista  
J - Professor Aulista  
M - Mensalista  
P - Pro-Labore  
S - Semanalista  
T - Tarefeiro  
  
4. Salve a Definição do Título, e Prossiga com a Geração.

**Saiba Mais:**

[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
