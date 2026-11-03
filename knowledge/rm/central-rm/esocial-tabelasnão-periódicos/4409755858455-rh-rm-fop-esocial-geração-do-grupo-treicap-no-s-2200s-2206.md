---
article_id: 4409755858455
category: eSocial - Tabelas/Não Periódicos
content_hash: e7ad37bc03a355f65e72e5176996021d40827eed6a1bd45294e207c873a81a6c
fetched_at: '2026-06-28T22:47:10.471992+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Geração do grupo treiCap no S-2200/S-2206
type: support-article
updated_at: '2024-11-05T12:24:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409755858455-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-grupo-treiCap-no-S-2200-S-2206
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845560727) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar o grupo **treiCap** (antigo S-2245) no S-2200/S-2206 do leiaute **S-1.0**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos patches 12.1.31.199, 12.1.32.136 e 12.1.33  
  
**Solução**O grupo **treiCap**refere-se a treinamentos, capacitações, exercícios e outras anotações. No leiaute 2.5, as informações eram enviadas através do evento S-2245 (evento excluído no S-1.0). 

Conforme o mapeamento dos eventos eSocial, o grupo **treiCap**será gerado conforme dados indicados na tabela **VCURSOS**(TOTVS Gestão de Pessoas).

![](https://totvssuporte.zendesk.com/attachments/token/mvvTMyXQlYv2qxeyocPEgozEa/?name=inline-1096289050.png)

![](https://totvssuporte.zendesk.com/attachments/token/n4ZhGxln6FuwsSyuqIOf02O46/?name=inline-535343338.png)

As informações dos cursos/capacitações são oriundas do módulo TOTVS Gestão de Pessoas e, apesar de ser gerado no XML do eSocial apenas o código do curso eSocial, é importante que o **registro completo** seja realizado no Módulo para o caso de uma eventual **fiscalização**.

Para as devidas configurações, siga os passos abaixo:

1. No TOTVS Gestão de Pessoas, acesse o menu **Desenvolvimento | Cursos**;  
1.1. Cadastre o curso desejado e marque o parâmetro **Curso eSocial**, preenchendo também os demais campos que serão exibidos;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845581079)

2. Ainda no Gestão de Pessoas, acesse o menu **Desenvolvimento | Turmas**;  
2.1. Cadastre a **Turma** informando no campo **Curso**, o curso criado na etapa 1.1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845591319)

2.2. Acesse **Anexos | Participantes** e cadastre o funcionário que irá realizar o curso na turma que está editando;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208797201431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208797210775)

2.3. Na **Turma** acesse **Anexos | Avaliação de Conhecimento** e informe o percentual de aproveitamento do Participante em **Anexos | Avaliados;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208797223063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845646103)

2.4. Após, encerre a **Avaliação de Conhecimento**acessando **Turma | Anexos | Fechar Avaliação de Conhecimento;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845659031)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845666071)

2.5. Por último, encerre a **Turma**em **Processos | Encerramento da Turma**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208845679127)**

3. Com a **turma encerrada**, acesse o **TOTVS Folha de Pagamento** **| Eventos Não Periódicos** e identifique o gatilho S-2200 ou S-2206 do funcionário desejado. Após gerar o XML verifique se a tag **treiCap** foi preenchida conforme o código do treinamento eSocial preenchido no curso.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22208893891095)

**Saiba mais**  
Para mais informações, acesse:  
     - [Alterações S-2200](https://tdn.totvs.com/pages/releaseview.action?pageId=599378929)  
     - [Leiaute Versão S-1.0](https://tdn.totvs.com/pages/releaseview.action?pageId=578383565)  
     - [Cursos - RHU](https://tdn.totvs.com.br/display/public/LRM/Cursos+-+RHU)  
     - [Turmas - RHU](https://tdn.totvs.com.br/display/public/LRM/Turmas+-+RHU)  
     - [eSocial - Eventos S-2200 e S-2206 - Geração da tag <treiCap>](https://tdn.totvs.com/pages/releaseview.action?pageId=732687383)
