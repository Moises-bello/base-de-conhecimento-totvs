---
article_id: 360037744193
category: Integrações Nativas
content_hash: 8f2e5eda65bba458a003a5763ade80040230acc45dc1e1407d5c5684bee0b5b1
fetched_at: '2026-06-28T22:42:35.529664+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Relação dos cadastros de funcionário do
  Manutenção de Ativos, Funcionários - GPEA010 e Funcionários - MNTA020
type: support-article
updated_at: '2021-07-29T21:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037744193-Manufatura-Linha-Protheus-MNT-Rela%C3%A7%C3%A3o-dos-cadastros-de-funcion%C3%A1rio-do-Manuten%C3%A7%C3%A3o-de-Ativos-Funcion%C3%A1rios-GPEA010-e-Funcion%C3%A1rios-MNTA020
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min****Dúvida**Qual a relação dos cadastros de funcionário do **Manutenção de Ativos**, **Funcionários - GPEA010**e **Funcionários - MNTA020**?**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**A **rotina Funcionários - GPEA010** tem a função de cadastrar os funcionários da empresa, e a rotina **Funcionários - MNTA020** fica responsável por complementar o cadastro agregando informações necessárias do próprio módulo ou incluir um novo cadastro de um funcionário que será destinado as **atividades** do **Manutenção de Ativos**.Na **MNTA020**, deve ser realizado o cadastramento dos funcionários que serão utilizados nos serviços de **manutenção** da empresa. Será necessário informar pelo menos uma **especialidade** do funcionário. Quando houver a execução de **plano** de **manutenção**, os funcionários serão selecionados conforme o **turno** de trabalho e a **especialidade** requerida pela tarefa de **manutenção**.  
  
Se o parâmetro **MV\_NGMNTRH** - **Integração Manutenção (MNT) com Recursos Humanos** estiver como **S**, os dados comuns ao cadastro de **funcionário da folha** de pagamento e a tabela de funcionários de manutenção serão atualizados automaticamente. Já campo **Turno** deve ser preenchido manualmente pelo usuário.  
  
**Saiba mais**  
Para informações complementares do cadastro de funcionários da manutenção, verifique o *link* [Funcionários (MNTA020 - SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=506389105)
